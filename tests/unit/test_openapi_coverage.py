"""Coverage for core infrastructure: OpenApiBase token/sign/request logic and AuthManager.

These tests exercise the real OpenApiBase state machine (token caching/refresh, request
signing, rate-limit integration) and AuthManager (token lifecycle with retry/backoff),
without hitting the network. aiohttp sessions and HttpBase are faked/patched.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from lingxing.core.auth import AuthManager  # noqa: E402
from lingxing.core.openapi import OpenApiBase  # noqa: E402
from lingxing.core.resp_schema import AccessTokenDto, ResponseResult  # noqa: E402

# ── helpers ──────────────────────────────────────────────────────────────────


def _no_op_rate_limiter() -> MagicMock:
    """A rate limiter stub whose wait_if_needed() always returns 0 (no sleeping)."""
    limiter = MagicMock()
    limiter.wait_if_needed = AsyncMock(return_value=0)
    return limiter


def _make_api(host: str = "https://openapi.test", threshold: int = 300) -> OpenApiBase:
    api = OpenApiBase(host=host, app_id="app_id_x", app_secret="app_secret_y", token_refresh_threshold=threshold)
    api._rate_limiter = _no_op_rate_limiter()
    return api


def _store_token(api: OpenApiBase, expires_in: int = 7200, access: str = "AT", refresh: str = "RT") -> None:
    api._store_token(AccessTokenDto(access_token=access, refresh_token=refresh, expires_in=expires_in))


class _FakeResp:
    """Async context manager mimicking an aiohttp response."""

    def __init__(self, status: int = 200, payload: dict | None = None, text: str = ""):
        self.status = status
        self._payload = payload if payload is not None else {}
        self._text = text

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        return False

    async def json(self):
        return self._payload

    async def text(self):
        return self._text


class _FakeSession:
    """Async context manager mimicking aiohttp.ClientSession (only .post used)."""

    def __init__(self, resp: _FakeResp):
        self._resp = resp

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc):
        return False

    def post(self, *args, **kwargs):
        return self._resp


def _patch_session(monkeypatch, resp: _FakeResp):
    """Patch aiohttp.ClientSession so every call returns a session yielding `resp`."""
    import aiohttp

    monkeypatch.setattr(aiohttp, "ClientSession", lambda *a, **kw: _FakeSession(resp))


# ── OpenApiBase: token state properties ──────────────────────────────────────


class TestTokenState:
    def test_no_token_is_invalid_and_needs_refresh(self):
        api = _make_api()
        assert api.has_valid_token is False
        assert api.cached_access_token is None
        assert api.token_expires_in_seconds is None
        assert api._should_refresh_token() is True

    def test_fresh_token_is_valid_and_not_refreshed(self):
        api = _make_api()
        _store_token(api, expires_in=7200)
        assert api.has_valid_token is True
        assert api.cached_access_token == "AT"
        # well above the 300s threshold
        assert api.token_expires_in_seconds > 7000
        assert api._should_refresh_token() is False

    def test_token_near_expiry_triggers_refresh(self):
        api = _make_api(threshold=300)
        # Expires in 100s -> within 300s window -> should refresh
        _store_token(api, expires_in=100)
        assert api.has_valid_token is True
        assert api._should_refresh_token() is True
        # remaining seconds clamped lower bound behavior: ~100s
        assert api.token_expires_in_seconds <= 100

    def test_token_expires_in_seconds_clamped_to_zero(self):
        api = _make_api()
        # Force expiry into the past
        api._access_token = "AT"
        api._token_expires_at = datetime.now() - timedelta(seconds=10)
        assert api.has_valid_token is False
        assert api.token_expires_in_seconds == 0

    def test_store_token_resets_refresh_attempts(self):
        api = _make_api()
        api._token_refresh_attempts = 5
        _store_token(api)
        assert api._token_refresh_attempts == 0


# ── OpenApiBase: get_valid_token state machine ───────────────────────────────


class TestGetValidToken:
    async def test_no_token_fetches_new(self):
        api = _make_api()
        api._do_generate_access_token = AsyncMock(
            return_value=AccessTokenDto(access_token="NEW", refresh_token="NR", expires_in=7200)
        )
        token = await api.get_valid_token()
        assert token == "NEW"
        api._do_generate_access_token.assert_awaited_once()
        # generated DTO carried a refresh token which must be cached
        assert api._refresh_token == "NR"

    async def test_valid_cached_token_no_network(self):
        api = _make_api()
        _store_token(api, expires_in=7200)
        api._do_generate_access_token = AsyncMock()
        api._do_refresh_token = AsyncMock()
        token = await api.get_valid_token()
        assert token == "AT"
        api._do_generate_access_token.assert_not_awaited()
        api._do_refresh_token.assert_not_awaited()

    async def test_expired_with_refresh_token_uses_refresh(self):
        api = _make_api()
        _store_token(api, expires_in=100)  # expired-ish -> within threshold
        api._do_refresh_token = AsyncMock(
            return_value=AccessTokenDto(access_token="REFRESHED", refresh_token="NR", expires_in=7200)
        )
        api._do_generate_access_token = AsyncMock()
        token = await api.get_valid_token()
        assert token == "REFRESHED"
        api._do_refresh_token.assert_awaited_once()
        api._do_generate_access_token.assert_not_awaited()

    async def test_refresh_failure_falls_back_to_generate(self):
        api = _make_api()
        _store_token(api, expires_in=100)
        api._do_refresh_token = AsyncMock(side_effect=RuntimeError("boom"))
        api._do_generate_access_token = AsyncMock(
            return_value=AccessTokenDto(access_token="FRESH", refresh_token="NR", expires_in=7200)
        )
        token = await api.get_valid_token()
        assert token == "FRESH"
        api._do_refresh_token.assert_awaited_once()
        api._do_generate_access_token.assert_awaited_once()

    async def test_clear_token_cache(self):
        api = _make_api()
        _store_token(api)
        assert api.has_valid_token is True
        await api.clear_token_cache()
        assert api.has_valid_token is False
        assert api.cached_access_token is None
        assert api._token_refresh_attempts == 0


# ── OpenApiBase: public generate/refresh wrappers ────────────────────────────


class TestTokenWrappers:
    async def test_generate_access_token_stores_and_returns(self):
        api = _make_api()
        api._do_generate_access_token = AsyncMock(
            return_value=AccessTokenDto(access_token="G", refresh_token="GR", expires_in=7200)
        )
        dto = await api.generate_access_token()
        assert dto.access_token == "G"
        assert api.cached_access_token == "G"

    async def test_refresh_token_stores_and_returns(self):
        api = _make_api()
        api._do_refresh_token = AsyncMock(
            return_value=AccessTokenDto(access_token="R", refresh_token="RR", expires_in=7200)
        )
        dto = await api.refresh_token("some-refresh")
        assert dto.access_token == "R"
        assert api.cached_access_token == "R"
        api._do_refresh_token.assert_awaited_once_with("some-refresh")


# ── OpenApiBase: low-level HTTP for token endpoints (aiohttp patched) ────────


class TestTokenHttp:
    async def test_do_generate_access_token_success(self, monkeypatch):
        api = _make_api()
        resp = _FakeResp(
            status=200,
            payload={"code": 200, "data": {"access_token": "T1", "refresh_token": "RT1", "expires_in": 600}},
        )
        _patch_session(monkeypatch, resp)
        dto = await api._do_generate_access_token()
        assert dto.access_token == "T1"
        assert dto.refresh_token == "RT1"
        assert dto.expires_in == 600

    async def test_do_generate_access_token_http_error(self, monkeypatch):
        api = _make_api()
        resp = _FakeResp(status=500, text="server boom")
        _patch_session(monkeypatch, resp)
        with pytest.raises(ValueError, match="HTTP 500"):
            await api._do_generate_access_token()

    async def test_do_generate_access_token_api_error(self, monkeypatch):
        api = _make_api()
        resp = _FakeResp(status=200, payload={"code": 400, "msg": "bad creds"})
        _patch_session(monkeypatch, resp)
        with pytest.raises(ValueError, match="generate_access_token failed"):
            await api._do_generate_access_token()

    async def test_do_generate_access_token_rate_limit_logged(self, monkeypatch, caplog):
        api = _make_api()
        resp = _FakeResp(status=200, payload={"code": 400, "msg": "3001008 too frequently"})
        _patch_session(monkeypatch, resp)
        with caplog.at_level("ERROR"):
            with pytest.raises(ValueError):
                await api._do_generate_access_token()
        assert any("rate limit" in r.message.lower() or "3001008" in r.message for r in caplog.records)

    async def test_do_refresh_token_success(self, monkeypatch):
        api = _make_api()
        resp = _FakeResp(
            status=200,
            payload={"code": 200, "data": {"access_token": "T2", "refresh_token": "RT2", "expires_in": 120}},
        )
        _patch_session(monkeypatch, resp)
        dto = await api._do_refresh_token("rt")
        assert dto.access_token == "T2"
        assert dto.expires_in == 120

    async def test_do_refresh_token_api_error(self, monkeypatch):
        api = _make_api()
        resp = _FakeResp(status=200, payload={"code": 401, "message": "invalid refresh"})
        _patch_session(monkeypatch, resp)
        with pytest.raises(ValueError, match="refresh_token failed"):
            await api._do_refresh_token("rt")


# ── OpenApiBase: request signing + wrappers ──────────────────────────────────


class TestRequestSigning:
    async def test_request_builds_sign_and_calls_http(self):
        api = _make_api()
        fake_result = ResponseResult(code=0, data={"ok": 1})
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=fake_result)
            result = await api.request(
                access_token="TOK",
                route_name="/route/x",
                method="POST",
                req_body={"a": 1, "b": [1, 2]},
            )
        assert result is fake_result
        http_cls.return_value.request.assert_awaited_once()
        call = http_cls.return_value.request.call_args
        assert call.args[0] == "POST"
        assert call.args[1] == "https://openapi.test/route/x"
        params = call.kwargs["params"]
        # sign params always present
        assert {"app_key", "access_token", "timestamp", "sign"} <= set(params)
        assert params["access_token"] == "TOK"
        assert params["app_key"] == "app_id_x"
        assert call.kwargs["json"] == {"a": 1, "b": [1, 2]}
        # body present -> default Content-Type applied
        assert call.kwargs["headers"]["Content-Type"] == "application/json"

    async def test_request_get_without_body_no_content_type(self):
        api = _make_api()
        fake_result = ResponseResult(code=0, data=None)
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=fake_result)
            await api.request(access_token="T", route_name="/r", method="GET", req_params={"q": "v"})
        call = http_cls.return_value.request.call_args
        assert call.args[0] == "GET"
        assert call.kwargs["headers"] == {}  # no body -> no default content type
        assert call.kwargs["params"]["q"] == "v"
        assert call.kwargs["json"] is None

    async def test_request_skip_rate_limit(self):
        api = _make_api()
        api._rate_limiter.wait_if_needed = AsyncMock(return_value=0)
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=ResponseResult())
            await api.request(access_token="T", route_name="/r", method="GET", skip_rate_limit=True)
        api._rate_limiter.wait_if_needed.assert_not_awaited()

    async def test_get_wrapper_auto_token(self):
        api = _make_api()
        api.get_valid_token = AsyncMock(return_value="AUTOTOK")
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=ResponseResult(code=0))
            await api.get(route_name="/g", req_params={"x": 1})
        call = http_cls.return_value.request.call_args
        assert call.args[0] == "GET"
        assert call.kwargs["params"]["access_token"] == "AUTOTOK"

    async def test_post_wrapper_auto_token(self):
        api = _make_api()
        api.get_valid_token = AsyncMock(return_value="AUTOTOK")
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=ResponseResult(code=0))
            await api.post(route_name="/p", req_body={"k": "v"})
        call = http_cls.return_value.request.call_args
        assert call.args[0] == "POST"
        assert call.kwargs["json"] == {"k": "v"}
        assert call.kwargs["headers"]["Content-Type"] == "application/json"

    async def test_request_with_auto_token_combines(self):
        api = _make_api()
        api.get_valid_token = AsyncMock(return_value="AT")
        with patch("lingxing.core.openapi.HttpBase") as http_cls:
            http_cls.return_value.request = AsyncMock(return_value=ResponseResult(code=0))
            await api.request_with_auto_token(route_name="/x", method="POST", req_body={"a": 1})
        api.get_valid_token.assert_awaited_once()
        assert http_cls.return_value.request.call_args.kwargs["params"]["access_token"] == "AT"


# ── AuthManager ──────────────────────────────────────────────────────────────


def _make_auth() -> tuple[AuthManager, MagicMock]:
    openapi = MagicMock()
    openapi.generate_access_token = AsyncMock(
        return_value=AccessTokenDto(access_token="GEN", refresh_token="GRT", expires_in=7200)
    )
    openapi.refresh_token = AsyncMock(
        return_value=AccessTokenDto(access_token="REF", refresh_token="RRT", expires_in=7200)
    )
    return AuthManager(openapi), openapi


class TestAuthManagerState:
    def test_access_token_none_initially(self):
        auth, _ = _make_auth()
        assert auth.access_token is None

    def test_should_refresh_false_without_token(self):
        auth, _ = _make_auth()
        # No token -> _should_refresh_token returns False (different from OpenApiBase)
        assert auth._should_refresh_token() is False

    def test_should_refresh_true_when_near_expiry(self):
        auth, _ = _make_auth()
        auth._access_token = "x"
        auth._token_expires_at = datetime.now() + timedelta(seconds=100)
        assert auth._should_refresh_token() is True

    def test_should_refresh_false_when_fresh(self):
        auth, _ = _make_auth()
        auth._access_token = "x"
        auth._token_expires_at = datetime.now() + timedelta(seconds=7200)
        assert auth._should_refresh_token() is False


class TestAuthManagerEnsureToken:
    async def test_first_call_gets_new_token(self):
        auth, openapi = _make_auth()
        token = await auth.ensure_token()
        assert token == "GEN"
        openapi.generate_access_token.assert_awaited_once()
        assert auth.access_token == "GEN"

    async def test_cached_token_reused_no_network(self):
        auth, openapi = _make_auth()
        await auth.ensure_token()
        openapi.generate_access_token.reset_mock()
        # Second call: token fresh -> no refresh, no new fetch
        token = await auth.ensure_token()
        assert token == "GEN"
        openapi.generate_access_token.assert_not_awaited()
        openapi.refresh_token.assert_not_awaited()

    async def test_expired_token_with_refresh_triggers_refresh(self):
        auth, openapi = _make_auth()
        await auth.ensure_token()
        # Force expiry within threshold
        auth._token_expires_at = datetime.now() + timedelta(seconds=10)
        token = await auth.ensure_token()
        assert token == "REF"
        openapi.refresh_token.assert_awaited_once()

    async def test_clear_tokens(self):
        auth, _ = _make_auth()
        await auth.ensure_token()
        assert auth.access_token is not None
        auth.clear_tokens()
        assert auth.access_token is None
        assert auth._token_refresh_attempts == 0


class TestAuthManagerRefreshLogic:
    async def test_refresh_fallback_to_get_when_no_refresh_token(self):
        auth, openapi = _make_auth()
        auth._access_token = "old"
        auth._token_expires_at = datetime.now() + timedelta(seconds=10)
        auth._refresh_token = None  # no refresh token -> fallback to get
        dto = await auth._refresh_access_token()
        assert dto.access_token == "GEN"
        openapi.generate_access_token.assert_awaited_once()
        openapi.refresh_token.assert_not_awaited()

    async def test_refresh_raises_after_max_attempts(self):
        auth, _ = _make_auth()
        auth._token_refresh_attempts = 3  # already at max -> next increment exceeds
        auth._refresh_token = "rt"
        with pytest.raises(Exception, match="Token refresh failed after"):
            await auth._refresh_access_token()

    async def test_refresh_failure_at_max_falls_back_to_get(self):
        auth, openapi = _make_auth()
        # attempts=2 -> after increment 3 (== max), refresh raises -> fallback to get
        auth._token_refresh_attempts = 2
        auth._refresh_token = "rt"
        openapi.refresh_token = AsyncMock(side_effect=RuntimeError("refresh down"))
        dto = await auth._refresh_access_token()
        assert dto.access_token == "GEN"
        openapi.generate_access_token.assert_awaited_once()

    async def test_refresh_failure_below_max_reraises(self):
        auth, openapi = _make_auth()
        auth._token_refresh_attempts = 0  # increment -> 1 (< max)
        auth._refresh_token = "rt"
        openapi.refresh_token = AsyncMock(side_effect=RuntimeError("transient"))
        with pytest.raises(RuntimeError, match="transient"):
            await auth._refresh_access_token()

    async def test_refresh_empty_token_raises_value_error(self):
        auth, openapi = _make_auth()
        auth._token_refresh_attempts = 0
        auth._refresh_token = "rt"
        openapi.refresh_token = AsyncMock(
            return_value=AccessTokenDto(access_token="", refresh_token="r", expires_in=100)
        )
        # empty token -> ValueError, but attempts(1) < max(3) -> reraised as ValueError
        with pytest.raises(ValueError, match="empty token"):
            await auth._refresh_access_token()

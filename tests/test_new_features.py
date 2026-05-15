"""Tests for new SDK features: retry, pagination, response models, exports."""
import asyncio
from unittest.mock import AsyncMock, MagicMock

import pytest

from lingxing.core.resp_schema import ResponseResult
from lingxing.endpoints._base import BaseEndpoint
from lingxing.errors import ApiError, RateLimitError


def _make_resp(code=0, message="ok", data=None, request_id=""):
    return ResponseResult(code=code, message=message, data=data, request_id=request_id)


# ===================================================================
# Retry
# ===================================================================

class TestAutoRetry:
    @pytest.fixture
    def ep(self):
        api = MagicMock()
        api.request_with_auto_token = AsyncMock()
        return BaseEndpoint(api)

    @pytest.mark.asyncio
    async def test_success_no_retry(self, ep):
        ep._openapi.request_with_auto_token.return_value = _make_resp(data={"list": [1]})
        resp = await ep._post("/t")
        assert resp.code == 0
        assert ep._openapi.request_with_auto_token.call_count == 1

    @pytest.mark.asyncio
    async def test_rate_limit_retries(self, ep):
        ep.max_retries = 2
        ep.retry_delay = 0.01
        ep._openapi.request_with_auto_token.side_effect = [
            _make_resp(code=3001008, message="limited"),
            _make_resp(data={"ok": True}),
        ]
        resp = await ep._post("/t")
        assert resp.code == 0
        assert ep._openapi.request_with_auto_token.call_count == 2

    @pytest.mark.asyncio
    async def test_rate_limit_exhausted(self, ep):
        ep.max_retries = 2
        ep.retry_delay = 0.01
        ep._openapi.request_with_auto_token.return_value = _make_resp(code=3001008, message="limited")
        with pytest.raises(RateLimitError):
            await ep._post("/t")
        assert ep._openapi.request_with_auto_token.call_count == 3

    @pytest.mark.asyncio
    async def test_network_error_retries(self, ep):
        ep.max_retries = 1
        ep.retry_delay = 0.01
        ep._openapi.request_with_auto_token.side_effect = [
            ConnectionError("net"),
            _make_resp(data={"ok": True}),
        ]
        resp = await ep._post("/t")
        assert resp.code == 0

    @pytest.mark.asyncio
    async def test_api_error_no_retry(self, ep):
        ep.max_retries = 3
        ep._openapi.request_with_auto_token.return_value = _make_resp(code=400, message="bad")
        with pytest.raises(ApiError):
            await ep._post("/t")
        assert ep._openapi.request_with_auto_token.call_count == 1


# ===================================================================
# Pagination
# ===================================================================

class TestPagination:
    @pytest.fixture
    def ep(self):
        api = MagicMock()
        api.request_with_auto_token = AsyncMock()
        return BaseEndpoint(api)

    @pytest.mark.asyncio
    async def test_iter_single_page(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.return_value = _make_resp(
            data={"list": [{"id": 1}, {"id": 2}], "total": 2}
        )
        pages = []
        async for p in ep._iter_pages("/t", Item, page_size=100):
            pages.append(p)
        assert len(pages) == 1
        assert len(pages[0]) == 2

    @pytest.mark.asyncio
    async def test_iter_multi_page(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.side_effect = [
            _make_resp(data={"list": [{"id": i} for i in range(5)], "total": 8}),
            _make_resp(data={"list": [{"id": i} for i in range(5, 8)], "total": 8}),
        ]
        pages = []
        async for p in ep._iter_pages("/t", Item, page_size=5):
            pages.append(p)
        assert len(pages) == 2
        assert len(pages[0]) == 5
        assert len(pages[1]) == 3

    @pytest.mark.asyncio
    async def test_iter_empty(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.return_value = _make_resp(
            data={"list": [], "total": 0}
        )
        pages = []
        async for p in ep._iter_pages("/t", Item):
            pages.append(p)
        assert len(pages) == 0

    @pytest.mark.asyncio
    async def test_iter_max_pages(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.return_value = _make_resp(
            data={"list": [{"id": i} for i in range(10)], "total": 1000}
        )
        pages = []
        async for p in ep._iter_pages("/t", Item, page_size=10, max_pages=3):
            pages.append(p)
        assert len(pages) == 3

    @pytest.mark.asyncio
    async def test_collect_all(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.side_effect = [
            _make_resp(data={"list": [{"id": i} for i in range(5)], "total": 8}),
            _make_resp(data={"list": [{"id": i} for i in range(5, 8)], "total": 8}),
        ]
        items = await ep._collect_all("/t", Item, page_size=5)
        assert len(items) == 8

    @pytest.mark.asyncio
    async def test_collect_max_items(self, ep):
        from pydantic import BaseModel
        class Item(BaseModel):
            id: int

        ep._openapi.request_with_auto_token.return_value = _make_resp(
            data={"list": [{"id": i} for i in range(10)], "total": 10}
        )
        items = await ep._collect_all("/t", Item, page_size=10, max_items=5)
        assert len(items) == 5


# ===================================================================
# Response Models
# ===================================================================

class TestResponseModels:
    def test_sale_listing_model(self):
        from lingxing.models.responses.sale import MwsListingResponse
        m = MwsListingResponse(sid=123, asin="B00TEST", marketplace="US")
        assert m.sid == 123
        assert m.asin == "B00TEST"

    def test_optional_fields_default_none(self):
        from lingxing.models.responses.sale import MwsListingResponse
        m = MwsListingResponse()
        assert m.sid is None
        assert m.asin is None

    def test_extra_fields_allowed(self):
        from lingxing.models.responses.sale import MwsListingResponse
        m = MwsListingResponse(sid=1, future_field="hello")
        assert m.sid == 1


# ===================================================================
# Request Models
# ===================================================================

class TestRequestModels:
    def test_request_model_fields(self):
        from lingxing.models.requests.sale import SaleListingRequest
        req = SaleListingRequest(sid="123", offset=0, length=20)
        assert req.sid == "123"
        assert req.offset == 0


# ===================================================================
# Exports
# ===================================================================

class TestExports:
    def test_version(self):
        import lingxing
        assert lingxing.__version__ == "0.4.0"

    def test_all_importable(self):
        import lingxing
        for name in lingxing.__all__:
            assert getattr(lingxing, name) is not None

    def test_19_endpoints(self):
        from lingxing.endpoints import __all__ as ep_all
        assert len(ep_all) == 19

    def test_errors_hierarchy(self):
        from lingxing.errors import LingXingError, ApiError, RateLimitError, AuthenticationError
        assert issubclass(ApiError, LingXingError)
        assert issubclass(RateLimitError, LingXingError)
        assert issubclass(AuthenticationError, LingXingError)

    def test_types(self):
        from lingxing.types import PageRequest, PageResult
        pr = PageRequest()
        assert pr.page == 1
        assert pr.offset == 0
        result = PageResult(total=100, page=1, page_size=50)
        assert result.has_more is True
        assert result.total_pages == 2

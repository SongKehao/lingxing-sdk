#!/usr/bin/python3
"""封装Openapi基础操作

Token请求限流（错误码3001008）: generate_access_token 和 refresh_token 共享限流配额
业务API限流: 100次/分钟
"""

from __future__ import annotations

import asyncio
import copy
import logging
import time
from collections.abc import Mapping
from datetime import datetime, timedelta
from typing import Any

import aiohttp

from .http_util import HttpBase
from .rate_limiter import get_rate_limiter
from .resp_schema import AccessTokenDto, ResponseResult
from .sign import SignBase

logger = logging.getLogger(__name__)

# 默认Token刷新阈值（秒）- 提前5分钟刷新
DEFAULT_TOKEN_REFRESH_THRESHOLD = 300


class OpenApiBase:
    """领星OpenAPI基础客户端 - Token自动缓存/刷新、限流保护"""

    def __init__(
        self,
        host: str,
        app_id: str,
        app_secret: str,
        token_refresh_threshold: int = DEFAULT_TOKEN_REFRESH_THRESHOLD,
    ):
        self.host = host
        self.app_id = app_id
        self.app_secret = app_secret
        self._rate_limiter = get_rate_limiter()
        self._token_refresh_threshold = token_refresh_threshold

        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._token_expires_at: datetime | None = None
        self._token_lock = asyncio.Lock()
        self._token_refresh_attempts: int = 0
        self._max_token_refresh_attempts: int = 3

    @property
    def has_valid_token(self) -> bool:
        if not self._access_token or not self._token_expires_at:
            return False
        return datetime.now() < self._token_expires_at

    @property
    def cached_access_token(self) -> str | None:
        return self._access_token

    @property
    def token_expires_in_seconds(self) -> int | None:
        if not self._token_expires_at:
            return None
        remaining = (self._token_expires_at - datetime.now()).total_seconds()
        return max(0, int(remaining))

    def _should_refresh_token(self) -> bool:
        if not self._access_token or not self._token_expires_at:
            return True
        # 在过期前提前刷新
        threshold = timedelta(seconds=self._token_refresh_threshold)
        return datetime.now() >= (self._token_expires_at - threshold)

    def _store_token(self, token_dto: AccessTokenDto) -> None:
        self._access_token = token_dto.access_token
        self._refresh_token = token_dto.refresh_token
        self._token_expires_at = datetime.now() + timedelta(seconds=token_dto.expires_in)
        self._token_refresh_attempts = 0  # 重置重试计数
        logger.debug(
            "Token cached, expires at %s, expires_in=%ss",
            self._token_expires_at.isoformat(),
            token_dto.expires_in,
        )

    async def get_valid_token(self) -> str:
        """获取有效access_token，自动缓存和刷新"""
        async with self._token_lock:
            # 检查是否需要刷新或获取新Token
            if self._should_refresh_token():
                # 如果有refresh_token，尝试刷新
                if self._refresh_token:
                    try:
                        token_dto = await self._do_refresh_token(self._refresh_token)
                        self._store_token(token_dto)
                        logger.info("Token refreshed successfully from cache")
                    except Exception as e:
                        logger.warning("Token refresh failed: %s, getting new token", e)
                        token_dto = await self._do_generate_access_token()
                        self._store_token(token_dto)
                else:
                    # 没有refresh_token，获取新Token
                    token_dto = await self._do_generate_access_token()
                    self._store_token(token_dto)

            assert self._access_token is not None
            return self._access_token

    async def clear_token_cache(self) -> None:
        async with self._token_lock:
            self._access_token = None
            self._refresh_token = None
            self._token_expires_at = None
            self._token_refresh_attempts = 0
            logger.info("Token cache cleared")

    async def generate_access_token(self) -> AccessTokenDto:
        """获取 access_token。推荐用 get_valid_token() 自动管理缓存。"""
        async with self._token_lock:
            token_dto = await self._do_generate_access_token()
            self._store_token(token_dto)
            return token_dto

    async def _do_generate_access_token(self) -> AccessTokenDto:
        wait_time = await self._rate_limiter.wait_if_needed("token")
        if wait_time > 0:
            logger.info("Rate limiter: waited %.1fs before token request", wait_time)

        # 官方文档: /api/auth-server/oauth/access-token
        path = "/api/auth-server/oauth/access-token"
        req_url = self.host + path

        # 官方文档: multipart/form-data 格式
        form_data = aiohttp.FormData()
        form_data.add_field("appId", self.app_id)
        form_data.add_field("appSecret", self.app_secret)

        try:
            async with (
                aiohttp.ClientSession() as session,
                session.post(req_url, data=form_data, timeout=aiohttp.ClientTimeout(total=30)) as resp,
            ):
                if resp.status != 200:
                    text = await resp.text()
                    msg = f"HTTP {resp.status}: {text}"
                    raise ValueError(msg)
                resp_json = await resp.json()

            # 检查响应
            code = resp_json.get("code")
            msg = resp_json.get("msg", resp_json.get("message", "Unknown error"))
            if code not in [200, "200"]:
                error_msg = f"generate_access_token failed: {msg}"
                raise ValueError(error_msg)

            data = resp_json.get("data", {})
            return AccessTokenDto(
                access_token=data.get("access_token"),
                refresh_token=data.get("refresh_token"),
                expires_in=data.get("expires_in", 7200),
            )
        except ValueError as e:
            # 检测限流错误并提供友好提示
            error_str = str(e)
            if "too frequently" in error_str.lower() or "3001008" in error_str:
                logger.exception(
                    "LingXing API rate limit detected! Please wait before retrying. Error: %s",
                    error_str,
                )
            raise

    async def refresh_token(self, refresh_token: str) -> AccessTokenDto:
        """续约access-token（与generate_access_token共享限流配额）"""
        async with self._token_lock:
            token_dto = await self._do_refresh_token(refresh_token)
            self._store_token(token_dto)
            return token_dto

    async def _do_refresh_token(self, refresh_token: str) -> AccessTokenDto:
        wait_time = await self._rate_limiter.wait_if_needed("token")
        if wait_time > 0:
            logger.info("Rate limiter: waited %.1fs before refresh request", wait_time)

        path = "/api/auth-server/oauth/refresh"
        req_url = self.host + path

        form_data = aiohttp.FormData()
        form_data.add_field("appId", self.app_id)
        form_data.add_field("refreshToken", refresh_token)

        try:
            async with (
                aiohttp.ClientSession() as session,
                session.post(req_url, data=form_data, timeout=aiohttp.ClientTimeout(total=30)) as resp,
            ):
                if resp.status != 200:
                    text = await resp.text()
                    msg = f"HTTP {resp.status}: {text}"
                    raise ValueError(msg)
                resp_json = await resp.json()

            code = resp_json.get("code")
            if code not in [200, "200"]:
                msg = resp_json.get("msg")
                if not msg:
                    msg = resp_json.get("message", "Unknown error")
                error_msg = f"refresh_token failed: {msg}"
                raise ValueError(error_msg)

            data = resp_json.get("data", {})
            return AccessTokenDto(
                access_token=data.get("access_token"),
                refresh_token=data.get("refresh_token"),
                expires_in=data.get("expires_in", 7200),
            )
        except ValueError as e:
            error_str = str(e)
            if "too frequently" in error_str.lower() or "3001008" in error_str:
                logger.exception(
                    "LingXing API rate limit detected! Please wait before retrying. Error: %s",
                    error_str,
                )
            raise

    async def request(
        self,
        access_token: str,
        route_name: str,
        method: str,
        req_params: Mapping[str, Any] | None = None,
        req_body: Mapping[str, Any] | None = None,
        skip_rate_limit: bool = False,
        **kwargs: Any,
    ) -> ResponseResult:
        """发送业务API请求"""
        if not skip_rate_limit:
            await self._rate_limiter.wait_if_needed("api")

        req_url = self.host + route_name
        headers = kwargs.pop("headers", {})
        req_params = dict(req_params or {})
        req_body = dict(req_body) if req_body is not None else None
        gen_sign_params = copy.deepcopy(req_body) if req_body else {}
        if req_params:
            gen_sign_params.update(req_params)

        sign_params = {
            "app_key": self.app_id,
            "access_token": access_token,
            "timestamp": f"{int(time.time())}",
        }
        gen_sign_params.update(sign_params)
        sign = SignBase.generate_sign(self.app_id, gen_sign_params)
        sign_params["sign"] = sign
        req_params.update(sign_params)

        # 对于带有请求体的, 需要设置默认的Content-Type
        if req_body and "Content-Type" not in headers:
            headers["Content-Type"] = "application/json"
        return await HttpBase().request(method, req_url, params=req_params, headers=headers, json=req_body, **kwargs)

    async def request_with_auto_token(
        self,
        route_name: str,
        method: str,
        req_params: Mapping[str, Any] | None = None,
        req_body: Mapping[str, Any] | None = None,
        skip_rate_limit: bool = False,
        **kwargs: Any,
    ) -> ResponseResult:
        """发送业务API请求（自动管理Token）"""
        access_token = await self.get_valid_token()
        return await self.request(
            access_token=access_token,
            route_name=route_name,
            method=method,
            req_params=req_params,
            req_body=req_body,
            skip_rate_limit=skip_rate_limit,
            **kwargs,
        )

    async def get(
        self,
        route_name: str,
        access_token: str | None = None,
        req_params: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> ResponseResult:
        if access_token is None:
            access_token = await self.get_valid_token()
        return await self.request(
            access_token=access_token, route_name=route_name, method="GET", req_params=req_params, **kwargs
        )

    async def post(
        self,
        route_name: str,
        access_token: str | None = None,
        req_params: Mapping[str, Any] | None = None,
        req_body: Mapping[str, Any] | None = None,
        **kwargs: Any,
    ) -> ResponseResult:
        if access_token is None:
            access_token = await self.get_valid_token()
        return await self.request(
            access_token=access_token,
            route_name=route_name,
            method="POST",
            req_params=req_params,
            req_body=req_body,
            **kwargs,
        )

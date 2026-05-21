from __future__ import annotations
#!/usr/bin/env python3
"""
领星ERP认证管理器

负责token的获取、刷新和生命周期管理
"""

import asyncio
import logging
from datetime import datetime, timedelta

from .openapi import OpenApiBase
from .resp_schema import AccessTokenDto

logger = logging.getLogger(__name__)


class AuthManager:
    """认证管理器 - 处理token获取和刷新"""

    def __init__(
        self,
        openapi: OpenApiBase,
        token_refresh_threshold_seconds: int = 300,
        max_refresh_attempts: int = 3
    ):
        """
        初始化认证管理器

        Args:
            openapi: OpenAPI基础客户端
            token_refresh_threshold_seconds: token刷新阈值（秒）
            max_refresh_attempts: 最大刷新尝试次数
        """
        self._openapi = openapi
        self._token_refresh_threshold = token_refresh_threshold_seconds
        self._max_refresh_attempts = max_refresh_attempts

        self._access_token: str | None = None
        self._refresh_token: str | None = None
        self._token_expires_at: datetime | None = None
        self._token_refresh_attempts: int = 0
        self._token_lock = asyncio.Lock()

    @property
    def access_token(self) -> str | None:
        """获取当前访问token"""
        return self._access_token

    async def ensure_token(self) -> str:
        """
        确保有有效的访问token

        Returns:
            有效的访问token

        Raises:
            Exception: token获取失败
        """
        async with self._token_lock:
            if self._should_refresh_token():
                await self._refresh_access_token()

            if not self._access_token:
                await self._get_access_token()

            return self._access_token

    def _should_refresh_token(self) -> bool:
        """检查是否需要刷新token"""
        if not self._access_token or not self._token_expires_at:
            return False

        threshold = timedelta(seconds=self._token_refresh_threshold)
        return datetime.now() >= (self._token_expires_at - threshold)

    async def _get_access_token(self) -> AccessTokenDto:
        """获取新的访问token"""
        logger.debug("Getting new access token")

        token_dto = await self._openapi.generate_access_token()

        self._access_token = token_dto.access_token
        self._refresh_token = token_dto.refresh_token
        self._token_expires_at = datetime.now() + timedelta(
            seconds=token_dto.expires_in
        )

        logger.debug("Access token obtained, expires at: %s", self._token_expires_at)
        return token_dto

    async def _refresh_access_token(self) -> AccessTokenDto:
        """刷新访问token"""
        logger.debug("Refreshing access token")

        self._token_refresh_attempts += 1
        if self._token_refresh_attempts > self._max_refresh_attempts:
            self._token_refresh_attempts = 0
            msg = f"Token refresh failed after {self._max_refresh_attempts} attempts"
            raise Exception(
                msg
            )

        if not self._refresh_token:
            self._token_refresh_attempts = 0
            return await self._get_access_token()

        try:
            if self._token_refresh_attempts > 1:
                delay = 2 ** (self._token_refresh_attempts - 1)
                logger.debug("Token refresh attempt %s, waiting %ss", self._token_refresh_attempts, delay)
                await asyncio.sleep(delay)

            token_dto = await self._openapi.refresh_token(self._refresh_token)

            if not token_dto.access_token:
                msg = "Refresh returned empty token"
                raise ValueError(msg)

            self._access_token = token_dto.access_token
            self._refresh_token = token_dto.refresh_token or self._refresh_token
            self._token_expires_at = datetime.now() + timedelta(
                seconds=token_dto.expires_in
            )
            self._token_refresh_attempts = 0

            logger.debug("Token refreshed, expires at: %s", self._token_expires_at)

        except Exception as e:
            logger.warning("Token refresh failed: %s", e)
            if self._token_refresh_attempts >= self._max_refresh_attempts:
                self._token_refresh_attempts = 0
                return await self._get_access_token()
            raise
        else:
            return token_dto

    def clear_tokens(self):
        """清除所有token"""
        self._access_token = None
        self._refresh_token = None
        self._token_expires_at = None
        self._token_refresh_attempts = 0

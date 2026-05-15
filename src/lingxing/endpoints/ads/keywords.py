#!/usr/bin/env python3
"""关键词和定向管理API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class KeywordsEndpoint(BaseEndpoint):
    """关键词和定向管理端点"""

    async def get_sp_keywords(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP关键词列表"""
        return await self._post(
            "/pb/openapi/newad/sp/keyword/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_targets(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP商品定向列表"""
        return await self._post(
            "/pb/openapi/newad/sp/target/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_negative_targets(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP否定商品定向列表"""
        return await self._post(
            "/pb/openapi/newad/sp/negativetarget/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_targeting(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB定向列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/targeting/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_negative_keywords(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB否定关键词列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/negativekeyword/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_negative_targets(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB否定定向列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/negativetarget/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_targets(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD定向列表"""
        return await self._post(
            "/pb/openapi/newad/sd/target/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_negative_targets(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD否定定向列表"""
        return await self._post(
            "/pb/openapi/newad/sd/negativetarget/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

#!/usr/bin/env python3
"""广告活动管理API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class CampaignsEndpoint(BaseEndpoint):
    """广告活动管理端点"""

    async def get_sp_campaigns(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP广告活动列表"""
        return await self._post(
            "/pb/openapi/newad/sp/campaign/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_adgroups(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP广告组列表"""
        return await self._post(
            "/pb/openapi/newad/sp/adgroup/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_product_ads(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP商品广告列表"""
        return await self._post(
            "/pb/openapi/newad/sp/productad/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_campaigns(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB广告活动列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/campaign/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_adgroups(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB广告组列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/adgroup/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_creatives(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB创意列表"""
        return await self._post(
            "/pb/openapi/newad/hsa/creative/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_campaigns(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD广告活动列表"""
        return await self._post(
            "/pb/openapi/newad/sd/campaign/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_adgroups(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD广告组列表"""
        return await self._post(
            "/pb/openapi/newad/sd/adgroup/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_product_ads(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD商品广告列表"""
        return await self._post(
            "/pb/openapi/newad/sd/productad/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_portfolios(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询广告组合列表"""
        return await self._post(
            "/pb/openapi/newad/portfolio/list",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

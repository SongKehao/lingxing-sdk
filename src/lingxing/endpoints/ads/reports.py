#!/usr/bin/env python3
"""广告报表API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class ReportsEndpoint(BaseEndpoint):
    """广告报表端点"""

    async def get_sp_campaign_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP广告活动报表"""
        return await self._post(
            "/pb/openapi/newad/sp/campaign/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_adgroup_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP广告组报表"""
        return await self._post(
            "/pb/openapi/newad/sp/adgroup/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_product_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP商品广告报表"""
        return await self._post(
            "/pb/openapi/newad/sp/productad/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_keyword_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP关键词报表"""
        return await self._post(
            "/pb/openapi/newad/sp/keyword/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_search_term_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP搜索词报表"""
        return await self._post(
            "/pb/openapi/newad/sp/searchterm/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_target_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP定向报表"""
        return await self._post(
            "/pb/openapi/newad/sp/target/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sp_asin_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SP ASIN报表"""
        return await self._post(
            "/pb/openapi/newad/sp/asin/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_campaign_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB广告活动报表"""
        return await self._post(
            "/pb/openapi/newad/hsa/campaign/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_adgroup_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB广告组报表"""
        return await self._post(
            "/pb/openapi/newad/hsa/adgroup/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_creative_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB创意报表"""
        return await self._post(
            "/pb/openapi/newad/hsa/creative/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_search_term_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB搜索词报表"""
        return await self._post(
            "/pb/openapi/newad/hsa/searchterm/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sb_targeting_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SB定向报表"""
        return await self._post(
            "/pb/openapi/newad/hsa/targeting/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_campaign_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD广告活动报表"""
        return await self._post(
            "/pb/openapi/newad/sd/campaign/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_adgroup_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD广告组报表"""
        return await self._post(
            "/pb/openapi/newad/sd/adgroup/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_product_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD商品广告报表"""
        return await self._post(
            "/pb/openapi/newad/sd/productad/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_sd_target_reports(
        self, sid: int, report_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SD定向报表"""
        return await self._post(
            "/pb/openapi/newad/sd/target/report",
            data={"sid": sid, "report_date": report_date, "offset": offset, "length": length, **kwargs}
        )

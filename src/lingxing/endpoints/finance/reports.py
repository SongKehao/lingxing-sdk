#!/usr/bin/env python3
"""财务报表API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class ReportsEndpoint(BaseEndpoint):
    """财务报表端点"""

    async def get_profit_report_msku(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询MSKU利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/msku",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_report_asin(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询ASIN利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/asin",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_report_sku(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询SKU利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/sku",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_report_seller(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询卖家利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/seller",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_seller_monthly(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询卖家月度利润"""
        return await self._post(
            "/pb/openapi/finance/profit/seller/monthly",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_stats_msku(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询MSKU利润统计"""
        return await self._post(
            "/pb/openapi/finance/profit/stats/msku",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_stats_asin(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询ASIN利润统计"""
        return await self._post(
            "/pb/openapi/finance/profit/stats/asin",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_long_term_storage_fee(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA长期仓储费"""
        return await self._post(
            "/pb/openapi/finance/fba/long/term/storage/fee",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_reimbursement_report(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询赔偿报表"""
        return await self._post(
            "/pb/openapi/finance/reimbursement/report",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_report_parent_asin(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询父ASIN利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/parent/asin",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_report_order(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询订单利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/order",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def recompute_profit_report(
        self, sid: int, start_date: str, end_date: str, **kwargs
    ) -> dict[str, Any]:
        """重新计算利润报表"""
        return await self._post(
            "/pb/openapi/finance/profit/report/recompute",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, **kwargs}
        )

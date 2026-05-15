#!/usr/bin/env python3
"""库存统计API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class InventoryEndpoint(BaseEndpoint):
    """库存统计端点"""

    async def get_fba_storage_fee_month(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA月度仓储费"""
        return await self._post(
            "/pb/openapi/statistics/fba/storage/fee/month",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_storage_fee_long_term(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA长期仓储费"""
        return await self._post(
            "/pb/openapi/statistics/fba/storage/fee/long/term",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_stock_report(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA库存报表"""
        return await self._post(
            "/pb/openapi/statistics/fba/stock/report",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_reimbursement_list(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询赔偿列表"""
        return await self._post(
            "/pb/openapi/statistics/reimbursement/list",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_return_orders(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA退货订单"""
        return await self._post(
            "/pb/openapi/statistics/fba/return/orders",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fbm_return_orders(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBM退货订单"""
        return await self._post(
            "/pb/openapi/statistics/fbm/return/orders",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_return_analysis(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询退货分析"""
        return await self._post(
            "/pb/openapi/statistics/return/analysis",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

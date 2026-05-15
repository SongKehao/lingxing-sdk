#!/usr/bin/env python3
"""销售统计API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class SalesEndpoint(BaseEndpoint):
    """销售统计端点"""

    async def get_product_performance(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询产品表现"""
        return await self._post(
            "/pb/openapi/statistics/product/performance",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_all_product_performance(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询所有产品表现"""
        return await self._post(
            "/pb/openapi/statistics/all/product/performance",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_store_sales_summary(
        self, sid: int, start_date: str, end_date: str, **kwargs
    ) -> dict[str, Any]:
        """查询店铺销售汇总"""
        return await self._post(
            "/pb/openapi/statistics/store/sales/summary",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, **kwargs}
        )

    async def get_asin_daily_lists(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询ASIN每日列表"""
        return await self._post(
            "/pb/openapi/statistics/asin/daily/lists",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_order_profit(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询订单利润"""
        return await self._post(
            "/pb/openapi/statistics/order/profit",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

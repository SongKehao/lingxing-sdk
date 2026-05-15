#!/usr/bin/env python3
"""绩效指标API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class PerformanceEndpoint(BaseEndpoint):
    """绩效指标端点"""

    async def get_profit_stat_asin(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询ASIN利润统计"""
        return await self._post(
            "/pb/openapi/statistics/profit/stat/asin",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_stat_msku(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询MSKU利润统计"""
        return await self._post(
            "/pb/openapi/statistics/profit/stat/msku",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_profit_stat_store(
        self, sid: int, start_date: str, end_date: str, **kwargs
    ) -> dict[str, Any]:
        """查询店铺利润统计"""
        return await self._post(
            "/pb/openapi/statistics/profit/stat/store",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, **kwargs}
        )

    async def get_profit_stat_parent_asin(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询父ASIN利润统计"""
        return await self._post(
            "/pb/openapi/statistics/profit/stat/parent/asin",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_purchase_report_buyer(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询采购报表-买家"""
        return await self._post(
            "/pb/openapi/statistics/purchase/report/buyer",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_purchase_report_product(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询采购报表-产品"""
        return await self._post(
            "/pb/openapi/statistics/purchase/report/product",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_purchase_report_supplier(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询采购报表-供应商"""
        return await self._post(
            "/pb/openapi/statistics/purchase/report/supplier",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_operate_log(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询操作日志"""
        return await self._post(
            "/pb/openapi/statistics/operate/log",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_cost_center_gather(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA成本中心汇总"""
        return await self._post(
            "/pb/openapi/statistics/fba/cost/center/gather",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_cost_center_detail(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA成本中心明细"""
        return await self._post(
            "/pb/openapi/statistics/fba/cost/center/detail",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

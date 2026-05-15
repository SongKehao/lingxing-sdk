#!/usr/bin/env python3
"""结算API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class SettlementsEndpoint(BaseEndpoint):
    """结算端点"""

    async def get_settlement_summary(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询结算汇总"""
        return await self._post(
            "/pb/openapi/finance/settlement/summary",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_settlement_transactions(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询结算交易"""
        return await self._post(
            "/pb/openapi/finance/settlement/transactions",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_prepay_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询预付款请求池"""
        return await self._post(
            "/pb/openapi/finance/prepay/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_logistics_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询物流请求池"""
        return await self._post(
            "/pb/openapi/finance/logistics/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_monthly_settlement_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询月度结算请求池"""
        return await self._post(
            "/pb/openapi/finance/monthly/settlement/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_spot_settlement_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询现货结算请求池"""
        return await self._post(
            "/pb/openapi/finance/spot/settlement/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_other_payable_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询其他应付请求池"""
        return await self._post(
            "/pb/openapi/finance/other/payable/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_other_fee_request_pool(
        self, sid: int, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询其他费用请求池"""
        return await self._post(
            "/pb/openapi/finance/other/fee/request/pool",
            data={"sid": sid, "offset": offset, "length": length, **kwargs}
        )

    async def get_receivable_report_list(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询应收报表列表"""
        return await self._post(
            "/pb/openapi/finance/receivable/report/list",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_receivable_report_basic_info(
        self, sid: int, report_id: str, **kwargs
    ) -> dict[str, Any]:
        """查询应收报表基本信息"""
        return await self._post(
            "/pb/openapi/finance/receivable/report/basic/info",
            data={"sid": sid, "report_id": report_id, **kwargs}
        )

    async def get_receivable_report_detail_list(
        self, sid: int, report_id: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询应收报表明细列表"""
        return await self._post(
            "/pb/openapi/finance/receivable/report/detail/list",
            data={"sid": sid, "report_id": report_id, "offset": offset, "length": length, **kwargs}
        )

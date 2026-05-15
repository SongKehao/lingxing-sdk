#!/usr/bin/env python3
"""交易记录API"""

import logging
from typing import Any

from ..base import BaseEndpoint

logger = logging.getLogger(__name__)


class TransactionsEndpoint(BaseEndpoint):
    """交易记录端点"""

    async def get_order_transactions(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询订单交易记录"""
        return await self._post(
            "/pb/openapi/finance/order/transaction/list",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_inventory_ledger_detail(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询库存账本明细"""
        return await self._post(
            "/pb/openapi/finance/inventory/ledger/detail",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_inventory_ledger_summary(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询库存账本汇总"""
        return await self._post(
            "/pb/openapi/finance/inventory/ledger/summary",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fba_cost_stream(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询FBA费用流水"""
        return await self._post(
            "/pb/openapi/finance/fba/cost/stream",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def get_fee_detail_list(
        self, sid: int, start_date: str, end_date: str, offset: int = 0, length: int = 100, **kwargs
    ) -> list[dict[str, Any]]:
        """查询费用明细列表"""
        return await self._post(
            "/pb/openapi/finance/fee/detail/list",
            data={"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, **kwargs}
        )

    async def create_fee_order(
        self, sid: int, fee_data: dict[str, Any], **kwargs
    ) -> dict[str, Any]:
        """创建费用订单"""
        return await self._post(
            "/pb/openapi/finance/fee/order/create",
            data={"sid": sid, **fee_data, **kwargs}
        )

    async def edit_fee_order(
        self, sid: int, order_id: str, fee_data: dict[str, Any], **kwargs
    ) -> dict[str, Any]:
        """编辑费用订单"""
        return await self._post(
            "/pb/openapi/finance/fee/order/edit",
            data={"sid": sid, "order_id": order_id, **fee_data, **kwargs}
        )

    async def delete_fee_order(
        self, sid: int, order_id: str, **kwargs
    ) -> dict[str, Any]:
        """删除费用订单"""
        return await self._post(
            "/pb/openapi/finance/fee/order/delete",
            data={"sid": sid, "order_id": order_id, **kwargs}
        )

    async def discard_fee_order(
        self, sid: int, order_id: str, **kwargs
    ) -> dict[str, Any]:
        """作废费用订单"""
        return await self._post(
            "/pb/openapi/finance/fee/order/discard",
            data={"sid": sid, "order_id": order_id, **kwargs}
        )

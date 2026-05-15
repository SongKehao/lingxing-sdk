"""多平台其他 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class MultiplatformOtherEndpoints(BaseEndpoint):
    """领星多平台其他 API (3个接口)."""

    async def batch_review(self, **kwargs) -> dict:
        """审核发货.

POST /basicOpen/openapi/multiplatform/order/review

Args:
    global_order_no: 系统单号列表 (required), array."""
        resp = await self._post("/basicOpen/openapi/multiplatform/order/review", kwargs if kwargs else None)
        return resp.data or {}
    async def pre_shipment(self, **kwargs) -> list | dict:
        """预发货.

POST /basicOpen/openapi/multiplatform/order/preShipment

Args:
    global_order_no: 系统单号列表 (required), array."""
        resp = await self._post("/basicOpen/openapi/multiplatform/order/preShipment", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_comment_list(self, **kwargs) -> list | dict:
        """查询Walmart Review列表.

POST /basicOpen/multiplatform/walmart/queryCommentList

Args:
    endDate: 结束日期 (required), string.
    pageNum: 页码, int.
    pageSize: 每页大小, int.
    ratings: 评分列表, array.
    searchDateField: 搜索日期字段, string.
    searchField: 搜索字段, string.
    searchValue: 搜索值列表, array.
    startDate: 开始日期 (required), string.
    storeIds: 店铺ID列表, array."""
        resp = await self._post("/basicOpen/multiplatform/walmart/queryCommentList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

"""多平台其他 API endpoints."""

from __future__ import annotations

from ..models.responses.multi_platform import (
    MultiplatformOrderPreshipmentResponse,
    MultiplatformOrderReviewResponse,
    MultiplatformWalmartQuerycommentlistResponse,
)
from ._base import BaseEndpoint


class MultiplatformOtherEndpoints(BaseEndpoint):
    """领星多平台其他 API (3个接口)."""

    async def batch_review(self, global_order_no: list = None) -> MultiplatformOrderReviewResponse | None:
        """审核发货.

        POST /basicOpen/openapi/multiplatform/order/review

        Args:
            global_order_no: 系统单号列表 (required), array."""
        resp = await self._post(
            "/basicOpen/openapi/multiplatform/order/review",
            {k: v for k, v in {"global_order_no": global_order_no}.items() if v is not None},
        )
        return self._parse_one(resp.data, MultiplatformOrderReviewResponse)

    async def pre_shipment(self, global_order_no: list = None) -> list[MultiplatformOrderPreshipmentResponse]:
        """预发货.

        POST /basicOpen/openapi/multiplatform/order/preShipment

        Args:
            global_order_no: 系统单号列表 (required), array."""
        resp = await self._post(
            "/basicOpen/openapi/multiplatform/order/preShipment",
            {k: v for k, v in {"global_order_no": global_order_no}.items() if v is not None},
        )
        return self._parse_list(resp.data, MultiplatformOrderPreshipmentResponse)

    async def walmart_comment_list(
        self,
        endDate: str = None,
        pageNum: int = None,
        pageSize: int = None,
        ratings: list = None,
        searchDateField: str = None,
        searchField: str = None,
        searchValue: list = None,
        startDate: str = None,
        storeIds: list = None,
    ) -> list[MultiplatformWalmartQuerycommentlistResponse]:
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
        resp = await self._post(
            "/basicOpen/multiplatform/walmart/queryCommentList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "ratings": ratings,
                    "searchDateField": searchDateField,
                    "searchField": searchField,
                    "searchValue": searchValue,
                    "startDate": startDate,
                    "storeIds": storeIds,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformWalmartQuerycommentlistResponse)

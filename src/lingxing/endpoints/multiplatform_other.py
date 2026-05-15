"""多平台其他 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class MultiplatformOtherEndpoints(BaseEndpoint):
    """领星多平台其他 API (3个接口)."""

    async def batch_review(self, **kwargs) -> list | dict:
        """BatchReview. POST /basicOpen/openapi/multiplatform/order/review"""
        resp = await self._post("/basicOpen/openapi/multiplatform/order/review", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def pre_shipment(self, **kwargs) -> list | dict:
        """PreShipment. POST /basicOpen/openapi/multiplatform/order/preShipment"""
        resp = await self._post("/basicOpen/openapi/multiplatform/order/preShipment", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_comment_list(self, **kwargs) -> list | dict:
        """WalmartCommentList. POST /basicOpen/multiplatform/walmart/queryCommentList"""
        resp = await self._post("/basicOpen/multiplatform/walmart/queryCommentList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

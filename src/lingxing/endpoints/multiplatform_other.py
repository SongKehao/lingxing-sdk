"""Auto-generated MultiplatformOtherEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class MultiplatformOtherEndpoints:
    """领星API - MultiplatformOtherEndpoints (3个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def batch_review(self, **kwargs) -> dict:
        """BatchReview.
        
        POST /basicOpen/openapi/multiplatform/order/review
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/multiplatform/order/review",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def pre_shipment(self, **kwargs) -> dict:
        """PreShipment.
        
        POST /basicOpen/openapi/multiplatform/order/preShipment
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/multiplatform/order/preShipment",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_comment_list(self, **kwargs) -> dict:
        """WalmartCommentList.
        
        POST /basicOpen/multiplatform/walmart/queryCommentList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/walmart/queryCommentList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

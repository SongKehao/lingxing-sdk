"""Auto-generated RestockingLimitEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class RestockingLimitEndpoints:
    """领星API - RestockingLimitEndpoints (2个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def get_ipi_info(self, **kwargs) -> dict:
        """GetIpiInfo.
        
        POST /erp/sc/routing/fbaLimit/restock/getIpiInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaLimit/restock/getIpiInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def replenishment_restriction_list(self, **kwargs) -> dict:
        """replenishmentRestrictionList.
        
        POST /basicOpen/openapi/replenishmentRestriction/page/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/replenishmentRestriction/page/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

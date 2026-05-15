"""FBA库存限制 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class RestockingLimitEndpoints(BaseEndpoint):
    """领星FBA库存限制 API (2个接口)."""

    async def get_ipi_info(self, **kwargs) -> list | dict:
        """GetIpiInfo. POST /erp/sc/routing/fbaLimit/restock/getIpiInfo"""
        resp = await self._post("/erp/sc/routing/fbaLimit/restock/getIpiInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def replenishment_restriction_list(self, **kwargs) -> list | dict:
        """replenishmentRestrictionList. POST /basicOpen/openapi/replenishmentRestriction/page/list"""
        resp = await self._post("/basicOpen/openapi/replenishmentRestriction/page/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

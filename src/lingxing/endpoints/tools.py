"""Auto-generated ToolsEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class ToolsEndpoints:
    """领星API - ToolsEndpoints (4个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def competitive_monitor_list(self, **kwargs) -> dict:
        """CompetitiveMonitorList.
        
        POST /basicOpen/tool/competitiveMonitor/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/tool/competitiveMonitor/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_keyword_list(self, **kwargs) -> dict:
        """GetKeywordList.
        
        POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/tool/toolKeywordRank/getKeywordList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warning_message_goods_list(self, **kwargs) -> dict:
        """warningMessageGoodsList.
        
        POST /basicOpen/settings/warningMessage/goodsList
        """
        return await self._request_with_token(
            route_name="/basicOpen/settings/warningMessage/goodsList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warning_message_inventory_list(self, **kwargs) -> dict:
        """warningMessageInventoryList.
        
        POST /basicOpen/settings/warningMessage/inventoryList
        """
        return await self._request_with_token(
            route_name="/basicOpen/settings/warningMessage/inventoryList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

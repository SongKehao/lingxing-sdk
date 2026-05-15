"""工具 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class ToolsEndpoints(BaseEndpoint):
    """领星工具 API (4个接口)."""

    async def competitive_monitor_list(self, **kwargs) -> list | dict:
        """CompetitiveMonitorList. POST /basicOpen/tool/competitiveMonitor/list"""
        resp = await self._post("/basicOpen/tool/competitiveMonitor/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_keyword_list(self, **kwargs) -> list | dict:
        """GetKeywordList. POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList"""
        resp = await self._post("/erp/sc/routing/tool/toolKeywordRank/getKeywordList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warning_message_goods_list(self, **kwargs) -> list | dict:
        """warningMessageGoodsList. POST /basicOpen/settings/warningMessage/goodsList"""
        resp = await self._post("/basicOpen/settings/warningMessage/goodsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warning_message_inventory_list(self, **kwargs) -> list | dict:
        """warningMessageInventoryList. POST /basicOpen/settings/warningMessage/inventoryList"""
        resp = await self._post("/basicOpen/settings/warningMessage/inventoryList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

"""物流 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class LogisticsEndpoints(BaseEndpoint):
    """领星物流 API (5个接口)."""

    async def add_channels(self, **kwargs) -> list | dict:
        """AddChannels. POST /erp/sc/routing/tms/FirstVessel/addChannels"""
        resp = await self._post("/erp/sc/routing/tms/FirstVessel/addChannels", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_providers(self, **kwargs) -> list | dict:
        """AddProviders. POST /erp/sc/routing/tms/FirstVessel/addProviders"""
        resp = await self._post("/erp/sc/routing/tms/FirstVessel/addProviders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def channel_list(self, **kwargs) -> list | dict:
        """ChannelList. POST /erp/sc/data/local_inventory/channelList"""
        resp = await self._post("/erp/sc/data/local_inventory/channelList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_head_logistics_provider(self, **kwargs) -> list | dict:
        """QueryHeadLogisticsProvider. POST /basicOpen/logistics/headLogisticsProvider/query/list"""
        resp = await self._post("/basicOpen/logistics/headLogisticsProvider/query/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def transport_method_list(self, **kwargs) -> list | dict:
        """transportMethodList. POST /basicOpen/businessConfig/transportMethod/list"""
        resp = await self._post("/basicOpen/businessConfig/transportMethod/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

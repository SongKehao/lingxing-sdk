"""Auto-generated LogisticsEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class LogisticsEndpoints:
    """领星API - LogisticsEndpoints (5个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def add_channels(self, **kwargs) -> dict:
        """AddChannels.
        
        POST /erp/sc/routing/tms/FirstVessel/addChannels
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/tms/FirstVessel/addChannels",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_providers(self, **kwargs) -> dict:
        """AddProviders.
        
        POST /erp/sc/routing/tms/FirstVessel/addProviders
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/tms/FirstVessel/addProviders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def channel_list(self, **kwargs) -> dict:
        """ChannelList.
        
        POST /erp/sc/data/local_inventory/channelList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/local_inventory/channelList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def query_head_logistics_provider(self, **kwargs) -> dict:
        """QueryHeadLogisticsProvider.
        
        POST /basicOpen/logistics/headLogisticsProvider/query/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/logistics/headLogisticsProvider/query/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def transport_method_list(self, **kwargs) -> dict:
        """transportMethodList.
        
        POST /basicOpen/businessConfig/transportMethod/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/businessConfig/transportMethod/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

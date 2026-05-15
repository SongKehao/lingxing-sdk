"""Auto-generated RestockingEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class RestockingEndpoints:
    """领星API - RestockingEndpoints (13个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def config_asin(self, **kwargs) -> dict:
        """ConfigASIN.
        
        POST /erp/sc/routing/fbaSug/asin/getConfig
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/getConfig",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def config_msku(self, **kwargs) -> dict:
        """ConfigMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/getConfig
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/getConfig",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def daily_sales_info_feature_asin(self, **kwargs) -> dict:
        """DailySalesInfoFeatureASIN.
        
        POST /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def daily_sales_info_feature_msku(self, **kwargs) -> dict:
        """DailySalesInfoFeatureMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_summary_list(self, **kwargs) -> dict:
        """GetSummaryList.
        
        POST /erp/sc/routing/restocking/analysis/getSummaryList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def info_asin(self, **kwargs) -> dict:
        """InfoASIN.
        
        POST /erp/sc/routing/fbaSug/asin/getInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/getInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def info_msku(self, **kwargs) -> dict:
        """InfoMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/getInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/getInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_config_asin(self, **kwargs) -> dict:
        """SetConfigASIN.
        
        POST /erp/sc/routing/fbaSug/asin/setConfig
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/setConfig",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_config_msku(self, **kwargs) -> dict:
        """SetConfigMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/setConfig
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/setConfig",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_configs_asin(self, **kwargs) -> dict:
        """SetConfigsASIN.
        
        POST /erp/sc/routing/fbaSug/asin/setConfigs
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/setConfigs",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_configs_msku(self, **kwargs) -> dict:
        """SetConfigsMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/setConfigs
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/setConfigs",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def source_list_asin(self, **kwargs) -> dict:
        """SourceListASIN.
        
        POST /erp/sc/routing/fbaSug/asin/getSourceList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/asin/getSourceList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def source_list_msku(self, **kwargs) -> dict:
        """SourceListMSKU.
        
        POST /erp/sc/routing/fbaSug/msku/getSourceList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fbaSug/msku/getSourceList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

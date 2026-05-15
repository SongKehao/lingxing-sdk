"""FBA补货建议 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class RestockingEndpoints(BaseEndpoint):
    """领星FBA补货建议 API (13个接口)."""

    async def config_asin(self, **kwargs) -> list | dict:
        """ConfigASIN. POST /erp/sc/routing/fbaSug/asin/getConfig"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/getConfig", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def config_msku(self, **kwargs) -> list | dict:
        """ConfigMSKU. POST /erp/sc/routing/fbaSug/msku/getConfig"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/getConfig", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def daily_sales_info_feature_asin(self, **kwargs) -> list | dict:
        """DailySalesInfoFeatureASIN. POST /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def daily_sales_info_feature_msku(self, **kwargs) -> list | dict:
        """DailySalesInfoFeatureMSKU. POST /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_summary_list(self, **kwargs) -> list | dict:
        """GetSummaryList. POST /erp/sc/routing/restocking/analysis/getSummaryList"""
        resp = await self._post("/erp/sc/routing/restocking/analysis/getSummaryList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def info_asin(self, **kwargs) -> list | dict:
        """InfoASIN. POST /erp/sc/routing/fbaSug/asin/getInfo"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/getInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def info_msku(self, **kwargs) -> list | dict:
        """InfoMSKU. POST /erp/sc/routing/fbaSug/msku/getInfo"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/getInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_config_asin(self, **kwargs) -> list | dict:
        """SetConfigASIN. POST /erp/sc/routing/fbaSug/asin/setConfig"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/setConfig", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_config_msku(self, **kwargs) -> list | dict:
        """SetConfigMSKU. POST /erp/sc/routing/fbaSug/msku/setConfig"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/setConfig", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_configs_asin(self, **kwargs) -> list | dict:
        """SetConfigsASIN. POST /erp/sc/routing/fbaSug/asin/setConfigs"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/setConfigs", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_configs_msku(self, **kwargs) -> list | dict:
        """SetConfigsMSKU. POST /erp/sc/routing/fbaSug/msku/setConfigs"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/setConfigs", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def source_list_asin(self, **kwargs) -> list | dict:
        """SourceListASIN. POST /erp/sc/routing/fbaSug/asin/getSourceList"""
        resp = await self._post("/erp/sc/routing/fbaSug/asin/getSourceList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def source_list_msku(self, **kwargs) -> list | dict:
        """SourceListMSKU. POST /erp/sc/routing/fbaSug/msku/getSourceList"""
        resp = await self._post("/erp/sc/routing/fbaSug/msku/getSourceList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

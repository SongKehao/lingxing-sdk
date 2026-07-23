"""物流 API endpoints."""
from __future__ import annotations

from ..models.responses.logistics import (
    WmsLogisticsListUsedLogisticsTypeResponse,
    LogisticsHeadReconciliationListResponse,
    LogisticsBillConfirmResponse,
    BusinessconfigTransportmethodListResponse,
    HeadlogisticsproviderQueryListResponse,
    LocalInventoryChannellistResponse,
    TmsFirstvesselAddchannelsResponse,
    TmsFirstvesselAddprovidersResponse,
)

from typing import Any

from ._base import BaseEndpoint


class LogisticsEndpoints(BaseEndpoint):
    """领星物流 API (5个接口)."""

    async def used_logistics_type(self, data: dict = None) -> list[WmsLogisticsListUsedLogisticsTypeResponse]:
        """查询已启用的自发货物流方式.

POST /erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType", data or {})
        return self._parse_list(resp.data, WmsLogisticsListUsedLogisticsTypeResponse)

    async def head_reconciliation_list(self, offset: int = None, length: int = None, search_field_time: str = None, search_field: str = None, search_value: str = None, shipping_method_ids: list = None) -> list[LogisticsHeadReconciliationListResponse]:
        """头程对账列表.

POST /basicOpen/logistics/headLogisticsReconciliation/list

Args:
    offset: see API doc.
    length: see API doc.
    search_field_time: see API doc.
    search_field: see API doc.
    search_value: see API doc.
    shipping_method_ids: see API doc."""
        resp = await self._post("/basicOpen/logistics/headLogisticsReconciliation/list", {k: v for k, v in {"offset": offset, "length": length, "searchFieldTime": search_field_time, "searchField": search_field, "searchValue": search_value, "shippingMethodIds": shipping_method_ids}.items() if v is not None})
        return self._parse_list(resp.data, LogisticsHeadReconciliationListResponse)

    async def logistics_bill_confirm(self, data: dict = None) -> list[LogisticsBillConfirmResponse]:
        """FBM物流对账-确认/批量确认.

POST /basicOpen/logistics/logisticsBill/confirm

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/logistics/logisticsBill/confirm", data or {})
        return self._parse_list(resp.data, LogisticsBillConfirmResponse)

    async def add_channels(self, channelsData: list = None) -> TmsFirstvesselAddchannelsResponse | None:
        """批量添加头程物流方式.

POST /erp/sc/routing/tms/FirstVessel/addChannels

Args:
    channelsData: 头程物流方式数据，每次请求限制20条 (required), array."""
        resp = await self._post("/erp/sc/routing/tms/FirstVessel/addChannels", {k: v for k, v in {"channelsData": channelsData}.items() if v is not None})
        return self._parse_one(resp.data, TmsFirstvesselAddchannelsResponse)
    async def add_providers(self, providersData: list = None) -> TmsFirstvesselAddprovidersResponse | None:
        """批量添加头程物流商.

POST /erp/sc/routing/tms/FirstVessel/addProviders

Args:
    providersData: 物流商数据，限制20条 (required), array."""
        resp = await self._post("/erp/sc/routing/tms/FirstVessel/addProviders", {k: v for k, v in {"providersData": providersData}.items() if v is not None})
        return self._parse_one(resp.data, TmsFirstvesselAddprovidersResponse)
    async def channel_list(self, offset: int = None, length: int = None) -> list[LocalInventoryChannellistResponse]:
        """查询头程物流渠道列表.

POST /erp/sc/data/local_inventory/channelList

Args:
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int."""
        resp = await self._post("/erp/sc/data/local_inventory/channelList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryChannellistResponse)
    async def query_head_logistics_provider(self, search: Any = None) -> list[HeadlogisticsproviderQueryListResponse]:
        """查询物流-头程物流商.

POST /basicOpen/logistics/headLogisticsProvider/query/list

Args:
    search: 搜索参数对象, object."""
        resp = await self._post("/basicOpen/logistics/headLogisticsProvider/query/list", {k: v for k, v in {"search": search}.items() if v is not None})
        return self._parse_list(resp.data, HeadlogisticsproviderQueryListResponse)
    async def transport_method_list(self, **kwargs) -> list[BusinessconfigTransportmethodListResponse]:
        """查询运输方式列表.

POST /basicOpen/businessConfig/transportMethod/list"""
        resp = await self._post("/basicOpen/businessConfig/transportMethod/list", kwargs if kwargs else None)
        return self._parse_list(resp.data, BusinessconfigTransportmethodListResponse)

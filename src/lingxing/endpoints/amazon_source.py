"""亚马逊原始数据 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class AmazonSourceEndpoints(BaseEndpoint):
    """领星亚马逊原始数据 API (20个接口)."""

    async def adjustment_list(self, **kwargs) -> list | dict:
        """AdjustmentList. POST /basicOpen/openapi/mwsReport/adjustmentList"""
        resp = await self._post("/basicOpen/openapi/mwsReport/adjustmentList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def afn_fulfillable_quantity(self, **kwargs) -> list | dict:
        """AfnFulfillableQuantity. POST /erp/sc/data/mws_report/getAfnFulfillableQuantity"""
        resp = await self._post("/erp/sc/data/mws_report/getAfnFulfillableQuantity", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def all_orders(self, **kwargs) -> list | dict:
        """AllOrders. POST /erp/sc/data/mws_report/allOrders"""
        resp = await self._post("/erp/sc/data/mws_report/allOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def daily_inventory(self, **kwargs) -> list | dict:
        """DailyInventory. POST /erp/sc/data/mws_report/dailyInventory"""
        resp = await self._post("/erp/sc/data/mws_report/dailyInventory", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_orders(self, **kwargs) -> list | dict:
        """FbaOrders. POST /erp/sc/data/mws_report/fbaOrders"""
        resp = await self._post("/erp/sc/data/mws_report/fbaOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def manage_inventory(self, **kwargs) -> list | dict:
        """ManageInventory. POST /erp/sc/data/mws_report/manageInventory"""
        resp = await self._post("/erp/sc/data/mws_report/manageInventory", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def refund_orders(self, **kwargs) -> list | dict:
        """RefundOrders. POST /erp/sc/data/mws_report/refundOrders"""
        resp = await self._post("/erp/sc/data/mws_report/refundOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def removal_lists(self, **kwargs) -> list | dict:
        """RemovalLists. POST /erp/sc/data/fba_report/removalLists"""
        resp = await self._post("/erp/sc/data/fba_report/removalLists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def removal_order_list_new(self, **kwargs) -> list | dict:
        """RemovalOrderListNew. POST /erp/sc/routing/data/order/removalOrderListNew"""
        resp = await self._post("/erp/sc/routing/data/order/removalOrderListNew", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def removal_shipment_list(self, **kwargs) -> list | dict:
        """RemovalShipmentList. POST /erp/sc/statistic/removalShipment/list"""
        resp = await self._post("/erp/sc/statistic/removalShipment/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def reserved_inventory(self, **kwargs) -> list | dict:
        """ReservedInventory. POST /erp/sc/data/mws_report/reservedInventory"""
        resp = await self._post("/erp/sc/data/mws_report/reservedInventory", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def source_removal_orders(self, **kwargs) -> list | dict:
        """SourceRemovalOrders. POST /erp/sc/data/mws_report/removalOrders"""
        resp = await self._post("/erp/sc/data/mws_report/removalOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def transaction(self, **kwargs) -> list | dict:
        """Transaction. POST /erp/sc/data/mws_report/transaction"""
        resp = await self._post("/erp/sc/data/mws_report/transaction", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_exchange_order_list(self, **kwargs) -> list | dict:
        """fbaExchangeOrderList. POST /erp/sc/routing/data/order/fbaExchangeOrderList"""
        resp = await self._post("/erp/sc/routing/data/order/fbaExchangeOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbm_return_order_list(self, **kwargs) -> list | dict:
        """fbmReturnOrderList. POST /erp/sc/routing/data/order/fbmReturnOrderList"""
        resp = await self._post("/erp/sc/routing/data/order/fbmReturnOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_amazon_fulfilled_shipments_list(self, **kwargs) -> list | dict:
        """getAmazonFulfilledShipmentsList. POST /erp/sc/data/mws_report/getAmazonFulfilledShipmentsList"""
        resp = await self._post("/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_fba_age_list(self, **kwargs) -> list | dict:
        """getFbaAgeList. POST /erp/sc/routing/fba/fbaStock/getFbaAgeList"""
        resp = await self._post("/erp/sc/routing/fba/fbaStock/getFbaAgeList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_fba_inventory_event_detail_list(self, **kwargs) -> list | dict:
        """getFbaInventoryEventDetailList. POST /erp/sc/data/mws_report/getFbaInventoryEventDetailList"""
        resp = await self._post("/erp/sc/data/mws_report/getFbaInventoryEventDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def v1get_amazon_fulfilled_shipments_list(self, **kwargs) -> list | dict:
        """v1getAmazonFulfilledShipmentsList. POST /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList"""
        resp = await self._post("/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def v1get_fba_inventory_event_detail_list(self, **kwargs) -> list | dict:
        """v1getFbaInventoryEventDetailList. POST /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList"""
        resp = await self._post("/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

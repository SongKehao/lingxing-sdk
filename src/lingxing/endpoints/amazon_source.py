"""Auto-generated AmazonSourceEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class AmazonSourceEndpoints:
    """领星API - AmazonSourceEndpoints (20个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def adjustment_list(self, **kwargs) -> dict:
        """AdjustmentList.
        
        POST /basicOpen/openapi/mwsReport/adjustmentList
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/mwsReport/adjustmentList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def afn_fulfillable_quantity(self, **kwargs) -> dict:
        """AfnFulfillableQuantity.
        
        POST /erp/sc/data/mws_report/getAfnFulfillableQuantity
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/getAfnFulfillableQuantity",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def all_orders(self, **kwargs) -> dict:
        """AllOrders.
        
        POST /erp/sc/data/mws_report/allOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/allOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def daily_inventory(self, **kwargs) -> dict:
        """DailyInventory.
        
        POST /erp/sc/data/mws_report/dailyInventory
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/dailyInventory",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fba_orders(self, **kwargs) -> dict:
        """FbaOrders.
        
        POST /erp/sc/data/mws_report/fbaOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/fbaOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def manage_inventory(self, **kwargs) -> dict:
        """ManageInventory.
        
        POST /erp/sc/data/mws_report/manageInventory
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/manageInventory",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def refund_orders(self, **kwargs) -> dict:
        """RefundOrders.
        
        POST /erp/sc/data/mws_report/refundOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/refundOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def removal_lists(self, **kwargs) -> dict:
        """RemovalLists.
        
        POST /erp/sc/data/fba_report/removalLists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/removalLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def removal_order_list_new(self, **kwargs) -> dict:
        """RemovalOrderListNew.
        
        POST /erp/sc/routing/data/order/removalOrderListNew
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/order/removalOrderListNew",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def removal_shipment_list(self, **kwargs) -> dict:
        """RemovalShipmentList.
        
        POST /erp/sc/statistic/removalShipment/list
        """
        return await self._request_with_token(
            route_name="/erp/sc/statistic/removalShipment/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def reserved_inventory(self, **kwargs) -> dict:
        """ReservedInventory.
        
        POST /erp/sc/data/mws_report/reservedInventory
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/reservedInventory",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def source_removal_orders(self, **kwargs) -> dict:
        """SourceRemovalOrders.
        
        POST /erp/sc/data/mws_report/removalOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/removalOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def transaction(self, **kwargs) -> dict:
        """Transaction.
        
        POST /erp/sc/data/mws_report/transaction
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/transaction",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fba_exchange_order_list(self, **kwargs) -> dict:
        """fbaExchangeOrderList.
        
        POST /erp/sc/routing/data/order/fbaExchangeOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/order/fbaExchangeOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbm_return_order_list(self, **kwargs) -> dict:
        """fbmReturnOrderList.
        
        POST /erp/sc/routing/data/order/fbmReturnOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/order/fbmReturnOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_amazon_fulfilled_shipments_list(self, **kwargs) -> dict:
        """getAmazonFulfilledShipmentsList.
        
        POST /erp/sc/data/mws_report/getAmazonFulfilledShipmentsList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_fba_age_list(self, **kwargs) -> dict:
        """getFbaAgeList.
        
        POST /erp/sc/routing/fba/fbaStock/getFbaAgeList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/fbaStock/getFbaAgeList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_fba_inventory_event_detail_list(self, **kwargs) -> dict:
        """getFbaInventoryEventDetailList.
        
        POST /erp/sc/data/mws_report/getFbaInventoryEventDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report/getFbaInventoryEventDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def v1get_amazon_fulfilled_shipments_list(self, **kwargs) -> dict:
        """v1getAmazonFulfilledShipmentsList.
        
        POST /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def v1get_fba_inventory_event_detail_list(self, **kwargs) -> dict:
        """v1getFbaInventoryEventDetailList.
        
        POST /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

"""Auto-generated PurchaseEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class PurchaseEndpoints:
    """领星API - PurchaseEndpoints (19个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def cancel(self, **kwargs) -> dict:
        """Cancel.
        
        POST /erp/sc/routing/purchase/purchase/cancel
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase/cancel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def cancel_purchase_return_order(self, **kwargs) -> dict:
        """CancelPurchaseReturnOrder.
        
        POST /basicOpen/purchase/cancelPurchaseReturnOrder
        """
        return await self._request_with_token(
            route_name="/basicOpen/purchase/cancelPurchaseReturnOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_purchase_order(self, **kwargs) -> dict:
        """CreatePurchaseOrder.
        
        POST /erp/sc/routing/purchase/purchase/createPurchaseOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase/createPurchaseOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def order_modify_remark(self, **kwargs) -> dict:
        """OrderModifyRemark.
        
        POST /basicOpen/purchase/orderModifyRemark
        """
        return await self._request_with_token(
            route_name="/basicOpen/purchase/orderModifyRemark",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_order_list(self, **kwargs) -> dict:
        """PurchaseOrderList.
        
        POST /erp/sc/routing/data/local_inventory/purchaseOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/purchaseOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_plan_cancel(self, **kwargs) -> dict:
        """PurchasePlanCancel.
        
        POST /basicOpen/purchase/planCancel
        """
        return await self._request_with_token(
            route_name="/basicOpen/purchase/planCancel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_orders(self, **kwargs) -> dict:
        """SetOrders.
        
        POST /erp/sc/routing/purchase/purchase/setOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase/setOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def supplier(self, **kwargs) -> dict:
        """Supplier.
        
        POST /erp/sc/data/local_inventory/supplier
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/local_inventory/supplier",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def supplier_edit(self, **kwargs) -> dict:
        """SupplierEdit.
        
        POST /erp/sc/routing/storage/supplier/edit
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/supplier/edit",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_logistics(self, **kwargs) -> dict:
        """addLogistics.
        
        POST /erp/sc/routing/purchase/purchase/addLogistics
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase/addLogistics",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def change_order_list(self, **kwargs) -> dict:
        """changeOrderList.
        
        POST /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_purchase_change_order(self, **kwargs) -> dict:
        """createPurchaseChangeOrder.
        
        POST /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_purchase_plan(self, **kwargs) -> dict:
        """createPurchasePlan.
        
        POST /erp/sc/routing/data/local_inventory/createPurchasePlan
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/createPurchasePlan",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_purchase_return_order(self, **kwargs) -> dict:
        """createPurchaseReturnOrder.
        
        POST /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_orders(self, **kwargs) -> dict:
        """getOrders.
        
        POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_purchase_plans(self, **kwargs) -> dict:
        """getPurchasePlans.
        
        POST /erp/sc/routing/data/local_inventory/getPurchasePlans
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/getPurchasePlans",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_purchase_return_order_list(self, **kwargs) -> dict:
        """getPurchaseReturnOrderList.
        
        POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchaser_lists(self, **kwargs) -> dict:
        """purchaserLists.
        
        POST /erp/sc/routing/data/purchaser/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/purchaser/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_order_finish(self, **kwargs) -> dict:
        """setOrderFinish.
        
        POST /basicOpen/purchase/setOrderFinish
        """
        return await self._request_with_token(
            route_name="/basicOpen/purchase/setOrderFinish",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

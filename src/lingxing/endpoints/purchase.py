"""采购 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint
from ..models.purchase import GetPurchasePlansItem, PurchaseOrderListItem, PurchaserListsItem, SupplierItem

class PurchaseEndpoints(BaseEndpoint):
    """领星采购 API (19个接口)."""

    async def cancel(self, **kwargs) -> dict:
        """写操作 Cancel. POST /erp/sc/routing/purchase/purchase/cancel"""
        resp = await self._post("/erp/sc/routing/purchase/purchase/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_purchase_return_order(self, **kwargs) -> dict:
        """写操作 CancelPurchaseReturnOrder. POST /basicOpen/purchase/cancelPurchaseReturnOrder"""
        resp = await self._post("/basicOpen/purchase/cancelPurchaseReturnOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_order(self, **kwargs) -> dict:
        """写操作 CreatePurchaseOrder. POST /erp/sc/routing/purchase/purchase/createPurchaseOrder"""
        resp = await self._post("/erp/sc/routing/purchase/purchase/createPurchaseOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def order_modify_remark(self, **kwargs) -> list | dict:
        """OrderModifyRemark. POST /basicOpen/purchase/orderModifyRemark"""
        resp = await self._post("/basicOpen/purchase/orderModifyRemark", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_order_list(self, **kwargs) -> list[PurchaseOrderListItem]:
        """PurchaseOrderList. POST /erp/sc/routing/data/local_inventory/purchaseOrderList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/purchaseOrderList", kwargs if kwargs else None)
        return self._parse_list(resp.data, PurchaseOrderListItem)
    async def purchase_plan_cancel(self, **kwargs) -> dict:
        """写操作 PurchasePlanCancel. POST /basicOpen/purchase/planCancel"""
        resp = await self._post("/basicOpen/purchase/planCancel", kwargs if kwargs else None)
        return resp.data or {}
    async def set_orders(self, **kwargs) -> list | dict:
        """SetOrders. POST /erp/sc/routing/purchase/purchase/setOrders"""
        resp = await self._post("/erp/sc/routing/purchase/purchase/setOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def supplier(self, **kwargs) -> list[SupplierItem]:
        """Supplier. POST /erp/sc/data/local_inventory/supplier"""
        resp = await self._post("/erp/sc/data/local_inventory/supplier", kwargs if kwargs else None)
        return self._parse_list(resp.data, SupplierItem)
    async def supplier_edit(self, **kwargs) -> dict:
        """写操作 SupplierEdit. POST /erp/sc/routing/storage/supplier/edit"""
        resp = await self._post("/erp/sc/routing/storage/supplier/edit", kwargs if kwargs else None)
        return resp.data or {}
    async def add_logistics(self, **kwargs) -> dict:
        """写操作 addLogistics. POST /erp/sc/routing/purchase/purchase/addLogistics"""
        resp = await self._post("/erp/sc/routing/purchase/purchase/addLogistics", kwargs if kwargs else None)
        return resp.data or {}
    async def change_order_list(self, **kwargs) -> list | dict:
        """changeOrderList. POST /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList"""
        resp = await self._post("/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_purchase_change_order(self, **kwargs) -> dict:
        """写操作 createPurchaseChangeOrder. POST /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder"""
        resp = await self._post("/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_plan(self, **kwargs) -> dict:
        """写操作 createPurchasePlan. POST /erp/sc/routing/data/local_inventory/createPurchasePlan"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/createPurchasePlan", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_return_order(self, **kwargs) -> dict:
        """写操作 createPurchaseReturnOrder. POST /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder"""
        resp = await self._post("/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_orders(self, **kwargs) -> list | dict:
        """getOrders. POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders"""
        resp = await self._post("/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_purchase_plans(self, **kwargs) -> list[GetPurchasePlansItem]:
        """getPurchasePlans. POST /erp/sc/routing/data/local_inventory/getPurchasePlans"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getPurchasePlans", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetPurchasePlansItem)
    async def get_purchase_return_order_list(self, **kwargs) -> list | dict:
        """getPurchaseReturnOrderList. POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList"""
        resp = await self._post("/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchaser_lists(self, **kwargs) -> tuple[list[PurchaserListsItem], int]:
        """purchaserLists（分页）. POST /erp/sc/routing/data/purchaser/lists"""
        resp = await self._post("/erp/sc/routing/data/purchaser/lists", kwargs if kwargs else None)
        return self._parse_page(resp.data, PurchaserListsItem)
    async def set_order_finish(self, **kwargs) -> list | dict:
        """setOrderFinish. POST /basicOpen/purchase/setOrderFinish"""
        resp = await self._post("/basicOpen/purchase/setOrderFinish", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

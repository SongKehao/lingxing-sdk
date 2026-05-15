"""Auto-generated WarehouseEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class WarehouseEndpoints:
    """领星API - WarehouseEndpoints (76个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def add_allocation_order(self, **kwargs) -> dict:
        """AddAllocationOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def adjust_order_confirm(self, **kwargs) -> dict:
        """AdjustOrderConfirm.
        
        POST /basicOpen/adjustOrder/adjust/setAdjust
        """
        return await self._request_with_token(
            route_name="/basicOpen/adjustOrder/adjust/setAdjust",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def cancel_storage_allocation_list(self, **kwargs) -> dict:
        """CancelStorageAllocationList.
        
        POST /basicOpen/storageAllocationList/cancel
        """
        return await self._request_with_token(
            route_name="/basicOpen/storageAllocationList/cancel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_inbound(self, **kwargs) -> dict:
        """CreateInbound.
        
        POST /erp/sc/routing/owms/inbound/createInbound
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/createInbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def delete_fba_shipment_list(self, **kwargs) -> dict:
        """DeleteFbaShipmentList.
        
        POST /basicOpen/openapi/fbaShipment/deleteShipmentList
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/fbaShipment/deleteShipmentList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def delete_over_sea_stock_order(self, **kwargs) -> dict:
        """DeleteOverSeaStockOrder.
        
        POST /basicOpen/overSeaWarehouse/stockOrder/delete
        """
        return await self._request_with_token(
            route_name="/basicOpen/overSeaWarehouse/stockOrder/delete",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def delete_storage_allocation_list(self, **kwargs) -> dict:
        """DeleteStorageAllocationList.
        
        POST /basicOpen/storageAllocationList/delete
        """
        return await self._request_with_token(
            route_name="/basicOpen/storageAllocationList/delete",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def edit_warehouse(self, **kwargs) -> dict:
        """EditWarehouse.
        
        POST /erp/sc/storage/wareHouse/edit
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/wareHouse/edit",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbastock(self, **kwargs) -> dict:
        """FBAStock.
        
        POST /erp/sc/routing/fba/fbaStock/fbaList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/fbaStock/fbaList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbastock_v2(self, **kwargs) -> dict:
        """FBAStock_v2.
        
        POST /basicOpen/openapi/storage/fbaWarehouseDetail
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/storage/fbaWarehouseDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fast_receive(self, **kwargs) -> dict:
        """FastReceive.
        
        POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_adjust_order_confirm_result(self, **kwargs) -> dict:
        """GetAdjustOrderConfirmResult.
        
        POST /basicOpen/adjustOrder/adjust/getAdjustStatus
        """
        return await self._request_with_token(
            route_name="/basicOpen/adjustOrder/adjust/getAdjustStatus",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_batch_detail_list(self, **kwargs) -> dict:
        """GetBatchDetailList.
        
        POST /erp/sc/routing/data/local_inventory/getBatchDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/getBatchDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_batch_statement_list(self, **kwargs) -> dict:
        """GetBatchStatementList.
        
        POST /erp/sc/routing/data/local_inventory/getBatchStatementList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/getBatchStatementList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_receive_good_records(self, **kwargs) -> dict:
        """GetReceiveGoodRecords.
        
        POST /erp/sc/routing/owms/inbound/getReceiveGoodRecords
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/getReceiveGoodRecords",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inbound_order_confirm(self, **kwargs) -> dict:
        """InboundOrderConfirm.
        
        POST /basicOpen/inboundOrder/inbound/setInbound
        """
        return await self._request_with_token(
            route_name="/basicOpen/inboundOrder/inbound/setInbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inventory_details(self, **kwargs) -> dict:
        """InventoryDetails.
        
        POST /erp/sc/routing/data/local_inventory/inventoryDetails
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/inventoryDetails",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def order_add(self, **kwargs) -> dict:
        """OrderAdd.
        
        POST /erp/sc/routing/storage/storage/orderAdd
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/storage/orderAdd",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def order_add_out(self, **kwargs) -> dict:
        """OrderAddOut.
        
        POST /erp/sc/routing/storage/storage/orderAddOut
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/storage/orderAddOut",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def outbound_order_confirm(self, **kwargs) -> dict:
        """OutboundOrderConfirm.
        
        POST /basicOpen/outboundOrder/outbound/setOutbound
        """
        return await self._request_with_token(
            route_name="/basicOpen/outboundOrder/outbound/setOutbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def over_seas_stock_detail(self, **kwargs) -> dict:
        """OverSeasStockDetail.
        
        POST /basicOpen/overSeaWarehouse/stockOrder/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/overSeaWarehouse/stockOrder/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def oversea_warehouse_match_list(self, **kwargs) -> dict:
        """OverseaWarehouseMatchList.
        
        POST /basicOpen/overseaWarehouseSetting/matchList
        """
        return await self._request_with_token(
            route_name="/basicOpen/overseaWarehouseSetting/matchList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def oversea_warehouse_product_match(self, **kwargs) -> dict:
        """OverseaWarehouseProductMatch.
        
        POST /basicOpen/overseaWarehouseSetting/productMatch
        """
        return await self._request_with_token(
            route_name="/basicOpen/overseaWarehouseSetting/productMatch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def oversea_warehouse_product_un_match(self, **kwargs) -> dict:
        """OverseaWarehouseProductUnMatch.
        
        POST /basicOpen/overseaWarehouseSetting/productUnMatch
        """
        return await self._request_with_token(
            route_name="/basicOpen/overseaWarehouseSetting/productUnMatch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_receipt_order_list(self, **kwargs) -> dict:
        """PurchaseReceiptOrderList.
        
        POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def receive(self, **kwargs) -> dict:
        """Receive.
        
        POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def send_inbound(self, **kwargs) -> dict:
        """SendInbound.
        
        POST /erp/sc/routing/owms/inbound/sendInbound
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/sendInbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_inbound_order_revoke(self, **kwargs) -> dict:
        """SetInboundOrderRevoke.
        
        POST /basicOpen/inboundOrder/inbound/setOrderRevoke
        """
        return await self._request_with_token(
            route_name="/basicOpen/inboundOrder/inbound/setOrderRevoke",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_outbound_order_revoke(self, **kwargs) -> dict:
        """SetOutboundOrderRevoke.
        
        POST /basicOpen/outboundOrder/outbound/setOrderRevoke
        """
        return await self._request_with_token(
            route_name="/basicOpen/outboundOrder/outbound/setOrderRevoke",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_logistics(self, **kwargs) -> dict:
        """UpdateLogistics.
        
        POST /erp/sc/routing/owms/inbound/updateLogistics
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/updateLogistics",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warehouse_lists(self, **kwargs) -> dict:
        """WarehouseLists.
        
        POST /erp/sc/data/local_inventory/warehouse
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/local_inventory/warehouse",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warehouse_statement(self, **kwargs) -> dict:
        """WarehouseStatement.
        
        POST /erp/sc/routing/data/local_inventory/wareHouseStatement
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/wareHouseStatement",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warehouse_statement_new(self, **kwargs) -> dict:
        """WarehouseStatementNew.
        
        POST /erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def wms_order_detail(self, **kwargs) -> dict:
        """WmsOrderDetail.
        
        POST /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers
        """
        return await self._request_with_token(
            route_name="/basicOpen/wmsOrder/getWmsOrdersByOrderNumbers",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def wms_order_list(self, **kwargs) -> dict:
        """WmsOrderList.
        
        POST /erp/sc/routing/wms/order/wmsOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/wms/order/wmsOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_adjustment_order(self, **kwargs) -> dict:
        """addAdjustmentOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_rebrand_adjustment_order(self, **kwargs) -> dict:
        """addRebrandAdjustmentOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_sku_adjustment_order(self, **kwargs) -> dict:
        """addSkuAdjustmentOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_storage_process_order(self, **kwargs) -> dict:
        """addStorageProcessOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def bin_create(self, **kwargs) -> dict:
        """binCreate.
        
        POST /erp/sc/routing/storage/wareHouseBin/create
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/wareHouseBin/create",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def cancel_wms_order(self, **kwargs) -> dict:
        """cancelWmsOrder.
        
        POST /basicOpen/wmsOrder/cancel
        """
        return await self._request_with_token(
            route_name="/basicOpen/wmsOrder/cancel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def check_add_order(self, **kwargs) -> dict:
        """checkAddOrder.
        
        POST /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def check_get_order_detail(self, **kwargs) -> dict:
        """checkGetOrderDetail.
        
        POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def check_get_order_list(self, **kwargs) -> dict:
        """checkGetOrderList.
        
        POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_receipt_order(self, **kwargs) -> dict:
        """createReceiptOrder.
        
        POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def finish_receive_allocation_order(self, **kwargs) -> dict:
        """finishReceiveAllocationOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_packing_data(self, **kwargs) -> dict:
        """getPackingData.
        
        POST /erp/sc/routing/owms/inbound/getPackingData
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/getPackingData",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_process_order_lists(self, **kwargs) -> dict:
        """getProcessOrderLists.
        
        POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_storage_adjust_order_list(self, **kwargs) -> dict:
        """getStorageAdjustOrderList.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_storage_allocation_list(self, **kwargs) -> dict:
        """getStorageAllocationList.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inbound_batches_receipt(self, **kwargs) -> dict:
        """inboundBatchesReceipt.
        
        POST /erp/sc/routing/owms/inbound/batchesReceipt
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/batchesReceipt",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inbound_complete_receipt(self, **kwargs) -> dict:
        """inboundCompleteReceipt.
        
        POST /erp/sc/routing/owms/inbound/completeReceipt
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/completeReceipt",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inbound_get_custom_types(self, **kwargs) -> dict:
        """inboundGetCustomTypes.
        
        POST /erp/sc/routing/storage/inbound/getCustomTypes
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/inbound/getCustomTypes",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inboundget_orders(self, **kwargs) -> dict:
        """inboundgetOrders.
        
        POST /erp/sc/routing/storage/inbound/getOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/inbound/getOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def inventory_bin_details(self, **kwargs) -> dict:
        """inventoryBinDetails.
        
        POST /erp/sc/routing/data/local_inventory/inventoryBinDetails
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/inventoryBinDetails",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def list_inbound(self, **kwargs) -> dict:
        """listInbound.
        
        POST /erp/sc/routing/owms/inbound/listInbound
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/listInbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def list_order_nos(self, **kwargs) -> dict:
        """listOrderNos.
        
        POST /erp/sc/routing/owms/inbound/listOrderNos
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/listOrderNos",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def match_sku_list(self, **kwargs) -> dict:
        """matchSkuList.
        
        POST /erp/sc/routing/owms/inbound/matchSkuList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/matchSkuList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def outbound_get_custom_types(self, **kwargs) -> dict:
        """outboundGetCustomTypes.
        
        POST /erp/sc/routing/storage/outbound/getCustomTypes
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/outbound/getCustomTypes",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def outbound_order_delete(self, **kwargs) -> dict:
        """outboundOrderDelete.
        
        POST /basicOpen/outboundOrder/outbound/delete
        """
        return await self._request_with_token(
            route_name="/basicOpen/outboundOrder/outbound/delete",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def outboundget_orders(self, **kwargs) -> dict:
        """outboundgetOrders.
        
        POST /erp/sc/routing/storage/outbound/getOrders
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/outbound/getOrders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def oversea_stock_order_allocate(self, **kwargs) -> dict:
        """overseaStockOrderAllocate.
        
        POST /basicOpen/overSeaWarehouse/stockOrder/allocate
        """
        return await self._request_with_token(
            route_name="/basicOpen/overSeaWarehouse/stockOrder/allocate",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def package_label(self, **kwargs) -> dict:
        """packageLabel.
        
        POST /erp/sc/routing/owms/inbound/packageLabel
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/packageLabel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def packing(self, **kwargs) -> dict:
        """packing.
        
        POST /erp/sc/routing/owms/inbound/packing
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/packing",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def partly_receive_allocation_order(self, **kwargs) -> dict:
        """partlyReceiveAllocationOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_label(self, **kwargs) -> dict:
        """productLabel.
        
        POST /erp/sc/routing/owms/inbound/productLabel
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/productLabel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def quality_inspection_order_detail(self, **kwargs) -> dict:
        """qualityInspectionOrderDetail.
        
        POST /basicOpen/qualityInspectionOrder/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/qualityInspectionOrder/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def receive_allocation_order(self, **kwargs) -> dict:
        """receiveAllocationOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def removal_inbound_list(self, **kwargs) -> dict:
        """removalInboundList.
        
        POST /erp/sc/routing/owms/removalInbound/list
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/removalInbound/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_tracking_no(self, **kwargs) -> dict:
        """setTrackingNo.
        
        POST /basicOpen/logisticsOrdering/setTrackingNo
        """
        return await self._request_with_token(
            route_name="/basicOpen/logisticsOrdering/setTrackingNo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def submit_allocation_order(self, **kwargs) -> dict:
        """submitAllocationOrder.
        
        POST /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def switch_status(self, **kwargs) -> dict:
        """switchStatus.
        
        POST /erp/sc/routing/storage/wareHouseBin/switchStatus
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/wareHouseBin/switchStatus",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_inbound(self, **kwargs) -> dict:
        """updateInbound.
        
        POST /erp/sc/routing/owms/inbound/updateInbound
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/owms/inbound/updateInbound",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def ware_house_bin_statement(self, **kwargs) -> dict:
        """wareHouseBinStatement.
        
        POST /erp/sc/routing/data/local_inventory/wareHouseBinStatement
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/wareHouseBinStatement",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def warehouse_bin(self, **kwargs) -> dict:
        """warehouseBin.
        
        POST /erp/sc/routing/data/local_inventory/warehouseBin
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/warehouseBin",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def wms_order_get_wms_logistics_labels(self, **kwargs) -> dict:
        """wmsOrderGetWmsLogisticsLabels.
        
        POST /erp/sc/routing/wms/order/getWmsLogisticsLabels
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/wms/order/getWmsLogisticsLabels",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

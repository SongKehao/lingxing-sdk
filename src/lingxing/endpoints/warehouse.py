"""仓库/库存 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class WarehouseEndpoints(BaseEndpoint):
    """领星仓库/库存 API (76个接口)."""

    async def add_allocation_order(self, **kwargs) -> list | dict:
        """AddAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def adjust_order_confirm(self, **kwargs) -> dict:
        """AdjustOrderConfirm. POST /basicOpen/adjustOrder/adjust/setAdjust"""
        resp = await self._post("/basicOpen/adjustOrder/adjust/setAdjust", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_storage_allocation_list(self, **kwargs) -> dict:
        """CancelStorageAllocationList. POST /basicOpen/storageAllocationList/cancel"""
        resp = await self._post("/basicOpen/storageAllocationList/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def create_inbound(self, **kwargs) -> dict:
        """CreateInbound. POST /erp/sc/routing/owms/inbound/createInbound"""
        resp = await self._post("/erp/sc/routing/owms/inbound/createInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_fba_shipment_list(self, **kwargs) -> dict:
        """DeleteFbaShipmentList. POST /basicOpen/openapi/fbaShipment/deleteShipmentList"""
        resp = await self._post("/basicOpen/openapi/fbaShipment/deleteShipmentList", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_over_sea_stock_order(self, **kwargs) -> dict:
        """DeleteOverSeaStockOrder. POST /basicOpen/overSeaWarehouse/stockOrder/delete"""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_storage_allocation_list(self, **kwargs) -> dict:
        """DeleteStorageAllocationList. POST /basicOpen/storageAllocationList/delete"""
        resp = await self._post("/basicOpen/storageAllocationList/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def edit_warehouse(self, **kwargs) -> dict:
        """EditWarehouse. POST /erp/sc/storage/wareHouse/edit"""
        resp = await self._post("/erp/sc/storage/wareHouse/edit", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_stock(self, **kwargs) -> list | dict:
        """FBAStock. POST /erp/sc/routing/fba/fbaStock/fbaList"""
        resp = await self._post("/erp/sc/routing/fba/fbaStock/fbaList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_stock_v2(self, **kwargs) -> list | dict:
        """FBAStock_v2. POST /basicOpen/openapi/storage/fbaWarehouseDetail"""
        resp = await self._post("/basicOpen/openapi/storage/fbaWarehouseDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fast_receive(self, **kwargs) -> dict:
        """FastReceive. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive", kwargs if kwargs else None)
        return resp.data or {}
    async def get_adjust_order_confirm_result(self, **kwargs) -> dict:
        """GetAdjustOrderConfirmResult. POST /basicOpen/adjustOrder/adjust/getAdjustStatus"""
        resp = await self._post("/basicOpen/adjustOrder/adjust/getAdjustStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def get_batch_detail_list(self, **kwargs) -> list | dict:
        """GetBatchDetailList. POST /erp/sc/routing/data/local_inventory/getBatchDetailList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_batch_statement_list(self, **kwargs) -> list | dict:
        """GetBatchStatementList. POST /erp/sc/routing/data/local_inventory/getBatchStatementList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchStatementList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_receive_good_records(self, **kwargs) -> dict:
        """GetReceiveGoodRecords. POST /erp/sc/routing/owms/inbound/getReceiveGoodRecords"""
        resp = await self._post("/erp/sc/routing/owms/inbound/getReceiveGoodRecords", kwargs if kwargs else None)
        return resp.data or {}
    async def inbound_order_confirm(self, **kwargs) -> dict:
        """InboundOrderConfirm. POST /basicOpen/inboundOrder/inbound/setInbound"""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def inventory_details(self, **kwargs) -> list | dict:
        """InventoryDetails. POST /erp/sc/routing/data/local_inventory/inventoryDetails"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryDetails", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_add(self, **kwargs) -> list | dict:
        """OrderAdd. POST /erp/sc/routing/storage/storage/orderAdd"""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAdd", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_add_out(self, **kwargs) -> list | dict:
        """OrderAddOut. POST /erp/sc/routing/storage/storage/orderAddOut"""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAddOut", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_order_confirm(self, **kwargs) -> dict:
        """OutboundOrderConfirm. POST /basicOpen/outboundOrder/outbound/setOutbound"""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOutbound", kwargs if kwargs else None)
        return resp.data or {}
    async def over_seas_stock_detail(self, **kwargs) -> list | dict:
        """OverSeasStockDetail. POST /basicOpen/overSeaWarehouse/stockOrder/detail"""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_match_list(self, **kwargs) -> list | dict:
        """OverseaWarehouseMatchList. POST /basicOpen/overseaWarehouseSetting/matchList"""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/matchList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_product_match(self, **kwargs) -> list | dict:
        """OverseaWarehouseProductMatch. POST /basicOpen/overseaWarehouseSetting/productMatch"""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productMatch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_product_un_match(self, **kwargs) -> list | dict:
        """OverseaWarehouseProductUnMatch. POST /basicOpen/overseaWarehouseSetting/productUnMatch"""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productUnMatch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_receipt_order_list(self, **kwargs) -> list | dict:
        """PurchaseReceiptOrderList. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def receive(self, **kwargs) -> dict:
        """Receive. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive", kwargs if kwargs else None)
        return resp.data or {}
    async def send_inbound(self, **kwargs) -> dict:
        """SendInbound. POST /erp/sc/routing/owms/inbound/sendInbound"""
        resp = await self._post("/erp/sc/routing/owms/inbound/sendInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def set_inbound_order_revoke(self, **kwargs) -> list | dict:
        """SetInboundOrderRevoke. POST /basicOpen/inboundOrder/inbound/setOrderRevoke"""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setOrderRevoke", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_outbound_order_revoke(self, **kwargs) -> list | dict:
        """SetOutboundOrderRevoke. POST /basicOpen/outboundOrder/outbound/setOrderRevoke"""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOrderRevoke", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_logistics(self, **kwargs) -> dict:
        """UpdateLogistics. POST /erp/sc/routing/owms/inbound/updateLogistics"""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateLogistics", kwargs if kwargs else None)
        return resp.data or {}
    async def warehouse_lists(self, **kwargs) -> list | dict:
        """WarehouseLists. POST /erp/sc/data/local_inventory/warehouse"""
        resp = await self._post("/erp/sc/data/local_inventory/warehouse", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warehouse_statement(self, **kwargs) -> list | dict:
        """WarehouseStatement. POST /erp/sc/routing/data/local_inventory/wareHouseStatement"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseStatement", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warehouse_statement_new(self, **kwargs) -> list | dict:
        """WarehouseStatementNew. POST /erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement"""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wms_order_detail(self, **kwargs) -> list | dict:
        """WmsOrderDetail. POST /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers"""
        resp = await self._post("/basicOpen/wmsOrder/getWmsOrdersByOrderNumbers", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wms_order_list(self, **kwargs) -> list | dict:
        """WmsOrderList. POST /erp/sc/routing/wms/order/wmsOrderList"""
        resp = await self._post("/erp/sc/routing/wms/order/wmsOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_adjustment_order(self, **kwargs) -> list | dict:
        """addAdjustmentOrder. POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_rebrand_adjustment_order(self, **kwargs) -> list | dict:
        """addRebrandAdjustmentOrder. POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_sku_adjustment_order(self, **kwargs) -> list | dict:
        """addSkuAdjustmentOrder. POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_storage_process_order(self, **kwargs) -> list | dict:
        """addStorageProcessOrder. POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def bin_create(self, **kwargs) -> dict:
        """binCreate. POST /erp/sc/routing/storage/wareHouseBin/create"""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/create", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_wms_order(self, **kwargs) -> dict:
        """cancelWmsOrder. POST /basicOpen/wmsOrder/cancel"""
        resp = await self._post("/basicOpen/wmsOrder/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def check_add_order(self, **kwargs) -> list | dict:
        """checkAddOrder. POST /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def check_get_order_detail(self, **kwargs) -> list | dict:
        """checkGetOrderDetail. POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def check_get_order_list(self, **kwargs) -> list | dict:
        """checkGetOrderList. POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_receipt_order(self, **kwargs) -> dict:
        """createReceiptOrder. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def finish_receive_allocation_order(self, **kwargs) -> dict:
        """finishReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_packing_data(self, **kwargs) -> list | dict:
        """getPackingData. POST /erp/sc/routing/owms/inbound/getPackingData"""
        resp = await self._post("/erp/sc/routing/owms/inbound/getPackingData", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_process_order_lists(self, **kwargs) -> list | dict:
        """getProcessOrderLists. POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_storage_adjust_order_list(self, **kwargs) -> list | dict:
        """getStorageAdjustOrderList. POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_storage_allocation_list(self, **kwargs) -> list | dict:
        """getStorageAllocationList. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_batches_receipt(self, **kwargs) -> list | dict:
        """inboundBatchesReceipt. POST /erp/sc/routing/owms/inbound/batchesReceipt"""
        resp = await self._post("/erp/sc/routing/owms/inbound/batchesReceipt", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_complete_receipt(self, **kwargs) -> list | dict:
        """inboundCompleteReceipt. POST /erp/sc/routing/owms/inbound/completeReceipt"""
        resp = await self._post("/erp/sc/routing/owms/inbound/completeReceipt", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_get_custom_types(self, **kwargs) -> list | dict:
        """inboundGetCustomTypes. POST /erp/sc/routing/storage/inbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/inbound/getCustomTypes", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inboundget_orders(self, **kwargs) -> list | dict:
        """inboundgetOrders. POST /erp/sc/routing/storage/inbound/getOrders"""
        resp = await self._post("/erp/sc/routing/storage/inbound/getOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inventory_bin_details(self, **kwargs) -> list | dict:
        """inventoryBinDetails. POST /erp/sc/routing/data/local_inventory/inventoryBinDetails"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryBinDetails", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def list_inbound(self, **kwargs) -> list | dict:
        """listInbound. POST /erp/sc/routing/owms/inbound/listInbound"""
        resp = await self._post("/erp/sc/routing/owms/inbound/listInbound", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def list_order_nos(self, **kwargs) -> list | dict:
        """listOrderNos. POST /erp/sc/routing/owms/inbound/listOrderNos"""
        resp = await self._post("/erp/sc/routing/owms/inbound/listOrderNos", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def match_sku_list(self, **kwargs) -> list | dict:
        """matchSkuList. POST /erp/sc/routing/owms/inbound/matchSkuList"""
        resp = await self._post("/erp/sc/routing/owms/inbound/matchSkuList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_get_custom_types(self, **kwargs) -> list | dict:
        """outboundGetCustomTypes. POST /erp/sc/routing/storage/outbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/outbound/getCustomTypes", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_order_delete(self, **kwargs) -> dict:
        """outboundOrderDelete. POST /basicOpen/outboundOrder/outbound/delete"""
        resp = await self._post("/basicOpen/outboundOrder/outbound/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def outboundget_orders(self, **kwargs) -> list | dict:
        """outboundgetOrders. POST /erp/sc/routing/storage/outbound/getOrders"""
        resp = await self._post("/erp/sc/routing/storage/outbound/getOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_stock_order_allocate(self, **kwargs) -> dict:
        """overseaStockOrderAllocate. POST /basicOpen/overSeaWarehouse/stockOrder/allocate"""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/allocate", kwargs if kwargs else None)
        return resp.data or {}
    async def package_label(self, **kwargs) -> list | dict:
        """packageLabel. POST /erp/sc/routing/owms/inbound/packageLabel"""
        resp = await self._post("/erp/sc/routing/owms/inbound/packageLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def packing(self, **kwargs) -> list | dict:
        """packing. POST /erp/sc/routing/owms/inbound/packing"""
        resp = await self._post("/erp/sc/routing/owms/inbound/packing", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def partly_receive_allocation_order(self, **kwargs) -> dict:
        """partlyReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def product_label(self, **kwargs) -> list | dict:
        """productLabel. POST /erp/sc/routing/owms/inbound/productLabel"""
        resp = await self._post("/erp/sc/routing/owms/inbound/productLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def quality_inspection_order_detail(self, **kwargs) -> list | dict:
        """qualityInspectionOrderDetail. POST /basicOpen/qualityInspectionOrder/detail"""
        resp = await self._post("/basicOpen/qualityInspectionOrder/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def receive_allocation_order(self, **kwargs) -> dict:
        """receiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def removal_inbound_list(self, **kwargs) -> list | dict:
        """removalInboundList. POST /erp/sc/routing/owms/removalInbound/list"""
        resp = await self._post("/erp/sc/routing/owms/removalInbound/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_tracking_no(self, **kwargs) -> dict:
        """setTrackingNo. POST /basicOpen/logisticsOrdering/setTrackingNo"""
        resp = await self._post("/basicOpen/logisticsOrdering/setTrackingNo", kwargs if kwargs else None)
        return resp.data or {}
    async def submit_allocation_order(self, **kwargs) -> dict:
        """submitAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def switch_status(self, **kwargs) -> dict:
        """switchStatus. POST /erp/sc/routing/storage/wareHouseBin/switchStatus"""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/switchStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def update_inbound(self, **kwargs) -> dict:
        """updateInbound. POST /erp/sc/routing/owms/inbound/updateInbound"""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def ware_house_bin_statement(self, **kwargs) -> list | dict:
        """wareHouseBinStatement. POST /erp/sc/routing/data/local_inventory/wareHouseBinStatement"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseBinStatement", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warehouse_bin(self, **kwargs) -> list | dict:
        """warehouseBin. POST /erp/sc/routing/data/local_inventory/warehouseBin"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/warehouseBin", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wms_order_get_wms_logistics_labels(self, **kwargs) -> list | dict:
        """wmsOrderGetWmsLogisticsLabels. POST /erp/sc/routing/wms/order/getWmsLogisticsLabels"""
        resp = await self._post("/erp/sc/routing/wms/order/getWmsLogisticsLabels", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

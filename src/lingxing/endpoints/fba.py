"""FBA发货 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint
from ..models.fba import GetFbaProductListItem, GetHeadLogisticsFeeTypesItem, GetInboundShipmentListItem, GetSeaTrackSupplierCarriersItem, ShipFromAddressListItem, ShipmentPlanListsItem

class FBAEndpoints(BaseEndpoint):
    """领星FBA发货 API (31个接口)."""

    async def box_info(self, **kwargs) -> list | dict:
        """BoxInfo. POST /erp/sc/routing/fba/shipment/boxInfo"""
        resp = await self._post("/erp/sc/routing/fba/shipment/boxInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_sended_order(self, **kwargs) -> dict:
        """写操作 CreateSendedOrder. POST /erp/sc/storage/shipment/createSendedOrder"""
        resp = await self._post("/erp/sc/storage/shipment/createSendedOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_ship_from_address(self, **kwargs) -> dict:
        """写操作 CreateShipFromAddress. POST /erp/sc/routing/fba/shipment/createShipFromAddress"""
        resp = await self._post("/erp/sc/routing/fba/shipment/createShipFromAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def create_shipment_plan(self, **kwargs) -> dict:
        """写操作 CreateShipmentPlan. POST /erp/sc/routing/storage/shipment/createShipmentPlan"""
        resp = await self._post("/erp/sc/routing/storage/shipment/createShipmentPlan", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_received_inventory(self, **kwargs) -> dict:
        """写操作 FBAReceivedInventory. POST /erp/sc/data/fba_report/receivedInventory"""
        resp = await self._post("/erp/sc/data/fba_report/receivedInventory", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_shipment_list(self, **kwargs) -> list | dict:
        """FBAShipmentList. POST /erp/sc/data/fba_report/shipmentList"""
        resp = await self._post("/erp/sc/data/fba_report/shipmentList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_fba_product_list(self, **kwargs) -> list[GetFbaProductListItem]:
        """GetFbaProductList. POST /erp/sc/routing/fba/shipment/getFbaProductList"""
        resp = await self._post("/erp/sc/routing/fba/shipment/getFbaProductList", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetFbaProductListItem)
    async def get_head_logistics_fee_types(self, **kwargs) -> list[GetHeadLogisticsFeeTypesItem]:
        """GetHeadLogisticsFeeTypes. POST /erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes"""
        resp = await self._post("/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetHeadLogisticsFeeTypesItem)
    async def get_inbound_shipment_list(self, **kwargs) -> tuple[list[GetInboundShipmentListItem], int]:
        """GetInboundShipmentList（分页）. POST /erp/sc/routing/storage/shipment/getInboundShipmentList"""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentList", kwargs if kwargs else None)
        return self._parse_page(resp.data, GetInboundShipmentListItem)
    async def get_inbound_shipment_list_mws_detail_list(self, **kwargs) -> list | dict:
        """GetInboundShipmentListMwsDetailList. POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList"""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_sea_track_supplier_carriers(self, **kwargs) -> list[GetSeaTrackSupplierCarriersItem]:
        """GetSeaTrackSupplierCarriers. POST /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers"""
        resp = await self._post("/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetSeaTrackSupplierCarriersItem)
    async def invalid_shipment_sn(self, **kwargs) -> list | dict:
        """InvalidShipmentSn. POST /basicOpen/openapi/fbaShipment/shipmentSn/invalid"""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shipmentSn/invalid", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def send_goods(self, **kwargs) -> dict:
        """写操作 SendGoods. POST /erp/sc/storage/shipment/sendGoods"""
        resp = await self._post("/erp/sc/storage/shipment/sendGoods", kwargs if kwargs else None)
        return resp.data or {}
    async def ship_from_address_list(self, **kwargs) -> dict:
        """写操作 ShipFromAddressList. POST /erp/sc/routing/fba/shipment/shipFromAddressList"""
        resp = await self._post("/erp/sc/routing/fba/shipment/shipFromAddressList", kwargs if kwargs else None)
        return resp.data or {}
    async def shipment_lock_stock(self, **kwargs) -> list | dict:
        """ShipmentLockStock. POST /erp/sc/routing/storage/shipment/lockStock"""
        resp = await self._post("/erp/sc/routing/storage/shipment/lockStock", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipment_plan_lists(self, **kwargs) -> list[ShipmentPlanListsItem]:
        """ShipmentPlanLists. POST /erp/sc/data/fba_report/shipmentPlanLists"""
        resp = await self._post("/erp/sc/data/fba_report/shipmentPlanLists", kwargs if kwargs else None)
        return self._parse_list(resp.data, ShipmentPlanListsItem)
    async def shopping_address(self, **kwargs) -> dict:
        """写操作 ShoppingAddress. POST /basicOpen/openapi/fbaShipment/shoppingAddress"""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shoppingAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def sync_shipment(self, **kwargs) -> dict:
        """写操作 SyncShipment. POST /erp/sc/routing/fba/shipment/syncShipment"""
        resp = await self._post("/erp/sc/routing/fba/shipment/syncShipment", kwargs if kwargs else None)
        return resp.data or {}
    async def update_custom_cost(self, **kwargs) -> dict:
        """写操作 UpdateCustomCost. POST /erp/sc/routing/storage/shipment/updateCustomCost"""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateCustomCost", kwargs if kwargs else None)
        return resp.data or {}
    async def update_plan_lists(self, **kwargs) -> dict:
        """写操作 UpdatePlanLists. POST /erp/sc/routing/storage/shipment/updateShipmentPlan"""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentPlan", kwargs if kwargs else None)
        return resp.data or {}
    async def update_ship_from_address(self, **kwargs) -> dict:
        """写操作 UpdateShipFromAddress. POST /erp/sc/routing/fba/shipment/updateShipFromAddress"""
        resp = await self._post("/erp/sc/routing/fba/shipment/updateShipFromAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def update_shipment_actual_status(self, **kwargs) -> dict:
        """写操作 UpdateShipmentActualStatus. POST /erp/sc/routing/storage/shipment/updateShipmentActualStatus"""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentActualStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_batch_send_goods(self, **kwargs) -> dict:
        """写操作 VcBatchSendGoods. POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods"""
        resp = await self._post("/basicOpen/openapi/getInvoice/invoice/batchSendGoods", kwargs if kwargs else None)
        return resp.data or {}
    async def create_ready_send_order(self, **kwargs) -> dict:
        """写操作 createReadySendOrder. POST /erp/sc/routing/storage/shipment/createReadySendOrder"""
        resp = await self._post("/erp/sc/routing/storage/shipment/createReadySendOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_inbound_shipment_list_mws_detail(self, **kwargs) -> list | dict:
        """getInboundShipmentListMwsDetail. POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail"""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_order_release_stock(self, **kwargs) -> dict:
        """写操作 outboundOrderReleaseStock. POST /erp/sc/routing/storage/shipment/releaseStock"""
        resp = await self._post("/erp/sc/routing/storage/shipment/releaseStock", kwargs if kwargs else None)
        return resp.data or {}
    async def print_fba_labels(self, **kwargs) -> dict:
        """写操作 printFbaLabels. POST /erp/sc/storage/shipment/printFbaLabels"""
        resp = await self._post("/erp/sc/storage/shipment/printFbaLabels", kwargs if kwargs else None)
        return resp.data or {}
    async def print_fnsku_labels(self, **kwargs) -> dict:
        """写操作 printFnskuLabels. POST /erp/sc/storage/shipment/printFnskuLabels"""
        resp = await self._post("/erp/sc/storage/shipment/printFnskuLabels", kwargs if kwargs else None)
        return resp.data or {}
    async def search_process_result(self, **kwargs) -> list | dict:
        """searchProcessResult. POST /erp/sc/routing/storage/shipment/searchProcessResult"""
        resp = await self._post("/erp/sc/routing/storage/shipment/searchProcessResult", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_inbound_shipment_list_mws(self, **kwargs) -> dict:
        """写操作 updateInboundShipmentListMws. POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws"""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateInboundShipmentListMws", kwargs if kwargs else None)
        return resp.data or {}
    async def update_list_logistics(self, **kwargs) -> dict:
        """写操作 updateListLogistics. POST /erp/sc/routing/storage/shipment/updateListLogistics"""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateListLogistics", kwargs if kwargs else None)
        return resp.data or {}

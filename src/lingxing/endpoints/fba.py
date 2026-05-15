"""Auto-generated FBAEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class FBAEndpoints:
    """领星API - FBAEndpoints (31个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def box_info(self, **kwargs) -> dict:
        """BoxInfo.
        
        POST /erp/sc/routing/fba/shipment/boxInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/boxInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_sended_order(self, **kwargs) -> dict:
        """CreateSendedOrder.
        
        POST /erp/sc/storage/shipment/createSendedOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/shipment/createSendedOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_ship_from_address(self, **kwargs) -> dict:
        """CreateShipFromAddress.
        
        POST /erp/sc/routing/fba/shipment/createShipFromAddress
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/createShipFromAddress",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_shipment_plan(self, **kwargs) -> dict:
        """CreateShipmentPlan.
        
        POST /erp/sc/routing/storage/shipment/createShipmentPlan
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/createShipmentPlan",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbareceived_inventory(self, **kwargs) -> dict:
        """FBAReceivedInventory.
        
        POST /erp/sc/data/fba_report/receivedInventory
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/receivedInventory",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbashipment_list(self, **kwargs) -> dict:
        """FBAShipmentList.
        
        POST /erp/sc/data/fba_report/shipmentList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/shipmentList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_fba_product_list(self, **kwargs) -> dict:
        """GetFbaProductList.
        
        POST /erp/sc/routing/fba/shipment/getFbaProductList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/getFbaProductList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_head_logistics_fee_types(self, **kwargs) -> dict:
        """GetHeadLogisticsFeeTypes.
        
        POST /erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_inbound_shipment_list(self, **kwargs) -> dict:
        """GetInboundShipmentList.
        
        POST /erp/sc/routing/storage/shipment/getInboundShipmentList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_inbound_shipment_list_mws_detail_list(self, **kwargs) -> dict:
        """GetInboundShipmentListMwsDetailList.
        
        POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_sea_track_supplier_carriers(self, **kwargs) -> dict:
        """GetSeaTrackSupplierCarriers.
        
        POST /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def invalid_shipment_sn(self, **kwargs) -> dict:
        """InvalidShipmentSn.
        
        POST /basicOpen/openapi/fbaShipment/shipmentSn/invalid
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/fbaShipment/shipmentSn/invalid",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def send_goods(self, **kwargs) -> dict:
        """SendGoods.
        
        POST /erp/sc/storage/shipment/sendGoods
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/shipment/sendGoods",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def ship_from_address_list(self, **kwargs) -> dict:
        """ShipFromAddressList.
        
        POST /erp/sc/routing/fba/shipment/shipFromAddressList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/shipFromAddressList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipment_lock_stock(self, **kwargs) -> dict:
        """ShipmentLockStock.
        
        POST /erp/sc/routing/storage/shipment/lockStock
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/lockStock",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipment_plan_lists(self, **kwargs) -> dict:
        """ShipmentPlanLists.
        
        POST /erp/sc/data/fba_report/shipmentPlanLists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/shipmentPlanLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopping_address(self, **kwargs) -> dict:
        """ShoppingAddress.
        
        POST /basicOpen/openapi/fbaShipment/shoppingAddress
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/fbaShipment/shoppingAddress",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def sync_shipment(self, **kwargs) -> dict:
        """SyncShipment.
        
        POST /erp/sc/routing/fba/shipment/syncShipment
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/syncShipment",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_custom_cost(self, **kwargs) -> dict:
        """UpdateCustomCost.
        
        POST /erp/sc/routing/storage/shipment/updateCustomCost
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/updateCustomCost",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_plan_lists(self, **kwargs) -> dict:
        """UpdatePlanLists.
        
        POST /erp/sc/routing/storage/shipment/updateShipmentPlan
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/updateShipmentPlan",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_ship_from_address(self, **kwargs) -> dict:
        """UpdateShipFromAddress.
        
        POST /erp/sc/routing/fba/shipment/updateShipFromAddress
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/shipment/updateShipFromAddress",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_shipment_actual_status(self, **kwargs) -> dict:
        """UpdateShipmentActualStatus.
        
        POST /erp/sc/routing/storage/shipment/updateShipmentActualStatus
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/updateShipmentActualStatus",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_batch_send_goods(self, **kwargs) -> dict:
        """VcBatchSendGoods.
        
        POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/getInvoice/invoice/batchSendGoods",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_ready_send_order(self, **kwargs) -> dict:
        """createReadySendOrder.
        
        POST /erp/sc/routing/storage/shipment/createReadySendOrder
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/createReadySendOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_inbound_shipment_list_mws_detail(self, **kwargs) -> dict:
        """getInboundShipmentListMwsDetail.
        
        POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def outbound_order_release_stock(self, **kwargs) -> dict:
        """outboundOrderReleaseStock.
        
        POST /erp/sc/routing/storage/shipment/releaseStock
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/releaseStock",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def print_fba_labels(self, **kwargs) -> dict:
        """printFbaLabels.
        
        POST /erp/sc/storage/shipment/printFbaLabels
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/shipment/printFbaLabels",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def print_fnsku_labels(self, **kwargs) -> dict:
        """printFnskuLabels.
        
        POST /erp/sc/storage/shipment/printFnskuLabels
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/shipment/printFnskuLabels",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def search_process_result(self, **kwargs) -> dict:
        """searchProcessResult.
        
        POST /erp/sc/routing/storage/shipment/searchProcessResult
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/searchProcessResult",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_inbound_shipment_list_mws(self, **kwargs) -> dict:
        """updateInboundShipmentListMws.
        
        POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/updateInboundShipmentListMws",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_list_logistics(self, **kwargs) -> dict:
        """updateListLogistics.
        
        POST /erp/sc/routing/storage/shipment/updateListLogistics
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/shipment/updateListLogistics",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

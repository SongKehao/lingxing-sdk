"""仓库/库存 API endpoints."""
from __future__ import annotations
from typing import TypedDict

from typing import Any

from ..models.responses.warehouse import GetProcessOrderListsItem, GetStorageAdjustOrderListItem, InboundGetCustomTypesItem, InboundgetOrdersItem, InventoryBinDetailsItem, InventoryDetailsItem, OutboundGetCustomTypesItem, OutboundgetOrdersItem, PurchaseReceiptOrderListItem, RemovalInboundListItem, WareHouseBinStatementItem, WarehouseListsItem, WarehouseStatementItem, WarehouseStatementNewItem, WmsOrderListItem
from ..models.responses.warehouse import (
    OverseaProductUnmatchResponse,
    WarehouseBinEntryRecommendResponse,
    OverseaStockOrderDetailResponse,
    PurchaseReceiptOrderCreateResponse,
    SalesReturnV2ListResponse,
    ReceiptOrderQcListResponse,
    ReturnOrderFastStorageInResponse,
    AllocationPartlyReceiveResponse,
    AllocationFinishReceiveResponse,
    CostChangeFinishResponse,
    WmsOrderSetPackageSizeResponse,
    AwdInboundPlanCancelResponse,
    AwdInboundPlanConfirmResponse,
    AwdInboundPlanCreateResponse,
    AwdInboundPlanDetailResponse,
    AwdInboundPlanPageResponse,
    AwdInboundPlanUpdateResponse,
    AwdInboundShipmentDetailResponse,
    AwdInboundShipmentPageResponse,
    AwdInboundShipmentUpdateTrackResponse,
    AwdInboundShipmentPrintLabelResponse,
    PackingTaskAddResponse,
    PackingTaskBatchEditResponse,
    PackingTaskDelResponse,
    PackingTaskDetailResponse,
    PackingTaskFinishResponse,
    PackingTaskListResponse,
    ProcessPlanListResponse,
    ProcessOrderAddResponse,
    ProcessOrderListResponse,
    AdjustorderAdjustGetadjuststatusResponse,
    AdjustorderAdjustSetadjustResponse,
    DeliveryreceiptPurchasereceiptorderGetorderlistResponse,
    FbaFbastockFbalistResponse,
    InboundorderInboundSetinboundResponse,
    InventorylogWarehouseinventoryWarehousecenterstatementResponse,
    InventoryreceiptInventorycheckAddorderResponse,
    InventoryreceiptInventorycheckGetorderdetailResponse,
    InventoryreceiptInventorycheckGetorderlistResponse,
    InventoryreceiptStorageadjustmentAddadjustmentorderResponse,
    InventoryreceiptStorageadjustmentAddrebrandadjustmentorderResponse,
    InventoryreceiptStorageadjustmentAddskuadjustmentorderResponse,
    InventoryreceiptStorageadjustmentGetstorageadjustorderlistResponse,
    InventoryreceiptStorageallocationAddallocationorderResponse,
    InventoryreceiptStorageallocationGetstorageallocationlistResponse,
    InventoryreceiptStorageallocationSubmitallocationorderResponse,
    InventoryreceiptStorageprocessAddstorageprocessorderResponse,
    InventoryreceiptStorageprocessGetorderlistsResponse,
    LocalInventoryGetbatchdetaillistResponse,
    LocalInventoryGetbatchstatementlistResponse,
    LocalInventoryInventorybindetailsResponse,
    LocalInventoryInventorydetailsResponse,
    LocalInventoryWarehouseResponse,
    LocalInventoryWarehousebinResponse,
    LocalInventoryWarehousebinstatementResponse,
    LocalInventoryWarehousestatementResponse,
    StorageFbawarehousedetailResponse,
    OutboundorderOutboundDeleteResponse,
    OutboundorderOutboundSetoutboundResponse,
    OverseawarehouseStockorderDetailResponse,
    OverseawarehousesettingMatchlistResponse,
    OwmsInboundCreateinboundResponse,
    OwmsInboundGetpackingdataResponse,
    OwmsInboundGetreceivegoodrecordsResponse,
    OwmsInboundListinboundResponse,
    OwmsInboundListordernosResponse,
    OwmsInboundMatchskulistResponse,
    OwmsInboundPackagelabelResponse,
    OwmsRemovalinboundListResponse,
    QualityinspectionorderDetailResponse,
    StorageInboundGetcustomtypesResponse,
    StorageInboundGetordersResponse,
    StorageOutboundGetcustomtypesResponse,
    StorageOutboundGetordersResponse,
    StorageStorageOrderaddResponse,
    StorageStorageOrderaddoutResponse,
    StorageWarehousebinSwitchstatusResponse,
    WmsOrderGetwmslogisticslabelsResponse,
    WmsOrderWmsorderlistResponse,
    WmsorderCancelResponse,
    WmsorderGetwmsordersbyordernumbersResponse,
)
from ._base import BaseEndpoint


class SingleProductReq(TypedDict, total=False):
    sku: str
    fnsku: str
    sid: int
    price_scale: float
    whb_code: str
    remark: str


class ProcessProductReq(TypedDict, total=False):
    combo_sku: str
    combo_sid: int
    combo_fnsku: str
    quantity_num: int
    combo_whb_code: str
    process_fee: float
    single_product_list: list  # List[SingleProductReq]


class ProcessOrderAddReq(TypedDict, total=False):
    type: int
    wid: int
    remark: str
    product_list: list  # List[ProcessProductReq]


class AwdDeliveredGoodsBoReq(TypedDict, total=False):
    boxQuantity: str
    expiration: str
    height: float
    labelOwner: str
    length: float
    lengthUnit: str
    msku: str
    prepCategory: str
    prepOwner: str
    quantityInBox: str
    weight: float
    weightUnit: str
    width: float


class AwdShippingAddressBoReq(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    city: str
    countryCode: str
    phoneNumber: str
    postalCode: str
    shipperName: str
    stateOrProvinceCode: str
    zone: str


class AwdCreateInboundPlanReq(TypedDict, total=False):
    awdDeliveredGoodsBOS: list  # List[AwdDeliveredGoodsBoReq]
    awdShippingAddressBO: dict  # AwdShippingAddressBoReq
    destinationRegion: str
    sid: int


class OverseaSkuUnmatchReq(TypedDict, total=False):
    twId: int
    twpId: int
    wpId: int
    productId: int
    matchNum: int
    matchAll: int
    fnsku: str
    sellerId: str

class ListItemReq(TypedDict, total=False):
    wid: str
    productId: str
    fnsku: str
    sid: str

class ProductBinRecommendListReq(TypedDict, total=False):
    list: list
    withHistory: bool

class ListItemReq(TypedDict, total=False):
    business_order_sn: str
    wid: int
    order_type: int
    expect_arrival_time: str
    logistics_company: str
    logistics_order_no: str
    shipping_cost: float
    other_fee: float
    remark: str
    item_list: list

class CreatePurchaseReceiptOrderReq(TypedDict, total=False):
    list: list

class ReqsItemReq(TypedDict, total=False):
    rmaOrderNo: str
    storeId: str
    wid: str
    itemReqs: list

class ReturnOrderFastStorageInReq(TypedDict, total=False):
    reqs: list

class ProductListItemReq(TypedDict, total=False):
    product_id: int
    seller_id: str
    fnsku: str
    received_good_num: int
    received_bad_num: int

class AllocationPartlyReceiveReq(TypedDict, total=False):
    order_sn: str
    product_list: list

class AllocationFinishReceiveReq(TypedDict, total=False):
    order_sn: str

class ListItemReq(TypedDict, total=False):
    product_id: int
    fnsku: str
    relation_order_out: str
    unit_cost_price: float
    unit_fee_price: float

class CostChangeFinishReq(TypedDict, total=False):
    type: int
    wid: int
    remark: str
    list: list

class SetOrderPackageSizeReq(TypedDict, total=False):
    wo_number: str
    pkg_length: str
    pkg_width: str
    pkg_height: str

class AwdCancelReq(TypedDict, total=False):
    orderId: str
    sid: int

class AwdConfirmReq(TypedDict, total=False):
    orderId: str
    sid: int

class AwdUpdateReq(TypedDict, total=False):
    awdDeliveredGoodsBOS: list

class AwdShipmentUpdateTrackReq(TypedDict, total=False):
    orderId: str
    shipmentId: str
    sid: int
    trackingId: str

class ShipmentidinfoItemReq(TypedDict, total=False):
    pageType: str
    shipmentId: str
    sid: int

class AwdShipmentPrintLabelReq(TypedDict, total=False):
    shipmentIdInfo: list

class DataItemReq(TypedDict, total=False):
    sid: int
    relateSn: str

class PackingTaskAddReq(TypedDict, total=False):
    relateSnType: int
    wid: int
    data: list

class ListItemReq(TypedDict, total=False):
    customBoxId: str
    boxLength: str
    boxWidth: str
    boxHeight: str
    boxWeight: str
    boxNum: int
    ptbId: str
    boxProduct: list

class PackingTaskBatchEditReq(TypedDict, total=False):
    snValue: str
    list: list

class PackingTaskDelReq(TypedDict, total=False):
    ptIds: list

class PackingTaskFinishReq(TypedDict, total=False):
    snValue: str
    needUpdate: bool


class WarehouseEndpoints(BaseEndpoint):

    async def oversea_sku_unmatch(self, data: Optional[OverseaSkuUnmatchReq] = None) -> list[OverseaProductUnmatchResponse]:
        """海外仓sku取消配对.

POST /basicOpen/overseaWarehouseSetting/productMatch

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productMatch", data or {})
        return self._parse_list(resp.data, OverseaProductUnmatchResponse)

    async def product_bin_recommend_list(self, data: Optional[ProductBinRecommendListReq] = None) -> list[WarehouseBinEntryRecommendResponse]:
        """查询产品仓位列表.

POST /basicOpen/warehouseConfig/warehouseBin/getEntryRecommendBinList

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/warehouseConfig/warehouseBin/getEntryRecommendBinList", data or {})
        return self._parse_list(resp.data, WarehouseBinEntryRecommendResponse)

    async def oversea_stockorder_detail(self, overseas_order_no: str = None) -> list[OverseaStockOrderDetailResponse]:
        """查询海外仓备货单详情.

POST /basicOpen/overSeaWarehouse/stockOrder/detail

Args:
    overseas_order_no: see API doc, str."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/detail", {k: v for k, v in {"overseas_order_no": overseas_order_no}.items() if v is not None})
        return self._parse_list(resp.data, OverseaStockOrderDetailResponse)

    async def create_purchase_receipt_order(self, data: Optional[CreatePurchaseReceiptOrderReq] = None) -> list[PurchaseReceiptOrderCreateResponse]:
        """创建待收货的收货单.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder", data or {})
        return self._parse_list(resp.data, PurchaseReceiptOrderCreateResponse)

    async def sales_return_order_list(self, offset: int = None, length: int = None, time_type: int = None, start_time: str = None, end_time: str = None, platform_code: str = None, sales_type: int = None, status: int = None, store_id: int = None, wid: int = None) -> list[SalesReturnV2ListResponse]:
        """查询销售退货单列表.

POST /pb/mp/returns/v2/list

Args:
    offset: see API doc, int.
    length: see API doc, int.
    time_type: see API doc, int.
    start_time: see API doc, str.
    end_time: see API doc, str.
    platform_code: see API doc, str.
    sales_type: see API doc, int.
    status: see API doc, int.
    store_id: see API doc, int.
    wid: see API doc, int."""
        resp = await self._post("/pb/mp/returns/v2/list", {k: v for k, v in {"offset": offset, "length": length, "time_type": time_type, "start_time": start_time, "end_time": end_time, "platform_code": platform_code, "sales_type": sales_type, "status": status, "store_id": store_id, "wid": wid}.items() if v is not None})
        return self._parse_list(resp.data, SalesReturnV2ListResponse)

    async def qc_order_list(self, offset: int = None, length: int = None, date_type: int = None, start_date: str = None, end_date: str = None, qc_sns: list = None, status: int = None, wid: int = None) -> list[ReceiptOrderQcListResponse]:
        """查询质检单列表.

POST /erp/sc/routing/deliveryReceipt/ReceiptOrderQc/getOrderList

Args:
    offset: see API doc, int.
    length: see API doc, int.
    date_type: see API doc, int.
    start_date: see API doc, str.
    end_date: see API doc, str.
    qc_sns: see API doc, list.
    status: see API doc, int.
    wid: see API doc, int."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/ReceiptOrderQc/getOrderList", {k: v for k, v in {"offset": offset, "length": length, "date_type": date_type, "start_date": start_date, "end_date": end_date, "qc_sns": qc_sns, "status": status, "wid": wid}.items() if v is not None})
        return self._parse_list(resp.data, ReceiptOrderQcListResponse)

    async def return_order_fast_storage_in(self, data: Optional[ReturnOrderFastStorageInReq] = None) -> list[ReturnOrderFastStorageInResponse]:
        """待收货退货单快捷入库.

POST /basicOpen/return/order/fastStorageIn

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/return/order/fastStorageIn", data or {})
        return self._parse_list(resp.data, ReturnOrderFastStorageInResponse)

    async def allocation_partly_receive(self, data: Optional[AllocationPartlyReceiveReq] = None) -> list[AllocationPartlyReceiveResponse]:
        """调拨单分批收货.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder", data or {})
        return self._parse_list(resp.data, AllocationPartlyReceiveResponse)

    async def allocation_finish_receive(self, data: Optional[AllocationFinishReceiveReq] = None) -> list[AllocationFinishReceiveResponse]:
        """调拨单结束到货.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder", data or {})
        return self._parse_list(resp.data, AllocationFinishReceiveResponse)

    async def cost_change_finish(self, data: Optional[CostChangeFinishReq] = None) -> list[CostChangeFinishResponse]:
        """创建已完成的成本补录单.

POST /erp/sc/routing/inventoryReceipt/CostChangeOrder/finishCostChangeOrder

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/CostChangeOrder/finishCostChangeOrder", data or {})
        return self._parse_list(resp.data, CostChangeFinishResponse)

    async def set_order_package_size(self, data: Optional[SetOrderPackageSizeReq] = None) -> list[WmsOrderSetPackageSizeResponse]:
        """设置包裹尺寸.

POST /erp/sc/routing/wms/order/setOrderPackageSize

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/wms/order/setOrderPackageSize", data or {})
        return self._parse_list(resp.data, WmsOrderSetPackageSizeResponse)

    """领星仓库/库存 API (76个接口)."""

    async def awd_cancel(self, data: Optional[AwdCancelReq] = None) -> list[AwdInboundPlanCancelResponse]:
        """取消AWD入库任务.

POST /amzStaServer/openapi/awd/inbound-plan/cancel

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/cancel", data or {})
        return self._parse_list(resp.data, AwdInboundPlanCancelResponse)

    async def awd_confirm(self, data: Optional[AwdConfirmReq] = None) -> list[AwdInboundPlanConfirmResponse]:
        """确认AWD入库任务.

POST /amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan", data or {})
        return self._parse_list(resp.data, AwdInboundPlanConfirmResponse)

    async def awd_create(self, data: Optional[AwdCreateInboundPlanReq] = None) -> list[AwdInboundPlanCreateResponse]:
        """创建AWD入库任务.

POST /amzStaServer/openapi/awd/inbound-plan/createInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/createInboundPlan", data or {})
        return self._parse_list(resp.data, AwdInboundPlanCreateResponse)

    async def awd_detail(self, order_id: str = None, sid: int = None) -> list[AwdInboundPlanDetailResponse]:
        """查询AWD入库任务详情.

POST /amzStaServer/openapi/awd/inbound-plan/detail

Args:
    order_id: see API doc, str.
    sid: see API doc, int."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/detail", {k: v for k, v in {"orderId": order_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, AwdInboundPlanDetailResponse)

    async def awd_list(self, page: int = None, date_type: int = None, start_date_time: str = None, end_date_time: str = None, order_id: str = None, shipment_id: str = None, sid_list: list = None, status_list: list = None, length: int = None) -> list[AwdInboundPlanPageResponse]:
        """查询AWD入库任务列表.

POST /amzStaServer/openapi/awd/inbound-plan/page

Args:
    page: see API doc, int.
    date_type: see API doc, int.
    start_date_time: see API doc, str.
    end_date_time: see API doc, str.
    order_id: see API doc, str.
    shipment_id: see API doc, str.
    sid_list: see API doc, list.
    status_list: see API doc, list.
    length: see API doc, int."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/page", {k: v for k, v in {"page": page, "dateType": date_type, "startDateTime": start_date_time, "endDateTime": end_date_time, "orderId": order_id, "shipmentId": shipment_id, "sidList": sid_list, "statusList": status_list, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, AwdInboundPlanPageResponse)

    async def awd_update(self, data: Optional[AwdUpdateReq] = None) -> list[AwdInboundPlanUpdateResponse]:
        """更新AWD入库任务.

POST /amzStaServer/openapi/awd/inbound-plan/updateInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-plan/updateInboundPlan", data or {})
        return self._parse_list(resp.data, AwdInboundPlanUpdateResponse)

    async def awd_shipment_detail(self, shipment_id: str = None, sid: int = None) -> list[AwdInboundShipmentDetailResponse]:
        """查询AWD入库货件详情.

POST /amzStaServer/openapi/awd/inbound-shipment/detail

Args:
    shipment_id: see API doc, str.
    sid: see API doc, int."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-shipment/detail", {k: v for k, v in {"shipmentId": shipment_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, AwdInboundShipmentDetailResponse)

    async def awd_shipment_list(self, page: int = None, date_type: int = None, start_date_time: str = None, end_date_time: str = None, shipment_id: str = None, sid_list: list = None, status_list: list = None, length: int = None) -> list[AwdInboundShipmentPageResponse]:
        """查询AWD入库货件列表.

POST /amzStaServer/openapi/awd/inbound-shipment/page

Args:
    page: see API doc, int.
    date_type: see API doc, int.
    start_date_time: see API doc, str.
    end_date_time: see API doc, str.
    shipment_id: see API doc, str.
    sid_list: see API doc, list.
    status_list: see API doc, list.
    length: see API doc, int."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-shipment/page", {k: v for k, v in {"page": page, "dateType": date_type, "startDateTime": start_date_time, "endDateTime": end_date_time, "shipmentId": shipment_id, "sidList": sid_list, "statusList": status_list, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, AwdInboundShipmentPageResponse)

    async def awd_shipment_update_track(self, data: Optional[AwdShipmentUpdateTrackReq] = None) -> list[AwdInboundShipmentUpdateTrackResponse]:
        """更新AWD货件跟踪编号.

POST /amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo", data or {})
        return self._parse_list(resp.data, AwdInboundShipmentUpdateTrackResponse)

    async def awd_shipment_print_label(self, data: Optional[AwdShipmentPrintLabelReq] = None) -> list[AwdInboundShipmentPrintLabelResponse]:
        """打印AWD入库货件箱子标签.

POST /amzStaServer/openapi/awd/inbound-shipment/uploadPacking

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/awd/inbound-shipment/uploadPacking", data or {})
        return self._parse_list(resp.data, AwdInboundShipmentPrintLabelResponse)

    async def packing_task_add(self, data: Optional[PackingTaskAddReq] = None) -> list[PackingTaskAddResponse]:
        """装箱任务-生成装箱任务.

POST /basicOpen/packingTask/addTask

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/packingTask/addTask", data or {})
        return self._parse_list(resp.data, PackingTaskAddResponse)

    async def packing_task_batch_edit(self, data: Optional[PackingTaskBatchEditReq] = None) -> list[PackingTaskBatchEditResponse]:
        """装箱任务-批量编辑装箱信息.

POST /basicOpen/packingTask/batchEditPackingBox

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/packingTask/batchEditPackingBox", data or {})
        return self._parse_list(resp.data, PackingTaskBatchEditResponse)

    async def packing_task_del(self, data: Optional[PackingTaskDelReq] = None) -> list[PackingTaskDelResponse]:
        """装箱任务-删除装箱任务.

POST /basicOpen/packingTask/delTask

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/packingTask/delTask", data or {})
        return self._parse_list(resp.data, PackingTaskDelResponse)

    async def packing_task_detail(self, pt_id: int = None) -> list[PackingTaskDetailResponse]:
        """装箱任务-任务详情.

POST /basicOpen/packingTask/taskDetail

Args:
    pt_id: see API doc, int."""
        resp = await self._post("/basicOpen/packingTask/taskDetail", {k: v for k, v in {"ptId": pt_id}.items() if v is not None})
        return self._parse_list(resp.data, PackingTaskDetailResponse)

    async def packing_task_finish(self, data: Optional[PackingTaskFinishReq] = None) -> list[PackingTaskFinishResponse]:
        """装箱任务-标记已完成.

POST /basicOpen/packingTask/finishTask

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/packingTask/finishTask", data or {})
        return self._parse_list(resp.data, PackingTaskFinishResponse)

    async def packing_task_list(self, relate_sn_type: int = None, start_date: str = None, end_date: str = None, search_field: str = None, search_value: str = None) -> list[PackingTaskListResponse]:
        """装箱任务-单据列表.

POST /basicOpen/packingTask/getRelateSnList

Args:
    relate_sn_type: see API doc, int.
    start_date: see API doc, str.
    end_date: see API doc, str.
    search_field: see API doc, str.
    search_value: see API doc, str."""
        resp = await self._post("/basicOpen/packingTask/getRelateSnList", {k: v for k, v in {"relateSnType": relate_sn_type, "startDate": start_date, "endDate": end_date, "searchField": search_field, "searchValue": search_value}.items() if v is not None})
        return self._parse_list(resp.data, PackingTaskListResponse)

    async def process_plan_list(self, offset: int = None, length: int = None, processing_step: int = None, lock_status: int = None, search_key: str = None, search_value: str = None, search_time_key: str = None, search_time_start: str = None, search_time_end: str = None, senior_search_list: list = None) -> list[ProcessPlanListResponse]:
        """查询加工计划列表.

POST /basicOpen/openapi/workOrder/processPlanList

Args:
    offset: see API doc, int.
    length: see API doc, int.
    processing_step: see API doc, int.
    lock_status: see API doc, int.
    search_key: see API doc, str.
    search_value: see API doc, str.
    search_time_key: see API doc, str.
    search_time_start: see API doc, str.
    search_time_end: see API doc, str.
    senior_search_list: see API doc, list."""
        resp = await self._post("/basicOpen/openapi/workOrder/processPlanList", {k: v for k, v in {"offset": offset, "length": length, "processing_step": processing_step, "lock_status": lock_status, "search_key": search_key, "search_value": search_value, "search_time_key": search_time_key, "search_time_start": search_time_start, "search_time_end": search_time_end, "senior_search_list": senior_search_list}.items() if v is not None})
        return self._parse_list(resp.data, ProcessPlanListResponse)

    async def process_order_add(self, data: Optional[ProcessOrderAddReq] = None) -> list[ProcessOrderAddResponse]:
        """创建加工单/拆分单.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder", data or {})
        return self._parse_list(resp.data, ProcessOrderAddResponse)

    async def process_order_list(self, operate_type: int = None, wid: int = None, process_sn: str = None, status: int = None, search_field_time: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None) -> list[ProcessOrderListResponse]:
        """加工单列表.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists

Args:
    operate_type: see API doc, int.
    wid: see API doc, int.
    process_sn: see API doc, str.
    status: see API doc, int.
    search_field_time: see API doc, str.
    start_date: see API doc, str.
    end_date: see API doc, str.
    offset: see API doc, int.
    length: see API doc, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists", {k: v for k, v in {"type": operate_type, "wid": wid, "process_sn": process_sn, "status": status, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, ProcessOrderListResponse)

    async def add_allocation_order(self, wid: int = None, sys_wid: int = None, to_wid: int = None, sys_to_wid: int = None, freight_fee: str = None, other_fee: str = None, fee_part_type: int = None, remark: str = None, type: int = None, predict_time: str = None, out_bin_type: str = None, product_list: Any = None, out_available_bin: list = None, out_inferior_bin: list = None, to_available_bin: list = None, to_inferior_bin: list = None) -> InventoryreceiptStorageallocationAddallocationorderResponse | None:
        """创建待收货/已完成的调拨单.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder

Args:
    wid: 客户出库仓库id（与系统仓库出库id任一必填，优先取客户出库仓库id）, int.
    sys_wid: 系统仓库出库id（与客户仓库出库id任一必填，优先取客户出库仓库id）, int.
    to_wid: 客户入库仓库id（与系统仓库入库id任一必填，优先取客户入库仓库id）, int.
    sys_to_wid: 系统仓库入库id（与客户仓库入库id任一必填，优先取客户入库仓库id）, int.
    freight_fee: 运费, string.
    other_fee: 其他费用, string.
    fee_part_type: 费用分摊方式：【默认0】 0 不分摊 2 按sku数量分摊 3 按重量 4 按体积 5 按自定义, int.
    remark: 备注, string.
    type: 调拨类型：【默认1】 1 简易调拨【创建已完成状态的单据】 2 完整调拨【创建待收货状态的单据】, int.
    predict_time: 预计到货时间，格式：Y-m-d, string.
    out_available_bin: 出库可用仓位列表, array.
    out_inferior_bin: 出库次品仓位列表, array.
    to_available_bin: 入库可用仓位列表, array.
    to_inferior_bin: 入库次品仓位列表, array.
    out_bin_type: 0 默认  1 出库仓位不为空时，必传, string."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder", {k: v for k, v in {"wid": wid, "sys_wid": sys_wid, "to_wid": to_wid, "sys_to_wid": sys_to_wid, "freight_fee": freight_fee, "other_fee": other_fee, "fee_part_type": fee_part_type, "remark": remark, "type": type, "predict_time": predict_time, "out_bin_type": out_bin_type, "product_list": product_list, "out_available_bin": out_available_bin, "out_inferior_bin": out_inferior_bin, "to_available_bin": to_available_bin, "to_inferior_bin": to_inferior_bin}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageallocationAddallocationorderResponse)
    async def adjust_order_confirm(self, orderSn: list = None) -> AdjustorderAdjustSetadjustResponse | None:
        """调整单确认调整.

POST /basicOpen/adjustOrder/adjust/setAdjust

Args:
    orderSn: 调整单单号, array."""
        resp = await self._post("/basicOpen/adjustOrder/adjust/setAdjust", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None})
        return self._parse_one(resp.data, AdjustorderAdjustSetadjustResponse)
    async def cancel_storage_allocation_list(self, order_sn: str = None) -> dict:
        """撤销调拨单.

POST /basicOpen/storageAllocationList/cancel

Args:
    order_sn: 调拨单号 对应查询调拨单列表data>>order_sn字段 (required), string."""
        resp = await self._post("/basicOpen/storageAllocationList/cancel", {k: v for k, v in {"order_sn": order_sn}.items() if v is not None})
        return resp.data or {}
    async def create_inbound(self, inbound_order_no: str = None, custom_s_wid: str = None, s_wid: int = None, r_wid: int = None, logistics_id: int = None, status: int = None, estimated_time: str = None, arrival_time: str = None, share_id: int = None, remark: str = None, file_id: str = None, overseas_type: int = None, real_delivery_time: str = None, logistics_list_type: int = None, method_id: str = None, custom_fields: dict = None, logistics_list: list = None, product_list: list = None, head_logistics_list: Any = None) -> OwmsInboundCreateinboundResponse | None:
        """创建待发货/待收货/已完成的备货单.

POST /erp/sc/routing/owms/inbound/createInbound

Args:
    inbound_order_no: 客户参考号（唯一单号） (required), string.
    custom_s_wid: 自定义仓库id，custom_s_wid和s_wid其中一项必填，都填则优先custom_s_wid, string.
    s_wid: 发货仓库，仅限本地仓 (required), int.
    r_wid: 收货仓库，仅限海外仓 (required), int.
    logistics_id: 物流方式id，查询头程物流渠道列表接口对应字段【id】 （按计费重分摊时，需有传对应物流方式，以获取材积参数用于计算） (required), int.
    status: 订单状态：【默认60】 40 待发货 50 待收货 60 已完成 注：收货仓支持三方海外仓的备货单状态只会到待发货, int.
    estimated_time: 预计到货时间, string.
    arrival_time: 实际到货时间, string.
    share_id: 头程费分摊方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积 注意：生成待发货状态备货单时，需要通过接口上传备货单装箱信息上传箱子信息； 待收货和已完成的订单不支持【上传备货单装箱信息】，无法按箱子体积分摊, int.
    remark: 备注, string.
    file_id: 附件id, string.
    overseas_type: 下单至第三方【默认2】： 1 否，2 是 注：当收货仓为API海外仓时可填，不填默认为是, int.
    real_delivery_time: 实际发货时间, string.
    logistics_list: 物流信息, array.
    product_list: 产品信息 (required), array.
    logistics_list_type: 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object.
    method_id: 运输方式 查询运输方式列表接口对应字段【method_id】, string.
    custom_fields: 自定义字段, object."""
        resp = await self._post("/erp/sc/routing/owms/inbound/createInbound", {k: v for k, v in {"inbound_order_no": inbound_order_no, "custom_s_wid": custom_s_wid, "s_wid": s_wid, "r_wid": r_wid, "logistics_id": logistics_id, "status": status, "estimated_time": estimated_time, "arrival_time": arrival_time, "share_id": share_id, "remark": remark, "file_id": file_id, "overseas_type": overseas_type, "real_delivery_time": real_delivery_time, "logistics_list_type": logistics_list_type, "method_id": method_id, "custom_fields": custom_fields, "logistics_list": logistics_list, "product_list": product_list, "head_logistics_list": head_logistics_list}.items() if v is not None})
        return self._parse_one(resp.data, OwmsInboundCreateinboundResponse)
    async def delete_fba_shipment_list(self, shipment_nos: Any = None) -> dict:
        """删除发货单.

POST /basicOpen/openapi/fbaShipment/deleteShipmentList

Args:
    shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (required), array."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/deleteShipmentList", {k: v for k, v in {"shipment_nos": shipment_nos}.items() if v is not None})
        return resp.data or {}
    async def delete_over_sea_stock_order(self, overseas_order_nos: Any = None) -> dict:
        """删除备货单.

POST /basicOpen/overSeaWarehouse/stockOrder/delete

Args:
    overseas_order_nos: 备货单单号，对应获取备货单号接口字段【overseas_order_no】 (required), array."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/delete", {k: v for k, v in {"overseas_order_nos": overseas_order_nos}.items() if v is not None})
        return resp.data or {}
    async def delete_storage_allocation_list(self, orderSn: Any = None) -> dict:
        """删除调拨单.

POST /basicOpen/storageAllocationList/delete

Args:
    orderSn: 调拨单单号，对应查询调拨单列表接口字段【order_sn】 (required), array."""
        resp = await self._post("/basicOpen/storageAllocationList/delete", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None})
        return resp.data or {}
    async def edit_warehouse(self, sys_wid: int = None, wid: str = None, name: str = None, contact: str = None, telephone: str = None, address: str = None, remark: str = None, type: int = None) -> dict:
        """添加/修改仓库.

POST /erp/sc/storage/wareHouse/edit

Args:
    sys_wid: 领星系统仓库id，编辑时必传, int.
    wid: 客户自定义仓库id【非领星系统ERP内仓库id】, string.
    name: 仓库名称 (required), string.
    contact: 负责人, string.
    telephone: 联系电话, string.
    address: 仓库地址, string.
    remark: 备注, string.
    type: 仓库属性：1 -本地仓 3 -海外自建仓，不传默认 1, int."""
        resp = await self._post("/erp/sc/storage/wareHouse/edit", {k: v for k, v in {"sys_wid": sys_wid, "wid": wid, "name": name, "contact": contact, "telephone": telephone, "address": address, "remark": remark, "type": type}.items() if v is not None})
        return resp.data or {}
    async def fba_stock(self, sid: str = None, offset: int = None, length: int = None) -> list[FbaFbastockFbalistResponse]:
        """查询FBA库存列表.

POST /erp/sc/routing/fba/fbaStock/fbaList

Args:
    sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/erp/sc/routing/fba/fbaStock/fbaList", {k: v for k, v in {"sid": sid, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, FbaFbastockFbalistResponse)
    async def fba_stock_v2(self, offset: int = 0, length: int = 20, search_field: str = None, search_value: str = None, cid: str = None, sid: str = None, bid: str = None, attribute: int = None, asin_principal: str = None, status: str = None, senior_search_list: str = None, fulfillment_channel_type: str = None, is_hide_zero_stock: int = 0, is_parant_asin_merge: int = 0, is_contain_del_ls: int = 0, query_fba_storage_quantity_list: bool = None, is_cost_page: int = 0, sort_field: str = "sku", sort_type: str = "asc") -> list[StorageFbawarehousedetailResponse]:
        """查询FBA库存列表-v2.

POST /basicOpen/openapi/storage/fbaWarehouseDetail

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20,取值范围[20,50,100,200], int.
    search_field: 搜索维度: sku product_name seller_sku fnsku asin parent_asin spu spu_name, string.
    search_value: 搜索值, string.
    cid: 分类, string.
    sid: 店铺id（支持多个，使用,分隔）, string.
    bid: 品牌, string.
    attribute: 属性, string.
    asin_principal: Listing负责人uid，对应查询ERP用户信息列表uid字段 多个使用,分隔, string.
    status: 在售状态: 0 停售 1 在售, string.
    senior_search_list: 高级搜索列表，详情见附加说明, string.
    fulfillment_channel_type: 配送方式: FBA FBM, string.
    is_hide_zero_stock: 是否隐藏零库存行: 0 不隐藏零库存行 1 隐藏零库存行, int.
    is_parant_asin_merge: 是否合并父ASIN: 0 不合并父ASIN 1 合并父ASIN, int.
    is_contain_del_ls: 是否显示已删除Listing: 0 不显示已删除Listing 1 显示已删除Listing, int.
    query_fba_storage_quantity_list: true 是、false 否；默认false，如果传入true,则出参数据中的欧洲共享仓会将出参字段-fba_storage_quantity_list的值返回, Boolean.
    is_cost_page: 是否查询成本页面: 1 是，返回cg_price字段, int.
    sort_field: 排序字段, 如 sku, string.
    sort_type: 排序方式: asc/desc, string."""
        resp = await self._post("/basicOpen/openapi/storage/fbaWarehouseDetail", {k: v for k, v in {"offset": offset, "length": length, "search_field": search_field, "search_value": search_value, "cid": cid, "sid": sid, "bid": bid, "attribute": attribute, "asin_principal": asin_principal, "status": status, "senior_search_list": senior_search_list, "fulfillment_channel_type": fulfillment_channel_type, "is_hide_zero_stock": is_hide_zero_stock, "is_parant_asin_merge": is_parant_asin_merge, "is_contain_del_ls": is_contain_del_ls, "query_fba_storage_quantity_list": query_fba_storage_quantity_list, "is_cost_page": is_cost_page, "sort_field": sort_field, "sort_type": sort_type}.items() if v is not None})
        return self._parse_list(resp.data, StorageFbawarehousedetailResponse)
    async def fast_receive(self, order_sn: str = None, expect_arrival_time: str = None, custom_receive_time: str = None, logistics_company: str = None, logistics_order_no: str = None, shipping_cost: float = None, other_fee: float = None, remark: str = None, item_list: list = None) -> dict:
        """收货单快捷入库.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive

Args:
    order_sn: 收货单号 (required), string.
    expect_arrival_time: 预计收货时间，不传时默认取自收货单, string.
    custom_receive_time: 自定义收货时间，  自定义日期须早于请求当天日期, string.
    logistics_company: 物流商，不传时默认取自收货单, string.
    logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单, string.
    shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单, number.
    other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单, number.
    remark: 备注，最大支持255个字符，不传时默认取自收货单, string.
    item_list: 收货明细 (required), array."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive", {k: v for k, v in {"order_sn": order_sn, "expect_arrival_time": expect_arrival_time, "custom_receive_time": custom_receive_time, "logistics_company": logistics_company, "logistics_order_no": logistics_order_no, "shipping_cost": shipping_cost, "other_fee": other_fee, "remark": remark, "item_list": item_list}.items() if v is not None})
        return resp.data or {}
    async def get_adjust_order_confirm_result(self, taskNo: str = None) -> AdjustorderAdjustGetadjuststatusResponse | None:
        """查询调整单确认调整异步结果.

POST /basicOpen/adjustOrder/adjust/getAdjustStatus

Args:
    taskNo: 异步任务编号, string."""
        resp = await self._post("/basicOpen/adjustOrder/adjust/getAdjustStatus", {k: v for k, v in {"taskNo": taskNo}.items() if v is not None})
        return self._parse_one(resp.data, AdjustorderAdjustGetadjuststatusResponse)
    async def get_batch_detail_list(self, offset: int = None, length: int = None, show_zero_stock: int = None, wids: str = None, stock_in_type_list: str = None, search_field: str = None, search_value: str = None) -> list[LocalInventoryGetbatchdetaillistResponse]:
        """查询批次明细.

POST /erp/sc/routing/data/local_inventory/getBatchDetailList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限400, int.
    show_zero_stock: 是否显示0库存信息：0 不显示，1 显示, int.
    wids: 仓库id，多个使用英文逗号分隔, string.
    stock_in_type_list: 入库类型，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 26 退货入库 27 移除入库 45 赠品入库, string.
    search_field: 搜索字段： sku SKU msku MSKU fnsku FNSKU order_sn 单据号 product_name 品名 batch_number 批次号 receipt_order 收货单 purchase_order 采购单 purchase_plan 采购计划 source_batch_number 源头批次号, string.
    search_value: 搜索值, string."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchDetailList", {k: v for k, v in {"offset": offset, "length": length, "show_zero_stock": show_zero_stock, "wids": wids, "stock_in_type_list": stock_in_type_list, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryGetbatchdetaillistResponse)
    async def get_batch_statement_list(self, statement_type_list: str = None, search_field: str = None, search_value: str = None, wid_list: str = None, offset: int = None, length: int = None) -> list[LocalInventoryGetbatchstatementlistResponse]:
        """查询批次流水.

POST /erp/sc/routing/data/local_inventory/getBatchStatementList

Args:
    statement_type_list: 批次流水主类型id，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 47 VC-PO出库 48 VC-DF出库 42 其他出库 41 调拨出库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 71 采购上架 72 委外上架 65 WFS出库 45 赠品入库 46 赠品质检入库 73 赠品上架 201 期初成本调整 202 尾差成本调整, string.
    search_field: 搜索字段： sku SKU msku MSKU fnsku FNSKU product_name 品名 purchase_plan 采购计划 purchase_order 采购单 receipt_order 收货单 order_sn 单据号 batch_number 批次号 source_batch_number 源头批次号, string.
    search_value: 搜索值, string.
    wid_list: 仓库id，多个使用英文逗号分隔, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限400, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchStatementList", {k: v for k, v in {"statement_type_list": statement_type_list, "search_field": search_field, "search_value": search_value, "wid_list": wid_list, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryGetbatchstatementlistResponse)
    async def get_receive_good_records(self, overseas_order_no: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None) -> list[OwmsInboundGetreceivegoodrecordsResponse]:
        """查询备货单收货记录.

POST /erp/sc/routing/owms/inbound/getReceiveGoodRecords

Args:
    overseas_order_no: 备货单单号【不支持批量】, string.
    start_date: 收货开始时间，闭区间，格式：Y-m-d, string.
    end_date: 收货结束时间，开区间，格式：Y-m-d, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认500, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/getReceiveGoodRecords", {k: v for k, v in {"overseas_order_no": overseas_order_no, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundGetreceivegoodrecordsResponse)
    async def inbound_order_confirm(self, orderSn: list = None) -> InboundorderInboundSetinboundResponse | None:
        """入库单确认入库.

POST /basicOpen/inboundOrder/inbound/setInbound

Args:
    orderSn: 入库单单号, array."""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setInbound", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None})
        return self._parse_one(resp.data, InboundorderInboundSetinboundResponse)
    async def inventory_details(self, wid: str = None, offset: int = None, length: int = None, sku: str = None) -> list[LocalInventoryInventorydetailsResponse]:
        """查询仓库库存明细.

POST /erp/sc/routing/data/local_inventory/inventoryDetails

Args:
    wid: 仓库id，多个使用英文逗号分隔, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限800, int.
    sku: SKU，单个,（模糊搜索）, string."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryDetails", {k: v for k, v in {"wid": wid, "offset": offset, "length": length, "sku": sku}.items() if v is not None})
        return self._parse_list(resp.data, InventoryDetailsItem)
    async def order_add(self, wid: str = None, sys_wid: int = None, type: int = None, supplier_id: str = None, sys_supplier_id: int = None, order_sn: str = None, remark: str = None, ship_fee: str = None, other_fee: str = None, fee_part_type: int = None, inbound_time: str = None, inbound_idempotent_code: str = None, product_list: list = None) -> StorageStorageOrderaddResponse | None:
        """添加入库单.

POST /erp/sc/routing/storage/storage/orderAdd

Args:
    wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid, string.
    sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (required), int.
    type: 单据类型： 1 其他入库 2 采购入库 26 退货入库 27 移除入库 (required), int.
    supplier_id: 自定义供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】, string.
    sys_supplier_id: 系统供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】, int.
    order_sn: 采购单号【对此采购单执行快捷入库】，不支持自定义采购单号, string.
    remark: 单据备注, string.
    ship_fee: 运费, string.
    other_fee: 其它费用, string.
    fee_part_type: 费用分配方式: 0 不分摊 1 按金额 2 按数量, int.
    inbound_time: 自定义入库时间，格式：Y-m-d, string.
    inbound_idempotent_code: （入库单）客户参考号, 该字段校验唯一不可重复, string.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAdd", {k: v for k, v in {"wid": wid, "sys_wid": sys_wid, "type": type, "supplier_id": supplier_id, "sys_supplier_id": sys_supplier_id, "order_sn": order_sn, "remark": remark, "ship_fee": ship_fee, "other_fee": other_fee, "fee_part_type": fee_part_type, "inbound_time": inbound_time, "inbound_idempotent_code": inbound_idempotent_code, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, StorageStorageOrderaddResponse)
    async def order_add_out(self, wid: str = None, sys_wid: int = None, type: int = None, status: int = None, sys_supplier_id: int = None, supplier_id: str = None, idempotent_code: str = None, remark: str = None, return_price: float = None, other_fee: float = None, sys_to_wid: int = None, to_wid: str = None, outbound_time: str = None, bin_type: int = None, product_list: list = None) -> StorageStorageOrderaddoutResponse | None:
        """添加出库单.

POST /erp/sc/routing/storage/storage/orderAddOut

Args:
    wid: 自定义仓库ID，wid和sys_wid其中一项必填，都填则优先wid, string.
    sys_wid: 系统仓库ID，sys_wid和wid其中一项必填，都填则优先wid (required), int.
    type: 单据类型： 11 其他出库 12 FBA出库 14 退货出库 18 销毁出库 (required), int.
    status: 新建单据状态： 10：待提交 30：待出库 40：已完成【默认值】, int.
    sys_supplier_id: 系统客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）, int.
    supplier_id: 客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）, string.
    idempotent_code: 客户参考号, 该字段校验唯一不可重复, string.
    remark: 单据备注, string.
    return_price: 退货费（退货出库）, number.
    other_fee: 其它费用（退货出库）, number.
    sys_to_wid: 系统客户目的仓库ID（非退货出库）, int.
    to_wid: 客户目的仓库ID（非退货出库）, string.
    outbound_time: 自定义出库时间，格式：Y-m-d, string.
    bin_type: 出库仓位指定方式： 0 系统指定仓位【默认值】 1 手动指定仓位, int.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAddOut", {k: v for k, v in {"wid": wid, "sys_wid": sys_wid, "type": type, "status": status, "sys_supplier_id": sys_supplier_id, "supplier_id": supplier_id, "idempotent_code": idempotent_code, "remark": remark, "return_price": return_price, "other_fee": other_fee, "sys_to_wid": sys_to_wid, "to_wid": to_wid, "outbound_time": outbound_time, "bin_type": bin_type, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, StorageStorageOrderaddoutResponse)
    async def outbound_order_confirm(self, orderSn: list = None) -> OutboundorderOutboundSetoutboundResponse | None:
        """出库单确认出库.

POST /basicOpen/outboundOrder/outbound/setOutbound

Args:
    orderSn: 出库单单号, array."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOutbound", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None})
        return self._parse_one(resp.data, OutboundorderOutboundSetoutboundResponse)
    async def over_seas_stock_detail(self, overseas_order_no: str = None) -> list[OverseawarehouseStockorderDetailResponse]:
        """查询备货单详情.

POST /basicOpen/overSeaWarehouse/stockOrder/detail

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/detail", {k: v for k, v in {"overseas_order_no": overseas_order_no}.items() if v is not None})
        return self._parse_list(resp.data, OverseawarehouseStockorderDetailResponse)
    async def oversea_warehouse_match_list(self, wpId: int = None, twIds: str = None, offset: int = None, length: int = None, isMatched: int = None, keyword: str = None) -> list[OverseawarehousesettingMatchlistResponse]:
        """查询海外仓sku配对列表.

POST /basicOpen/overseaWarehouseSetting/matchList

Args:
    wpId: 三方服务商id (required), int.
    twIds: 三方仓id，多个之间用逗号隔开, string.
    offset: 分页偏移量，默认0, int.
    length: 分页大小，默认20，上限200, int.
    isMatched: 是否配对，0否，1是, int.
    keyword: 关键词，搜索sku / 品名 / 第三方产品名 / 产品编码, string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/matchList", {k: v for k, v in {"wpId": wpId, "twIds": twIds, "offset": offset, "length": length, "isMatched": isMatched, "keyword": keyword}.items() if v is not None})
        return self._parse_list(resp.data, OverseawarehousesettingMatchlistResponse)
    async def oversea_warehouse_product_match(self, twId: int = None, twpId: int = None, wpId: int = None, productId: int = None, matchNum: int = None, matchAll: int = None, fnsku: str = None, sellerId: str = None) -> list | dict:
        """海外仓sku配对.

POST /basicOpen/overseaWarehouseSetting/productMatch

Args:
    twId: 三方仓id (required), int.
    twpId: 三方商品id (required), int.
    wpId: 三方服务商id (required), int.
    productId: 商品id (required), int.
    matchNum: 整箱配对数量 (required), int.
    matchAll: 是否配对海外仓所有仓库，0否；1是，默认0, int.
    fnsku: fnsku, string.
    sellerId: 店铺id, string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productMatch", {k: v for k, v in {"twId": twId, "twpId": twpId, "wpId": wpId, "productId": productId, "matchNum": matchNum, "matchAll": matchAll, "fnsku": fnsku, "sellerId": sellerId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_product_un_match(self, wpId: str = None, wpmId: str = None) -> list | dict:
        """海外仓sku取消配对.

POST /basicOpen/overseaWarehouseSetting/productUnMatch

Args:
    wpId: 三方服务商id (required), string.
    wpmId: 配对id (required), string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productUnMatch", {k: v for k, v in {"wpId": wpId, "wpmId": wpmId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_receipt_order_list(self, date_type: int = None, start_date: str = None, end_date: str = None, order_sns: str = None, status: int = None, wid: str = None, order_type: int = None, qc_status: str = None, offset: int = None, length: int = None) -> tuple[list[DeliveryreceiptPurchasereceiptorderGetorderlistResponse], int]:
        """查询收货单列表.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList

Args:
    date_type: 查询时间类型：1 预计到货时间，2 收货时间，3 创建时间，4 更新时间, int.
    start_date: 开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sns: 收货单号，多个使用英文逗号分隔, string.
    status: 状态：10 待收货，40 已完成, int.
    wid: 仓库id，多个使用英文逗号分隔, string.
    order_type: 收货类型：1 采购订单，2 委外订单, int.
    qc_status: 质检状态，多个使用英文逗号分隔：0 未质检，1 部分质检，2 完成质检, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认200，上限500, int."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList", {k: v for k, v in {"date_type": date_type, "start_date": start_date, "end_date": end_date, "order_sns": order_sns, "status": status, "wid": wid, "order_type": order_type, "qc_status": qc_status, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_page(resp.data, PurchaseReceiptOrderListItem)
    async def receive(self, order_sn: str = None, expect_arrival_time: str = None, custom_receive_time: str = None, logistics_company: str = None, logistics_order_no: str = None, shipping_cost: float = None, other_fee: float = None, remark: str = None, item_list: list = None) -> dict:
        """收货单到货.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive

Args:
    order_sn: 收货单号 (required), string.
    expect_arrival_time: 预计收货时间，不传时默认取自收货单, string.
    custom_receive_time: 自定义收货时间，  自定义日期须早于请求当天日期, string.
    logistics_company: 物流商，不传时默认取自收货单, string.
    logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单, string.
    shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单, number.
    other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单, number.
    remark: 备注，最大支持255个字符，不传时默认取自收货单, string.
    item_list: 收货明细 (required), array."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive", {k: v for k, v in {"order_sn": order_sn, "expect_arrival_time": expect_arrival_time, "custom_receive_time": custom_receive_time, "logistics_company": logistics_company, "logistics_order_no": logistics_order_no, "shipping_cost": shipping_cost, "other_fee": other_fee, "remark": remark, "item_list": item_list}.items() if v is not None})
        return resp.data or {}
    async def send_inbound(self, overseas_order_no: str = None) -> dict:
        """海外仓备货单发货.

POST /erp/sc/routing/owms/inbound/sendInbound

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/sendInbound", {k: v for k, v in {"overseas_order_no": overseas_order_no}.items() if v is not None})
        return resp.data or {}
    async def set_inbound_order_revoke(self, order_sn: str = None, delete_receipt_order: int = None) -> list | dict:
        """撤销入库单.

POST /basicOpen/inboundOrder/inbound/setOrderRevoke

Args:
    order_sn: 入库单号 对应查询入库单列表data>>order_sn字段 (required), string.
    delete_receipt_order: 是否同步删除收货单  删除则传值 1，否则不传值, int."""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setOrderRevoke", {k: v for k, v in {"order_sn": order_sn, "delete_receipt_order": delete_receipt_order}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_outbound_order_revoke(self, order_sn: str = None) -> list | dict:
        """撤销出库单.

POST /basicOpen/outboundOrder/outbound/setOrderRevoke

Args:
    order_sn: 出库单号 对应查询出库单列表data>>order_sn字段 (required), string."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOrderRevoke", {k: v for k, v in {"order_sn": order_sn}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_logistics(self, overseas_order_no: str = None, logistics_list_type: int = None, logistics_list: list = None, head_logistics_list: Any = None) -> dict:
        """更新备货单物流信息.

POST /erp/sc/routing/owms/inbound/updateLogistics

Args:
    overseas_order_no: 海外仓备货单号 (required), string.
    logistics_list: 物流信息 (required), array.
    logistics_list_type: 物流信息版本： 0：旧版，即将下线 1：新版 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object."""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateLogistics", {k: v for k, v in {"overseas_order_no": overseas_order_no, "logistics_list_type": logistics_list_type, "logistics_list": logistics_list, "head_logistics_list": head_logistics_list}.items() if v is not None})
        return resp.data or {}
    async def warehouse_lists(self, type: int = None, sub_type: int = None, is_delete: str = None, offset: int = None, length: int = None) -> list[LocalInventoryWarehouseResponse]:
        """查询仓库列表.

POST /erp/sc/data/local_inventory/warehouse

Args:
    type: 仓库类型： 1 本地仓【默认值】 3 海外仓 4 亚马逊平台仓 6 AWD仓, int.
    sub_type: 海外仓子类型：  1 无API海外仓  2 有API海外仓【此参数只在type=3生效】, int.
    is_delete: 是否删除，多个使用英文逗号分隔： 0 未删除【默认值】 1 已删除, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000条, int."""
        resp = await self._post("/erp/sc/data/local_inventory/warehouse", {k: v for k, v in {"type": type, "sub_type": sub_type, "is_delete": is_delete, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, WarehouseListsItem)
    async def warehouse_statement(self, wid: str = None, type: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None) -> list[LocalInventoryWarehousestatementResponse]:
        """查询库存流水（旧）.

POST /erp/sc/routing/data/local_inventory/wareHouseStatement

Args:
    wid: 仓库ID，多个仓库ID用英文逗号分隔，不填默认所有仓库, string.
    type: 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】  1 其他入库 2 采购入库 3 调拨入库 10 其它入库（已撤销） 11 其他出库 12 FBA出库 13 调拨出库 14 退货出库 15 FBM退货 16 换标入库 17 加工入库 18 拆分入库 20 采购入库（已撤销） 21 库存调整 23 委外入库 25 盘盈入库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 43 FBM出库 50 成本补录 110 其它出库（已撤销） 120 FBA出库（已撤销） 130 调拨出库（已撤销） 140 退货出库（已撤销） 210 库存调整（已撤销） 500 成本补录（已撤销）, string.
    start_date: 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseStatement", {k: v for k, v in {"wid": wid, "type": type, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, WarehouseStatementItem)
    async def warehouse_statement_new(self, wids: str = None, types: str = None, sub_types: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None) -> list[InventorylogWarehouseinventoryWarehousecenterstatementResponse]:
        """查询库存流水（新）.

POST /erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement

Args:
    wids: 仓库id，多个使用英文逗号分隔, string.
    types: 流水类型，多个使用英文逗号分隔：【不填默认全部类型】 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 15 FBM退货  16 换标入库 17 加工入库 18 拆分入库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 71 采购上架 72 委外上架 42 其他出库 41 调拨出库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 65 WFS出库 100 锁定流水  51 销毁出库 47 VC-PO出库 48 VC-DF出库 49 Temu出库, string.
    sub_types: 子类流水类型，多个使用英文逗号分隔：【不填默认全部类型】 1901 其他入库 手工其他入库 1902 其他入库 用户初始化 1903 其他入库 系统初始化 2201 采购入库 手工采购入库 2202 采购入库 采购单创建入库单 2801 采购质检 质检 7101 采购上架 PDA上架入库 7201 委外上架 PDA委外上架 2401 调拨入库 调拨单入在途 2402 调拨入库 调拨单收货 2403 调拨入库 备货单入在途 2404 调拨入库 备货单收货 2405 调拨入库 备货单入库结束到货 2301 委外入库 委外订单完成加工后入库 2901 委外质检 委外订单质检 2501 盘盈入库 盘点单入库 2502 盘盈入库 数量调整单正向 1501 FBM退货 退货入库 1502 FBM退货 退货入库质检 1601 换标入库 换标调整入库 1701 加工入库 加工单入库 1702 加工入库 委外订单加工入库 1801 拆分入库 拆分单入库 2601 自动退货入库 2602 手动退货入库 2701 移除入库 4201 其他出库 手工其他出库 4101 调拨出库 调拨单出库 4102 调拨出库 备货单出库 3201 委外出库 委外订单完成加工后出库 3301 盘亏出库 盘点单出库 3302 盘亏出库 数量调整单负向 3401 换标出库 换标调整出库 3501 加工出库 加工单出库 3502 加工出库 委外订单加工出库 3601 拆分出库 拆分单出库 3701 FBA出库 发货单出库 3702 FBA出库 手工FBA出库 3801 FBM出库 销售出库单 3901 退货出库 手工退货出库 3902 退货出库 采购单生成的退货出库单 10001 库存锁定-出库 10002 库存锁定-调拨 10003 库存锁定-调整 10004 库存锁定-加工 10005 库存锁定-加工计划 10006 库存锁定-拆分 10007 库存锁定-海外备货 10008 库存锁定-发货 10009 库存锁定-自发货 10010 库存锁定-主动释放 10012 库存锁定-发货拣货 10013 库存锁定-发货计划 10014 库存锁定-WFS库存调整 10011 仓位转移和一键上架, string.
    start_date: 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement", {k: v for k, v in {"wids": wids, "types": types, "sub_types": sub_types, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, WarehouseStatementNewItem)
    async def wms_order_detail(self, isPrintCenter: int = None, orderNumbers: str = None) -> list[WmsorderGetwmsordersbyordernumbersResponse]:
        """查询销售出库单详情.

POST /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers

Args:
    isPrintCenter: 是否需要拣货信息，枚举值：1-是, 0-否, int.
    orderNumbers: 系统单号，必填，多个以逗号连接, string."""
        resp = await self._post("/basicOpen/wmsOrder/getWmsOrdersByOrderNumbers", {k: v for k, v in {"isPrintCenter": isPrintCenter, "orderNumbers": orderNumbers}.items() if v is not None})
        return self._parse_list(resp.data, WmsorderGetwmsordersbyordernumbersResponse)
    async def wms_order_list(self, page: int = None, page_size: int = None, sid_arr: list = None, status_arr: list = None, logistics_status_arr: list = None, platform_order_no_arr: list = None, order_number_arr: list = None, wo_number_arr: list = None, time_type: str = None, start_date: str = None, end_date: str = None) -> list[WmsOrderWmsorderlistResponse]:
        """查询销售出库单列表.

POST /erp/sc/routing/wms/order/wmsOrderList

Args:
    page: 分页页码，默认1, int.
    page_size: 分页长度，默认20，上限200, int.
    sid_arr: 店铺id, array.
    status_arr: 状态： 1 物流下单 2 待出库 3 已出库 4 已截单, array.
    logistics_status_arr: 物流状态： 1 待导入 2 物流待下单 3 物流下单中 4 下单异常 5 下单完成 6 待海外仓下单 7 海外仓下单中 11 待导入国内物流 41 物流取消中 42 物流取消异常 43 物流取消完成, array.
    platform_order_no_arr: 平台单号, array.
    order_number_arr: 系统单号, array.
    wo_number_arr: 销售出库单号, array.
    time_type: 时间类型： 创建时间 create_at  出库时间【单据操作】 delivered_at 流水出库时间 stock_delivered_at 变更时间 update_at, string.
    start_date: 开始日期，格式：Y-m-d，默认为最近1个月, string.
    end_date: 结束日期，格式：Y-m-d，默认为最近1个月, string."""
        resp = await self._post("/erp/sc/routing/wms/order/wmsOrderList", {k: v for k, v in {"page": page, "page_size": page_size, "sid_arr": sid_arr, "status_arr": status_arr, "logistics_status_arr": logistics_status_arr, "platform_order_no_arr": platform_order_no_arr, "order_number_arr": order_number_arr, "wo_number_arr": wo_number_arr, "time_type": time_type, "start_date": start_date, "end_date": end_date}.items() if v is not None})
        return self._parse_list(resp.data, WmsOrderListItem)
    async def add_adjustment_order(self, wid: int = None, remark: str = None, product_list: list = None) -> InventoryreceiptStorageadjustmentAddadjustmentorderResponse | None:
        """创建已完成的数量调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder", {k: v for k, v in {"wid": wid, "remark": remark, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageadjustmentAddadjustmentorderResponse)
    async def add_rebrand_adjustment_order(self, wid: int = None, remark: str = None, bin_type: int = None, product_list: list = None) -> InventoryreceiptStorageadjustmentAddrebrandadjustmentorderResponse | None:
        """创建已完成的换标调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    bin_type: 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位, int.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder", {k: v for k, v in {"wid": wid, "remark": remark, "bin_type": bin_type, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageadjustmentAddrebrandadjustmentorderResponse)
    async def add_sku_adjustment_order(self, wid: int = None, remark: str = None, bin_type: int = None, product_list: list = None) -> InventoryreceiptStorageadjustmentAddskuadjustmentorderResponse | None:
        """创建已完成的SKU调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    bin_type: 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位, int.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder", {k: v for k, v in {"wid": wid, "remark": remark, "bin_type": bin_type, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageadjustmentAddskuadjustmentorderResponse)
    async def add_storage_process_order(self, type: int = None, wid: int = None, remark: str = None, product_list: list = None) -> InventoryreceiptStorageprocessAddstorageprocessorderResponse | None:
        """创建加工单 / 拆分单.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder

Args:
    type: 单据类型：1 加工单，2 拆分单 (required), int.
    wid: 系统仓库id (required), int.
    remark: 备注, string.
    product_list: 产品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder", {k: v for k, v in {"type": type, "wid": wid, "remark": remark, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageprocessAddstorageprocessorderResponse)
    async def bin_create(self, wid: int = None, code: str = None, type: int = None) -> dict:
        """添加仓位.

POST /erp/sc/routing/storage/wareHouseBin/create

Args:
    wid: 仓库id (required), int.
    code: 仓位名称 (required), string.
    type: 仓位类型： 5 可用 6 次品 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/create", {k: v for k, v in {"wid": wid, "code": code, "type": type}.items() if v is not None})
        return resp.data or {}
    async def cancel_wms_order(self, orderNumbers: Any = None, tagType: str = None, orderComment: str = None) -> WmsorderCancelResponse | None:
        """销售出库单截单.

POST /basicOpen/wmsOrder/cancel

Args:
    orderNumbers: 系统单号 对应查询销售出库单列表data>>order_number字段 (required), array.
    tagType: 截单标签，3-5：待人工审核；3-17：其他 (required), string.
    orderComment: 截单备注, string."""
        resp = await self._post("/basicOpen/wmsOrder/cancel", {k: v for k, v in {"orderNumbers": orderNumbers, "tagType": tagType, "orderComment": orderComment}.items() if v is not None})
        return self._parse_one(resp.data, WmsorderCancelResponse)
    async def check_add_order(self, wid: int = None, is_display_check: int = None, check_uid: int = None, remark: str = None, product_list: list = None) -> InventoryreceiptInventorycheckAddorderResponse | None:
        """创建已完成的盘点单.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder

Args:
    wid: 盘点仓库id,对应领星系统的仓库id (required), int.
    is_display_check: 是否明盘：0 否，1 是【默认值】 (required), int.
    check_uid: 盘点人id (required), int.
    remark: 单据备注, string.
    product_list: 盘点明细 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder", {k: v for k, v in {"wid": wid, "is_display_check": is_display_check, "check_uid": check_uid, "remark": remark, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptInventorycheckAddorderResponse)
    async def check_get_order_detail(self, order_sn: str = None, search_field: str = None, search_value: str = None, sort_field: str = None, sort_type: str = None, page: int = None, page_size: int = None) -> list[InventoryreceiptInventorycheckGetorderdetailResponse]:
        """查询盘点单详情.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail

Args:
    order_sn: 盘点单号 (required), string.
    search_field: 搜索字段： sku SKU fnsku FNSKU product_name 品名 whb_code_text 仓位 whb_type_text 仓位类型, string.
    search_value: 搜索值, string.
    sort_field: 排序字段： book_inventory 账面库存 actual_inventory 实盘库存 different_count 库存差异, string.
    sort_type: 排序规则：desc 降序【默认】，asc 升序, string.
    page: 分页页码，默认1【控制 product_list 返回数目】, int.
    page_size: 分页长度，默认20【控制 product_list 返回数目】, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail", {k: v for k, v in {"order_sn": order_sn, "search_field": search_field, "search_value": search_value, "sort_field": sort_field, "sort_type": sort_type, "page": page, "page_size": page_size}.items() if v is not None})
        return self._parse_list(resp.data, InventoryreceiptInventorycheckGetorderdetailResponse)
    async def check_get_order_list(self, wid: str = None, check_type: str = None, date_field: str = None, start_date: str = None, end_date: str = None, search_field: str = None, search_value: str = None, status: int = None, page: int = None, page_size: int = None) -> list[InventoryreceiptInventorycheckGetorderlistResponse]:
        """查询盘点单列表.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList

Args:
    wid: 盘点仓库id，多个使用英文逗号分隔, string.
    check_type: 盘点类型，多个盘点类型用英文逗号分隔： 1 整仓盘点 2 SKU盘点 3 仓位盘点 4 SKU+仓位盘点, string.
    date_field: 搜索时间类型： create_date 创建时间【默认值】 check_date 盘点时间, string.
    start_date: 开始日期，格式：Y-m-d, string.
    end_date: 结束日期，格式：Y-m-d, string.
    search_field: 搜索字段： order_sn 盘点单号 create_user 创建人 check_user 盘点人 remark 备注, string.
    search_value: 搜索值, string.
    status: 盘点状态： 10 待盘点 20 预锁 30 盘点中 40 已盘点 121 待审核 122 已驳回 123 通过 124 作废, int.
    page: 分页页码，默认1, int.
    page_size: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList", {k: v for k, v in {"wid": wid, "check_type": check_type, "date_field": date_field, "start_date": start_date, "end_date": end_date, "search_field": search_field, "search_value": search_value, "status": status, "page": page, "page_size": page_size}.items() if v is not None})
        return self._parse_list(resp.data, InventoryreceiptInventorycheckGetorderlistResponse)
    async def create_receipt_order(self, **kwargs) -> dict:
        """写操作 createReceiptOrder. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def finish_receive_allocation_order(self, **kwargs) -> dict:
        """写操作 finishReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_packing_data(self, overseas_order_no: str = None) -> list[OwmsInboundGetpackingdataResponse]:
        """查询备货单装箱信息.

POST /erp/sc/routing/owms/inbound/getPackingData

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/getPackingData", {k: v for k, v in {"overseas_order_no": overseas_order_no}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundGetpackingdataResponse)
    async def get_process_order_lists(self, type: Any = None, wid: Any = None, process_sn: Any = None, status: Any = None, search_field_time: Any = None, start_date: Any = None, end_date: Any = None, offset: Any = None, length: Any = None) -> list[InventoryreceiptStorageprocessGetorderlistsResponse]:
        """加工单列表.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists

Args:
    type: 单据类型：1加工单，2拆分单, 是.
    wid: 仓库id，多个用英文逗号分隔, 否.
    process_sn: 加工单号，多个用英文逗号分隔, 否.
    status: 加工状态： 0 待配货 1 待完成 2 已完成, 否.
    search_field_time: 时间搜索维度： create_time 创建时间 finish_time 完成时间 update_time 更新时间, 否.
    start_date: 开始时间，格式：Y-m-d, 否.
    end_date: 结束时间，格式：Y-m-d, 否.
    offset: 分页偏移量，默认0, 是.
    length: 分页长度，默认500, 是."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists", {k: v for k, v in {"type": type, "wid": wid, "process_sn": process_sn, "status": status, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, GetProcessOrderListsItem)
    async def get_storage_adjust_order_list(self, search_date_type: int = None, start_date: str = None, end_date: str = None, order_sn: str = None, adjust_status: int = None, wid: str = None, type: int = None, page: int = None, page_size: int = None) -> list[InventoryreceiptStorageadjustmentGetstorageadjustorderlistResponse]:
        """查询调整单列表.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList

Args:
    search_date_type: 时间类型： 1 创建时间 2 调整时间 3 更新时间, int.
    start_date: 开始日期，格式：Y-m-d, string.
    end_date: 结束日期，格式：Y-m-d, string.
    order_sn: 调整单号，多个使用英文逗号分隔, string.
    adjust_status: 单据状态： 5 待提交 10 待调整 20 已完成 30 已删除 121 待审批 122 已驳回, int.
    wid: 系统仓库id，多个使用英文逗号分隔, string.
    type: 调整类型： 0 数量调整 1 换标调整 2 sku调整, int.
    page: 当前页码，默认1, int.
    page_size: 分页条数，默认20, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList", {k: v for k, v in {"search_date_type": search_date_type, "start_date": start_date, "end_date": end_date, "order_sn": order_sn, "adjust_status": adjust_status, "wid": wid, "type": type, "page": page, "page_size": page_size}.items() if v is not None})
        return self._parse_list(resp.data, GetStorageAdjustOrderListItem)
    async def get_storage_allocation_list(self, wid: str = None, to_wid: str = None, search_date_type: int = None, start_date: str = None, end_date: str = None, page: int = None, page_size: int = None) -> list[InventoryreceiptStorageallocationGetstorageallocationlistResponse]:
        """查询调拨单列表.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList

Args:
    wid: 出库仓库id，多个以英文逗号分隔, string.
    to_wid: 入库仓库id，多个以英文逗号分隔, string.
    search_date_type: 时间类型：【不传或传空则默认为 1】 1 创建时间 2 调拨时间 3 完成时间 4 更新时间, int.
    start_date: 开始日期，格式：Y-m-d，只有和结束日期同时有值才会生效, string.
    end_date: 结束日期，格式：Y-m-d，只有和开始日期同时有值才会生效, string.
    page: 当前页码，默认1, int.
    page_size: 分页条数，默认15, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList", {k: v for k, v in {"wid": wid, "to_wid": to_wid, "search_date_type": search_date_type, "start_date": start_date, "end_date": end_date, "page": page, "page_size": page_size}.items() if v is not None})
        return self._parse_list(resp.data, InventoryreceiptStorageallocationGetstorageallocationlistResponse)
    async def inbound_batches_receipt(self, overseas_order_no: str = None, product_list: list = None) -> dict:
        """备货单分批收货.

POST /erp/sc/routing/owms/inbound/batchesReceipt

Args:
    overseas_order_no: 备货单号 (required), string.
    product_list: 产品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/batchesReceipt", {k: v for k, v in {"overseas_order_no": overseas_order_no, "product_list": product_list}.items() if v is not None})
        return resp.data or {}
    async def inbound_complete_receipt(self, overseas_order_no: str = None) -> list | dict:
        """备货单结束到货.

POST /erp/sc/routing/owms/inbound/completeReceipt

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/completeReceipt", {k: v for k, v in {"overseas_order_no": overseas_order_no}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_get_custom_types(self, **kwargs) -> tuple[list[StorageInboundGetcustomtypesResponse], int]:
        """获取自定义入库类型.

POST /erp/sc/routing/storage/inbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/inbound/getCustomTypes", kwargs if kwargs else None)
        return self._parse_page(resp.data, InboundGetCustomTypesItem)
    async def inboundget_orders(self, offset: int = None, length: int = None, wid: int = None, search_field_time: str = None, start_date: str = None, end_date: str = None, order_sn: str = None, inbound_idempotent_code: str = None, status: int = None, type: int = None) -> list[StorageInboundGetordersResponse]:
        """查询入库单列表.

POST /erp/sc/routing/storage/inbound/getOrders

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    wid: 系统仓库id, int.
    search_field_time: 日期筛选类型： 创建时间 create_time 入库时间 opt_time 更新时间 increment_time, string.
    start_date: 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sn: 入库单单号，多个使用英文逗号分隔, string.
    inbound_idempotent_code: 客户参考单号，多个使用英文逗号分隔, string.
    status: 入库单状态： 10 待提交 20 待入库 40 已完成 50 已撤销 121 待审批 122 已驳回, int.
    type: 入库类型： -1 其他入库（含所有自定义类型）  1 其他入库（非自定义类型） 2 采购入库 3 调拨入库 4 赠品入库 26 退货入库 27 移除入库, int."""
        resp = await self._post("/erp/sc/routing/storage/inbound/getOrders", {k: v for k, v in {"offset": offset, "length": length, "wid": wid, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "order_sn": order_sn, "inbound_idempotent_code": inbound_idempotent_code, "status": status, "type": type}.items() if v is not None})
        return self._parse_list(resp.data, InboundgetOrdersItem)
    async def inventory_bin_details(self, wid: str = None, bin_type_list: str = None, offset: int = None, length: int = None) -> list[LocalInventoryInventorybindetailsResponse]:
        """查询仓位库存明细.

POST /erp/sc/routing/data/local_inventory/inventoryBinDetails

Args:
    wid: 仓库id，多个仓库用英文逗号分隔，默认所有仓库, string.
    bin_type_list: 仓位类型，多个类型用英文逗号分隔： 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20 ，上限500, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryBinDetails", {k: v for k, v in {"wid": wid, "bin_type_list": bin_type_list, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, InventoryBinDetailsItem)
    async def list_inbound(self, status: int = None, sub_status: int = None, s_wid: list = None, r_wid: list = None, overseas_order_no: str = None, create_time_from: str = None, create_time_to: str = None, page_size: int = None, page: int = None, date_type: str = None, is_delete: int = None) -> list[OwmsInboundListinboundResponse]:
        """查询海外仓备货单列表.

POST /erp/sc/routing/owms/inbound/listInbound

Args:
    status: 状态： 10 待审核 20 已驳回 30 待配货 40 待发货 50 待收货 51 已撤销 60 已完成, int.
    sub_status: 子状态：【仅在待收货状态下生效】  0 全部  1 未收货  2 部分收货, int.
    s_wid: 发货仓库id, array.
    r_wid: 收货仓库id, array.
    overseas_order_no: 备货单号, string.
    create_time_from: 查询开始日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    create_time_to: 查询结束日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    page_size: 分页数量，最大50，默认20, int.
    page: 当前页码，默认1, int.
    date_type: 备货单时间查询类型：【默认create_time】 delivery_time 发货时间 create_time 创建时间 receive_time 收货时间 update_time 更新时间, string.
    is_delete: 订单是否删除： 0 未删除【默认】 1 已删除 2 全部, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/listInbound", {k: v for k, v in {"status": status, "sub_status": sub_status, "s_wid": s_wid, "r_wid": r_wid, "overseas_order_no": overseas_order_no, "create_time_from": create_time_from, "create_time_to": create_time_to, "page_size": page_size, "page": page, "date_type": date_type, "is_delete": is_delete}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundListinboundResponse)
    async def list_order_nos(self, inbound_order_no: list = None) -> list[OwmsInboundListordernosResponse]:
        """获取备货单号.

POST /erp/sc/routing/owms/inbound/listOrderNos

Args:
    inbound_order_no: 客户参考号 数组, array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/listOrderNos", {k: v for k, v in {"inbound_order_no": inbound_order_no}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundListordernosResponse)
    async def match_sku_list(self, wid: str = None, is_matched: int = None, offset: int = None, length: int = None) -> list[OwmsInboundMatchskulistResponse]:
        """查询系统产品与第三方海外仓产品映射列表.

POST /erp/sc/routing/owms/inbound/matchSkuList

Args:
    wid: 仓库id，多个用英文逗号分隔 (required), string.
    is_matched: 是否配对：【空表示都返回】 0 未配对 1 配对, int.
    offset: 分页偏移量, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/matchSkuList", {k: v for k, v in {"wid": wid, "is_matched": is_matched, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundMatchskulistResponse)
    async def outbound_get_custom_types(self, **kwargs) -> tuple[list[StorageOutboundGetcustomtypesResponse], int]:
        """获取自定义出库类型.

POST /erp/sc/routing/storage/outbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/outbound/getCustomTypes", kwargs if kwargs else None)
        return self._parse_page(resp.data, OutboundGetCustomTypesItem)
    async def outbound_order_delete(self, orderSn: list = None) -> OutboundorderOutboundDeleteResponse | None:
        """删除出库单.

POST /basicOpen/outboundOrder/outbound/delete

Args:
    orderSn: 出库单单号, array."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/delete", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None})
        return self._parse_one(resp.data, OutboundorderOutboundDeleteResponse)
    async def outboundget_orders(self, offset: int = None, length: int = None, wid: str = None, search_field_time: str = None, start_date: str = None, end_date: str = None, order_sn: str = None, idempotent_code: str = None, status: int = None, type: int = None) -> list[StorageOutboundGetordersResponse]:
        """查询出库单列表.

POST /erp/sc/routing/storage/outbound/getOrders

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    wid: 系统仓库id, string.
    search_field_time: 日期筛选类型： 创建时间 create_time 出库时间 opt_time 更新时间 increment_time, string.
    start_date: 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sn: 出库单单号，多个使用英文逗号分隔, string.
    idempotent_code: 客户参考号，多个使用英文逗号分隔, string.
    status: 出库单状态： 10 待提交 30 待出库 40 已完成 50 已撤销 121 待审批 122 已驳回, int.
    type: 出库类型： 11 其他出库 12 FBA出库 14 退货出库 15 调拨出库 16 WFS出库 17 Temu出库 18 销毁出库, int."""
        resp = await self._post("/erp/sc/routing/storage/outbound/getOrders", {k: v for k, v in {"offset": offset, "length": length, "wid": wid, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "order_sn": order_sn, "idempotent_code": idempotent_code, "status": status, "type": type}.items() if v is not None})
        return self._parse_list(resp.data, OutboundgetOrdersItem)
    async def oversea_stock_order_allocate(self, orderNo: str = None) -> dict:
        """备货单分配库存.

POST /basicOpen/overSeaWarehouse/stockOrder/allocate

Args:
    orderNo: 备货单号 (required), string."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/allocate", {k: v for k, v in {"orderNo": orderNo}.items() if v is not None})
        return resp.data or {}
    async def package_label(self, size: int = None, overseas_order_no: str = None) -> list[OwmsInboundPackagelabelResponse]:
        """获取第三方箱唛.

POST /erp/sc/routing/owms/inbound/packageLabel

Args:
    size: 尺寸映射： 1=西邮尺寸专属 2=谷仓A4 3=谷仓100x100 4=谷仓100x150 5=谷仓100x60 11=易仓A4(按SKU) 12=易仓A4(按箱) 13=易仓100x100(无产品名称) 14=易仓100x150(无产品名称) 15=易仓100x100(有产品名称) 16=易仓100x150(有产品名称) 17=易仓100x100(二维码) 18=易仓70x30(显示条码) 19=易仓70x30(无条码) (required), int.
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/packageLabel", {k: v for k, v in {"size": size, "overseas_order_no": overseas_order_no}.items() if v is not None})
        return self._parse_list(resp.data, OwmsInboundPackagelabelResponse)
    async def packing(self, overseas_order_no: str = None, packaging_type: int = None, box_count: int = None, box_list: list = None) -> list | dict:
        """上传备货单装箱信息.

POST /erp/sc/routing/owms/inbound/packing

Args:
    overseas_order_no: 备货单号 (required), string.
    packaging_type: 装箱类型：1 每箱多个sku，2 每箱一个sku (required), int.
    box_count: 总箱数 (required), int.
    box_list: 装箱数据 (required), array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/packing", {k: v for k, v in {"overseas_order_no": overseas_order_no, "packaging_type": packaging_type, "box_count": box_count, "box_list": box_list}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def partly_receive_allocation_order(self, **kwargs) -> dict:
        """写操作 partlyReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def product_label(self, **kwargs) -> list | dict:
        """获取第三方SKU标签PDF文件.

POST /erp/sc/routing/owms/inbound/productLabel"""
        resp = await self._post("/erp/sc/routing/owms/inbound/productLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def quality_inspection_order_detail(self, **kwargs) -> list[QualityinspectionorderDetailResponse]:
        """查询质检单详情.

POST /basicOpen/qualityInspectionOrder/detail"""
        resp = await self._post("/basicOpen/qualityInspectionOrder/detail", kwargs if kwargs else None)
        return self._parse_list(resp.data, QualityinspectionorderDetailResponse)
    async def receive_allocation_order(self, orderSnMany: str = None) -> dict:
        """调拨单全部收货.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder

Args:
    orderSnMany: 调拨单号，支持多个，英文逗号分隔 (required), string."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder", {k: v for k, v in {"orderSnMany": orderSnMany}.items() if v is not None})
        return resp.data or {}
    async def removal_inbound_list(self, status: int = None, start_date: str = None, end_date: str = None, order_no: list = None, offset: int = None, length: int = None) -> list[OwmsRemovalinboundListResponse]:
        """查询移除入库单列表.

POST /erp/sc/routing/owms/removalInbound/list

Args:
    status: 订单状态： 1 待提交-未提交 2 待提交-提交中 3 待提交-失败 4 待收货-未收货 5 待收货-异常 6 已完成 7 已作废, int.
    start_date: 开始日期【发货日期，双闭区间】, string.
    end_date: 结束日期【发货日期，双闭区间】, string.
    order_no: 移除入库单号, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int."""
        resp = await self._post("/erp/sc/routing/owms/removalInbound/list", {k: v for k, v in {"status": status, "start_date": start_date, "end_date": end_date, "order_no": order_no, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, RemovalInboundListItem)
    async def set_tracking_no(self, waybill_no: str = None, wo_number: str = None, tracking_no: str = None, logistics_freight: str = None, logistics_freight_currency_code: str = None, pkg_fee_weight: str = None, pkg_fee_weight_unit: str = None) -> dict:
        """物流下单 - 编辑运单号/跟踪号.

POST /basicOpen/logisticsOrdering/setTrackingNo

Args:
    waybill_no: 运单号 (required), string.
    wo_number: 销售出库单号 (required), string.
    tracking_no: 跟踪号, string.
    logistics_freight: 物流运费, string.
    logistics_freight_currency_code: 物流运费币种： CNY USD EUR JPY AUD CAD MXN GBP INR AED SGD SAR BRL SEK PLN TRY HKD, string.
    pkg_fee_weight: 计费重, string.
    pkg_fee_weight_unit: 计费重单位： g kg, string."""
        resp = await self._post("/basicOpen/logisticsOrdering/setTrackingNo", {k: v for k, v in {"waybill_no": waybill_no, "wo_number": wo_number, "tracking_no": tracking_no, "logistics_freight": logistics_freight, "logistics_freight_currency_code": logistics_freight_currency_code, "pkg_fee_weight": pkg_fee_weight, "pkg_fee_weight_unit": pkg_fee_weight_unit}.items() if v is not None})
        return resp.data or {}
    async def submit_allocation_order(self, sys_wid: int = None, sys_to_wid: int = None, freight_fee: str = None, other_fee: str = None, fee_part_type: int = None, remark: str = None, predict_time: str = None, type: str = None, out_bin_type: str = None, product_list: list = None) -> InventoryreceiptStorageallocationSubmitallocationorderResponse | None:
        """创建待调拨的调拨单.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder

Args:
    sys_wid: 系统出库仓库ID (required), int.
    sys_to_wid: 系统入库仓库ID (required), int.
    freight_fee: 运费, string.
    other_fee: 其他费用, string.
    fee_part_type: 费用分摊方式：0 不分摊【默认值】，2 按sku数量分摊，3 按重量，4 按体积，5 按自定义, int.
    remark: 备注, string.
    predict_time: 预计到货时间, string.
    type: 默认为2-标准调拨, string.
    out_bin_type: 默认0 出库仓位不为空时必传1 (required), string.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder", {k: v for k, v in {"sys_wid": sys_wid, "sys_to_wid": sys_to_wid, "freight_fee": freight_fee, "other_fee": other_fee, "fee_part_type": fee_part_type, "remark": remark, "predict_time": predict_time, "type": type, "out_bin_type": out_bin_type, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, InventoryreceiptStorageallocationSubmitallocationorderResponse)
    async def switch_status(self, wid: str = None, whbCode: str = None, status: int = None) -> StorageWarehousebinSwitchstatusResponse | None:
        """启用、禁用仓位.

POST /erp/sc/routing/storage/wareHouseBin/switchStatus

Args:
    wid: 仓库id (required), string.
    whbCode: 仓位名称 (required), string.
    status: 仓位状态：0 禁用，1 启用 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/switchStatus", {k: v for k, v in {"wid": wid, "whbCode": whbCode, "status": status}.items() if v is not None})
        return self._parse_one(resp.data, StorageWarehousebinSwitchstatusResponse)
    async def update_inbound(self, overseas_order_no: str = None, logistics_id: int = None, estimated_time: str = None, arrival_time: str = None, share_id: int = None, remark: str = None, file_id: str = None, overseas_type: int = None, real_delivery_time: str = None, logistics_list_type: int = None, product_list: list = None, head_logistics_list: Any = None, logistics_list: list = None) -> dict:
        """更新备货单.

POST /erp/sc/routing/owms/inbound/updateInbound

Args:
    overseas_order_no: 海外仓备货单号 (required), string.
    logistics_id: 物流方式id【按计费重分摊时，需传对应物流方式，以获取材积参数用于计算】, int.
    product_list: 产品信息, array.
    estimated_time: 预计到货时间, string.
    arrival_time: 实际到货时间, string.
    share_id: 头程费分配方式： 0 按计费重【默认值】 1 按实重 2 按体积重 3 按SKU数量 4自定义, int.
    remark: 备注, string.
    file_id: 附件id, string.
    overseas_type: 下单至第三方【当收货仓为API海外仓时可填，不填默认为是】：1 否，2 是【默认】, int.
    real_delivery_time: 实际发货时间，格式：Y-m-d H:i:s, string.
    logistics_list_type: 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateInbound", {k: v for k, v in {"overseas_order_no": overseas_order_no, "logistics_id": logistics_id, "estimated_time": estimated_time, "arrival_time": arrival_time, "share_id": share_id, "remark": remark, "file_id": file_id, "overseas_type": overseas_type, "real_delivery_time": real_delivery_time, "logistics_list_type": logistics_list_type, "product_list": product_list, "head_logistics_list": head_logistics_list, "logistics_list": logistics_list}.items() if v is not None})
        return resp.data or {}
    async def ware_house_bin_statement(self, wid: str = None, type: str = None, bin_type_list: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None) -> list[LocalInventoryWarehousebinstatementResponse]:
        """查询仓位流水.

POST /erp/sc/routing/data/local_inventory/wareHouseBinStatement

Args:
    wid: 仓库ID，多个仓库ID用英文逗号,分隔，传或者传空则默认所有仓库, string.
    type: 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】 16 换标入库 17 加工入库 18 拆分入库 19 其他入库 22 采购入库 23 委外入库 24 调拨入库 25 盘盈入库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 41 调拨出库 42 其他出库 65 WFS出库 71 采购上架 72 委外上架 100 库存调整 200 成本补录 30001 已撤销, string.
    bin_type_list: 仓位类型：【多个类型用逗号分隔】 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品, string.
    start_date: 操作开始时间，Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseBinStatement", {k: v for k, v in {"wid": wid, "type": type, "bin_type_list": bin_type_list, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, WareHouseBinStatementItem)
    async def warehouse_bin(self, wid: str = None, id: str = None, status: str = None, type: str = None, offset: int = None, limit: int = None) -> list[LocalInventoryWarehousebinResponse]:
        """查询本地仓位列表.

POST /erp/sc/routing/data/local_inventory/warehouseBin

Args:
    wid: 仓库ID，字符串id，多个使用英文逗号分隔, string.
    id: 仓位ID，字符串id，多个使用英文逗号分隔, string.
    status: 仓位状态： 1 禁用 2 启用, string.
    type: 仓位类型： 5 可用 6 次品, string.
    offset: 分页偏移量，默认为0, int.
    limit: 限制条数，默认20条, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/warehouseBin", {k: v for k, v in {"wid": wid, "id": id, "status": status, "type": type, "offset": offset, "limit": limit}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryWarehousebinResponse)
    async def wms_order_get_wms_logistics_labels(self, wo_number_arr: list = None, order_number_arr: list = None) -> list[WmsOrderGetwmslogisticslabelsResponse]:
        """查询销售出库单物流面单.

POST /erp/sc/routing/wms/order/getWmsLogisticsLabels

Args:
    wo_number_arr: 销售出库单号,上限50【销售出库单号与系统单号二选一必填】, array.
    order_number_arr: 系统单号,上限50【销售出库单号与系统单号二选一必填】, array."""
        resp = await self._post("/erp/sc/routing/wms/order/getWmsLogisticsLabels", {k: v for k, v in {"wo_number_arr": wo_number_arr, "order_number_arr": order_number_arr}.items() if v is not None})
        return self._parse_list(resp.data, WmsOrderGetwmslogisticslabelsResponse)

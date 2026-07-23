"""FBA发货 API endpoints."""
from __future__ import annotations
from typing import TypedDict

from typing import Any

from ..models.responses.fba import GetFbaProductListItem, GetHeadLogisticsFeeTypesItem, GetInboundShipmentListItem, GetSeaTrackSupplierCarriersItem, ShipmentPlanListsItem
from ..models.responses.fba import (
    FbaPlanAllocateStorageResponse,
    FbaPlanReleaseStorageResponse,
    StaCancelInboundPlanResponse,
    StaCommitDeliverTimeResponse,
    StaConfirmPlacementResponse,
    StaCreateInboundPlanResponse,
    StaDetailResponse,
    StaGatherInboundPlanResponse,
    StaGenerateDeliveryDateResponse,
    StaGeneratePlacementResponse,
    StaGenerateTransportResponse,
    StaGetDeliveryDateResponse,
    StaGetPackingBoxInfoResponse,
    StaGetPrepDetailsResponse,
    StaGetTransportResponse,
    StaListGroupPackingResponse,
    StaListPackingGroupResponse,
    StaOperateResponse,
    StaPageResponse,
    StaSaveLocalPackingResponse,
    StaSetDeliveryServiceResponse,
    StaSetPackingResponse,
    StaShipmentPreviewResponse,
    StaUpdateShipmentPackingResponse,
    StaUpdateShipmentTrackResponse,
    FbaReportReceivedinventoryResponse,
    FbaReportShipmentlistResponse,
    FbaReportShipmentplanlistsResponse,
    FbaShipmentBoxinfoResponse,
    FbaShipmentCreateshipfromaddressResponse,
    FbaShipmentGetfbaproductlistResponse,
    FbaShipmentGetheadlogisticsfeetypesResponse,
    FbaShipmentGetseatracksuppliercarriersResponse,
    FbaShipmentShipfromaddresslistResponse,
    FbaShipmentSyncshipmentResponse,
    GetinvoiceInvoiceBatchsendgoodsResponse,
    OpenapiFbashipmentShoppingaddressResponse,
    StorageShipmentCreatereadysendorderResponse,
    StorageShipmentCreatesendedorderResponse,
    StorageShipmentCreateshipmentplanResponse,
    StorageShipmentGetinboundshipmentlistResponse,
    StorageShipmentGetinboundshipmentlistmwsdetailResponse,
    StorageShipmentGetinboundshipmentlistmwsdetaillistResponse,
    StorageShipmentPrintfbalabelsResponse,
    StorageShipmentPrintfnskulabelsResponse,
    StorageShipmentSearchprocessresultResponse,
)
from ._base import BaseEndpoint


class StaSaveLocalPackingReq(TypedDict, total=False):
    boxes: list
    inboundPlanId: str
    packingGroupId: str
    shipmentId: str

class InboundPlanItemReq(TypedDict, total=False):
    expiration: str
    labelOwner: str
    msku: str
    prepOwner: str
    quantity: int
    prepCategory: str
    prepTypes: list
    invoiceSns: list


class StaCreateInboundPlanReq(TypedDict, total=False):
    addressLine1: str
    addressLine2: str
    city: str
    companyName: str
    countryCode: str
    email: str
    phoneNumber: str
    planName: str
    positionType: str
    postalCode: str
    remark: str
    shipperName: str
    sid: int
    stateOrProvinceCode: str
    inboundPlanItems: list  # List[InboundPlanItemReq]


class FbaPlanAllocateStorageReq(TypedDict, total=False):
    orderNos: list
    isComboAutoProcess: int

class FbaPlanReleaseStorageReq(TypedDict, total=False):
    orderNos: list

class PackagegroupingsItemReq(TypedDict, total=False):
    boxes: list

class StaSetPackingReq(TypedDict, total=False):
    inboundPlanId: str
    packageGroupings: list

class StaGeneratePlacementReq(TypedDict, total=False):
    inboundPlanId: str
    sid: int

class StaConfirmPlacementReq(TypedDict, total=False):
    inboundPlanId: str
    placementOptionId: str
    shipmentIds: list
    sid: int

class ShipmentidlistItemReq(TypedDict, total=False):
    palletList: list

class StaGenerateTransportReq(TypedDict, total=False):
    inboundPlanId: str
    shipmentIdList: list

class StaGenerateDeliveryDateReq(TypedDict, total=False):
    inboundPlanId: str
    shipmentId: str
    sid: int

class StaCommitDeliverTimeReq(TypedDict, total=False):
    deliveryWindowOptionId: str
    endDate: str
    inboundPlanId: str
    shipmentId: str
    sid: int
    startDate: str

class ShipmentdistributioninfoItemReq(TypedDict, total=False):
    alphaCode: str
    alphaName: str
    declaredAmount: float
    declaredCode: str
    deliveryWindowOptionId: str
    endDate: str
    freightClass: str
    palletList: list

class StaSetDeliveryServiceReq(TypedDict, total=False):
    inboundPlanId: str
    shipmentDistributionInfo: list

class BoxesItemReq(TypedDict, total=False):
    contentInformationSource: str
    dimensions: dict
    items: list

class StaUpdateShipmentPackingReq(TypedDict, total=False):
    boxes: list

class TrackbolistItemReq(TypedDict, total=False):
    boxId: str
    localBoxId: str
    trackingId: str

class StaUpdateShipmentTrackReq(TypedDict, total=False):
    billOfLadingNumber: str
    freightBillNumber: str
    inboundPlanId: str
    shipmentConfirmationId: str
    shipmentId: str
    sid: int
    trackBOList: list

class StaCancelInboundPlanReq(TypedDict, total=False):
    inboundPlanId: str
    sid: int

class StaOperateReq(TypedDict, total=False):
    taskId: str

class StaGatherInboundPlanReq(TypedDict, total=False):
    inboundPlanIdList: list
    sid: int

class StaDetailReq(TypedDict, total=False):
    inboundPlanId: str
    sid: int


class FBAEndpoints(BaseEndpoint):
    """领星FBA发货 API (56个接口)."""

    async def fba_plan_allocate_storage(self, data: Optional[FbaPlanAllocateStorageReq] = None) -> FbaPlanAllocateStorageResponse | None:
        """FBA仓发货计划锁库存.

POST /basicOpen/openapi/fba/allocateStorage

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/openapi/fba/allocateStorage", data or {})
        return self._parse_one(resp.data, FbaPlanAllocateStorageResponse)

    async def fba_plan_release_storage(self, data: Optional[FbaPlanReleaseStorageReq] = None) -> FbaPlanReleaseStorageResponse | None:
        """FBA仓发货计划释放库存.

POST /basicOpen/openapi/fba/releaseStorage

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/basicOpen/openapi/fba/releaseStorage", data or {})
        return self._parse_one(resp.data, FbaPlanReleaseStorageResponse)

    async def sta_create_inbound_plan(self, data: Optional[StaCreateInboundPlanReq] = None) -> StaCreateInboundPlanResponse | None:
        """创建STA任务.

POST /amzStaServer/openapi/inbound-plan/createInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/createInboundPlan", data or {})
        return self._parse_one(resp.data, StaCreateInboundPlanResponse)

    async def sta_list_packing_group(self, inbound_plan_id: str = None, sid: int = None) -> list[StaListPackingGroupResponse]:
        """查询包装组.

POST /amzStaServer/openapi/inbound-packing/listPackingGroupItems

Args:
    inbound_plan_id: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/listPackingGroupItems", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaListPackingGroupResponse)

    async def sta_save_local_packing(self, data: Optional[StaSaveLocalPackingReq] = None) -> StaSaveLocalPackingResponse | None:
        """保存装箱信息.

POST /amzStaServer/openapi/inbound-packing/setLocalPackingInformation

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/setLocalPackingInformation", data or {})
        return self._parse_one(resp.data, StaSaveLocalPackingResponse)

    async def sta_set_packing(self, data: Optional[StaSetPackingReq] = None) -> StaSetPackingResponse | None:
        """提交装箱信息.

POST /amzStaServer/openapi/inbound-packing/setPackingInformation

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/setPackingInformation", data or {})
        return self._parse_one(resp.data, StaSetPackingResponse)

    async def sta_generate_placement(self, data: Optional[StaGeneratePlacementReq] = None) -> StaGeneratePlacementResponse | None:
        """生成货件方案.

POST /amzStaServer/openapi/inbound-shipment/generatePlacementOptions

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/generatePlacementOptions", data or {})
        return self._parse_one(resp.data, StaGeneratePlacementResponse)

    async def sta_shipment_preview(self, inbound_plan_id: str = None, sid: int = None) -> list[StaShipmentPreviewResponse]:
        """查询货件方案.

POST /amzStaServer/openapi/inbound-shipment/shipmentPreView

Args:
    inbound_plan_id: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/shipmentPreView", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaShipmentPreviewResponse)

    async def sta_get_packing_box_info(self, inbound_plan_id: str = None, sid: int = None) -> list[StaGetPackingBoxInfoResponse]:
        """查询货件方案的装箱信息.

POST /amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo

Args:
    inbound_plan_id: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaGetPackingBoxInfoResponse)

    async def sta_confirm_placement(self, data: Optional[StaConfirmPlacementReq] = None) -> StaConfirmPlacementResponse | None:
        """确认货件方案.

POST /amzStaServer/openapi/inbound-shipment/confirmPlacementOption

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/confirmPlacementOption", data or {})
        return self._parse_one(resp.data, StaConfirmPlacementResponse)

    async def sta_generate_transport(self, data: Optional[StaGenerateTransportReq] = None) -> StaGenerateTransportResponse | None:
        """生成承运方式.

POST /amzStaServer/openapi/inbound-shipment/generateTransportList

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/generateTransportList", data or {})
        return self._parse_one(resp.data, StaGenerateTransportResponse)

    async def sta_generate_delivery_date(self, data: Optional[StaGenerateDeliveryDateReq] = None) -> StaGenerateDeliveryDateResponse | None:
        """生成可选送达时间.

POST /amzStaServer/openapi/inbound-shipment/generateDeliveryDateList

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/generateDeliveryDateList", data or {})
        return self._parse_one(resp.data, StaGenerateDeliveryDateResponse)

    async def sta_get_transport(self, inbound_plan_id: str = None, shipment_id: str = None, sid: int = None) -> list[StaGetTransportResponse]:
        """查询承运方式.

POST /amzStaServer/openapi/inbound-shipment/getTransportList

Args:
    inbound_plan_id: see API doc.
    shipment_id: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/getTransportList", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "shipmentId": shipment_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaGetTransportResponse)

    async def sta_get_delivery_date(self, inbound_plan_id: str = None, shipment_id: str = None, sid: int = None) -> list[StaGetDeliveryDateResponse]:
        """查询可选送达时间.

POST /amzStaServer/openapi/inbound-shipment/getDeliveryDateList

Args:
    inbound_plan_id: see API doc.
    shipment_id: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/getDeliveryDateList", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "shipmentId": shipment_id, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaGetDeliveryDateResponse)

    async def sta_commit_deliver_time(self, data: Optional[StaCommitDeliverTimeReq] = None) -> StaCommitDeliverTimeResponse | None:
        """提交送达时间.

POST /amzStaServer/openapi/inbound-shipment/commitStaDeliverTime

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/commitStaDeliverTime", data or {})
        return self._parse_one(resp.data, StaCommitDeliverTimeResponse)

    async def sta_set_delivery_service(self, data: Optional[StaSetDeliveryServiceReq] = None) -> StaSetDeliveryServiceResponse | None:
        """提交货件配送服务.

POST /amzStaServer/openapi/inbound-shipment/setDeliveryService

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/setDeliveryService", data or {})
        return self._parse_one(resp.data, StaSetDeliveryServiceResponse)

    async def sta_update_shipment_packing(self, data: Optional[StaUpdateShipmentPackingReq] = None) -> StaUpdateShipmentPackingResponse | None:
        """修改货件装箱信息.

POST /amzStaServer/openapi/inbound-packing/updateShipmentPacking

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/updateShipmentPacking", data or {})
        return self._parse_one(resp.data, StaUpdateShipmentPackingResponse)

    async def sta_update_shipment_track(self, data: Optional[StaUpdateShipmentTrackReq] = None) -> StaUpdateShipmentTrackResponse | None:
        """上传货件跟踪号.

POST /amzStaServer/openapi/inbound-shipment/updateShipmentTrack

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-shipment/updateShipmentTrack", data or {})
        return self._parse_one(resp.data, StaUpdateShipmentTrackResponse)

    async def sta_cancel_inbound_plan(self, data: Optional[StaCancelInboundPlanReq] = None) -> StaCancelInboundPlanResponse | None:
        """取消STA任务.

POST /amzStaServer/openapi/inbound-plan/cancelInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/cancelInboundPlan", data or {})
        return self._parse_one(resp.data, StaCancelInboundPlanResponse)

    async def sta_operate(self, data: Optional[StaOperateReq] = None) -> StaOperateResponse | None:
        """查询异步任务状态.

POST /amzStaServer/openapi/task-plan/operate

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/task-plan/operate", data or {})
        return self._parse_one(resp.data, StaOperateResponse)

    async def sta_get_prep_details(self, sid: int = None, msku: str = None) -> list[StaGetPrepDetailsResponse]:
        """获取商品预处理信息.

POST /amzStaServer/openapi/inbound-packing/getPrepDetails

Args:
    sid: see API doc.
    msku: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-packing/getPrepDetails", {k: v for k, v in {"sid": sid, "msku": msku}.items() if v is not None})
        return self._parse_list(resp.data, StaGetPrepDetailsResponse)

    async def sta_gather_inbound_plan(self, data: Optional[StaGatherInboundPlanReq] = None) -> StaGatherInboundPlanResponse | None:
        """同步STA任务到ERP.

POST /amzStaServer/openapi/inbound-plan/gatherInboundPlan

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/gatherInboundPlan", data or {})
        return self._parse_one(resp.data, StaGatherInboundPlanResponse)

    async def sta_page(self, page: int = None, length: int = None, date_begin: str = None, date_end: str = None, date_type: int = None, plan_name: str = None, shipment_id_list: list = None, sids: list = None, sort_field: str = None, sort_type: str = None) -> list[StaPageResponse]:
        """查询STA任务列表.

POST /amzStaServer/openapi/inbound-plan/page

Args:
    page: see API doc.
    length: see API doc.
    date_begin: see API doc.
    date_end: see API doc.
    date_type: see API doc.
    plan_name: see API doc.
    shipment_id_list: see API doc.
    sids: see API doc.
    sort_field: see API doc.
    sort_type: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/page", {k: v for k, v in {"page": page, "length": length, "dateBegin": date_begin, "dateEnd": date_end, "dateType": date_type, "planName": plan_name, "shipmentIdList": shipment_id_list, "sids": sids, "sortField": sort_field, "sortType": sort_type}.items() if v is not None})
        return self._parse_list(resp.data, StaPageResponse)

    async def sta_detail(self, data: Optional[StaDetailReq] = None) -> StaDetailResponse | None:
        """查询STA任务详情.

POST /amzStaServer/openapi/inbound-plan/detail

Args:
    data: 请求体，字段参考接口文档, dict."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/detail", data or {})
        return self._parse_one(resp.data, StaDetailResponse)

    async def sta_list_group_packing(self, inbound_plan_id: str = None, packing_group_id_list: list = None, sid: int = None) -> list[StaListGroupPackingResponse]:
        """查询STA任务包装组装箱信息.

POST /amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking

Args:
    inbound_plan_id: see API doc.
    packing_group_id_list: see API doc.
    sid: see API doc."""
        resp = await self._post("/amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking", {k: v for k, v in {"inboundPlanId": inbound_plan_id, "packingGroupIdList": packing_group_id_list, "sid": sid}.items() if v is not None})
        return self._parse_list(resp.data, StaListGroupPackingResponse)

    async def box_info(self, sid: int = None, shipment_id: str = None) -> list[FbaShipmentBoxinfoResponse]:
        """查询货件装箱信息.

POST /erp/sc/routing/fba/shipment/boxInfo

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    shipment_id: 货件编号 (required), string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/boxInfo", {k: v for k, v in {"sid": sid, "shipment_id": shipment_id}.items() if v is not None})
        return self._parse_list(resp.data, FbaShipmentBoxinfoResponse)
    async def create_sended_order(self, wid: int = None, sys_wid: int = None, expected_arrival_date: str = None, etd_date: str = None, eta_date: str = None, delivery_date: str = None, actual_shipment_time: str = None, head_fee_type: int = None, tax_fee_type: int = None, is_points_behind: int = None, points_behind_coeffient: int = None, logistics_channel_id: int = None, is_related: int = None, request_flag: str = None, ship_mode: int = None, hand_pick_purchase: int = None, remark: str = None, box_type: str = None, box_remark: str = None, logistics_list_type: int = None, list_field: Any = None, box_list: list = None, head_logistics_list: Any = None, logistics_list: list = None) -> StorageShipmentCreatesendedorderResponse | None:
        """生成已发货的发货单.

POST /erp/sc/storage/shipment/createSendedOrder

Args:
    wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid, int.
    sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (required), int.
    expected_arrival_date: 预计到达时间：Y-m-d, string.
    etd_date: 开船时间，格式：Y-m-d, string.
    eta_date: 预计到港时间，格式：Y-m-d, string.
    delivery_date: 实际妥投时间，格式：Y-m-d, string.
    actual_shipment_time: 实际发货时间，格式：Y-m-d, string.
    head_fee_type: 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积, int.
    tax_fee_type: 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 5 箱子-体积, int.
    is_points_behind: 是否分抛计算：0 否，1 是，头程分摊方式为按计费重时用, int.
    points_behind_coeffient: 分抛系数：0~100，分抛计算选是时必填, int.
    logistics_channel_id: 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】, int.
    is_related: 组合商品扣减库存时是否自动拆分成单品进行扣减： 0 否 1 是【会拆分组合商品】, int.
    request_flag: 自定义请求标识，本次请求超时后可根据此标识查询此次请求的结果，由请求方保持标识唯一性, string.
    ship_mode: 发货方式：1-默认，2-工厂直发, int.
    hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是, int.
    remark: 备注, string.
    box_type: 装箱类型： SINGLE 每箱只允许一款SKU MULTIPLE 每箱允许多款SKU, string.
    box_remark: 装箱备注, string.
    box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填, array.
    logistics_list_type: 物流信息版本： 0 旧版 1 新版, int.
    head_logistics_list: 新版头程物流信息 (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/storage/shipment/createSendedOrder", {k: v for k, v in {"wid": wid, "sys_wid": sys_wid, "expected_arrival_date": expected_arrival_date, "etd_date": etd_date, "eta_date": eta_date, "delivery_date": delivery_date, "actual_shipment_time": actual_shipment_time, "head_fee_type": head_fee_type, "tax_fee_type": tax_fee_type, "is_points_behind": is_points_behind, "points_behind_coeffient": points_behind_coeffient, "logistics_channel_id": logistics_channel_id, "is_related": is_related, "request_flag": request_flag, "ship_mode": ship_mode, "hand_pick_purchase": hand_pick_purchase, "remark": remark, "box_type": box_type, "box_remark": box_remark, "logistics_list_type": logistics_list_type, "list_field": list_field, "box_list": box_list, "head_logistics_list": head_logistics_list, "logistics_list": logistics_list}.items() if v is not None})
        return self._parse_one(resp.data, StorageShipmentCreatesendedorderResponse)
    async def create_ship_from_address(self, sid: int = None, alias_name: str = None, country_name: str = None, sender_name: str = None, street_detail1: str = None, street_detail2: str = None, city: str = None, region: str = None, province: str = None, zip_code: str = None, phone: str = None) -> FbaShipmentCreateshipfromaddressResponse | None:
        """地址簿-发货地址创建.

POST /erp/sc/routing/fba/shipment/createShipFromAddress

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    alias_name: 地址簿别名，店铺内唯一 (required), string.
    country_name: 发货国家/地区 (required), string.
    sender_name: 发货方名称 (required), string.
    street_detail1: 街道地址1 (required), string.
    street_detail2: 街道地址2, string.
    city: 城市 (required), string.
    region: 区, string.
    province: 省/州/地区，美国发货地址限制长度为2位 (required), string.
    zip_code: 邮政编码 (required), string.
    phone: 电话号码, string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/createShipFromAddress", {k: v for k, v in {"sid": sid, "alias_name": alias_name, "country_name": country_name, "sender_name": sender_name, "street_detail1": street_detail1, "street_detail2": street_detail2, "city": city, "region": region, "province": province, "zip_code": zip_code, "phone": phone}.items() if v is not None})
        return self._parse_one(resp.data, FbaShipmentCreateshipfromaddressResponse)
    async def create_shipment_plan(self, remark: str = None, product_list: list = None) -> StorageShipmentCreateshipmentplanResponse | None:
        """创建FBA发货计划.

POST /erp/sc/routing/storage/shipment/createShipmentPlan

Args:
    remark: 批次信息备注, string.
    product_list: 商品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/createShipmentPlan", {k: v for k, v in {"remark": remark, "product_list": product_list}.items() if v is not None})
        return self._parse_one(resp.data, StorageShipmentCreateshipmentplanResponse)
    async def fba_received_inventory(self, sid: int = None, event_date: str = None, fba_shipment_id: list = None, offset: int = None, length: int = None) -> FbaReportReceivedinventoryResponse | None:
        """查询FBA到货接收明细.

POST /erp/sc/data/fba_report/receivedInventory

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    event_date: 签收日期，格式：Y-m-d，未填写fba_shipment_id时必填 (required), string.
    fba_shipment_id: 货件单号，未填写event_date时必填, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int."""
        resp = await self._post("/erp/sc/data/fba_report/receivedInventory", {k: v for k, v in {"sid": sid, "event_date": event_date, "fba_shipment_id": fba_shipment_id, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_one(resp.data, FbaReportReceivedinventoryResponse)
    async def fba_shipment_list(self, sid: str = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None, shipment_id: str = None, shipment_status: str = None, extra_date_field: str = None, start_extra_date: str = None, end_extra_date: str = None) -> list[FbaReportShipmentlistResponse]:
        """查询货件列表.

POST /erp/sc/data/fba_report/shipmentList

Args:
    sid: 店铺id，多个以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    start_date: 货件创建开始日期，格式：Y-m-d，左闭右开 (required), string.
    end_date: 货件创建截止日期，格式：Y-m-d，左闭右开 (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int.
    shipment_id: 货件单号，多个以英文逗号隔开，仅支持精确搜索, string.
    shipment_status: 货件状态，多个以英文逗号分隔： UNCONFIRMED IN_TRANSIT DELIVERED CHECKED_IN ABANDONED  DELETED CLOSED CANCELLED WORKING RECEIVING SHIPPED READY_TO_SHIP, string.
    extra_date_field: 根据start_extra_date和end_extra_date日期范围查询： update 货件修改日期【默认值为update，目前只支持查询货件修改日期】, string.
    start_extra_date: 开始日期，格式：Y-m-d，左闭右开, string.
    end_extra_date: 结束日期，格式：Y-m-d，左闭右开, string."""
        resp = await self._post("/erp/sc/data/fba_report/shipmentList", {k: v for k, v in {"sid": sid, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, "shipment_id": shipment_id, "shipment_status": shipment_status, "extra_date_field": extra_date_field, "start_extra_date": start_extra_date, "end_extra_date": end_extra_date}.items() if v is not None})
        return self._parse_list(resp.data, FbaReportShipmentlistResponse)
    async def get_fba_product_list(self, sids: list = None, search_field: str = None, search_value: str = None, offset: int = None, length: int = None) -> list[FbaShipmentGetfbaproductlistResponse]:
        """查询FBA商品信息列表.

POST /erp/sc/routing/fba/shipment/getFbaProductList

Args:
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 模糊搜索字段：【搜索时支持以下单个字段】 msku=>MSKU fnsku=>FNSKU asin=>ASIN sku=>SKU title=>标题 product_name=>品名, string.
    search_value: 搜索值【对应搜索字段的值】, string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/getFbaProductList", {k: v for k, v in {"sids": sids, "search_field": search_field, "search_value": search_value, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, GetFbaProductListItem)
    async def get_head_logistics_fee_types(self, **kwargs) -> list[FbaShipmentGetheadlogisticsfeetypesResponse]:
        """获取发货单头程物流信息-其他费类型.

POST /erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes"""
        resp = await self._post("/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetHeadLogisticsFeeTypesItem)
    async def get_inbound_shipment_list(self, search_value: str = None, search_field: str = None, sids: str = None, mids: str = None, wid: str = None, logistics_type: list = None, status: int = None, print_status: str = None, pick_status: str = None, time_type: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None, is_delete: float = None, senior_search_list: list = None) -> tuple[list[StorageShipmentGetinboundshipmentlistResponse], int]:
        """查询发货单列表.

POST /erp/sc/routing/storage/shipment/getInboundShipmentList

Args:
    search_value: 搜索的值, string.
    search_field: 搜索字段： sku shipment_sn 发货单号 shipment_id 货件单号, string.
    sids: 店铺id,多个时通过英文逗号分隔,如1,2,3，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    mids: 国家id,多个时通过英文逗号分隔,如1,2,3, string.
    wid: 仓库id,多个时通过英文逗号分隔,如1,2,3, string.
    logistics_type: 物流方式id, array.
    status: 发货单状态： -1 : 待配货，  0：待发货， 1：已发货， 3：已作废， 4：已删除, int.
    print_status: 打印状态 0未打印 1 已打印, string.
    pick_status: 拣货状态 0 未拣货 1已拣货, string.
    time_type: 时间类型：  3创建时间 (允许精确到时分秒)  2创建时间  1到货时间   0发货时间  4更新时间 (允许精确到时分秒), int.
    start_date: 开始日期, string.
    end_date: 结束日期, string.
    offset: 偏移量=（currentPage -1）*length (required), int.
    length: 长度 (required), int.
    is_delete: 是否删除：0 未删除【默认】 1 已删除 2 全部, number.
    senior_search_list: 精准搜索, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentList", {k: v for k, v in {"search_value": search_value, "search_field": search_field, "sids": sids, "mids": mids, "wid": wid, "logistics_type": logistics_type, "status": status, "print_status": print_status, "pick_status": pick_status, "time_type": time_type, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, "is_delete": is_delete, "senior_search_list": senior_search_list}.items() if v is not None})
        return self._parse_page(resp.data, GetInboundShipmentListItem)
    async def get_inbound_shipment_list_mws_detail_list(self, shipment_sn_arr: Any = None, return_deleted: bool = None) -> list[StorageShipmentGetinboundshipmentlistmwsdetaillistResponse]:
        """批量查询发货单详情.

POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList

Args:
    shipment_sn_arr: 发货单号数组，上限50 (required), array.
    return_deleted: 是否返回已删除数据: false-否(默认)，true-是, boolean."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList", {k: v for k, v in {"shipment_sn_arr": shipment_sn_arr, "return_deleted": return_deleted}.items() if v is not None})
        return self._parse_list(resp.data, StorageShipmentGetinboundshipmentlistmwsdetaillistResponse)
    async def get_sea_track_supplier_carriers(self, vehicle_type: str = None) -> list[FbaShipmentGetseatracksuppliercarriersResponse]:
        """获取发货单头程物流信息-承运商信息.

POST /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers

Args:
    vehicle_type: 运输类型【默认Sea】： Sea 海运 Express 快递 Aviation 空运, string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers", {k: v for k, v in {"vehicle_type": vehicle_type}.items() if v is not None})
        return self._parse_list(resp.data, GetSeaTrackSupplierCarriersItem)
    async def invalid_shipment_sn(self, shipmentNos: Any = None, isReturnStock: int = None, isReturnStockAux: int = None, cancelReason: str = None) -> list | dict:
        """FBA-作废发货单.

POST /basicOpen/openapi/fbaShipment/shipmentSn/invalid

Args:
    shipmentNos: 发货单号 (required), array.
    isReturnStock: 产品库存是否恢复 1恢复 0不恢复 (required), int.
    isReturnStockAux: 辅料库存是否恢复 1恢复 0不恢复 (required), int.
    cancelReason: 作废原因, string."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shipmentSn/invalid", {k: v for k, v in {"shipmentNos": shipmentNos, "isReturnStock": isReturnStock, "isReturnStockAux": isReturnStockAux, "cancelReason": cancelReason}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def send_goods(self, shipment_nos: Any = None) -> dict:
        """FBA发货单发货.

POST /erp/sc/storage/shipment/sendGoods

Args:
    shipment_nos: 发货单号列表 (required), array."""
        resp = await self._post("/erp/sc/storage/shipment/sendGoods", {k: v for k, v in {"shipment_nos": shipment_nos}.items() if v is not None})
        return resp.data or {}
    async def ship_from_address_list(self, sid: list = None, search_field: str = None, search_value: str = None, offset: int = None, length: int = None) -> list[FbaShipmentShipfromaddresslistResponse]:
        """地址簿-发货地址列表.

POST /erp/sc/routing/fba/shipment/shipFromAddressList

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 搜索字段： alias_name 地址簿别名 sender_name 发货方名称, string.
    search_value: 对应搜索字段模糊搜索值, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/shipFromAddressList", {k: v for k, v in {"sid": sid, "search_field": search_field, "search_value": search_value, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, FbaShipmentShipfromaddresslistResponse)
    async def shipment_lock_stock(self, shipment_nos: Any = None, is_auto_batch: int = None) -> list | dict:
        """发货单分配库存.

POST /erp/sc/routing/storage/shipment/lockStock

Args:
    shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (required), array.
    is_auto_batch: 是否锁定至批次，1：是，0：否，默认为否，否：只锁定库存数量，发货时按先进先出规则匹配出库批次；是：按先进先锁规则自动指定批次并锁定，发货时按锁定批次出库；分配库存后，可在【查询发货单详情】接口的采购信息中查看锁定的批次, int."""
        resp = await self._post("/erp/sc/routing/storage/shipment/lockStock", {k: v for k, v in {"shipment_nos": shipment_nos, "is_auto_batch": is_auto_batch}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipment_plan_lists(self, sids: str = None, wid: str = None, packing_type: str = None, search_field_time: str = None, search_field: str = None, search_value: str = None, status: str = None, mids: str = None, offset: int = None, length: int = None, start_date: str = None, end_date: str = None) -> list[FbaReportShipmentplanlistsResponse]:
        """查询FBA发货计划.

POST /erp/sc/data/fba_report/shipmentPlanLists

Args:
    sids: 店铺ids，12,13组成，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    wid: 仓库id, string.
    packing_type: 包装类型2原装 1混装, string.
    search_field_time: 查找时间字段(gmt_create-创建时间,estimated_delivery_time-计划发货时间)，不传该字段默认为gmt_create, string.
    search_field: 查找字段  order_sn发货计划单号, string.
    search_value: 查找值, string.
    status: 状态, string.
    mids: 国家id, string.
    offset: 偏移量 0 偏移量 (currentPage -1) * length, int.
    length: 长度 默认20, int.
    start_date: 开始日期 如:2021-09-07, string.
    end_date: 结束日期 如:2021-09-08, string."""
        resp = await self._post("/erp/sc/data/fba_report/shipmentPlanLists", {k: v for k, v in {"sids": sids, "wid": wid, "packing_type": packing_type, "search_field_time": search_field_time, "search_field": search_field, "search_value": search_value, "status": status, "mids": mids, "offset": offset, "length": length, "start_date": start_date, "end_date": end_date}.items() if v is not None})
        return self._parse_list(resp.data, ShipmentPlanListsItem)
    async def shopping_address(self, id: int = None) -> OpenapiFbashipmentShoppingaddressResponse | None:
        """地址簿-配送地址详情.

POST /basicOpen/openapi/fbaShipment/shoppingAddress

Args:
    id: 唯一记录id，查询FBA列表接口对应字段【id】 (required), int."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shoppingAddress", {k: v for k, v in {"id": id}.items() if v is not None})
        return self._parse_one(resp.data, OpenapiFbashipmentShoppingaddressResponse)
    async def sync_shipment(self, sid: int = None, shipment_ids: Any = None, sync_anyway: int = None) -> FbaShipmentSyncshipmentResponse | None:
        """同步亚马逊货件到ERP.

POST /erp/sc/routing/fba/shipment/syncShipment

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    shipment_ids: 货件编号 (required), array.
    sync_anyway: 报错是否继续：0 否【默认】，1 是 当系统检测到货件归属国家与店铺不符时，会提示报错，此时传1则按照店铺进行同步, int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/syncShipment", {k: v for k, v in {"sid": sid, "shipment_ids": shipment_ids, "sync_anyway": sync_anyway}.items() if v is not None})
        return self._parse_one(resp.data, FbaShipmentSyncshipmentResponse)
    async def update_custom_cost(self, shipment_sn: str = None, is_custom_cost: int = None, list_field: list = None) -> dict:
        """更新发货单自定义成本.

POST /erp/sc/routing/storage/shipment/updateCustomCost

Args:
    shipment_sn: 发货单号 (required), string.
    is_custom_cost: 是否自定义成本 (required), int.
    list: 自定义成本信息数组, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateCustomCost", {k: v for k, v in {"shipment_sn": shipment_sn, "is_custom_cost": is_custom_cost, "list_field": list_field}.items() if v is not None})
        return resp.data or {}
    async def update_plan_lists(self, order_sn: str = None, shipment_time: str = None, packing_type: int = None, logistics_provider_id: int = None, logistics_channel_id: int = None, shipment_plan_quantity: int = None, quantity_in_case: int = None, box_num: int = None, sys_wid: int = None, cg_package_length: float = None, cg_package_width: float = None, cg_package_height: float = None, cg_box_length: float = None, cg_box_width: float = None, cg_box_height: float = None, nw: float = None, gw: float = None, cg_box_weight: float = None, remark: str = None) -> dict:
        """编辑FBA发货计划.

POST /erp/sc/routing/storage/shipment/updateShipmentPlan

Args:
    order_sn: 发货计划单号 (required), string.
    shipment_time: 发货时间，格式：Y-m-d, string.
    packing_type: 包装类型： 1 混装，2 原厂, int.
    logistics_provider_id: 物流商id, int.
    logistics_channel_id: 物流渠道id, int.
    shipment_plan_quantity: 计划发货量, int.
    quantity_in_case: 单箱数量（PCS）, int.
    box_num: 箱数, int.
    sys_wid: 系统仓库id【发货仓库】, int.
    cg_package_length: 包装规格长（cm）【保留两位小数】, number.
    cg_package_width: 包装规格宽（cm）【保留两位小数】, number.
    cg_package_height: 包装规格高（cm）【保留两位小数】, number.
    cg_box_length: 箱规长（cm）【保留两位小数】, number.
    cg_box_width: 箱规宽（cm）【保留两位小数】, number.
    cg_box_height: 箱规高（cm）【保留两位小数】, number.
    nw: 单品净重（g）【保留两位小数】, number.
    gw: 单品毛重（g）【保留两位小数】, number.
    cg_box_weight: 单箱重量（kg）【保留两位小数】, number.
    remark: 备注, string."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentPlan", {k: v for k, v in {"order_sn": order_sn, "shipment_time": shipment_time, "packing_type": packing_type, "logistics_provider_id": logistics_provider_id, "logistics_channel_id": logistics_channel_id, "shipment_plan_quantity": shipment_plan_quantity, "quantity_in_case": quantity_in_case, "box_num": box_num, "sys_wid": sys_wid, "cg_package_length": cg_package_length, "cg_package_width": cg_package_width, "cg_package_height": cg_package_height, "cg_box_length": cg_box_length, "cg_box_width": cg_box_width, "cg_box_height": cg_box_height, "nw": nw, "gw": gw, "cg_box_weight": cg_box_weight, "remark": remark}.items() if v is not None})
        return resp.data or {}
    async def update_ship_from_address(self, sid: int = None, alias_name: str = None, country_name: str = None, sender_name: str = None, street_detail1: str = None, street_detail2: str = None, city: str = None, region: str = None, province: str = None, zip_code: str = None, phone: str = None, id: int = None) -> dict:
        """地址簿-发货地址修改.

POST /erp/sc/routing/fba/shipment/updateShipFromAddress

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    alias_name: 地址簿别名，店铺内唯一 (required), string.
    country_name: 发货国家/地区 (required), string.
    sender_name: 发货方名称 (required), string.
    street_detail1: 街道地址1 (required), string.
    street_detail2: 街道地址2, string.
    city: 城市 (required), string.
    region: 区, string.
    province: 省/州/地区，美国发货地址限制长度为2位 (required), string.
    zip_code: 邮政编码 (required), string.
    phone: 电话号码, string.
    id: 地址簿-发货地址列表接口返回id (required), int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/updateShipFromAddress", {k: v for k, v in {"sid": sid, "alias_name": alias_name, "country_name": country_name, "sender_name": sender_name, "street_detail1": street_detail1, "street_detail2": street_detail2, "city": city, "region": region, "province": province, "zip_code": zip_code, "phone": phone, "id": id}.items() if v is not None})
        return resp.data or {}
    async def update_shipment_actual_status(self, is_closed: int = None, list_field: list = None) -> dict:
        """修改货件实际状态.

POST /erp/sc/routing/storage/shipment/updateShipmentActualStatus

Args:
    is_closed: 货件状态：0 进行中，1 已完成 (required), int.
    list: 货件信息 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentActualStatus", {k: v for k, v in {"is_closed": is_closed, "list_field": list_field}.items() if v is not None})
        return resp.data or {}
    async def vc_batch_send_goods(self, orderNoList: list = None) -> GetinvoiceInvoiceBatchsendgoodsResponse | None:
        """VC发货单-确认发货.

POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods

Args:
    orderNoList: orderNo列表, array."""
        resp = await self._post("/basicOpen/openapi/getInvoice/invoice/batchSendGoods", {k: v for k, v in {"orderNoList": orderNoList}.items() if v is not None})
        return self._parse_one(resp.data, GetinvoiceInvoiceBatchsendgoodsResponse)
    async def create_ready_send_order(self, wid: int = None, sys_wid: int = None, expected_arrival_date: str = None, etd_date: str = None, eta_date: str = None, delivery_date: str = None, actual_shipment_time: str = None, head_fee_type: int = None, tax_fee_type: int = None, is_points_behind: int = None, points_behind_coeffient: int = None, logistics_channel_id: int = None, is_related: int = None, vat_code: str = None, is_pick: int = None, remark: str = None, ship_mode: int = None, hand_pick_purchase: int = None, box_type: str = None, box_remark: str = None, logistics_list_type: int = None, list_field: Any = None, box_list: list = None, head_logistics_list: Any = None, logistics_list: list = None) -> StorageShipmentCreatereadysendorderResponse | None:
        """生成待发货的发货单.

POST /erp/sc/routing/storage/shipment/createReadySendOrder

Args:
    wid: 自定义仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。, int.
    sys_wid: 系统仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。多仓库发货时传 -1。, int.
    expected_arrival_date: 预计到达时间，格式：Y-m-d, string.
    etd_date: 开船时间，格式：Y-m-d, string.
    eta_date: 预计到港时间，格式：Y-m-d, string.
    delivery_date: 实际妥投时间，格式：Y-m-d, string.
    actual_shipment_time: 实际发货时间，格式：Y-m-d, string.
    head_fee_type: 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积, int.
    tax_fee_type: 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积, int.
    is_points_behind: 是否分抛计算：0 否，1 是；头程分摊方式为按计费重时用, int.
    points_behind_coeffient: 分抛系数：0~100,分抛计算选是时必填, int.
    logistics_channel_id: 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】, int.
    is_related: 是否关联普通商品： 0 否 1 是【会拆分组合商品】, int.
    vat_code: 店铺VAT税号, string.
    is_pick: 是否拣货：【默认0】 0 否 1 是, int.
    remark: 备注, string.
    ship_mode: 发货方式：1-默认，2-工厂直发, int.
    hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是, int.
    box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU, string.
    box_remark: 装箱备注, string.
    box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填 (required), array.
    logistics_list_type: 物流信息版本： 0 旧版 1 新版, int.
    head_logistics_list: 新版头程物流信息 (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/createReadySendOrder", {k: v for k, v in {"wid": wid, "sys_wid": sys_wid, "expected_arrival_date": expected_arrival_date, "etd_date": etd_date, "eta_date": eta_date, "delivery_date": delivery_date, "actual_shipment_time": actual_shipment_time, "head_fee_type": head_fee_type, "tax_fee_type": tax_fee_type, "is_points_behind": is_points_behind, "points_behind_coeffient": points_behind_coeffient, "logistics_channel_id": logistics_channel_id, "is_related": is_related, "vat_code": vat_code, "is_pick": is_pick, "remark": remark, "ship_mode": ship_mode, "hand_pick_purchase": hand_pick_purchase, "box_type": box_type, "box_remark": box_remark, "logistics_list_type": logistics_list_type, "list_field": list_field, "box_list": box_list, "head_logistics_list": head_logistics_list, "logistics_list": logistics_list}.items() if v is not None})
        return self._parse_one(resp.data, StorageShipmentCreatereadysendorderResponse)
    async def get_inbound_shipment_list_mws_detail(self, shipment_sn: str = None, return_deleted: bool = None) -> list[StorageShipmentGetinboundshipmentlistmwsdetailResponse]:
        """查询发货单详情.

POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail

Args:
    shipment_sn: 发货单号 (required), string.
    return_deleted: 是否返回已删除数据: false-否(默认)，true-是, boolean."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail", {k: v for k, v in {"shipment_sn": shipment_sn, "return_deleted": return_deleted}.items() if v is not None})
        return self._parse_list(resp.data, StorageShipmentGetinboundshipmentlistmwsdetailResponse)
    async def outbound_order_release_stock(self, shipment_nos: Any = None) -> dict:
        """发货单释放库存.

POST /erp/sc/routing/storage/shipment/releaseStock

Args:
    shipment_nos: 发货单号 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/releaseStock", {k: v for k, v in {"shipment_nos": shipment_nos}.items() if v is not None})
        return resp.data or {}
    async def print_fba_labels(self, hide_ship_from_company_name: int = None, hide_ship_to_company_name: int = None, print_sta_name_page: int = None, sort_label: int = None, type: str = None, data: list = None) -> StorageShipmentPrintfbalabelsResponse | None:
        """查询FBA货件箱子、卡板标签.

POST /erp/sc/storage/shipment/printFbaLabels

Args:
    data: 请求数据 (required), array.
    hide_ship_from_company_name: 隐藏ship from公司名,默认不隐藏,非必填,传值1为开启, int.
    hide_ship_to_company_name: 传值1为隐藏ship to公司名,默认不隐藏,非必填,传值1为开启, int.
    print_sta_name_page: 传值1为新增任务名称页,默认不新增,非必填,仅打印box箱子标签时生效,传值1为开启, int.
    sort_label: 传值1为按箱子顺序重排,默认不按箱子顺序重排,仅打印box箱子子标签时生效(说明:不按箱子顺序重排时,打印文件, int.
    type: 打印类型：box 箱子标签，card 卡板标签 (required), string."""
        resp = await self._post("/erp/sc/storage/shipment/printFbaLabels", {k: v for k, v in {"hide_ship_from_company_name": hide_ship_from_company_name, "hide_ship_to_company_name": hide_ship_to_company_name, "print_sta_name_page": print_sta_name_page, "sort_label": sort_label, "type": type, "data": data}.items() if v is not None})
        return self._parse_one(resp.data, StorageShipmentPrintfbalabelsResponse)
    async def print_fnsku_labels(self, page_type: str = None, print_content: str = None, content_type: str = None, print_custom: str = None, custom_content: str = None, new_tag: str = None, data: Any = None) -> StorageShipmentPrintfnskulabelsResponse | None:
        """查询FBA货件商品FNSKU标签.

POST /erp/sc/storage/shipment/printFnskuLabels

Args:
    page_type: 标签页面类型： SINGLE_COL_50_30 热敏纸【50X30】单排 SINGLE_COL_70_30 热敏纸【70X30】单排 DOUBLE_COL_100_30 热敏纸【100X30】双排 A4_FOUR_COL_40 A4纸【每页40个标签】四排 A4_FOUR_COL_44 A4纸【每页44个标签】四排 US_LETTER_THREE_COL_30 美国信纸【每页30个标签】三排 (required), string.
    print_content: 是否打印：【默认yes】 yes 是 no 否, string.
    content_type: 打印SKU/品名：【默认sku】 sku SKU sku_name 品名, string.
    print_custom: 是否打印自定义内容：【默认yes】 yes 是 no 否, string.
    custom_content: 自定义内容，默认MADE IN CHINA, string.
    new_tag: 标签中是否显示‘new’字样：【默认yes】 yes 是 no 否, string."""
        resp = await self._post("/erp/sc/storage/shipment/printFnskuLabels", {k: v for k, v in {"page_type": page_type, "print_content": print_content, "content_type": content_type, "print_custom": print_custom, "custom_content": custom_content, "new_tag": new_tag, "data": data}.items() if v is not None})
        return self._parse_one(resp.data, StorageShipmentPrintfnskulabelsResponse)
    async def search_process_result(self, request_flag: str = None) -> list[StorageShipmentSearchprocessresultResponse]:
        """发货单创建接口结果查询.

POST /erp/sc/routing/storage/shipment/searchProcessResult

Args:
    request_flag: 生成单据时传的请求标识 (required), string."""
        resp = await self._post("/erp/sc/routing/storage/shipment/searchProcessResult", {k: v for k, v in {"request_flag": request_flag}.items() if v is not None})
        return self._parse_list(resp.data, StorageShipmentSearchprocessresultResponse)
    async def update_inbound_shipment_list_mws(self, shipment_sn: str = None, remark: str = None, box_type: str = None, items: list = None, box_list: list = None) -> dict:
        """编辑发货单.

POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws

Args:
    shipment_sn: 发货单号 (required), string.
    remark: 备注, string.
    items: 发货商品, array.
    box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU, string.
    box_list: 装箱数据, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateInboundShipmentListMws", {k: v for k, v in {"shipment_sn": shipment_sn, "remark": remark, "box_type": box_type, "items": items, "box_list": box_list}.items() if v is not None})
        return resp.data or {}
    async def update_list_logistics(self, data: list = None, head_logistics_list: Any = None) -> dict:
        """更新发货单物流信息.

POST /erp/sc/routing/storage/shipment/updateListLogistics

Args:
    data: 参数数组 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateListLogistics", {k: v for k, v in {"data": data, "head_logistics_list": head_logistics_list}.items() if v is not None})
        return resp.data or {}

"""Auto-generated response models for FBA."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


# ==================== STA 货件系列 + 发货计划锁/释放库存（US-004 补全，data 透传模式）===================
class FbaPlanAllocateStorageResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class FbaPlanReleaseStorageResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaCancelInboundPlanResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaCommitDeliverTimeResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaConfirmPlacementResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaCreateInboundPlanResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaDetailResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGatherInboundPlanResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGenerateDeliveryDateResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGeneratePlacementResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGenerateTransportResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGetDeliveryDateResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGetPackingBoxInfoResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGetPrepDetailsResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaGetTransportResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaListGroupPackingResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaListPackingGroupResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaOperateResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaPageResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaSaveLocalPackingResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaSetDeliveryServiceResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaSetPackingResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaShipmentPreviewResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaUpdateShipmentPackingResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class StaUpdateShipmentTrackResponse(LingXingModel):
    """STA/FBA 接口响应（最小化，extra=allow 兜底）."""
    msg: Optional[str] = None


class OpenapiInboundPackingGetinboundpackingboxinfoPlacementoptionlist(LingXingModel):
    """placementOptionList sub-structure."""
    placement_option_id: Optional[str] = Field(None, description="货件方案id")
    placement_status: Optional[str] = Field(None, description="状态：含OFFERED、ACCEPTED、EXPIRED")
    shipment_information_list: Optional[list] = Field(None, description="货件信息")

class OpenapiInboundPackingGetinboundpackingboxinfoResponse(LingXingModel):
    """查询货件方案的装箱信息."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    placement_option_list: Optional[List[OpenapiInboundPackingGetinboundpackingboxinfoPlacementoptionlist]] = Field(None, description="货件方案id")


class OpenapiInboundPackingGetprepdetailsResponse(LingXingModel):
    """获取商品预处理信息."""
    sid: Optional[str] = Field(None, description="亚马逊店铺sid")
    msku: Optional[str] = Field(None, description="msku")
    prep_owner: Optional[str] = Field(None, description="预处理方式")
    label_owner: Optional[str] = Field(None, description="标签方式")
    prep_category: Optional[str] = Field(None, description="预处理分类，具体见附加说明")
    prep_types: Optional[list] = Field(None, description="预处理类型集合，具体见附加说明")


class OpenapiInboundPackingListpackinggroupitemsPackinggrouplist(LingXingModel):
    """packingGroupList sub-structure."""
    packing_group_id: Optional[str] = Field(None, description="包装组ID")
    packing_group_item_list: Optional[list] = Field(None, description="包装组商品信息")

class OpenapiInboundPackingListpackinggroupitemsResponse(LingXingModel):
    """查询包装组."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    packing_group_list: Optional[List[OpenapiInboundPackingListpackinggroupitemsPackinggrouplist]] = Field(None, description="包装组")


class OpenapiInboundPackingSetpackinginformationResponse(LingXingModel):
    """提交装箱信息."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundPackingUpdateshipmentpackingResponse(LingXingModel):
    """修改货件装箱信息."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundPlanCancelinboundplanResponse(LingXingModel):
    """取消STA任务."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundPlanCreateinboundplanResponse(LingXingModel):
    """创建STA任务."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundPlanDetailAddressvo(LingXingModel):
    """addressVO sub-structure."""
    address_line1: Optional[str] = Field(None, description="街道地址1")
    address_line2: Optional[str] = Field(None, description="街道地址2")
    city: Optional[str] = Field(None, description="城市")
    country_code: Optional[str] = Field(None, description="国家code")
    country_name: Optional[str] = Field(None, description="国家名称")
    email: Optional[str] = Field(None, description="邮箱")
    phone_number: Optional[str] = Field(None, description="电话号码")
    postal_code: Optional[str] = Field(None, description="邮政编码")
    shipper_name: Optional[str] = Field(None, description="发货方名称")
    state_or_province_code: Optional[str] = Field(None, description="州/省/地区")

class OpenapiInboundPlanDetailProductlist(LingXingModel):
    """productList sub-structure."""
    asin: Optional[str] = Field(None, description="asin")
    fnsku: Optional[str] = Field(None, description="fnsku")
    msku: Optional[str] = Field(None, description="msku")
    parent_asin: Optional[str] = Field(None, description="父asin")
    product_name: Optional[str] = Field(None, description="品名")
    quantity: Optional[int] = Field(None, description="申报量")
    sku: Optional[str] = Field(None, description="sku")
    title: Optional[str] = Field(None, description="标题(【listing】中的标题)")
    url: Optional[str] = Field(None, description="图片url")

class OpenapiInboundPlanDetailShipmentlist(LingXingModel):
    """shipmentList sub-structure."""
    shipment_id: Optional[str] = Field(None, description="货件id")
    shipment_confirmation_id: Optional[str] = Field(None, description="货件单号")
    status: Optional[str] = Field(None, description="货件状态: WORKING READY_TO_SHIP SHIPPED RECEIVING CANCELLED DELETED CLOSED ERROR IN_TRANSIT DELIVERED CHECKED_IN UNCONFIRMED")

class OpenapiInboundPlanDetailResponse(LingXingModel):
    """查询STA任务详情."""
    address_vo: Optional[List[OpenapiInboundPlanDetailAddressvo]] = Field(None, description="发货地址")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    plan_create_time: Optional[str] = Field(None, description="计划创建时间")
    plan_name: Optional[str] = Field(None, description="STA任务名称")
    plan_update_time: Optional[str] = Field(None, description="计划更新时间")
    product_list: Optional[List[OpenapiInboundPlanDetailProductlist]] = Field(None, description="商品信息")
    shipment_list: Optional[List[OpenapiInboundPlanDetailShipmentlist]] = Field(None, description="货件信息")
    status: Optional[str] = Field(None, description="STA任务状态： ACTIVE 进行中 VOIDED 已取消 SHIPPED 已发货")
    position_type: Optional[int] = Field(None, description="分仓方式，1-先装箱再分仓，2-先分仓再装箱")


class OpenapiInboundPlanGatherinboundplanResponse(LingXingModel):
    """同步STA任务到ERP."""
    error_msg: Optional[str] = Field(None, description="失败原因")
    fail_inbound_plan_ids: Optional[list] = Field(None, description="同步失败STA任务编号数组")
    fail_num: Optional[int] = Field(None, description="同步失败数量")
    success_inbound_plan_ids: Optional[list] = Field(None, description="同步成功的STA任务编号数组")
    success_num: Optional[int] = Field(None, description="同步成功数量")


class OpenapiInboundPlanListinboundplangrouppackingPackinggrouplist(LingXingModel):
    """packingGroupList sub-structure."""
    packing_group_id: Optional[str] = Field(None, description="包装组id")
    shipment_packing_list: Optional[list] = Field(None, description="装箱明细")

class OpenapiInboundPlanListinboundplangrouppackingResponse(LingXingModel):
    """查询STA任务包装组装箱信息."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    packing_group_list: Optional[List[OpenapiInboundPlanListinboundplangrouppackingPackinggrouplist]] = Field(None, description="包装组")


class OpenapiInboundPlanPageOrders(LingXingModel):
    """orders sub-structure."""
    asc: Optional[bool] = Field(None, description="是否升序排列")
    column: Optional[str] = Field(None, description="排序列")

class OpenapiInboundPlanPageRecords(LingXingModel):
    """records sub-structure."""
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    inbound_plan_item_list: Optional[list] = Field(None, description="商品信息")
    plan_name: Optional[str] = Field(None, description="STA任务名称")
    shipment_list: Optional[list] = Field(None, description="货件信息")
    status: Optional[str] = Field(None, description="STA任务状态")
    position_type: Optional[int] = Field(None, description="分仓方式，1-先装箱再分仓，2-先分仓再装箱")
    plan_create_time: Optional[str] = Field(None, description="计划创建时间")
    plan_update_time: Optional[str] = Field(None, description="计划更新时间")

class OpenapiInboundPlanPageResponse(LingXingModel):
    """查询STA任务列表."""
    current: Optional[int] = Field(None, description="当前页")
    orders: Optional[List[OpenapiInboundPlanPageOrders]] = Field(None, description="排序")
    pages: Optional[int] = Field(None, description="页数")
    records: Optional[List[OpenapiInboundPlanPageRecords]] = Field(None, description="记录行")
    search_count: Optional[int] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总记录数")


class OpenapiInboundShipmentCommitstadelivertimeResponse(LingXingModel):
    """提交送达时间."""
    operation_id: Optional[str] = Field(None, description="操作id")


class OpenapiInboundShipmentConfirmplacementoptionResponse(LingXingModel):
    """确认货件方案."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundShipmentGeneratedeliverydatelistResponse(LingXingModel):
    """生成可选送达时间."""
    operation_id: Optional[str] = Field(None, description="操作id")


class OpenapiInboundShipmentGenerateplacementoptionsResponse(LingXingModel):
    """生成货件方案."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiInboundShipmentGeneratetransportlistResponse(LingXingModel):
    """生成承运方式."""
    operation_id: Optional[str] = Field(None, description="操作id")


class OpenapiInboundShipmentGetdeliverydatelistShipmentlist(LingXingModel):
    """shipmentList sub-structure."""
    delivery_window_option_id: Optional[str] = Field(None, description="选项id")
    end_date: Optional[str] = Field(None, description="结束时间 格式：yyyy-MM-dd HH:mm:ss")
    start_date: Optional[str] = Field(None, description="开始时间 格式：yyyy-MM-dd HH:mm:ss")
    valid_until: Optional[str] = Field(None, description="过期时间 格式：yyyy-MM-dd HH:mm:ss")

class OpenapiInboundShipmentGetdeliverydatelistResponse(LingXingModel):
    """查询可选送达时间."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    shipment_id: Optional[str] = Field(None, description="货件单号")
    shipment_list: Optional[List[OpenapiInboundShipmentGetdeliverydatelistShipmentlist]] = Field(None, description="可选送达时间")


class OpenapiInboundShipmentGettransportlistTransportvolist(LingXingModel):
    """transportVOList sub-structure."""
    alpha_code: Optional[str] = Field(None, description="承运方式编码")
    alpha_name: Optional[str] = Field(None, description="承运方式名称")
    shipping_mode: Optional[str] = Field(None, description="货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））")
    shipping_solution: Optional[str] = Field(None, description="承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)")
    transportation_option_id: Optional[str] = Field(None, description="承运方式ID")
    alpha_alias_name: Optional[str] = Field(None, description="承运方式别名")

class OpenapiInboundShipmentGettransportlistResponse(LingXingModel):
    """查询承运方式."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    shipment_id: Optional[str] = Field(None, description="货件号")
    transport_vo_list: Optional[List[OpenapiInboundShipmentGettransportlistTransportvolist]] = Field(None, description="承运方式列表")


class OpenapiInboundShipmentListshipmentboxesShipmentlist(LingXingModel):
    """shipmentList sub-structure."""
    pallet_list: Optional[list] = Field(None, description="托帕明细")
    shipment_id: Optional[str] = Field(None, description="货件id")
    shipment_packing_list: Optional[list] = Field(None, description="装箱明细")

class OpenapiInboundShipmentListshipmentboxesResponse(LingXingModel):
    """查询货件装箱信息."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    shipment_list: Optional[List[OpenapiInboundShipmentListshipmentboxesShipmentlist]] = Field(None, description="货件装箱信息")


class OpenapiInboundShipmentSetdeliveryserviceResponse(LingXingModel):
    """提交货件配送服务."""
    operation_id: Optional[str] = Field(None, description="操作id")


class OpenapiInboundShipmentShipmentdetaillistShipmentlist(LingXingModel):
    """shipmentList sub-structure."""
    alpha_code: Optional[str] = Field(None, description="承运方式")
    amazon_reference_id: Optional[str] = Field(None, description="关联号")
    end_date: Optional[str] = Field(None, description="送达时段-结束时间 格式：yyyy-MM-dd HH:mm:ss")
    inbound_region: Optional[str] = Field(None, description="入库区域")
    item_count: Optional[int] = Field(None, description="商品总数")
    item_list: Optional[list] = Field(None, description="商品信息")
    pick_up_id: Optional[str] = Field(None, description="提货单号")
    send_address: Optional[str] = Field(None, description="是")
    shiping_time: Optional[str] = Field(None, description="发货日期 格式：yyyy-MM-dd")
    shipment_confirmation_id: Optional[str] = Field(None, description="货件单号")
    shipment_name: Optional[str] = Field(None, description="货件名称")
    shipping_address: Optional[str] = Field(None, description="是")
    shipping_mode: Optional[str] = Field(None, description="货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））")
    shipping_solution: Optional[str] = Field(None, description="承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)")
    sid: Optional[int] = Field(None, description="店铺ID")
    start_date: Optional[str] = Field(None, description="送达时段-开始时间")
    status: Optional[str] = Field(None, description="货件状态")
    tracking_number_list: Optional[list] = Field(None, description="追踪编号")
    warehouse_id: Optional[str] = Field(None, description="物流中心编码")

class OpenapiInboundShipmentShipmentdetaillistResponse(LingXingModel):
    """查询货件详情."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    shipment_list: Optional[List[OpenapiInboundShipmentShipmentdetaillistShipmentlist]] = Field(None, description="是")


class OpenapiInboundShipmentShipmentpreviewPlacementoptionlist(LingXingModel):
    """placementOptionList sub-structure."""
    fee_count: Optional[float] = Field(None, description="费用")
    fees: Optional[list] = Field(None, description="费用明细：array")
    placement_option_id: Optional[str] = Field(None, description="货件方案id")
    placement_status: Optional[str] = Field(None, description="状态：含OFFERED、ACCEPTED、EXPIRED")
    shipment_information_list: Optional[list] = Field(None, description="货件信息")

class OpenapiInboundShipmentShipmentpreviewResponse(LingXingModel):
    """查询货件方案."""
    inbound_plan_id: Optional[str] = Field(None, description="STA任务编号")
    placement_option_list: Optional[List[OpenapiInboundShipmentShipmentpreviewPlacementoptionlist]] = Field(None, description="货件方案")


class OpenapiInboundShipmentUpdateshipmenttrackResponse(LingXingModel):
    """上传货件跟踪号."""
    error_enums: Optional[list] = Field(None, description="错误编码（让openapi的用户进行后续操作）,OpenApiTypeEnum 枚举值")
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态")


class OpenapiTaskPlanOperateResponse(LingXingModel):
    """查询异步任务状态."""
    error_msg: Optional[str] = Field(None, description="错误信息")
    inbound_plan_id: Optional[str] = Field(None, description="亚马逊任务编号")
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态 process success failure local_failure")


class OpenapiFbashipmentShoppingaddressResponse(LingXingModel):
    """地址簿-配送地址详情."""
    ship_to_address: Optional[str] = Field(None, description="收件人详细地址")
    ship_to_postal_code: Optional[str] = Field(None, description="收件人邮政编码")
    ship_to_country: Optional[str] = Field(None, description="收件国家")
    ship_to_province_code: Optional[str] = Field(None, description="收件省份代码")
    ship_to_city: Optional[str] = Field(None, description="收件城市")
    ship_to_name: Optional[str] = Field(None, description="收件人姓名")
    total: Optional[int] = Field(None, description="总数")


class GetinvoiceInvoiceBatchsendgoodsErrormsg(LingXingModel):
    """errorMsg sub-structure."""
    order_no: Optional[str] = Field(None, description="异常单号")
    error_msg: Optional[str] = Field(None, description="异常信息")

class GetinvoiceInvoiceBatchsendgoodsResponse(LingXingModel):
    """VC发货单-确认发货."""
    error_msg: Optional[List[GetinvoiceInvoiceBatchsendgoodsErrormsg]] = Field(None, description="异常信息列表")
    failed_count: Optional[int] = Field(None, description="failedCount")
    success_count: Optional[int] = Field(None, description="successCount")
    total: Optional[int] = Field(None, description="总记录数")


class FbaReportReceivedinventoryResponse(LingXingModel):
    """查询FBA到货接收明细."""
    sid: Optional[int] = Field(None, description="店铺id, 等于入参sid，非货件实际对应的sid。字段即将下线，具体sid与货件对应关系，请用 [查询货件列表](docs/FBA/FBAShipmentList) 确认")
    received_date: Optional[str] = Field(None, description="接收日期")
    received_date_locale: Optional[str] = Field(None, description="当地接收日期")
    received_date_timestamp: Optional[int] = Field(None, description="接收日期时间戳")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sku: Optional[str] = Field(None, description="MSKU")
    product_name: Optional[str] = Field(None, description="Listing标题")
    quantity: Optional[float] = Field(None, description="数量")
    fba_shipment_id: Optional[str] = Field(None, description="货件单号")
    fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    unique_index: Optional[int] = Field(None, description="单内签收日期索引")
    unique_md5: Optional[str] = Field(None, description="与unique_index组成唯一索引")
    received_date_report: Optional[str] = Field(None, description="处理过的接收日期")
    total: Optional[int] = Field(None, description="总数")


class FbaReportShipmentlistList(LingXingModel):
    """list sub-structure."""
    id: Optional[int] = Field(None, description="唯一记录id")
    sid: Optional[int] = Field(None, description="店铺id")
    seller: Optional[str] = Field(None, description="店铺名称")
    uid: Optional[int] = Field(None, description="创建人id")
    username: Optional[str] = Field(None, description="创建人姓名")
    shipment_id: Optional[str] = Field(None, description="亚马逊货件编号")
    shipment_name: Optional[str] = Field(None, description="货件名称")
    sta_shipment_id: Optional[str] = Field(None, description="亚马逊货件id（sta货件时返回）")
    sta_inbound_plan_id: Optional[str] = Field(None, description="亚马逊货件编号（sta货件时返回）")
    sta_plan_name: Optional[str] = Field(None, description="STA任务名称（sta货件时返回）")
    is_closed: Optional[int] = Field(None, description="是否是已完成状态：0 进行中，1 已完成")
    shipment_status: Optional[str] = Field(None, description="状态： WORKING：卖家已创建货件，但尚未发货 SHIPPED：承运人已取件 IN_TRANSIT：承运人已通知亚马逊配送中心，知晓货件的存在 DELIVERED：承运人已将货件配送至亚马逊配送中心 CHECK_IN：货件已在亚马逊配送中心的收货区域登记 RECEIVING：货件已到达亚马逊配送中心，但有部分商品尚未标记为已收到 CLOSED：货件已到达亚马逊配送中心，且所有商品已标记为...")
    gmt_modified: Optional[str] = Field(None, description="数据更新时间")
    gmt_create: Optional[str] = Field(None, description="数据创建时间")
    sync_time: Optional[str] = Field(None, description="同步时间【已废弃】")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    is_synchronous: Optional[int] = Field(None, description="是否erp创建：0 erp创建，1 亚马逊后台同步")
    is_uploaded_box: Optional[int] = Field(None, description="是否已上传装箱信息：0 未上传，1 已上传")
    is_sta: Optional[int] = Field(None, description="是否sta货件：0 否，1 是")
    shipping_mode: Optional[str] = Field(None, description="货件类型(GROUND_SMALL_PARCEL 小包裹快递（SPD）、FREIGHT_LTL 汽运零担（LTL）)")
    shipping_solution: Optional[str] = Field(None, description="承运人(USE_YOUR_OWN_CARRIER 其他承运人、AMAZON_PARTNERED_CARRIER 亚马逊合作承运人)")
    alpha_code: Optional[str] = Field(None, description="承运方式编码")
    alpha_name: Optional[str] = Field(None, description="承运方式名称")
    sta_shipment_date: Optional[str] = Field(None, description="发货日期 格式：yyyy-MM-dd")
    sta_delivery_start_date: Optional[str] = Field(None, description="送达时段-开始时间 格式：yyyy-MM-dd HH:mm:ss")
    sta_delivery_end_date: Optional[str] = Field(None, description="送达时段-结束时间 格式：yyyy-MM-dd HH:mm:ss")
    tracking_number_list: Optional[list] = Field(None, description="追踪编号（SPD类型货件时返回）")
    bill_of_lading_number: Optional[str] = Field(None, description="提货单号（BOL）")
    freight_bill_number: Optional[str] = Field(None, description="跟踪编号（PRO）")
    item_list: Optional[list] = Field(None, description="子项数据")
    working_time: Optional[str] = Field(None, description="WORKING时间")
    shipped_time: Optional[str] = Field(None, description="SHIPPED时间")
    receiving_time: Optional[str] = Field(None, description="RECEIVING时间")
    closed_time: Optional[str] = Field(None, description="CLOSED时间")
    reference_id: Optional[str] = Field(None, description="Reference ID")
    ship_from_address: Optional[dict] = Field(None, description="发货地址")
    ship_to_address: Optional[dict] = Field(None, description="配送地址")

class FbaReportShipmentlistResponse(LingXingModel):
    """查询货件列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[FbaReportShipmentlistList]] = Field(None, description="数据列表")


class FbaReportShipmentplanlistsCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class FbaReportShipmentplanlistsList(LingXingModel):
    """list sub-structure."""
    ispg_id: Optional[int] = Field(None, description="发货计划组父ID")
    isp_id: Optional[int] = Field(None, description="发货计划id")
    logistics_channel_id: Optional[int] = Field(None, description="物流ID")
    custom_fields: Optional[list] = Field(None, description="自定义字段")
    fnsku: Optional[str] = Field(None, description="fnsku")
    msku: Optional[str] = Field(None, description="seller_sku")
    wid: Optional[int] = Field(None, description="仓库id")
    wname: Optional[str] = Field(None, description="仓库名称")
    sid: Optional[int] = Field(None, description="店铺id")
    create_time: Optional[str] = Field(None, description="创建时间")
    status: Optional[int] = Field(None, description="状态： -5、已驳回， 0、待审核， 5、待处理， 10、已处理")
    packing_type: Optional[int] = Field(None, description="包装类型 2原装 1混装")
    shipment_time: Optional[str] = Field(None, description="计划发货时间")
    shipment_plan_quantity: Optional[int] = Field(None, description="计划发货量")
    seq: Optional[str] = Field(None, description="批次号")
    logistics_name: Optional[str] = Field(None, description="物流名称")
    quantity_in_case: Optional[int] = Field(None, description="单箱数量")
    box_num: Optional[int] = Field(None, description="箱数")
    is_relate_mws: Optional[int] = Field(None, description="是否关联货件")
    is_relate_list: Optional[int] = Field(None, description="是否关联发货单")
    remark: Optional[str] = Field(None, description="备注")
    print_num: Optional[int] = Field(None, description="打印次数")
    create_user: Optional[str] = Field(None, description="创建用户")
    small_image_url: Optional[str] = Field(None, description="商品图片")
    order_sn: Optional[str] = Field(None, description="计划发货单号")
    product_name: Optional[str] = Field(None, description="产品名称")
    product_id: Optional[int] = Field(None, description="产品id")
    sku: Optional[str] = Field(None, description="sku")
    pic_url: Optional[str] = Field(None, description="商品图片")
    is_combo: Optional[int] = Field(None, description="是否组合商品")
    cg_package_length: Optional[str] = Field(None, description="包装长(CM,2位小数)")
    cg_package_height: Optional[str] = Field(None, description="包装高(CM,2位小数)")
    cg_package_width: Optional[str] = Field(None, description="包装宽(CM,2位小数)")
    cg_box_length: Optional[str] = Field(None, description="箱子长(CM,2位小数)")
    cg_box_width: Optional[str] = Field(None, description="箱子宽(CM,2位小数)")
    cg_box_height: Optional[str] = Field(None, description="箱子高(CM,2位小数)")
    cg_box_weight: Optional[str] = Field(None, description="单箱重量(KG,2位小数)")
    cg_box_net_weight: Optional[str] = Field(None, description="单箱净重(KG,2位小数)")
    cg_box_gross_weight: Optional[str] = Field(None, description="单箱毛重(KG,2位小数)")
    is_urgent: Optional[int] = Field(None, description="是否加急（0-否，1-是）")
    storage_list: Optional[list] = Field(None, description="库存列表")
    mws_relate: Optional[list] = Field(None, description="发货单关联")
    status_name: Optional[str] = Field(None, description="状态名称")
    packing_type_name: Optional[str] = Field(None, description="包装类型名称")
    diff_num: Optional[int] = Field(None, description="差额")
    sname: Optional[str] = Field(None, description="店铺")
    nation: Optional[str] = Field(None, description="国家")
    lock_status: Optional[int] = Field(None, description="锁定状态：1-未锁定 2-已锁定 3-已使用")

class FbaReportShipmentplanlistsResponse(LingXingModel):
    """查询FBA发货计划."""
    ispg_id: Optional[int] = Field(None, description="发货计划组id")
    create_time: Optional[str] = Field(None, description="创建时间")
    seq: Optional[str] = Field(None, description="批次号")
    remark: Optional[str] = Field(None, description="创建时间")
    create_user: Optional[str] = Field(None, description="创建用户")
    custom_fields: Optional[List[FbaReportShipmentplanlistsCustomFields]] = Field(None, description="自定义字段")
    list: Optional[List[FbaReportShipmentplanlistsList]] = Field(None, description="子项目列表")
    total: Optional[int] = Field(None, description="发货计划量总数")


class FbaShipmentBoxinfoBoxList(LingXingModel):
    """box_list sub-structure."""
    box_length: Optional[str] = Field(None, description="箱子长")
    box_width: Optional[str] = Field(None, description="箱子宽")
    box_height: Optional[str] = Field(None, description="箱子高")
    box_weight: Optional[str] = Field(None, description="箱子重")
    box_dimensions_unit: Optional[str] = Field(None, description="长度单位，公制：cm，英制：in")
    box_weight_unit: Optional[str] = Field(None, description="重量单位，公制：kg，英制：lb")
    box_num: Optional[float] = Field(None, description="箱数")
    is_pile: Optional[int] = Field(None, description="LTL合作承运人是否允许箱子堆叠：0 否，1 是")
    box_mskus: Optional[list] = Field(None, description="箱内产品（LTL合作承运人时为空）")

class FbaShipmentBoxinfoResponse(LingXingModel):
    """查询货件装箱信息."""
    total: Optional[int] = Field(None, description="总数")
    box_type: Optional[str] = Field(None, description="装箱类型： SINGLE 每箱1款SKU MULTIPLE 每箱多款SKU")
    box_list: Optional[List[FbaShipmentBoxinfoBoxList]] = Field(None, description="箱子信息")
    is_partner: Optional[float] = Field(None, description="是否为亚马逊合作承运人:0 否，1 是")
    carrier_name: Optional[str] = Field(None, description="承运方式")
    transport_type: Optional[str] = Field(None, description="货件类型：SPD，LTL")


class FbaShipmentCreateshipfromaddressResponse(LingXingModel):
    """地址簿-发货地址创建."""
    id: Optional[int] = Field(None, description="创建成功时返回地址ID")


class FbaShipmentGetfbaproductlistResponse(LingXingModel):
    """查询FBA商品信息列表."""
    total: Optional[int] = Field(None, description="总数")
    image: Optional[str] = Field(None, description="图片")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN对应亚马逊页面地址")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    title: Optional[str] = Field(None, description="标题")
    local_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="sku")
    product_id: Optional[int] = Field(None, description="产品id")
    sid: Optional[int] = Field(None, description="店铺id")


class FbaShipmentGetheadlogisticsfeetypesResponse(LingXingModel):
    """获取发货单头程物流信息-其他费类型."""
    fee_type_id: Optional[str] = Field(None, description="其他费ID")
    name: Optional[str] = Field(None, description="其他费名称")
    remark: Optional[str] = Field(None, description="其他费备注")
    created_at: Optional[str] = Field(None, description="其他费创建时间")


class FbaShipmentGetseatracksuppliercarriersResponse(LingXingModel):
    """获取发货单头程物流信息-承运商信息."""
    shippers: Optional[str] = Field(None, description="承运商code")
    name: Optional[str] = Field(None, description="承运商名称")
    home_page: Optional[str] = Field(None, description="承运商链接主页地址")


class FbaShipmentShipfromaddresslistResponse(LingXingModel):
    """地址簿-发货地址列表."""
    id: Optional[int] = Field(None, description="发货地址唯一id")
    sid: Optional[int] = Field(None, description="店铺id")
    alias_name: Optional[str] = Field(None, description="地址别名")
    country_code: Optional[str] = Field(None, description="国家code")
    country_name: Optional[str] = Field(None, description="发货国家/地区")
    sender_name: Optional[str] = Field(None, description="发货方名称")
    province: Optional[str] = Field(None, description="省/州/地区，美国发货地址限制长度为2位")
    city: Optional[str] = Field(None, description="城市")
    region: Optional[str] = Field(None, description="区")
    street_detail1: Optional[str] = Field(None, description="街道地址1")
    street_detail2: Optional[str] = Field(None, description="街道地址2")
    zip_code: Optional[str] = Field(None, description="邮编")
    phone: Optional[str] = Field(None, description="是")
    is_default: Optional[int] = Field(None, description="是否默认地址： 0 否 1 是")
    seller_name: Optional[str] = Field(None, description="店铺名")
    seller_country_name: Optional[int] = Field(None, description="是")


class FbaShipmentSyncshipmentError(LingXingModel):
    """error sub-structure."""
    shipment_id: Optional[str] = Field(None, description="失败货件编号")
    detail: Optional[str] = Field(None, description="原因")
    is_error_seller: Optional[int] = Field(None, description="是否是店铺不匹配：0 否，1 是")

class FbaShipmentSyncshipmentResponse(LingXingModel):
    """同步亚马逊货件到ERP."""
    succ_num: Optional[int] = Field(None, description="同步成功数量")
    fail_num: Optional[int] = Field(None, description="同步事变数量")
    error: Optional[List[FbaShipmentSyncshipmentError]] = Field(None, description="失败具体原因")
    total: Optional[int] = Field(None, description="总数")


class StorageShipmentCreatereadysendorderResponse(LingXingModel):
    """生成待发货的发货单."""
    order_sn: Optional[str] = Field(None, description="发货单号")


class StorageShipmentCreateshipmentplanResponse(LingXingModel):
    """创建FBA发货计划."""
    total: Optional[int] = Field(None, description="总数")
    seq: Optional[str] = Field(None, description="批次号")
    order_sn: Optional[list] = Field(None, description="计划编号")


class StorageShipmentGetinboundshipmentlistList(LingXingModel):
    """list sub-structure."""
    id: Optional[int] = Field(None, description="发货单id")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    status: Optional[int] = Field(None, description="发货单状态， -1 : 待配货 0：待发货， 1：已发货， 2：已完成， 3：已作废")
    shipment_time: Optional[str] = Field(None, description="发货时间")
    wname: Optional[str] = Field(None, description="仓库名称")
    create_user: Optional[str] = Field(None, description="创建用户")
    logistics_provider_id: Optional[str] = Field(None, description="物流商ID")
    logistics_provider_name: Optional[str] = Field(None, description="物流商名称")
    logistics_channel_name: Optional[str] = Field(None, description="物流渠道名称")
    expected_arrival_date: Optional[str] = Field(None, description="到货时间")
    actual_shipment_time: Optional[str] = Field(None, description="实际发货时间（已废弃）")
    etd_date: Optional[str] = Field(None, description="开船时间")
    eta_date: Optional[str] = Field(None, description="预计到港时间")
    delivery_date: Optional[str] = Field(None, description="实际妥投时间")
    create_time: Optional[str] = Field(None, description="创建时间")
    gmt_create: Optional[str] = Field(None, description="创建时间(精确到时分秒)")
    is_pick: Optional[int] = Field(None, description="拣货状态 0 未拣货 1已拣货")
    is_print: Optional[int] = Field(None, description="是否打印 0-否,1-是")
    pick_time: Optional[str] = Field(None, description="拣货时间")
    print_num: Optional[int] = Field(None, description="打印次数")
    head_fee_type: Optional[int] = Field(None, description="头程费分配方式， 0：按计费重； 1：按实重； 2：按体积重； 3：按SKU数量； 4：自定义； 5：按箱子体积")
    file_id: Optional[str] = Field(None, description="附件文件")
    update_time: Optional[str] = Field(None, description="更新时间")
    remark: Optional[str] = Field(None, description="备注")
    wid: Optional[int] = Field(None, description="仓库ID")
    is_return_stock: Optional[int] = Field(None, description="是否恢复库存:0-否，1-是")
    pay_status: Optional[int] = Field(None, description="付款状态： 0：未申请， 1：已申请， 2：部分付款， 3：已付清， 4：无")
    audit_status: Optional[int] = Field(None, description="审批状态： 121：待审核， 122：驳回， 123：通过， 124：作废")
    shipment_user: Optional[str] = Field(None, description="发货人")
    is_exist_declaration: Optional[int] = Field(None, description="是否关联报关单，0：否，1：是")
    is_exist_clearance: Optional[int] = Field(None, description="是否关联清关单，0：否，1：是")
    third_party_order_mode: Optional[int] = Field(None, description="下单模式，0：无，1：系统下单，2：手工下单")
    third_party_order_status: Optional[int] = Field(None, description="第三方仓下单状态，待发货下才有： 1：未下单， 2：已下单， 3：异常， 4：已发货")
    vat_code: Optional[str] = Field(None, description="店铺VAT税号")
    method_id: Optional[str] = Field(None, description="运输方式ID")
    method_name: Optional[str] = Field(None, description="运输方式名称")
    is_custom_shipment_time: Optional[int] = Field(None, description="是否自定义发货时间，1：是，0：否")
    logistics_tracking_number: Optional[str] = Field(None, description="物流商单号")
    logistics: Optional[list] = Field(None, description="物流轨迹列表")
    relate_list: Optional[list] = Field(None, description="关联货件列表")
    not_relate_list: Optional[list] = Field(None, description="未关联货件列表")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    status_name: Optional[str] = Field(None, description="状态名称")
    head_fee_type_name: Optional[str] = Field(None, description="头程分摊名称")
    head_fee_type_name_new: Optional[str] = Field(None, description="新头程费分配名称方式： 0 产品-计费重（默认） 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积")
    file_list: Optional[list] = Field(None, description="文件列表")
    shipment_time_second: Optional[str] = Field(None, description="发货时间(精确到时分秒)")
    is_delete: Optional[float] = Field(None, description="删除状态：0-未删除 1-已删除")

class StorageShipmentGetinboundshipmentlistResponse(LingXingModel):
    """查询发货单列表."""
    list: Optional[List[StorageShipmentGetinboundshipmentlistList]] = Field(None, description="发货单列表")
    total: Optional[int] = Field(None, description="是")


class StorageShipmentGetinboundshipmentlistmwsdetailItems(LingXingModel):
    """items sub-structure."""
    id: Optional[int] = Field(None, description="商品明细ID")
    zid: Optional[int] = Field(None, description="ZID")
    pid: Optional[int] = Field(None, description="货件明细ID")
    inbound_shipment_list_id: Optional[int] = Field(None, description="发货单ID")
    box_num: Optional[int] = Field(None, description="箱数")
    num: Optional[int] = Field(None, description="发货数量")
    wid: Optional[int] = Field(None, description="仓库ID")
    ware_house_storage_id: Optional[int] = Field(None, description="已作废字段")
    product_id: Optional[int] = Field(None, description="本地商品ID")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="仓库FNSKU")
    status: Optional[int] = Field(None, description="状态")
    shipment_time: Optional[int] = Field(None, description="发货时间")
    aux_cost: Optional[str] = Field(None, description="辅料费用")
    fba_stock_cost: Optional[str] = Field(None, description="采购单价")
    fee_cost: Optional[str] = Field(None, description="仓库费用(已废弃)")
    stock_cost: Optional[str] = Field(None, description="单位FBA仓入库成本")
    tax_amount: Optional[str] = Field(None, description="税费值")
    tax_currency: Optional[str] = Field(None, description="税费币种")
    create_time: Optional[str] = Field(None, description="是")
    update_time: Optional[str] = Field(None, description="是")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    cost_weight: Optional[str] = Field(None, description="每个商品对应的计费重(体积重)")
    total_transport_cost: Optional[str] = Field(None, description="总头程费用")
    cg_package_length: Optional[str] = Field(None, description="包装规格（CM）长")
    cg_package_width: Optional[str] = Field(None, description="包装规格（CM）宽")
    cg_package_height: Optional[str] = Field(None, description="包装规格（CM）高")
    cg_product_gross_weight: Optional[str] = Field(None, description="商品毛重（G）")
    calculate_tax_amount: Optional[str] = Field(None, description="税费值(人民币)")
    product_name: Optional[str] = Field(None, description="商品名称")
    whb_code: Optional[list] = Field(None, description="仓位编码列表")
    sname: Optional[str] = Field(None, description="店铺名称")
    nation: Optional[str] = Field(None, description="店铺所在国家")
    cg_product_net_weight: Optional[str] = Field(None, description="商品净重（G）")
    total_nw: Optional[str] = Field(None, description="总净重（G）")
    total_gw: Optional[str] = Field(None, description="总毛重（G）")
    shipment_plan_quantity: Optional[int] = Field(None, description="计划发货量")
    apply_num: Optional[int] = Field(None, description="申报量")
    remark: Optional[str] = Field(None, description="备注")
    isp_id: Optional[int] = Field(None, description="发货计划id")
    is_combo: Optional[int] = Field(None, description="组合商品：0-否，1-是")
    create_by_mws: Optional[int] = Field(None, description="货件生成发货单: 0-否，1-是")
    cg_box_width: Optional[str] = Field(None, description="箱子宽度(CM)宽")
    cg_box_height: Optional[str] = Field(None, description="箱子宽度(CM)高")
    cg_box_weight: Optional[str] = Field(None, description="单箱重量（KG）")
    cg_box_net_weight: Optional[str] = Field(None, description="单箱净重（KG）")
    cg_box_gross_weight: Optional[str] = Field(None, description="单箱毛重（KG）")
    cg_box_length: Optional[str] = Field(None, description="箱子宽度(CM)长")
    cbm: Optional[str] = Field(None, description="CBM，商品体积，非装箱信息体积")
    product_mws_id: Optional[int] = Field(None, description="在线商品ID")
    volume_weight: Optional[str] = Field(None, description="体积重")
    quantity_in_case: Optional[int] = Field(None, description="单箱数量")
    pic_url: Optional[str] = Field(None, description="图片URL")
    packing_type: Optional[int] = Field(None, description="混装类型： 1：原装， 2：原装")
    shipment_id: Optional[str] = Field(None, description="货件编号")
    sid: Optional[int] = Field(None, description="店铺ID")
    wname: Optional[str] = Field(None, description="仓库名")
    fulfillment_network_sku: Optional[str] = Field(None, description="listing的fnsku")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    msku: Optional[str] = Field(None, description="seller_sku")
    transport_cost: Optional[str] = Field(None, description="单位头程费用")
    diff_num: Optional[int] = Field(None, description="差额")
    mid: Optional[str] = Field(None, description="店铺所在国家ID")
    shipment_order_sn: Optional[str] = Field(None, description="发货计划单号")
    calculate_transportation_cost: Optional[str] = Field(None, description="运费（人民币）")
    calculate_other_cost: Optional[str] = Field(None, description="其他费用(人民币)")
    calculate_predicted_transportation_cost: Optional[str] = Field(None, description="预估运费（人民币）")
    calculate_predicted_other_cost: Optional[str] = Field(None, description="预估其他费用(人民币)")
    predicted_transport_cost: Optional[str] = Field(None, description="预估单位头程费用")
    predicted_total_transport_cost: Optional[str] = Field(None, description="预估总头程费用")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    quantity_shipped: Optional[int] = Field(None, description="货件申报量")
    is_delete: Optional[int] = Field(None, description="是")
    shipment_status: Optional[str] = Field(None, description="货件状态")
    quantity_receive: Optional[str] = Field(None, description="待到货量")
    is_relate_mws: Optional[int] = Field(None, description="关联货件：0-否，1-是")
    product_qc_num: Optional[int] = Field(None, description="待检量")
    product_valid_num: Optional[int] = Field(None, description="可用量")
    sku_box_key: Optional[str] = Field(None, description="产品装箱唯一键，发货单内唯一，可用于关联箱子信息")
    asin: Optional[str] = Field(None, description="ASIN")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    seller_id: Optional[int] = Field(None, description="发货仓库店铺ID")
    seller_name: Optional[str] = Field(None, description="发货仓库店铺名称")
    custom_stock_cost: Optional[float] = Field(None, description="单位库存成本(自定义)")
    custom_aux_cost: Optional[float] = Field(None, description="单位辅料费用(自定义)")
    tax_unit: Optional[float] = Field(None, description="单位税费")
    outbound_head_cost_unit: Optional[float] = Field(None, description="单位出库头程")
    purchase_price_unit: Optional[float] = Field(None, description="采购单价")
    outbound_cost_unit: Optional[float] = Field(None, description="单位出库费用")
    third_party_product_name: Optional[str] = Field(None, description="第三方仓产品名")
    third_party_product_code: Optional[str] = Field(None, description="第三方仓SKU")
    match_num: Optional[int] = Field(None, description="配对数量")
    third_party_order_quantity: Optional[int] = Field(None, description="下单数量")
    product_declared_value: Optional[float] = Field(None, description="申报价值")
    label_replacement_qty: Optional[int] = Field(None, description="换标总数量")
    hs_code: Optional[str] = Field(None, description="海关编码(6~10位数字)")
    box_no: Optional[str] = Field(None, description="箱号")
    box_pu_number: Optional[str] = Field(None, description="贴标数量")
    for_finance_cost: Optional[float] = Field(None, description="采购单价+单位出库费用")
    custom_purchase_price_unit: Optional[float] = Field(None, description="采购单价(自定义)")
    custom_outbound_cost_unit: Optional[str] = Field(None, description="单位出库费用(自定义)")
    custom_fba_inbound_cost_unit: Optional[str] = Field(None, description="单位FBA仓入库成本(自定义)")
    list_item_volume_proportion: Optional[float] = Field(None, description="体积比例")
    list_item_chargeable_weight_proportion: Optional[float] = Field(None, description="重量比例")
    process_fee_unit: Optional[float] = Field(None, description="单位加工费")
    purchase_items: Optional[list] = Field(None, description="工厂直发关联采购单信息")
    storage_list: Optional[list] = Field(None, description="是")
    shipment_order_list: Optional[str] = Field(None, description="是")
    shipment_ids: Optional[str] = Field(None, description="是")
    cost_source: Optional[str] = Field(None, description="实际费用")
    whb_code_list: Optional[list] = Field(None, description="仓位编码列表")
    son_storage_arr: Optional[list] = Field(None, description="组合商品列表")
    max_product_valid_num: Optional[int] = Field(None, description="组合商品最大可用量")
    sta_shipment_id: Optional[str] = Field(None, description="sta的shipmentId")
    is_sta: Optional[str] = Field(None, description="是否sta货件， 1：是， 0：否")
    sta_inbound_plan_id: Optional[str] = Field(None, description="sta货件关联的发货编号")

class StorageShipmentGetinboundshipmentlistmwsdetailLogistics(LingXingModel):
    """logistics sub-structure."""
    id: Optional[int] = Field(None, description="物流信息ID")
    zid: Optional[int] = Field(None, description="是")
    inbound_shipment_list_mws_id: Optional[int] = Field(None, description="发货单ID")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    tracking_number: Optional[str] = Field(None, description="物流商号")
    replace_tracking_number: Optional[str] = Field(None, description="跟踪单号")
    transportation_cost: Optional[str] = Field(None, description="实际物流费用")
    other_cost: Optional[str] = Field(None, description="实际其他费用")
    transportation_currency: Optional[str] = Field(None, description="实际物流费用币种")
    other_currency: Optional[str] = Field(None, description="实际其他费用币种")
    other_cost_remark: Optional[str] = Field(None, description="实际其他费用备注")
    predicted_transportation_cost: Optional[str] = Field(None, description="预估物流费用")
    predicted_transportation_currency: Optional[str] = Field(None, description="预估物流费用币种")
    predicted_other_cost: Optional[str] = Field(None, description="预估其他费用")
    predicted_other_currency: Optional[str] = Field(None, description="预估其他费用币种")
    predicted_other_cost_remark: Optional[str] = Field(None, description="预估其他费用备注")

class StorageShipmentGetinboundshipmentlistmwsdetailAuxs(LingXingModel):
    """auxs sub-structure."""
    isialm_id: Optional[int] = Field(None, description="辅料自增ID")
    zid: Optional[int] = Field(None, description="是")
    company_id: Optional[str] = Field(None, description="是")
    aux_id: Optional[int] = Field(None, description="辅料产品ID")
    pid: Optional[int] = Field(None, description="货件明细ID")
    num: Optional[int] = Field(None, description="商品发货数量")
    aux_sku: Optional[str] = Field(None, description="辅料SKU")
    aux_name: Optional[str] = Field(None, description="辅料名称")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    shipment_plan_sn: Optional[str] = Field(None, description="发货计划单号")
    shipment_id: Optional[str] = Field(None, description="货件编号")
    inbound_shipment_list_id: Optional[int] = Field(None, description="发货计划ID")
    cg_price: Optional[str] = Field(None, description="辅料单位成本")
    cg_total_price: Optional[str] = Field(None, description="辅料总成本")
    cg_product_net_weight: Optional[str] = Field(None, description="辅料净重")
    cg_product_length: Optional[str] = Field(None, description="箱子规格(CM)长")
    remark: Optional[str] = Field(None, description="备注")
    cg_product_width: Optional[str] = Field(None, description="箱子规格(CM)宽")
    cg_product_height: Optional[str] = Field(None, description="箱子规格(CM)高")
    relation_product_msku: Optional[str] = Field(None, description="关联MSKU")
    relation_type: Optional[int] = Field(None, description="1关联商品,2关联整单")
    relation_product_sku: Optional[str] = Field(None, description="关联SKU")
    relation_product_fnsku: Optional[str] = Field(None, description="关联FNSKU")
    aux_num: Optional[int] = Field(None, description="关联数量")
    relation_product_id: Optional[int] = Field(None, description="关联产品ID")
    relation_isilm_id: Optional[int] = Field(None, description="关联发货单ID")
    update_uid: Optional[int] = Field(None, description="修改人UID")
    update_user: Optional[str] = Field(None, description="修改人")
    create_user: Optional[str] = Field(None, description="创建人")
    create_uid: Optional[int] = Field(None, description="创建人UID")
    aux_head_fee_type: Optional[int] = Field(None, description="辅料分摊类型 1:按sku分摊, 2:实重分摊, 3:按体积重分摊, 4:按计费重分摊")
    is_points_behind: Optional[int] = Field(None, description="是否分抛计算(0:否,1:是)")
    points_behind_coeffient: Optional[int] = Field(None, description="分抛系数(0-100)")
    create_time: Optional[str] = Field(None, description="是")
    update_time: Optional[str] = Field(None, description="是")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="修改时间")

class StorageShipmentGetinboundshipmentlistmwsdetailPrincipals(LingXingModel):
    """principals sub-structure."""
    isp_id: Optional[str] = Field(None, description="主键ID")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    company_id: Optional[str] = Field(None, description="是")
    zid: Optional[int] = Field(None, description="是")
    isil_id: Optional[int] = Field(None, description="发货单ID")
    principal_uid: Optional[int] = Field(None, description="权限人UID")
    operate_user: Optional[str] = Field(None, description="操作人")
    operate_uid: Optional[int] = Field(None, description="操作人UID")
    principal_user: Optional[str] = Field(None, description="权限人")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")

class StorageShipmentGetinboundshipmentlistmwsdetailHeadLogisticsList(LingXingModel):
    """head_logistics_list sub-structure."""
    track_list: Optional[list] = Field(None, description="轨迹信息")
    logistics_tracking_number: Optional[str] = Field(None, description="物流商单号")
    estimate_expenses_list: Optional[dict] = Field(None, description="费用数组-预估费用数组")
    actual_expenses_list: Optional[dict] = Field(None, description="费用明细-实际费用数组 (参考estimate_expenses_list)")

class StorageShipmentGetinboundshipmentlistmwsdetailBoxList(LingXingModel):
    """box_list sub-structure."""
    box_num: Optional[str] = Field(None, description="箱子数")
    cg_box_length: Optional[str] = Field(None, description="箱子长")
    cg_box_width: Optional[str] = Field(None, description="箱子宽")
    cg_box_height: Optional[str] = Field(None, description="箱子高")
    cg_box_weight: Optional[str] = Field(None, description="箱子重")
    box_range: Optional[str] = Field(None, description="箱子范围")
    box_codes: Optional[str] = Field(None, description="自定义箱号,通过 n分隔")
    box_skus: Optional[list] = Field(None, description="箱子内包含的SKU信息， SINGLE类型装箱，只会有一个子项， MULTIPLE类型装箱，可能会有多个子项")

class StorageShipmentGetinboundshipmentlistmwsdetailOutboundBatch(LingXingModel):
    """outbound_batch sub-structure."""
    sku: Optional[str] = Field(None, description="sku")
    product_id: Optional[str] = Field(None, description="产品id")
    product_name: Optional[str] = Field(None, description="产品名称")
    pic_url: Optional[str] = Field(None, description="图片链接")
    wid: Optional[str] = Field(None, description="仓库id")
    wname: Optional[str] = Field(None, description="仓库名称")
    seller_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    fnsku: Optional[str] = Field(None, description="fnsku")
    total_outbound_num: Optional[str] = Field(None, description="可用总出库量")
    batch_record_list: Optional[list] = Field(None, description="批次记录列表")

class StorageShipmentGetinboundshipmentlistmwsdetailResponse(LingXingModel):
    """查询发货单详情."""
    id: Optional[int] = Field(None, description="发货单ID")
    zid: Optional[int] = Field(None, description="ZID")
    tracking_id: Optional[int] = Field(None, description="物流追踪(运单)ID")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    status: Optional[int] = Field(None, description="发货单状态， -1 : 待配货 0：待发货， 1：已发货， 3：已作废， 4：已删除")
    shipment_time: Optional[str] = Field(None, description="发货时间")
    wid: Optional[int] = Field(None, description="仓库ID")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    remark: Optional[str] = Field(None, description="备注")
    creator_uid: Optional[int] = Field(None, description="创建人UID")
    opt_uid: Optional[int] = Field(None, description="最后操作人UID")
    msku_count: Optional[int] = Field(None, description="种类数")
    quantity_total: Optional[int] = Field(None, description="发货总量")
    logistics_channel_id: Optional[int] = Field(None, description="渠道商ID")
    confirm_uid: Optional[int] = Field(None, description="确认人UID")
    shipment_uid: Optional[int] = Field(None, description="发货人UID")
    confirm_time: Optional[int] = Field(None, description="确认时间(时间戳格式)")
    expected_arrival_date: Optional[str] = Field(None, description="预计到货日期")
    is_related: Optional[int] = Field(None, description="1=关联；0=不关联")
    is_whb_checked: Optional[int] = Field(None, description="1=自动选择仓位扣减； 0=不选择仓位扣减")
    head_fee_type: Optional[int] = Field(None, description="头程费分配方式： 0 产品-计费重（默认） 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积")
    is_points_behind: Optional[int] = Field(None, description="是否分抛计算： 0:否, 1:是")
    points_behind_coeffient: Optional[int] = Field(None, description="分抛系数(0-100)")
    is_return_stock: Optional[int] = Field(None, description="是否恢复库存， 0=否， 1=是")
    ware_house_bak_name: Optional[str] = Field(None, description="仓库名称(作为被删仓库的备用值)")
    is_print: Optional[int] = Field(None, description="是否打印拣货单： 0：未打印， 1：已打印")
    print_num: Optional[int] = Field(None, description="打印次数")
    is_pick: Optional[int] = Field(None, description="是否拣货： 0：未拣货， 1:已拣货")
    pick_time: Optional[str] = Field(None, description="完成拣货时间")
    print_time: Optional[int] = Field(None, description="最后一次打印时间")
    etd_date: Optional[str] = Field(None, description="开船时间")
    eta_date: Optional[str] = Field(None, description="预计到港时间")
    delivery_date: Optional[str] = Field(None, description="实际妥投时间")
    order_logistics_status: Optional[str] = Field(None, description="订单物流状态")
    shipment_user: Optional[str] = Field(None, description="发货人")
    wname: Optional[str] = Field(None, description="仓库名称")
    create_user: Optional[str] = Field(None, description="创建人")
    file_id: Optional[str] = Field(None, description="附件文件")
    actual_shipment_time: Optional[str] = Field(None, description="实际发货时间")
    logistics_channel_name: Optional[str] = Field(None, description="物流渠道名称")
    is_delete: Optional[int] = Field(None, description="0-未删除")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    cancel_time: Optional[int] = Field(None, description="作废时间(时间戳格式)")
    logistics_provider_id: Optional[int] = Field(None, description="物流商ID")
    logistics_provider_name: Optional[str] = Field(None, description="物流商名称")
    transportation_cost_status: Optional[int] = Field(None, description="物流费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    other_cost_status: Optional[int] = Field(None, description="其他费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    pay_status: Optional[int] = Field(None, description="付款状态： 0：未申请， 1：已申请， 2：部分付款， 3：已付清， 4：无")
    predicted_transportation_cost_status: Optional[int] = Field(None, description="预估物流费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    predicted_other_cost_status: Optional[int] = Field(None, description="预估其他费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    audit_status: Optional[int] = Field(None, description="审批状态， 121：待审核， 122：驳回， 123：通过， 124：作废")
    stash_shipment_uid: Optional[int] = Field(None, description="暂存发货人UID（审批流专用）")
    stash_shipment_time: Optional[int] = Field(None, description="暂存发货时间（审批流专用）")
    is_exist_declaration: Optional[int] = Field(None, description="是否关联报关单， 0：否， 1：是")
    is_exist_clearance: Optional[int] = Field(None, description="是否关联清关单， 0：否， 1：是")
    is_relate_aux: Optional[int] = Field(None, description="是否关联辅料， 0：否， 1：是")
    third_party_order_mode: Optional[int] = Field(None, description="下单模式， 0：无， 1：系统下单， 2：手工下单")
    third_party_logistics_wp_code: Optional[str] = Field(None, description="第三方仓服务商代码，如Gucang、Xyzc")
    third_party_order_status: Optional[int] = Field(None, description="第三方仓下单状态，待发货下才有， 1：未下单， 2：已下单， 3：异常， 4：已发货")
    third_party_order_status_code: Optional[str] = Field(None, description="第三方海外仓API返回的订单状态代码")
    third_party_order_sn: Optional[str] = Field(None, description="第三方海外仓API订单号")
    third_party_order_exception_reason: Optional[str] = Field(None, description="第三方仓订单异常原因")
    is_change_label: Optional[int] = Field(None, description="（谷仓）换标服务， 0：不换标， 1：换标")
    label_replacement_option: Optional[int] = Field(None, description="（谷仓）换标要求， 1：外箱， 2：内箱")
    is_signature: Optional[int] = Field(None, description="（谷仓/西邮智仓）签名服务， 0：不选择签名服务， 1：签名服务")
    age_detection: Optional[int] = Field(None, description="（谷仓）年龄检测服务，可选值16 18")
    is_insurance: Optional[int] = Field(None, description="（谷仓/西邮智仓）保险服务，0：不需要，1：需要")
    insurance_value: Optional[float] = Field(None, description="（谷仓/西邮智仓）保险费/投保金额")
    lift_gate: Optional[int] = Field(None, description="（谷仓）LiftGate服务，0：否，1：是")
    ware_operation_type: Optional[int] = Field(None, description="（西邮智仓）库内操作， 0：无， 1换条码， 2:换箱唛， 3换条码换箱唛")
    other_ware_operation: Optional[int] = Field(None, description="（西邮智仓）其他库内操作， 0：无， 1换托唛")
    inventory_type: Optional[int] = Field(None, description="（西邮智仓）库存类型， 0：标准， 1：不良品， 4：退货")
    order_cod_currency: Optional[str] = Field(None, description="（西邮智仓）下单币种")
    is_split_prediction: Optional[int] = Field(None, description="（西邮智仓）是否拆单预报， 0：否， 1：是")
    is_custom_cost: Optional[int] = Field(None, description="是否自定义成本， 1：是， 0：否")
    pick_num: Optional[int] = Field(None, description="已拣货数量")
    vat_code: Optional[str] = Field(None, description="店铺VAT税号")
    head_fee_status: Optional[int] = Field(None, description="头程分摊相关规格填写状态， 0：未完整填写， 1：已完整填写")
    is_custom_shipment_time: Optional[int] = Field(None, description="是否自定义发货时间，1：是，0：否")
    return_stock_type: Optional[int] = Field(None, description="恢复库存类型： 0未恢复； 1全部恢复； 2产品库存； 3辅料库存")
    cancel_reason: Optional[str] = Field(None, description="作废理由")
    packing_task_sn: Optional[str] = Field(None, description="装箱任务编号")
    is_auto_adjust: Optional[int] = Field(None, description="是否自动换标调整， 1：是，0：否")
    volume_parameter: Optional[float] = Field(None, description="材积参数")
    logistics_estimated_day: Optional[int] = Field(None, description="物流时效")
    estimated_shipment_date: Optional[str] = Field(None, description="预计发货时间")
    cost_source: Optional[int] = Field(None, description="取值来源 1预估 2 实际")
    is_relate_head_logistics: Optional[int] = Field(None, description="是否关联头程物流, 0:否, 1:是")
    method_name: Optional[str] = Field(None, description="运输方式名称")
    method_id: Optional[str] = Field(None, description="运输方式ID")
    items: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailItems]] = Field(None, description="商品列表")
    logistics: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailLogistics]] = Field(None, description="物流信息列表")
    auxs: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailAuxs]] = Field(None, description="辅料列表")
    principals: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailPrincipals]] = Field(None, description="权限人列表")
    msg: Optional[str] = Field(None, description="是")
    status_name: Optional[str] = Field(None, description="状态名称")
    last_update_time: Optional[str] = Field(None, description="最后修改日期")
    head_fee_type_name: Optional[str] = Field(None, description="头程费用名称")
    file_list: Optional[list] = Field(None, description="附件列表")
    box_type: Optional[str] = Field(None, description="装箱类型： SINGLE-每箱只允许一款SKU， MULTIPLE-每箱允许多款SKU")
    box_remark: Optional[str] = Field(None, description="装箱备注")
    logistics_list_type: Optional[dict] = Field(None, description="物流信息版本 0旧版 1新版")
    head_logistics_list: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailHeadLogisticsList]] = Field(None, description="新版物流信息列表(logistics_list_type = 1时才有意义)")
    box_list: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailBoxList]] = Field(None, description="箱规列表，每个子项代表一个箱规")
    outbound_batch: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetailOutboundBatch]] = Field(None, description="采购信息")
    total: Optional[int] = Field(None, description="是")


class StorageShipmentGetinboundshipmentlistmwsdetaillistItems(LingXingModel):
    """items sub-structure."""
    id: Optional[int] = Field(None, description="商品明细ID")
    pid: Optional[int] = Field(None, description="货件明细ID")
    inbound_shipment_list_id: Optional[int] = Field(None, description="发货单ID")
    box_num: Optional[int] = Field(None, description="箱数")
    num: Optional[int] = Field(None, description="发货数量")
    wid: Optional[int] = Field(None, description="仓库ID")
    ware_house_storage_id: Optional[int] = Field(None, description="已作废字段")
    product_id: Optional[int] = Field(None, description="本地商品ID")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="仓库FNSKU")
    status: Optional[int] = Field(None, description="状态")
    shipment_time: Optional[int] = Field(None, description="发货时间")
    aux_cost: Optional[str] = Field(None, description="辅料费用")
    fba_stock_cost: Optional[str] = Field(None, description="fba库存费用")
    fee_cost: Optional[str] = Field(None, description="仓库费用")
    stock_cost: Optional[str] = Field(None, description="仓库发货成本价")
    tax_amount: Optional[str] = Field(None, description="税费值")
    tax_currency: Optional[str] = Field(None, description="税费币种")
    create_time: Optional[str] = Field(None, description="是")
    update_time: Optional[str] = Field(None, description="是")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    cost_weight: Optional[str] = Field(None, description="每个商品对应的计费重(体积重)")
    total_transport_cost: Optional[str] = Field(None, description="总费用(商品的运费和税费之和)")
    cg_package_length: Optional[str] = Field(None, description="包装规格（CM）长")
    cg_package_width: Optional[str] = Field(None, description="包装规格（CM）宽")
    cg_package_height: Optional[str] = Field(None, description="包装规格（CM）高")
    cg_product_gross_weight: Optional[str] = Field(None, description="商品毛重（G）")
    calculate_tax_amount: Optional[str] = Field(None, description="税费值(人民币)")
    product_name: Optional[str] = Field(None, description="商品名称")
    whb_code: Optional[list] = Field(None, description="仓位编码列表")
    sname: Optional[str] = Field(None, description="店铺名称")
    nation: Optional[str] = Field(None, description="店铺所在国家")
    cg_product_net_weight: Optional[str] = Field(None, description="商品净重（G）")
    total_nw: Optional[str] = Field(None, description="总净重（G）")
    total_gw: Optional[str] = Field(None, description="总毛重（G）")
    shipment_plan_quantity: Optional[int] = Field(None, description="计划发货量")
    apply_num: Optional[int] = Field(None, description="申报量")
    remark: Optional[str] = Field(None, description="备注")
    isp_id: Optional[int] = Field(None, description="发货计划id")
    is_combo: Optional[int] = Field(None, description="组合商品：0-否，1-是")
    create_by_mws: Optional[int] = Field(None, description="货件生成发货单: 0-否，1-是")
    cg_box_width: Optional[str] = Field(None, description="箱子宽度(CM)宽")
    cg_box_height: Optional[str] = Field(None, description="箱子宽度(CM)高")
    cg_box_weight: Optional[str] = Field(None, description="单箱重量（KG）")
    cg_box_net_weight: Optional[str] = Field(None, description="单箱净重（KG）")
    cg_box_gross_weight: Optional[str] = Field(None, description="单箱毛重（KG）")
    cg_box_length: Optional[str] = Field(None, description="箱子宽度(CM)长")
    cbm: Optional[str] = Field(None, description="CBM")
    product_mws_id: Optional[int] = Field(None, description="在线商品ID")
    volume_weight: Optional[str] = Field(None, description="体积重")
    quantity_in_case: Optional[int] = Field(None, description="单箱数量")
    pic_url: Optional[str] = Field(None, description="图片URL")
    packing_type: Optional[int] = Field(None, description="混装类型：1：原装，2：原装")
    shipment_id: Optional[str] = Field(None, description="货件编号")
    sid: Optional[int] = Field(None, description="店铺ID")
    wname: Optional[str] = Field(None, description="仓库名")
    fulfillment_network_sku: Optional[str] = Field(None, description="listing的fnsku")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    msku: Optional[str] = Field(None, description="seller_sku")
    transport_cost: Optional[str] = Field(None, description="每个商品对应的头程价格")
    diff_num: Optional[int] = Field(None, description="差额")
    mid: Optional[str] = Field(None, description="店铺所在国家ID")
    shipment_order_sn: Optional[str] = Field(None, description="发货计划单号")
    calculate_transportation_cost: Optional[str] = Field(None, description="运费（人民币）")
    calculate_other_cost: Optional[str] = Field(None, description="其他费用(人民币)")
    calculate_predicted_transportation_cost: Optional[str] = Field(None, description="预估运费（人民币）")
    calculate_predicted_other_cost: Optional[str] = Field(None, description="预估其他费用(人民币)")
    predicted_transport_cost: Optional[str] = Field(None, description="预估每个商品对应的头程价格")
    predicted_total_transport_cost: Optional[str] = Field(None, description="预估总费用(预估物流费用和税费之和)")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    quantity_shipped: Optional[int] = Field(None, description="货件申报量")
    is_delete: Optional[int] = Field(None, description="是")
    shipment_status: Optional[str] = Field(None, description="货件状态")
    quantity_receive: Optional[str] = Field(None, description="待到货量")
    is_relate_mws: Optional[int] = Field(None, description="关联货件：0-否，1-是")
    product_qc_num: Optional[int] = Field(None, description="待检量")
    product_valid_num: Optional[int] = Field(None, description="可用量")
    sku_box_key: Optional[str] = Field(None, description="产品装箱唯一键，发货单内唯一，可用于关联箱子信息")
    storage_list: Optional[list] = Field(None, description="是")
    shipment_order_list: Optional[str] = Field(None, description="是")
    shipment_ids: Optional[str] = Field(None, description="是")
    cost_source: Optional[str] = Field(None, description="实际费用")
    whb_code_list: Optional[list] = Field(None, description="仓位编码列表")
    son_storage_arr: Optional[list] = Field(None, description="组合商品列表")
    max_product_valid_num: Optional[int] = Field(None, description="组合商品最大可用量")
    sta_shipment_id: Optional[str] = Field(None, description="sta的shipmentId")
    is_sta: Optional[str] = Field(None, description="是否sta货件，1：是，0：否")
    sta_inbound_plan_id: Optional[str] = Field(None, description="sta任务编号")

class StorageShipmentGetinboundshipmentlistmwsdetaillistLogistics(LingXingModel):
    """logistics sub-structure."""
    id: Optional[int] = Field(None, description="物流信息ID（旧版物流信息）")
    inbound_shipment_list_mws_id: Optional[int] = Field(None, description="发货单ID（旧版物流信息）")
    gmt_modified: Optional[str] = Field(None, description="修改时间（旧版物流信息）")
    gmt_create: Optional[str] = Field(None, description="创建时间（旧版物流信息）")
    tracking_number: Optional[str] = Field(None, description="物流商号（旧版物流信息）")
    replace_tracking_number: Optional[str] = Field(None, description="跟踪单号（旧版物流信息）")
    transportation_cost: Optional[str] = Field(None, description="实际物流费用（旧版物流信息）")
    other_cost: Optional[str] = Field(None, description="实际其他费用（旧版物流信息）")
    transportation_currency: Optional[str] = Field(None, description="实际物流费用币种（旧版物流信息）")
    other_currency: Optional[str] = Field(None, description="实际其他费用币种（旧版物流信息）")
    other_cost_remark: Optional[str] = Field(None, description="实际其他费用备注（旧版物流信息）")
    predicted_transportation_cost: Optional[str] = Field(None, description="预估物流费用（旧版物流信息）")
    predicted_transportation_currency: Optional[str] = Field(None, description="预估物流费用币种（旧版物流信息）")
    predicted_other_cost: Optional[str] = Field(None, description="预估其他费用（旧版物流信息）")
    predicted_other_currency: Optional[str] = Field(None, description="预估其他费用币种（旧版物流信息）")
    predicted_other_cost_remark: Optional[str] = Field(None, description="预估其他费用备注（旧版物流信息）")

class StorageShipmentGetinboundshipmentlistmwsdetaillistAuxs(LingXingModel):
    """auxs sub-structure."""
    isialm_id: Optional[int] = Field(None, description="辅料自增ID")
    aux_id: Optional[int] = Field(None, description="辅料产品ID")
    pid: Optional[int] = Field(None, description="货件明细ID")
    num: Optional[int] = Field(None, description="商品发货数量")
    aux_sku: Optional[str] = Field(None, description="辅料SKU")
    aux_name: Optional[str] = Field(None, description="辅料名称")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    shipment_plan_sn: Optional[str] = Field(None, description="发货计划单号")
    shipment_id: Optional[str] = Field(None, description="货件编号")
    inbound_shipment_list_id: Optional[int] = Field(None, description="发货计划ID")
    cg_price: Optional[str] = Field(None, description="辅料单位成本")
    cg_total_price: Optional[str] = Field(None, description="辅料总成本")
    cg_product_net_weight: Optional[str] = Field(None, description="辅料净重")
    cg_product_length: Optional[str] = Field(None, description="箱子规格(CM)长")
    remark: Optional[str] = Field(None, description="备注")
    cg_product_width: Optional[str] = Field(None, description="箱子规格(CM)宽")
    cg_product_height: Optional[str] = Field(None, description="箱子规格(CM)高")
    relation_product_msku: Optional[str] = Field(None, description="关联MSKU")
    relation_type: Optional[int] = Field(None, description="1关联商品,2关联整单")
    relation_product_sku: Optional[str] = Field(None, description="关联SKU")
    relation_product_fnsku: Optional[str] = Field(None, description="关联FNSKU")
    aux_num: Optional[int] = Field(None, description="关联数量")
    relation_product_id: Optional[int] = Field(None, description="关联产品ID")
    relation_isilm_id: Optional[int] = Field(None, description="关联发货单ID")
    update_uid: Optional[int] = Field(None, description="修改人UID")
    update_user: Optional[str] = Field(None, description="修改人")
    create_user: Optional[str] = Field(None, description="创建人")
    create_uid: Optional[int] = Field(None, description="创建人UID")
    aux_head_fee_type: Optional[int] = Field(None, description="辅料分摊类型 1:按sku分摊, 2:实重分摊, 3:按体积重分摊, :按计费重分摊")
    is_points_behind: Optional[int] = Field(None, description="是否分抛计算(0:否,1:是)")
    points_behind_coeffient: Optional[int] = Field(None, description="分抛系数(0-100)")
    create_time: Optional[str] = Field(None, description="是")
    update_time: Optional[str] = Field(None, description="是")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="修改时间")

class StorageShipmentGetinboundshipmentlistmwsdetaillistPrincipals(LingXingModel):
    """principals sub-structure."""
    isp_id: Optional[str] = Field(None, description="主键ID")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    isil_id: Optional[int] = Field(None, description="发货单ID")
    principal_uid: Optional[int] = Field(None, description="权限人UID")
    operate_user: Optional[str] = Field(None, description="操作人")
    operate_uid: Optional[int] = Field(None, description="操作人UID")
    principal_user: Optional[str] = Field(None, description="权限人")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")

class StorageShipmentGetinboundshipmentlistmwsdetaillistHeadLogisticsList(LingXingModel):
    """head_logistics_list sub-structure."""
    track_list: Optional[list] = Field(None, description="轨迹信息")
    logistics_tracking_number: Optional[str] = Field(None, description="物流商单号")
    estimate_expenses_list: Optional[dict] = Field(None, description="费用数组-预估费用数组")
    actual_expenses_list: Optional[dict] = Field(None, description="费用明细-实际费用数组 (参考estimate_expenses_list)")

class StorageShipmentGetinboundshipmentlistmwsdetaillistBoxList(LingXingModel):
    """box_list sub-structure."""
    box_num: Optional[str] = Field(None, description="箱子数")
    cg_box_length: Optional[str] = Field(None, description="箱子长")
    cg_box_width: Optional[str] = Field(None, description="箱子宽")
    cg_box_height: Optional[str] = Field(None, description="箱子高")
    cg_box_weight: Optional[str] = Field(None, description="箱子重")
    box_range: Optional[str] = Field(None, description="箱子范围")
    box_codes: Optional[str] = Field(None, description="自定义箱号,通过 n分隔")
    box_skus: Optional[list] = Field(None, description="箱子内包含的SKU信息，SINGLE类型装箱，只会有一个子项，MULTIPLE类型装箱，可能会有多个子项")

class StorageShipmentGetinboundshipmentlistmwsdetaillistResponse(LingXingModel):
    """批量查询发货单详情."""
    id: Optional[int] = Field(None, description="发货单ID")
    tracking_id: Optional[int] = Field(None, description="物流追踪(运单)ID")
    shipment_sn: Optional[str] = Field(None, description="发货单号")
    status: Optional[int] = Field(None, description="发货单状态， -1 : 待配货 0：待发货， 1：已发货， 3：已作废， 4：已删除")
    shipment_time: Optional[str] = Field(None, description="发货时间")
    wid: Optional[int] = Field(None, description="仓库ID")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    remark: Optional[str] = Field(None, description="备注")
    creator_uid: Optional[int] = Field(None, description="创建人UID")
    opt_uid: Optional[int] = Field(None, description="最后操作人UID")
    msku_count: Optional[int] = Field(None, description="种类数")
    quantity_total: Optional[int] = Field(None, description="发货总量")
    logistics_channel_id: Optional[int] = Field(None, description="渠道商ID")
    confirm_uid: Optional[int] = Field(None, description="确认人UID")
    shipment_uid: Optional[int] = Field(None, description="发货人UID")
    confirm_time: Optional[int] = Field(None, description="确认时间(时间戳格式)")
    expected_arrival_date: Optional[str] = Field(None, description="预计到货日期")
    is_related: Optional[int] = Field(None, description="1=关联；0=不关联")
    is_whb_checked: Optional[int] = Field(None, description="1=自动选择仓位扣减； 0=不选择仓位扣减")
    head_fee_type: Optional[int] = Field(None, description="头程费分配方式： 0 产品-计费重（默认） 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积")
    is_points_behind: Optional[int] = Field(None, description="是否分抛计算(0:否,1:是)")
    points_behind_coeffient: Optional[int] = Field(None, description="分抛系数(0-100)")
    is_return_stock: Optional[int] = Field(None, description="是否恢复库存， 0=否， 1=是")
    ware_house_bak_name: Optional[str] = Field(None, description="仓库名称(作为被删仓库的备用值)")
    is_print: Optional[int] = Field(None, description="是否打印拣货单 （0：未打印，1：已打印）")
    print_num: Optional[int] = Field(None, description="打印次数")
    is_pick: Optional[int] = Field(None, description="是否拣货 （0：未拣货，1:已拣货）")
    pick_time: Optional[str] = Field(None, description="完成拣货时间")
    print_time: Optional[int] = Field(None, description="最后一次打印时间")
    etd_date: Optional[str] = Field(None, description="开船时间")
    eta_date: Optional[str] = Field(None, description="预计到港时间")
    delivery_date: Optional[str] = Field(None, description="实际妥投时间")
    order_logistics_status: Optional[str] = Field(None, description="订单物流状态")
    shipment_user: Optional[str] = Field(None, description="发货人")
    wname: Optional[str] = Field(None, description="仓库名称")
    create_user: Optional[str] = Field(None, description="创建人")
    file_id: Optional[str] = Field(None, description="附件文件")
    actual_shipment_time: Optional[str] = Field(None, description="实际发货时间")
    logistics_channel_name: Optional[str] = Field(None, description="物流渠道名称")
    is_delete: Optional[int] = Field(None, description="0-未删除")
    destination_fulfillment_center_id: Optional[str] = Field(None, description="物流中心编码")
    cancel_time: Optional[int] = Field(None, description="作废时间(时间戳格式)")
    logistics_provider_id: Optional[int] = Field(None, description="物流商ID")
    logistics_provider_name: Optional[str] = Field(None, description="物流商名称")
    transportation_cost_status: Optional[int] = Field(None, description="物流费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    other_cost_status: Optional[int] = Field(None, description="其他费用填写状态 ，1：全部填写， 2：部分填写， 3：全未填写")
    pay_status: Optional[int] = Field(None, description="付款状态 0：未申请， 1：已申请， 2：部分付款， 3：已付清， 4：无")
    predicted_transportation_cost_status: Optional[int] = Field(None, description="预估物流费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    predicted_other_cost_status: Optional[int] = Field(None, description="预估其他费用填写状态， 1：全部填写， 2：部分填写， 3：全未填写")
    audit_status: Optional[int] = Field(None, description="审批状态， 121：待审核， 122：驳回， 123：通过， 124：作废")
    stash_shipment_uid: Optional[int] = Field(None, description="暂存发货人UID（审批流专用）")
    stash_shipment_time: Optional[int] = Field(None, description="暂存发货时间（审批流专用）")
    is_relate_aux: Optional[int] = Field(None, description="是否关联辅料， 0：否， 1：是")
    items: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistItems]] = Field(None, description="商品列表")
    logistics: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistLogistics]] = Field(None, description="物流信息列表（旧版物流信息）")
    auxs: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistAuxs]] = Field(None, description="辅料列表")
    principals: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistPrincipals]] = Field(None, description="权限人列表")
    msg: Optional[str] = Field(None, description="是")
    status_name: Optional[str] = Field(None, description="状态名称")
    last_update_time: Optional[str] = Field(None, description="最后修改日期")
    head_fee_type_name: Optional[str] = Field(None, description="头程费用名称")
    file_list: Optional[list] = Field(None, description="附件列表")
    box_type: Optional[str] = Field(None, description="装箱类型： SINGLE-每箱只允许一款SKU， MULTIPLE-每箱允许多款SKU")
    box_remark: Optional[str] = Field(None, description="装箱备注")
    logistics_list_type: Optional[dict] = Field(None, description="物流信息版本0旧版1新版")
    head_logistics_list: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistHeadLogisticsList]] = Field(None, description="新版物流信息列表(logistics_list_type = 1时才有意义)")
    box_list: Optional[List[StorageShipmentGetinboundshipmentlistmwsdetaillistBoxList]] = Field(None, description="箱规列表，每个子项代表一个箱规")


class StorageShipmentSearchprocessresultProcessResult(LingXingModel):
    """process_result sub-structure."""
    error_details: Optional[list] = Field(None, description="失败时返回错误信息数组")
    code: Optional[str] = Field(None, description="失败时返回错误代码")
    data: Optional[dict] = Field(None, description="成功时返回")

class StorageShipmentSearchprocessresultResponse(LingXingModel):
    """发货单创建接口结果查询."""
    request_flag: Optional[str] = Field(None, description="请求标识")
    request_url: Optional[str] = Field(None, description="请求接口")
    process_result: Optional[List[StorageShipmentSearchprocessresultProcessResult]] = Field(None, description="请求结果")
    process_msg: Optional[str] = Field(None, description="否")
    process_status: Optional[int] = Field(None, description="请求状态说明： 0 处理中 1 已成功处理 2 已失败处理")
    order_sn: Optional[str] = Field(None, description="成功时返回单号，失败时为空字符串")
    gmt_create: Optional[str] = Field(None, description="请求创建时间")
    gmt_modified: Optional[str] = Field(None, description="请求修改时间")


class StorageShipmentCreatesendedorderResponse(LingXingModel):
    """生成已发货的发货单."""
    order_sn: Optional[str] = Field(None, description="发货单号")


class StorageShipmentPrintfbalabelsResponse(LingXingModel):
    """查询FBA货件箱子、卡板标签."""
    total: Optional[int] = Field(None, description="总数")
    file_base64: Optional[str] = Field(None, description="成功时，将返回打印PDF文件的base64编码")


class StorageShipmentPrintfnskulabelsResponse(LingXingModel):
    """查询FBA货件商品FNSKU标签."""
    total: Optional[int] = Field(None, description="总数")
    file_base64: Optional[str] = Field(None, description="成功时，将返回打印PDF文件的base64编码")


# Migrated from old models/
class GetFbaProductListItem(LingXingModel):
    """Response item for GetFbaProductList."""

    asin: Optional[str] = None
    asin_url: Optional[str] = None
    fnsku: Optional[str] = None
    image: Optional[str] = None
    local_name: Optional[str] = None
    msku: Optional[str] = None
    parent_asin: Optional[str] = None
    product_id: Optional[int] = None
    sid: Optional[int] = None
    sku: Optional[str] = None
    title: Optional[str] = None


class GetHeadLogisticsFeeTypesItem(LingXingModel):
    """Response item for GetHeadLogisticsFeeTypes."""

    created_at: Optional[str] = None
    fee_type_id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None


class GetInboundShipmentListItem(LingXingModel):
    """Response item for GetInboundShipmentList."""

    actual_shipment_time: Optional[str] = None
    audit_status: Optional[int] = None
    create_time: Optional[str] = None
    create_user: Optional[str] = None
    custom_fields: Optional[list] = None
    delivery_date: Optional[str] = None
    destination_fulfillment_center_id: Optional[str] = None
    eta_date: Optional[str] = None
    etd_date: Optional[str] = None
    expected_arrival_date: Optional[str] = None
    fileList: Optional[list] = None
    file_id: Optional[str] = None
    gmt_create: Optional[str] = None
    head_fee_type: Optional[int] = None
    head_fee_type_name: Optional[str] = None
    head_fee_type_name_new: Optional[str] = None
    id: Optional[int] = None
    is_custom_shipment_time: Optional[int] = None
    is_delete: Optional[int] = None
    is_exist_clearance: Optional[int] = None
    is_exist_declaration: Optional[int] = None
    is_pick: Optional[int] = None
    is_print: Optional[int] = None
    is_return_stock: Optional[int] = None
    last_update_time: Optional[str] = None
    logistics: Optional[list] = None
    logistics_channel_name: Optional[str] = None
    logistics_list: Optional[list] = None
    logistics_provider_id: Optional[str] = None
    logistics_provider_name: Optional[str] = None
    logistics_tracking_number: Optional[str] = None
    method_id: Optional[str] = None
    method_name: Optional[str] = None
    not_relate_list: Optional[list] = None
    pay_status: Optional[int] = None
    pick_time: Optional[str] = None
    principal_user: Optional[list] = None
    print_num: Optional[int] = None
    relate_list: Optional[list] = None
    remark: Optional[str] = None
    shipment_sn: Optional[str] = None
    shipment_time: Optional[str] = None
    shipment_time_second: Optional[str] = None
    shipment_user: Optional[str] = None
    status: Optional[int] = None
    status_name: Optional[str] = None
    third_party_order_mode: Optional[int] = None
    third_party_order_status: Optional[int] = None
    update_time: Optional[str] = None
    vat_code: Optional[str] = None
    wid: Optional[int] = None
    wname: Optional[str] = None


class GetSeaTrackSupplierCarriersItem(LingXingModel):
    """Response item for GetSeaTrackSupplierCarriers."""

    home_page: Optional[str] = None
    name: Optional[str] = None
    shippers: Optional[str] = None


class ShipmentPlanListsItem(LingXingModel):
    """Response item for ShipmentPlanLists."""

    create_time: Optional[str] = None
    create_user: Optional[str] = None
    custom_fields: Optional[list] = None
    ispg_id: Optional[int] = None
    list: Optional[list] = None
    remark: Optional[str] = None
    seq: Optional[str] = None

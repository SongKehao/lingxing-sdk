"""Auto-generated response models for Warehouse."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class AwdInboundPlanCancelResponse(LingXingModel):
    """取消AWD入库任务."""
    order_id: Optional[str] = Field(None, description="AWD任务编号")


class AwdInboundPlanCreateinboundplanResponse(LingXingModel):
    """创建AWD入库任务."""
    order_id: Optional[str] = Field(None, description="AWD任务编号")


class AwdInboundPlanDetailAwddeliveredgoodsbo(LingXingModel):
    """awdDeliveredGoodsBO sub-structure."""
    destination_address_line1: Optional[str] = Field(None, description="配送地址-详细街道地址1")
    destination_address_line2: Optional[str] = Field(None, description="配送地址-详细街道地址2")
    destination_city: Optional[str] = Field(None, description="配送地址-城市")
    destination_country_code: Optional[str] = Field(None, description="配送地址-国家（地区）")
    destination_postal_code: Optional[str] = Field(None, description="配送地址-邮政编码")
    destination_state_or_region: Optional[str] = Field(None, description="配送地址-州/省/地区编码")

class AwdInboundPlanDetailAwddeliveredgoodsitembos(LingXingModel):
    """awdDeliveredGoodsItemBOS sub-structure."""
    asin: Optional[str] = Field(None, description="asin")
    box_quantity: Optional[str] = Field(None, description="箱数")
    expiration: Optional[str] = Field(None, description="有效期（yyyy-MM-dd）")
    fnsku: Optional[str] = Field(None, description="fnsku")
    height: Optional[float] = Field(None, description="箱子高")
    label_owner: Optional[str] = Field(None, description="标签类型（AMAZON,SELF）")
    length: Optional[float] = Field(None, description="箱子长")
    length_unit: Optional[str] = Field(None, description="长度单位(INCHES-英制, CENTIMETERS-公制)")
    msku: Optional[str] = Field(None, description="msku")
    parent_asin: Optional[str] = Field(None, description="父asin")
    prep_category: Optional[str] = Field(None, description="预处理类别：ADULT：成人；HANGER：悬挂在衣架上的服装；TEXTILE：服装、面料、毛绒玩具和纺织品；BABY：母婴用品；FRAGILE：易碎品；LIQUID：液体（未存放在玻璃容器中）；PERFORATED：打孔包装；GRANULAR：粉末、球状或颗粒状物品；SHARP：尖利物品；SMALL：小号；SET：套装销售；NONE：无需进行预处理；FC_Provided：亚马逊指定分类（...")
    prep_owner: Optional[str] = Field(None, description="预处理提供方（AMAZON,SELF）")
    product_name: Optional[str] = Field(None, description="品名")
    quantity_in_box: Optional[str] = Field(None, description="单箱数量")
    sku: Optional[str] = Field(None, description="sku")
    title: Optional[str] = Field(None, description="标题")
    url: Optional[str] = Field(None, description="图片url")
    weight: Optional[float] = Field(None, description="箱子重量")
    weight_unit: Optional[str] = Field(None, description="重量单位（（POUNDS-磅，KILOGRAMS-千克））")
    width: Optional[float] = Field(None, description="箱子宽")

class AwdInboundPlanDetailAwdshipmentvos(LingXingModel):
    """awdShipmentVOS sub-structure."""
    shipment_id: Optional[str] = Field(None, description="AWD货件单号")
    awd_delivered_goods_bo: Optional[dict] = Field(None, description="配送地址")
    awd_delivered_goods_item_bos: Optional[list] = Field(None, description="发货商品")
    awd_shipping_address_bo: Optional[dict] = Field(None, description="发货地址")
    carrier_code: Optional[str] = Field(None, description="承运方式")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    order_id: Optional[str] = Field(None, description="AWD入库任务号")
    remark: Optional[str] = Field(None, description="备注")
    ship_by: Optional[str] = Field(None, description="发货时间")
    sid: Optional[int] = Field(None, description="领星店铺ID")
    status: Optional[str] = Field(None, description="货件状态：CREATED：已创建；SHIPPED：已发货；IN_TRANSIT：运输中；RECEIVING：接收中；DELIVERED：已送达；CLOSED：已关闭；CANCELLED：已取消")
    tracking_id: Optional[str] = Field(None, description="跟踪编码")
    warehouse_reference_id: Optional[str] = Field(None, description="物流中心编码")

class AwdInboundPlanDetailAwdshippingaddressbo(LingXingModel):
    """awdShippingAddressBO sub-structure."""
    address_line1: Optional[str] = Field(None, description="发货地址-详细街道地址1")
    address_line2: Optional[str] = Field(None, description="发货地址-详细街道地址2")
    city: Optional[str] = Field(None, description="发货地址-城市")
    country_code: Optional[str] = Field(None, description="发货地址-国家(地区）")
    phone_number: Optional[str] = Field(None, description="发货地址-电话号码")
    postal_code: Optional[str] = Field(None, description="发货地址-邮箱编码")
    shipper_name: Optional[str] = Field(None, description="发货地址-发货方名称")
    state_or_province_code: Optional[str] = Field(None, description="发货地址-州/省/地区编码")
    zone: Optional[str] = Field(None, description="发货地址-区")

class AwdInboundPlanDetailResponse(LingXingModel):
    """查询AWD入库任务详情."""
    awd_delivered_goods_bo: Optional[List[AwdInboundPlanDetailAwddeliveredgoodsbo]] = Field(None, description="配送地址")
    awd_delivered_goods_item_bos: Optional[List[AwdInboundPlanDetailAwddeliveredgoodsitembos]] = Field(None, description="发货商品")
    awd_shipment_vos: Optional[List[AwdInboundPlanDetailAwdshipmentvos]] = Field(None, description="AWD货件")
    awd_shipping_address_bo: Optional[List[AwdInboundPlanDetailAwdshippingaddressbo]] = Field(None, description="发货地址")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    destination_region: Optional[str] = Field(None, description="地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-southeast：美国东南部（南卡罗来纳州分拨中心）；null：亚马逊分配（亚马逊将为您的货件分配最佳分拨中心）")
    gmt_create: Optional[str] = Field(None, description="创建时间（yyyy-MM-dd HH:mm:ss）")
    gmt_modified: Optional[str] = Field(None, description="更新时间（yyyy-MM-dd HH:mm:ss）")
    order_id: Optional[str] = Field(None, description="AWD入库任务号")
    remark: Optional[str] = Field(None, description="备注")
    sid: Optional[int] = Field(None, description="店铺id")
    status: Optional[str] = Field(None, description="任务状态：LOCALDRAFT：草稿；DRAFT：待确认；VALIDATING：更新中；CONFIRMED：已确认；CLOSED： 已关闭；EXPIRED：已过期；CANCELLED：已取消")


class AwdInboundPlanPageOrders(LingXingModel):
    """orders sub-structure."""
    asc: Optional[Any] = Field(None, description="否")
    column: Optional[Any] = Field(None, description="否")

class AwdInboundPlanPageRecords(LingXingModel):
    """records sub-structure."""
    awd_delivered_goods_bo: Optional[dict] = Field(None, description="配送地址")
    awd_delivered_goods_item_bos: Optional[list] = Field(None, description="发货商品")
    awd_shipment_vos: Optional[list] = Field(None, description="AWD货件")
    awd_shipping_address_bo: Optional[dict] = Field(None, description="发货地址")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    destination_region: Optional[str] = Field(None, description="地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-southeast：美国东南部（南卡罗来纳州分拨中心）；null：亚马逊分配（亚马逊将为您的货件分配最佳分拨中心）")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    order_id: Optional[str] = Field(None, description="AWD入库任务号")
    remark: Optional[str] = Field(None, description="备注")
    sid: Optional[int] = Field(None, description="店铺id")
    status: Optional[str] = Field(None, description="任务状态：LOCALDRAFT：草稿；DRAFT：待确认；VALIDATING：更新中；CONFIRMED：已确认；CLOSED： 已关闭；EXPIRED：已过期；CANCELLED：已取消")

class AwdInboundPlanPageResponse(LingXingModel):
    """查询AWD入库任务列表."""
    count_id: Optional[str] = Field(None, description="否")
    current: Optional[Any] = Field(None, description="否")
    max_limit: Optional[Any] = Field(None, description="否")
    optimize_count_sql: Optional[int] = Field(None, description="否")
    orders: Optional[List[AwdInboundPlanPageOrders]] = Field(None, description="否")
    pages: Optional[Any] = Field(None, description="否")
    records: Optional[List[AwdInboundPlanPageRecords]] = Field(None, description="否")
    search_count: Optional[int] = Field(None, description="否")
    size: Optional[Any] = Field(None, description="否")
    total: Optional[int] = Field(None, description="总数")


class AwdInboundPlanUpdateinboundplanResponse(LingXingModel):
    """更新AWD入库任务."""
    order_id: Optional[str] = Field(None, description="AWD任务编号")


class AwdInboundShipmentDetailAwddeliveredgoodsbo(LingXingModel):
    """awdDeliveredGoodsBO sub-structure."""
    destination_address_line1: Optional[str] = Field(None, description="配送地址-详细街道地址1")
    destination_address_line2: Optional[str] = Field(None, description="配送地址-详细街道地址2")
    destination_city: Optional[str] = Field(None, description="配送地址-城市")
    destination_country_code: Optional[str] = Field(None, description="配送地址-国家（地区）")
    destination_postal_code: Optional[str] = Field(None, description="配送地址-邮政编码")
    destination_state_or_region: Optional[str] = Field(None, description="配送地址-州/省/地区编码")

class AwdInboundShipmentDetailAwddeliveredgoodsitembos(LingXingModel):
    """awdDeliveredGoodsItemBOS sub-structure."""
    asin: Optional[str] = Field(None, description="asin")
    box_quantity: Optional[str] = Field(None, description="箱数")
    expiration: Optional[str] = Field(None, description="有效期（yyyy-MM-dd）")
    fnsku: Optional[str] = Field(None, description="fnsku")
    height: Optional[float] = Field(None, description="箱子高")
    label_owner: Optional[str] = Field(None, description="标签类型（AMAZON,SELF,NULL）")
    length: Optional[float] = Field(None, description="箱子长")
    length_unit: Optional[str] = Field(None, description="长度单位(INCHES-英制, CENTIMETERS-公制)")
    msku: Optional[str] = Field(None, description="msku")
    parent_asin: Optional[str] = Field(None, description="父asin")
    prep_category: Optional[str] = Field(None, description="预处理类别：ADULT：成人；HANGER：悬挂在衣架上的服装；TEXTILE：服装、面料、毛绒玩具和纺织品；BABY：母婴用品；FRAGILE：易碎品；LIQUID：液体（未存放在玻璃容器中）；PERFORATED：打孔包装；GRANULAR：粉末、球状或颗粒状物品；SHARP：尖利物品；SMALL：小号；SET：套装销售；NONE：无需进行预处理；FC_Provided：亚马逊指定分类（...")
    prep_owner: Optional[str] = Field(None, description="预处理提供方（AMAZON,SELF,NULL）")
    product_name: Optional[str] = Field(None, description="品名")
    quantity_in_box: Optional[str] = Field(None, description="单箱数量")
    sku: Optional[str] = Field(None, description="sku")
    title: Optional[str] = Field(None, description="标题")
    url: Optional[str] = Field(None, description="图片url")
    weight: Optional[float] = Field(None, description="箱子重量")
    weight_unit: Optional[str] = Field(None, description="重量单位（POUNDS-磅，KILOGRAMS-千克）")
    width: Optional[float] = Field(None, description="箱子宽")

class AwdInboundShipmentDetailAwdshippingaddressbo(LingXingModel):
    """awdShippingAddressBO sub-structure."""
    address_line1: Optional[str] = Field(None, description="发货地址-详细街道地址1")
    address_line2: Optional[str] = Field(None, description="发货地址-详细街道地址2")
    city: Optional[str] = Field(None, description="发货地址-城市")
    country_code: Optional[str] = Field(None, description="发货地址-国家(地区）")
    phone_number: Optional[str] = Field(None, description="发货地址-电话号码")
    postal_code: Optional[str] = Field(None, description="发货地址-邮箱编码")
    shipper_name: Optional[str] = Field(None, description="发货地址-发货方名称")
    state_or_province_code: Optional[str] = Field(None, description="发货地址-州/省/地区编码")
    zone: Optional[str] = Field(None, description="发货地址-区")

class AwdInboundShipmentDetailResponse(LingXingModel):
    """查询AWD入库货件详情."""
    awd_delivered_goods_bo: Optional[List[AwdInboundShipmentDetailAwddeliveredgoodsbo]] = Field(None, description="配送地址")
    awd_delivered_goods_item_bos: Optional[List[AwdInboundShipmentDetailAwddeliveredgoodsitembos]] = Field(None, description="发货商品")
    awd_shipping_address_bo: Optional[List[AwdInboundShipmentDetailAwdshippingaddressbo]] = Field(None, description="发货地址")
    carrier_code: Optional[str] = Field(None, description="承运方式")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    order_id: Optional[str] = Field(None, description="AWD入库任务号")
    stock_order_id: Optional[str] = Field(None, description="备货单号")
    remark: Optional[str] = Field(None, description="备注")
    ship_by: Optional[str] = Field(None, description="发货时间")
    sid: Optional[int] = Field(None, description="领星店铺ID")
    status: Optional[str] = Field(None, description="货件状态：CREATED：已创建；SHIPPED：已发货；IN_TRANSIT：运输中；RECEIVING：接收中；DELIVERED：已送达；CLOSED：已关闭；CANCELLED：已取消")
    tracking_id: Optional[str] = Field(None, description="跟踪编码")
    warehouse_reference_id: Optional[str] = Field(None, description="物流中心编码")


class AwdInboundShipmentPageOrders(LingXingModel):
    """orders sub-structure."""
    asc: Optional[Any] = Field(None, description="否")
    column: Optional[Any] = Field(None, description="否")

class AwdInboundShipmentPageRecords(LingXingModel):
    """records sub-structure."""
    awd_delivered_goods_bo: Optional[dict] = Field(None, description="配送地址")
    awd_delivered_goods_item_bos: Optional[list] = Field(None, description="发货商品")
    awd_shipping_address_bo: Optional[dict] = Field(None, description="发货地址")
    carrier_code: Optional[str] = Field(None, description="承运方式")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    order_id: Optional[str] = Field(None, description="AWD入库任务号")
    stock_order_id: Optional[str] = Field(None, description="备货单号")
    remark: Optional[str] = Field(None, description="备注")
    ship_by: Optional[str] = Field(None, description="发货时间")
    sid: Optional[int] = Field(None, description="领星店铺ID")
    status: Optional[str] = Field(None, description="货件状态：CREATED：已创建；SHIPPED：已发货；IN_TRANSIT：运输中；RECEIVING：接收中；DELIVERED：已送达；CLOSED：已关闭；CANCELLED：已取消")
    tracking_id: Optional[str] = Field(None, description="跟踪编码")
    warehouse_reference_id: Optional[str] = Field(None, description="物流中心编码")

class AwdInboundShipmentPageResponse(LingXingModel):
    """查询AWD入库货件列表."""
    count_id: Optional[str] = Field(None, description="否")
    current: Optional[Any] = Field(None, description="否")
    max_limit: Optional[Any] = Field(None, description="否")
    optimize_count_sql: Optional[int] = Field(None, description="否")
    orders: Optional[List[AwdInboundShipmentPageOrders]] = Field(None, description="否")
    pages: Optional[Any] = Field(None, description="否")
    records: Optional[List[AwdInboundShipmentPageRecords]] = Field(None, description="否")
    search_count: Optional[int] = Field(None, description="否")
    size: Optional[Any] = Field(None, description="否")
    total: Optional[Any] = Field(None, description="否")


class AdjustorderAdjustGetadjuststatusFaillist(LingXingModel):
    """failList sub-structure."""
    order_sn: Optional[str] = Field(None, description="单号")
    detail: Optional[str] = Field(None, description="失败原因")

class AdjustorderAdjustGetadjuststatusResponse(LingXingModel):
    """查询调整单确认调整异步结果."""
    success: Optional[str] = Field(None, description="成功数量")
    fail: Optional[str] = Field(None, description="失败数量")
    total: Optional[str] = Field(None, description="总单数")
    fail_list: Optional[List[AdjustorderAdjustGetadjuststatusFaillist]] = Field(None, description="失败明细")


class AdjustorderAdjustSetadjustResponse(LingXingModel):
    """调整单确认调整."""
    task_no: Optional[str] = Field(None, description="异步任务编号")
    type: Optional[Any] = Field(None, description="是")
    action_type: Optional[str] = Field(None, description="是")


class InboundorderInboundSetinboundFaillist(LingXingModel):
    """failList sub-structure."""
    order_sn: Optional[str] = Field(None, description="单号")
    detail: Optional[str] = Field(None, description="失败原因")

class InboundorderInboundSetinboundResponse(LingXingModel):
    """入库单确认入库."""
    success: Optional[str] = Field(None, description="成功数量")
    fail: Optional[str] = Field(None, description="失败数量")
    total: Optional[str] = Field(None, description="总单数")
    fail_list: Optional[List[InboundorderInboundSetinboundFaillist]] = Field(None, description="失败明细")


class OpenapiStorageFbawarehousedetailFbaStorageQuantityList(LingXingModel):
    """fba_storage_quantity_list sub-structure."""
    sid: Optional[int] = Field(None, description="店铺id")
    name: Optional[str] = Field(None, description="店铺名称")
    quantity_for_local_fulfillment: Optional[int] = Field(None, description="FBA可售数量")

class OpenapiStorageFbawarehousedetailResponse(LingXingModel):
    """查询FBA库存列表-v2."""
    name: Optional[str] = Field(None, description="仓库名")
    seller_group_name: Optional[str] = Field(None, description="共享仓店铺名")
    sid: Optional[int] = Field(None, description="店铺id【当仓库为共享仓时，sid为0返回】")
    asin: Optional[str] = Field(None, description="ASIN")
    product_name: Optional[str] = Field(None, description="品名")
    small_image_url: Optional[str] = Field(None, description="预览图链接")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sku: Optional[str] = Field(None, description="SKU")
    category_text: Optional[str] = Field(None, description="分类文本")
    cid: Optional[int] = Field(None, description="分类Id")
    product_brand_text: Optional[str] = Field(None, description="品牌文本")
    bid: Optional[int] = Field(None, description="品牌Id")
    share_type: Optional[int] = Field(None, description="共享类型: 0 非共享 1 北美共享 2 欧洲共享")
    total: Optional[int] = Field(None, description="总数")
    total_price: Optional[float] = Field(None, description="总价")
    available_total: Optional[int] = Field(None, description="可用总数")
    available_total_price: Optional[str] = Field(None, description="可用总数成本价")
    afn_fulfillable_quantity: Optional[int] = Field(None, description="FBA可售")
    afn_fulfillable_quantity_price: Optional[str] = Field(None, description="FBA可售成本价")
    reserved_fc_transfers: Optional[int] = Field(None, description="待调仓")
    reserved_fc_transfers_price: Optional[str] = Field(None, description="待调仓成本价")
    reserved_fc_processing: Optional[int] = Field(None, description="调仓中")
    reserved_fc_processing_price: Optional[str] = Field(None, description="调仓中成本价")
    reserved_customerorders: Optional[int] = Field(None, description="待发货")
    reserved_customerorders_price: Optional[str] = Field(None, description="待发货成本价")
    quantity: Optional[int] = Field(None, description="FBM可售")
    quantity_price: Optional[str] = Field(None, description="FBM可售成本价")
    afn_unsellable_quantity: Optional[int] = Field(None, description="不可售")
    afn_unsellable_quantity_price: Optional[str] = Field(None, description="不可售成本价")
    afn_inbound_working_quantity: Optional[int] = Field(None, description="计划入库")
    afn_inbound_working_quantity_price: Optional[str] = Field(None, description="计划入库成本价")
    afn_inbound_shipped_quantity: Optional[int] = Field(None, description="在途")
    afn_inbound_shipped_quantity_price: Optional[str] = Field(None, description="在途成本价")
    afn_inbound_receiving_quantity: Optional[int] = Field(None, description="入库中")
    afn_inbound_receiving_quantity_price: Optional[str] = Field(None, description="入库中成本价")
    stock_up_num: Optional[int] = Field(None, description="实际在途")
    stock_up_num_price: Optional[str] = Field(None, description="实际在途成本价")
    afn_researching_quantity: Optional[int] = Field(None, description="调查中数量")
    afn_researching_quantity_price: Optional[str] = Field(None, description="调查中数量成本价")
    total_fulfillable_quantity: Optional[int] = Field(None, description="总可用库存: 可售+待调仓+调仓中 【非ERP页面对应总库存】")
    inv_age_0_to_30_days: Optional[int] = Field(None, description="0-1个月库龄")
    inv_age_0_to_30_price: Optional[str] = Field(None, description="0-1个月库龄成本价")
    inv_age_31_to_60_days: Optional[int] = Field(None, description="1-2个月库龄")
    inv_age_31_to_60_price: Optional[str] = Field(None, description="1-2个月库龄成本价")
    inv_age_61_to_90_days: Optional[int] = Field(None, description="2-3个月库龄")
    inv_age_61_to_90_price: Optional[str] = Field(None, description="2-3个月库龄成本价")
    inv_age_0_to_90_days: Optional[int] = Field(None, description="0-3个月库龄")
    inv_age_0_to_90_price: Optional[str] = Field(None, description="0-3个月库龄成本价")
    inv_age_91_to_180_days: Optional[int] = Field(None, description="3-6个月库龄")
    inv_age_91_to_180_price: Optional[str] = Field(None, description="3-6个月库龄成本价")
    inv_age_181_to_270_days: Optional[int] = Field(None, description="6-9个月库龄")
    inv_age_181_to_270_price: Optional[str] = Field(None, description="6-9个月库龄成本价")
    inv_age_271_to_330_days: Optional[int] = Field(None, description="9-11个月库龄")
    inv_age_271_to_330_price: Optional[str] = Field(None, description="9-11个月库龄成本价")
    inv_age_271_to_365_days: Optional[int] = Field(None, description="9-12个月库龄")
    inv_age_271_to_365_price: Optional[str] = Field(None, description="9-12个月库龄成本价")
    inv_age_331_to_365_days: Optional[int] = Field(None, description="11-12个月库龄")
    inv_age_331_to_365_price: Optional[str] = Field(None, description="11-12个月库龄成本价")
    inv_age_365_plus_days: Optional[int] = Field(None, description="12个月以上库龄")
    inv_age_365_plus_price: Optional[str] = Field(None, description="12个月以上库龄成本价")
    recommended_action: Optional[str] = Field(None, description="推荐操作")
    sell_through: Optional[float] = Field(None, description="售出率")
    estimated_excess_quantity: Optional[float] = Field(None, description="预计冗余数量")
    estimated_storage_cost_next_month: Optional[float] = Field(None, description="预计30天仓储费用")
    fba_minimum_inventory_level: Optional[float] = Field(None, description="最低库存水平")
    fba_inventory_level_health_status: Optional[str] = Field(None, description="库存水平健康度")
    historical_days_of_supply: Optional[float] = Field(None, description="历史供货天数")
    historical_days_of_supply_price: Optional[str] = Field(None, description="历史供货天数成本价")
    low_inventory_level_fee_applied: Optional[str] = Field(None, description="低库存水平费收取情况")
    fulfillment_channel: Optional[str] = Field(None, description="配送方式")
    cg_price: Optional[str] = Field(None, description="单位采购成本")
    cg_transport_costs: Optional[str] = Field(None, description="单位头程费用")
    warehouse_damaged_quantity: Optional[int] = Field(None, description="不可售详情：房屋残损")
    customer_damaged_quantity: Optional[int] = Field(None, description="不可售详情：买家残损")
    carrier_damaged_quantity: Optional[int] = Field(None, description="不可售详情：承运人残损")
    distributor_damaged_quantity: Optional[int] = Field(None, description="不可售详情：分销商残损")
    defective_quantity: Optional[int] = Field(None, description="不可售详情：存在瑕疵")
    expired_quantity: Optional[int] = Field(None, description="不可售详情：已过期")
    fba_storage_quantity_list: Optional[List[OpenapiStorageFbawarehousedetailFbaStorageQuantityList]] = Field(None, description="FBA可售信息列表，当仓库为共享仓库时，该字段才返回")
    total: Optional[int] = Field(None, description="总数")


class OutboundorderOutboundDeleteFaillist(LingXingModel):
    """failList sub-structure."""
    order_sn: Optional[str] = Field(None, description="失败单号")
    detail: Optional[str] = Field(None, description="失败原因")

class OutboundorderOutboundDeleteResponse(LingXingModel):
    """删除出库单."""
    success: Optional[str] = Field(None, description="成功数量")
    fail: Optional[str] = Field(None, description="失败数量")
    total: Optional[str] = Field(None, description="总单数")
    fail_list: Optional[List[OutboundorderOutboundDeleteFaillist]] = Field(None, description="失败明细")


class OutboundorderOutboundSetoutboundFaillist(LingXingModel):
    """failList sub-structure."""
    order_sn: Optional[str] = Field(None, description="单号")
    detail: Optional[str] = Field(None, description="失败原因")

class OutboundorderOutboundSetoutboundResponse(LingXingModel):
    """出库单确认出库."""
    success: Optional[str] = Field(None, description="成功数量")
    fail: Optional[str] = Field(None, description="失败数量")
    total: Optional[str] = Field(None, description="总单数")
    fail_list: Optional[List[OutboundorderOutboundSetoutboundFaillist]] = Field(None, description="失败明细")


class OverseawarehouseStockorderDetailTotal(LingXingModel):
    """total sub-structure."""
    product_count: Optional[float] = Field(None, description="产品总数")
    package_num: Optional[str] = Field(None, description="装箱数量")
    stock_num: Optional[str] = Field(None, description="备货数量")

class OverseawarehouseStockorderDetailProducts(LingXingModel):
    """products sub-structure."""
    product_code: Optional[str] = Field(None, description="第三方sku")
    twp_name: Optional[str] = Field(None, description="第三方产品名")
    product_id: Optional[float] = Field(None, description="产品id")
    sku: Optional[str] = Field(None, description="系统sku")
    product_name: Optional[str] = Field(None, description="产品名称")
    fnsku: Optional[str] = Field(None, description="fnsku")
    seller_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    match_num: Optional[float] = Field(None, description="配对数量")
    stock_num: Optional[float] = Field(None, description="备货数量")
    package_num: Optional[float] = Field(None, description="装箱数量")
    tariffs_currency_unit: Optional[str] = Field(None, description="预估税费单位")
    tariffs: Optional[float] = Field(None, description="预估税费")
    spec_name: Optional[str] = Field(None, description="箱规名称")
    pic_url: Optional[str] = Field(None, description="图片链接")
    country_name: Optional[str] = Field(None, description="国家名称")
    outbound_cost_unit: Optional[float] = Field(None, description="单位出库费用(¥)")
    auxiliary_cost_unit: Optional[float] = Field(None, description="单位辅料费用(¥)")
    tariffs_unit: Optional[float] = Field(None, description="单位税费(¥)")
    outbound_head_cost_unit: Optional[float] = Field(None, description="单位出库头程(¥)")
    fba_cost: Optional[float] = Field(None, description="单位头程费用(¥)")
    stock_cost: Optional[float] = Field(None, description="单位库存成本(¥)")
    stock_profit: Optional[float] = Field(None, description="库存成本盈亏(¥)")
    spec_info: Optional[dict] = Field(None, description="箱规信息")
    cg_package_length: Optional[float] = Field(None, description="包装规格长度")
    cg_package_width: Optional[float] = Field(None, description="包装规格宽度")
    cg_package_height: Optional[float] = Field(None, description="包装规格高度")
    cg_product_gross_weight: Optional[float] = Field(None, description="单品毛重")
    remark: Optional[str] = Field(None, description="备注")
    awd_shipment_id: Optional[str] = Field(None, description="AWD货件")
    warehouse_items: Optional[list] = Field(None, description="备货产品列表")

class OverseawarehouseStockorderDetailPurchaseinfo(LingXingModel):
    """purchaseInfo sub-structure."""
    product_id: Optional[float] = Field(None, description="产品ID")
    product_name: Optional[str] = Field(None, description="产品名称")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    seller_id: Optional[str] = Field(None, description="店铺ID")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    stock_num: Optional[float] = Field(None, description="可用总出库量")
    batch_record_list: Optional[list] = Field(None, description="批次记录列表")

class OverseawarehouseStockorderDetailLogisticsinfo(LingXingModel):
    """logisticsInfo sub-structure."""
    head_logistics_info: Optional[dict] = Field(None, description="物流信息")
    head_logistics_fee_info: Optional[list] = Field(None, description="新版费用明细列表")
    logistics_list: Optional[list] = Field(None, description="旧版费用明细列表")
    head_logistics_tracking_info: Optional[list] = Field(None, description="轨迹信息")
    head_logistics_fee_provider_info: Optional[list] = Field(None, description="多物流商列表")

class OverseawarehouseStockorderDetailBoxData(LingXingModel):
    """box_data sub-structure."""
    box_type: Optional[float] = Field(None, description="装箱方式")
    box_content: Optional[list] = Field(None, description="装箱内容列表")
    box_remark: Optional[str] = Field(None, description="装箱备注")
    total_box_num: Optional[float] = Field(None, description="总箱数")
    total_box_weight: Optional[float] = Field(None, description="总重量（kg）")
    total_box_volume: Optional[float] = Field(None, description="总体积（m³）")
    total_box_volume_weight: Optional[float] = Field(None, description="总体积重（kg）")

class OverseawarehouseStockorderDetailHeadLogisticsList(LingXingModel):
    """head_logistics_list sub-structure."""
    actual_expenses_list: Optional[dict] = Field(None, description="实际费用列表")

class OverseawarehouseStockorderDetailResponse(LingXingModel):
    """查询备货单详情."""
    overseas_order_no: Optional[str] = Field(None, description="备货单号")
    inbound_order_no: Optional[str] = Field(None, description="第三方单号")
    s_wid: Optional[float] = Field(None, description="发货仓库id")
    s_wname: Optional[str] = Field(None, description="发货仓库名称")
    r_wid: Optional[float] = Field(None, description="收货仓库id")
    r_wname: Optional[str] = Field(None, description="收货仓库名称")
    transportation_name: Optional[str] = Field(None, description="运输方式")
    logistics_name: Optional[str] = Field(None, description="物流商名称")
    logistics_provider_id: Optional[float] = Field(None, description="物流商id")
    logistics_provider_name: Optional[str] = Field(None, description="物流商名称")
    logistics_way_id: Optional[float] = Field(None, description="物流渠道id")
    logistics_way_name: Optional[str] = Field(None, description="物流渠道名称")
    share_text: Optional[str] = Field(None, description="分摊方式")
    estimated_time: Optional[str] = Field(None, description="预计到货时间")
    real_delivery_time: Optional[str] = Field(None, description="实际发货时间")
    status: Optional[str] = Field(None, description="备货单状态 枚举类，详情见附加说明")
    status_text: Optional[str] = Field(None, description="备货单状态名称 枚举类，详情见附加说明")
    remark: Optional[str] = Field(None, description="备注")
    total: Optional[List[OverseawarehouseStockorderDetailTotal]] = Field(None, description="总计信息")
    products: Optional[List[OverseawarehouseStockorderDetailProducts]] = Field(None, description="备货产品列表")
    purchase_info: Optional[List[OverseawarehouseStockorderDetailPurchaseinfo]] = Field(None, description="采购信息列表")
    logistics_info: Optional[List[OverseawarehouseStockorderDetailLogisticsinfo]] = Field(None, description="物流信息")
    box_data: Optional[List[OverseawarehouseStockorderDetailBoxData]] = Field(None, description="装箱信息")
    custom_fields: Optional[dict] = Field(None, description="自定义字段，返回格式见附加说明")
    head_logistics_list: Optional[List[OverseawarehouseStockorderDetailHeadLogisticsList]] = Field(None, description="头程物流列表")


class OverseawarehousesettingMatchlistResponse(LingXingModel):
    """查询海外仓sku配对列表."""
    total: Optional[int] = Field(None, description="总数")
    country_name: Optional[str] = Field(None, description="国家")
    fnsku: Optional[str] = Field(None, description="fnsku")
    is_matched: Optional[bool] = Field(None, description="是否配对")
    is_matched_text: Optional[str] = Field(None, description="是否配对")
    local_name: Optional[str] = Field(None, description="本地品名")
    local_sku: Optional[str] = Field(None, description="本地sku")
    match_msg: Optional[str] = Field(None, description="配对信息")
    match_num: Optional[int] = Field(None, description="配对数量")
    oversea_product_code: Optional[str] = Field(None, description="第三方仓sku")
    oversea_product_name: Optional[str] = Field(None, description="第三方仓品名")
    oversea_spec: Optional[str] = Field(None, description="规格，winit专用")
    oversea_unique_code: Optional[str] = Field(None, description="三方sku唯一编码")
    product_id: Optional[int] = Field(None, description="产品id")
    seller_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    sid: Optional[int] = Field(None, description="同sellerId")
    tw_id: Optional[int] = Field(None, description="三方仓id")
    twp_id: Optional[int] = Field(None, description="三方商品id")
    warehouse_code: Optional[str] = Field(None, description="第三方仓仓库代码")
    warehouse_name: Optional[str] = Field(None, description="第三方仓仓库")
    warehouse_name_local: Optional[str] = Field(None, description="本地仓库名称")
    wid: Optional[int] = Field(None, description="仓库id")
    wpm_id: Optional[int] = Field(None, description="配对id")


class QualityinspectionorderDetailImage(LingXingModel):
    """image sub-structure."""
    file_id: Optional[str] = Field(None, description="图片ID")
    name: Optional[str] = Field(None, description="图片名称")
    url: Optional[str] = Field(None, description="链接")

class QualityinspectionorderDetailQcStandard(LingXingModel):
    """qc_standard sub-structure."""
    pqs_id: Optional[str] = Field(None, description="质检标准id")
    qc_id: Optional[str] = Field(None, description="质检单id")
    qc_sn: Optional[str] = Field(None, description="质检单号")
    type: Optional[int] = Field(None, description="质检标准类型： 1 系统 2 自定义")
    qc_item: Optional[str] = Field(None, description="质检项")
    qc_content: Optional[str] = Field(None, description="质检内容")

class QualityinspectionorderDetailWhbCodeGoodList(LingXingModel):
    """whb_code_good_list sub-structure."""
    whb_num: Optional[int] = Field(None, description="仓位数量")
    whb_code: Optional[str] = Field(None, description="仓位编码")

class QualityinspectionorderDetailWhbCodeBadList(LingXingModel):
    """whb_code_bad_list sub-structure."""
    whb_num: Optional[int] = Field(None, description="仓位数量")
    whb_code: Optional[str] = Field(None, description="仓位编码")

class QualityinspectionorderDetailResponse(LingXingModel):
    """查询质检单详情."""
    total: Optional[int] = Field(None, description="总数")
    qc_id: Optional[str] = Field(None, description="质检单id")
    qc_sn: Optional[str] = Field(None, description="质检单号")
    qc_type: Optional[str] = Field(None, description="质检类型： 1 仓库质检 2 预检 3 免检")
    qc_type_text: Optional[str] = Field(None, description="质检类型名称")
    qc_method: Optional[str] = Field(None, description="质检方式： 1 抽检 2 全检")
    qc_method_text: Optional[str] = Field(None, description="质检方式名称")
    qc_image: Optional[str] = Field(None, description="质检标准图片id")
    receive_time: Optional[str] = Field(None, description="收货时间")
    receive_uid: Optional[str] = Field(None, description="收货人id")
    qc_uid: Optional[str] = Field(None, description="质检人id")
    sid: Optional[str] = Field(None, description="店铺id")
    product_receive_num: Optional[int] = Field(None, description="质检量")
    product_good_num: Optional[int] = Field(None, description="良品量")
    product_bad_num: Optional[int] = Field(None, description="次品量")
    qc_time: Optional[str] = Field(None, description="质检时间")
    status: Optional[str] = Field(None, description="质检状态： 0 待质检(质检中) 1 已质检 2 已免检 10 已质检(已撤销) 20 已免检(已撤销)")
    status_text: Optional[str] = Field(None, description="质检状态说明")
    price: Optional[str] = Field(None, description="单价")
    product_id: Optional[str] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    wid: Optional[int] = Field(None, description="仓库id")
    order_id: Optional[str] = Field(None, description="采购单id/委外单id")
    order_sn: Optional[str] = Field(None, description="采购单号/委外单号")
    order_type: Optional[str] = Field(None, description="订单类型")
    cg_uid: Optional[str] = Field(None, description="采购员id")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    file_id: Optional[str] = Field(None, description="附件id")
    qc_num: Optional[int] = Field(None, description="抽检数量")
    qc_bad_num: Optional[int] = Field(None, description="质检次品量")
    qc_rate: Optional[str] = Field(None, description="抽检比例")
    qc_rate_pass: Optional[str] = Field(None, description="抽检合格率")
    qc_remark: Optional[str] = Field(None, description="备注")
    qc_pic_url: Optional[list] = Field(None, description="图片地址")
    whb_code_good: Optional[str] = Field(None, description="可用仓位")
    whb_code_bad: Optional[str] = Field(None, description="次品仓位")
    product_qc_num: Optional[int] = Field(None, description="质检量")
    qc_realname: Optional[str] = Field(None, description="质检员")
    receive_realname: Optional[str] = Field(None, description="收货员")
    opt_realname: Optional[str] = Field(None, description="操作员")
    pic_url: Optional[str] = Field(None, description="产品图片地址")
    is_combo: Optional[int] = Field(None, description="是否组合产品： 0 否 1 是")
    is_aux: Optional[int] = Field(None, description="是否辅料： 0 否 1 是")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    source: Optional[int] = Field(None, description="采购数据来源： 0 web 1 金蝶 2 openApi")
    file: Optional[list] = Field(None, description="附件")
    image: Optional[List[QualityinspectionorderDetailImage]] = Field(None, description="质检标准图片")
    qc_standard: Optional[List[QualityinspectionorderDetailQcStandard]] = Field(None, description="质检标准")
    custom_receive_time: Optional[str] = Field(None, description="收货时间")
    custom_qc_time: Optional[str] = Field(None, description="质检时间")
    delivery_order_sn: Optional[str] = Field(None, description="收货单号")
    source_custom_order_sn: Optional[str] = Field(None, description="自定义单号")
    whb_code_good_list: Optional[List[QualityinspectionorderDetailWhbCodeGoodList]] = Field(None, description="良品仓位")
    whb_code_bad_list: Optional[List[QualityinspectionorderDetailWhbCodeBadList]] = Field(None, description="次品仓位")


class WmsorderCancelFailedreason(LingXingModel):
    """failedReason sub-structure."""
    order_number: Optional[str] = Field(None, description="失败的单号")
    message: Optional[str] = Field(None, description="失败的原因")

class WmsorderCancelResponse(LingXingModel):
    """销售出库单截单."""
    success_num: Optional[int] = Field(None, description="成功的数量")
    failed_num: Optional[int] = Field(None, description="失败的数量")
    failed_reason: Optional[List[WmsorderCancelFailedreason]] = Field(None, description="失败的原因列表")


class WmsorderGetwmsordersbyordernumbersOrderlist(LingXingModel):
    """orderList sub-structure."""
    actual_carrier: Optional[str] = Field(None, description="实际承运商")
    amazon_order_id: Optional[str] = Field(None, description="平台单号")
    auto_complete: Optional[int] = Field(None, description="是否快速出库，枚举值：1-是, 0-否")
    batch_no: Optional[str] = Field(None, description="波次号")
    company_id: Optional[int] = Field(None, description="企业ID")
    is_advance_delivery: Optional[int] = Field(None, description="是否预发货，枚举值：1-是, 0-否")
    is_check: Optional[int] = Field(None, description="是否已验货，枚举值：1-是, 0-否")
    is_lock_storage: Optional[int] = Field(None, description="是否已锁定库存，枚举值：1-是, 0-否")
    is_order_print: Optional[int] = Field(None, description="是否已打印发货单，枚举值：1-是, 0-否")
    is_surface_print: Optional[int] = Field(None, description="是否已打印面单，枚举值：1-是, 0-否")
    is_weigh: Optional[int] = Field(None, description="是否已称重，枚举值：1-是, 0-否")
    logistics_provider_name: Optional[str] = Field(None, description="物流商名称")
    logistics_type_name: Optional[str] = Field(None, description="物流方式名称")
    order_buyer_notes: Optional[str] = Field(None, description="买家备注")
    order_customer_service_notes: Optional[str] = Field(None, description="客服备注")
    order_from: Optional[int] = Field(None, description="订单来源，枚举值：1-线上订单, 2-手工订单, 3-补发订单")
    order_number: Optional[str] = Field(None, description="系统单号")
    order_type: Optional[int] = Field(None, description="订单类型，枚举值：1-一单一件, 2-多品多件, 3-单品多件")
    platform_code: Optional[int] = Field(None, description="平台代码")
    product_info: Optional[list] = Field(None, description="商品信息列表")
    product_list: Optional[list] = Field(None, description="商品列表（拣货）")
    reference_no: Optional[str] = Field(None, description="参考号")
    sid: Optional[int] = Field(None, description="店铺ID")
    site_code: Optional[str] = Field(None, description="站点代码")
    status: Optional[int] = Field(None, description="状态，枚举值：1-物流下单, 2-发货中, 3-已发货, 4-已删除")
    surface_file_id: Optional[int] = Field(None, description="面单ID")
    surface_pdf: Optional[str] = Field(None, description="面单PDF链接")
    tracking_no: Optional[str] = Field(None, description="跟踪号")
    warehouse_type: Optional[int] = Field(None, description="仓库类型")
    waybill_no: Optional[str] = Field(None, description="运单号")
    wid: Optional[int] = Field(None, description="仓库ID")
    wo_id: Optional[int] = Field(None, description="销售出库单ID")
    wo_number: Optional[str] = Field(None, description="销售出库单号")
    zid: Optional[int] = Field(None, description="企业ID")

class WmsorderGetwmsordersbyordernumbersResponse(LingXingModel):
    """查询销售出库单详情."""
    order_count: Optional[int] = Field(None, description="订单数量")
    order_list: Optional[List[WmsorderGetwmsordersbyordernumbersOrderlist]] = Field(None, description="订单列表")
    total: Optional[int] = Field(None, description="总记录数")


class LocalInventoryWarehouseResponse(LingXingModel):
    """查询仓库列表."""
    total: Optional[int] = Field(None, description="总数")
    wid: Optional[int] = Field(None, description="系统仓库id")
    name: Optional[str] = Field(None, description="仓库名")
    type: Optional[int] = Field(None, description="仓库类型： 1 本地仓 3 海外仓 4 平台仓 6 AWD仓")
    is_delete: Optional[str] = Field(None, description="是否删除：0 未删除，1 已删除")
    t_country_area_name: Optional[str] = Field(None, description="第三方仓库国家/地区")
    t_status: Optional[int] = Field(None, description="状态:0 未启用 ，1 启用")
    t_warehouse_code: Optional[str] = Field(None, description="第三方仓库代码")
    t_warehouse_name: Optional[str] = Field(None, description="第三方仓库名")
    country_code: Optional[str] = Field(None, description="国家代码")
    wp_id: Optional[int] = Field(None, description="服务商ID，仅type=3且仓库为第三方海外仓时有值")
    wp_name: Optional[str] = Field(None, description="系统服务商名称")


class LocalInventoryGetbatchdetaillistResponse(LingXingModel):
    """查询批次明细."""
    total: Optional[int] = Field(None, description="总数")
    batch_no: Optional[str] = Field(None, description="批次号")
    source_batch_no: Optional[str] = Field(None, description="源头批次号")
    order_sn: Optional[str] = Field(None, description="入库单号")
    type: Optional[int] = Field(None, description="入库类型")
    type_name: Optional[str] = Field(None, description="入库类型描述")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    wid: Optional[int] = Field(None, description="仓库id")
    wh_name: Optional[str] = Field(None, description="仓库名称")
    total: Optional[int] = Field(None, description="结存总数【在途结存 + 在库结存】")
    transit_balance_num: Optional[int] = Field(None, description="在途结存")
    balance_num: Optional[int] = Field(None, description="在库结存")
    good_transit_num: Optional[int] = Field(None, description="可用在途量")
    bad_transit_num: Optional[int] = Field(None, description="次品在途量")
    qc_num: Optional[int] = Field(None, description="待检量")
    good_num: Optional[int] = Field(None, description="可用量")
    bad_num: Optional[int] = Field(None, description="次品量")
    plan_sn: Optional[list] = Field(None, description="采购计划单号信息")
    purchase_order_sns: Optional[list] = Field(None, description="采购单单号信息")
    delivery_order_sns: Optional[list] = Field(None, description="收货单单号信息")
    supplier_ids: Optional[list] = Field(None, description="供应商id信息")
    supplier_names: Optional[list] = Field(None, description="供应商名称列表")
    amount: Optional[str] = Field(None, description="货值")
    head_stock_cost: Optional[str] = Field(None, description="头程")
    fee: Optional[str] = Field(None, description="费用")
    stock_cost: Optional[str] = Field(None, description="库存成本")


class LocalInventoryGetbatchstatementlistResponse(LingXingModel):
    """查询批次流水."""
    total: Optional[int] = Field(None, description="总数")
    batch_state_id: Optional[str] = Field(None, description="批次流水id")
    type: Optional[int] = Field(None, description="批次流水子类型id")
    type_name: Optional[str] = Field(None, description="流水类型名称")
    batch_no: Optional[str] = Field(None, description="批次号")
    order_sn: Optional[str] = Field(None, description="单据号")
    source_batch_no: Optional[list] = Field(None, description="源头批次号")
    source_order_sn: Optional[list] = Field(None, description="源头单据号")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    wid: Optional[int] = Field(None, description="仓库id")
    wh_name: Optional[str] = Field(None, description="仓库名称")
    transit_balance_num: Optional[int] = Field(None, description="在途结存量")
    balance_num: Optional[int] = Field(None, description="在库结存量")
    good_transit_num: Optional[int] = Field(None, description="可用在途量")
    bad_transit_num: Optional[int] = Field(None, description="次品在途量")
    qc_num: Optional[int] = Field(None, description="待检量")
    good_num: Optional[int] = Field(None, description="可用量")
    bad_num: Optional[int] = Field(None, description="次品量")
    amount: Optional[str] = Field(None, description="货值")
    fee: Optional[str] = Field(None, description="费用")
    head_stock_cost: Optional[str] = Field(None, description="头程")
    stock_cost: Optional[str] = Field(None, description="库存成本")
    plan_sn: Optional[list] = Field(None, description="采购计划单号信息")
    purchase_order_sns: Optional[list] = Field(None, description="采购单单号信息")
    delivery_order_sns: Optional[list] = Field(None, description="收货单单号信息")
    supplier_ids: Optional[list] = Field(None, description="供应商id信息")
    supplier_names: Optional[list] = Field(None, description="供应商名称信息")


class LocalInventoryInventorybindetailsThirdInventory(LingXingModel):
    """third_inventory sub-structure."""
    qty_sellable: Optional[int] = Field(None, description="可用量")
    qty_pending: Optional[int] = Field(None, description="待上架库存")
    qty_reserved: Optional[int] = Field(None, description="锁定量")
    qty_onway: Optional[int] = Field(None, description="备货在途")

class LocalInventoryInventorybindetailsResponse(LingXingModel):
    """查询仓位库存明细."""
    wid: Optional[int] = Field(None, description="仓库id")
    wh_name: Optional[str] = Field(None, description="仓库名称")
    whb_id: Optional[int] = Field(None, description="仓位id")
    whb_name: Optional[str] = Field(None, description="仓位名称")
    whb_type: Optional[str] = Field(None, description="仓位类型")
    whb_type_name: Optional[str] = Field(None, description="仓位类型名称")
    product_id: Optional[int] = Field(None, description="商品id")
    sku: Optional[str] = Field(None, description="SKU")
    seller_id: Optional[str] = Field(None, description="店铺id")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    total: Optional[int] = Field(None, description="总量")
    lock_num: Optional[int] = Field(None, description="锁定量")
    valid_num: Optional[str] = Field(None, description="未锁定量")
    third_inventory: Optional[List[LocalInventoryInventorybindetailsThirdInventory]] = Field(None, description="海外仓第三方库存信息")
    total: Optional[int] = Field(None, description="总条数")


class LocalInventoryInventorydetailsThirdInventory(LingXingModel):
    """third_inventory sub-structure."""
    qty_sellable: Optional[int] = Field(None, description="可用量")
    qty_pending: Optional[int] = Field(None, description="待上架库存")
    qty_reserved: Optional[int] = Field(None, description="锁定量")
    qty_onway: Optional[int] = Field(None, description="第三方海外仓备货在途")
    third_inventory_data: Optional[list] = Field(None, description="海外仓子产品库存明细")

class LocalInventoryInventorydetailsStockAgeList(LingXingModel):
    """stock_age_list sub-structure."""
    name: Optional[str] = Field(None, description="标题")
    qty: Optional[int] = Field(None, description="数量")

class LocalInventoryInventorydetailsResponse(LingXingModel):
    """查询仓库库存明细."""
    total: Optional[int] = Field(None, description="总数")
    wid: Optional[int] = Field(None, description="仓库id")
    product_id: Optional[int] = Field(None, description="本地产品id")
    sku: Optional[str] = Field(None, description="SKU")
    seller_id: Optional[str] = Field(None, description="店铺id")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    product_total: Optional[int] = Field(None, description="实际库存总量【可用量+次品量+待检待上架量+锁定量】")
    product_valid_num: Optional[int] = Field(None, description="可用量")
    product_bad_num: Optional[int] = Field(None, description="次品量")
    product_qc_num: Optional[int] = Field(None, description="待检待上架量")
    product_lock_num: Optional[int] = Field(None, description="锁定量")
    stock_cost_total: Optional[str] = Field(None, description="库存成本")
    quantity_receive: Optional[str] = Field(None, description="待到货量")
    stock_cost: Optional[str] = Field(None, description="单位库存成本")
    product_onway: Optional[int] = Field(None, description="调拨在途")
    transit_head_cost: Optional[str] = Field(None, description="调拨在途头程成本")
    average_age: Optional[int] = Field(None, description="平均库龄")
    third_inventory: Optional[List[LocalInventoryInventorydetailsThirdInventory]] = Field(None, description="海外仓第三方库存信息")
    stock_age_list: Optional[List[LocalInventoryInventorydetailsStockAgeList]] = Field(None, description="库龄信息")
    purchase_price: Optional[str] = Field(None, description="采购单价")
    price: Optional[str] = Field(None, description="单位费用")
    head_stock_price: Optional[str] = Field(None, description="单位头程")
    stock_price: Optional[str] = Field(None, description="单位库存成本")


class LocalInventoryWarehousebinstatementResponse(LingXingModel):
    """查询仓位流水."""
    wid: Optional[int] = Field(None, description="仓库ID")
    ware_house_name: Optional[str] = Field(None, description="仓库名")
    whb_id: Optional[str] = Field(None, description="仓位id")
    whb_name: Optional[str] = Field(None, description="仓位名称")
    whb_type_name: Optional[str] = Field(None, description="仓位类型名称")
    order_sn: Optional[str] = Field(None, description="单据号")
    product_id: Optional[int] = Field(None, description="商品ID")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    num: Optional[int] = Field(None, description="数量")
    type: Optional[int] = Field(None, description="流水类型")
    remark: Optional[str] = Field(None, description="备注")
    opt_uid: Optional[int] = Field(None, description="操作人员ID")
    opt_time: Optional[str] = Field(None, description="操作时间")
    type_text: Optional[str] = Field(None, description="流水类型文本")
    opt_realname: Optional[str] = Field(None, description="操作人员姓名")
    total: Optional[int] = Field(None, description="总数目")


class LocalInventoryWarehousestatementResponse(LingXingModel):
    """查询库存流水（旧）."""
    statement_id: Optional[str] = Field(None, description="流水ID")
    wid: Optional[int] = Field(None, description="仓库ID")
    ware_house_name: Optional[str] = Field(None, description="仓库名")
    bid: Optional[int] = Field(None, description="商品品牌ID")
    order_sn: Optional[str] = Field(None, description="单据号")
    product_id: Optional[int] = Field(None, description="商品ID")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    product_total: Optional[float] = Field(None, description="商品总量")
    product_good_num: Optional[float] = Field(None, description="良品量")
    product_bad_num: Optional[float] = Field(None, description="次品量")
    product_qc_num: Optional[float] = Field(None, description="质检量")
    product_lock_num: Optional[float] = Field(None, description="锁定量")
    price: Optional[float] = Field(None, description="单价")
    amount: Optional[float] = Field(None, description="金额")
    type: Optional[str] = Field(None, description="流水类型： 1 其他入库 2 采购入库 3 调拨入库 10 其它入库（已撤销） 11 其他出库 12 FBA出库 13 调拨出库 14 退货出库 15 FBM退货 16 换标入库 17 加工入库 18 拆分入库 20 采购入库（已撤销） 21 库存调整 23 委外入库 25 盘盈入库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 43 FBM出库 50 成本...")
    remark: Optional[str] = Field(None, description="备注")
    opt_uid: Optional[int] = Field(None, description="操作人员ID")
    opt_time: Optional[str] = Field(None, description="操作时间")
    cancel_time: Optional[str] = Field(None, description="撤销时间")
    fee_cost: Optional[str] = Field(None, description="费用成本")
    brand_name: Optional[str] = Field(None, description="品牌")
    single_fee_cost: Optional[float] = Field(None, description="单位费用成本")
    single_cg_price: Optional[float] = Field(None, description="采购单价")
    product_amounts: Optional[float] = Field(None, description="货值")
    type_text: Optional[str] = Field(None, description="流水类型文本")
    opt_realname: Optional[str] = Field(None, description="操作人员姓名")
    total: Optional[int] = Field(None, description="总数目")


class LocalInventoryWarehousebinSkuFnsku(LingXingModel):
    """sku_fnsku sub-structure."""
    sku: Optional[str] = Field(None, description="sku")
    fnsku: Optional[str] = Field(None, description="fnsku")

class LocalInventoryWarehousebinResponse(LingXingModel):
    """查询本地仓位列表."""
    id: Optional[int] = Field(None, description="仓位id")
    wid: Optional[int] = Field(None, description="仓库ID")
    ware_house_name: Optional[str] = Field(None, description="仓库名")
    storage_bin: Optional[int] = Field(None, description="仓位")
    whb_status: Optional[str] = Field(None, description="仓位状态")
    type: Optional[str] = Field(None, description="仓位类型")
    sku_fnsku: Optional[List[LocalInventoryWarehousebinSkuFnsku]] = Field(None, description="仓位商品关系")
    total: Optional[int] = Field(None, description="是")


class DeliveryreceiptPurchasereceiptorderGetorderlistList(LingXingModel):
    """list sub-structure."""
    order_sn: Optional[str] = Field(None, description="收货单号")
    status: Optional[int] = Field(None, description="状态：10 待收货，40 已完成")
    create_time: Optional[str] = Field(None, description="创建时间")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人")
    update_time: Optional[str] = Field(None, description="更新时间")
    receive_time: Optional[str] = Field(None, description="收货时间")
    receive_uid: Optional[int] = Field(None, description="收货人id")
    receive_realname: Optional[str] = Field(None, description="收货人")
    wid: Optional[int] = Field(None, description="仓库id")
    order_type: Optional[int] = Field(None, description="收货类型：1 采购订单，2 委外订单")
    qc_type: Optional[int] = Field(None, description="质检类型：1 仓库质检，2 预检，3 免检")
    business_order_sn: Optional[str] = Field(None, description="来源单号")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    logistics_company: Optional[str] = Field(None, description="物流商")
    logistics_order_no: Optional[str] = Field(None, description="物流单号")
    expect_arrival_time: Optional[str] = Field(None, description="预计到货时间")
    shipping_currency: Optional[str] = Field(None, description="运费币种")
    shipping_cost: Optional[str] = Field(None, description="运费")
    other_currency: Optional[str] = Field(None, description="其他费用币种")
    other_fee: Optional[str] = Field(None, description="其他费用")
    opt_uid: Optional[int] = Field(None, description="采购员id")
    opt_realname: Optional[str] = Field(None, description="采购员")
    inbound_order_sns: Optional[list] = Field(None, description="入库单号")
    remark: Optional[str] = Field(None, description="单据备注")
    item_list: Optional[list] = Field(None, description="产品列表")

class DeliveryreceiptPurchasereceiptorderGetorderlistResponse(LingXingModel):
    """查询收货单列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[DeliveryreceiptPurchasereceiptorderGetorderlistList]] = Field(None, description="列表")


class FbaFbastockFbalistList(LingXingModel):
    """list sub-structure."""
    wname: Optional[str] = Field(None, description="仓库名称")
    name: Optional[str] = Field(None, description="仓库名称【同wname】")
    sid: Optional[int] = Field(None, description="店铺id")
    asin: Optional[str] = Field(None, description="ASIN")
    product_name: Optional[str] = Field(None, description="品名")
    product_image: Optional[str] = Field(None, description="图片")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sku: Optional[str] = Field(None, description="SKU")
    category_name: Optional[str] = Field(None, description="分类名称")
    category_id: Optional[int] = Field(None, description="分类Id")
    brand_name: Optional[str] = Field(None, description="品牌名称")
    brand_id: Optional[int] = Field(None, description="品牌id")
    stock_cost_total: Optional[float] = Field(None, description="货值")
    cost: Optional[float] = Field(None, description="库存成本")
    share_type: Optional[int] = Field(None, description="共享类型： 0 非共享 1 北美共享 2 欧洲共享")
    afn_fulfillable_quantity: Optional[str] = Field(None, description="可售")
    reserved_fc_transfers: Optional[str] = Field(None, description="待调仓")
    reserved_fc_processing: Optional[str] = Field(None, description="调仓中")
    reserved_customerorders: Optional[str] = Field(None, description="待发货")
    total_fulfillable_quantity: Optional[int] = Field(None, description="总可用库存：可售+待调仓+调仓中 【非ERP页面对应总库存】")
    afn_unsellable_quantity: Optional[int] = Field(None, description="不可售")
    afn_inbound_working_quantity: Optional[int] = Field(None, description="计划入库")
    afn_inbound_shipped_quantity: Optional[int] = Field(None, description="在途")
    afn_inbound_receiving_quantity: Optional[int] = Field(None, description="入库中")
    afn_erp_real_shipped_quantity: Optional[int] = Field(None, description="实际在途")
    afn_researching_quantity: Optional[int] = Field(None, description="调查中数量")
    inv_age_0_to_30_days: Optional[str] = Field(None, description="0-1个月库龄")
    inv_age_31_to_60_days: Optional[str] = Field(None, description="1-2个月库龄")
    inv_age_61_to_90_days: Optional[str] = Field(None, description="2-3个月库龄")
    inv_age_0_to_90_days: Optional[str] = Field(None, description="0-3个月库龄")
    inv_age_91_to_180_days: Optional[str] = Field(None, description="3-6个月库龄")
    inv_age_181_to_270_days: Optional[str] = Field(None, description="6-9个月库龄")
    inv_age_271_to_330_days: Optional[str] = Field(None, description="9-11个月库龄")
    inv_age_331_to_365_days: Optional[str] = Field(None, description="11-12个月库龄")
    inv_age_271_to_365_days: Optional[str] = Field(None, description="9-12个月库存")
    inv_age_365_plus_days: Optional[str] = Field(None, description="12个月以上库龄")
    fulfillment_channel_name: Optional[str] = Field(None, description="配送方式")
    afn_fulfillable_quantity_multi: Optional[list] = Field(None, description="欧洲共享的多国店铺列表")

class FbaFbastockFbalistResponse(LingXingModel):
    """查询FBA库存列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[FbaFbastockFbalistList]] = Field(None, description="列表数据")


class InventorylogWarehouseinventoryWarehousecenterstatementResponse(LingXingModel):
    """查询库存流水（新）."""
    wid: Optional[int] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    order_sn: Optional[str] = Field(None, description="操作单据号")
    product_id: Optional[int] = Field(None, description="产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="sku")
    seller_id: Optional[int] = Field(None, description="店铺id")
    fnsku: Optional[str] = Field(None, description="fnsku")
    product_good_num: Optional[int] = Field(None, description="可用量")
    product_bad_num: Optional[int] = Field(None, description="次品量")
    product_qc_num: Optional[int] = Field(None, description="待检量")
    product_lock_good_num: Optional[int] = Field(None, description="可用锁定量")
    product_lock_bad_num: Optional[int] = Field(None, description="次品锁定量")
    good_transit_num: Optional[int] = Field(None, description="良品在途")
    bad_transit_num: Optional[int] = Field(None, description="次品在途")
    type: Optional[int] = Field(None, description="流水类型")
    type_text: Optional[str] = Field(None, description="流水类型文本")
    sub_type: Optional[str] = Field(None, description="子类型")
    sub_type_text: Optional[str] = Field(None, description="子类型文本")
    fee_cost: Optional[str] = Field(None, description="总费用成本")
    single_cg_price: Optional[str] = Field(None, description="采购单价")
    single_fee_cost: Optional[str] = Field(None, description="单位费用")
    single_stock_price: Optional[str] = Field(None, description="单位库存成本")
    stock_cost: Optional[str] = Field(None, description="库存成本")
    product_amounts: Optional[str] = Field(None, description="货值")
    head_stock_price: Optional[str] = Field(None, description="单位头程")
    head_stock_cost: Optional[str] = Field(None, description="头程")
    opt_uid: Optional[int] = Field(None, description="操作人员ID")
    opt_time: Optional[str] = Field(None, description="操作时间")
    opt_real_name: Optional[str] = Field(None, description="操作人员姓名")
    remark: Optional[str] = Field(None, description="备注")
    bid: Optional[int] = Field(None, description="品牌id")
    brand_name: Optional[str] = Field(None, description="品牌名称")
    ref_order_sn: Optional[str] = Field(None, description="关联单据号")
    product_total: Optional[int] = Field(None, description="总量")
    good_balance_num: Optional[int] = Field(None, description="可用结存量")
    bad_balance_num: Optional[int] = Field(None, description="次品结存量")
    good_lock_balance_num: Optional[int] = Field(None, description="可用锁定结存量")
    bad_lock_balance_num: Optional[int] = Field(None, description="次品锁定结存量")
    qc_balance_num: Optional[int] = Field(None, description="质检结存量")
    good_transit_balance_num: Optional[int] = Field(None, description="可用在途结存量")
    statement_id: Optional[str] = Field(None, description="流水ID")
    bad_transit_balance_num: Optional[int] = Field(None, description="次品在途结存量")


class InventoryreceiptInventorycheckAddorderResponse(LingXingModel):
    """创建已完成的盘点单."""
    total: Optional[int] = Field(None, description="总数")
    order_sn: Optional[str] = Field(None, description="盘点单号")


class InventoryreceiptInventorycheckGetorderdetailFile(LingXingModel):
    """file sub-structure."""
    file_id: Optional[int] = Field(None, description="附件id")
    file_name: Optional[str] = Field(None, description="附件名称")
    file_url: Optional[str] = Field(None, description="附件URL")

class InventoryreceiptInventorycheckGetorderdetailProductList(LingXingModel):
    """product_list sub-structure."""
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    seller_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country_name: Optional[str] = Field(None, description="店铺所属国家名称")
    whb_id: Optional[int] = Field(None, description="仓位id")
    whb_code: Optional[str] = Field(None, description="仓位")
    whb_code_text: Optional[str] = Field(None, description="仓位名称")
    whb_type: Optional[int] = Field(None, description="仓位类型： 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品 7 可用在途 8 次品在途")
    whb_type_text: Optional[str] = Field(None, description="仓位类型文本")
    book_inventory: Optional[int] = Field(None, description="账面库存")
    actual_inventory: Optional[int] = Field(None, description="实盘库存")
    different_count: Optional[int] = Field(None, description="盘点差异")
    remark: Optional[str] = Field(None, description="明细备注")
    pic_url: Optional[str] = Field(None, description="产品图片链接")
    is_combo: Optional[int] = Field(None, description="是否组合产品：0 否，1 是")
    is_aux: Optional[int] = Field(None, description="是否辅料：0 否，1 是")

class InventoryreceiptInventorycheckGetorderdetailItemTotal(LingXingModel):
    """item_total sub-structure."""
    book_inventory: Optional[int] = Field(None, description="账面库存总数")
    actual_inventory: Optional[int] = Field(None, description="实盘库存总数")
    different_count: Optional[int] = Field(None, description="盘点差异总数")

class InventoryreceiptInventorycheckGetorderdetailResponse(LingXingModel):
    """查询盘点单详情."""
    order_sn: Optional[str] = Field(None, description="盘点单号")
    status: Optional[int] = Field(None, description="盘点状态： 10 待盘点 20 预锁 30 盘点中 40 已盘点 121 待审核 122 已驳回 123 通过 124 作废")
    status_text: Optional[str] = Field(None, description="状态文本")
    wid: Optional[int] = Field(None, description="盘点仓库id")
    ware_house_name: Optional[str] = Field(None, description="盘点仓库名称")
    check_type: Optional[int] = Field(None, description="盘点类型： 1 整仓盘点 2 SKU盘点 3 仓位盘点 4 SKU+仓位盘点")
    check_type_text: Optional[str] = Field(None, description="盘点类型说明")
    is_display_check: Optional[int] = Field(None, description="是否明盘：0 否，1 是")
    display_check_name: Optional[str] = Field(None, description="是否明盘文本")
    is_zero: Optional[int] = Field(None, description="是否零库存参与盘点：0 否，1 是")
    product_type: Optional[int] = Field(None, description="产品种类")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_user: Optional[str] = Field(None, description="创建人姓名")
    create_time: Optional[str] = Field(None, description="创建时间")
    check_uid: Optional[int] = Field(None, description="盘点人id")
    check_user: Optional[str] = Field(None, description="盘点人姓名")
    real_check_uid: Optional[int] = Field(None, description="实际盘点人id")
    real_check_user: Optional[str] = Field(None, description="实际盘点人姓名")
    check_time: Optional[str] = Field(None, description="盘点时间")
    commit_uid: Optional[int] = Field(None, description="提交人id")
    commit_user: Optional[str] = Field(None, description="提交人姓名")
    commit_time: Optional[str] = Field(None, description="提交时间")
    cancel_uid: Optional[int] = Field(None, description="作废人id")
    cancel_user: Optional[str] = Field(None, description="作废人姓名")
    cancel_time: Optional[str] = Field(None, description="作废时间")
    cancel_reason: Optional[str] = Field(None, description="作废原因")
    remark: Optional[str] = Field(None, description="备注")
    request_status: Optional[int] = Field(None, description="单据状态：0 正常，1 处理中")
    file: Optional[List[InventoryreceiptInventorycheckGetorderdetailFile]] = Field(None, description="上传附件信息")
    product_list: Optional[List[InventoryreceiptInventorycheckGetorderdetailProductList]] = Field(None, description="盘点明细列表")
    total: Optional[int] = Field(None, description="盘点明细总数")
    item_total: Optional[List[InventoryreceiptInventorycheckGetorderdetailItemTotal]] = Field(None, description="盘点明细信息")


class InventoryreceiptInventorycheckGetorderlistFile(LingXingModel):
    """file sub-structure."""
    file_id: Optional[int] = Field(None, description="附件id")
    file_name: Optional[str] = Field(None, description="附件名称")
    file_url: Optional[str] = Field(None, description="附件URL")

class InventoryreceiptInventorycheckGetorderlistResponse(LingXingModel):
    """查询盘点单列表."""
    total: Optional[int] = Field(None, description="总数")
    order_sn: Optional[str] = Field(None, description="盘点单号")
    status: Optional[int] = Field(None, description="盘点状态： 10 待盘点 20 预锁 30 盘点中 40 已盘点 121 待审核 122 已驳回 123 通过 124 作废")
    status_text: Optional[str] = Field(None, description="状态文本")
    wid: Optional[int] = Field(None, description="盘点仓库id")
    ware_house_name: Optional[str] = Field(None, description="盘点仓库名称")
    check_type: Optional[int] = Field(None, description="盘点类型： 1 整仓盘点 2 SKU盘点 3 仓位盘点 4 SKU+仓位盘点")
    check_type_text: Optional[str] = Field(None, description="盘点类型文本")
    is_display_check: Optional[int] = Field(None, description="是否明盘：0 否，1 是")
    display_check_name: Optional[str] = Field(None, description="是否明盘文本")
    is_zero: Optional[int] = Field(None, description="是否零库存参与盘点：0 否，1 是")
    product_type: Optional[int] = Field(None, description="产品种类")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_user: Optional[str] = Field(None, description="创建人姓名")
    create_time: Optional[str] = Field(None, description="创建时间")
    check_uid: Optional[int] = Field(None, description="盘点人id")
    check_user: Optional[str] = Field(None, description="盘点人姓名")
    real_check_uid: Optional[int] = Field(None, description="实际盘点人id")
    real_check_user: Optional[str] = Field(None, description="实际盘点人姓名")
    check_time: Optional[str] = Field(None, description="盘点时间")
    commit_uid: Optional[int] = Field(None, description="提交人id")
    commit_user: Optional[str] = Field(None, description="提交人姓名")
    commit_time: Optional[str] = Field(None, description="提交时间")
    cancel_uid: Optional[int] = Field(None, description="作废人id")
    cancel_user: Optional[str] = Field(None, description="作废人姓名")
    cancel_time: Optional[str] = Field(None, description="作废时间")
    cancel_reason: Optional[str] = Field(None, description="作废原因")
    remark: Optional[str] = Field(None, description="备注")
    request_status: Optional[str] = Field(None, description="单据状态：0 正常，1 处理中")
    file: Optional[List[InventoryreceiptInventorycheckGetorderlistFile]] = Field(None, description="上传附件信息")


class InventoryreceiptStorageadjustmentAddadjustmentorderResponse(LingXingModel):
    """创建已完成的数量调整单."""
    order_sn: Optional[str] = Field(None, description="生成的调整单的单据号")


class InventoryreceiptStorageadjustmentAddrebrandadjustmentorderResponse(LingXingModel):
    """创建已完成的换标调整单."""
    order_sn: Optional[str] = Field(None, description="生成的调整单的单据号")


class InventoryreceiptStorageadjustmentAddskuadjustmentorderResponse(LingXingModel):
    """创建已完成的SKU调整单."""
    order_sn: Optional[str] = Field(None, description="生成的调整单的单据号")


class InventoryreceiptStorageadjustmentGetstorageadjustorderlistItemList(LingXingModel):
    """item_list sub-structure."""
    sku: Optional[str] = Field(None, description="本地产品sku")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    pic_url: Optional[str] = Field(None, description="图片链接")
    product_remark: Optional[str] = Field(None, description="产品备注")
    fnsku: Optional[str] = Field(None, description="fnsku")
    seller_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country_name: Optional[str] = Field(None, description="店铺所属国家")
    adjustment_valid_num: Optional[int] = Field(None, description="可用调整量")
    available_bin_list: Optional[list] = Field(None, description="出库的可用仓位列表【只有换标调整才有该字段】")
    to_sku: Optional[str] = Field(None, description="调整的sku【只有SKU调整才有该字段】")
    to_product_name: Optional[str] = Field(None, description="调整的品名【只有SKU调整才有该字段】")
    to_fnsku: Optional[str] = Field(None, description="调整的fnsku【数量调整没有该字段】")
    to_seller_id: Optional[str] = Field(None, description="调整的店铺id【数量调整没有该字段】")
    to_seller_name: Optional[str] = Field(None, description="调整的店铺名称【数量调整没有该字段】")
    to_country_name: Optional[str] = Field(None, description="调整的店铺所属国家【数量调整没有该字段】")
    to_available_bin: Optional[str] = Field(None, description="【废弃字段】换标的入库仓位【只有换标调整才有该字段】")
    to_available_bin_name: Optional[str] = Field(None, description="【废弃字段】换标的入库仓位名称【只有换标调整才有该字段】")
    available_bin: Optional[str] = Field(None, description="可用仓位【只有数量调整有该字段】")
    available_bin_name: Optional[str] = Field(None, description="可用仓位名称【只有数量调整有该字段】")
    inferior_bin: Optional[str] = Field(None, description="次品仓位【只有数量调整有该字段】")
    inferior_bin_name: Optional[str] = Field(None, description="次品仓位名称【只有数量调整有该字段】")
    adjustment_bad_num: Optional[int] = Field(None, description="次品调整量【只有数量调整有该字段】")
    to_available_bin_list: Optional[list] = Field(None, description="换标的入库仓位列表")

class InventoryreceiptStorageadjustmentGetstorageadjustorderlistResponse(LingXingModel):
    """查询调整单列表."""
    total: Optional[int] = Field(None, description="查询总数")
    order_sn: Optional[str] = Field(None, description="单据号")
    wid: Optional[int] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    type: Optional[int] = Field(None, description="调整类型： 0 数量调整 1 换标调整 2 sku调整")
    type_text: Optional[str] = Field(None, description="调整类型文本")
    status: Optional[int] = Field(None, description="单据状态： 5 待提交 10 待调整 20 已完成 30 已删除 121 待审批 122 已驳回")
    status_text: Optional[str] = Field(None, description="单据状态说明")
    remark: Optional[str] = Field(None, description="单据备注")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    commit_uid: Optional[int] = Field(None, description="提交人id")
    commit_realname: Optional[str] = Field(None, description="提交人名称")
    commit_time: Optional[str] = Field(None, description="提交时间")
    adjustment_uid: Optional[int] = Field(None, description="调整人id")
    adjustment_realname: Optional[str] = Field(None, description="调整人名称")
    adjustment_time: Optional[str] = Field(None, description="调整时间")
    opt_uid: Optional[int] = Field(None, description="单据最后操作人id")
    opt_realname: Optional[str] = Field(None, description="单据最后操作人名称")
    opt_time: Optional[str] = Field(None, description="单据最后操作时间")
    increment_time: Optional[str] = Field(None, description="单据增量时间")
    item_list: Optional[List[InventoryreceiptStorageadjustmentGetstorageadjustorderlistItemList]] = Field(None, description="单据明细列表")


class InventoryreceiptStorageallocationAddallocationorderResponse(LingXingModel):
    """创建待收货/已完成的调拨单."""
    order_sn: Optional[str] = Field(None, description="调拨单号")
    total: Optional[int] = Field(None, description="总数")


class InventoryreceiptStorageallocationGetstorageallocationlistItemList(LingXingModel):
    """item_list sub-structure."""
    product_id: Optional[int] = Field(None, description="产品id")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    product_total: Optional[int] = Field(None, description="调拨总量")
    product_good_num: Optional[int] = Field(None, description="调拨可用量")
    product_bad_num: Optional[int] = Field(None, description="调拨次品量")
    price: Optional[float] = Field(None, description="单价")
    amount: Optional[float] = Field(None, description="货值")
    seller_id: Optional[int] = Field(None, description="店铺id")
    to_available_bin: Optional[str] = Field(None, description="入库可用仓位编码")
    to_inferior_bin: Optional[str] = Field(None, description="入库次品仓位编码")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country_name: Optional[str] = Field(None, description="店铺所属国家名称")
    product_name: Optional[str] = Field(None, description="品名")
    in_available_storage_bin_code: Optional[str] = Field(None, description="入库可用仓位名称")
    in_inferior_storage_bin_code: Optional[str] = Field(None, description="入库次品仓位名称")
    outbound_list: Optional[list] = Field(None, description="出库仓位列表")
    out_stock_cost: Optional[str] = Field(None, description="出库单位费用")
    pic_url: Optional[str] = Field(None, description="产品图片链接")
    cg_package_length: Optional[float] = Field(None, description="包装规格-长（CM）")
    cg_package_width: Optional[float] = Field(None, description="包装规格-宽（CM）")
    cg_package_height: Optional[float] = Field(None, description="包装规格-高（CM）")
    cg_product_gross_weight: Optional[float] = Field(None, description="单品净重")
    freight_fee_unit: Optional[float] = Field(None, description="单位运费")
    other_fee_unit: Optional[float] = Field(None, description="单位其他费用")
    product_remark: Optional[str] = Field(None, description="产品备注")
    out_available_bin_list: Optional[list] = Field(None, description="出库可用仓位列表")
    out_inferior_bin_list: Optional[list] = Field(None, description="出库次品仓位列表")
    in_available_bin_list: Optional[list] = Field(None, description="入库可用仓位列表")
    in_inferior_bin_list: Optional[list] = Field(None, description="入库次品仓位列表")

class InventoryreceiptStorageallocationGetstorageallocationlistResponse(LingXingModel):
    """查询调拨单列表."""
    order_sn: Optional[str] = Field(None, description="单据号")
    wid: Optional[int] = Field(None, description="出库仓库id")
    to_wid: Optional[int] = Field(None, description="入库仓库id")
    opt_uid: Optional[int] = Field(None, description="操作人（用户id）")
    opt_time: Optional[str] = Field(None, description="操作时间")
    order_amount: Optional[float] = Field(None, description="订单金额")
    out_bin_type: Optional[int] = Field(None, description="出仓类型： 0 不指定仓位 1 指定仓位")
    ware_house_bak_name: Optional[str] = Field(None, description="出库仓库名称")
    to_ware_house_bak_name: Optional[str] = Field(None, description="入库仓库名称")
    status: Optional[int] = Field(None, description="单据状态： 5-待提交 10 待调拨 19 待收货 20 已完成 30 已删除 121 待审批 122 已驳回")
    status_text: Optional[str] = Field(None, description="单据状态文本")
    create_time: Optional[str] = Field(None, description="创建时间")
    create_uid: Optional[int] = Field(None, description="创建人（用户id）")
    transfer_time: Optional[str] = Field(None, description="操作调拨时间")
    transfer_uid: Optional[int] = Field(None, description="操作调拨人（用户id）")
    remark: Optional[str] = Field(None, description="单据备注")
    freight_fee: Optional[float] = Field(None, description="运费")
    other_fee: Optional[float] = Field(None, description="其他费用")
    fee_part_type: Optional[int] = Field(None, description="费用分摊方式： 0 不分摊 1 按金额分摊 2 按sku数量分摊 3 按重量 4 按体积 5 按自定义")
    type: Optional[int] = Field(None, description="调拨类型：1-简易调拨；2-完整调拨")
    receive_uid: Optional[int] = Field(None, description="确认收货操作人（用户id）")
    receive_time: Optional[str] = Field(None, description="确认收货收货时间")
    finish_time: Optional[str] = Field(None, description="单据完成时间")
    finish_uid: Optional[int] = Field(None, description="单据完成操作人（用户id）")
    increment_time: Optional[str] = Field(None, description="单据更新时间")
    outbound_order_sn: Optional[str] = Field(None, description="关联的出库单单号")
    inbound_order_sn: Optional[str] = Field(None, description="关联的入库单单号")
    opt_realname: Optional[str] = Field(None, description="操作人姓名")
    create_realname: Optional[str] = Field(None, description="创建人姓名")
    transfer_realname: Optional[str] = Field(None, description="确认调拨操作人姓名")
    receive_realname: Optional[str] = Field(None, description="确认收货操作人姓名")
    finish_realname: Optional[str] = Field(None, description="单据完成操作人姓名")
    fee_part_type_text: Optional[str] = Field(None, description="费用分摊方式文本")
    out_bin_type_text: Optional[str] = Field(None, description="出仓方式文本")
    item_list: Optional[List[InventoryreceiptStorageallocationGetstorageallocationlistItemList]] = Field(None, description="产品明细列表")
    good_total_num: Optional[int] = Field(None, description="订单可用调拨总量")
    bad_total_num: Optional[int] = Field(None, description="订单次品调拨总量")
    total: Optional[int] = Field(None, description="查询总数")


class InventoryreceiptStorageallocationSubmitallocationorderResponse(LingXingModel):
    """创建待调拨的调拨单."""
    order_sn: Optional[str] = Field(None, description="调拨单号")


class InventoryreceiptStorageprocessAddstorageprocessorderResponse(LingXingModel):
    """创建加工单 / 拆分单."""
    order_sn: Optional[str] = Field(None, description="加工单/拆分单 单号")
    total: Optional[int] = Field(None, description="总数")


class InventoryreceiptStorageprocessGetorderlistsProductList(LingXingModel):
    """product_list sub-structure."""
    sku: Optional[str] = Field(None, description="组合品sku")
    product_name: Optional[str] = Field(None, description="组合品产品名称")
    fnsku: Optional[str] = Field(None, description="组合品fnksu")
    seller_id: Optional[int] = Field(None, description="组合品店铺id")
    seller_name: Optional[str] = Field(None, description="组合品店铺名称")
    process_fee: Optional[str] = Field(None, description="加工费")
    remark: Optional[str] = Field(None, description="备注")
    whb_code_good: Optional[list] = Field(None, description="加工单组合品入库仓位")
    pic_url: Optional[str] = Field(None, description="组合品图片")
    quantity: Optional[int] = Field(None, description="加工量/拆分量")
    item_list: Optional[list] = Field(None, description="单品明细项")

class InventoryreceiptStorageprocessGetorderlistsResponse(LingXingModel):
    """加工单列表."""
    total: Optional[int] = Field(None, description="单据总数")
    process_sn: Optional[str] = Field(None, description="加工/拆分单号")
    status: Optional[int] = Field(None, description="订单状态： 0 待配货 1 待完成 2 已完成")
    type: Optional[str] = Field(None, description="单据类型： 1 加工单 2 拆分单")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    wid: Optional[int] = Field(None, description="仓库id")
    create_by: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    finish_realname: Optional[str] = Field(None, description="最后操作人")
    finish_time: Optional[str] = Field(None, description="最后操作时间")
    finish_uid: Optional[int] = Field(None, description="最后操作人id")
    remark: Optional[str] = Field(None, description="备注")
    update_time: Optional[str] = Field(None, description="更新时间")
    product_list: Optional[List[InventoryreceiptStorageprocessGetorderlistsProductList]] = Field(None, description="组合品项")


class OwmsInboundCreateinboundResponse(LingXingModel):
    """创建待发货/待收货/已完成的备货单."""
    overseas_order_no: Optional[str] = Field(None, description="系统备货单号")
    total: Optional[int] = Field(None, description="数据总量")


class OwmsInboundGetpackingdataBoxList(LingXingModel):
    """box_list sub-structure."""
    box_no: Optional[int] = Field(None, description="箱号")
    height: Optional[float] = Field(None, description="箱子高(CM)")
    length: Optional[float] = Field(None, description="箱子长(CM)")
    width: Optional[float] = Field(None, description="箱子宽(CM)")
    weight: Optional[float] = Field(None, description="箱子重(KG)")
    items: Optional[list] = Field(None, description="商品详情")

class OwmsInboundGetpackingdataResponse(LingXingModel):
    """查询备货单装箱信息."""
    overseas_order_no: Optional[str] = Field(None, description="备货单号")
    packaging_type: Optional[float] = Field(None, description="装箱类型：1 每箱多个sku，2 每箱一个sku")
    box_count: Optional[float] = Field(None, description="总箱数")
    box_list: Optional[List[OwmsInboundGetpackingdataBoxList]] = Field(None, description="装箱信息")
    total: Optional[int] = Field(None, description="是")


class OwmsInboundGetreceivegoodrecordsResponse(LingXingModel):
    """查询备货单收货记录."""
    woop_id: Optional[int] = Field(None, description="订单商品id")
    overseas_order_no: Optional[str] = Field(None, description="备货单单号")
    inbound_order_no: Optional[str] = Field(None, description="入库单号")
    current_receive_num: Optional[int] = Field(None, description="本次收货数量")
    receive_num: Optional[int] = Field(None, description="应收数量")
    update_user: Optional[str] = Field(None, description="操作人")
    update_time: Optional[str] = Field(None, description="操作时间")
    sid: Optional[int] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    product_id: Optional[int] = Field(None, description="产品id")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sku: Optional[str] = Field(None, description="本地商品sku")
    in_storage_bins: Optional[str] = Field(None, description="入库仓位")
    real_receive_at: Optional[str] = Field(None, description="实际收货时间")
    product_name: Optional[str] = Field(None, description="本地商品名称")
    twp_sku: Optional[str] = Field(None, description="第三方海外仓商品sku")
    twp_name: Optional[str] = Field(None, description="第三方海外仓商品名称")
    match_num: Optional[int] = Field(None, description="第三方海外仓商品对应的本地商品配对数量")
    total: Optional[int] = Field(None, description="总数")


class OwmsInboundListinboundProducts(LingXingModel):
    """products sub-structure."""
    product_id: Optional[int] = Field(None, description="产品id")
    sku: Optional[str] = Field(None, description="sku")
    product_name: Optional[str] = Field(None, description="产品名")
    fnsku: Optional[str] = Field(None, description="fnsku")
    pic_url: Optional[str] = Field(None, description="商品图片")
    seller_arr: Optional[list] = Field(None, description="店铺信息【已废弃】")
    stock_num: Optional[int] = Field(None, description="备货数量")
    receive_num: Optional[int] = Field(None, description="收货数量")
    product_valid_num: Optional[int] = Field(None, description="可用库存")
    sid: Optional[str] = Field(None, description="店铺id")
    product_code: Optional[str] = Field(None, description="三方产品编码")
    remark: Optional[str] = Field(None, description="商品备注")
    batch_record_list: Optional[list] = Field(None, description="采购信息")

class OwmsInboundListinboundLogistics(LingXingModel):
    """logistics sub-structure."""
    logistics_order_no: Optional[str] = Field(None, description="物流单号")
    logistics_money: Optional[str] = Field(None, description="预估物流费用")
    logistics_money_unit: Optional[str] = Field(None, description="预估物流费用币种")
    other_money: Optional[str] = Field(None, description="预估其他费用")
    other_money_unit: Optional[str] = Field(None, description="预估其他费用币种")
    track_order_no: Optional[str] = Field(None, description="追踪号")
    other_money_remark: Optional[str] = Field(None, description="预估费用备注")
    real_logistics_money: Optional[float] = Field(None, description="实际物流费用")
    real_logistics_money_unit: Optional[str] = Field(None, description="实际物流费用币种")
    real_other_money: Optional[float] = Field(None, description="实际其他费用")
    real_other_money_unit: Optional[str] = Field(None, description="实际其他费用币种")
    real_other_money_remark: Optional[str] = Field(None, description="实际其他费用备注")
    wool_id: Optional[str] = Field(None, description="物流记录id")

class OwmsInboundListinboundHeadLogisticsList(LingXingModel):
    """head_logistics_list sub-structure."""
    tracking_list: Optional[list] = Field(None, description="轨迹信息数组")
    estimate_expenses_list: Optional[dict] = Field(None, description="费用明细-预估费用")
    actual_expenses_list: Optional[dict] = Field(None, description="费用明细-实际费用")

class OwmsInboundListinboundResponse(LingXingModel):
    """查询海外仓备货单列表."""
    overseas_order_no: Optional[str] = Field(None, description="备货单号")
    inbound_order_no: Optional[str] = Field(None, description="三方入库单号")
    customer_reference_no: Optional[str] = Field(None, description="客户提交参考号")
    s_wid: Optional[int] = Field(None, description="发货仓id")
    s_wname: Optional[str] = Field(None, description="发货仓名称")
    r_wid: Optional[int] = Field(None, description="收货仓id")
    r_wname: Optional[str] = Field(None, description="收货仓名称")
    logistics_id: Optional[int] = Field(None, description="物流方式id")
    logistics_name: Optional[str] = Field(None, description="物流方式")
    remark: Optional[str] = Field(None, description="备注")
    status: Optional[int] = Field(None, description="状态： 10 待审核 20 已驳回 30 待配货 40 待发货 50 待收货 51 已撤销 60 已完成")
    rollback_remark: Optional[str] = Field(None, description="驳回备注")
    is_delete: Optional[int] = Field(None, description="是否已删除： 0 正常 1 已删除")
    transportation_mode: Optional[str] = Field(None, description="运输方式ID")
    transportation_name: Optional[str] = Field(None, description="运输方式名称")
    uid: Optional[int] = Field(None, description="创建用户id")
    create_user: Optional[str] = Field(None, description="创建人")
    update_user: Optional[str] = Field(None, description="最后更新人")
    create_time: Optional[str] = Field(None, description="创建时间")
    estimated_time: Optional[str] = Field(None, description="预计到货时间")
    audit_handle_time: Optional[dict] = Field(None, description="审核时间")
    send_good_handle_time: Optional[str] = Field(None, description="发货时间")
    receive_good_handle_time: Optional[str] = Field(None, description="收货时间")
    real_delivery_time: Optional[str] = Field(None, description="实际发货时间")
    update_time: Optional[str] = Field(None, description="最后更新时间")
    products: Optional[List[OwmsInboundListinboundProducts]] = Field(None, description="商品信息")
    logistics: Optional[List[OwmsInboundListinboundLogistics]] = Field(None, description="物流数据")
    logistics_list_type: Optional[int] = Field(None, description="物流信息版本：【默认0】 0 旧版 1 新版")
    head_logistics_list: Optional[List[OwmsInboundListinboundHeadLogisticsList]] = Field(None, description="新版头程物流信息 【对应 logistics_list_type = 1】 【注意：新版头程物流数据为覆盖式更新，包括tracking_list、estimate_expenses_list、actual_expenses_list，不传或者传空也会置空】")
    total: Optional[int] = Field(None, description="总数")


class OwmsInboundListordernosResponse(LingXingModel):
    """获取备货单号."""
    overseas_order_no: Optional[str] = Field(None, description="备货单号")
    inbound_order_no: Optional[str] = Field(None, description="客户参考号")
    create_time: Optional[str] = Field(None, description="创建时间")


class OwmsInboundMatchskulistResponse(LingXingModel):
    """查询系统产品与第三方海外仓产品映射列表."""
    warehouse_name: Optional[str] = Field(None, description="仓库名称")
    warehouse_code: Optional[str] = Field(None, description="仓库代码code")
    wid: Optional[int] = Field(None, description="仓库id")
    local_sku: Optional[str] = Field(None, description="本地sku编码")
    local_name: Optional[str] = Field(None, description="本地sku名称")
    match_num: Optional[int] = Field(None, description="配对数量，默认为1")
    oversea_product_name: Optional[str] = Field(None, description="三方产品名称")
    oversea_unique_code: Optional[str] = Field(None, description="三方产品唯一code，可能为空")
    oversea_product_code: Optional[str] = Field(None, description="三方sku编码")
    is_matched: Optional[bool] = Field(None, description="是否已配对： false 未配对 true 已配对")
    is_matched_text: Optional[str] = Field(None, description="对is_matched的文本展示")
    twp_id: Optional[int] = Field(None, description="三方产品id")
    sid: Optional[int] = Field(None, description="店铺id 库存中心过渡版本之后返回")
    total: Optional[int] = Field(None, description="是")


class OwmsInboundPackagelabelResponse(LingXingModel):
    """获取第三方箱唛."""
    file_type: Optional[str] = Field(None, description="标签数据类型，目前仅支持pdf")
    file_contents: Optional[list] = Field(None, description="base64字符串数组")


class OwmsRemovalinboundListAddress(LingXingModel):
    """address sub-structure."""
    sid: Optional[int] = Field(None, description="店铺id")
    order_id: Optional[int] = Field(None, description="移除入库单id")
    order_no: Optional[str] = Field(None, description="移除入库单号")
    address_line1: Optional[str] = Field(None, description="详细地址1")
    address_line2: Optional[str] = Field(None, description="详细地址2")
    address_line3: Optional[str] = Field(None, description="详细地址3")
    country_code: Optional[str] = Field(None, description="国家代码")
    state_or_province: Optional[str] = Field(None, description="省州")
    city: Optional[str] = Field(None, description="城市")
    county: Optional[str] = Field(None, description="县")
    district: Optional[str] = Field(None, description="区")
    postal_code: Optional[str] = Field(None, description="邮编")
    name: Optional[str] = Field(None, description="收件人名称")
    address_str: Optional[str] = Field(None, description="格式化地址")

class OwmsRemovalinboundListProduct(LingXingModel):
    """product sub-structure."""
    id: Optional[int] = Field(None, description="子项记录id")
    sid: Optional[int] = Field(None, description="店铺id")
    order_id: Optional[int] = Field(None, description="移除入库单id")
    order_no: Optional[str] = Field(None, description="移除入库单号")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sku: Optional[str] = Field(None, description="SKU")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="产品名称")
    pic_url: Optional[str] = Field(None, description="产品图片url")
    third_product_name: Optional[str] = Field(None, description="三方产品名称")
    third_code: Optional[str] = Field(None, description="三方产品编码")
    sellable_num: Optional[int] = Field(None, description="可售数量")
    unsellable_num: Optional[int] = Field(None, description="不可售数量")
    declare_num: Optional[int] = Field(None, description="申报量")
    avaliable_num: Optional[int] = Field(None, description="可用量")
    defective_num: Optional[int] = Field(None, description="次品量")
    recieve_num: Optional[int] = Field(None, description="收货数量")
    differences: Optional[int] = Field(None, description="待收货量")

class OwmsRemovalinboundListResponse(LingXingModel):
    """查询移除入库单列表."""
    total: Optional[int] = Field(None, description="总数")
    id: Optional[int] = Field(None, description="记录id")
    sid: Optional[int] = Field(None, description="店铺id")
    sid_name: Optional[str] = Field(None, description="店铺名称")
    order_no: Optional[str] = Field(None, description="移除入库单号")
    removal_order_no: Optional[str] = Field(None, description="移除订单号")
    wid: Optional[int] = Field(None, description="入库仓库id")
    wid_name: Optional[str] = Field(None, description="入库仓库名称")
    estimated_arrival_time: Optional[str] = Field(None, description="预计到货时间")
    shippment_time: Optional[str] = Field(None, description="发货时间")
    shipper: Optional[str] = Field(None, description="承运商")
    delivery_no: Optional[str] = Field(None, description="跟踪号")
    order_status: Optional[int] = Field(None, description="订单状态： 1 待提交-未提交 2 待提交-提交中 3 待提交-失败 4 待收货-未收货 5 待收货-异常 6 已完成 7 已作废")
    remark: Optional[str] = Field(None, description="备注")
    uid: Optional[int] = Field(None, description="提交人id")
    uid_name: Optional[str] = Field(None, description="提交人姓名【同submiter】")
    submiter: Optional[str] = Field(None, description="提交人姓名")
    submit: Optional[int] = Field(None, description="是否提交到三方海外仓：1 否，2 是")
    inbound_order_sns: Optional[list] = Field(None, description="关联入库单号")
    address: Optional[List[OwmsRemovalinboundListAddress]] = Field(None, description="仓库收货地址信息")
    product: Optional[List[OwmsRemovalinboundListProduct]] = Field(None, description="产品信息")


class StorageInboundGetcustomtypesList(LingXingModel):
    """list sub-structure."""
    id: Optional[int] = Field(None, description="类型ID")
    name: Optional[str] = Field(None, description="类型名称")
    is_delete: Optional[str] = Field(None, description="是否删除： 0 否 1 是")
    status: Optional[str] = Field(None, description="状态： 0 关闭 1 开启")

class StorageInboundGetcustomtypesResponse(LingXingModel):
    """获取自定义入库类型."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[StorageInboundGetcustomtypesList]] = Field(None, description="类型列表")
    total: Optional[int] = Field(None, description="行数")


class StorageInboundGetordersCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class StorageInboundGetordersItemList(LingXingModel):
    """item_list sub-structure."""
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="sku")
    fnsku: Optional[str] = Field(None, description="fnsku")
    seller_id: Optional[str] = Field(None, description="系统店铺id")
    purchase_item_id: Optional[int] = Field(None, description="采购单子项id")
    price: Optional[str] = Field(None, description="采购单价")
    amount: Optional[str] = Field(None, description="入库成本")
    fee_cost: Optional[str] = Field(None, description="费用")
    product_good_num: Optional[int] = Field(None, description="良品量")
    product_bad_num: Optional[int] = Field(None, description="次品量")
    product_qc_num: Optional[int] = Field(None, description="待检量")
    product_total: Optional[int] = Field(None, description="入库量")
    product_amounts: Optional[str] = Field(None, description="货值")
    single_fee: Optional[str] = Field(None, description="单位费用")
    single_stock_cost: Optional[str] = Field(None, description="单位入库成本")
    product_remark: Optional[str] = Field(None, description="产品备注")
    custom_fields: Optional[list] = Field(None, description="自定义字段")

class StorageInboundGetordersResponse(LingXingModel):
    """查询入库单列表."""
    total: Optional[int] = Field(None, description="总数")
    increment_time: Optional[str] = Field(None, description="单据数据更新时间")
    custom_fields: Optional[List[StorageInboundGetordersCustomFields]] = Field(None, description="自定义字段")
    opt_realname: Optional[str] = Field(None, description="入库人姓名")
    opt_time: Optional[str] = Field(None, description="入库时间")
    opt_uid: Optional[int] = Field(None, description="操作人id")
    inbound_time: Optional[str] = Field(None, description="自定义入库时间")
    commit_realname: Optional[str] = Field(None, description="提交人名称")
    commit_uid: Optional[int] = Field(None, description="提交人id")
    commit_time: Optional[str] = Field(None, description="提交时间")
    order_sn: Optional[str] = Field(None, description="入库单号")
    status: Optional[int] = Field(None, description="入库单状态")
    status_text: Optional[str] = Field(None, description="入库单状态名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人名称")
    purchase_order_sn: Optional[str] = Field(None, description="采购单号")
    receipt_order_sn: Optional[str] = Field(None, description="收货单号")
    revoke_realname: Optional[str] = Field(None, description="撤销人名称")
    revoke_uid: Optional[int] = Field(None, description="撤销人id")
    revoke_time: Optional[str] = Field(None, description="撤销时间")
    supplier_id: Optional[str] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    source_sn: Optional[str] = Field(None, description="关联单据号")
    order_amount: Optional[str] = Field(None, description="单据入库成本")
    cg_uid: Optional[int] = Field(None, description="采购员id")
    return_price: Optional[str] = Field(None, description="运费")
    currency: Optional[str] = Field(None, description="运费币种")
    other_fee: Optional[str] = Field(None, description="其他费用")
    fee_part_type: Optional[str] = Field(None, description="费用分摊方式")
    fee_part_type_text: Optional[str] = Field(None, description="费用分摊方式名称")
    type: Optional[int] = Field(None, description="入库类型")
    type_text: Optional[str] = Field(None, description="入库类型名称")
    custom_type_id: Optional[int] = Field(None, description="自定义类型ID")
    custom_type_name: Optional[str] = Field(None, description="自定义类型名称")
    cg_realname: Optional[str] = Field(None, description="采购员姓名")
    wid: Optional[str] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    remark: Optional[str] = Field(None, description="单据备注")
    inbound_idempotent_code: Optional[str] = Field(None, description="（入库单）客户参考号, 该字段校验唯一不可重复")
    item_list: Optional[List[StorageInboundGetordersItemList]] = Field(None, description="产品明细")


class StorageOutboundGetcustomtypesList(LingXingModel):
    """list sub-structure."""
    id: Optional[int] = Field(None, description="类型ID")
    name: Optional[str] = Field(None, description="类型名称")
    is_delete: Optional[str] = Field(None, description="是否删除： 0 否 1 是")
    status: Optional[str] = Field(None, description="状态： 0 关闭 1 开启")

class StorageOutboundGetcustomtypesResponse(LingXingModel):
    """获取自定义出库类型."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[StorageOutboundGetcustomtypesList]] = Field(None, description="类型列表")
    total: Optional[int] = Field(None, description="行数")


class StorageOutboundGetordersCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class StorageOutboundGetordersItemList(LingXingModel):
    """item_list sub-structure."""
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="sku")
    fnsku: Optional[str] = Field(None, description="fnsku")
    seller_id: Optional[str] = Field(None, description="系统店铺id")
    price: Optional[str] = Field(None, description="采购单价")
    amount: Optional[str] = Field(None, description="出库成本")
    fee_cost: Optional[str] = Field(None, description="费用")
    product_good_num: Optional[int] = Field(None, description="良品量")
    product_bad_num: Optional[int] = Field(None, description="次品量")
    product_qc_num: Optional[int] = Field(None, description="待检量")
    product_total: Optional[int] = Field(None, description="出库量")
    product_amounts: Optional[str] = Field(None, description="货值")
    single_fee: Optional[str] = Field(None, description="单位费用")
    single_stock_cost: Optional[str] = Field(None, description="单位出库成本")
    product_remark: Optional[str] = Field(None, description="产品备注")
    out_available_bin: Optional[str] = Field(None, description="可用仓位列表")
    out_inferior_bin: Optional[str] = Field(None, description="次品仓位列表")
    custom_fields: Optional[list] = Field(None, description="自定义字段")

class StorageOutboundGetordersResponse(LingXingModel):
    """查询出库单列表."""
    total: Optional[int] = Field(None, description="总数")
    increment_time: Optional[str] = Field(None, description="单据数据更新时间")
    custom_fields: Optional[List[StorageOutboundGetordersCustomFields]] = Field(None, description="自定义字段")
    opt_realname: Optional[str] = Field(None, description="出库人姓名")
    opt_time: Optional[str] = Field(None, description="出库时间")
    opt_uid: Optional[int] = Field(None, description="操作人id")
    outbound_time: Optional[str] = Field(None, description="自定义出库时间")
    commit_realname: Optional[str] = Field(None, description="提交人名称")
    commit_uid: Optional[int] = Field(None, description="提交人id")
    commit_time: Optional[str] = Field(None, description="提交时间")
    order_sn: Optional[str] = Field(None, description="出库单号")
    status: Optional[int] = Field(None, description="出库单状态")
    status_text: Optional[str] = Field(None, description="出库单状态名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人名称")
    purchase_order_sn: Optional[str] = Field(None, description="采购单号")
    revoke_realname: Optional[str] = Field(None, description="撤销人名称")
    revoke_uid: Optional[int] = Field(None, description="撤销人id")
    revoke_time: Optional[str] = Field(None, description="撤销时间")
    supplier_id: Optional[str] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    source_sn: Optional[str] = Field(None, description="关联单据号")
    order_amount: Optional[str] = Field(None, description="单据入库成本")
    cg_uid: Optional[int] = Field(None, description="采购员id")
    return_price: Optional[str] = Field(None, description="运费")
    currency: Optional[str] = Field(None, description="运费币种")
    other_fee: Optional[str] = Field(None, description="其他费用")
    fee_part_type: Optional[str] = Field(None, description="费用分摊方式")
    fee_part_type_text: Optional[str] = Field(None, description="费用分摊方式名称")
    type: Optional[int] = Field(None, description="出库类型")
    type_text: Optional[str] = Field(None, description="出库类型名称")
    custom_type_id: Optional[int] = Field(None, description="自定义类型ID")
    custom_type_name: Optional[str] = Field(None, description="自定义类型名称")
    cg_realname: Optional[str] = Field(None, description="采购员姓名")
    wid: Optional[str] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    to_wid: Optional[str] = Field(None, description="目的仓库id")
    to_ware_house_name: Optional[str] = Field(None, description="目的仓库名称")
    remark: Optional[str] = Field(None, description="单据备注")
    idempotent_code: Optional[str] = Field(None, description="客户参考号, 该字段校验唯一不可重复")
    item_list: Optional[List[StorageOutboundGetordersItemList]] = Field(None, description="是")


class StorageStorageOrderaddResponse(LingXingModel):
    """添加入库单."""
    order_sn_arr: Optional[list] = Field(None, description="入库单号数组【兼容多个单号情况】")
    order_sn: Optional[str] = Field(None, description="入库单号【多个单号情况下值为order_sn_arr里的第一个】")


class StorageStorageOrderaddoutResponse(LingXingModel):
    """添加出库单."""
    order_sn: Optional[str] = Field(None, description="出库单号")


class StorageWarehousebinSwitchstatusResponse(LingXingModel):
    """启用、禁用仓位."""
    success_msg: Optional[str] = Field(None, description="成功信息")


class WmsOrderGetwmslogisticslabelsResponse(LingXingModel):
    """查询销售出库单物流面单."""
    wo_number: Optional[str] = Field(None, description="销售出库单号")
    order_number: Optional[str] = Field(None, description="系统单号")
    logistics_provider_id: Optional[float] = Field(None, description="物流服务商id")
    logistics_type_id: Optional[float] = Field(None, description="物流方式id")
    file_id: Optional[float] = Field(None, description="文件id")
    file_type: Optional[str] = Field(None, description="文件类型")
    file_size: Optional[str] = Field(None, description="文件尺寸")
    file_b64: Optional[str] = Field(None, description="面单base64")


class WmsOrderWmsorderlistSurfaceFile(LingXingModel):
    """surface_file sub-structure."""
    uri: Optional[str] = Field(None, description="链接")
    ext: Optional[str] = Field(None, description="文件后缀")
    size: Optional[str] = Field(None, description="文件尺寸")

class WmsOrderWmsorderlistProductInfo(LingXingModel):
    """product_info sub-structure."""
    wod_id: Optional[int] = Field(None, description="出库单明细id")
    product_id: Optional[int] = Field(None, description="商品id")
    sku: Optional[str] = Field(None, description="SKU")
    count: Optional[int] = Field(None, description="数量")
    bundle_type: Optional[int] = Field(None, description="捆绑类型： 0 普通商品 - 含组合产品、子产品 1 捆绑产品 2 捆绑产品拆分子产品")
    bundle_wod_id: Optional[int] = Field(None, description="捆绑产品wod_id【只有拆分子产品才有】")
    product_name: Optional[str] = Field(None, description="商品名")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    customization: Optional[str] = Field(None, description="商品备注")
    cn_name: Optional[str] = Field(None, description="中文申报名")
    en_name: Optional[str] = Field(None, description="英文申报名")
    third_product_name: Optional[str] = Field(None, description="三方仓品名")
    third_product_code: Optional[str] = Field(None, description="三方仓SKU")
    unit_price: Optional[str] = Field(None, description="商品单价")
    currency_code: Optional[str] = Field(None, description="币种")
    apportion_freight: Optional[str] = Field(None, description="分摊运费 (总计)")
    apportion_freight_single: Optional[str] = Field(None, description="分摊运费 (单个)")
    logistics_freight_currency_code: Optional[str] = Field(None, description="物流运费币种")
    stock_cost: Optional[str] = Field(None, description="库存成本 (总计)")
    stock_sid: Optional[str] = Field(None, description="库存颗粒度店铺id")
    stock_seller_name: Optional[str] = Field(None, description="库存颗粒度店铺名称")
    item_unit_price: Optional[str] = Field(None, description="销售单价")
    item_total_price: Optional[str] = Field(None, description="销售总价")
    real_weight_total: Optional[str] = Field(None, description="费用分摊-总实重")
    fee_weight_total: Optional[str] = Field(None, description="费用分摊-总计费重")
    volume_weight_total: Optional[str] = Field(None, description="费用分摊-总体集中")
    declared_currency_icon: Optional[str] = Field(None, description="申报比重图标")

class WmsOrderWmsorderlistResponse(LingXingModel):
    """查询销售出库单列表."""
    total: Optional[int] = Field(None, description="总数")
    wo_id: Optional[int] = Field(None, description="出库单id")
    wo_number: Optional[str] = Field(None, description="销售出库单号")
    sid: Optional[int] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    site_text: Optional[str] = Field(None, description="站点名称")
    wid: Optional[int] = Field(None, description="仓库id")
    warehouse_name: Optional[str] = Field(None, description="仓库名")
    warehouse_type: Optional[int] = Field(None, description="仓库类型： 1 本地仓库 2 FBA仓 3 第三方海外仓")
    logistics_way: Optional[int] = Field(None, description="下单流程 1:物流 2:海外仓 3:仓配分离")
    batch_no: Optional[str] = Field(None, description="批次号")
    reference_no: Optional[str] = Field(None, description="参考号")
    waybill_no: Optional[str] = Field(None, description="运单号")
    tracking_no: Optional[str] = Field(None, description="跟踪号")
    picker: Optional[str] = Field(None, description="拣货人")
    platform_name: Optional[str] = Field(None, description="平台名称")
    platform_order_no: Optional[list] = Field(None, description="平台单号")
    order_number: Optional[str] = Field(None, description="系统单号")
    order_from: Optional[str] = Field(None, description="订单来源")
    order_type: Optional[int] = Field(None, description="订单类型： 1 一单一件 2 多品多件【原一单多件】 3 单品多件")
    order_origin_amount: Optional[str] = Field(None, description="订单金额")
    order_currency_code: Optional[str] = Field(None, description="订单币种")
    order_customer_service_notes: Optional[str] = Field(None, description="客服备注")
    order_buyer_notes: Optional[str] = Field(None, description="买家留言")
    status: Optional[int] = Field(None, description="状态： 1 物流下单 2 待出库 3 已出库 4 已截单")
    status_name: Optional[str] = Field(None, description="状态名称")
    logistics_status: Optional[int] = Field(None, description="物流下单状态： 1 待导入 2 物流待下单 3 物流下单中 4 下单异常 5 下单完成 6 待海外仓下单 7 海外仓下单中 11 待导入国内物流 41 物流取消中 42 物流取消异常 43 物流取消完成")
    logistics_status_name: Optional[str] = Field(None, description="物流下单状态名称")
    logistics_message: Optional[str] = Field(None, description="物流下单消息")
    cancel_status: Optional[int] = Field(None, description="第三方仓取消状态：0无需处理、1取消中、2取消异常、3取消成功")
    cancel_message: Optional[str] = Field(None, description="第三方仓取消返回消息")
    delivery_status: Optional[int] = Field(None, description="第三方仓发货状态：20待发货、21发货中、22发货异常、23发货成功")
    delivery_message: Optional[str] = Field(None, description="第三方仓发货异常消息")
    logistics_provider_id: Optional[int] = Field(None, description="物流服务商id")
    logistics_provider_name: Optional[str] = Field(None, description="物流服务商名称")
    logistics_type_id: Optional[int] = Field(None, description="物流方式id")
    logistics_type_name: Optional[str] = Field(None, description="物流方式名称")
    logistics_freight: Optional[str] = Field(None, description="物流运费")
    logistics_freight_currency_code: Optional[str] = Field(None, description="物流运费币种")
    logistics_estimated_freight: Optional[str] = Field(None, description="预估运费")
    logistics_estimated_freight_currency_code: Optional[str] = Field(None, description="预估运费币种")
    is_check: Optional[int] = Field(None, description="是否验货：0 否，1 是")
    is_weigh: Optional[int] = Field(None, description="是否称重：0 否，1 是")
    is_surface_print: Optional[int] = Field(None, description="面单是否打印：0 否，1 是")
    is_order_print: Optional[int] = Field(None, description="订单是否打印：0 否，1 是")
    process_sn: Optional[str] = Field(None, description="加工单号")
    target_country: Optional[str] = Field(None, description="收货国家")
    tag_names: Optional[list] = Field(None, description="标签")
    pkg_volume: Optional[str] = Field(None, description="包裹体积")
    pkg_length: Optional[str] = Field(None, description="包裹尺寸长")
    pkg_width: Optional[str] = Field(None, description="包裹尺寸宽")
    pkg_height: Optional[str] = Field(None, description="包裹尺寸高")
    pkg_weight: Optional[str] = Field(None, description="估算重量")
    pkg_real_weight: Optional[str] = Field(None, description="包裹实重")
    pkg_fee_weight: Optional[str] = Field(None, description="包裹计费重")
    pkg_weight_unit: Optional[str] = Field(None, description="预估重量单位")
    pkg_real_weight_unit: Optional[str] = Field(None, description="包裹实重单位")
    pkg_fee_weight_unit: Optional[str] = Field(None, description="包裹计费重单位")
    pkg_size_unit: Optional[str] = Field(None, description="包裹尺寸单位")
    recipient_tax_no: Optional[str] = Field(None, description="收件人税号")
    sender_tax_no: Optional[str] = Field(None, description="发件人税号")
    deliverer: Optional[str] = Field(None, description="发货人")
    deliver_deadline: Optional[str] = Field(None, description="发货时限")
    delivered_at: Optional[str] = Field(None, description="出库时间")
    stock_delivered_at: Optional[str] = Field(None, description="库存流水出库时间")
    create_at: Optional[str] = Field(None, description="创建时间")
    update_at: Optional[str] = Field(None, description="变更时间")
    purchase_time: Optional[str] = Field(None, description="下单时间")
    payment_time: Optional[str] = Field(None, description="付款时间")
    surface_print_time: Optional[str] = Field(None, description="面单打印时间")
    order_print_time: Optional[str] = Field(None, description="订单打印时间")
    platform_payment_time: Optional[str] = Field(None, description="平台结算时间")
    package_no: Optional[str] = Field(None, description="小包号(用于组包)")
    package_delivered_data: Optional[list] = Field(None, description="包裹出库信息")
    transfer_logistics_company_code: Optional[str] = Field(None, description="国内中转物流公司代码")
    transfer_logistics_company_id: Optional[str] = Field(None, description="国内中转物流公司id")
    transfer_tracking_no: Optional[str] = Field(None, description="国内中转跟踪号")
    is_lock_storage: Optional[int] = Field(None, description="是否已锁定库存：0 否，1 是")
    is_advance_delivery: Optional[int] = Field(None, description="是否预发货：0 否，1 是")
    apportion_status: Optional[int] = Field(None, description="费用分摊状态： 1 未分摊 2 分摊失败 3 分摊成功")
    apportion_message: Optional[str] = Field(None, description="费用分摊消息")
    remark_attachment: Optional[str] = Field(None, description="客服备注附件json")
    consignee: Optional[str] = Field(None, description="收件人")
    consignee_phone: Optional[str] = Field(None, description="收件人电话")
    consignee_postcode: Optional[str] = Field(None, description="收件人邮编")
    consignee_address: Optional[str] = Field(None, description="收件人地址")
    consignee_full_address: Optional[str] = Field(None, description="收件地址")
    surface_file_type: Optional[str] = Field(None, description="面单文件类型")
    surface_file: Optional[List[WmsOrderWmsorderlistSurfaceFile]] = Field(None, description="面单文件")
    product_info: Optional[List[WmsOrderWmsorderlistProductInfo]] = Field(None, description="商品信息")


class ReturnsV2ListList(LingXingModel):
    """list sub-structure."""
    complete_time: Optional[str] = Field(None, description="完成时间")
    global_order_no: Optional[int] = Field(None, description="系统单号")
    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    has_prediction: Optional[int] = Field(None, description="是否三方仓预报 0 否 1 是")
    logistics_provider_name: Optional[str] = Field(None, description="物流商")
    platform: Optional[str] = Field(None, description="平台")
    pre_arrival_time: Optional[str] = Field(None, description="预计到货时间")
    reason: Optional[str] = Field(None, description="退货原因")
    remark: Optional[str] = Field(None, description="备注")
    rma_order_no: Optional[str] = Field(None, description="退货单号")
    sales_type: Optional[str] = Field(None, description="退货类型")
    site: Optional[str] = Field(None, description="站点")
    status: Optional[str] = Field(None, description="订单状态")
    store_id: Optional[int] = Field(None, description="多平台店铺id")
    sid: Optional[int] = Field(None, description="亚马逊店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    tracking_no: Optional[str] = Field(None, description="跟踪号")
    uid_name: Optional[str] = Field(None, description="创建人名称")
    sys_wid: Optional[int] = Field(None, description="退货仓库id")
    w_name: Optional[str] = Field(None, description="退货仓库名称")
    relation_order_info: Optional[dict] = Field(None, description="关联单据")
    items: Optional[list] = Field(None, description="商品信息")

class ReturnsV2ListResponse(LingXingModel):
    """查询销售退货单列表."""
    total: Optional[int] = Field(None, description="总条数")
    list: Optional[List[ReturnsV2ListList]] = Field(None, description="详细列表")


# Migrated from old models/
class GetBatchDetailListItem(LingXingModel):
    """Response item for GetBatchDetailList."""

    amount: Optional[float] = None
    bad_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    balance_num: Optional[int] = None
    batch_no: Optional[str] = None
    batch_time: Optional[str] = None
    delivery_order_sns: Optional[list] = None
    fee: Optional[float] = None
    fnsku: Optional[str] = None
    good_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[float] = None
    inventory_age: Optional[int] = None
    msku: Optional[str] = None
    order_sn: Optional[str] = None
    plan_sn: Optional[list] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    purchase_in_time: Optional[str] = None
    purchase_order_sns: Optional[list] = None
    qc_num: Optional[int] = None
    sku: Optional[str] = None
    source_batch_no: Optional[list] = None
    stock_cost: Optional[float] = None
    store_id: Optional[int] = None
    store_name: Optional[str] = None
    supplier_ids: Optional[list] = None
    supplier_names: Optional[list] = None
    total: Optional[int] = None
    transit_balance_num: Optional[int] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    update_time: Optional[str] = None
    wh_name: Optional[str] = None
    wid: Optional[int] = None


class GetBatchStatementListItem(LingXingModel):
    """Response item for GetBatchStatementList."""

    amount: Optional[float] = None
    bad_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    balance_num: Optional[int] = None
    batch_no: Optional[str] = None
    batch_state_id: Optional[str] = None
    delivery_order_sns: Optional[list] = None
    fee: Optional[float] = None
    fnsku: Optional[str] = None
    good_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[float] = None
    msku: Optional[str] = None
    order_sn: Optional[str] = None
    plan_sn: Optional[list] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    purchase_order_sns: Optional[list] = None
    qc_num: Optional[int] = None
    sku: Optional[str] = None
    source_batch_no: Optional[list] = None
    source_order_sn: Optional[list] = None
    stock_cost: Optional[float] = None
    store_id: Optional[int] = None
    store_name: Optional[str] = None
    supplier_ids: Optional[list] = None
    supplier_names: Optional[list] = None
    transit_balance_num: Optional[int] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    wh_name: Optional[str] = None
    wid: Optional[int] = None


class InventoryDetailsItem(LingXingModel):
    """Response item for InventoryDetails."""

    available_inventory_box_qty: Optional[int] = None
    average_age: Optional[int] = None
    bad_lock_num: Optional[int] = None
    fnsku: Optional[str] = None
    good_lock_num: Optional[int] = None
    head_stock_price: Optional[float] = None
    price: Optional[float] = None
    product_bad_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_num: Optional[int] = None
    product_onway: Optional[int] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    product_valid_num: Optional[int] = None
    purchase_price: Optional[float] = None
    quantity_receive: Optional[int] = None
    seller_id: Optional[int] = None
    sku: Optional[str] = None
    stock_age_list: Optional[list] = None
    stock_cost: Optional[float] = None
    stock_cost_total: Optional[float] = None
    stock_price: Optional[float] = None
    third_inventory: Optional[dict] = None
    transit_head_cost: Optional[float] = None
    wid: Optional[int] = None


class PurchaseReceiptOrderListItem(LingXingModel):
    """Response item for PurchaseReceiptOrderList."""

    business_order_sn: Optional[str] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    expect_arrival_time: Optional[str] = None
    inbound_order_sns: Optional[list] = None
    item_list: Optional[list] = None
    logistics_company: Optional[str] = None
    logistics_order_no: Optional[str] = None
    opt_realname: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    order_type: Optional[int] = None
    other_currency: Optional[str] = None
    other_fee: Optional[float] = None
    qc_type: Optional[int] = None
    receive_realname: Optional[str] = None
    receive_time: Optional[str] = None
    receive_uid: Optional[int] = None
    remark: Optional[str] = None
    shipping_cost: Optional[float] = None
    shipping_currency: Optional[str] = None
    status: Optional[int] = None
    supplier_id: Optional[int] = None
    update_time: Optional[str] = None
    wid: Optional[int] = None


class WarehouseListsItem(LingXingModel):
    """Response item for WarehouseLists."""

    country_code: Optional[str] = None
    is_delete: Optional[int] = None
    name: Optional[str] = None
    sub_type: Optional[int] = None
    t_country_area_name: Optional[str] = None
    t_status: Optional[str] = None
    t_warehouse_code: Optional[str] = None
    t_warehouse_name: Optional[str] = None
    type: Optional[int] = None
    wid: Optional[int] = None
    wp_id: Optional[int] = None
    wp_name: Optional[str] = None


class WarehouseStatementItem(LingXingModel):
    """Response item for WarehouseStatement."""

    amount: Optional[float] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    cancel_time: Optional[str] = None
    fee_cost: Optional[float] = None
    fnsku: Optional[str] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    price: Optional[float] = None
    product_amounts: Optional[float] = None
    product_bad_num: Optional[int] = None
    product_good_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_num: Optional[int] = None
    product_name: Optional[str] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    ref_order_sn: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[int] = None
    single_cg_price: Optional[float] = None
    single_fee_cost: Optional[float] = None
    sku: Optional[str] = None
    statement_id: Optional[int] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class WarehouseStatementNewItem(LingXingModel):
    """Response item for WarehouseStatementNew."""

    bad_balance_num: Optional[int] = None
    bad_lock_balance_num: Optional[int] = None
    bad_transit_balance_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    fee_cost: Optional[float] = None
    fnsku: Optional[str] = None
    good_balance_num: Optional[int] = None
    good_lock_balance_num: Optional[int] = None
    good_transit_balance_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[float] = None
    head_stock_price: Optional[float] = None
    opt_real_name: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    product_amounts: Optional[float] = None
    product_bad_num: Optional[int] = None
    product_good_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_bad_num: Optional[int] = None
    product_lock_good_num: Optional[int] = None
    product_name: Optional[str] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    qc_balance_num: Optional[int] = None
    ref_order_sn: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[int] = None
    single_cg_price: Optional[float] = None
    single_fee_cost: Optional[float] = None
    single_stock_price: Optional[float] = None
    sku: Optional[str] = None
    statement_id: Optional[int] = None
    stock_cost: Optional[float] = None
    sub_type: Optional[int] = None
    sub_type_text: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class WmsOrderListItem(LingXingModel):
    """Response item for WmsOrderList."""

    actual_carrier: Optional[str] = None
    apportion_message: Optional[str] = None
    apportion_status: Optional[int] = None
    auto_allocate_status: Optional[int] = None
    auto_complete: Optional[int] = None
    batch_no: Optional[str] = None
    cancel_message: Optional[str] = None
    cancel_status: Optional[int] = None
    consignee: Optional[str] = None
    consignee_address: Optional[str] = None
    consignee_full_address: Optional[str] = None
    consignee_phone: Optional[str] = None
    consignee_postcode: Optional[str] = None
    create_at: Optional[str] = None
    deliver_deadline: Optional[str] = None
    delivered_at: Optional[str] = None
    deliverer: Optional[str] = None
    delivery_message: Optional[str] = None
    delivery_status: Optional[int] = None
    district: Optional[str] = None
    documents_file_id: Optional[int] = None
    email: Optional[str] = None
    first_mile_status: Optional[int] = None
    gross_profit_amount: Optional[str] = None
    gross_profit_rate: Optional[str] = None
    invoice_status: Optional[int] = None
    is_advance_delivery: Optional[int] = None
    is_check: Optional[int] = None
    is_lock_storage: Optional[int] = None
    is_order_print: Optional[int] = None
    is_surface_print: Optional[int] = None
    is_weigh: Optional[int] = None
    logistics_estimated_freight: Optional[float] = None
    logistics_estimated_freight_currency_code: Optional[str] = None
    logistics_freight: Optional[float] = None
    logistics_freight_currency_code: Optional[str] = None
    logistics_message: Optional[str] = None
    logistics_provider_id: Optional[int] = None
    logistics_provider_name: Optional[str] = None
    logistics_status: Optional[int] = None
    logistics_status_name: Optional[str] = None
    logistics_success_time: Optional[str] = None
    logistics_type_id: Optional[int] = None
    logistics_type_name: Optional[str] = None
    logistics_way: Optional[int] = None
    mark_label_file_id: Optional[int] = None
    mark_label_status: Optional[int] = None
    need_invoice: Optional[int] = None
    noShippingProductList: Optional[list] = None
    omsAttachments: Optional[dict] = None
    order_buyer_notes: Optional[str] = None
    order_currency_code: Optional[str] = None
    order_customer_service_notes: Optional[str] = None
    order_from: Optional[str] = None
    order_number: Optional[int] = None
    order_origin_amount: Optional[float] = None
    order_print_time: Optional[str] = None
    order_sns: Optional[list] = None
    order_tags: Optional[list] = None
    order_type: Optional[int] = None
    owms_waybill_no: Optional[str] = None
    package_delivered_data: Optional[list] = None
    package_no: Optional[str] = None
    payment_time: Optional[str] = None
    pick_index: Optional[int] = None
    picker: Optional[str] = None
    pkg_fee_weight: Optional[float] = None
    pkg_fee_weight_unit: Optional[str] = None
    pkg_height: Optional[float] = None
    pkg_length: Optional[float] = None
    pkg_real_weight: Optional[float] = None
    pkg_real_weight_unit: Optional[str] = None
    pkg_size_unit: Optional[str] = None
    pkg_volume: Optional[float] = None
    pkg_weight: Optional[float] = None
    pkg_weight_unit: Optional[str] = None
    pkg_width: Optional[float] = None
    platform_name: Optional[str] = None
    platform_order_no: Optional[list] = None
    platform_payment_time: Optional[str] = None
    process_sn: Optional[str] = None
    product_info: Optional[list] = None
    purchase_time: Optional[str] = None
    recipient_tax_no: Optional[str] = None
    reference_no: Optional[str] = None
    remark_attachment: Optional[str] = None
    report_message: Optional[str] = None
    report_status: Optional[int] = None
    seller_name: Optional[str] = None
    sender_tax_no: Optional[str] = None
    sid: Optional[int] = None
    site_text: Optional[str] = None
    split_num: Optional[int] = None
    status: Optional[int] = None
    status_name: Optional[str] = None
    stock_delivered_at: Optional[str] = None
    surface_file: Optional[dict] = None
    surface_file_id: Optional[int] = None
    surface_file_type: Optional[str] = None
    surface_print_time: Optional[str] = None
    tag_names: Optional[list] = None
    target_country: Optional[str] = None
    track_record: Optional[str] = None
    tracking_no: Optional[str] = None
    transfer_logistics_company_code: Optional[str] = None
    transfer_logistics_company_id: Optional[str] = None
    transfer_tracking_no: Optional[str] = None
    update_at: Optional[str] = None
    warehouse_name: Optional[str] = None
    warehouse_type: Optional[int] = None
    waybill_no: Optional[str] = None
    wid: Optional[int] = None
    wo_id: Optional[int] = None
    wo_number: Optional[str] = None


class GetProcessOrderListsItem(LingXingModel):
    """Response item for getProcessOrderLists."""

    create_by: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    finish_realname: Optional[str] = None
    finish_time: Optional[str] = None
    finish_uid: Optional[int] = None
    process_sn: Optional[str] = None
    product_list: Optional[list] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    type: Optional[int] = None
    update_time: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class GetStorageAdjustOrderListItem(LingXingModel):
    """Response item for getStorageAdjustOrderList."""

    adjustment_realname: Optional[str] = None
    adjustment_time: Optional[str] = None
    adjustment_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    company_id: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class InboundGetCustomTypesItem(LingXingModel):
    """Response item for inboundGetCustomTypes."""

    list: Optional[list] = None
    total: Optional[int] = None


class InboundgetOrdersItem(LingXingModel):
    """Response item for inboundgetOrders."""

    cg_realname: Optional[str] = None
    cg_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    currency: Optional[str] = None
    custom_fields: Optional[list] = None
    custom_type_id: Optional[int] = None
    custom_type_name: Optional[str] = None
    fee_part_type: Optional[int] = None
    fee_part_type_text: Optional[str] = None
    inbound_idempotent_code: Optional[str] = None
    inbound_time: Optional[str] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_amount: Optional[float] = None
    order_sn: Optional[str] = None
    origin_purchase_rate: Optional[float] = None
    origin_shipping_currency: Optional[str] = None
    origin_shipping_fee: Optional[float] = None
    other_fee: Optional[float] = None
    purchase_order_sn: Optional[str] = None
    receipt_order_sn: Optional[str] = None
    remark: Optional[str] = None
    return_price: Optional[float] = None
    revoke_realname: Optional[str] = None
    revoke_time: Optional[str] = None
    revoke_uid: Optional[int] = None
    source_sn: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class InventoryBinDetailsItem(LingXingModel):
    """Response item for inventoryBinDetails."""

    fnsku: Optional[str] = None
    lockNum: Optional[int] = None
    msku: Optional[str] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    sku: Optional[str] = None
    store_id: Optional[int] = None
    third_inventory: Optional[dict] = None
    total: Optional[int] = None
    validNum: Optional[int] = None
    wh_name: Optional[str] = None
    whb_id: Optional[int] = None
    whb_name: Optional[str] = None
    whb_type: Optional[int] = None
    whb_type_name: Optional[str] = None
    wid: Optional[int] = None


class OutboundGetCustomTypesItem(LingXingModel):
    """Response item for outboundGetCustomTypes."""

    list: Optional[list] = None
    total: Optional[int] = None


class OutboundgetOrdersItem(LingXingModel):
    """Response item for outboundgetOrders."""

    cg_realname: Optional[str] = None
    cg_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    currency: Optional[str] = None
    custom_fields: Optional[list] = None
    custom_type_id: Optional[int] = None
    custom_type_name: Optional[str] = None
    fee_part_type: Optional[int] = None
    fee_part_type_text: Optional[str] = None
    idempotent_code: Optional[str] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_amount: Optional[float] = None
    order_sn: Optional[str] = None
    other_fee: Optional[float] = None
    outbound_time: Optional[str] = None
    purchase_order_sn: Optional[str] = None
    remark: Optional[str] = None
    return_price: Optional[float] = None
    revoke_realname: Optional[str] = None
    revoke_time: Optional[str] = None
    revoke_uid: Optional[int] = None
    source_sn: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    to_ware_house_name: Optional[str] = None
    to_wid: Optional[int] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class RemovalInboundListItem(LingXingModel):
    """Response item for removalInboundList."""

    address: Optional[dict] = None
    delivery_no: Optional[str] = None
    estimated_arrival_time: Optional[str] = None
    id: Optional[int] = None
    inbound_order_sns: Optional[list] = None
    order_no: Optional[str] = None
    order_status: Optional[int] = None
    product: Optional[list] = None
    remark: Optional[str] = None
    removal_order_no: Optional[str] = None
    shipper: Optional[str] = None
    shippment_time: Optional[str] = None
    sid: Optional[int] = None
    sid_name: Optional[str] = None
    submit: Optional[int] = None
    submiter: Optional[str] = None
    uid: Optional[int] = None
    uid_name: Optional[str] = None
    wid: Optional[int] = None
    wid_name: Optional[str] = None


class WareHouseBinStatementItem(LingXingModel):
    """Response item for wareHouseBinStatement."""

    fnsku: Optional[str] = None
    num: Optional[int] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[int] = None
    sku: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    whb_id: Optional[int] = None
    whb_name: Optional[str] = None
    whb_type_name: Optional[str] = None
    wid: Optional[int] = None


class AwdInboundPlanConfirmResponse(LingXingModel):
    """确认AWD入库任务 (/amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan)."""
    msg: Optional[str] = None


class AwdInboundPlanCreateResponse(LingXingModel):
    """创建AWD入库任务 (/amzStaServer/openapi/awd/inbound-plan/createInboundPlan)."""
    msg: Optional[str] = None


class AwdInboundPlanUpdateResponse(LingXingModel):
    """更新AWD入库任务 (/amzStaServer/openapi/awd/inbound-plan/updateInboundPlan)."""
    msg: Optional[str] = None


class AwdInboundShipmentUpdateTrackResponse(LingXingModel):
    """更新AWD货件跟踪编号 (/amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo)."""
    msg: Optional[str] = None


class AwdInboundShipmentPrintLabelResponse(LingXingModel):
    """打印AWD入库货件箱子标签 (/amzStaServer/openapi/awd/inbound-shipment/uploadPacking)."""
    msg: Optional[str] = None


class PackingTaskAddResponse(LingXingModel):
    """装箱任务-生成装箱任务 (/basicOpen/packingTask/addTask)."""
    msg: Optional[str] = None


class PackingTaskBatchEditResponse(LingXingModel):
    """装箱任务-批量编辑装箱信息 (/basicOpen/packingTask/batchEditPackingBox)."""
    msg: Optional[str] = None


class PackingTaskDelResponse(LingXingModel):
    """装箱任务-删除装箱任务 (/basicOpen/packingTask/delTask)."""
    msg: Optional[str] = None


class PackingTaskDetailResponse(LingXingModel):
    """装箱任务-任务详情 (/basicOpen/packingTask/taskDetail)."""
    msg: Optional[str] = None


class PackingTaskFinishResponse(LingXingModel):
    """装箱任务-标记已完成 (/basicOpen/packingTask/finishTask)."""
    msg: Optional[str] = None


class PackingTaskListResponse(LingXingModel):
    """装箱任务-单据列表 (/basicOpen/packingTask/getRelateSnList)."""
    msg: Optional[str] = None


class ProcessPlanListResponse(LingXingModel):
    """查询加工计划列表 (/basicOpen/openapi/workOrder/processPlanList)."""
    msg: Optional[str] = None


class ProcessOrderAddResponse(LingXingModel):
    """创建加工单/拆分单 (/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder)."""
    msg: Optional[str] = None


class ProcessOrderListResponse(LingXingModel):
    """加工单列表 (/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists)."""
    msg: Optional[str] = None


class OverseaProductUnmatchResponse(LingXingModel):
    """海外仓sku取消配对 (/basicOpen/overseaWarehouseSetting/productMatch)."""
    msg: Optional[str] = None


class WarehouseBinEntryRecommendResponse(LingXingModel):
    """查询产品仓位列表 (/basicOpen/warehouseConfig/warehouseBin/getEntryRecommendBinList)."""
    msg: Optional[str] = None


class OverseaStockOrderDetailResponse(LingXingModel):
    """查询海外仓备货单详情 (/basicOpen/overSeaWarehouse/stockOrder/detail)."""
    msg: Optional[str] = None


class PurchaseReceiptOrderCreateResponse(LingXingModel):
    """创建待收货的收货单 (/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder)."""
    msg: Optional[str] = None


class SalesReturnV2ListResponse(LingXingModel):
    """查询销售退货单列表 (/pb/mp/returns/v2/list)."""
    msg: Optional[str] = None


class ReceiptOrderQcListResponse(LingXingModel):
    """查询质检单列表 (/erp/sc/routing/deliveryReceipt/ReceiptOrderQc/getOrderList)."""
    msg: Optional[str] = None


class ReturnOrderFastStorageInResponse(LingXingModel):
    """待收货退货单快捷入库 (/basicOpen/return/order/fastStorageIn)."""
    msg: Optional[str] = None


class AllocationPartlyReceiveResponse(LingXingModel):
    """调拨单分批收货 (/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder)."""
    msg: Optional[str] = None


class AllocationFinishReceiveResponse(LingXingModel):
    """调拨单结束到货 (/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder)."""
    msg: Optional[str] = None


class CostChangeFinishResponse(LingXingModel):
    """创建已完成的成本补录单 (/erp/sc/routing/inventoryReceipt/CostChangeOrder/finishCostChangeOrder)."""
    msg: Optional[str] = None


class WmsOrderSetPackageSizeResponse(LingXingModel):
    """设置包裹尺寸 (/erp/sc/routing/wms/order/setOrderPackageSize)."""
    msg: Optional[str] = None

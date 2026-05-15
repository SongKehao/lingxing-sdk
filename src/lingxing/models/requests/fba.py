"""Request models for FBA APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class FBAShipmentPlanListsRequest(LingXingModel):
    """Request for 查询FBA发货计划.
    
    POST /erp/sc/data/fba_report/shipmentPlanLists
    """
    sids: Optional[str] = None  # 店铺ids，12,13组成，对应查询亚马逊店铺列表接口对应字段【sid】
    wid: Optional[str] = None  # 仓库id
    packing_type: Optional[str] = None  # 包装类型2原装 1混装
    search_field_time: Optional[str] = None  # 查找时间字段(gmt_create-创建时间,estimated_delivery_time-计划发货时间)，不传该字段默认为gmt_create
    search_field: Optional[str] = None  # 查找字段  order_sn发货计划单号
    search_value: Optional[str] = None  # 查找值
    status: Optional[str] = None  # 状态
    mids: Optional[str] = None  # 国家id
    offset: Optional[int] = None  # 偏移量 0 偏移量 (currentPage -1) * length
    length: Optional[int] = None  # 长度 默认20
    start_date: Optional[str] = None  # 开始日期 如:2021-09-07
    end_date: Optional[str] = None  # 结束日期 如:2021-09-08


class FBACreateShipmentPlanRequestProductListItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    packing_type: int  # 包装类型： 1 混装，2 原厂
    shipment_time: Optional[str] = None  # 发货时间，格式：Y-m-d
    msku: str  # MSKU
    fnsku: str  # FNSKU
    shipment_plan_quantity: int  # 计划发货量
    quantity_in_case: Optional[int] = None  # 单箱数量【PCS】
    box_num: Optional[int] = None  # 箱数
    logistics_provider_id: Optional[int] = None  # 物流商id，查询头程物流渠道列表 接口对应字段【data>>provider>>id】
    logistics_channel_id: Optional[int] = None  # 物流渠道id，查询头程物流渠道列表 接口对应字段【data>>id】
    wid: Optional[int] = None  # 系统仓库id
    remark: Optional[str] = None  # 商品信息备注
    purchase_plan_sn: Optional[str] = None  # 关联采购计划单号

class FBACreateShipmentPlanRequest(LingXingModel):
    """Request for 创建FBA发货计划.
    
    POST /erp/sc/routing/storage/shipment/createShipmentPlan
    """
    remark: Optional[str] = None  # 批次信息备注
    product_list: List[FBACreateShipmentPlanRequestProductListItem]


class FBAUpdatePlanListsRequest(LingXingModel):
    """Request for 编辑FBA发货计划.
    
    POST /erp/sc/routing/storage/shipment/updateShipmentPlan
    """
    order_sn: str  # 发货计划单号
    shipment_time: Optional[str] = None  # 发货时间，格式：Y-m-d
    packing_type: Optional[int] = None  # 包装类型： 1 混装，2 原厂
    logistics_provider_id: Optional[int] = None  # 物流商id
    logistics_channel_id: Optional[int] = None  # 物流渠道id
    shipment_plan_quantity: Optional[int] = None  # 计划发货量
    quantity_in_case: Optional[int] = None  # 单箱数量（PCS）
    box_num: Optional[int] = None  # 箱数
    sys_wid: Optional[int] = None  # 系统仓库id【发货仓库】
    cg_package_length: Optional[float] = None  # 包装规格长（cm）【保留两位小数】
    cg_package_width: Optional[float] = None  # 包装规格宽（cm）【保留两位小数】
    cg_package_height: Optional[float] = None  # 包装规格高（cm）【保留两位小数】
    cg_box_length: Optional[float] = None  # 箱规长（cm）【保留两位小数】
    cg_box_width: Optional[float] = None  # 箱规宽（cm）【保留两位小数】
    cg_box_height: Optional[float] = None  # 箱规高（cm）【保留两位小数】
    nw: Optional[float] = None  # 单品净重（g）【保留两位小数】
    gw: Optional[float] = None  # 单品毛重（g）【保留两位小数】
    cg_box_weight: Optional[float] = None  # 单箱重量（kg）【保留两位小数】
    remark: Optional[str] = None  # 备注


class FBAGetInboundShipmentListRequestSeniorSearchListItem(LingXingModel):
    search_field: str  # 搜索字段： sku shipment_sn 发货单号 shipment_id 货件单号
    search_value: List  # 搜索值

class FBAGetInboundShipmentListRequest(LingXingModel):
    """Request for 查询发货单列表.
    
    POST /erp/sc/routing/storage/shipment/getInboundShipmentList
    """
    search_value: Optional[str] = None  # 搜索的值
    search_field: Optional[str] = None  # 搜索字段： sku shipment_sn 发货单号 shipment_id 货件单号
    sids: Optional[str] = None  # 店铺id,多个时通过英文逗号分隔,如1,2,3，对应查询亚马逊店铺列表接口对应字段【sid】
    mids: Optional[str] = None  # 国家id,多个时通过英文逗号分隔,如1,2,3
    wid: Optional[str] = None  # 仓库id,多个时通过英文逗号分隔,如1,2,3
    logistics_type: Optional[list] = None  # 物流方式id
    status: Optional[int] = None  # 发货单状态： -1 : 待配货，  0：待发货， 1：已发货， 3：已作废， 4：已删除
    print_status: Optional[str] = None  # 打印状态 0未打印 1 已打印
    pick_status: Optional[str] = None  # 拣货状态 0 未拣货 1已拣货
    time_type: Optional[int] = None  # 时间类型：  3创建时间 (允许精确到时分秒)  2创建时间  1到货时间   0发货时间  4更新时间 (允许精确到时分秒)
    start_date: Optional[str] = None  # 开始日期
    end_date: Optional[str] = None  # 结束日期
    offset: int  # 偏移量=（currentPage -1）*length
    length: int  # 长度
    is_delete: Optional[float] = None  # 是否删除：0 未删除【默认】 1 已删除 2 全部
    senior_search_list: Optional[List[FBAGetInboundShipmentListRequestSeniorSearchListItem]] = None


class FBAGetinboundshipmentlistmwsdetailRequest(LingXingModel):
    """Request for 查询发货单详情.
    
    POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail
    """
    shipment_sn: str  # 发货单号
    return_deleted: Optional[bool] = None  # 是否返回已删除数据: false-否(默认)，true-是


class FBAGetInboundShipmentListMwsDetailListRequest(LingXingModel):
    """Request for 批量查询发货单详情.
    
    POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList
    """
    shipment_sn_arr: List  # 发货单号数组，上限50
    return_deleted: Optional[bool] = None  # 是否返回已删除数据: false-否(默认)，true-是


class FBACreatereadysendorderRequestListItem(LingXingModel):
    seller_id: str  # 亚马逊店铺id
    warehouse_seller_id: Optional[int] = None  # 仓库店铺id
    marketplace_id: str  # 亚马逊市场id
    shipment_id: str  # 货件单号
    fulfillment_network_sku: str  # 货件fnsku
    fnsku: Optional[str] = None  # 本地发货的fnsku，默认空
    num: int  # 发货数量
    box_num: Optional[int] = None  # 箱数
    sku: str  # sku
    tax_currency: Optional[str] = None  # 报关税费币种
    tax_amount: Optional[str] = None  # 税费值
    cg_product_gross_weight: Optional[str] = None  # 采购：单品毛重（G）；不传值则自动取【商品管理】模块维护的SKU“单品毛重”；按计费重分摊时需用到该字段
    cg_product_net_weight: Optional[str] = None  # 采购：单品净重（G）；不传值则自动取【商品管理】模块维护的SKU“单品净重”；
    cg_package_length: Optional[str] = None  # 采购：包装规格-长（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-长”；按计费重分摊时需用到该字段
    cg_package_width: Optional[str] = None  # 采购：包装规格-宽（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-宽”；按计费重分摊时需用到该字段
    cg_package_height: Optional[str] = None  # 采购：包装规格-高（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-高”；按计费重分摊时需用到该字段
    cg_box_weight: Optional[str] = None  # 采购：单箱重量（KG）；不传值则自动取【商品管理】模块维护的SKU“单箱重量”；按计费重分摊时需用到该字段
    transport_cost: Optional[str] = None  # 自定义头程费，head_fee_type为4才生效
    cg_box_length: Optional[str] = None  # 箱规-长（CM）
    cg_box_width: Optional[str] = None  # 箱规-宽（CM）
    cg_box_height: Optional[str] = None  # 箱规-高（CM）
    quantity_in_case: Optional[int] = None  # 单箱数量（PCS）
    remark: Optional[str] = None  # 备注
    purchase_items: Optional[list] = None  # 工厂直发手动选择出库批次
    purchase_items__relation_num: int  # 关联量
    purchase_items__purchase_sn: Optional[str] = None  # 系统采购单号
    purchase_items__custom_purchase_sn: Optional[str] = None  # 自定义采购单号(无系统采购单号时必填)
    warehouse_items: Optional[list] = None  # 多仓发货商品
    warehouse_items__sys_wid: Optional[int] = None  # 多仓系统仓库id
    warehouse_items__warehouse_seller_id: Optional[int] = None  # 多仓发货仓库店铺id
    warehouse_items__warehouse_fnsku: Optional[str] = None  # 多仓发货仓库fnsku
    warehouse_items__out_num: Optional[int] = None  # 调出量

class FBACreatereadysendorderRequestBoxListItem(LingXingModel):
    box_num: str  # 箱子数
    cg_box_length: float  # 箱子长（CM）
    cg_box_width: float  # 箱子宽（CM）
    cg_box_height: float  # 箱子高（CM）
    cg_box_weight: float  # 箱子重（KG）
    box_skus: List  # 箱子内包含的SKU信息，需与list里的数据保持一致
    box_skus__seller_id: str  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    box_skus__marketplace_id: str  # 亚马逊市场id
    box_skus__shipment_id: str  # 货件单号
    box_skus__fulfillment_network_sku: str  # 货件fnsku
    box_skus__quantity_in_case: float  # 单箱数量
    box_skus__sku: str  # SKU

class FBACreatereadysendorderRequestHeadLogisticsListItem(LingXingModel):
    tracking_list: Optional[list] = None  # 轨迹信息数组
    tracking_list__tracking_no: Optional[str] = None  # 查询单号
    tracking_list__transport_type: Optional[str] = None  # 运输类型： 1 快递 2 海运 3 空运 4 其他
    tracking_list__order_type_code: Optional[int] = None  # 单号类型：【注意：与运输类型联动关系】 1 订舱号 2 提单号 3 箱号 4 其他 5 跟踪单号 6航班号 当transport_type=1时只能传5 当transport_type=2时只能传1、
    tracking_list__shippers: Optional[str] = None  # 承运商，运输类型为海运时才有意义： 获取发货单头程物流-承运商信息接口获取
    tracking_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list: Optional[dict] = None  # 费用明细-预估费用
    estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)
    estimate_expenses_list__price: str  # 单价
    estimate_expenses_list__price_currency: str  # 单价币种
    estimate_expenses_list__logistics_fee: str  # 物流费用
    estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    estimate_expenses_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id
    estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    actual_expenses_list: Optional[dict] = None  # 费用明细-实际费用
    actual_expenses_list__tax_fee: str  # 税费
    actual_expenses_list__tax_fee_currency: str  # 税费币种
    actual_expenses_list__chargeable_weight: str  # 计费重【废弃字段】
    actual_expenses_list__weight: str  # 实重（单位：KG）
    actual_expenses_list__volume: str  # 体积（单位：m³）
    actual_expenses_list__price: str  # 单价
    actual_expenses_list__price_currency: str  # 单价币种
    actual_expenses_list__logistics_fee: str  # 物流费用
    actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    actual_expenses_list__remark: Optional[str] = None  # 备注
    actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id
    actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种

class FBACreatereadysendorderRequestLogisticsListItem(LingXingModel):
    tracking_number: Optional[str] = None  # 物流商单号
    replace_tracking_number: Optional[str] = None  # 跟踪号
    transportation_cost: Optional[float] = None  # 实际物流费用
    transportation_currency: Optional[str] = None  # 实际物流费用币种
    other_cost: Optional[float] = None  # 实际其他费用
    other_currency: Optional[str] = None  # 实际其他费用币种
    other_cost_remark: Optional[str] = None  # 其他费用备注
    predicted_transportation_cost: Optional[float] = None  # 预估物流费用
    predicted_transportation_currency: Optional[str] = None  # 预估物流费用币种
    predicted_other_cost: Optional[float] = None  # 预估其他费用
    predicted_other_currency: Optional[str] = None  # 预估其他费用币种

class FBACreatereadysendorderRequest(LingXingModel):
    """Request for 生成待发货的发货单.
    
    POST /erp/sc/routing/storage/shipment/createReadySendOrder
    """
    wid: Optional[int] = None  # 自定义仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。
    sys_wid: Optional[int] = None  # 系统仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。多仓库发货时传 -1。
    expected_arrival_date: Optional[str] = None  # 预计到达时间，格式：Y-m-d
    etd_date: Optional[str] = None  # 开船时间，格式：Y-m-d
    eta_date: Optional[str] = None  # 预计到港时间，格式：Y-m-d
    delivery_date: Optional[str] = None  # 实际妥投时间，格式：Y-m-d
    actual_shipment_time: Optional[str] = None  # 实际发货时间，格式：Y-m-d
    head_fee_type: Optional[int] = None  # 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积
    tax_fee_type: Optional[int] = None  # 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积
    is_points_behind: Optional[int] = None  # 是否分抛计算：0 否，1 是；头程分摊方式为按计费重时用
    points_behind_coeffient: Optional[int] = None  # 分抛系数：0~100,分抛计算选是时必填
    logistics_channel_id: Optional[int] = None  # 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】
    is_related: Optional[int] = None  # 是否关联普通商品： 0 否 1 是【会拆分组合商品】
    vat_code: Optional[str] = None  # 店铺VAT税号
    is_pick: Optional[int] = None  # 是否拣货：【默认0】 0 否 1 是
    remark: Optional[str] = None  # 备注
    ship_mode: Optional[int] = None  # 发货方式：1-默认，2-工厂直发
    hand_pick_purchase: Optional[int] = None  # 工厂直发时手动选择出库批次：1-否，2-是
    box_type: Optional[str] = None  # 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU
    box_remark: Optional[str] = None  # 装箱备注
    logistics_list_type: Optional[int] = None  # 物流信息版本： 0 旧版 1 新版
    list_field: FBACreatereadysendorderRequestListItem = Field(alias="list")
    box_list: List[FBACreatereadysendorderRequestBoxListItem]
    head_logistics_list: FBACreatereadysendorderRequestHeadLogisticsListItem
    logistics_list: Optional[List[FBACreatereadysendorderRequestLogisticsListItem]] = None


class FBACreateSendedOrderRequestListItem(LingXingModel):
    seller_id: str  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    warehouse_seller_id: Optional[int] = None  # 仓库店铺id
    marketplace_id: str  # 市场id
    shipment_id: str  # 货件单号
    fulfillment_network_sku: str  # 货件fnsku
    fnsku: Optional[str] = None  # 本地发货的fnsku，默认空
    num: int  # 发货数量
    box_num: Optional[int] = None  # 箱数
    sku: str  # sku
    tax_currency: Optional[str] = None  # 报关税费币种
    tax_amount: Optional[str] = None  # 税费值
    cg_product_gross_weight: Optional[str] = None  # 采购：单品净重（G）；不传值则自动取【商品管理】模块维护的SKU“单品毛重”；按计费重分摊时需用到该字段
    cg_package_length: Optional[str] = None  # 采购：包装规格-长（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-长”；按计费重分摊时需用到该字段
    cg_package_width: Optional[str] = None  # 采购：包装规格-宽（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-宽”；按计费重分摊时需用到该字段
    cg_package_height: Optional[str] = None  # 采购：包装规格-高（CM）；不传值则自动取【商品管理】模块维护的SKU“包装规格-高”；按计费重分摊时需用到该字段
    cg_box_weight: Optional[str] = None  # 采购：单箱重量（KG）；不传值则自动取【商品管理】模块维护的SKU“单箱重量”；按计费重分摊时需用到该字段
    transport_cost: Optional[str] = None  # 自定义头程费，head_fee_type为4才生效
    purchase_items: Optional[list] = None  # 工厂直发手动选择出库批次
    purchase_items__relation_num: int  # 关联量
    purchase_items__purchase_sn: Optional[str] = None  # 系统采购单号
    purchase_items__custom_purchase_sn: Optional[str] = None  # 自定义采购单号(无系统采购单号时必填)

class FBACreateSendedOrderRequestBoxListItem(LingXingModel):
    box_num: str  # 箱子数
    cg_box_length: float  # 箱子长
    cg_box_width: float  # 箱子宽
    cg_box_height: float  # 箱子高
    cg_box_weight: float  # 箱子重
    box_skus: List  # 箱子内包含的SKU信息，需与list里的数据保持一致
    box_skus__seller_id: str  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    box_skus__marketplace_id: str  # 市场id
    box_skus__shipment_id: str  # 货件单号
    box_skus__fulfillment_network_sku: str  # 货件fnsku
    box_skus__quantity_in_case: int  # 单箱数量
    box_skus__sku: str  # SKU

class FBACreateSendedOrderRequestHeadLogisticsListItem(LingXingModel):
    tracking_list: Optional[list] = None  # 轨迹信息数组
    tracking_list__tracking_no: Optional[str] = None  # 查询单号
    tracking_list__transport_type: Optional[int] = None  # 运输类型： 1 快递 2 海运 3 空运 4 其他
    tracking_list__order_type_code: Optional[int] = None  # 单号类型：【注意：与运输类型联动关系】 1 订舱号 2 提单号 3 箱号 4 其他 5 跟踪单号 6航班号 当transport_type=1时只能传5 当transport_type=2时只能传1、
    tracking_list__shippers: Optional[str] = None  # 承运商，运输类型为海运时才有意义： 获取发货单头程物流-承运商信息接口获取
    tracking_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list: Optional[dict] = None  # 费用明细-预估费用
    estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)
    estimate_expenses_list__price: str  # 单价
    estimate_expenses_list__price_currency: str  # 单价币种
    estimate_expenses_list__logistics_fee: str  # 物流费用
    estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    estimate_expenses_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id
    estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    actual_expenses_list: Optional[dict] = None  # 费用明细-实际费用
    actual_expenses_list__tax_fee: str  # 税费
    actual_expenses_list__tax_fee_currency: str  # 税费币种
    actual_expenses_list__chargeable_weight: str  # 计费重【废弃字段】
    actual_expenses_list__weight: str  # 实重（单位：KG）
    actual_expenses_list__volume: str  # 体积（单位：m³）
    actual_expenses_list__price: str  # 单价
    actual_expenses_list__price_currency: str  # 单价币种
    actual_expenses_list__logistics_fee: str  # 物流费用
    actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    actual_expenses_list__remark: Optional[str] = None  # 备注
    actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id
    actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种

class FBACreateSendedOrderRequestLogisticsListItem(LingXingModel):
    tracking_number: Optional[str] = None  # 物流商单号
    replace_tracking_number: Optional[str] = None  # 跟踪号
    transportation_cost: Optional[float] = None  # 实际物流费用
    transportation_currency: Optional[str] = None  # 实际物流费用币种
    other_cost: Optional[float] = None  # 实际其他费用
    other_currency: Optional[str] = None  # 实际其他费用币种
    other_cost_remark: Optional[str] = None  # 其他费用备注
    predicted_transportation_cost: Optional[float] = None  # 预估物流费用
    predicted_transportation_currency: Optional[str] = None  # 预估物流费用币种
    predicted_other_cost: Optional[float] = None  # 预估其他费用
    predicted_other_currency: Optional[str] = None  # 预估其他费用币种

class FBACreateSendedOrderRequest(LingXingModel):
    """Request for 生成已发货的发货单.
    
    POST /erp/sc/storage/shipment/createSendedOrder
    """
    wid: Optional[int] = None  # 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid
    sys_wid: int  # 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid
    expected_arrival_date: Optional[str] = None  # 预计到达时间：Y-m-d
    etd_date: Optional[str] = None  # 开船时间，格式：Y-m-d
    eta_date: Optional[str] = None  # 预计到港时间，格式：Y-m-d
    delivery_date: Optional[str] = None  # 实际妥投时间，格式：Y-m-d
    actual_shipment_time: Optional[str] = None  # 实际发货时间，格式：Y-m-d
    head_fee_type: Optional[int] = None  # 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积
    tax_fee_type: Optional[int] = None  # 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 5 箱子-体积
    is_points_behind: Optional[int] = None  # 是否分抛计算：0 否，1 是，头程分摊方式为按计费重时用
    points_behind_coeffient: Optional[int] = None  # 分抛系数：0~100，分抛计算选是时必填
    logistics_channel_id: Optional[int] = None  # 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】
    is_related: Optional[int] = None  # 组合商品扣减库存时是否自动拆分成单品进行扣减： 0 否 1 是【会拆分组合商品】
    request_flag: Optional[str] = None  # 自定义请求标识，本次请求超时后可根据此标识查询此次请求的结果，由请求方保持标识唯一性
    ship_mode: Optional[int] = None  # 发货方式：1-默认，2-工厂直发
    hand_pick_purchase: Optional[int] = None  # 工厂直发时手动选择出库批次：1-否，2-是
    remark: Optional[str] = None  # 备注
    box_type: Optional[str] = None  # 装箱类型： SINGLE 每箱只允许一款SKU MULTIPLE 每箱允许多款SKU
    box_remark: Optional[str] = None  # 装箱备注
    logistics_list_type: Optional[int] = None  # 物流信息版本： 0 旧版 1 新版
    list_field: FBACreateSendedOrderRequestListItem = Field(alias="list")
    box_list: Optional[List[FBACreateSendedOrderRequestBoxListItem]] = None
    head_logistics_list: FBACreateSendedOrderRequestHeadLogisticsListItem
    logistics_list: Optional[List[FBACreateSendedOrderRequestLogisticsListItem]] = None


class FBASearchprocessresultRequest(LingXingModel):
    """Request for 发货单创建接口结果查询.
    
    POST /erp/sc/routing/storage/shipment/searchProcessResult
    """
    request_flag: str  # 生成单据时传的请求标识


class FBAShipmentLockStockRequest(LingXingModel):
    """Request for 发货单分配库存.
    
    POST /erp/sc/routing/storage/shipment/lockStock
    """
    shipment_nos: List  # 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】
    is_auto_batch: Optional[int] = None  # 是否锁定至批次，1：是，0：否，默认为否，否：只锁定库存数量，发货时按先进先出规则匹配出库批次；是：按先进先锁规则自动指定批次并锁定，发货时按锁定批次出库；分配库存后，可在【查询发货单详情】接口的采购


class FBAOutboundorderreleasestockRequest(LingXingModel):
    """Request for 发货单释放库存.
    
    POST /erp/sc/routing/storage/shipment/releaseStock
    """
    shipment_nos: List  # 发货单号


class FBASendGoodsRequest(LingXingModel):
    """Request for FBA发货单发货.
    
    POST /erp/sc/storage/shipment/sendGoods
    """
    shipment_nos: List  # 发货单号列表


class FBAUpdateinboundshipmentlistmwsRequestItemsItem(LingXingModel):
    id: Optional[int] = None  # 商品明细id，查询发货单详情接口对应字段【data>>items>>id】
    num: Optional[str] = None  # 发货量，发货量不允许大于计划发货量

class FBAUpdateinboundshipmentlistmwsRequestBoxListItem(LingXingModel):
    box_num: float  # 箱子数
    cg_box_length: float  # 箱子长（CM）
    cg_box_width: float  # 箱子宽（CM）
    cg_box_height: float  # 箱子高（CM）
    cg_box_weight: float  # 箱子重（KG）
    box_skus: List  # 箱子内包含的SKU信息
    box_skus__item_id: float  # 发货单商品ID
    box_skus__quantity_in_case: float  # 单箱数量
    box_nos: Optional[list] = None  # 自定义箱号

class FBAUpdateinboundshipmentlistmwsRequest(LingXingModel):
    """Request for 编辑发货单.
    
    POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws
    """
    shipment_sn: str  # 发货单号
    remark: Optional[str] = None  # 备注
    box_type: Optional[str] = None  # 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU
    items: Optional[List[FBAUpdateinboundshipmentlistmwsRequestItemsItem]] = None
    box_list: Optional[List[FBAUpdateinboundshipmentlistmwsRequestBoxListItem]] = None


class FBAInvalidShipmentSnRequest(LingXingModel):
    """Request for FBA-作废发货单.
    
    POST /basicOpen/openapi/fbaShipment/shipmentSn/invalid
    """
    shipmentNos: List  # 发货单号
    isReturnStock: int  # 产品库存是否恢复 1恢复 0不恢复
    isReturnStockAux: int  # 辅料库存是否恢复 1恢复 0不恢复
    cancelReason: Optional[str] = None  # 作废原因


class FBAUpdatelistlogisticsRequestDataItem(LingXingModel):
    order_sn: str  # 发货单号
    expected_arrival_date: Optional[str] = None  # 到货时间，格式：Y-m-d
    etd_date: Optional[str] = None  # 开船时间，格式：Y-m-d
    eta_date: Optional[str] = None  # 预计到港时间，格式：Y-m-d
    delivery_date: Optional[str] = None  # 实际妥投时间，格式：Y-m-d
    actual_shipment_time: Optional[str] = None  # 实际发货时间，格式：Y-m-d
    tax_fee_type: Optional[int] = None  # 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积/体积重 6 箱子-计费重 7 箱子-实重 8 产品-根据清关单价*税率占比
    logistics_channel_id: Optional[int] = None  # 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】
    logistics_list_type: Optional[int] = None  # 物流信息版本： 1 新版
    head_logistics_list: Optional[dict] = None  # 新版头程物流信息 【对应 logistics_list_type = 1】 【注意：新版头程物流数据为覆盖式更新，包括tracking_list、estimate_expenses_list、actu
    head_logistics_list__tracking_list: List  # 轨迹信息数组
    head_logistics_list__tracking_list__tracking_no: Optional[str] = None  # 查询单号
    head_logistics_list__tracking_list__transport_type: int  # 运输类型： 1 快递 2 海运 3 空运 4 其他
    head_logistics_list__tracking_list__order_type_code: int  # 单号类型：【注意：与运输类型联动关系】 1 订舱号 2 提单号 3 箱号 4 其他 5 跟踪单号 6航班号 当transport_type=1时只能传5 当transport_type=2时只能传1、
    head_logistics_list__tracking_list__shippers: Optional[str] = None  # 承运商，运输类型为海运时才有意义： 获取发货单头程物流-承运商信息接口获取
    head_logistics_list__tracking_list__remark: Optional[str] = None  # 备注
    head_logistics_list__estimate_expenses_list: dict  # 费用明细-预估费用
    head_logistics_list__estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)【废弃字段】
    head_logistics_list__estimate_expenses_list__price: str  # 单价
    head_logistics_list__estimate_expenses_list__price_currency: str  # 单价币种
    head_logistics_list__estimate_expenses_list__logistics_fee: str  # 物流费用
    head_logistics_list__estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    head_logistics_list__estimate_expenses_list__remark: Optional[str] = None  # 备注
    head_logistics_list__estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    head_logistics_list__estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id（20位）
    head_logistics_list__estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    head_logistics_list__estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    head_logistics_list__actual_expenses_list: dict  # 费用明细-实际费用
    head_logistics_list__actual_expenses_list__tax_fee: str  # 税费
    head_logistics_list__actual_expenses_list__tax_fee_currency: str  # 税费币种
    head_logistics_list__actual_expenses_list__price: str  # 单价
    head_logistics_list__actual_expenses_list__price_currency: str  # 单价币种
    head_logistics_list__actual_expenses_list__logistics_fee: str  # 物流费用
    head_logistics_list__actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    head_logistics_list__actual_expenses_list__remark: Optional[str] = None  # 备注
    head_logistics_list__actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    head_logistics_list__actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id
    head_logistics_list__actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    head_logistics_list__actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    logistics_list: List  # 旧版物流信息，即将下线
    logistics_list__tracking_number: str  # 物流商单号
    logistics_list__replace_tracking_number: str  # 跟踪号
    logistics_list__transportation_cost: Optional[float] = None  # 实际物流费用，精度是小数点后2位
    logistics_list__transportation_currency: Optional[str] = None  # 实际物流费用币种，费用填写时必填
    logistics_list__other_cost: Optional[float] = None  # 实际其他费用，精度是小数点后2位
    logistics_list__other_currency: Optional[str] = None  # 实际其他费用币种，费用填写时必填
    logistics_list__other_cost_remark: Optional[str] = None  # 其他费用备注
    logistics_list__predicted_transportation_cost: Optional[float] = None  # 预估物流费用，精度是小数点后2位
    logistics_list__predicted_transportation_currency: Optional[str] = None  # 预估物流费用币种，费用填写时必填
    logistics_list__predicted_other_cost: Optional[float] = None  # 预估其他费用，精度是小数点后2位
    logistics_list__predicted_other_currency: Optional[str] = None  # 预估其他费用币种，费用填写时必填

class FBAUpdatelistlogisticsRequestHeadLogisticsListItem(LingXingModel):
    actual_expenses_list__chargeable_weight: str  # 计费重【废弃字段】
    actual_expenses_list__weight: str  # 实重（单位：KG）
    actual_expenses_list__volume: str  # 体积（单位：m³）

class FBAUpdatelistlogisticsRequest(LingXingModel):
    """Request for 更新发货单物流信息.
    
    POST /erp/sc/routing/storage/shipment/updateListLogistics
    """
    data: List[FBAUpdatelistlogisticsRequestDataItem]
    head_logistics_list: FBAUpdatelistlogisticsRequestHeadLogisticsListItem


class FBAUpdateCustomCostRequestListItem(LingXingModel):
    msku: Optional[str] = None  # msku
    sku: Optional[str] = None  # sku
    shipment_id: Optional[str] = None  # 货件单号
    custom_purchase_price_unit: Optional[float] = None  # 采购单价（自定义成本)
    custom_outbound_cost_unit: Optional[float] = None  # 单位出库费用（自定义成本)
    custom_aux_cost: Optional[float] = None  # 单位辅料费用（自定义成本)
    custom_outbound_head_cost_unit: Optional[float] = None  # 单位出库头程（自定义成本)

class FBAUpdateCustomCostRequest(LingXingModel):
    """Request for 更新发货单自定义成本.
    
    POST /erp/sc/routing/storage/shipment/updateCustomCost
    """
    shipment_sn: str  # 发货单号
    is_custom_cost: int  # 是否自定义成本
    list_field: Optional[List[FBAUpdateCustomCostRequestListItem]] = Field(None, alias="list")


class FBAGetSeaTrackSupplierCarriersRequest(LingXingModel):
    """Request for 获取发货单头程物流信息-承运商信息.
    
    POST /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers
    """
    vehicle_type: Optional[str] = None  # 运输类型【默认Sea】： Sea 海运 Express 快递 Aviation 空运


class FBACreateSTATaskRequestInboundplanitemsItem(LingXingModel):
    expiration: Optional[str] = None  # 有效期
    labelOwner: str  # 标签类型 AMAZON SELLER NONE
    msku: str  # msku
    prepOwner: str  # 预处理提供方 AMAZON SELLER NONE
    quantity: int  # 申报量
    prepCategory: Optional[str] = None  # 预处理分类：（当商品未在卖家中心设置过预处理指导时可填写）  ADULT-成人：对应的预处理类型通常为无需预处理[ITEM_NO_PREP]，也可传其他预处理类型  HANGER-悬挂在衣架上的服装：
    prepTypes: Optional[list] = None  # 预处理类型：（当商品未在卖家中心设置过预处理指导时可填写）  ITEM_POLYBAGGING-聚乙烯塑料袋包装：将商品放在透明袋中，以防破损、落尘或泄漏。包装袋必须印有窒息警告，必须密封（如果不是自
    invoiceSns: Optional[list] = None  # 发货计划编码列表

class FBACreateSTATaskRequest(LingXingModel):
    """Request for 创建STA任务.
    
    POST /amzStaServer/openapi/inbound-plan/createInboundPlan
    """
    addressLine1: str  # 详细街道地址1
    addressLine2: Optional[str] = None  # 详细街道地址2
    city: str  # 城市
    companyName: Optional[str] = None  # 公司名称
    countryCode: str  # 国家(地区）
    email: Optional[str] = None  # 邮箱
    phoneNumber: str  # 电话号码
    planName: Optional[str] = None  # 计划名称
    positionType: str  # 分仓方式(1-先装箱再分仓，2-先分仓再装箱)
    postalCode: str  # 邮政编码
    remark: Optional[str] = None  # 备注
    shipperName: str  # 发货方名称
    sid: int  # 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】
    stateOrProvinceCode: str  # 州/省/地区
    inboundPlanItems: List[FBACreateSTATaskRequestInboundplanitemsItem]


class FBAListPackingGroupItemsRequest(LingXingModel):
    """Request for 查询包装组.
    
    POST /amzStaServer/openapi/inbound-packing/listPackingGroupItems
    """
    inboundPlanId: str  # STA任务编号,，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBASavePackingInfomationRequestBoxesItem(LingXingModel):
    dimensions__height: str  # 高
    dimensions__length: str  # 长
    dimensions__unitOfMeasurement: str  # 长度单位：IN、CM
    dimensions__width: str  # 宽
    items: List  # 商品信息
    items__expiration: Optional[str] = None  # 有效期
    items__labelOwner: str  # 标签类型：AMAZON、SELLER、NONE
    items__msku: str  # msku
    items__prepOwner: str  # 预处理提供方：AMAZON、SELLER、NONE
    items__quantity: int  # 申报量
    weight: dict  # 重量
    weight__unit: str  # 重量单位：LB、KG
    weight__value: str  # 重量单位值

class FBASavePackingInfomationRequest(LingXingModel):
    """Request for 保存装箱信息.
    
    POST 
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    packingGroupId: Optional[str] = None  # 包装组id：先装箱后分仓方式时必填；先分仓后装箱方式时无需填写
    shipmentId: Optional[str] = None  # 货件id：先分仓后装箱方式时必填；分装箱后分仓方式时无需填写
    sid: str  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】
    boxes: List[FBASavePackingInfomationRequestBoxesItem]


class FBASubPackingInformationRequestPackagegroupingsItem(LingXingModel):
    boxes: List  # 箱子信息
    boxes__dimensions: Optional[dict] = None  # 维度信息
    boxes__dimensions__height: float  # 高
    boxes__dimensions__length: float  # 长
    boxes__dimensions__unitOfMeasurement: str  # 长度单位：IN、CM
    boxes__dimensions__width: float  # 宽
    boxes__items: List  # 商品信息
    boxes__items__expiration: Optional[str] = None  # 有效期
    boxes__items__labelOwner: str  # 标签类型 AMAZON SELLER NONE
    boxes__items__msku: str  # msku
    boxes__items__prepOwner: str  # 预处理提供方 AMAZON SELLER NONE
    boxes__items__quantity: int  # 申报量
    boxes__weight: Optional[dict] = None  # 重量
    boxes__weight__unit: str  # 重量单位：LB、KG
    boxes__weight__value: float  # 重量单位值
    packingGroupId: Optional[str] = None  # 包装组id：先装箱后分仓方式时必填；先分仓后装箱方式时无需填写
    shipmentId: Optional[str] = None  # 货件id：先分仓后装箱方式时必填；分装箱后分仓方式时无需填写

class FBASubPackingInformationRequest(LingXingModel):
    """Request for 提交装箱信息.
    
    POST /amzStaServer/openapi/inbound-packing/setPackingInformation
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】
    packageGroupings: List[FBASubPackingInformationRequestPackagegroupingsItem]


class FBAGenerateShipmentPlanRequest(LingXingModel):
    """Request for 生成货件方案.
    
    POST /amzStaServer/openapi/inbound-shipment/generatePlacementOptions
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAShipmentPreViewRequest(LingXingModel):
    """Request for 查询货件方案.
    
    POST /amzStaServer/openapi/inbound-shipment/shipmentPreView
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAGetinboundpackingboxinfoRequest(LingXingModel):
    """Request for 查询货件方案的装箱信息.
    
    POST /amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo
    """
    inboundPlanId: Optional[str] = None  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: Optional[int] = None  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAConfirmShipmentPlanRequest(LingXingModel):
    """Request for 确认货件方案.
    
    POST /amzStaServer/openapi/inbound-shipment/confirmPlacementOption
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    placementOptionId: str  # 货件方案id
    shipmentIds: List  # 货件列表：传入对应货件方案id下的所有货件id
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAGenerateTransportListRequestShipmentidlistItem(LingXingModel):
    palletList: Optional[list] = None  # 帕托信息：如果修改了帕托信息需要重新生成承运方式
    palletList__height: float  # 高
    palletList__length: float  # 长
    palletList__lengthUnit: str  # 长度单位(IN-英制,CM-公制)
    palletList__quantity: int  # 数量
    palletList__stackability: str  # 是否可堆叠（STACKABLE、NON_STACKABLE）
    palletList__weight: float  # 单个重量
    palletList__weightUnit: str  # 重量单位（LB-磅，KG-千克）
    palletList__width: float  # 宽
    shipingTime: str  # 发货时间：如果修改了发货时间需要重新生成承运方式 格式：yyyy-MM-dd
    shipmentId: str  # 货件id

class FBAGenerateTransportListRequest(LingXingModel):
    """Request for 生成承运方式.
    
    POST /amzStaServer/openapi/inbound-shipment/generateTransportList
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】
    shipmentIdList: List[FBAGenerateTransportListRequestShipmentidlistItem]


class FBAGenerateDeliveryDateListRequest(LingXingModel):
    """Request for 生成可选送达时间.
    
    POST /amzStaServer/openapi/inbound-shipment/generateDeliveryDateList
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentId: str  # 货件id，对应查询货件方案接口对应字段【shipmentId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAGetTransportListRequest(LingXingModel):
    """Request for 查询承运方式.
    
    POST /amzStaServer/openapi/inbound-shipment/getTransportList
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentId: str  # 货件id，对应查询货件方案接口对应字段【shipmentId】
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAGetDeliveryDateListRequest(LingXingModel):
    """Request for 查询可选送达时间.
    
    POST /amzStaServer/openapi/inbound-shipment/getDeliveryDateList
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentId: str  # 货件id，对应查询货件方案接口对应字段【shipmentId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBASubDeliveryTimeRequest(LingXingModel):
    """Request for 提交送达时间.
    
    POST /amzStaServer/openapi/inbound-shipment/commitStaDeliverTime
    """
    deliveryWindowOptionId: str  # 送达时间id
    endDate: str  # (北京时间) 备注:格式：YYYY-MM-DD
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentId: str  # 货件id，对应查询货件方案接口对应字段【shipmentId】
    sid: int  # 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # (北京时间) 备注:格式：YYYY-MM-DD


class FBASubShipmentDistributionServiceRequestShipmentdistributioninfoItem(LingXingModel):
    alphaCode: str  # 承运方式编码
    alphaName: str  # 承运方式名称
    declaredAmount: Optional[float] = None  # 申报价值
    declaredCode: Optional[str] = None  # 申报价值货币
    deliveryWindowOptionId: str  # 送达时间ID
    endDate: str  # 送达时段-结束时间:(北京时间) 备注:格式：YYYY-MM-DD
    freightClass: Optional[str] = None  # 货物等级
    palletList: Optional[list] = None  # 帕托信息
    palletList__height: Optional[float] = None  # 高
    palletList__length: Optional[float] = None  # 长
    palletList__lengthUnit: Optional[str] = None  # 长度单位(IN-英制,CM-公制)
    palletList__quantity: Optional[int] = None  # 数量
    palletList__stackability: Optional[str] = None  # 是否可堆叠
    palletList__weight: Optional[float] = None  # 单个重量
    palletList__weightUnit: Optional[str] = None  # 重量单位（LB-磅，KG-千克）
    palletList__width: Optional[float] = None  # 宽
    shipingTime: str  # 发货时间:(北京时间) 备注:格式：YYYY-MM-DD
    shipmentId: str  # 货件单号
    shippingMode: str  # 货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））
    shippingSolution: str  # 承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)
    startDate: str  # 送达时段-开始时间:(北京时间) 备注:格式：YYYY-MM-DD
    transportationOptionId: str  # 承运方式ID

class FBASubShipmentDistributionServiceRequest(LingXingModel):
    """Request for 提交货件配送服务.
    
    POST /amzStaServer/openapi/inbound-shipment/setDeliveryService
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】
    shipmentDistributionInfo: List[FBASubShipmentDistributionServiceRequestShipmentdistributioninfoItem]


class FBAUpdateShipmentPackingRequestBoxesItem(LingXingModel):
    contentInformationSource: str  # 提供方式 BOX_CONTENT_PROVIDED、MANUAL_PROCESS、BARCODE_2D
    dimensions__height: float  # 高
    dimensions__length: float  # 长
    dimensions__unitOfMeasurement: str  # 长度单位：IN、CM
    dimensions__width: float  # 宽
    items: List  # 商品信息
    items__expiration: Optional[str] = None  # 有效期
    items__labelOwner: str  # 标签类型（AMAZON,SELLER,NONE）
    items__msku: str  # msku
    items__prepOwner: str  # 预处理提供方（AMAZON,SELLER,NONE）
    items__quantity: int  # 申报量
    packageId: Optional[str] = None  # 包裹id
    weight__unit: str  # 重量单位：LB、KG
    weight__value: float  # 重量

class FBAUpdateShipmentPackingRequestItemsItem(LingXingModel):
    expiration: Optional[str] = None  # 有效期
    labelOwner: str  # 标签类型（AMAZON,SELLER,NONE）
    msku: str  # msku
    prepOwner: str  # 预处理提供方（AMAZON,SELLER,NONE）
    quantity: int  # 申报量

class FBAUpdateShipmentPackingRequest(LingXingModel):
    """Request for 修改货件装箱信息.
    
    POST /amzStaServer/openapi/inbound-packing/updateShipmentPacking
    """
    inboundPlanId: Optional[str] = None  # 任务编号
    shipmentId: Optional[str] = None  # 货件号
    sid: Optional[int] = None  # 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】
    boxes: List[FBAUpdateShipmentPackingRequestBoxesItem]
    items: FBAUpdateShipmentPackingRequestItemsItem


class FBAUpdateShipmentActualStatusRequestListItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    shipment_id: str  # 货件单号

class FBAUpdateShipmentActualStatusRequest(LingXingModel):
    """Request for 修改货件实际状态.
    
    POST /erp/sc/routing/storage/shipment/updateShipmentActualStatus
    """
    is_closed: int  # 货件状态：0 进行中，1 已完成
    list_field: List[FBAUpdateShipmentActualStatusRequestListItem] = Field(alias="list")


class FBAUpdateShipmentTrackRequestTrackbolistItem(LingXingModel):
    boxId: Optional[str] = None  # 箱子id
    localBoxId: Optional[str] = None  # 本地箱子id
    trackingId: Optional[str] = None  # 跟踪id

class FBAUpdateShipmentTrackRequest(LingXingModel):
    """Request for 上传货件跟踪号.
    
    POST /amzStaServer/openapi/inbound-shipment/updateShipmentTrack
    """
    billOfLadingNumber: Optional[str] = None  # 提货单号,LTL建议填写,非必填
    freightBillNumber: Optional[str] = None  # LTL跟踪编号(LTL必填)
    inboundPlanId: Optional[str] = None  # STA任务编号
    shipmentConfirmationId: Optional[str] = None  # 货件单号
    shipmentId: Optional[str] = None  # 货件id
    sid: int  # 领星店铺ID
    trackBOList: Optional[List[FBAUpdateShipmentTrackRequestTrackbolistItem]] = None


class FBACancelSTATaskRequest(LingXingModel):
    """Request for 取消STA任务.
    
    POST /amzStaServer/openapi/inbound-plan/cancelInboundPlan
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAOperateRequest(LingXingModel):
    """Request for 查询异步任务状态.
    
    POST /amzStaServer/openapi/task-plan/operate
    """
    taskId: str  # 操作任务号


class FBAGetPrepareDetailsRequest(LingXingModel):
    """Request for 获取商品预处理信息.
    
    POST /amzStaServer/openapi/inbound-packing/getPrepDetails
    """
    sid: float  # sid店铺id
    msku: List  # 商品MSKU: 最多不超过100个


class FBASynchronizeSTATaskRequest(LingXingModel):
    """Request for 同步STA任务到ERP.
    
    POST /amzStaServer/openapi/inbound-plan/gatherInboundPlan
    """
    inboundPlanIdList: List  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】


class FBASyncShipmentRequest(LingXingModel):
    """Request for 同步亚马逊货件到ERP.
    
    POST /erp/sc/routing/fba/shipment/syncShipment
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    shipment_ids: List  # 货件编号
    sync_anyway: Optional[int] = None  # 报错是否继续：0 否【默认】，1 是 当系统检测到货件归属国家与店铺不符时，会提示报错，此时传1则按照店铺进行同步


class FBAPrintfbalabelsRequestDataItem(LingXingModel):
    shipment_id: str  # 货件编号
    page_type: str  # 页面类型： PackageLabel_A4_2 - 每张A4纸打印2个标签 PackageLabel_A4_4 - 每张A4纸打印4个标签 PackageLabel_Plain_Paper - 每张美
    num: Optional[int] = None  # 页数【非合作承运人货件必填；合作承运人标签无法指定页数，不需要填】
    page_start_index: Optional[int] = None  # 箱子打印的起始页，默认为1

class FBAPrintfbalabelsRequest(LingXingModel):
    """Request for 查询FBA货件箱子、卡板标签.
    
    POST /erp/sc/storage/shipment/printFbaLabels
    """
    hide_ship_from_company_name: Optional[int] = None  # 隐藏ship from公司名,默认不隐藏,非必填,传值1为开启
    hide_ship_to_company_name: Optional[int] = None  # 传值1为隐藏ship to公司名,默认不隐藏,非必填,传值1为开启
    print_sta_name_page: Optional[int] = None  # 传值1为新增任务名称页,默认不新增,非必填,仅打印box箱子标签时生效,传值1为开启
    sort_label: Optional[int] = None  # 传值1为按箱子顺序重排,默认不按箱子顺序重排,仅打印box箱子子标签时生效(说明:不按箱子顺序重排时,打印文件...
    type: str  # 打印类型：box 箱子标签，card 卡板标签
    data: List[FBAPrintfbalabelsRequestDataItem]


class FBAPrintfnskulabelsRequestDataItem(LingXingModel):
    shipment_id: str  # 货件编号
    num: int  # 标签打印个数
    seller_sku: str  # MSKU
    fnsku: str  # FNSKU

class FBAPrintfnskulabelsRequest(LingXingModel):
    """Request for 查询FBA货件商品FNSKU标签.
    
    POST /erp/sc/storage/shipment/printFnskuLabels
    """
    page_type: str  # 标签页面类型： SINGLE_COL_50_30 热敏纸【50X30】单排 SINGLE_COL_70_30 热敏纸【70X30】单排 DOUBLE_COL_100_30 热敏纸【100X30】双排 
    print_content: Optional[str] = None  # 是否打印：【默认yes】 yes 是 no 否
    content_type: Optional[str] = None  # 打印SKU/品名：【默认sku】 sku SKU sku_name 品名
    print_custom: Optional[str] = None  # 是否打印自定义内容：【默认yes】 yes 是 no 否
    custom_content: Optional[str] = None  # 自定义内容，默认MADE IN CHINA
    new_tag: Optional[str] = None  # 标签中是否显示‘new’字样：【默认yes】 yes 是 no 否
    data: FBAPrintfnskulabelsRequestDataItem


class FBAQuerySTATaskListRequest(LingXingModel):
    """Request for 查询STA任务列表.
    
    POST /amzStaServer/openapi/inbound-plan/page
    """
    page: int  # 分页页码
    length: int  # 分页大小，上限200
    dateBegin: str  # 开始时间(北京时间) 备注:格式：YYYY-MM-DD 双闭区间
    dateEnd: str  # 结束时间(北京时间) 备注:格式：YYYY-MM-DD 双闭区间
    dateType: int  # 时间类型 1:创建 2更新
    planName: Optional[str] = None  # STA任务名称(模糊搜索)
    shipmentIdList: Optional[list] = None  # 货件id或者货件单号(精确搜索)
    sids: Optional[list] = None  # 领星店铺ID 列表，对应查询亚马逊店铺列表
    statusList: Optional[list] = None  # STA任务状态： ACTIVE VOIDED SHIPPED ERRORED


class FBAStaTaskDetailRequest(LingXingModel):
    """Request for 查询STA任务详情.
    
    POST /amzStaServer/openapi/inbound-plan/detail
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAQuerySTATaskBoxInformationRequest(LingXingModel):
    """Request for 查询STA任务包装组装箱信息.
    
    POST /amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    packingGroupIdList: List  # 包装组id
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAFBAShipmentListRequest(LingXingModel):
    """Request for 查询货件列表.
    
    POST /erp/sc/data/fba_report/shipmentList
    """
    sid: str  # 店铺id，多个以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 货件创建开始日期，格式：Y-m-d，左闭右开
    end_date: str  # 货件创建截止日期，格式：Y-m-d，左闭右开
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000
    shipment_id: Optional[str] = None  # 货件单号，多个以英文逗号隔开，仅支持精确搜索
    shipment_status: Optional[str] = None  # 货件状态，多个以英文逗号分隔： UNCONFIRMED IN_TRANSIT DELIVERED CHECKED_IN ABANDONED  DELETED CLOSED CANCELLED WORK
    extra_date_field: Optional[str] = None  # 根据start_extra_date和end_extra_date日期范围查询： update 货件修改日期【默认值为update，目前只支持查询货件修改日期】
    start_extra_date: Optional[str] = None  # 开始日期，格式：Y-m-d，左闭右开
    end_extra_date: Optional[str] = None  # 结束日期，格式：Y-m-d，左闭右开


class FBAShipmentDetailListRequest(LingXingModel):
    """Request for 查询货件详情.
    
    POST /amzStaServer/openapi/inbound-shipment/shipmentDetailList
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentIds: List  # 货件id
    sid: int  # 店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】


class FBABoxInfoRequest(LingXingModel):
    """Request for 查询货件装箱信息.
    
    POST /erp/sc/routing/fba/shipment/boxInfo
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    shipment_id: str  # 货件编号


class FBAGetFbaProductListRequest(LingXingModel):
    """Request for 查询FBA商品信息列表.
    
    POST /erp/sc/routing/fba/shipment/getFbaProductList
    """
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = None  # 模糊搜索字段：【搜索时支持以下单个字段】 msku=>MSKU fnsku=>FNSKU asin=>ASIN sku=>SKU title=>标题 product_name=>品名
    search_value: Optional[str] = None  # 搜索值【对应搜索字段的值】
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20


class FBAListShipmentBoxesRequest(LingXingModel):
    """Request for 查询货件装箱信息.
    
    POST /amzStaServer/openapi/inbound-shipment/listShipmentBoxes
    """
    inboundPlanId: str  # STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】
    shipmentIdList: List  # 货件id
    sid: int  # 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】


class FBAFBAReceivedInventoryRequest(LingXingModel):
    """Request for 查询FBA到货接收明细.
    
    POST /erp/sc/data/fba_report/receivedInventory
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    event_date: str  # 签收日期，格式：Y-m-d，未填写fba_shipment_id时必填
    fba_shipment_id: Optional[list] = None  # 货件单号，未填写event_date时必填
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class FBAShipFromAddressListRequest(LingXingModel):
    """Request for 地址簿-发货地址列表.
    
    POST /erp/sc/routing/fba/shipment/shipFromAddressList
    """
    sid: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = None  # 搜索字段： alias_name 地址簿别名 sender_name 发货方名称
    search_value: Optional[str] = None  # 对应搜索字段模糊搜索值
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class FBACreateShipFromAddressRequest(LingXingModel):
    """Request for 地址簿-发货地址创建.
    
    POST /erp/sc/routing/fba/shipment/createShipFromAddress
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    alias_name: str  # 地址簿别名，店铺内唯一
    country_name: str  # 发货国家/地区
    sender_name: str  # 发货方名称
    street_detail1: str  # 街道地址1
    street_detail2: Optional[str] = None  # 街道地址2
    city: str  # 城市
    region: Optional[str] = None  # 区
    province: str  # 省/州/地区，美国发货地址限制长度为2位
    zip_code: str  # 邮政编码
    phone: Optional[str] = None  # 电话号码


class FBAUpdateShipFromAddressRequest(LingXingModel):
    """Request for 地址簿-发货地址修改.
    
    POST /erp/sc/routing/fba/shipment/updateShipFromAddress
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    alias_name: str  # 地址簿别名，店铺内唯一
    country_name: str  # 发货国家/地区
    sender_name: str  # 发货方名称
    street_detail1: str  # 街道地址1
    street_detail2: Optional[str] = None  # 街道地址2
    city: str  # 城市
    region: Optional[str] = None  # 区
    province: str  # 省/州/地区，美国发货地址限制长度为2位
    zip_code: str  # 邮政编码
    phone: Optional[str] = None  # 电话号码
    id: int  # 地址簿-发货地址列表接口返回id


class FBAShoppingAddressRequest(LingXingModel):
    """Request for 地址簿-配送地址详情.
    
    POST /basicOpen/openapi/fbaShipment/shoppingAddress
    """
    id: int  # 唯一记录id，查询FBA列表接口对应字段【id】


class FBAVcBatchSendGoodsRequest(LingXingModel):
    """Request for VC发货单-确认发货.
    
    POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods
    """
    orderNoList: Optional[list] = None  # orderNo列表

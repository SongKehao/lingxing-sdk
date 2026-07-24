"""Request models for Warehouse APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class WarehouseDeleteFbaShipmentListRequest(LingXingModel):
    """Request for 删除发货单.

    POST /basicOpen/openapi/fbaShipment/deleteShipmentList
    """

    shipment_nos: List  # 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】


class WarehouseAwdinboundplancancelRequest(LingXingModel):
    """Request for 取消AWD入库任务.

    POST /amzStaServer/openapi/awd/inbound-plan/cancel
    """

    orderId: str  # AWD任务编号
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】


class WarehouseAwdinboundplanconfirminboundplanRequest(LingXingModel):
    """Request for 确认AWD入库任务.

    POST /amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan
    """

    orderId: str  # AWD任务编号
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】


class WarehouseAwdinboundplancreateplanRequestAwddeliveredgoodsbosItem(LingXingModel):
    boxQuantity: str  # 箱数（只能是正整数）
    expiration: Optional[str] = None  # 有效期（yyyy-MM-dd）
    height: Optional[float] = None  # 箱子高（2位小数）
    labelOwner: Optional[str] = None  # 标签类型（AMAZON,SELF）
    length: float  # 箱子长（2位小数）
    lengthUnit: Optional[str] = None  # 长度单位(INCHES-英制,CENTIMETERS-公制)
    msku: str  # msku
    prepCategory: Optional[str] = (
        None  # 预处理类别：ADULT：成人；HANGER：悬挂在衣架上的服装；TEXTILE：服装、面料、毛绒玩具和纺织品；BABY：母婴用品；FRAGILE：易碎品；LIQUID：液体（未存放在玻璃容器中）；PE
    )
    prepOwner: Optional[str] = None  # 预处理提供方（AMAZON,SELF）
    quantityInBox: str  # 单箱数量（只能是正整数）
    weight: float  # 箱子重量（2位小数）
    weightUnit: Optional[str] = None  # 重量单位（POUNDS-磅，KILOGRAMS-千克
    width: float  # 箱子宽（2位小数）


class WarehouseAwdinboundplancreateplanRequestAwdshippingaddressboItem(LingXingModel):
    addressLine1: str  # 发货地址-详细街道地址1
    addressLine2: Optional[str] = None  # 发货地址-详细街道地址2
    city: str  # 发货地址-城市
    countryCode: str  # 发货地址-国家(地区）
    phoneNumber: str  # 发货地址-电话号码
    postalCode: str  # 发货地址-邮箱编码
    shipperName: str  # 发货地址-发货方名称
    stateOrProvinceCode: str  # 发货地址-州/省/地区编码
    zone: Optional[str] = None  # 发货地址-区


class WarehouseAwdinboundplancreateplanRequest(LingXingModel):
    """Request for 创建AWD入库任务.

    POST /amzStaServer/openapi/awd/inbound-plan/createInboundPlan
    """

    destinationRegion: Optional[str] = (
        None  # 地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-sou
    )
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】
    awdDeliveredGoodsBOS: List[WarehouseAwdinboundplancreateplanRequestAwddeliveredgoodsbosItem]
    awdShippingAddressBO: WarehouseAwdinboundplancreateplanRequestAwdshippingaddressboItem


class WarehouseAwdinboundplandetailRequest(LingXingModel):
    """Request for 查询AWD入库任务详情.

    POST /amzStaServer/openapi/awd/inbound-plan/detail
    """

    orderId: str  # STA任务编号
    sid: int  # 领星店铺ID 列表，对应查询亚马逊店铺列表


class WarehouseAwdinboundplanpageRequest(LingXingModel):
    """Request for 查询AWD入库任务列表.

    POST /amzStaServer/openapi/awd/inbound-plan/page
    """

    page: int  # 分页页码
    dateType: int  # 时间类型 1:创建 2更新
    endDateTime: str  # 结束时间，格式：YYYY-MM-DD  双闭区间
    orderId: Optional[str] = None  # awd入库任务编号
    shipmentId: Optional[str] = None  # awd货件单号
    sidList: Optional[list] = None  # 店铺id列表
    length: int  # 分页大小，上限
    startDateTime: str  # 开始时间，格式：YYYY-MM-DD  双闭区间
    statusList: Optional[list] = (
        None  # 任务状态：LOCALDRAFT：草稿；DRAFT：待确认；VALIDATING：更新中；CONFIRMED：已确认；CLOSED： 已关闭；EXPIRED：已过期；CANCELLED：已取消
    )


class WarehouseAwdinboundplanupdateinboundplanRequestAwddeliveredgoodsbosItem(LingXingModel):
    boxQuantity: str  # 箱数（只能是正整数）
    expiration: Optional[str] = None  # 有效期（yyyy-MM-dd）
    height: float  # 箱子高（2位小数）
    labelOwner: Optional[str] = None  # 标签类型（AMAZON,SELF）
    length: float  # 箱子长（2位小数）
    lengthUnit: str  # 长度单位(INCHES-英制,CENTIMETERS-公制)
    msku: str  # msku
    prepCategory: Optional[str] = (
        None  # 预处理类别：ADULT：成人；HANGER：悬挂在衣架上的服装；TEXTILE：服装、面料、毛绒玩具和纺织品；BABY：母婴用品；FRAGILE：易碎品；LIQUID：液体（未存放在玻璃容器中）；PE
    )
    prepOwner: Optional[str] = None  # 预处理提供方（AMAZON,SELF）
    quantityInBox: str  # 单箱数量（只能是正整数）
    weight: float  # 箱子重量（2位小数）
    weightUnit: str  # 重量单位（POUNDS-磅，KILOGRAMS-千克）
    width: float  # 箱子宽（2位小数）


class WarehouseAwdinboundplanupdateinboundplanRequestAwdshippingaddressboItem(LingXingModel):
    addressLine1: str  # 发货地址-详细街道地址1
    addressLine2: Optional[str] = None  # 发货地址-详细街道地址2
    city: str  # 发货地址-城市
    countryCode: str  # 发货地址-国家(地区）
    phoneNumber: str  # 发货地址-电话号码
    postalCode: str  # 发货地址-邮箱编码
    shipperName: str  # 发货地址-发货方名称
    stateOrProvinceCode: str  # 发货地址-州/省/地区编码
    zone: Optional[str] = None  # 发货地址-区


class WarehouseAwdinboundplanupdateinboundplanRequest(LingXingModel):
    """Request for 更新AWD入库任务.

    POST /amzStaServer/openapi/awd/inbound-plan/updateInboundPlan
    """

    createBy: Optional[str] = None  # 创建人id，默认API账号id
    destinationRegion: Optional[str] = (
        None  # 地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-sou
    )
    orderId: str  # STA任务编号
    remark: Optional[str] = None  # 备注
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】
    awdDeliveredGoodsBOS: List[WarehouseAwdinboundplanupdateinboundplanRequestAwddeliveredgoodsbosItem]
    awdShippingAddressBO: WarehouseAwdinboundplanupdateinboundplanRequestAwdshippingaddressboItem


class WarehouseAwdinboundshipmentdetailRequest(LingXingModel):
    """Request for 查询AWD入库货件详情.

    POST /amzStaServer/openapi/awd/inbound-shipment/detail
    """

    shipmentId: str  # AWD入库货件单号
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】


class WarehouseAwdinboundshipmentpageRequest(LingXingModel):
    """Request for 查询AWD入库货件列表.

    POST /amzStaServer/openapi/awd/inbound-shipment/page
    """

    page: int  # 分页页码
    dateType: int  # 时间类型 1:创建 2更新
    endDateTime: str  # 结束时间，格式：YYYY-MM-DD  双闭区间
    shipmentId: Optional[str] = None  # 货件单号
    sidList: Optional[list] = None  # 店铺id列表
    length: int  # 分页大小，上限
    startDateTime: str  # 开始时间，格式：YYYY-MM-DD  双闭区间
    statusList: Optional[list] = (
        None  # 任务状态：CREATED：已创建；SHIPPED：已发货；IN_TRANSIT：运输中；RECEIVING：接收中；DELIVERED：已送达；CLOSED：已关闭；CANCELLED：已取消
    )


class WarehouseAwdinboundshipmentupdateshipmentinfoRequest(LingXingModel):
    """Request for 更新AWD货件跟踪编号.

    POST /amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo
    """

    orderId: str  # STA任务编号
    shipmentId: str  # 货件号
    sid: int  # 领星店铺ID 对应查询亚马逊店铺列表接口对应字段【sid】
    trackingId: str  # 跟踪编号


class WarehouseAwdinboundshipmentuploadpackingRequestShipmentidinfoItem(LingXingModel):
    pageType: str  # 纸张类型：THERMAL_NONPCP：热敏纸1个标签；THERMAL_NONPCP_01：热敏纸（152 x 108 mm）1个标签；THERMAL_NONPCP_01_WATERMARK：热敏纸（
    shipmentId: str  # 货件单号
    sid: int  # 领星店铺ID 对应查询亚马逊店铺列表接口对应字段【sid】


class WarehouseAwdinboundshipmentuploadpackingRequest(LingXingModel):
    """Request for 打印AWD入库货件箱子标签.

    POST /amzStaServer/openapi/awd/inbound-shipment/uploadPacking
    """

    shipmentIdInfo: WarehouseAwdinboundshipmentuploadpackingRequestShipmentidinfoItem


class WarehouseWarehouseListsRequest(LingXingModel):
    """Request for 查询仓库列表.

    POST /erp/sc/data/local_inventory/warehouse
    """

    type: Optional[int] = None  # 仓库类型： 1 本地仓【默认值】 3 海外仓 4 亚马逊平台仓 6 AWD仓
    sub_type: Optional[int] = None  # 海外仓子类型：  1 无API海外仓  2 有API海外仓【此参数只在type=3生效】
    is_delete: Optional[str] = None  # 是否删除，多个使用英文逗号分隔： 0 未删除【默认值】 1 已删除
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000条


class WarehouseEditWarehouseRequest(LingXingModel):
    """Request for 添加/修改仓库.

    POST /erp/sc/storage/wareHouse/edit
    """

    sys_wid: Optional[int] = None  # 领星系统仓库id，编辑时必传
    wid: Optional[str] = None  # 客户自定义仓库id【非领星系统ERP内仓库id】
    name: str  # 仓库名称
    contact: Optional[str] = None  # 负责人
    telephone: Optional[str] = None  # 联系电话
    address: Optional[str] = None  # 仓库地址
    remark: Optional[str] = None  # 备注
    type: Optional[int] = None  # 仓库属性：1 -本地仓 3 -海外自建仓，不传默认 1


class WarehouseWarehousebinRequest(LingXingModel):
    """Request for 查询本地仓位列表.

    POST /erp/sc/routing/data/local_inventory/warehouseBin
    """

    wid: Optional[str] = None  # 仓库ID，字符串id，多个使用英文逗号分隔
    id: Optional[str] = None  # 仓位ID，字符串id，多个使用英文逗号分隔
    status: Optional[str] = None  # 仓位状态： 1 禁用 2 启用
    type: Optional[str] = None  # 仓位类型： 5 可用 6 次品
    offset: Optional[int] = None  # 分页偏移量，默认为0
    limit: Optional[int] = None  # 限制条数，默认20条


class WarehouseBincreateRequest(LingXingModel):
    """Request for 添加仓位.

    POST /erp/sc/routing/storage/wareHouseBin/create
    """

    wid: int  # 仓库id
    code: str  # 仓位名称
    type: int  # 仓位类型： 5 可用 6 次品


class WarehouseSwitchstatusRequest(LingXingModel):
    """Request for 启用、禁用仓位.

    POST /erp/sc/routing/storage/wareHouseBin/switchStatus
    """

    wid: str  # 仓库id
    whbCode: str  # 仓位名称
    status: int  # 仓位状态：0 禁用，1 启用


class WarehouseOverseaWarehouseProductMatchRequest(LingXingModel):
    """Request for 海外仓sku配对.

    POST /basicOpen/overseaWarehouseSetting/productMatch
    """

    twId: int  # 三方仓id
    twpId: int  # 三方商品id
    wpId: int  # 三方服务商id
    productId: int  # 商品id
    matchNum: int  # 整箱配对数量
    matchAll: Optional[int] = None  # 是否配对海外仓所有仓库，0否；1是，默认0
    fnsku: Optional[str] = None  # fnsku
    sellerId: Optional[str] = None  # 店铺id


class WarehouseOverseaWarehouseProductUnMatchRequest(LingXingModel):
    """Request for 海外仓sku取消配对.

    POST /basicOpen/overseaWarehouseSetting/productUnMatch
    """

    wpId: str  # 三方服务商id
    wpmId: str  # 配对id


class WarehouseGetentryrecommendbinlistRequestListItem(LingXingModel):
    wid: str  # 仓库id
    productId: str  # 产品id
    fnsku: Optional[str] = None  # fnsku
    sid: Optional[str] = None  # 店铺id


class WarehouseGetentryrecommendbinlistRequest(LingXingModel):
    """Request for 查询产品仓位列表.

    POST
    """

    withHistory: Optional[bool] = None  # 是否查询历史仓位，false-否true-是;默认否
    list_field: WarehouseGetentryrecommendbinlistRequestListItem = Field(alias="list")


class WarehouseFBAStockRequest(LingXingModel):
    """Request for 查询FBA库存列表.

    POST /erp/sc/routing/fba/fbaStock/fbaList
    """

    sid: str  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class WarehouseFBAStockV2Request(LingXingModel):
    """Request for 查询FBA库存列表-v2.

    POST /basicOpen/openapi/storage/fbaWarehouseDetail
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20,取值范围[20,200]
    search_field: Optional[str] = None  # 搜索维度: sku product_name seller_sku fnsku asin parent_asin spu spu_name
    search_value: Optional[str] = None  # 搜索值
    cid: Optional[str] = None  # 分类
    sid: Optional[str] = None  # 店铺id（支持多个，使用,分隔）
    bid: Optional[str] = None  # 品牌
    attribute: Optional[str] = None  # 属性
    asin_principal: Optional[str] = None  # Listing负责人uid，对应查询ERP用户信息列表uid字段 多个使用,分隔
    status: Optional[str] = None  # 在售状态: 0 停售 1 在售
    senior_search_list: Optional[str] = None  # 高级搜索列表，详情见附加说明
    fulfillment_channel_type: Optional[str] = None  # 配送方式: FBA FBM
    is_hide_zero_stock: Optional[str] = None  # 是否隐藏零库存行: 0 不隐藏零库存行 1 隐藏零库存行
    is_parant_asin_merge: Optional[str] = None  # 是否合并父ASIN: 0 不合并父ASIN 1 合并父ASIN
    is_contain_del_ls: Optional[str] = None  # 是否显示已删除Listing: 0 不显示已删除Listing 1 显示已删除Listing
    query_fba_storage_quantity_list: Optional[bool] = (
        None  # true 是、false 否；默认false，如果传入true,则出参数据中的欧洲共享仓会将出参字段-fba_storage_quantity_list的值返回
    )


class WarehouseAwdWarehouseDetailRequest(LingXingModel):
    """Request for 查询AWD库存列表.

    POST
    """

    wids: Optional[str] = None  # 仓库ID列表，使用逗号分隔
    cid: Optional[str] = None  # 分类ID列表，使用逗号分隔
    bid: Optional[str] = None  # 品牌ID列表，使用逗号分隔
    attribute: Optional[int] = None  # 属性值
    asin_principal: Optional[str] = None  # ASIN负责人UID列表，使用逗号分隔      * 0、负责人为空
    search_field: str  # 搜索字段，指定进行搜索的列      * sku      * product_name      * seller_sku      * fnsku      * asin      * paren
    search_value: Optional[str] = None  # 搜索值
    status: Optional[str] = None  # 状态列表，使用逗号分隔      * 0、停售      * 1、在售
    is_hide_zero_stock: Optional[float] = None  # 是否隐藏零库存      * 0、不隐藏      * 1、隐藏
    offset: Optional[float] = None  # 分页偏移量
    length___200: Optional[float] = None  # 分页长度


class WarehouseInventoryDetailsRequest(LingXingModel):
    """Request for 查询仓库库存明细.

    POST /erp/sc/routing/data/local_inventory/inventoryDetails
    """

    wid: Optional[str] = None  # 仓库id，多个使用英文逗号分隔
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限800
    sku: Optional[str] = None  # SKU，单个,（模糊搜索）


class WarehouseInventorybindetailsRequest(LingXingModel):
    """Request for 查询仓位库存明细.

    POST /erp/sc/routing/data/local_inventory/inventoryBinDetails
    """

    wid: Optional[str] = None  # 仓库id，多个仓库用英文逗号分隔，默认所有仓库
    bin_type_list: Optional[str] = (
        None  # 仓位类型，多个类型用英文逗号分隔： 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品
    )
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20 ，上限500


class WarehouseGetBatchDetailListRequest(LingXingModel):
    """Request for 查询批次明细.

    POST /erp/sc/routing/data/local_inventory/getBatchDetailList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限400
    show_zero_stock: Optional[int] = None  # 是否显示0库存信息：0 不显示，1 显示
    wids: Optional[str] = None  # 仓库id，多个使用英文逗号分隔
    stock_in_type_list: Optional[str] = (
        None  # 入库类型，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 26 退货入库 27 移除入库 45
    )
    search_field: Optional[str] = (
        None  # 搜索字段： sku SKU msku MSKU fnsku FNSKU order_sn 单据号 product_name 品名 batch_number 批次号 receipt_order 收货单
    )
    search_value: Optional[str] = None  # 搜索值


class WarehouseGetBatchStatementListRequest(LingXingModel):
    """Request for 查询批次流水.

    POST /erp/sc/routing/data/local_inventory/getBatchStatementList
    """

    statement_type_list: Optional[str] = (
        None  # 批次流水主类型id，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 47 VC-PO出库 48
    )
    search_field: Optional[str] = (
        None  # 搜索字段： sku SKU msku MSKU fnsku FNSKU product_name 品名 purchase_plan 采购计划 purchase_order 采购单 receipt_or
    )
    search_value: Optional[str] = None  # 搜索值
    wid_list: Optional[str] = None  # 仓库id，多个使用英文逗号分隔
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限400


class WarehouseWarehouseStatementRequest(LingXingModel):
    """Request for 查询库存流水（旧）.

    POST /erp/sc/routing/data/local_inventory/wareHouseStatement
    """

    wid: Optional[str] = None  # 仓库ID，多个仓库ID用英文逗号分隔，不填默认所有仓库
    type: Optional[str] = (
        None  # 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】  1 其他入库 2 采购入库 3 调拨入库 10 其它入库（已撤销） 11 其他出库 12 FBA出库 13 调拨出库 14 退货出库 15
    )
    start_date: Optional[str] = None  # 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用
    end_date: Optional[str] = None  # 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class WarehouseWarehouseStatementNewRequest(LingXingModel):
    """Request for 查询库存流水（新）.

    POST /erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement
    """

    wids: Optional[str] = None  # 仓库id，多个使用英文逗号分隔
    types: Optional[str] = (
        None  # 流水类型，多个使用英文逗号分隔：【不填默认全部类型】 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 15 FBM退货  16 换标入库 17 加工入库 18 拆分入库
    )
    sub_types: Optional[str] = (
        None  # 子类流水类型，多个使用英文逗号分隔：【不填默认全部类型】 1901 其他入库 手工其他入库 1902 其他入库 用户初始化 1903 其他入库 系统初始化 2201 采购入库 手工采购入库 2202
    )
    start_date: Optional[str] = None  # 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用
    end_date: Optional[str] = None  # 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20


class WarehouseWarehousebinstatementRequest(LingXingModel):
    """Request for 查询仓位流水.

    POST /erp/sc/routing/data/local_inventory/wareHouseBinStatement
    """

    wid: Optional[str] = None  # 仓库ID，多个仓库ID用英文逗号,分隔，传或者传空则默认所有仓库
    type: Optional[str] = (
        None  # 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】 16 换标入库 17 加工入库 18 拆分入库 19 其他入库 22 采购入库 23 委外入库 24 调拨入库 25 盘盈入库 26 退货入
    )
    bin_type_list: Optional[str] = (
        None  # 仓位类型：【多个类型用逗号分隔】 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品
    )
    start_date: Optional[str] = None  # 操作开始时间，Y-m-d，闭区间，联合结束时间使用
    end_date: Optional[str] = None  # 操作结束时间，Y-m-d，开区间，联合开始时间使用
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class WarehousePurchaseReceiptOrderListRequest(LingXingModel):
    """Request for 查询收货单列表.

    POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList
    """

    date_type: Optional[int] = None  # 查询时间类型：1 预计到货时间，2 收货时间，3 创建时间，4 更新时间
    start_date: Optional[str] = None  # 开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    end_date: Optional[str] = None  # 结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    order_sns: Optional[str] = None  # 收货单号，多个使用英文逗号分隔
    status: Optional[int] = None  # 状态：10 待收货，40 已完成
    wid: Optional[str] = None  # 仓库id，多个使用英文逗号分隔
    order_type: Optional[int] = None  # 收货类型：1 采购订单，2 委外订单
    qc_status: Optional[str] = None  # 质检状态，多个使用英文逗号分隔：0 未质检，1 部分质检，2 完成质检
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认200，上限500


class WarehouseCreatereceiptorderRequestListItem(LingXingModel):
    business_order_sn: str  # 业务单号
    wid: int  # 仓库id
    order_type: int  # 订单类型：1 采购单，2 委外订单
    expect_arrival_time: str  # 期望收货时间
    logistics_company: str  # 物流商
    logistics_order_no: str  # 物流单号
    shipping_cost: float  # 物流费用
    other_fee: float  # 其他费用
    remark: str  # 备注
    item_list: List  # 收货明细
    item_list__order_item_id: int  # 采购单子项id，查询采购单列表接口对应字段【id】
    item_list__notice_num_total: int  # 通知收货量
    item_list__remark: str  # 备注


class WarehouseCreatereceiptorderRequest(LingXingModel):
    """Request for 创建待收货的收货单.

    POST
    """

    list_field: List[WarehouseCreatereceiptorderRequestListItem] = Field(alias="list")


class WarehouseReceiveRequestItemListItem(LingXingModel):
    id: int  # 收货单子项id，查询收货单列表接口对应字段【item_id】
    product_receive_num: int  # 收货量，收货量必须大于0
    remark: Optional[str] = None  # 备注，最大支持255个字符，不传时默认取自收货单


class WarehouseReceiveRequest(LingXingModel):
    """Request for 收货单到货.

    POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive
    """

    order_sn: str  # 收货单号
    expect_arrival_time: Optional[str] = None  # 预计收货时间，不传时默认取自收货单
    custom_receive_time: Optional[str] = None  # 自定义收货时间，  自定义日期须早于请求当天日期
    logistics_company: Optional[str] = None  # 物流商，不传时默认取自收货单
    logistics_order_no: Optional[str] = None  # 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单
    shipping_cost: Optional[float] = None  # 运费，仅支持2位小数，不传时默认取自收货单
    other_fee: Optional[float] = None  # 其他费用，仅支持2位小数，不传时默认取自收货单
    remark: Optional[str] = None  # 备注，最大支持255个字符，不传时默认取自收货单
    item_list: List[WarehouseReceiveRequestItemListItem]


class WarehouseFastReceiveRequestItemListItem(LingXingModel):
    id: int  # 收货单子项id，查询收货单列表接口对应字段【item_id】
    product_good_num: int  # 良品量，总良品量+总次品量必须大于0
    product_bad_num: int  # 次品量，总良品量+总次品量必须大于0
    remark: Optional[str] = None  # 备注，最大支持255个字符，不传时默认取自收货单


class WarehouseFastReceiveRequest(LingXingModel):
    """Request for 收货单快捷入库.

    POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive
    """

    order_sn: str  # 收货单号
    expect_arrival_time: Optional[str] = None  # 预计收货时间，不传时默认取自收货单
    custom_receive_time: Optional[str] = None  # 自定义收货时间，  自定义日期须早于请求当天日期
    logistics_company: Optional[str] = None  # 物流商，不传时默认取自收货单
    logistics_order_no: Optional[str] = None  # 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单
    shipping_cost: Optional[float] = None  # 运费，仅支持2位小数，不传时默认取自收货单
    other_fee: Optional[float] = None  # 其他费用，仅支持2位小数，不传时默认取自收货单
    remark: Optional[str] = None  # 备注，最大支持255个字符，不传时默认取自收货单
    item_list: List[WarehouseFastReceiveRequestItemListItem]


class WarehouseReturnListRequest(LingXingModel):
    """Request for 查询销售退货单列表.

    POST /pb/mp/returns/v2/list
    """

    offset: int  # 页码，非偏移量 offset传1，则返回第一页数据
    length: int  # 每页记录数
    time_type: Optional[str] = None  # 搜索时间类型：updateTime 更新时间【不传默认为创建时间】
    start_time: str  # 开始时间，格式：Y-m-d H:i:s
    end_time: str  # 结束时间，格式：Y-m-d H:i:s
    platform_code: Optional[list] = None  # 平台code
    sales_type: Optional[int] = None  # 退货类型：1 买家退货，2 物流商退货
    status: Optional[list] = None  # 订单状态： -1 异常 1 待提交 2 待审批 3 待收货 4 已作废 5 已完成 6 导入中
    store_id: Optional[list] = None  # 店铺id
    wid: Optional[list] = None  # 系统仓库id


class WarehouseReceiptOrderQcListRequest(LingXingModel):
    """Request for 查询质检单列表.

    POST
    """

    date_type: Optional[int] = None  # 查询时间类型：1 质检时间，2 收货时间，3 创建时间
    start_date: Optional[str] = None  # 开始时间
    end_date: Optional[str] = None  # 结束时间
    qc_sns: Optional[str] = None  # 质检单号，多个使用英文逗号分隔
    status: Optional[str] = (
        None  # 状态，多个使用英文逗号分隔： 0 待质检 1 已质检 2 已免检 10 已质检（撤销） 20 已免检（撤销）
    )
    wid: Optional[str] = None  # 仓库id，多个用英文逗号分隔
    offset: Optional[int] = None  # 分页偏移量，默认为0
    length: Optional[int] = None  # 分页长度，默认为200，上限500


class WarehouseReturnorderfaststorageinRequestReqsItem(LingXingModel):
    rmaOrderNo: str  # 退货单号
    storeId: str  # 店铺ID
    wid: str  # 退货仓库
    itemReqs__id: str  # 退货商品行id
    itemReqs__picIds: Optional[list] = None  # 售后图片
    itemReqs__picIds__accessUrl: Optional[str] = None  # 访问地址
    itemReqs__picIds__fileName: Optional[str] = None  # 图片名
    itemReqs__picIds__mappingKey: Optional[str] = None  # 映射键
    itemReqs__availableQuantity: float  # 可用量
    itemReqs__availableWhbCode: str  # 可用仓位编码
    itemReqs__defectiveQuantity: float  # 次品量
    itemReqs__defectiveWhbCode: str  # 次品仓位编码
    itemReqs__destroyedQuantity: float  # 销毁量


class WarehouseReturnorderfaststorageinRequest(LingXingModel):
    """Request for 待收货退货单快捷入库.

    POST
    """

    reqs: WarehouseReturnorderfaststorageinRequestReqsItem


class WarehouseOrderAddRequestProductListItem(LingXingModel):
    sku: str  # sku
    good_num: int  # 良品数量
    bad_num: int  # 次品数量
    price: str  # 单价
    seller_id: int  # 店铺id【没有店铺时传0】 亚马逊店铺对应查询亚马逊店铺信息字段【sid】 多平台店铺对应查询多平台店铺信息字段【store_id】
    fnsku: str  # fnsku【存在fnsku时店铺id必填，没有时传空字符串】
    good_whb_code: Optional[str] = None  # 可用仓位
    bad_whb_code: Optional[str] = None  # 次品仓位


class WarehouseOrderAddRequest(LingXingModel):
    """Request for 添加入库单.

    POST /erp/sc/routing/storage/storage/orderAdd
    """

    wid: Optional[str] = None  # 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid
    sys_wid: int  # 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid
    type: int  # 单据类型： 1 其他入库 2 采购入库 26 退货入库 27 移除入库
    supplier_id: Optional[str] = (
        None  # 自定义供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】
    )
    sys_supplier_id: Optional[int] = (
        None  # 系统供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】
    )
    order_sn: Optional[str] = None  # 采购单号【对此采购单执行快捷入库】，不支持自定义采购单号
    remark: Optional[str] = None  # 单据备注
    ship_fee: Optional[str] = None  # 运费
    other_fee: Optional[str] = None  # 其它费用
    fee_part_type: Optional[int] = None  # 费用分配方式: 0 不分摊 1 按金额 2 按数量
    inbound_time: Optional[str] = None  # 自定义入库时间，格式：Y-m-d
    inbound_idempotent_code: Optional[str] = None  # （入库单）客户参考号, 该字段校验唯一不可重复
    product_list: List[WarehouseOrderAddRequestProductListItem]


class WarehouseInboundgetordersRequest(LingXingModel):
    """Request for 查询入库单列表.

    POST /erp/sc/routing/storage/inbound/getOrders
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    wid: Optional[int] = None  # 系统仓库id
    search_field_time: Optional[str] = (
        None  # 日期筛选类型： 创建时间 create_time 入库时间 opt_time 更新时间 increment_time
    )
    start_date: Optional[str] = None  # 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    end_date: Optional[str] = None  # 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    order_sn: Optional[str] = None  # 入库单单号，多个使用英文逗号分隔
    inbound_idempotent_code: Optional[str] = None  # 客户参考单号，多个使用英文逗号分隔
    status: Optional[int] = None  # 入库单状态： 10 待提交 20 待入库 40 已完成 50 已撤销 121 待审批 122 已驳回
    type: Optional[int] = (
        None  # 入库类型： -1 其他入库（含所有自定义类型）  1 其他入库（非自定义类型） 2 采购入库 3 调拨入库 4 赠品入库 26 退货入库 27 移除入库
    )


class WarehouseSetInboundOrderRevokeRequest(LingXingModel):
    """Request for 撤销入库单.

    POST /basicOpen/inboundOrder/inbound/setOrderRevoke
    """

    order_sn: str  # 入库单号 对应查询入库单列表data>>order_sn字段
    delete_receipt_order: Optional[int] = None  # 是否同步删除收货单  删除则传值 1，否则不传值


class WarehouseOrderAddOutRequestProductListItem(LingXingModel):
    sku: str  # sku
    good_num: int  # 良品数量
    bad_num: int  # 次品数量
    seller_id: int  # 店铺id【没有店铺时传0】 亚马逊店铺对应查询亚马逊店铺信息字段【sid】 多平台店铺对应查询多平台店铺信息字段【store_id】
    fnsku: str  # fnsku【存在fnsku时店铺id必填，没有时传空字符串】
    out_available_bin: Optional[list] = None  # 可用出库仓位列表
    out_available_bin__whb_code: Optional[str] = None  # 可用出库仓位编码
    out_available_bin__whb_num: Optional[int] = None  # 可用出库仓位数量
    out_inferior_bin: Optional[list] = None  # 次品出库仓位列表
    out_inferior_bin__whb_code: Optional[str] = None  # 次品出库仓位编码
    out_inferior_bin__whb_num: Optional[int] = None  # 次品出库仓位数量


class WarehouseOrderAddOutRequest(LingXingModel):
    """Request for 添加出库单.

    POST /erp/sc/routing/storage/storage/orderAddOut
    """

    wid: Optional[str] = None  # 自定义仓库ID，wid和sys_wid其中一项必填，都填则优先wid
    sys_wid: int  # 系统仓库ID，sys_wid和wid其中一项必填，都填则优先wid
    type: int  # 单据类型： 11 其他出库 12 FBA出库 14 退货出库 18 销毁出库
    status: Optional[int] = None  # 新建单据状态： 10：待提交 30：待出库 40：已完成【默认值】
    sys_supplier_id: Optional[int] = (
        None  # 系统客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）
    )
    supplier_id: Optional[str] = (
        None  # 客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）
    )
    idempotent_code: Optional[str] = None  # 客户参考号, 该字段校验唯一不可重复
    remark: Optional[str] = None  # 单据备注
    return_price: Optional[float] = None  # 退货费（退货出库）
    other_fee: Optional[float] = None  # 其它费用（退货出库）
    sys_to_wid: Optional[int] = None  # 系统客户目的仓库ID（非退货出库）
    to_wid: Optional[str] = None  # 客户目的仓库ID（非退货出库）
    outbound_time: Optional[str] = None  # 自定义出库时间，格式：Y-m-d
    bin_type: Optional[int] = None  # 出库仓位指定方式： 0 系统指定仓位【默认值】 1 手动指定仓位
    product_list: List[WarehouseOrderAddOutRequestProductListItem]


class WarehouseOutboundgetordersRequest(LingXingModel):
    """Request for 查询出库单列表.

    POST /erp/sc/routing/storage/outbound/getOrders
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    wid: Optional[str] = None  # 系统仓库id
    search_field_time: Optional[str] = (
        None  # 日期筛选类型： 创建时间 create_time 出库时间 opt_time 更新时间 increment_time
    )
    start_date: Optional[str] = None  # 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    end_date: Optional[str] = None  # 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    order_sn: Optional[str] = None  # 出库单单号，多个使用英文逗号分隔
    idempotent_code: Optional[str] = None  # 客户参考号，多个使用英文逗号分隔
    status: Optional[int] = None  # 出库单状态： 10 待提交 30 待出库 40 已完成 50 已撤销 121 待审批 122 已驳回
    type: Optional[int] = (
        None  # 出库类型： 11 其他出库 12 FBA出库 14 退货出库 15 调拨出库 16 WFS出库 17 Temu出库 18 销毁出库
    )


class WarehouseWmsOrderDetailRequest(LingXingModel):
    """Request for 查询销售出库单详情.

    POST /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers
    """

    isPrintCenter: Optional[int] = None  # 是否需要拣货信息，枚举值：1-是, 0-否
    orderNumbers: Optional[str] = None  # 系统单号，必填，多个以逗号连接


class WarehouseSetOutboundOrderRevokeRequest(LingXingModel):
    """Request for 撤销出库单.

    POST /basicOpen/outboundOrder/outbound/setOrderRevoke
    """

    order_sn: str  # 出库单号 对应查询出库单列表data>>order_sn字段


class WarehouseAddstorageprocessorderRequestProductListItem(LingXingModel):
    combo_sku: str  # 组合品sku
    combo_sid: int  # 组合品店铺id，没有传0即可
    combo_fnsku: Optional[str] = None  # 组合品fnsku
    quantity_num: int  # 加工量 / 拆分量
    combo_whb_code: Optional[str] = (
        None  # 加工单组合品入库仓位，不传默认暂存可用；拆分单不用传 【查询本地仓位列表 接口对应字段【storage_bin】】
    )
    process_fee: Optional[float] = None  # 加工费【默认0】；加工单专有，拆分单可不传
    single_product_list: List  # 单品明细项
    single_product_list__sku: str  # 单品sku
    single_product_list__fnsku: Optional[str] = None  # 单品fnsku
    single_product_list__sid: int  # 单品店铺id，组合品店铺id为0时此字段值传0
    single_product_list__price_scale: float  # 单品拆分比例
    single_product_list__whb_code: Optional[str] = (
        None  # 拆分单的单品入库仓位，不传默认可用暂存；加工单不用传 【查询本地仓位列表 接口对应字段【storage_bin】】
    )
    single_product_list__remark: Optional[str] = None  # remark


class WarehouseAddstorageprocessorderRequest(LingXingModel):
    """Request for 创建加工单 / 拆分单.

    POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder
    """

    type: int  # 单据类型：1 加工单，2 拆分单
    wid: int  # 系统仓库id
    remark: Optional[str] = None  # 备注
    product_list: List[WarehouseAddstorageprocessorderRequestProductListItem]


class WarehouseGetprocessorderlistsRequest(LingXingModel):
    """Request for 加工单列表.

    POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists
    """

    type: Optional[Any] = None  # 单据类型：1加工单，2拆分单
    wid: Optional[Any] = None  # 仓库id，多个用英文逗号分隔
    process_sn: Optional[Any] = None  # 加工单号，多个用英文逗号分隔
    status: Optional[Any] = None  # 加工状态： 0 待配货 1 待完成 2 已完成
    search_field_time: Optional[Any] = (
        None  # 时间搜索维度： create_time 创建时间 finish_time 完成时间 update_time 更新时间
    )
    start_date: Optional[Any] = None  # 开始时间，格式：Y-m-d
    end_date: Optional[Any] = None  # 结束时间，格式：Y-m-d
    offset: Optional[Any] = None  # 分页偏移量，默认0
    length: Optional[Any] = None  # 分页长度，默认500


class WarehouseGetstorageallocationlistRequest(LingXingModel):
    """Request for 查询调拨单列表.

    POST /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList
    """

    wid: Optional[str] = None  # 出库仓库id，多个以英文逗号分隔
    to_wid: Optional[str] = None  # 入库仓库id，多个以英文逗号分隔
    search_date_type: Optional[int] = (
        None  # 时间类型：【不传或传空则默认为 1】 1 创建时间 2 调拨时间 3 完成时间 4 更新时间
    )
    start_date: Optional[str] = None  # 开始日期，格式：Y-m-d，只有和结束日期同时有值才会生效
    end_date: Optional[str] = None  # 结束日期，格式：Y-m-d，只有和开始日期同时有值才会生效
    page: Optional[int] = None  # 当前页码，默认1
    page_size: Optional[int] = None  # 分页条数，默认15


class WarehouseAddAllocationOrderRequestProductListItem(LingXingModel):
    sku: str  # sku
    seller_id: Optional[int] = None  # 店铺id，不传默认0【对应查询亚马逊店铺信息接口字段sid】
    fnsku: Optional[str] = None  # fnsku，不传默认为空
    good_num: Optional[int] = None  # 可用调拨量，和次品调拨量其中一项必填
    bad_num: Optional[int] = None  # 次品调拨量，和可用调拨量其中一项必填
    cg_package_length: Optional[str] = None  # 包装规格-长（CM），不传或者传空则取产品管理的值
    cg_package_width: Optional[str] = None  # 包装规格-宽（CM），不传或者传空则取产品管理的值
    cg_package_height: Optional[str] = None  # 包装规格-高（CM），不传或者传空则取产品管理的值
    cg_product_gross_weight: Optional[str] = None  # 单品净重，不传或者传空则取产品管理的值
    freight_fee_unit: Optional[str] = None  # 单位运费，若费用分摊方式为5-自定义则必填，其他则该字段无效
    other_fee_unit: Optional[str] = None  # 单位其他费用，若费用分摊方式为5-自定义则必填，其他则该字段无效
    product_remark: Optional[str] = None  # 明细备注，最大长度为255个字符


class WarehouseAddAllocationOrderRequestOutAvailableBinItem(LingXingModel):
    whb_code: Optional[str] = None  # 出库可用仓位编码
    num: Optional[str] = None  # 出库可用仓位调拨量


class WarehouseAddAllocationOrderRequestOutInferiorBinItem(LingXingModel):
    whb_code: Optional[str] = None  # 出库次品仓位编码
    num: Optional[str] = None  # 出库次品仓位数量


class WarehouseAddAllocationOrderRequestToAvailableBinItem(LingXingModel):
    whb_code: Optional[str] = None  # 入库可用仓位编码
    num: Optional[str] = None  # 入库可用仓位数量


class WarehouseAddAllocationOrderRequestToInferiorBinItem(LingXingModel):
    whb_code: Optional[str] = None  # 入库次品仓位编码
    num: Optional[str] = None  # 入库次品仓位数量


class WarehouseAddAllocationOrderRequest(LingXingModel):
    """Request for 创建待收货/已完成的调拨单.

    POST /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder
    """

    wid: Optional[int] = None  # 客户出库仓库id（与系统仓库出库id任一必填，优先取客户出库仓库id）
    sys_wid: Optional[int] = None  # 系统仓库出库id（与客户仓库出库id任一必填，优先取客户出库仓库id）
    to_wid: Optional[int] = None  # 客户入库仓库id（与系统仓库入库id任一必填，优先取客户入库仓库id）
    sys_to_wid: Optional[int] = None  # 系统仓库入库id（与客户仓库入库id任一必填，优先取客户入库仓库id）
    freight_fee: Optional[str] = None  # 运费
    other_fee: Optional[str] = None  # 其他费用
    fee_part_type: Optional[int] = None  # 费用分摊方式：【默认0】 0 不分摊 2 按sku数量分摊 3 按重量 4 按体积 5 按自定义
    remark: Optional[str] = None  # 备注
    type: Optional[int] = (
        None  # 调拨类型：【默认1】 1 简易调拨【创建已完成状态的单据】 2 完整调拨【创建待收货状态的单据】
    )
    predict_time: Optional[str] = None  # 预计到货时间，格式：Y-m-d
    out_bin_type: Optional[str] = None  # 0 默认  1 出库仓位不为空时，必传
    product_list: WarehouseAddAllocationOrderRequestProductListItem
    out_available_bin: Optional[List[WarehouseAddAllocationOrderRequestOutAvailableBinItem]] = None
    out_inferior_bin: Optional[List[WarehouseAddAllocationOrderRequestOutInferiorBinItem]] = None
    to_available_bin: Optional[List[WarehouseAddAllocationOrderRequestToAvailableBinItem]] = None
    to_inferior_bin: Optional[List[WarehouseAddAllocationOrderRequestToInferiorBinItem]] = None


class WarehouseReceiveallocationorderRequest(LingXingModel):
    """Request for 调拨单全部收货.

    POST /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder
    """

    orderSnMany: str  # 调拨单号，支持多个，英文逗号分隔


class WarehousePartlyreceiveallocationorderRequestProductListItem(LingXingModel):
    product_id: int  # 产品id
    seller_id: Optional[str] = None  # 店铺id，不传或者传空则默认为0 ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    fnsku: Optional[str] = None  # fnsku，不传则默认为空
    received_good_num: Optional[int] = None  # 本次收货可用收货量，和本次次品收货次品收货量其中一项必填且大于0
    received_bad_num: Optional[int] = None  # 本次收货次品收货量，和本次可用收货次品收货量其中一项必填且大于0


class WarehousePartlyreceiveallocationorderRequest(LingXingModel):
    """Request for 调拨单分批收货.

    POST
    """

    order_sn: str  # 调拨单单号
    product_list: List[WarehousePartlyreceiveallocationorderRequestProductListItem]


class WarehouseFinishreceiveallocationorderRequest(LingXingModel):
    """Request for 调拨单结束到货.

    POST
    """

    order_sn: str  # 调拨单单号


class WarehouseDeleteStorageAllocationListRequest(LingXingModel):
    """Request for 删除调拨单.

    POST /basicOpen/storageAllocationList/delete
    """

    orderSn: List  # 调拨单单号，对应查询调拨单列表接口字段【order_sn】


class WarehouseCancelStorageAllocationListRequest(LingXingModel):
    """Request for 撤销调拨单.

    POST /basicOpen/storageAllocationList/cancel
    """

    order_sn: str  # 调拨单号 对应查询调拨单列表data>>order_sn字段


class WarehouseGetstorageadjustorderlistRequest(LingXingModel):
    """Request for 查询调整单列表.

    POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList
    """

    search_date_type: Optional[int] = None  # 时间类型： 1 创建时间 2 调整时间 3 更新时间
    start_date: Optional[str] = None  # 开始日期，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期，格式：Y-m-d
    order_sn: Optional[str] = None  # 调整单号，多个使用英文逗号分隔
    adjust_status: Optional[int] = None  # 单据状态： 5 待提交 10 待调整 20 已完成 30 已删除 121 待审批 122 已驳回
    wid: Optional[str] = None  # 系统仓库id，多个使用英文逗号分隔
    type: Optional[int] = None  # 调整类型： 0 数量调整 1 换标调整 2 sku调整
    page: Optional[int] = None  # 当前页码，默认1
    page_size: Optional[int] = None  # 分页条数，默认20


class WarehouseAddadjustmentorderRequestProductListItem(LingXingModel):
    adjustment_valid_num: int  # 可用调整数量，不调整则传0，但不能与次品调整数量同时为0
    adjustment_bad_num: int  # 次品调整数量，不调整则传0，但不能与可用调整数量同时为0
    adjustment_available_bin: str  # 可用仓位编号，为空则默认可用暂存
    adjustment_inferior_bin: str  # 次品仓位编号，为空则默认为次品暂存
    adjustment_valid_sgn: str  # 可用增加标志符号，增加时+  ，减少是-
    adjustment_bad_sgn: str  # 次品增加标志符号，增加时+  ，减少是-
    sku: str  # sku
    fnsku: str  # fnsku，没有可以为空
    product_id: int  # 产品id
    seller_id: int  # 店铺id，默认为0 ,对应查询亚马逊店铺列表接口对应字段【seller_id】


class WarehouseAddadjustmentorderRequest(LingXingModel):
    """Request for 创建已完成的数量调整单.

    POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder
    """

    wid: int  # 系统仓库id
    remark: Optional[str] = None  # 单据备注
    product_list: List[WarehouseAddadjustmentorderRequestProductListItem]


class WarehouseAddrebrandadjustmentorderRequestProductListItem(LingXingModel):
    product_id: int  # 产品id
    seller_id: Optional[str] = None  # 原店铺id，默认为0 ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    fnsku: Optional[str] = None  # 原FNSKU，默认为空
    to_seller_id: Optional[int] = None  # 新店铺id，默认为0
    to_fnsku: Optional[str] = None  # 新FNSKU，默认空
    adjustment_valid_num: int  # 调整量
    product_remark: Optional[str] = None  # 产品备注
    out_available_bin: Optional[list] = None  # 出库仓位列表，默认可用暂存【仅当bin_type = 2 生效】
    out_available_bin__whb_code: Optional[str] = None  # 出库仓位
    out_available_bin__num: Optional[int] = (
        None  # 出库数量，默认按ERP页面逻辑出库 【out_available_bin>>num 之和 等于 adjustment_valid_num】
    )
    in_available_bin: Optional[list] = None  # 入库仓位列表，默认可用暂存
    in_available_bin__whb_code: Optional[str] = None  # 入库仓位
    in_available_bin__num: Optional[int] = (
        None  # 入库数量，当填写入库仓位时，该字段必填 【in_available_bin>>num 之和 等于 adjustment_valid_num】
    )


class WarehouseAddrebrandadjustmentorderRequest(LingXingModel):
    """Request for 创建已完成的换标调整单.

    POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder
    """

    wid: int  # 系统仓库id
    remark: Optional[str] = None  # 单据备注
    bin_type: Optional[int] = None  # 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位
    product_list: List[WarehouseAddrebrandadjustmentorderRequestProductListItem]


class WarehouseAddskuadjustmentorderRequestProductListItem(LingXingModel):
    product_id: int  # 产品id
    seller_id: Optional[str] = None  # 原店铺id，默认为0 ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    fnsku: Optional[str] = None  # 原FNSKU，默认为空
    to_product_id: str  # 新产品id
    to_seller_id: Optional[int] = None  # 新店铺id，默认为0
    to_fnsku: Optional[str] = None  # 新FNSKU，默认空
    adjustment_valid_num: int  # 调整量
    product_remark: Optional[str] = None  # 产品备注
    out_available_bin: Optional[list] = None  # 出库仓位列表，默认可用暂存【仅当bin_type = 2 生效】
    out_available_bin__whb_code: Optional[str] = None  # 出库仓位
    out_available_bin__num: Optional[int] = (
        None  # 出库数量，默认按ERP页面逻辑出库 【out_available_bin>>num 之和 等于 adjustment_valid_num】
    )
    in_available_bin: Optional[list] = None  # 入库仓位列表，默认可用暂存
    in_available_bin__whb_code: Optional[str] = None  # 入库仓位
    in_available_bin__num: Optional[int] = (
        None  # 入库数量，当填写入库仓位时，该字段必填 【in_available_bin>>num 之和 等于 adjustment_valid_num】
    )


class WarehouseAddskuadjustmentorderRequest(LingXingModel):
    """Request for 创建已完成的SKU调整单.

    POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder
    """

    wid: int  # 系统仓库id
    remark: Optional[str] = None  # 单据备注
    bin_type: Optional[int] = None  # 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位
    product_list: List[WarehouseAddskuadjustmentorderRequestProductListItem]


class WarehouseCheckgetorderlistRequest(LingXingModel):
    """Request for 查询盘点单列表.

    POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList
    """

    wid: Optional[str] = None  # 盘点仓库id，多个使用英文逗号分隔
    check_type: Optional[str] = (
        None  # 盘点类型，多个盘点类型用英文逗号分隔： 1 整仓盘点 2 SKU盘点 3 仓位盘点 4 SKU+仓位盘点
    )
    date_field: Optional[str] = None  # 搜索时间类型： create_date 创建时间【默认值】 check_date 盘点时间
    start_date: Optional[str] = None  # 开始日期，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索字段： order_sn 盘点单号 create_user 创建人 check_user 盘点人 remark 备注
    search_value: Optional[str] = None  # 搜索值
    status: Optional[int] = (
        None  # 盘点状态： 10 待盘点 20 预锁 30 盘点中 40 已盘点 121 待审核 122 已驳回 123 通过 124 作废
    )
    page: Optional[int] = None  # 分页页码，默认1
    page_size: Optional[int] = None  # 分页长度，默认20


class WarehouseCheckgetorderdetailRequest(LingXingModel):
    """Request for 查询盘点单详情.

    POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail
    """

    order_sn: str  # 盘点单号
    search_field: Optional[str] = (
        None  # 搜索字段： sku SKU fnsku FNSKU product_name 品名 whb_code_text 仓位 whb_type_text 仓位类型
    )
    search_value: Optional[str] = None  # 搜索值
    sort_field: Optional[str] = (
        None  # 排序字段： book_inventory 账面库存 actual_inventory 实盘库存 different_count 库存差异
    )
    sort_type: Optional[str] = None  # 排序规则：desc 降序【默认】，asc 升序
    page: Optional[int] = None  # 分页页码，默认1【控制 product_list 返回数目】
    page_size: Optional[int] = None  # 分页长度，默认20【控制 product_list 返回数目】


class WarehouseCheckaddorderRequestProductListItem(LingXingModel):
    product_id: int  # 本地产品id
    seller_id: Optional[str] = None  # 店铺id，传空或者不传则默认0 ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    fnsku: Optional[str] = None  # FNSKU，不传则默认空
    whb_code: Optional[str] = None  # 仓位，传空或者不传则默认可用暂存
    actual_inventory: int  # 实盘库存
    remark: Optional[str] = None  # 盘点明细备注


class WarehouseCheckaddorderRequest(LingXingModel):
    """Request for 创建已完成的盘点单.

    POST /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder
    """

    wid: int  # 盘点仓库id,对应领星系统的仓库id
    is_display_check: int  # 是否明盘：0 否，1 是【默认值】
    check_uid: int  # 盘点人id
    remark: Optional[str] = None  # 单据备注
    product_list: List[WarehouseCheckaddorderRequestProductListItem]


class WarehouseSubmitallocationorderRequestProductListItem(LingXingModel):
    product_id: str  # 产品id
    seller_id: Optional[str] = None  # 店铺id，不传默认0【对应查询亚马逊店铺信息接口字段sid】
    fnsku: Optional[str] = None  # fnsku，不传默认为空
    good_num: Optional[int] = None  # 可用调拨量，和次品调拨量其中一项必填
    bad_num: Optional[int] = None  # 次品调拨量，和可用调拨量其中一项必填
    cg_package_length: Optional[str] = None  # 包装规格-长（CM），不传或者传空则取产品管理的值
    cg_package_width: Optional[str] = None  # 包装规格-宽（CM），不传或者传空则取产品管理的值
    cg_package_height: Optional[str] = None  # 包装规格-高（CM），不传或者传空则取产品管理的值
    cg_product_gross_weight: Optional[str] = None  # 单品净重，不传或者传空则取产品管理的值
    freight_fee_unit: Optional[str] = None  # 单位运费，若费用分摊方式为5-自定义则必填，其他则该字段无效
    other_fee_unit: Optional[str] = None  # 单位其他费用，若费用分摊方式为5-自定义则必填，其他则该字段无效
    product_remark: Optional[str] = None  # 明细备注，最大长度为255个字符
    out_available_bin: Optional[list] = None  # 出库可用仓位列表，不指定则传空数组 []
    out_available_bin__whb_code: Optional[str] = None  # 出库可用仓位编码
    out_available_bin__num: Optional[str] = None  # 出库可用仓位调拨量
    out_inferior_bin: Optional[list] = None  # 出库次品仓位列表，不指定则传空数组 []
    out_inferior_bin__whb_code: Optional[str] = None  # 出库次品仓位编码
    out_inferior_bin__num: Optional[str] = None  # 出库次品仓位调拨量
    to_available_bin: Optional[list] = None  # 入库可用仓位列表，不指定则传空数组 []
    to_available_bin__whb_code: Optional[str] = None  # 入库可用仓位编码
    to_available_bin__num: Optional[str] = None  # 入库可用仓位调拨量
    to_inferior_bin: Optional[list] = None  # 入库次品仓位列表，不指定则传空数组 []
    to_inferior_bin__whb_code: Optional[str] = None  # 入库次品仓位编码
    to_inferior_bin__num: Optional[str] = None  # 入库次品仓位调拨量


class WarehouseSubmitallocationorderRequest(LingXingModel):
    """Request for 创建待调拨的调拨单.

    POST /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder
    """

    sys_wid: int  # 系统出库仓库ID
    sys_to_wid: int  # 系统入库仓库ID
    freight_fee: Optional[str] = None  # 运费
    other_fee: Optional[str] = None  # 其他费用
    fee_part_type: Optional[int] = (
        None  # 费用分摊方式：0 不分摊【默认值】，2 按sku数量分摊，3 按重量，4 按体积，5 按自定义
    )
    remark: Optional[str] = None  # 备注
    predict_time: Optional[str] = None  # 预计到货时间
    type: Optional[str] = None  # 默认为2-标准调拨
    out_bin_type: str  # 默认0 出库仓位不为空时必传1
    product_list: List[WarehouseSubmitallocationorderRequestProductListItem]


class WarehouseInboundOrderConfirmRequest(LingXingModel):
    """Request for 入库单确认入库.

    POST /basicOpen/inboundOrder/inbound/setInbound
    """

    orderSn: Optional[list] = None  # 入库单单号


class WarehouseOutboundOrderConfirmRequest(LingXingModel):
    """Request for 出库单确认出库.

    POST /basicOpen/outboundOrder/outbound/setOutbound
    """

    orderSn: Optional[list] = None  # 出库单单号


class WarehouseAdjustOrderConfirmRequest(LingXingModel):
    """Request for 调整单确认调整.

    POST /basicOpen/adjustOrder/adjust/setAdjust
    """

    orderSn: Optional[list] = None  # 调整单单号


class WarehouseGetAdjustOrderConfirmResultRequest(LingXingModel):
    """Request for 查询调整单确认调整异步结果.

    POST /basicOpen/adjustOrder/adjust/getAdjustStatus
    """

    taskNo: Optional[str] = None  # 异步任务编号


class WarehouseOutboundorderdeleteRequest(LingXingModel):
    """Request for 删除出库单.

    POST /basicOpen/outboundOrder/outbound/delete
    """

    orderSn: Optional[list] = None  # 出库单单号


class WarehouseFinishCostChangeOrderRequestListItem(LingXingModel):
    product_id: int  # 产品ID
    seller_id_______________docs_BasicData_SellerLists________sid_: Optional[Any] = None  # 否
    fnsku: Optional[str] = None  # FNSKU，默认为空
    relation_order_out: str  # 入库单号
    unit_cost_price: float  # 变更后采购单价
    unit_fee_price: float  # 变更后单位费用


class WarehouseFinishCostChangeOrderRequest(LingXingModel):
    """Request for 创建已完成的成本补录单.

    POST
    """

    type: int  # 补录类型—只支持入库成本(1)
    wid: int  # 仓库ID
    remark: str  # 备注
    list_field: List[WarehouseFinishCostChangeOrderRequestListItem] = Field(alias="list")


class WarehouseListinboundRequest(LingXingModel):
    """Request for 查询海外仓备货单列表.

    POST /erp/sc/routing/owms/inbound/listInbound
    """

    status: Optional[int] = None  # 状态： 10 待审核 20 已驳回 30 待配货 40 待发货 50 待收货 51 已撤销 60 已完成
    sub_status: Optional[int] = None  # 子状态：【仅在待收货状态下生效】  0 全部  1 未收货  2 部分收货
    s_wid: Optional[list] = None  # 发货仓库id
    r_wid: Optional[list] = None  # 收货仓库id
    overseas_order_no: Optional[str] = None  # 备货单号
    create_time_from: Optional[str] = None  # 查询开始日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    create_time_to: Optional[str] = None  # 查询结束日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    page_size: Optional[int] = None  # 分页数量，最大50，默认20
    page: Optional[int] = None  # 当前页码，默认1
    date_type: Optional[str] = (
        None  # 备货单时间查询类型：【默认create_time】 delivery_time 发货时间 create_time 创建时间 receive_time 收货时间 update_time 更新时间
    )
    is_delete: Optional[int] = None  # 订单是否删除： 0 未删除【默认】 1 已删除 2 全部


class WarehouseOverSeasStockDetailRequest(LingXingModel):
    """Request for 查询备货单详情.

    POST /basicOpen/overSeaWarehouse/stockOrder/detail
    """

    overseas_order_no: str  # 备货单号


class WarehouseListordernosRequest(LingXingModel):
    """Request for 获取备货单号.

    POST /erp/sc/routing/owms/inbound/listOrderNos
    """

    inbound_order_no: Optional[list] = None  # 客户参考号 数组


class WarehouseDeleteOverSeaStockOrderRequest(LingXingModel):
    """Request for 删除备货单.

    POST /basicOpen/overSeaWarehouse/stockOrder/delete
    """

    overseas_order_nos: List  # 备货单单号，对应获取备货单号接口字段【overseas_order_no】


class WarehouseUpdateinboundRequestProductListItem(LingXingModel):
    product_id: Optional[int] = None  # 本地商品id
    fnsku: Optional[str] = None  # fnsku
    tariffs: Optional[float] = None  # 报关费用
    tariffs_currency_unit: Optional[str] = None  # 报关费用币种
    cg_product_gross_weight: Optional[float] = None  # 单品净重（G）
    cg_package_length: Optional[float] = None  # 包装规格-长（CM）
    cg_package_width: Optional[float] = None  # 包装规格-宽（CM）
    cg_package_height: Optional[float] = None  # 包装规格-高（CM）
    stock_num: Optional[int] = None  # 备货数量,整箱配对需要乘以配对数量
    sid: Optional[str] = None  # 店铺id，有fnsku填
    product_code: Optional[str] = None  # 三方产品编码
    fba_cost: Optional[float] = None  # 单位头程费用
    fba_cost_currency_unit: Optional[str] = None  # 单位头程费用币种单位
    remark: Optional[str] = None  # 商品备注


class WarehouseUpdateinboundRequestHeadLogisticsListItem(LingXingModel):
    tax_fee_type: (
        int  # 税费分摊方式：  0：产品-计费重  1：产品-实重  2：产品-体积重  3：产品-数量  4：自定义  5：箱子-体积)
    )
    tracking_list: List  # 轨迹信息
    tracking_list__tracking_no: str  # 查询单号
    tracking_list__transport_type: int  # 运输类型： 1：快递 2：海运 3：空运 4：其他
    tracking_list__order_type_code: int  # 单号类型：【注意：与运输类型联动关系】 1：订舱号 2：提单号 3：箱号 4：其他 5：跟踪单号 6：航班号 当transport_type=1时只能传5 当transport_type=2时只能传1
    tracking_list__shippers: str  # 承运商【运输类型为海运时才有意义】
    tracking_list__remark: str  # 备注
    estimate_expenses_list: dict  # 费用明细-预估费用
    estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)
    estimate_expenses_list__price: str  # 单价
    estimate_expenses_list__price_currency: str  # 单价币种
    estimate_expenses_list__logistics_fee: str  # 物流费用
    estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    estimate_expenses_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id（20位）
    estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    actual_expenses_list: dict  # 费用明细-实际费用
    actual_expenses_list__tax_fee: str  # 税费
    actual_expenses_list__tax_fee_currency: str  # 税费币种
    actual_expenses_list__chargeable_weight: str  # 计费重
    actual_expenses_list__price: str  # 单价
    actual_expenses_list__price_currency: str  # 单价币种
    actual_expenses_list__logistics_fee: str  # 物流费用
    actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    actual_expenses_list__remark: Optional[str] = None  # 备注
    actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id(20位)
    actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种


class WarehouseUpdateinboundRequestLogisticsListItem(LingXingModel):
    logistics_order_no: Optional[str] = None  # 物流单号
    logistics_money: Optional[str] = None  # 预估物流费用
    logistics_money_unit: Optional[str] = None  # 预估物流费用币种
    other_money: Optional[str] = None  # 预估其他费用
    other_money_unit: Optional[str] = None  # 预估其他费用币种
    track_order_no: Optional[str] = None  # 追踪号
    other_money_remark: Optional[str] = None  # 预估费用备注
    real_logistics_money: Optional[float] = None  # 实际物流费用
    real_logistics_money_unit: Optional[str] = None  # 实际物流费用币种
    real_other_money: Optional[float] = None  # 实际其他费用
    real_other_money_unit: Optional[str] = None  # 实际其他费用币种
    real_other_money_remark: Optional[str] = None  # 实际其他费用备注
    wool_id: Optional[int] = None  # 物流记录id
    operation_type: Optional[int] = None  # 物流费用操作类型:=新增2=修改3=删除


class WarehouseUpdateinboundRequest(LingXingModel):
    """Request for 更新备货单.

    POST /erp/sc/routing/owms/inbound/updateInbound
    """

    overseas_order_no: str  # 海外仓备货单号
    logistics_id: Optional[int] = None  # 物流方式id【按计费重分摊时，需传对应物流方式，以获取材积参数用于计算】
    estimated_time: Optional[str] = None  # 预计到货时间
    arrival_time: Optional[str] = None  # 实际到货时间
    share_id: Optional[int] = None  # 头程费分配方式： 0 按计费重【默认值】 1 按实重 2 按体积重 3 按SKU数量 4自定义
    remark: Optional[str] = None  # 备注
    file_id: Optional[str] = None  # 附件id
    overseas_type: Optional[int] = None  # 下单至第三方【当收货仓为API海外仓时可填，不填默认为是】：1 否，2 是【默认】
    real_delivery_time: Optional[str] = None  # 实际发货时间，格式：Y-m-d H:i:s
    logistics_list_type: int  # 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息
    product_list: Optional[List[WarehouseUpdateinboundRequestProductListItem]] = None
    head_logistics_list: WarehouseUpdateinboundRequestHeadLogisticsListItem
    logistics_list: Optional[List[WarehouseUpdateinboundRequestLogisticsListItem]] = None


class WarehouseUpdateLogisticsRequestLogisticsListItem(LingXingModel):
    logistics_order_no: str  # 物流单号
    logistics_money: str  # 预估物流费用
    logistics_money_unit: str  # 预估物流费用币种
    other_money: str  # 预估其他费用
    other_money_unit: str  # 预估其他费用币种
    track_order_no: str  # 追踪号
    other_money_remark: str  # 预估费用备注
    real_logistics_money: float  # 实际物流费用
    real_logistics_money_unit: str  # 实际物流费用币种
    real_other_money: float  # 实际其他费用
    real_other_money_unit: str  # 实际其他费用币种
    real_other_money_remark: str  # 实际其他费用备注


class WarehouseUpdateLogisticsRequestHeadLogisticsListItem(LingXingModel):
    tax_fee_type: (
        int  # 税费分摊方式：  0：产品-计费重  1：产品-实重  2：产品-体积重  3：产品-数量  4：自定义  5：箱子-体积)
    )
    tracking_list: List  # 轨迹信息
    tracking_list__tracking_no: str  # 查询单号
    tracking_list__transport_type: int  # 运输类型： 1：快递 2：海运 3：空运 4：其他
    tracking_list__order_type_code: int  # 单号类型：【注意：与运输类型联动关系】 1：订舱号 2：提单号 3：箱号 4：其他 5：跟踪单号 6：航班号 当transport_type=1时只能传5 当transport_type=2时只能传1
    tracking_list__shippers: str  # 承运商【运输类型为海运时才有意义】
    tracking_list__remark: str  # 备注
    estimate_expenses_list: dict  # 费用明细-预估费用
    estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)
    estimate_expenses_list__price: str  # 单价
    estimate_expenses_list__price_currency: str  # 单价币种
    estimate_expenses_list__logistics_fee: str  # 物流费用
    estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    estimate_expenses_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id（20位）
    estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    actual_expenses_list: dict  # 费用明细-实际费用
    actual_expenses_list__tax_fee: str  # 税费
    actual_expenses_list__tax_fee_currency: str  # 税费币种
    actual_expenses_list__chargeable_weight: str  # 计费重
    actual_expenses_list__price: str  # 单价
    actual_expenses_list__price_currency: str  # 单价币种
    actual_expenses_list__logistics_fee: str  # 物流费用
    actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    actual_expenses_list__remark: Optional[str] = None  # 备注
    actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id(20位)
    actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种


class WarehouseUpdateLogisticsRequest(LingXingModel):
    """Request for 更新备货单物流信息.

    POST /erp/sc/routing/owms/inbound/updateLogistics
    """

    overseas_order_no: str  # 海外仓备货单号
    logistics_list_type: int  # 物流信息版本： 0：旧版，即将下线 1：新版
    logistics_list: List[WarehouseUpdateLogisticsRequestLogisticsListItem]
    head_logistics_list: WarehouseUpdateLogisticsRequestHeadLogisticsListItem


class WarehouseGetpackingdataRequest(LingXingModel):
    """Request for 查询备货单装箱信息.

    GET /erp/sc/routing/owms/inbound/getPackingData
    """

    overseas_order_no: str  # 备货单号


class WarehousePackingRequestBoxListItem(LingXingModel):
    box_no: int  # 箱号
    box_count: Optional[int] = None  # 箱数，默认1
    box_nos: Optional[list] = None  # 自定义箱号数组，箱数大于1时必传
    height: float  # 箱规-高（cm）
    length: float  # 箱规-长（cm）
    width: float  # 箱规-宽（cm）
    weight: float  # 箱子毛重（KG）
    items: List  # 商品详情
    items__product_id: int  # 商品id
    items__twp_id: Optional[int] = (
        None  # 三方商品id，查询系统产品与第三方海外仓产品映射列表接口对应字段【twp_id】， 注：收货仓库是第三方仓时必填
    )
    items__quantity_shipped: int  # 装箱数：计算公式=备货数量/箱数
    items__oversea_product_code: Optional[int] = None  # 三方商品编码（收货仓库为三方海外仓，可不传product_id）
    items__match_num: int  # 配对数量【默认1】：传 1 为单个配对，其他值均为整箱配对
    items__fnsku: Optional[str] = None  # fnsku
    items__barcode: Optional[str] = None  # 万邑通SN码
    items__is_a_plus: Optional[int] = None  # 万邑通是否A+包裹：0-否，1-是
    items__sid: int  # 店铺id，库存中心过渡版本后有fnsku必填 ，对应查询亚马逊店铺列表接口对应字段【sid】


class WarehousePackingRequest(LingXingModel):
    """Request for 上传备货单装箱信息.

    POST /erp/sc/routing/owms/inbound/packing
    """

    overseas_order_no: str  # 备货单号
    packaging_type: int  # 装箱类型：1 每箱多个sku，2 每箱一个sku
    box_count: int  # 总箱数
    box_list: List[WarehousePackingRequestBoxListItem]


class WarehouseGetReceiveGoodRecordsRequest(LingXingModel):
    """Request for 查询备货单收货记录.

    POST /erp/sc/routing/owms/inbound/getReceiveGoodRecords
    """

    overseas_order_no: Optional[str] = None  # 备货单单号【不支持批量】
    start_date: Optional[str] = None  # 收货开始时间，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 收货结束时间，开区间，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认500


class WarehouseSendInboundRequest(LingXingModel):
    """Request for 海外仓备货单发货.

    POST /erp/sc/routing/owms/inbound/sendInbound
    """

    overseas_order_no: str  # 备货单号


class WarehouseInboundbatchesreceiptRequestProductListItem(LingXingModel):
    product_id: int  # 本地产品id
    current_receive_num: int  # 收货数量
    sid: Optional[int] = None  # 店铺id【备货单中对应有值则必填】 ，对应查询亚马逊店铺列表接口对应字段【sid】
    fnsku: Optional[str] = None  # fnsku【备货单中对应有值则必填】
    product_code: Optional[str] = None  # 第三方仓sku【备货单中对应有值则必填】


class WarehouseInboundbatchesreceiptRequest(LingXingModel):
    """Request for 备货单分批收货.

    POST /erp/sc/routing/owms/inbound/batchesReceipt
    """

    overseas_order_no: str  # 备货单号
    product_list: List[WarehouseInboundbatchesreceiptRequestProductListItem]


class WarehouseInboundcompletereceiptRequest(LingXingModel):
    """Request for 备货单结束到货.

    POST /erp/sc/routing/owms/inbound/completeReceipt
    """

    overseas_order_no: str  # 备货单号


class WarehouseCreateInboundRequestLogisticsListItem(LingXingModel):
    logistics_order_no: Optional[str] = None  # 物流单号
    logistics_money: Optional[str] = None  # 预估物流费用
    logistics_money_unit: Optional[str] = None  # 预估物流费用币种
    other_money: Optional[str] = None  # 预估其他费用
    other_money_unit: Optional[str] = None  # 预估其他费用币种
    track_order_no: Optional[str] = None  # 追踪号
    other_money_remark: Optional[str] = None  # 预估费用备注
    real_logistics_money: Optional[float] = None  # 实际物流费用
    real_logistics_money_unit: Optional[str] = None  # 实际物流费用币种
    real_other_money: Optional[float] = None  # 实际其他费用
    real_other_money_unit: Optional[str] = None  # 实际其他费用币种
    real_other_money_remark: Optional[str] = None  # 实际其他费用备注
    wool_id: Optional[int] = None  # 物流记录id


class WarehouseCreateInboundRequestProductListItem(LingXingModel):
    product_id: int  # 本地商品id
    fnsku: Optional[str] = None  # fnsku
    tariffs: Optional[float] = None  # 报关费用
    tariffs_currency_unit: Optional[str] = None  # 报关费用币种
    cg_product_gross_weight: Optional[float] = None  # 单品净重（G）
    cg_package_length: Optional[float] = None  # 包装规格-长（CM）
    cg_package_width: Optional[float] = None  # 包装规格-宽（CM）
    cg_package_height: Optional[float] = None  # 包装规格-高（CM）
    stock_num: int  # 备货数量，整箱配对需要乘以配对数量
    receive_num: int  # 收货数量（收货数量可以为0）
    oversea_product_code: Optional[str] = (
        None  # 三方sku编码，查询系统产品与第三方海外仓产品映射列表接口对应字段【oversea_product_code】 【当仓库是有api海外仓必填】
    )
    sid: Optional[str] = None  # 店铺id，有fnsku填 ，对应查询亚马逊店铺列表接口对应字段【sid】


class WarehouseCreateInboundRequestHeadLogisticsListItem(LingXingModel):
    tax_fee_type: (
        int  # 税费分摊方式：  0：产品-计费重  1：产品-实重  2：产品-体积重  3：产品-数量  4：自定义  5：箱子-体积)
    )
    tracking_list: List  # 轨迹信息
    tracking_list__tracking_no: str  # 查询单号
    tracking_list__transport_type: int  # 运输类型： 1：快递 2：海运 3：空运 4：其他
    tracking_list__order_type_code: int  # 单号类型：【注意：与运输类型联动关系】 1：订舱号 2：提单号 3：箱号 4：其他 5：跟踪单号 6：航班号 当transport_type=1时只能传5 当transport_type=2时只能传1
    tracking_list__shippers: str  # 承运商【运输类型为海运时才有意义】
    tracking_list__remark: str  # 备注
    estimate_expenses_list: dict  # 费用明细-预估费用
    estimate_expenses_list__chargeable_weight: Optional[str] = None  # 计费重(单位KG)
    estimate_expenses_list__price: str  # 单价
    estimate_expenses_list__price_currency: str  # 单价币种
    estimate_expenses_list__logistics_fee: str  # 物流费用
    estimate_expenses_list__logistics_fee_currency: str  # 物流费用币种
    estimate_expenses_list__remark: Optional[str] = None  # 备注
    estimate_expenses_list__other_fee_arr: List  # 预估费用-其他费： 获取发货单头程物流-其他费类型接口获取
    estimate_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id（20位）
    estimate_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    estimate_expenses_list__other_fee_arr__other_currency: str  # 其他费币种
    actual_expenses_list: dict  # 费用明细-实际费用
    actual_expenses_list__tax_fee: str  # 税费
    actual_expenses_list__tax_fee_currency: str  # 税费币种
    actual_expenses_list__chargeable_weight: str  # 计费重
    actual_expenses_list__price: str  # 单价
    actual_expenses_list__price_currency: str  # 单价币种
    actual_expenses_list__logistics_fee: str  # 物流费用
    actual_expenses_list__logistics_fee_currency: str  # 物流费用币种
    actual_expenses_list__remark: Optional[str] = None  # 备注
    actual_expenses_list__other_fee_arr: List  # 实际费用-其他费： 获取发货单头程物流-其他费类型接口获取
    actual_expenses_list__other_fee_arr__fee_type_id: str  # 其他费id(20位)
    actual_expenses_list__other_fee_arr__other_amount: str  # 其他费金额
    actual_expenses_list__other_fee_arr__other_currency: str  # 其他费币种


class WarehouseCreateInboundRequest(LingXingModel):
    """Request for 创建待发货/待收货/已完成的备货单.

    POST /erp/sc/routing/owms/inbound/createInbound
    """

    inbound_order_no: str  # 客户参考号（唯一单号）
    custom_s_wid: Optional[str] = None  # 自定义仓库id，custom_s_wid和s_wid其中一项必填，都填则优先custom_s_wid
    s_wid: int  # 发货仓库，仅限本地仓
    r_wid: int  # 收货仓库，仅限海外仓
    logistics_id: int  # 物流方式id，查询头程物流渠道列表接口对应字段【id】 （按计费重分摊时，需有传对应物流方式，以获取材积参数用于计算）
    status: Optional[int] = (
        None  # 订单状态：【默认60】 40 待发货 50 待收货 60 已完成 注：收货仓支持三方海外仓的备货单状态只会到待发货
    )
    estimated_time: Optional[str] = None  # 预计到货时间
    arrival_time: Optional[str] = None  # 实际到货时间
    share_id: Optional[int] = (
        None  # 头程费分摊方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积 注意：生成待发货状态备货单时，需要通过接口上传备货单装箱信息上传箱子信息； 待收货和已
    )
    remark: Optional[str] = None  # 备注
    file_id: Optional[str] = None  # 附件id
    overseas_type: Optional[int] = (
        None  # 下单至第三方【默认2】： 1 否，2 是 注：当收货仓为API海外仓时可填，不填默认为是
    )
    real_delivery_time: Optional[str] = None  # 实际发货时间
    logistics_list_type: int  # 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息
    method_id: Optional[str] = None  # 运输方式 查询运输方式列表接口对应字段【method_id】
    custom_fields: Optional[dict] = None  # 自定义字段
    logistics_list: Optional[List[WarehouseCreateInboundRequestLogisticsListItem]] = None
    product_list: List[WarehouseCreateInboundRequestProductListItem]
    head_logistics_list: WarehouseCreateInboundRequestHeadLogisticsListItem


class WarehouseMatchskulistRequest(LingXingModel):
    """Request for 查询系统产品与第三方海外仓产品映射列表.

    POST /erp/sc/routing/owms/inbound/matchSkuList
    """

    wid: str  # 仓库id，多个用英文逗号分隔
    is_matched: Optional[int] = None  # 是否配对：【空表示都返回】 0 未配对 1 配对
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，默认20


class WarehouseOverseaWarehouseMatchListRequest(LingXingModel):
    """Request for 查询海外仓sku配对列表.

    POST /basicOpen/overseaWarehouseSetting/matchList
    """

    wpId: int  # 三方服务商id
    twIds: Optional[str] = None  # 三方仓id，多个之间用逗号隔开
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页大小，默认20，上限200
    isMatched: Optional[int] = None  # 是否配对，0否，1是
    keyword: Optional[str] = None  # 关键词，搜索sku / 品名 / 第三方产品名 / 产品编码


class WarehousePackagelabelRequest(LingXingModel):
    """Request for 获取第三方箱唛.

    POST /erp/sc/routing/owms/inbound/packageLabel
    """

    size: int  # 尺寸映射： 1=西邮尺寸专属 2=谷仓A4 3=谷仓100x100 4=谷仓100x150 5=谷仓100x60 11=易仓A4(按SKU) 12=易仓A4(按箱) 13=易仓100x100(无产品名
    overseas_order_no: str  # 备货单号


class WarehouseRemovalinboundlistRequest(LingXingModel):
    """Request for 查询移除入库单列表.

    POST /erp/sc/routing/owms/removalInbound/list
    """

    status: Optional[int] = (
        None  # 订单状态： 1 待提交-未提交 2 待提交-提交中 3 待提交-失败 4 待收货-未收货 5 待收货-异常 6 已完成 7 已作废
    )
    start_date: Optional[str] = None  # 开始日期【发货日期，双闭区间】
    end_date: Optional[str] = None  # 结束日期【发货日期，双闭区间】
    order_no: Optional[list] = None  # 移除入库单号
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限1000


class WarehouseOverseastockorderallocateRequest(LingXingModel):
    """Request for 备货单分配库存.

    POST /basicOpen/overSeaWarehouse/stockOrder/allocate
    """

    orderNo: str  # 备货单号


class WarehouseWmsOrderListRequest(LingXingModel):
    """Request for 查询销售出库单列表.

    POST /erp/sc/routing/wms/order/wmsOrderList
    """

    page: Optional[int] = None  # 分页页码，默认1
    page_size: Optional[int] = None  # 分页长度，默认20，上限200
    sid_arr: Optional[list] = None  # 店铺id
    status_arr: Optional[list] = None  # 状态： 1 物流下单 2 待出库 3 已出库 4 已截单
    logistics_status_arr: Optional[list] = (
        None  # 物流状态： 1 待导入 2 物流待下单 3 物流下单中 4 下单异常 5 下单完成 6 待海外仓下单 7 海外仓下单中 11 待导入国内物流 41 物流取消中 42 物流取消异常 43 物流取消完成
    )
    platform_order_no_arr: Optional[list] = None  # 平台单号
    order_number_arr: Optional[list] = None  # 系统单号
    wo_number_arr: Optional[list] = None  # 销售出库单号
    time_type: Optional[str] = (
        None  # 时间类型： 创建时间 create_at  出库时间【单据操作】 delivered_at 流水出库时间 stock_delivered_at 变更时间 update_at
    )
    start_date: Optional[str] = None  # 开始日期，格式：Y-m-d，默认为最近1个月
    end_date: Optional[str] = None  # 结束日期，格式：Y-m-d，默认为最近1个月


class WarehouseSettrackingnoRequest(LingXingModel):
    """Request for 物流下单 - 编辑运单号/跟踪号.

    POST /basicOpen/logisticsOrdering/setTrackingNo
    """

    waybill_no: str  # 运单号
    wo_number: str  # 销售出库单号
    tracking_no: Optional[str] = None  # 跟踪号
    logistics_freight: Optional[str] = None  # 物流运费
    logistics_freight_currency_code: Optional[str] = (
        None  # 物流运费币种： CNY USD EUR JPY AUD CAD MXN GBP INR AED SGD SAR BRL SEK PLN TRY HKD
    )
    pkg_fee_weight: Optional[str] = None  # 计费重
    pkg_fee_weight_unit: Optional[str] = None  # 计费重单位： g kg


class WarehouseWmsordergetwmslogisticslabelsRequest(LingXingModel):
    """Request for 查询销售出库单物流面单.

    POST /erp/sc/routing/wms/order/getWmsLogisticsLabels
    """

    wo_number_arr: Optional[list] = None  # 销售出库单号,上限50【销售出库单号与系统单号二选一必填】
    order_number_arr: Optional[list] = None  # 系统单号,上限50【销售出库单号与系统单号二选一必填】


class WarehouseCancelwmsorderRequest(LingXingModel):
    """Request for 销售出库单截单.

    POST /basicOpen/wmsOrder/cancel
    """

    orderNumbers: List  # 系统单号 对应查询销售出库单列表data>>order_number字段
    tagType: str  # 截单标签，3-5：待人工审核；3-17：其他
    orderComment: Optional[str] = None  # 截单备注

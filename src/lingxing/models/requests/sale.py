"""Request models for Sale APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class SaleListingRequest(LingXingModel):
    """Request for 查询亚马逊Listing.
    
    POST /erp/sc/data/mws/listing
    """
    sid: str  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    is_pair: Optional[int] = None  # 是否配对：1 已配对，2 未配对
    is_delete: Optional[int] = None  # 是否删除：0 未删除，1 已删除
    pair_update_start_time: Optional[str] = None  # 【配对更新时间】的开始时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1
    pair_update_end_time: Optional[str] = None  # 【配对更新时间】的结束时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1
    listing_update_start_time: Optional[str] = None  # 【All Listing报表更新时间】的开始时间（此为零时区时间，格式Y-m-d H:i:s）
    listing_update_end_time: Optional[str] = None  # 【All Listing报表更新时间】的结束时间（此为零时区时间，格式Y-m-d H:i:s）
    search_field: Optional[str] = None  # 搜索支持字段：seller_sku、asin、sku
    search_value: Optional[list] = None  # 搜索值，上限10个
    exact_search: Optional[int] = None  # 搜索模式：0 模糊搜索，1 精确搜索【默认值】
    store_type: Optional[int] = None  # 商品类型，1-非低价商店 ，2-低价商店商品
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000


class SaleUpdatePrincipalRequestSidAsinListItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # asin
    principal_name: Optional[list] = None  # 负责人姓名，最多支持10个负责人，传空或者不传表示清空负责人

class SaleUpdatePrincipalRequest(LingXingModel):
    """Request for 批量分配Listing负责人.
    
    POST /listing/listing/open/api/asin/updatePrincipal
    """
    sid_asin_list: List[SaleUpdatePrincipalRequestSidAsinListItem]


class SaleProductlinkRequestDataItem(LingXingModel):
    seller_id: Optional[str] = None  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    marketplace_id: Optional[str] = None  # 市场id
    msku: str  # msku
    sku: str  # 本地sku
    is_sync_pic: int  # 是否同步listing图片：0 否，1 是

class SaleProductlinkRequest(LingXingModel):
    """Request for 批量添加/编辑Listing配对.
    
    POST /erp/sc/storage/product/link
    """
    data: SaleProductlinkRequestDataItem


class SalePricingsubmitRequestPricingParamsItem(LingXingModel):
    sid: Any  # [int]
    msku: Any  # [string]
    standard_price: Any  # [number]
    sale_price: Optional[Any] = None  # [number]
    start_date: Optional[Any] = None  # [string]
    end_date: Optional[Any] = None  # [string]

class SalePricingsubmitRequest(LingXingModel):
    """Request for 批量修改Listing价格.
    
    POST /erp/sc/listing/ProductPricing/pricingSubmit
    """
    pricing_params: List[SalePricingsubmitRequestPricingParamsItem]


class SaleGetPricesRequestDataItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU

class SaleGetPricesRequest(LingXingModel):
    """Request for 批量获取Listing费用.
    
    POST /listing/listing/open/api/listing/getPrices
    """
    data: List[SaleGetPricesRequestDataItem]


class SaleQuerylistingrelationtaglistRequestBindDetailItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    relation_id: str  # msku，查询亚马逊Listing 接口对应字段【seller_sku】

class SaleQuerylistingrelationtaglistRequest(LingXingModel):
    """Request for 查询Listing标记标签列表.
    
    POST 
    """
    bind_detail: List[SaleQuerylistingrelationtaglistRequestBindDetailItem]


class SaleGlobaltagpagelistRequest(LingXingModel):
    """Request for 查询Listing标签列表.
    
    POST /basicOpen/globalTag/listing/page/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    search_field: Optional[str] = None  # 搜索类型：tag_name 标签名称
    search_value: Optional[str] = None  # 搜索值


class SaleGlobaltagaddtagRequest(LingXingModel):
    """Request for 添加Listing标签.
    
    POST /basicOpen/globalTag/listing/addTag
    """
    tag_name: str  # 标签名称


class SaleGlobaltagremovetagRequest(LingXingModel):
    """Request for 删除Listing标签.
    
    POST /basicOpen/globalTag/listing/removeTag
    """
    tag_ids: List  # 标签id，上限200


class SaleFbafeedifferencelistRequest(LingXingModel):
    """Request for FBA费差异-异常订单-订单.
    
    POST /basicOpen/openapi/sale/fbaFeeDifference/order/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    start_date: Optional[str] = None  # 开始时间【结算时间】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束时间【结算时间】，闭区间，格式：Y-m-d
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = None  # 搜索字段：order_id 订单号，msku MSKU
    search_value: Optional[str] = None  # 搜索值：多个使用英文逗号分隔，上限200


class SaleFbafeedifferencemskulistRequest(LingXingModel):
    """Request for FBA费差异-异常订单-MSKU.
    
    POST /basicOpen/openapi/sale/fbaFeeDifference/msku/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    start_date: Optional[str] = None  # 开始时间【结算时间】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束时间【结算时间】，闭区间，格式：Y-m-d
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = None  # 搜索字段：msku MSKU
    search_value: Optional[str] = None  # 搜索值：多个使用英文逗号分隔，上限200


class SaleListingoperatelogpagelistRequest(LingXingModel):
    """Request for 查询Listing操作日志列表.
    
    POST /basicOpen/listingManage/listingOperateLog/pageList
    """
    sid: str  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20
    operate_uid: Optional[list] = None  # 操作人id
    operate_type: Optional[list] = None  # 操作类型：  1  调价   2  调库存   3  修改标题   4  编辑商品   5  B2B调价
    operate_time_start: Optional[str] = None  # 开始时间【操作时间】，格式：Y-m-d H:i:s
    operate_time_end: Optional[str] = None  # 结束时间【操作时间】，格式：Y-m-d H:i:s


class SaleB2bpricemodifypriceRequestContentItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    asin: str  # ASIN
    b2b_price: str  # B2B价格

class SaleB2bpricemodifypriceRequest(LingXingModel):
    """Request for 修改B2B价格.
    
    POST /basicOpen/b2bPrice/modifyPrice
    """
    content: List[SaleB2bpricemodifypriceRequestContentItem]


class SaleAddGoodsTagRequestBinddetailItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    relationId: str  # msku，查询亚马逊Listing 接口对应字段【seller_sku】

class SaleAddGoodsTagRequest(LingXingModel):
    """Request for Listing新增商品标签.
    
    POST /basicOpen/listingManage/bindListingAndTag
    """
    tagIds: List  # 标签id数组
    bindDetail: List[SaleAddGoodsTagRequestBinddetailItem]


class SaleDeleteGoodsTagRequestBinddetailItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    relationId: str  # msku，查询亚马逊Listing 接口对应字段【seller_sku】

class SaleDeleteGoodsTagRequest(LingXingModel):
    """Request for Listing删除商品标签.
    
    POST /basicOpen/listingManage/removeListingAndTag
    """
    globalTagIds: List  # 标签id数组
    bindDetail: List[SaleDeleteGoodsTagRequestBinddetailItem]


class SaleUpdateFbmInventoryRequestFbminventorylistItem(LingXingModel):
    storeId: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # 要修改FBM库存或处理时间的MSKU
    fbmInventory: int  # FBM库存（此项必填）
    shipDays: Optional[str] = None  # 处理时间

class SaleUpdateFbmInventoryRequest(LingXingModel):
    """Request for 修改 FBM库存&处理时间.
    
    POST /basicOpen/FbmManagement/modifyFbmInventory
    """
    fbmInventoryList: List[SaleUpdateFbmInventoryRequestFbminventorylistItem]


class SaleUnlinkListingRequestListItem(LingXingModel):
    storeId: int  # 对应亚马逊店铺【sid】
    msku: str  # msku

class SaleUnlinkListingRequest(LingXingModel):
    """Request for 解除Listing配对.
    
    POST /basicOpen/listingManage/unLinkListingPairs
    """
    list_field: List[SaleUnlinkListingRequestListItem] = Field(alias="list")


class SaleAdjustpriceadjustpricemanualRequest(LingXingModel):
    """Request for 查询调价队列.
    
    POST /basicOpen/module/adjustPrice/AdjustPriceManual
    """
    offset: float  # 偏移量
    length: float  # 页长度，上限500
    sid: Optional[list] = None  # 搜索店铺id
    processing_status: Optional[list] = None  # 调价状态，支持多选，数组 1待调价 2调价中 3调价成功 4调价失败 5审批中 6已驳回 7已作废
    time_type: Optional[float] = None  # 搜索时间类型：1创建时间 2完成时间
    start_time: Optional[str] = None  # 开始时间
    end_time: Optional[str] = None  # 结束时间
    search_field: Optional[str] = None  # 搜索字段：msku，asin
    search_value: Optional[list] = None  # 搜索值，msku和asin支持多个搜索，数组
    tab_status: Optional[float] = None  # tab状态栏  0全部 1待审批 2调价中 3成功 4失败 5已作废 默认0


class SalePublishManageCategoryRootRequest(LingXingModel):
    """Request for 刊登管理-查询 Amazon 根分类.
    
    POST /basicOpen/openapi/publish/manage/categoryRoot
    """
    storeId: float  # 店铺id


class SalePublishManageCategoryChildrenRequest(LingXingModel):
    """Request for 刊登管理-查询 Amazon 子分类.
    
    POST /basicOpen/openapi/publish/manage/categoryChildren
    """
    storeId: float  # 店铺id
    categoryUniqueId: float  # 类目唯一ID


class SalePublishManageGetProductTypeRequest(LingXingModel):
    """Request for 刊登管理-获取指定 productType 的 JSON Schema.
    
    POST /basicOpen/openapi/publish/manage/getProductType
    """
    marketplaceId: str  # 市场ID
    productTypeOrigin: str  # 商品原始类型


class SaleGetMerchantShippingGroupRequest(LingXingModel):
    """Request for 刊登管理-获取运费模板.
    
    POST /basicOpen/openapi/publish/manage/getMerchantShippingGroup
    """
    sellerId: str  # 店铺id
    marketplaceId: str  # 市场id
    productType: str  # 商品原始类目
    flag: Optional[float] = None  # 默认传0，返回为空则传1，实时请求亚马逊获取后台最新数据


class SaleProductPublishRequestDataItem(LingXingModel):
    sku: str  # sku
    productType: str  # 商品类型
    attributes: dict  # 商品属性对象
    operationType: int  # 刊登类型 0 刊登新品 1 更新已有商品信息

class SaleProductPublishRequest(LingXingModel):
    """Request for 刊登管理-提交商品资料.
    
    POST /listing/publish/openapi/amazon/product/publish
    """
    store_id: float  # store_id
    data: SaleProductPublishRequestDataItem


class SaleProductListRequestOperateTimeItem(LingXingModel):
    start: Optional[str] = None  # 开始时间
    end: Optional[str] = None  # 结束时间
    end: Optional[str] = None  # 结束时间

class SaleProductListRequest(LingXingModel):
    """Request for 刊登管理-查询刊登结果.
    
    POST /listing/publish/openapi/amazon/product/list
    """
    record_unique_id: Optional[int] = None  # 批次唯一ID
    sku: Optional[str] = None  # sku
    store_id: Optional[int] = None  # store_id
    operate_time: Optional[dict] = None  # 操作时间
    operate_time_: Optional[SaleProductListRequestOperateTimeItem] = None


class SaleQueryProductListRequest(LingXingModel):
    """Request for 查询已有商品信息.
    
    POST /listing/publish/openapi/amazon/product/search
    """
    store_id: int  # store_id
    skus: List  # sku列表，最多20个


class SaleOrderlistsRequest(LingXingModel):
    """Request for 查询亚马逊订单列表.
    
    POST /erp/sc/data/mws/orders
    """
    sid: Optional[int] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    sid_list: Optional[list] = None  # 店铺id列表，最大长度20
    start_date: str  # 查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s 当date_type=3时，需要传入时间格式为：Y-m-d H:i:s
    end_date: str  # 查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s 当date_type=3时，需要传入时间格式为：Y-m-d H:i:s
    date_type: Optional[int] = None  # 查询日期类型：【默认1】 1 订购时间【站点时间】 2 订单修改时间【北京时间】 3 平台更新时间【UTC时间】 10 发货时间【站点时间】 查询时间范围不超过一年
    order_status: Optional[list] = None  # Pending 待处理 Unshipped 未发货 PartiallyShipped 部分发货 Shipped 已发货 Canceled 取消
    sort_desc_by_date_type: Optional[int] = None  # 是否按查询日期类型排序：0 否，1 降序，2 升序【默认0】
    fulfillment_channel: Optional[int] = None  # 配送方式：1 亚马逊订单-AFN，2 自发货-MFN
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限5000


class SaleOrderDetailRequest(LingXingModel):
    """Request for 查询亚马逊订单详情.
    
    POST /erp/sc/data/mws/orderDetail
    """
    order_id: str  # 亚马逊订单号，多个使用英文逗号分隔，上限200


class SaleScOrderSetRemarkRequest(LingXingModel):
    """Request for SC订单-设置订单备注.
    
    POST /basicOpen/platformOrder/scOrder/setRemark
    """
    sid: int  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】
    amazonOrderId: str  # 订单id
    remark: str  # 备注


class SaleMCFOrderListRequest(LingXingModel):
    """Request for 查询亚马逊多渠道订单列表-v2.
    
    POST /order/amzod/api/orderList
    """
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: Optional[str] = None  # 订购时间-开始（不传默认最近6个月），格式：Y-m-d
    end_date: Optional[str] = None  # 订购时间-结束（不传默认最近6个月），格式：Y-m-d
    date_type: Optional[int] = None  # 查询日期类型：1 订购时间【默认值】，2 订单修改时间
    order_status: Optional[list] = None  # 订单状态列表，枚举值：NEW（待发货-待验证），RECEIVED（待发货-待处理），PLANNING（待发货-准备中），PROCESSING（待发货-处理中），CANCELLED（已取消），COMPL
    offset: int  # 分页偏移量
    length: int  # 分页长度，默认10，上限1000


class SaleProductInformationRequestOrderInfoItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_fulfillment_order_id: str  # 卖家订单号

class SaleProductInformationRequest(LingXingModel):
    """Request for 查询亚马逊多渠道订单详情-商品信息.
    
    POST /order/amzod/api/orderDetails/productInformation
    """
    order_info: List[SaleProductInformationRequestOrderInfoItem]


class SaleLogisticsInformationRequestOrderInfoItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_fulfillment_order_id: str  # 卖家订单号

class SaleLogisticsInformationRequest(LingXingModel):
    """Request for 查询亚马逊多渠道订单详情-物流信息.
    
    POST /order/amzod/api/orderDetails/logisticsInformation
    """
    order_info: List[SaleLogisticsInformationRequestOrderInfoItem]


class SaleReturnInfomationRequestOrderInfoItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_fulfillment_order_id: str  # 卖家订单号

class SaleReturnInfomationRequest(LingXingModel):
    """Request for 查询亚马逊多渠道订单详情-退货换货信息.
    
    POST /order/amzod/api/orderDetails/returnInformation
    """
    order_info: List[SaleReturnInfomationRequestOrderInfoItem]


class SaleFbaCreateOrderRequestItemListItem(LingXingModel):
    msku: str  # MSKU
    quantity_shipped: float  # 发货量
    declared_value: Optional[float] = None  # 申报价值
    declared_currency: Optional[str] = None  # 申报货币

class SaleFbaCreateOrderRequest(LingXingModel):
    """Request for 创建亚马逊多渠道订单.
    
    POST /order/amzod/api/createOrder
    """
    store_name: str  # 店铺名
    country: str  # 店铺国家
    order_id: str  # 订单号
    is_blank_box: Optional[str] = None  # 是否使用无品牌包装箱（“是”/“否”，默认为“否”）
    is_block_amzl: Optional[str] = None  # 是否阻止亚马逊物流（“是”/“否”，默认为“否”）
    receiver: str  # 收件人
    country_code: str  # 收货地址国家/地区（输入国家/地区简码）
    region: str  # 地区
    city: Optional[str] = None  # 城市（日本市场非必填，其他市场必填）
    address1: str  # 地址1
    address2: Optional[str] = None  # 地址2
    postcode: str  # 邮编
    phone_number: Optional[str] = None  # 电话号码
    buyers_mailbox: str  # 买家邮箱
    order_id_for_packing: str  # 装箱单-订单号
    date_for_packing: str  # 装箱单-订单日期
    remark_for_packing: Optional[str] = None  # 装箱单-装箱单备注
    delivery_operation: Optional[str] = None  # 配送操作（“立即配送”/“保留订单”）
    delivery_service: Optional[str] = None  # 配送服务（“标准配送”/“加急配送”/“优先配送”）
    remark: Optional[str] = None  # 订单备注
    item_list: List[SaleFbaCreateOrderRequestItemListItem]


class SaleAftersalelistRequest(LingXingModel):
    """Request for 查询售后订单列表.
    
    POST 
    """
    sid: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 查询时间，左闭右开，格式：Y-m-d
    end_date: str  # 查询时间，左闭右开，格式：Y-m-d
    date_type: Optional[int] = None  # 查询时间类型：【默认1】 1 售后时间，对应data>>deal_time字段 2 订购时间 3 更新时间
    after_type: Optional[str] = None  # 售后类型，多个使用英文逗号分隔： 1 退款 2 退货 3 换货
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000
    amazon_order_id_list: Optional[list] = None  # 亚马逊订单id列表，上限50


class SaleCancelorderRequest(LingXingModel):
    """Request for 取消多渠道订单.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_fulfillment_order_id: str  # 卖家订单号


class SaleMutilChannelTransactionDetailRequest(LingXingModel):
    """Request for 多渠道订单-交易明细.
    
    POST 
    """
    amazonOrderId: str  # 亚马逊订单ID
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】


class SaleFBMOrderListRequest(LingXingModel):
    """Request for 查询亚马逊自发货订单列表.
    
    POST /erp/sc/routing/order/Order/getOrderList
    """
    sid: str  # 店铺sid，用英文逗号分隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】
    order_status: Optional[str] = None  # 订单状态，多个用英文逗号分隔： 2 已发货 3 未付款 4 待审核 5 待发货 6 已取消
    page: Optional[int] = None  # 页码数，默认1
    length: Optional[int] = None  # 分页长度，默认100
    start_time: Optional[str] = None  # 订购时间开始
    end_time: Optional[str] = None  # 订购时间结束


class SaleFBMOrderDetailRequest(LingXingModel):
    """Request for 查询亚马逊自发货订单详情.
    
    POST /erp/sc/routing/order/Order/getOrderDetail
    """
    order_number: str  # 系统单号


class SaleSubmitFulfillmentRequestOrderListItem(LingXingModel):
    id: int  # 标发记录id【20位以内的正整数，对应标发结果中的message_id】
    platform_order_no: str  # 平台单号
    tracking_no: str  # 物流追踪号
    carrier_code: str  # 承运商code
    carrier_name: str  # 承运商名称
    shipping_service: str  # 配送服务，没有可以传空字符串
    order_item: List  # 商品信息
    order_item__order_item_no: str  # 亚马逊商品行id
    order_item__quantity: int  # 商品数量

class SaleSubmitFulfillmentRequest(LingXingModel):
    """Request for 亚马逊订单提交标发.
    
    POST /pb/mp/order/submitFulfillment
    """
    region: str  # 店铺注册所属区域：仅支持 NA、EU、FE 【对应区域值支持国家见附加说明】
    seller_id: str  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    marketplace_id: str  # 市场id
    order_list: List[SaleSubmitFulfillmentRequestOrderListItem]


class SaleGetFulfillmentResultRequest(LingXingModel):
    """Request for 查询亚马逊标发结果.
    
    POST /pb/mp/order/getFulfillmentResult
    """
    seller_id: str  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    task_id: List  # 任务id【提交标发接口返回】，单次请求最多支持查询10个任务ID。


class SaleUploadTrackingRequest(LingXingModel):
    """Request for 导入面单.
    
    POST /basicOpen/selfShipmentOrder/importLabel
    """
    fileName: str  # 面单文件名
    base64File: str  # PDF/PNG/JPG/JPEG格式文件 Base64编码
    trackingNo: str  # 运单号
    waybillNo: str  # 跟踪号
    woId: int  # 出库单id，对应查询销售出库单列表


class SalePromotionalactivitiescouponlistRequest(LingXingModel):
    """Request for 查询促销活动列表-优惠券.
    
    POST /basicOpen/promotionalActivities/coupon/list
    """
    start_date: Optional[str] = None  # 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: Optional[str] = None  # 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    sids: Optional[list] = None  # 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class SalePromotionalactivitiesseckilllistRequest(LingXingModel):
    """Request for 查询促销活动列表-秒杀.
    
    POST /basicOpen/promotionalActivities/secKill/list
    """
    start_date: Optional[str] = None  # 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: Optional[str] = None  # 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class SalePromotionalactivitiesmanagelistRequest(LingXingModel):
    """Request for 查询促销活动列表-管理促销.
    
    POST /basicOpen/promotionalActivities/manage/list
    """
    start_date: Optional[str] = None  # 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: Optional[str] = None  # 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class SalePromotionalactivitiesvipdiscountlistRequest(LingXingModel):
    """Request for 查询促销活动列表-会员折扣/价格折扣.
    
    POST /basicOpen/promotionalActivities/vipDiscount/list
    """
    start_date: Optional[str] = None  # 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: Optional[str] = None  # 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class SalePromotioncouponalldetailbatchRequestItemlistItem(LingXingModel):
    promotionId: str  # 活动id，唯一标识
    storeId: str  # 店铺id
    orderPageNum: float  # 活动订单分页页数,最小为1
    orderPageSize: float  # 活动订单分页大小,最小为1,最大为200
    listingPageNum: float  # 活动listing分页页数,最小为1
    listingPageSize: float  # 活动listing分页大小,最小为1,最大为200

class SalePromotioncouponalldetailbatchRequest(LingXingModel):
    """Request for 查询优惠券详情+listing+订单(批量).
    
    POST /promotionApi/open/promotion/couponAllDetailBatch
    """
    itemList: List[SalePromotioncouponalldetailbatchRequestItemlistItem]


class SalePromotionmanagementalldetailbatchRequestItemlistItem(LingXingModel):
    promotionId: str  # 活动id
    storeId: str  # 店铺id
    orderPageNum: float  # 活动订单分页页数，最小1
    orderPageSize: float  # 活动订单分页大小，最小为1，最大为200
    listingPageNum: float  # 活动listing分页页数，最小1
    listingPageSize: float  # 活动listing分页大小，最小为1，最大为200

class SalePromotionmanagementalldetailbatchRequest(LingXingModel):
    """Request for 查询管理促销详情+listing+订单(批量).
    
    POST /promotionApi/open/promotion/managementAllDetailBatch
    """
    itemList: List[SalePromotionmanagementalldetailbatchRequestItemlistItem]


class SalePromotionprimediscountalldetailbatchRequestItemlistItem(LingXingModel):
    promotionId: str  # 活动id
    storeId: str  # 店铺id
    orderPageNum: float  # 活动订单分页页数，最小为1
    orderPageSize: float  # 活动订单分页大小，最小为1，最大为200
    listingPageNum: float  # 活动listing分页页数，最小为1
    listingPageSize: float  # 活动listing分页大小，最小为1，最大为200

class SalePromotionprimediscountalldetailbatchRequest(LingXingModel):
    """Request for 查询会员折扣or价格折扣详情+listing+订单(批量).
    
    POST /promotionApi/open/promotion/primeDiscountAllDetailBatch
    """
    itemList: List[SalePromotionprimediscountalldetailbatchRequestItemlistItem]


class SalePromotionseckillalldetailbatchRequestItemlistItem(LingXingModel):
    promotionId: str  # 活动id
    storeId: str  # 店铺id
    orderPageNum: float  # 活动订单分页页数，最小为1
    orderPageSize: float  # 活动订单分页大小，最小为1,最大为200
    listingPageNum: float  # 活动listing分页页数，最小为1
    listingPageSize: float  # 活动listing分页大小，最小为1,最大为200

class SalePromotionseckillalldetailbatchRequest(LingXingModel):
    """Request for 查询秒杀详情+listing+订单(批量).
    
    POST /promotionApi/open/promotion/secKillAllDetailBatch
    """
    itemList: List[SalePromotionseckillalldetailbatchRequestItemlistItem]


class SalePromotionlistinglistRequest(LingXingModel):
    """Request for 查询商品折扣列表.
    
    POST /basicOpen/promotion/listingList
    """
    site_date: str  # 站点时间，格式：Y-m-d
    start_time: Optional[str] = None  # 开始时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_time: Optional[str] = None  # 结束时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    is_overlay: Optional[int] = None  # 是否优惠叠加： 0  否 1  是
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    status: Optional[list] = None  # 促销状态： 0  其他 1  进行中 2  已过期 3  未开始
    product_status: Optional[list] = None  # 商品状态： -1  已删除 0  停售 1  在售
    promotion_category: Optional[list] = None  # 促销类型： 1  优惠券 2  秒杀 3  管理促销 4   会员折扣


class SalePromotionlistingdetailcouponRequest(LingXingModel):
    """Request for 查询商品折扣详情-列表-优惠卷.
    
    POST /basicOpen/promotion/listingDetailCoupon
    """
    sellerSku: str  # seller_sku(msku)
    promotionType: Optional[list] = None  # 促销类型
    status: Optional[list] = None  # 促销状态： 0 其他 1 进行中 2 已过期 3 未开始
    storeId: str  # 店铺id
    startTime: str  # 活动开始时间
    endTime: str  # 活动结束时间
    sortField: str  # 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmoun
    sortType: str  # 排序类型 asc desc
    pageNum: float  # 分页页码
    pageSize: float  # 分页大小


class SalePromotionlistingdetailmanageRequest(LingXingModel):
    """Request for 查询商品折扣详情-列表-管理促销.
    
    POST /basicOpen/promotion/listingDetailManage
    """
    sellerSku: str  # seller_sku(msku)
    promotionType: Optional[list] = None  # 促销类型
    status: Optional[list] = None  # 促销状态
    storeId: str  # 店铺id
    startTime: str  # 活动开始时间
    endTime: str  # 活动结束时间
    sortField: str  # 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmoun
    sortType: str  # 排序类型 asc desc
    pageNum: float  # 分页页码
    pageSize: float  # 分页大小


class SalePromotionlistingdetailprimediscountRequest(LingXingModel):
    """Request for 查询商品折扣详情-列表-会员折扣.
    
    POST /basicOpen/promotion/listingDetailPrimeDiscount
    """
    sellerSku: str  # seller_sku(msku)
    promotionType: Optional[list] = None  # 促销类型
    status: Optional[list] = None  # 促销状态
    storeId: str  # 店铺id
    startTime: str  # 活动开始时间
    endTime: str  # 活动结束时间
    sortField: str  # 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmoun
    sortType: str  # 排序类型 asc desc
    pageNum: float  # 分页页码
    pageSize: float  # 分页大小


class SalePromotionlistingdetailseckillRequest(LingXingModel):
    """Request for 查询商品折扣详情-列表-秒杀.
    
    POST /basicOpen/promotion/listingDetailSecKill
    """
    sellerSku: str  # sellerSku
    promotionType: Optional[list] = None  # 促销类型
    status: Optional[list] = None  # 促销状态
    storeId: str  # 店铺id
    startTime: str  # 活动开始时间
    endTime: str  # 活动结束时间
    sortField: str  # 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmoun
    sortType: str  # 排序类型 asc desc
    pageNum: float  # 分页页码
    pageSize: float  # 分页大小


class SaleRefundOrderRequestDataItem(LingXingModel):
    orderItemId: str  # 商品行id
    asin: str  # asin
    sellerSku: str  # msku
    title: str  # 商品名称
    quantityOrdered: float  # 下单数量
    quantityShipped: float  # 到货数量
    reason: str  # 退款原因 CustomerReturn GeneralAdjustment
    asinUrl: Optional[str] = None  # asinUrl
    smallImageUrl: Optional[str] = None  # 商品图片
    unitPriceIcon: Optional[str] = None  # 商品单价货币符号
    unitPriceAmount: Optional[float] = None  # 单价
    itemList: Optional[list] = None  # 退款费用项目列表
    itemList__type: str  # 费用类型
    itemList__name: Optional[str] = None  # 费用名称
    itemList__currencyCode: str  # 货币编码
    itemList__icon: Optional[str] = None  # 货币符号
    itemList__amount: Optional[float] = None  # 金额
    itemList__refundedPrice: Optional[str] = None  # 已申请退款金额
    itemList__returnAmount: str  # 本次申请退款金额
    itemRefundTotal: Optional[Any] = None  # 是

class SaleRefundOrderRequest(LingXingModel):
    """Request for 订单退款.
    
    POST /basicOpen/openapi/salesOrder/refundOrder
    """
    sid: float  # 店铺id
    amazonOrderId: str  # 亚马逊订单ID
    purchaseDateLocal: str  # 订购时间
    data: SaleRefundOrderRequestDataItem


class SaleProductrelationbatchlinkRequestSidasinsItem(LingXingModel):
    sid: str  # 店铺id(seller表主键)
    asin: str  # asin

class SaleProductrelationbatchlinkRequest(LingXingModel):
    """Request for 配对/批量配对.
    
    POST /basicOpen/vcservice/productRelation/batchLink
    """
    productId: float  # 本地商品表主键ID
    isSyncPic: float  # 是否同步图片到本地商品
    sidAsins: List[SaleProductrelationbatchlinkRequestSidasinsItem]

"""Auto-generated response models for Service."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class CrmCustomerIndexList(LingXingModel):
    """list sub-structure."""
    buyer_email: Optional[str] = Field(None, description="买家邮箱")
    buyer_name: Optional[str] = Field(None, description="买家姓名")
    sid: Optional[list] = Field(None, description="店铺id")
    country: Optional[str] = Field(None, description="国家名称")
    order_items: Optional[float] = Field(None, description="总订单")
    volume: Optional[float] = Field(None, description="总销量")
    amount: Optional[float] = Field(None, description="总销售额")
    per_customer_transaction: Optional[float] = Field(None, description="平均客单价")
    currency_icon: Optional[str] = Field(None, description="币种")
    refund_number: Optional[float] = Field(None, description="退款订单数")
    refund_sales_number: Optional[float] = Field(None, description="退款销售数")
    refund_rate: Optional[float] = Field(None, description="退款率")
    return_number: Optional[float] = Field(None, description="退货订单数")
    return_sales_number: Optional[float] = Field(None, description="退货销量数")
    return_rate: Optional[float] = Field(None, description="退货率")
    feedback_number: Optional[float] = Field(None, description="Feedback评论数")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    feedback_bad_number: Optional[float] = Field(None, description="Feedback差评数")
    feedback_rate: Optional[float] = Field(None, description="Feedback留评率")
    feedback_bad_rate: Optional[float] = Field(None, description="Feedback差评率")
    first_purchase_date: Optional[str] = Field(None, description="首次购买时间")
    last_purchase_date: Optional[str] = Field(None, description="最近购买时间")
    remark: Optional[str] = Field(None, description="备注")
    group: Optional[list] = Field(None, description="分组")

class CrmCustomerIndexResponse(LingXingModel):
    """查询客户列表（新）."""
    list: Optional[List[CrmCustomerIndexList]] = Field(None, description="是")
    total: Optional[float] = Field(None, description="总数")
    total: Optional[int] = Field(None, description="总数")


class CustomerservicePerformancenoticeListList(LingXingModel):
    """list sub-structure."""
    id: Optional[float] = Field(None, description="主键ID")
    company_id: Optional[float] = Field(None, description="企业ID")
    performance_notice_uuid: Optional[str] = Field(None, description="唯一标识ID")
    sid: Optional[float] = Field(None, description="店铺ID")
    mail_id: Optional[str] = Field(None, description="亚马逊邮件唯一标识")
    subject: Optional[str] = Field(None, description="主题")
    status: Optional[float] = Field(None, description="处理状态：0（无），1（待处理），2（已处理），3（无需处理）")
    is_read: Optional[float] = Field(None, description="是否已读，-1 全部，0 未读，1 已读")
    content: Optional[str] = Field(None, description="内容")
    mail_create_date: Optional[str] = Field(None, description="亚马逊邮件创建时间")
    tag_list: Optional[list] = Field(None, description="邮件标签信息列表")

class CustomerservicePerformancenoticeListResponse(LingXingModel):
    """查询业绩通知列表."""
    list: Optional[List[CustomerservicePerformancenoticeListList]] = Field(None, description="是")
    total: Optional[float] = Field(None, description="总数")
    last_update_date: Optional[str] = Field(None, description="最后更新时间")
    total: Optional[int] = Field(None, description="总数")


class CustomerserviceRmamanageListRecords(LingXingModel):
    """records sub-structure."""
    id: Optional[str] = Field(None, description="id")
    create_time: Optional[str] = Field(None, description="创建时间")
    rma_no: Optional[str] = Field(None, description="rma编号")
    sid: Optional[float] = Field(None, description="店铺id")
    creator: Optional[str] = Field(None, description="创建人")
    amazon_order_id: Optional[str] = Field(None, description="订单号")
    asin: Optional[str] = Field(None, description="asin")
    seller_sku: Optional[str] = Field(None, description="msku")
    item_name: Optional[str] = Field(None, description="商品描述")
    sku: Optional[str] = Field(None, description="本地sku")
    local_name: Optional[str] = Field(None, description="本地品名")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家")
    channel_source_name: Optional[str] = Field(None, description="渠道来源名称")
    channel_source: Optional[float] = Field(None, description="渠道来源id")
    after_sale_type_name: Optional[str] = Field(None, description="售后类型名称")
    after_sale_type: Optional[str] = Field(None, description="售后类型id")
    after_sale_count: Optional[float] = Field(None, description="售后数量")
    process_way_name: Optional[str] = Field(None, description="处理方式名称")
    process_way: Optional[str] = Field(None, description="处理方式id")
    buyer_name: Optional[str] = Field(None, description="买家名")
    buyer_email: Optional[str] = Field(None, description="买家邮箱")
    purchase_date_local: Optional[str] = Field(None, description="订购时间")

class CustomerserviceRmamanageListResponse(LingXingModel):
    """查询RMA管理."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[int] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[int] = Field(None, description="是")
    has_previous_page: Optional[int] = Field(None, description="是")
    records: Optional[List[CustomerserviceRmamanageListRecords]] = Field(None, description="返回结果数据")


class CustomerserviceStoretargetDetailAccounthealthrating(LingXingModel):
    """accountHealthRating sub-structure."""
    ahr_score: Optional[str] = Field(None, description="账户健康评分")
    ahr_status: Optional[str] = Field(None, description="账户健康状态")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailCommoditypolicycompliance(LingXingModel):
    """commodityPolicyCompliance sub-structure."""
    count: Optional[str] = Field(None, description="总数")
    customer_product_reviews_policy_violations: Optional[str] = Field(None, description="违反买家商品评论政策")
    food_and_product_safety_issues: Optional[str] = Field(None, description="食品和商品安全问题")
    intellectual_property_data: Optional[str] = Field(None, description="知识产权投诉")
    listing_policy_data: Optional[str] = Field(None, description="上架政策违规")
    other_policy_violations: Optional[str] = Field(None, description="其他违反政策")
    policy_violation_warnings: Optional[str] = Field(None, description="违反政策警告")
    product_authenticity_data: Optional[str] = Field(None, description="商品真实性买家投诉")
    product_condition_customer_complaints: Optional[str] = Field(None, description="商品状况买家投诉")
    product_safety_data: Optional[str] = Field(None, description="商品安全投诉")
    restricted_product_policy_violations: Optional[str] = Field(None, description="违反受限商品政策")
    suspected_intellectual_property_violations: Optional[str] = Field(None, description="涉嫌侵犯知识产权")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailFbaorderwithdefect(LingXingModel):
    """fbaOrderWithDefect sub-structure."""
    child: Optional[dict] = Field(None, description="子项详情对象")
    count: Optional[str] = Field(None, description="FBA订单缺陷数")
    order_count: Optional[str] = Field(None, description="FBA订单总数")
    rate: Optional[str] = Field(None, description="FBA订单缺陷率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailInvoicedefect(LingXingModel):
    """invoiceDefect sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    invoice_defect_count: Optional[str] = Field(None, description="发票缺失订单数")
    late_invoice_count: Optional[str] = Field(None, description="逾期发票订单数")
    missing_invoice_count: Optional[str] = Field(None, description="遗失发票订单数")
    order_count: Optional[str] = Field(None, description="订单总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailLateshipment(LingXingModel):
    """lateShipment sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    order_count: Optional[str] = Field(None, description="订单总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailOntimedelivery(LingXingModel):
    """onTimeDelivery sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    order_count: Optional[str] = Field(None, description="订单总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailOrderwithdefect(LingXingModel):
    """orderWithDefect sub-structure."""
    child: Optional[dict] = Field(None, description="子项详情对象")
    count: Optional[str] = Field(None, description="FBM订单缺陷数")
    order_count: Optional[str] = Field(None, description="FBM订单总数")
    rate: Optional[str] = Field(None, description="FBM订单缺陷率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailPrefulfillmentcancellation(LingXingModel):
    """preFulfillmentCancellation sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    order_count: Optional[str] = Field(None, description="订单总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailStandard(LingXingModel):
    """standard sub-structure."""
    commodity_policy_compliance: Optional[str] = Field(None, description="商品政策合规性评分标准，百分比")
    fba_order_with_defect: Optional[str] = Field(None, description="FBA订单缺陷率评分标准，百分比")
    invoice_defect: Optional[str] = Field(None, description="发票缺陷评分标准，百分比")
    late_shipment: Optional[str] = Field(None, description="迟发率评分标准，百分比")
    on_time_delivery: Optional[str] = Field(None, description="准时交货率评分标准，百分比")
    order_with_defect: Optional[str] = Field(None, description="订单缺陷率评分标准，百分比")
    pre_fulfillment_cancellation: Optional[str] = Field(None, description="预配送取消率评分标准，百分比")
    return_dissatisfaction: Optional[str] = Field(None, description="退货不满意度评分标准，百分比")
    unit_on_time_delivery: Optional[str] = Field(None, description="单位准时交货率评分标准，百分比")
    valid_tracking: Optional[int] = Field(None, description="有效追踪率评分标准，百分比")

class CustomerserviceStoretargetDetailUnitontimedelivery(LingXingModel):
    """unitOnTimeDelivery sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    order_count: Optional[str] = Field(None, description="订单总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailValidtracking(LingXingModel):
    """validTracking sub-structure."""
    count: Optional[str] = Field(None, description="比率对应的数量")
    order_count: Optional[str] = Field(None, description="货件总数")
    rate: Optional[str] = Field(None, description="比率，百分比")
    window_day_count: Optional[str] = Field(None, description="窗口期的天数")
    window_time_end: Optional[str] = Field(None, description="窗口期的结束日期")
    window_time_start: Optional[str] = Field(None, description="窗口期的开始日期")

class CustomerserviceStoretargetDetailResponse(LingXingModel):
    """查询店铺绩效详情."""
    account_health_rating: Optional[List[CustomerserviceStoretargetDetailAccounthealthrating]] = Field(None, description="账户健康评级对象")
    commodity_policy_compliance: Optional[List[CustomerserviceStoretargetDetailCommoditypolicycompliance]] = Field(None, description="商品政策合规性对象")
    fba_order_with_defect: Optional[List[CustomerserviceStoretargetDetailFbaorderwithdefect]] = Field(None, description="FBA订单缺陷率对象")
    invoice_defect: Optional[List[CustomerserviceStoretargetDetailInvoicedefect]] = Field(None, description="发票缺陷率对象")
    late_shipment: Optional[List[CustomerserviceStoretargetDetailLateshipment]] = Field(None, description="迟发率对象")
    on_time_delivery: Optional[List[CustomerserviceStoretargetDetailOntimedelivery]] = Field(None, description="准时交货率对象")
    on_time_delivery_source: Optional[int] = Field(None, description="准时交货率数据来源 1：取'onTimeDelivery' 2：取'unitOnTimeDelivery'")
    order_with_defect: Optional[List[CustomerserviceStoretargetDetailOrderwithdefect]] = Field(None, description="FBM订单缺陷率对象")
    pre_fulfillment_cancellation: Optional[List[CustomerserviceStoretargetDetailPrefulfillmentcancellation]] = Field(None, description="预配送取消率对象")
    pull_date: Optional[str] = Field(None, description="报表获取时间日期，日期格式：yyyy-MM-dd")
    standard: Optional[List[CustomerserviceStoretargetDetailStandard]] = Field(None, description="评分标准对象")
    unit_on_time_delivery: Optional[List[CustomerserviceStoretargetDetailUnitontimedelivery]] = Field(None, description="单位准时交货率对象")
    update_date: Optional[str] = Field(None, description="报表数据更新时间，日期格式：yyyy-MM-dd")
    valid_tracking: Optional[List[CustomerserviceStoretargetDetailValidtracking]] = Field(None, description="有效追踪率对象")
    total: Optional[int] = Field(None, description="总记录数")


class CustomerserviceStoretargetListResponse(LingXingModel):
    """查询店铺绩效列表."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    pull_date: Optional[str] = Field(None, description="报表获取日期")
    update_date: Optional[str] = Field(None, description="报表数据更新时间")
    order_with_defect: Optional[str] = Field(None, description="fbm订单缺陷率，百分比")
    return_dissatisfaction: Optional[str] = Field(None, description="退货不满意度，百分比")
    late_shipment: Optional[str] = Field(None, description="迟发率，百分比")
    pre_fulfillment_cancellation: Optional[str] = Field(None, description="预配送取消率，百分比")
    valid_tracking: Optional[str] = Field(None, description="有效追踪率，百分比")
    on_time_delivery: Optional[str] = Field(None, description="准时交货率，百分比")
    commodity_policy_compliance: Optional[str] = Field(None, description="商品政策合规性")
    fba_order_with_defect: Optional[str] = Field(None, description="fba订单缺陷率，百分比")
    invoice_defect: Optional[str] = Field(None, description="发票缺陷率，百分比")
    ahr_score: Optional[str] = Field(None, description="账户状况分数")
    ahr_status: Optional[str] = Field(None, description="账户状况评级")


class CustomerserviceVoiceofbuyerListResponse(LingXingModel):
    """查询买家之声列表."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家名称")
    image_url: Optional[str] = Field(None, description="图片地址")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    title: Optional[str] = Field(None, description="标题")
    msku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    fulfillment_channel: Optional[str] = Field(None, description="配送方式： FBA FBA MFN FBM")
    ncx_rate: Optional[str] = Field(None, description="不满意率")
    ncx_count: Optional[int] = Field(None, description="不满意订单数量")
    order_count: Optional[int] = Field(None, description="订单总数")
    most_common_return_reason_bucket: Optional[str] = Field(None, description="主要退货原因")
    last_action_date: Optional[str] = Field(None, description="最近停售日期")
    event_date: Optional[str] = Field(None, description="上次更新日期")
    pcx_health_text: Optional[str] = Field(None, description="满意度状况说明")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    listing_exists: Optional[bool] = Field(None, description="是否删除： true 删除 false 不删除")
    star_rating: Optional[str] = Field(None, description="评分")
    return_badge: Optional[str] = Field(None, description="退货标记")
    return_rate: Optional[str] = Field(None, description="退货率")


class V3MwsReviewsLocalInfo(LingXingModel):
    """local_info sub-structure."""
    local_sku: Optional[str] = Field(None, description="本地SKU")
    local_name: Optional[str] = Field(None, description="本地品名")
    category_name: Optional[str] = Field(None, description="分类名")

class V3MwsReviewsAmazonOrderList(LingXingModel):
    """amazon_order_list sub-structure."""
    seller_name: Optional[str] = Field(None, description="店铺")
    amazon_order_id: Optional[str] = Field(None, description="订单号")
    buyer_email: Optional[str] = Field(None, description="买家邮箱")

class V3MwsReviewsResponse(LingXingModel):
    """查询评论管理 - Review(新)."""
    small_image_url: Optional[str] = Field(None, description="图片")
    asin: Optional[str] = Field(None, description="ASIN")
    seller_sku: Optional[list] = Field(None, description="MSKU")
    last_star: Optional[float] = Field(None, description="评级 - 星级")
    last_title: Optional[str] = Field(None, description="评级 - 标签")
    review_likes: Optional[float] = Field(None, description="点赞数")
    review_id: Optional[str] = Field(None, description="Review ID")
    review_url: Optional[str] = Field(None, description="评价链接")
    last_content: Optional[str] = Field(None, description="评价内容")
    parent_asin: Optional[list] = Field(None, description="父ASIN")
    item_name: Optional[list] = Field(None, description="标题")
    local_info: Optional[List[V3MwsReviewsLocalInfo]] = Field(None, description="本地信息")
    author: Optional[str] = Field(None, description="买家信息")
    images: Optional[list] = Field(None, description="评论图片链接")
    videos: Optional[list] = Field(None, description="评论视频链接")
    is_vp: Optional[int] = Field(None, description="是")
    seller_name: Optional[list] = Field(None, description="店铺")
    marketplace: Optional[str] = Field(None, description="国家")
    review_date: Optional[str] = Field(None, description="评价时间")
    create_time: Optional[str] = Field(None, description="创建时间")
    update_time: Optional[str] = Field(None, description="更新时间")
    crawl_date: Optional[str] = Field(None, description="操作时间")
    amazon_order_list: Optional[List[V3MwsReviewsAmazonOrderList]] = Field(None, description="订单号列表")
    buyer_email: Optional[list] = Field(None, description="买家邮箱")
    remark: Optional[str] = Field(None, description="备注")
    status: Optional[float] = Field(None, description="处理状态：0 待处理，1 处理中，2 已完成")
    tags: Optional[list] = Field(None, description="标签")
    cs_principals: Optional[list] = Field(None, description="处理人")
    total: Optional[int] = Field(None, description="总数")


class CrmCustomerListResponse(LingXingModel):
    """查询客户列表（旧）."""
    store_name: Optional[str] = Field(None, description="店铺名称")
    country_name: Optional[str] = Field(None, description="国家名称")
    group: Optional[list] = Field(None, description="分组")
    order_items: Optional[float] = Field(None, description="总订单")
    volume: Optional[float] = Field(None, description="总销量")
    amount: Optional[float] = Field(None, description="总销售额")
    per_customer_transaction: Optional[float] = Field(None, description="平均客单价")
    currency_icon: Optional[str] = Field(None, description="币种符号")
    refund_number: Optional[float] = Field(None, description="退款订单数")
    refund_sales_number: Optional[dict] = Field(None, description="退款销售数")
    refund_rate: Optional[dict] = Field(None, description="退款率")
    return_number: Optional[float] = Field(None, description="退货订单数")
    return_sales_number: Optional[float] = Field(None, description="退货销量数")
    return_rate: Optional[float] = Field(None, description="退货率")
    feedback_number: Optional[str] = Field(None, description="Feedback评论数")
    feedback_bad_number: Optional[str] = Field(None, description="Feedback差评数")
    feedback_rate: Optional[str] = Field(None, description="留平率")
    first_purchase_date: Optional[str] = Field(None, description="首次购买时间")
    last_purchase_date: Optional[str] = Field(None, description="最近购买时间")
    total: Optional[int] = Field(None, description="总数")


class CsFeedbackListProductlist(LingXingModel):
    """productList sub-structure."""
    title: Optional[str] = Field(None, description="商品标题")
    asin: Optional[str] = Field(None, description="asin")
    seller_sku: Optional[str] = Field(None, description="msku")

class CsFeedbackListResponse(LingXingModel):
    """查询评价管理 4-5星Feedback列表."""
    sid: Optional[int] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家")
    star: Optional[float] = Field(None, description="星级")
    amazon_order_id: Optional[str] = Field(None, description="订单号")
    feedback_date: Optional[str] = Field(None, description="评论时间")
    feedback_content: Optional[str] = Field(None, description="评论内容")
    update_time: Optional[str] = Field(None, description="更新时间")
    operation_time: Optional[str] = Field(None, description="操作时间")
    remark: Optional[str] = Field(None, description="备注")
    status: Optional[int] = Field(None, description="feedback处理状态： 0 待处理 1 处理中 2 已完成")
    product_list: Optional[List[CsFeedbackListProductlist]] = Field(None, description="商品信息")
    total: Optional[int] = Field(None, description="总数")


class CsFeedbackListmwsProductlist(LingXingModel):
    """productList sub-structure."""
    title: Optional[str] = Field(None, description="商品标题")
    asin: Optional[str] = Field(None, description="asin")
    seller_sku: Optional[str] = Field(None, description="msku")

class CsFeedbackListmwsResponse(LingXingModel):
    """查询评价管理 1-3星Feedback列表."""
    sid: Optional[int] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家")
    star: Optional[float] = Field(None, description="星级")
    amazon_order_id: Optional[str] = Field(None, description="订单号")
    feedback_date: Optional[str] = Field(None, description="评论时间")
    feedback_content: Optional[str] = Field(None, description="评论内容")
    update_time: Optional[str] = Field(None, description="更新时间")
    operation_time: Optional[str] = Field(None, description="操作时间")
    remark: Optional[str] = Field(None, description="备注")
    status: Optional[float] = Field(None, description="feedback处理状态： 0 待处理 1 处理中 2 已完成")
    product_list: Optional[List[CsFeedbackListmwsProductlist]] = Field(None, description="商品信息")
    total: Optional[int] = Field(None, description="总数")


class CsFeedbackreportDetailResponse(LingXingModel):
    """查询评价统计-Feedback每日新增数."""
    report_date: Optional[str] = Field(None, description="日期")
    feedback_num: Optional[float] = Field(None, description="每日feedback新增数")
    five_star: Optional[float] = Field(None, description="5星feedback新增数")
    four_star: Optional[float] = Field(None, description="4星feedback新增数")
    three_star: Optional[float] = Field(None, description="3星feedback新增数")
    two_star: Optional[float] = Field(None, description="2星feedback新增数")
    one_star: Optional[float] = Field(None, description="1星feedback新增数")
    total: Optional[int] = Field(None, description="总数")


class CsFeedbackreportListsResponse(LingXingModel):
    """查询评价统计-Feedback列表."""
    count_lifetime: Optional[float] = Field(None, description="feedback总数")
    count_12: Optional[float] = Field(None, description="近1年feedback数")
    count_30: Optional[float] = Field(None, description="近30天feedback数")
    count_90: Optional[float] = Field(None, description="近90天feedback数")
    feedback_num: Optional[float] = Field(None, description="feedback获取总数")
    five_star: Optional[float] = Field(None, description="五星feedback获取数")
    four_star: Optional[float] = Field(None, description="四星feedback获取数")
    three_star: Optional[float] = Field(None, description="三星feedback获取数")
    two_star: Optional[float] = Field(None, description="二星feedback获取数")
    one_star: Optional[float] = Field(None, description="一星feedback获取数")
    modified_num: Optional[float] = Field(None, description="feedback删评数")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家")
    score: Optional[float] = Field(None, description="评分")
    negative_lifetime: Optional[float] = Field(None, description="feedback累计差评率")
    neutral_lifetime: Optional[float] = Field(None, description="feedback累计中评率")
    positive_lifetime: Optional[float] = Field(None, description="feedback累计好评率")
    total: Optional[int] = Field(None, description="总数")


class CsReviewreportDetailResponse(LingXingModel):
    """查询评价统计-Review每日新增数."""
    report_date: Optional[str] = Field(None, description="日期")
    review_num: Optional[float] = Field(None, description="review新增数")
    five_star: Optional[float] = Field(None, description="5星review新增数")
    four_star: Optional[float] = Field(None, description="4星review新增数")
    three_star: Optional[float] = Field(None, description="3星review新增数")
    two_star: Optional[float] = Field(None, description="2星review新增数")
    one_star: Optional[float] = Field(None, description="1星review新增数")
    ratings: Optional[float] = Field(None, description="rating总数")
    ratings_inc: Optional[float] = Field(None, description="rating新增数 备注：可以为负值，代表减少数")
    total: Optional[int] = Field(None, description="总数")


class MailDetailAttachments(LingXingModel):
    """attachments sub-structure."""
    name: Optional[str] = Field(None, description="附件名称")
    size: Optional[float] = Field(None, description="附件大小（b）")

class MailDetailResponse(LingXingModel):
    """查询邮件详情."""
    webmail_uuid: Optional[str] = Field(None, description="邮件唯一标识")
    subject: Optional[str] = Field(None, description="邮件标题")
    from_name: Optional[str] = Field(None, description="发件人姓名")
    from_address: Optional[str] = Field(None, description="发件人地址")
    to_address_all: Optional[str] = Field(None, description="所有收件人地址")
    date: Optional[str] = Field(None, description="日期")
    cc: Optional[str] = Field(None, description="抄送")
    bcc: Optional[str] = Field(None, description="密送地址")
    text_html: Optional[str] = Field(None, description="邮件内容")
    text_plain: Optional[str] = Field(None, description="纯文本的邮件内容")
    attachments: Optional[List[MailDetailAttachments]] = Field(None, description="附件")
    type: Optional[str] = Field(None, description="邮件类型 0、QA 1、买家邮件 2、亚马逊邮件 3、站外邮件")
    total: Optional[int] = Field(None, description="总数")


class MailListsResponse(LingXingModel):
    """查询邮件列表."""
    webmail_uuid: Optional[str] = Field(None, description="邮件唯一标识")
    date: Optional[str] = Field(None, description="日期")
    subject: Optional[str] = Field(None, description="邮件标题")
    from_name: Optional[str] = Field(None, description="发件人姓名")
    from_address: Optional[str] = Field(None, description="发件人地址")
    to_name: Optional[str] = Field(None, description="接收人")
    to_address: Optional[str] = Field(None, description="接收人地址")
    has_attachment: Optional[int] = Field(None, description="是否存在附件： 1 存在 0 不存在")
    total: Optional[int] = Field(None, description="总数")


class CsReviewreportListsLocalInfo(LingXingModel):
    """local_info sub-structure."""
    local_sku: Optional[str] = Field(None, description="sku")
    local_name: Optional[str] = Field(None, description="品名")

class CsReviewreportListsSellerList(LingXingModel):
    """seller_list sub-structure."""
    sid: Optional[int] = Field(None, description="sid")
    seller_name: Optional[str] = Field(None, description="店铺名称")

class CsReviewreportListsResponse(LingXingModel):
    """查询评价统计-Review列表."""
    total: Optional[int] = Field(None, description="总数")
    ratings: Optional[float] = Field(None, description="子rating总数")
    five_star: Optional[float] = Field(None, description="5星review新增数")
    four_star: Optional[float] = Field(None, description="4星review新增数")
    three_star: Optional[float] = Field(None, description="3星review新增数")
    two_star: Optional[float] = Field(None, description="2星review新增数")
    one_star: Optional[float] = Field(None, description="1星review新增数")
    review_num: Optional[float] = Field(None, description="review数")
    good_num: Optional[float] = Field(None, description="review好评数")
    negative_num: Optional[float] = Field(None, description="review中差评数")
    good_rate: Optional[float] = Field(None, description="review好评率")
    negative_rate: Optional[float] = Field(None, description="review中差评率")
    modified_num: Optional[float] = Field(None, description="review改评数")
    remove_num: Optional[float] = Field(None, description="review删评数")
    asin: Optional[str] = Field(None, description="子asin")
    asin_url: Optional[str] = Field(None, description="asin链接")
    image_url: Optional[str] = Field(None, description="图片链接")
    title: Optional[str] = Field(None, description="商品标题")
    country: Optional[str] = Field(None, description="国家")
    score: Optional[float] = Field(None, description="评分")
    mark: Optional[float] = Field(None, description="仅评分数")
    seller_name: Optional[list] = Field(None, description="店铺名称")
    local_info: Optional[List[CsReviewreportListsLocalInfo]] = Field(None, description="是")
    parent_asin: Optional[list] = Field(None, description="父asin")
    seller_list: Optional[List[CsReviewreportListsSellerList]] = Field(None, description="店铺列表")


class V2MwsReviewsAttachments(LingXingModel):
    """attachments sub-structure."""
    type: Optional[str] = Field(None, description="附件类型：image 图片，video 视频")
    url: Optional[str] = Field(None, description="链接地址")

class V2MwsReviewsResponse(LingXingModel):
    """查询评价管理-Review."""
    asin: Optional[str] = Field(None, description="ASIN")
    last_star: Optional[int] = Field(None, description="星级")
    last_title: Optional[str] = Field(None, description="评论标题")
    last_content: Optional[str] = Field(None, description="评价内容")
    review_likes: Optional[int] = Field(None, description="点赞数")
    author: Optional[str] = Field(None, description="评论客户")
    author_id: Optional[str] = Field(None, description="评论客户id")
    review_date: Optional[str] = Field(None, description="评论时间")
    review_id: Optional[str] = Field(None, description="Review ID")
    status: Optional[int] = Field(None, description="处理状态：0 待处理，1 处理中，2 已完成")
    update_time: Optional[int] = Field(None, description="更新时间，时间戳")
    create_time: Optional[int] = Field(None, description="创建时间，时间戳")
    review_modified_status: Optional[int] = Field(None, description="评论状态：-1 已删除，0 无标识，1 已变更")
    remark: Optional[str] = Field(None, description="备注")
    amazon_order_list: Optional[list] = Field(None, description="匹配订单列表")
    marketplace: Optional[str] = Field(None, description="国家")
    is_vp: Optional[int] = Field(None, description="是否是VP：0 否，1 是")
    is_er: Optional[int] = Field(None, description="是否是ER：0 否，1 是")
    is_topc: Optional[int] = Field(None, description="是否是TOPC：0 否，1 是")
    is_topr: Optional[int] = Field(None, description="是否是TOPR：0 否，1 是")
    is_vine: Optional[int] = Field(None, description="是否是VINE：0 否，1 是")
    asin_url: Optional[str] = Field(None, description="ASIN 链接")
    review_url: Optional[str] = Field(None, description="评价链接")
    seller_name: Optional[list] = Field(None, description="店铺名")
    sids: Optional[list] = Field(None, description="店铺ID")
    attachments: Optional[List[V2MwsReviewsAttachments]] = Field(None, description="附件")
    total: Optional[int] = Field(None, description="总数")


class ReturnsWorkorderListList(LingXingModel):
    """list sub-structure."""
    rma_id: Optional[str] = Field(None, description="售后单号")
    rma_type: Optional[int] = Field(None, description="售后类型： 1 退货退款 2 仅退货 3 仅退款 4 退货补发 5 补发")
    status: Optional[str] = Field(None, description="状态【售后单状态/订单状态】")
    order_number: Optional[str] = Field(None, description="系统单号")
    platform_code: Optional[str] = Field(None, description="平台code")
    country: Optional[str] = Field(None, description="国家")
    store_name: Optional[str] = Field(None, description="店铺名称")
    rma_from: Optional[int] = Field(None, description="单据来源：1 手工创建，2 线上同步")
    rma_reason: Optional[str] = Field(None, description="售后原因")
    return_warehouse_code: Optional[str] = Field(None, description="退货仓库id")
    return_warehouse_name: Optional[str] = Field(None, description="退货仓库名称")
    return_type_code: Optional[int] = Field(None, description="退货类型：1 买家退货，2 卖家退货")
    return_logistice_type_code: Optional[int] = Field(None, description="物流类型：1 自选物流，2 三方物流")
    return_logistics: Optional[str] = Field(None, description="物流商")
    tracking_number: Optional[str] = Field(None, description="跟踪号")
    estimate_arrive_date: Optional[str] = Field(None, description="预计到货时间")
    order_amount: Optional[str] = Field(None, description="订单金额")
    returen_method: Optional[int] = Field(None, description="退款方式：0 无选择，1 手动退款")
    refund_status: Optional[str] = Field(None, description="退款状态： 待退款 退款中 退款失败 退款完成")
    comment: Optional[str] = Field(None, description="备注")
    create_time: Optional[str] = Field(None, description="创建时间")
    update_time: Optional[str] = Field(None, description="更新时间")
    complete_time: Optional[str] = Field(None, description="完成时间")
    tag_list: Optional[list] = Field(None, description="标签信息")
    refund: Optional[list] = Field(None, description="退款信息")
    rma_info: Optional[list] = Field(None, description="售后信息")
    related_info: Optional[list] = Field(None, description="关联单据")

class ReturnsWorkorderListResponse(LingXingModel):
    """查询售后工单列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[ReturnsWorkorderListList]] = Field(None, description="列表信息")


class ReturnsWorkOrderListResponse(LingXingModel):
    """查询售后工单列表 (/pb/mp/returns/workOrder/list)."""
    msg: Optional[str] = None

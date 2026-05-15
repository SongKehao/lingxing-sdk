"""Auto-generated response models for Sale."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class FbmmanagementModifyfbminventoryFailuredetail(LingXingModel):
    """failureDetail sub-structure."""
    store_id: Optional[int] = Field(None, description="店铺id")
    asin: Optional[str] = Field(None, description="asin")
    msku: Optional[str] = Field(None, description="msku")
    msg: Optional[str] = Field(None, description="错误信息")

class FbmmanagementModifyfbminventoryResponse(LingXingModel):
    """修改 FBM库存&处理时间."""
    total: Optional[int] = Field(None, description="总数(默认为0)")
    success_num: Optional[int] = Field(None, description="成功数量")
    failure_num: Optional[int] = Field(None, description="失败数量")
    failure_detail: Optional[List[FbmmanagementModifyfbminventoryFailuredetail]] = Field(None, description="错误信息详情")


class B2bpriceModifypriceFailureDetailList(LingXingModel):
    """failure_detail_list sub-structure."""
    sid: Optional[int] = Field(None, description="店铺id")
    msku: Optional[str] = Field(None, description="MSKU")
    asin: Optional[str] = Field(None, description="ASIN")
    msg: Optional[str] = Field(None, description="失败原因")

class B2bpriceModifypriceResponse(LingXingModel):
    """修改B2B价格."""
    total: Optional[int] = Field(None, description="总数")
    success_num: Optional[int] = Field(None, description="成功数量")
    failure_num: Optional[int] = Field(None, description="失败数量")
    failure_detail_list: Optional[List[B2bpriceModifypriceFailureDetailList]] = Field(None, description="修改失败数据")


class ListingPageListResponse(LingXingModel):
    """查询Listing标签列表."""
    total: Optional[int] = Field(None, description="总数")
    global_tag_id: Optional[str] = Field(None, description="标签id")
    tag_name: Optional[str] = Field(None, description="标签名称")
    type: Optional[str] = Field(None, description="标签类型")
    relation_count: Optional[int] = Field(None, description="标签条目")
    tag_object: Optional[str] = Field(None, description="标签对象")
    create_by_name: Optional[str] = Field(None, description="创建人名称")
    modify_by_name: Optional[str] = Field(None, description="最后编辑人名称")
    create_by: Optional[str] = Field(None, description="创建时间")
    modify_by: Optional[str] = Field(None, description="更新时间")


class ListingmanageListingoperatelogPagelistResponse(LingXingModel):
    """查询Listing操作日志列表."""
    total: Optional[int] = Field(None, description="总数")
    operate_time: Optional[str] = Field(None, description="操作时间")
    operate_user: Optional[str] = Field(None, description="操作人名称")
    operate_type: Optional[int] = Field(None, description="操作类型")
    operate_type_text: Optional[str] = Field(None, description="操作类型说明")
    operate_detail: Optional[str] = Field(None, description="详情")
    sid: Optional[str] = Field(None, description="店铺id")


class ModuleAdjustpriceAdjustpricemanualList(LingXingModel):
    """list sub-structure."""
    msku: Optional[str] = Field(None, description="亚马逊卖家sku")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    asin: Optional[str] = Field(None, description="ASIN")
    sid: Optional[float] = Field(None, description="店铺id")
    processing_status: Optional[float] = Field(None, description="调价状态")
    failure_reason: Optional[str] = Field(None, description="调价失败原因，当处理状态为“调价失败”该字段有值")
    finish_time: Optional[str] = Field(None, description="完成时间")
    create_time: Optional[str] = Field(None, description="创建时间")
    adjust_type: Optional[float] = Field(None, description="调价类型")
    profit_estimate: Optional[dict] = Field(None, description="预估利润")
    store_name: Optional[str] = Field(None, description="店铺名")
    marketplace: Optional[str] = Field(None, description="国家")
    create_user: Optional[str] = Field(None, description="创建人")
    processing_status_text: Optional[str] = Field(None, description="调价状态文字说明")
    adjust_before_obj: Optional[dict] = Field(None, description="调价前详情")
    adjust_after_obj: Optional[dict] = Field(None, description="调价后详情")
    adjust_range: Optional[dict] = Field(None, description="调价幅度")
    asin_url: Optional[str] = Field(None, description="asin跳转亚马逊前台链接")
    business_id: Optional[str] = Field(None, description="调价记录id")
    can_audit: Optional[float] = Field(None, description="是否可以审批 1是 0不是")
    small_image_url: Optional[str] = Field(None, description="商品缩略图地址")
    local_sku: Optional[str] = Field(None, description="本地产品SKU")
    local_name: Optional[str] = Field(None, description="品名")
    adjust_before: Optional[list] = Field(None, description="调整前")
    adjust_after: Optional[list] = Field(None, description="调整后")
    audit_info: Optional[Any] = Field(None, description="审批信息，审批中")

class ModuleAdjustpriceAdjustpricemanualResponse(LingXingModel):
    """查询调价队列."""
    count: Optional[float] = Field(None, description="总记录数")
    list: Optional[List[ModuleAdjustpriceAdjustpricemanualList]] = Field(None, description="数据列表")
    total: Optional[int] = Field(None, description="总数")


class PublishManageCategorychildrenCategory(LingXingModel):
    """category sub-structure."""
    category_unique_id: Optional[str] = Field(None, description="类目唯一ID")
    category_name: Optional[str] = Field(None, description="类目名称")
    category_id: Optional[float] = Field(None, description="亚马逊定义的类目ID")
    marketplace_id: Optional[str] = Field(None, description="市场ID")
    parent_id: Optional[float] = Field(None, description="父级ID")
    is_root: Optional[float] = Field(None, description="否为根类目（1为根，0为子）")
    has_children: Optional[float] = Field(None, description="是否包含子类目（1有，0无）")
    child_category: Optional[list] = Field(None, description="子类目id列表")
    product_type_origin: Optional[list] = Field(None, description="商品原始类型")

class PublishManageCategorychildrenCategorychildren(LingXingModel):
    """categoryChildren sub-structure."""
    category_unique_id: Optional[str] = Field(None, description="类目唯一ID")
    category_name: Optional[str] = Field(None, description="类目名称")
    category_id: Optional[float] = Field(None, description="类目ID")
    marketplace_id: Optional[str] = Field(None, description="市场ID")
    parent_id: Optional[float] = Field(None, description="父级ID")
    is_root: Optional[float] = Field(None, description="否为根类目（1为根，0为子）")
    has_children: Optional[float] = Field(None, description="是否包含子类目（1有，0无）")
    child_category: Optional[list] = Field(None, description="子类目id列表")
    product_type_origin: Optional[list] = Field(None, description="商品原始类型")
    browse_node_attributes: Optional[dict] = Field(None, description="类目节点属性")
    category_path_id: Optional[dict] = Field(None, description="类目路径ID")
    category_path_name: Optional[dict] = Field(None, description="类目路径名称")

class PublishManageCategorychildrenResponse(LingXingModel):
    """刊登管理-查询 Amazon 子分类."""
    category: Optional[List[PublishManageCategorychildrenCategory]] = Field(None, description="类目对象")
    category_children: Optional[List[PublishManageCategorychildrenCategorychildren]] = Field(None, description="子类目列表")
    total: Optional[int] = Field(None, description="子类目总数")


class PublishManageCategoryrootCategory(LingXingModel):
    """category sub-structure."""
    category_unique_id: Optional[str] = Field(None, description="类目唯一ID")
    category_name: Optional[str] = Field(None, description="类目名称")
    category_id: Optional[float] = Field(None, description="亚马逊定义的类目ID")
    marketplace_id: Optional[str] = Field(None, description="市场ID")
    parent_id: Optional[float] = Field(None, description="父级ID")
    is_root: Optional[float] = Field(None, description="否为根类目（1为根，0为子）")
    has_children: Optional[float] = Field(None, description="是否包含子类目（1有，0无）")
    child_category: Optional[list] = Field(None, description="子类目ID列表")

class PublishManageCategoryrootResponse(LingXingModel):
    """刊登管理-查询 Amazon 根分类."""
    category: Optional[List[PublishManageCategoryrootCategory]] = Field(None, description="类目列表")
    total: Optional[int] = Field(None, description="总数")


class PublishManageGetmerchantshippinggroupResponse(LingXingModel):
    """刊登管理-获取运费模板."""
    name: Optional[str] = Field(None, description="运费模板名称")
    value: Optional[str] = Field(None, description="运费模板id")
    total: Optional[int] = Field(None, description="总数")


class PublishManageGetproducttypeProducttype(LingXingModel):
    """productType sub-structure."""
    product_type_unique_id: Optional[str] = Field(None, description="商品类型唯一id")
    marketplace_id: Optional[str] = Field(None, description="市场id")
    product_type_origin: Optional[str] = Field(None, description="商品类型")
    display_name: Optional[str] = Field(None, description="商品类型名称")
    properties: Optional[str] = Field(None, description="商品类型的JSON Schema(站点语言版本)")
    properties_zh: Optional[str] = Field(None, description="商品类型的JSON Schema(中文版本)")

class PublishManageGetproducttypeResponse(LingXingModel):
    """刊登管理-获取指定 productType 的 JSON Schema."""
    product_type: Optional[List[PublishManageGetproducttypeProducttype]] = Field(None, description="商品分类信息")
    total: Optional[int] = Field(None, description="是")


class FbafeedifferenceMskuListResponse(LingXingModel):
    """FBA费差异-异常订单-MSKU."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    title: Optional[str] = Field(None, description="标题")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    msku: Optional[str] = Field(None, description="MSKU")
    sku: Optional[str] = Field(None, description="SKU")
    quantity: Optional[str] = Field(None, description="数量")
    local_name: Optional[str] = Field(None, description="本地sku名称")
    small_image_url: Optional[str] = Field(None, description="图片地址")
    difference_order_quantity: Optional[str] = Field(None, description="异常订单量")
    expected_compensation: Optional[str] = Field(None, description="预计赔偿金额")
    currency_expected_compensation: Optional[str] = Field(None, description="预计赔偿金额货币符号")
    currency_expected_compensations: Optional[str] = Field(None, description="预计赔偿金额货币")
    compensation: Optional[str] = Field(None, description="已赔偿金额")
    currency_compensation: Optional[str] = Field(None, description="已赔偿金额货币符号")


class FbafeedifferenceOrderListResponse(LingXingModel):
    """FBA费差异-异常订单-订单."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    amazon_order_id: Optional[str] = Field(None, description="订单号")
    title: Optional[str] = Field(None, description="标题")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    msku: Optional[str] = Field(None, description="MSKU")
    quantity: Optional[str] = Field(None, description="数量")
    sku: Optional[str] = Field(None, description="本地产品sku")
    local_name: Optional[str] = Field(None, description="品名")
    small_image_url: Optional[str] = Field(None, description="图片地址")
    rule_name: Optional[str] = Field(None, description="规则名称")
    chargeable: Optional[str] = Field(None, description="应收费用")
    currency_chargeable: Optional[str] = Field(None, description="应收费用货币符号")
    currency_chargeables: Optional[str] = Field(None, description="应收费用货币")
    actual_fba_fee: Optional[str] = Field(None, description="实收FBA费")
    currency_actual_fba_fee: Optional[str] = Field(None, description="实收FBA费货币符号")
    expected_compensation: Optional[str] = Field(None, description="预计赔偿金额")
    currency_expected_compensation: Optional[str] = Field(None, description="预计赔偿金额货币符号")
    is_reparation: Optional[str] = Field(None, description="是否赔偿")
    compensation: Optional[str] = Field(None, description="已赔偿金额")
    currency_compensation: Optional[str] = Field(None, description="已赔偿金额货币符号")
    compensation_date: Optional[str] = Field(None, description="赔偿时间")
    posted_date: Optional[str] = Field(None, description="结算时间")


class PromotionListingdetailcouponRecords(LingXingModel):
    """records sub-structure."""
    promotion_id: Optional[str] = Field(None, description="优惠券id")
    name: Optional[str] = Field(None, description="优惠券名称")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    status: Optional[float] = Field(None, description="商品状态：1 active，2 draft，3 archived，4 deleted")
    needs_attention: Optional[bool] = Field(None, description="状态")
    status_text: Optional[str] = Field(None, description="状态")
    origin_status: Optional[str] = Field(None, description="活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 RUNNING 生效中 NEEDS ACTION 需要注意 EXPIRING SOON 即将过期 SUBMITTED 已提交 FAILED 失败")
    origin_status_text: Optional[str] = Field(None, description="活动状态")
    discount: Optional[str] = Field(None, description="折扣")
    budget: Optional[str] = Field(None, description="预算")
    cost: Optional[float] = Field(None, description="支出")
    draw_quantity: Optional[float] = Field(None, description="领取数")
    exchange_quantity: Optional[float] = Field(None, description="兑换数")
    exchange_rate: Optional[float] = Field(None, description="兑换率")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_amount_usd: Optional[float] = Field(None, description="活动总销售额，换算成美元")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_start_time_utc: Optional[Any] = Field(None, description="活动开始时间UTC时间")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间")
    remark: Optional[str] = Field(None, description="备注")

class PromotionListingdetailcouponResponse(LingXingModel):
    """查询商品折扣详情-列表-优惠卷."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    records: Optional[List[PromotionListingdetailcouponRecords]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总数")


class PromotionListingdetailmanageRecords(LingXingModel):
    """records sub-structure."""
    promotion_id: Optional[str] = Field(None, description="活动id，唯一标识")
    name: Optional[str] = Field(None, description="名称-内部描述")
    tracking_id: Optional[str] = Field(None, description="追踪编码")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    status: Optional[float] = Field(None, description="状态")
    status_text: Optional[str] = Field(None, description="状态")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    origin_status_text: Optional[str] = Field(None, description="促销活动平台状态")
    promotion_type: Optional[float] = Field(None, description="促销类型")
    promotion_type_text: Optional[str] = Field(None, description="促销类型")
    promotion_code: Optional[str] = Field(None, description="优惠码")
    promotion_code_type: Optional[Any] = Field(None, description="优惠码类型，1优先型，2无限型")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_amount_usd: Optional[float] = Field(None, description="活动总销售额，换算成美元")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    participate_condition: Optional[str] = Field(None, description="参与条件")
    participate_condition_num: Optional[float] = Field(None, description="参与条件数值")
    buyer_gets: Optional[str] = Field(None, description="买家获得")
    buyer_gets_num: Optional[float] = Field(None, description="买家获得值")
    purchase_product: Optional[str] = Field(None, description="需购买商品")
    discount_product: Optional[str] = Field(None, description="优惠商品")
    exclude_product: Optional[str] = Field(None, description="排除商品")
    exchange_limit: Optional[float] = Field(None, description="是否限制兑换，1是0否")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_start_time_utc: Optional[Any] = Field(None, description="活动开始时间Utc")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间")
    remark: Optional[str] = Field(None, description="备注")

class PromotionListingdetailmanageResponse(LingXingModel):
    """查询商品折扣详情-列表-管理促销."""
    total: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    records: Optional[List[PromotionListingdetailmanageRecords]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="是")


class PromotionListingdetailprimediscountRecords(LingXingModel):
    """records sub-structure."""
    promotion_id: Optional[str] = Field(None, description="活动id，唯一标识")
    customer_target: Optional[str] = Field(None, description="消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣")
    name: Optional[str] = Field(None, description="折扣名称")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    status: Optional[float] = Field(None, description="状态")
    status_text: Optional[str] = Field(None, description="状态")
    error_count: Optional[str] = Field(None, description="errorCount>0时 ，代表“需要注意”状态")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    origin_status_text: Optional[str] = Field(None, description="促销活动平台状态")
    product_quantity: Optional[float] = Field(None, description="商品数量")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间（productQuantity）")
    promotion_start_time_utc: Optional[Any] = Field(None, description="活动开始时间UTC")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_amount_usd: Optional[float] = Field(None, description="活动总销售额，换算成美元")
    page_view: Optional[str] = Field(None, description="浏览量")
    exchange_rate: Optional[float] = Field(None, description="转化率")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间")
    remark: Optional[str] = Field(None, description="备注")

class PromotionListingdetailprimediscountResponse(LingXingModel):
    """查询商品折扣详情-列表-会员折扣."""
    total: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    records: Optional[List[PromotionListingdetailprimediscountRecords]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总数")


class PromotionListingdetailseckillRecords(LingXingModel):
    """records sub-structure."""
    promotion_id: Optional[str] = Field(None, description="活动id，唯一标识")
    name: Optional[str] = Field(None, description="秒杀标题")
    product_quantity: Optional[float] = Field(None, description="商品数量")
    store_id: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    status: Optional[float] = Field(None, description="状态，系统内部状态（非促销活动状态）")
    status_text: Optional[str] = Field(None, description="状态，系统内部状态（非促销活动状态）")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态（与ERP中显示一致）")
    origin_status_text: Optional[str] = Field(None, description="促销活动平台状态（与ERP中显示一致）")
    promotion_type: Optional[float] = Field(None, description="秒杀类型")
    promotion_type_text: Optional[str] = Field(None, description="秒杀类型")
    description: Optional[str] = Field(None, description="描述")
    seckill_fee: Optional[float] = Field(None, description="秒杀费")
    seckill_fee_min: Optional[float] = Field(None, description="最小秒杀费")
    seckill_fee_max: Optional[float] = Field(None, description="最大秒杀费")
    waived: Optional[bool] = Field(None, description="该秒杀是否“已豁免”")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_amount_usd: Optional[float] = Field(None, description="活动总销售额，换算成美元")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    participate_inventory: Optional[float] = Field(None, description="参与库存数")
    sold_rate: Optional[float] = Field(None, description="售出率")
    page_view: Optional[str] = Field(None, description="浏览量")
    exchange_rate: Optional[float] = Field(None, description="转化率")
    pcos: Optional[float] = Field(None, description="费用除以销售额")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_start_time_utc: Optional[Any] = Field(None, description="活动开始时间UTC")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间")
    remark: Optional[str] = Field(None, description="备注")

class PromotionListingdetailseckillResponse(LingXingModel):
    """查询商品折扣详情-列表-秒杀."""
    total: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    records: Optional[List[PromotionListingdetailseckillRecords]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总数")


class PromotionListinglistPromotionList(LingXingModel):
    """promotion_list sub-structure."""
    promotion_id: Optional[str] = Field(None, description="优惠券id")
    name: Optional[str] = Field(None, description="优惠券名称")
    status: Optional[str] = Field(None, description="优惠券状态： 0 其他 1 进行中 2 已过期 3 未开始")
    origin_status: Optional[str] = Field(None, description="优惠券平台原始状态")
    category: Optional[str] = Field(None, description="促销活动类别： 1 优惠券 2 秒杀 3 管理促销 4 促销折扣")
    category_text: Optional[str] = Field(None, description="促销活动类型说明")
    promotion_type: Optional[str] = Field(None, description="促销类型")
    promotion_type_text: Optional[str] = Field(None, description="促销类型说明")
    discount_price: Optional[str] = Field(None, description="折扣价格")
    discount_rate: Optional[str] = Field(None, description="折扣率")
    promotion_start_time: Optional[str] = Field(None, description="促销开始时间")
    promotion_end_time: Optional[str] = Field(None, description="促销结束时间")

class PromotionListinglistListingTags(LingXingModel):
    """listing_tags sub-structure."""
    global_tag_id: Optional[str] = Field(None, description="标签id")
    tag_name: Optional[str] = Field(None, description="标签名")
    color: Optional[str] = Field(None, description="标签颜色")

class PromotionListinglistResponse(LingXingModel):
    """查询商品折扣列表."""
    total: Optional[int] = Field(None, description="总数")
    item_name: Optional[str] = Field(None, description="商品标题")
    sid: Optional[str] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    region_name: Optional[str] = Field(None, description="国家/地区")
    currency_icon: Optional[str] = Field(None, description="货币符号")
    small_image_url: Optional[str] = Field(None, description="商品缩略图地址")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN跳转地址")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    promotion_list: Optional[List[PromotionListinglistPromotionList]] = Field(None, description="商品优惠券")
    promotion_combo_num: Optional[int] = Field(None, description="折扣叠加数量")
    sales_price: Optional[str] = Field(None, description="优惠价")
    sales_price_usd: Optional[str] = Field(None, description="优惠券【美元】")
    avg_deal_price: Optional[str] = Field(None, description="平均成交价")
    discount_price_min: Optional[str] = Field(None, description="最低折扣价")
    discount_rate_rate: Optional[str] = Field(None, description="最低折扣率")
    principal_list: Optional[list] = Field(None, description="listing负责人")
    listing_tags: Optional[List[PromotionListinglistListingTags]] = Field(None, description="listing标签列表")
    afn_fulfillable_quantity: Optional[str] = Field(None, description="FBA可售")
    quantity: Optional[str] = Field(None, description="FBM可售")


class PromotionalactivitiesCouponListResponse(LingXingModel):
    """查询促销活动列表-优惠券."""
    total: Optional[int] = Field(None, description="总数")
    promotion_id: Optional[str] = Field(None, description="促销活动id")
    name: Optional[str] = Field(None, description="优惠券名称")
    sid: Optional[int] = Field(None, description="店铺id")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    origin_status: Optional[str] = Field(None, description="活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 RUNNING 生效中 NEEDS ACTION 需要注意 EXPIRING SOON 即将过期 SUBMITTED 已提交 FAILED 失败")
    discount: Optional[str] = Field(None, description="折扣")
    budget: Optional[str] = Field(None, description="预算")
    cost: Optional[str] = Field(None, description="支出")
    draw_quantity: Optional[str] = Field(None, description="领取数")
    exchange_quantity: Optional[str] = Field(None, description="兑换数")
    exchange_rate: Optional[str] = Field(None, description="兑换率")
    sales_amount: Optional[str] = Field(None, description="活动总销售额")
    sales_volume: Optional[str] = Field(None, description="活动总销量")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间【站点时间】")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间【站点时间】")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间【站点时间】")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间【站点时间】")
    remark: Optional[str] = Field(None, description="备注")


class PromotionalactivitiesManageListResponse(LingXingModel):
    """查询促销活动列表-管理促销."""
    total: Optional[int] = Field(None, description="总数")
    promotion_id: Optional[str] = Field(None, description="促销活动id")
    name: Optional[str] = Field(None, description="内部描述")
    sid: Optional[int] = Field(None, description="店铺id")
    promotion_type: Optional[int] = Field(None, description="活动类型： 3 买一赠一 4 购买折扣 5 一口价 8 社媒促销")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    origin_status: Optional[str] = Field(None, description="活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 PENDING 未开始")
    promotion_code: Optional[str] = Field(None, description="优惠码")
    sales_amount: Optional[str] = Field(None, description="活动总销售额")
    sales_volume: Optional[str] = Field(None, description="活动总销量")
    participate_condition: Optional[str] = Field(None, description="参与条件")
    participate_condition_num: Optional[str] = Field(None, description="参与条件数值")
    buyer_gets: Optional[str] = Field(None, description="买家获得")
    buyer_gets_num: Optional[str] = Field(None, description="买家获得值")
    purchase_product: Optional[str] = Field(None, description="需购买商品")
    discount_product: Optional[str] = Field(None, description="优惠商品")
    exclude_product: Optional[str] = Field(None, description="排除商品")
    exchange_limit: Optional[int] = Field(None, description="是否限制兑换： 1 是 0 否")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间【站点时间】")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间【站点时间】")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间【站点时间】")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间【站点时间】")
    remark: Optional[str] = Field(None, description="备注")


class PromotionalactivitiesSeckillListResponse(LingXingModel):
    """查询促销活动列表-秒杀."""
    total: Optional[int] = Field(None, description="总数")
    promotion_id: Optional[str] = Field(None, description="促销活动id")
    name: Optional[str] = Field(None, description="秒杀标题")
    product_quantity: Optional[int] = Field(None, description="商品数量")
    sid: Optional[int] = Field(None, description="店铺id")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    origin_status: Optional[str] = Field(None, description="活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 APPROVED 未开始 SUPPRESSED 需要注意 DISMISSED 禁止显示 DRAFT 未定 ENDED 已结束")
    promotion_type: Optional[int] = Field(None, description="秒杀类型： 1 Best Deal 2 Lighting Deal")
    description: Optional[str] = Field(None, description="描述")
    seckill_fee: Optional[str] = Field(None, description="秒杀费")
    sales_amount: Optional[str] = Field(None, description="活动总销售额")
    sales_volume: Optional[str] = Field(None, description="活动总销量")
    participate_inventory: Optional[str] = Field(None, description="参与库存数")
    sold_rate: Optional[str] = Field(None, description="售出率")
    page_view: Optional[str] = Field(None, description="浏览量")
    exchange_rate: Optional[str] = Field(None, description="转化率")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间【站点时间】")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间【站点时间】")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间【站点时间】")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间【站点时间】")
    remark: Optional[str] = Field(None, description="备注")


class PromotionalactivitiesVipdiscountListResponse(LingXingModel):
    """查询促销活动列表-会员折扣/价格折扣."""
    total: Optional[int] = Field(None, description="总数")
    promotion_id: Optional[str] = Field(None, description="促销活动id")
    name: Optional[str] = Field(None, description="折扣名称")
    product_quantity: Optional[int] = Field(None, description="商品数量")
    sid: Optional[int] = Field(None, description="店铺id")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    customer_target: Optional[str] = Field(None, description="消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣")
    origin_status: Optional[str] = Field(None, description="活动状态： ACTIVE 进行中 CANCELED 已取消 EXPIRED 已过期 AWAITTING 待上传商品 SCHEDULED 已计划 NEEDS ATTENTION 需要注意 ENDED 已结束")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间【站点时间】")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间【站点时间】")
    first_sync_time: Optional[str] = Field(None, description="首次同步时间【站点时间】")
    last_sync_time: Optional[str] = Field(None, description="最后同步时间【站点时间】")
    update_time: Optional[str] = Field(None, description="更新时间【站点时间】")
    remark: Optional[str] = Field(None, description="备注")


class MwsListingPrincipalInfo(LingXingModel):
    """principal_info sub-structure."""
    principal_uid: Optional[int] = Field(None, description="负责人用户id")
    principal_name: Optional[str] = Field(None, description="负责人姓名")

class MwsListingDimensionInfo(LingXingModel):
    """dimension_info sub-structure."""
    item_height: Optional[str] = Field(None, description="商品高度")
    item_height_units_type: Optional[str] = Field(None, description="商品高度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    item_length: Optional[str] = Field(None, description="商品长度")
    item_length_units_type: Optional[str] = Field(None, description="商品长度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    item_width: Optional[str] = Field(None, description="商品宽度")
    item_width_units_type: Optional[str] = Field(None, description="商品宽度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    item_weight: Optional[str] = Field(None, description="商品重量")
    item_weight_units_type: Optional[dict] = Field(None, description="商品重量单位： unkown未知单位 空字符串 pounds(ce(盎司,o磅,ib) kg(千克,kg) ounce(盎司,oz) gram(克,g) carat(克拉,ct)")
    package_height: Optional[str] = Field(None, description="包装高度")
    package_height_units_type: Optional[str] = Field(None, description="包装高度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    package_length: Optional[str] = Field(None, description="包装长度")
    package_length_units_type: Optional[str] = Field(None, description="包装长度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    package_width: Optional[str] = Field(None, description="包装宽度")
    package_width_units_type: Optional[str] = Field(None, description="包装宽度单位： unkown未知单位 空字符串 inches(英寸复数,in) inch(英寸单数,in) centimeter(厘米,cm) yard(码,yd) veron(弗隆,fur) foot(英尺,ft)")
    package_weight: Optional[str] = Field(None, description="包装重量")
    package_weight_units_type: Optional[str] = Field(None, description="包装重量单位： unkown未知单位 空字符串 pounds(ce(盎司,o磅,ib) kg(千克,kg) ounce(盎司,oz) gram(克,g) carat(克拉,ct)")

class MwsListingSmallRank(LingXingModel):
    """small_rank sub-structure."""
    category: Optional[str] = Field(None, description="小类名称")
    rank: Optional[str] = Field(None, description="小类排名")

class MwsListingGlobalTags(LingXingModel):
    """global_tags sub-structure."""
    global_tag_id: Optional[str] = Field(None, description="全局标签ID")
    tag_name: Optional[str] = Field(None, description="标签名称")
    color: Optional[str] = Field(None, description="颜色")

class MwsListingResponse(LingXingModel):
    """查询亚马逊Listing."""
    total: Optional[int] = Field(None, description="总数")
    listing_id: Optional[str] = Field(None, description="亚马逊定义的listing的id【可能为空】")
    sid: Optional[int] = Field(None, description="店铺id")
    marketplace: Optional[str] = Field(None, description="国家")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    asin: Optional[str] = Field(None, description="ASIN")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    small_image_url: Optional[str] = Field(None, description="商品缩略图地址")
    status: Optional[int] = Field(None, description="状态：0 停售，1 在售")
    is_delete: Optional[int] = Field(None, description="是否删除：0 否，1 是")
    item_name: Optional[str] = Field(None, description="标题")
    local_sku: Optional[str] = Field(None, description="本地产品SKU")
    local_name: Optional[str] = Field(None, description="品名")
    currency_code: Optional[str] = Field(None, description="币种")
    price: Optional[str] = Field(None, description="价格【不包含促销，运费，积分】")
    landed_price: Optional[str] = Field(None, description="总价【包含了促销、运费、积分】")
    listing_price: Optional[str] = Field(None, description="优惠价")
    shipping: Optional[str] = Field(None, description="运费")
    points: Optional[str] = Field(None, description="积分，日本站才有")
    quantity: Optional[int] = Field(None, description="FBM库存")
    afn_fulfillable_quantity: Optional[int] = Field(None, description="FBA可售")
    afn_unsellable_quantity: Optional[int] = Field(None, description="FBA不可售")
    reserved_fc_transfers: Optional[int] = Field(None, description="待调仓")
    reserved_fc_processing: Optional[int] = Field(None, description="调仓中")
    reserved_customerorders: Optional[int] = Field(None, description="待发货")
    afn_inbound_shipped_quantity: Optional[int] = Field(None, description="在途")
    afn_inbound_working_quantity: Optional[int] = Field(None, description="计划入库")
    afn_inbound_receiving_quantity: Optional[int] = Field(None, description="入库中")
    open_date: Optional[str] = Field(None, description="商品创建时间")
    open_date_display: Optional[str] = Field(None, description="商品创建时间，格式：Y-m-d H:i:s+时区")
    listing_update_date: Optional[str] = Field(None, description="All Listing报表更新时间 (注意：此为零时区时间)")
    seller_rank: Optional[int] = Field(None, description="排名")
    seller_brand: Optional[str] = Field(None, description="亚马逊品牌")
    seller_category: Optional[str] = Field(None, description="排名所属的类别(后续不再维护，改用seller_category_new)")
    review_num: Optional[int] = Field(None, description="评论条数")
    last_star: Optional[str] = Field(None, description="星级评分")
    fulfillment_channel_type: Optional[str] = Field(None, description="配送方式")
    principal_info: Optional[List[MwsListingPrincipalInfo]] = Field(None, description="负责人信息")
    seller_category_new: Optional[list] = Field(None, description="排名所属的类别")
    pair_update_time: Optional[str] = Field(None, description="配对更新时间 (注意：此为北京时间)")
    first_order_time: Optional[str] = Field(None, description="首单时间，格式：Y-m-d")
    on_sale_time: Optional[str] = Field(None, description="开售时间，格式：Y-m-d")
    store_type: Optional[int] = Field(None, description="商品类型，1-非低价商店 ，2-低价商店商品")
    total_volume: Optional[str] = Field(None, description="销量-7天")
    yesterday_volume: Optional[str] = Field(None, description="销量-昨天")
    fourteen_volume: Optional[str] = Field(None, description="销量-14天")
    thirty_volume: Optional[str] = Field(None, description="销量-30天")
    yesterday_amount: Optional[str] = Field(None, description="销售额-昨天")
    seven_amount: Optional[str] = Field(None, description="销售额-7天")
    fourteen_amount: Optional[str] = Field(None, description="销售额-14天")
    thirty_amount: Optional[str] = Field(None, description="销售额-30天")
    average_seven_volume: Optional[str] = Field(None, description="日均销量-7日")
    average_fourteen_volume: Optional[str] = Field(None, description="日均销量-14日")
    average_thirty_volume: Optional[str] = Field(None, description="日均销量-30日")
    dimension_info: Optional[List[MwsListingDimensionInfo]] = Field(None, description="尺寸信息，没有尺寸信息时是空")
    small_rank: Optional[List[MwsListingSmallRank]] = Field(None, description="小类排名信息")
    global_tags: Optional[List[MwsListingGlobalTags]] = Field(None, description="全局标签")


class MwsOrderdetailItemList(LingXingModel):
    """item_list sub-structure."""
    id: Optional[int] = Field(None, description="订单商品自增id")
    title: Optional[str] = Field(None, description="商品标题")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="asin链接")
    sid: Optional[int] = Field(None, description="店铺id")
    sku: Optional[str] = Field(None, description="本地SKU")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    pic_url: Optional[str] = Field(None, description="图片链接")
    order_item_id: Optional[str] = Field(None, description="订单商品编码【订单下唯一，但亚马逊返回值可能会发生变更，以最新数据为准】")
    points_monetary_value_amount: Optional[str] = Field(None, description="积分成本（日本站会有此数据）")
    quantity_ordered: Optional[int] = Field(None, description="下单量")
    quantity_shipped: Optional[int] = Field(None, description="已配送")
    item_price_amount: Optional[str] = Field(None, description="商品支付金额")
    item_tax_amount: Optional[str] = Field(None, description="商品税")
    shipping_price_amount: Optional[str] = Field(None, description="买家运费")
    shipping_tax_amount: Optional[str] = Field(None, description="商品运费税")
    gift_wrap_price_amount: Optional[str] = Field(None, description="礼品包装费")
    gift_wrap_tax_amount: Optional[str] = Field(None, description="礼品包装税")
    shipping_discount_amount: Optional[str] = Field(None, description="配送折扣")
    cod_fee_amount: Optional[str] = Field(None, description="COD服务费用（货到付款服务费）")
    promotion_ids: Optional[list] = Field(None, description="商品促销id")
    shipping_discount_tax_amount: Optional[str] = Field(None, description="配送折扣税")
    promotion_discount_amount: Optional[str] = Field(None, description="商品促销折扣")
    promotion_discount_tax_amount: Optional[str] = Field(None, description="商品促销折扣税")
    cod_fee_discount_amount: Optional[str] = Field(None, description="COD服务费用折扣")
    gift_message_text: Optional[str] = Field(None, description="礼品信息（买家提供）")
    gift_wrap_level: Optional[str] = Field(None, description="礼品包装级别（买家提供）")
    condition_note: Optional[str] = Field(None, description="商品状况说明（卖家提供）")
    condition_id: Optional[str] = Field(None, description="商品状况（卖家提供）")
    condition_subtype_id: Optional[str] = Field(None, description="商品子状况（卖家提供）")
    scheduled_delivery_start_date: Optional[str] = Field(None, description="计划交货开始日期")
    scheduled_delivery_end_date: Optional[str] = Field(None, description="计划交货结束日期")
    price_designation: Optional[str] = Field(None, description="B2B价格")
    cg_price: Optional[float] = Field(None, description="采购成本")
    fee_name: Optional[str] = Field(None, description="其他费名称，比如推广费")
    cg_transport_costs: Optional[float] = Field(None, description="头程费用")
    fba_shipment_amount: Optional[float] = Field(None, description="FBA发货费")
    commission_amount: Optional[float] = Field(None, description="平台费")
    other_amount: Optional[float] = Field(None, description="亚马逊收取的其他费用，比如参与“Amazon Exlusives Program”产生的费用")
    fee_currency: Optional[str] = Field(None, description="其他费币种，比如推广费")
    fee_icon: Optional[str] = Field(None, description="其他费币种符号，比如推广费")
    fee_cost_amount: Optional[float] = Field(None, description="自定义费用本金（店铺对应的币种，例：站外推广费本金）")
    fee_cost: Optional[float] = Field(None, description="自定义费用本金（fee_currency对应的币种，例：站外推广费本金）")
    sales_price_amount: Optional[float] = Field(None, description="销售收益")
    unit_price_amount: Optional[float] = Field(None, description="单价")
    tax_amount: Optional[float] = Field(None, description="税费")
    promotion_amount: Optional[float] = Field(None, description="促销费")
    profit: Optional[float] = Field(None, description="毛利润")
    item_discount: Optional[float] = Field(None, description="商品折扣")
    customized_json: Optional[str] = Field(None, description="订单定制化信息json")
    is_settled: Optional[int] = Field(None, description="商品已结算标识:0 未结算,1 已结算")

class MwsOrderdetailResponse(LingXingModel):
    """查询亚马逊订单详情."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    amazon_order_id: Optional[str] = Field(None, description="亚马逊订单号")
    fulfillment_channel: Optional[str] = Field(None, description="发货渠道")
    order_status: Optional[str] = Field(None, description="订单状态")
    order_total_amount: Optional[float] = Field(None, description="订单总金额")
    currency: Optional[str] = Field(None, description="订单金额币种")
    icon: Optional[str] = Field(None, description="订单金额币种符号")
    is_assessed: Optional[int] = Field(None, description="是否为推广订单： 0 否，1 是")
    is_mcf_order: Optional[int] = Field(None, description="是否多渠道订单：0 普通订单，1 多渠道订单")
    is_return_order: Optional[int] = Field(None, description="是否为退货订单：0 否，1 是")
    is_replaced_order: Optional[int] = Field(None, description="是否已换货：0 否，1 是")
    is_replacement_order: Optional[int] = Field(None, description="是否为换货订单：0 否，1 是")
    purchase_date_local: Optional[str] = Field(None, description="订购时间（站点时间）")
    purchase_date_local_utc: Optional[str] = Field(None, description="订购时间（utc时间）")
    last_update_date: Optional[str] = Field(None, description="订单更新（站点时间）")
    last_update_date_utc: Optional[str] = Field(None, description="订单更新时间（utc时间）")
    posted_date: Optional[str] = Field(None, description="结算时间（站点时间）")
    shipment_date: Optional[str] = Field(None, description="发货时间（站点时间）")
    earliest_ship_date: Optional[str] = Field(None, description="发货时限（站点时间）")
    earliest_ship_date_utc: Optional[str] = Field(None, description="发货时限（utc时间）")
    is_business_order: Optional[int] = Field(None, description="是否为B2B订单：0 否，1 是")
    is_prime: Optional[int] = Field(None, description="是否prime订单：0 否，1 是")
    is_premium_order: Optional[int] = Field(None, description="是否优先配送订单：0 否，1 是")
    is_promotion: Optional[int] = Field(None, description="是否促销订单：0 否，1 是")
    taxes_included: Optional[int] = Field(None, description="费用是否含税：1 含税，2 不含税 仅针对欧洲市场订单使用，对应字段如下：item_price_amount、shipping_price_amount、gift_wrap_price_amount、shipping_discount_amount、promotion_discount_amount、cod_fee_amount")
    ship_service_level: Optional[str] = Field(None, description="配送服务")
    shipment_service_level_category: Optional[str] = Field(None, description="装运服务级别")
    purchase_order_number: Optional[str] = Field(None, description="采购订单编号（买家结账时输入）")
    payment_method: Optional[str] = Field(None, description="付款方式： COD (Cash on delivery) CVS（Convenience store） Other（A payment method other than COD and CVS）")
    cba_displayable_shipping_label: Optional[str] = Field(None, description="亚马逊结账（CBA）的自定义发货标签")
    order_type: Optional[str] = Field(None, description="订单类型")
    latest_ship_date: Optional[str] = Field(None, description="最晚发货时间（承诺配送订单的最晚发货时间）")
    earliest_delivery_date: Optional[str] = Field(None, description="最早送达时间（承诺送达订单的最早送达时间） 备注：UTC时间")
    latest_delivery_date: Optional[str] = Field(None, description="最晚送达时间（承诺送达订单的最晚送达时间） 备注：UTC时间")
    number_of_items_shipped: Optional[int] = Field(None, description="已发货的商品数")
    number_of_items_unshipped: Optional[int] = Field(None, description="未发货的商品数")
    sales_channel: Optional[str] = Field(None, description="销售渠道")
    item_list: Optional[List[MwsOrderdetailItemList]] = Field(None, description="订单明细")


class MwsOrdersItemList(LingXingModel):
    """item_list sub-structure."""
    asin: Optional[str] = Field(None, description="ASIN")
    quantity_ordered: Optional[str] = Field(None, description="数量")
    seller_sku: Optional[str] = Field(None, description="MSKU")
    local_sku: Optional[str] = Field(None, description="本地sku")
    local_name: Optional[str] = Field(None, description="本地品名")

class MwsOrdersResponse(LingXingModel):
    """查询亚马逊订单列表."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    amazon_order_id: Optional[str] = Field(None, description="亚马逊订单号")
    order_status: Optional[str] = Field(None, description="订单状态")
    order_total_amount: Optional[str] = Field(None, description="订单金额")
    fulfillment_channel: Optional[str] = Field(None, description="配送方式：亚马逊订单-AFN，自发货-MFN")
    postal_code: Optional[str] = Field(None, description="邮编")
    is_return: Optional[int] = Field(None, description="退款状态：0 未退款，1 退款中，2 退款完成")
    is_mcf_order: Optional[int] = Field(None, description="是否多渠道订单：0 否，1 是 【2023年后的多渠道订单数据均不在此接口返回】")
    is_assessed: Optional[int] = Field(None, description="是否推广订单：0 否，1 是")
    is_replaced_order: Optional[int] = Field(None, description="是否换货订单：0 否，1 是")
    is_replacement_order: Optional[int] = Field(None, description="是否已换货订单：0 否，1 是")
    is_return_order: Optional[int] = Field(None, description="是否退货订单：0 否，1 是")
    order_total_currency_code: Optional[str] = Field(None, description="币种，order_total_amount为0时，币种信息为空")
    sales_channel: Optional[str] = Field(None, description="销售渠道")
    tracking_number: Optional[str] = Field(None, description="物流运单号")
    refund_amount: Optional[float] = Field(None, description="退款金额(含币种)")
    item_list: Optional[List[MwsOrdersItemList]] = Field(None, description="商品信息")
    purchase_date_local: Optional[str] = Field(None, description="订购时间【站点时间】")
    purchase_date_local_utc: Optional[str] = Field(None, description="订购时间【UTC】")
    shipment_date: Optional[str] = Field(None, description="发货日期【亚马逊返回时间，不一定为站点时间】")
    shipment_date_utc: Optional[str] = Field(None, description="发货日期【UTC】")
    shipment_date_local: Optional[str] = Field(None, description="发货日期【站点时间】")
    last_update_date: Optional[str] = Field(None, description="订单更新时间【站点时间】")
    last_update_date_utc: Optional[str] = Field(None, description="订单更新时间【UTC】")
    posted_date: Optional[str] = Field(None, description="付款时间【亚马逊返回时间，不一定为站点时间】")
    posted_date_utc: Optional[str] = Field(None, description="付款时间【UTC】")
    purchase_date: Optional[str] = Field(None, description="订购时间【亚马逊返回时间，不一定为站点时间】")
    purchase_date_utc: Optional[str] = Field(None, description="订购时间【UTC】")
    earliest_ship_date: Optional[str] = Field(None, description="发货时限【亚马逊返回时间，不一定为站点时间】")
    earliest_ship_date_utc: Optional[str] = Field(None, description="发货时限【UTC】")
    gmt_modified: Optional[str] = Field(None, description="订单修改时间")
    gmt_modified_utc: Optional[str] = Field(None, description="订单修改时间【UTC】")


class ListingProductpricingPricingsubmitFailureDetail(LingXingModel):
    """failure_detail sub-structure."""
    sid: Optional[Any] = Field(None, description="[int]")
    msku: Optional[Any] = Field(None, description="[string]")
    asin: Optional[Any] = Field(None, description="[string]")
    msg: Optional[Any] = Field(None, description="[string]")

class ListingProductpricingPricingsubmitResponse(LingXingModel):
    """批量修改Listing价格."""
    success_num: Optional[Any] = Field(None, description="[int]")
    failure_num: Optional[Any] = Field(None, description="[int]")
    failure_detail: Optional[List[ListingProductpricingPricingsubmitFailureDetail]] = Field(None, description="[array]")
    total: Optional[int] = Field(None, description="[int]")


class OrderOrderGetorderdetailOrderItem(LingXingModel):
    """order_item sub-structure."""
    platform_order_id: Optional[str] = Field(None, description="平台单号")
    msku: Optional[str] = Field(None, description="MSKU")
    order_item_no: Optional[str] = Field(None, description="订单明细单号")
    pic_url: Optional[str] = Field(None, description="图片连接")
    sku: Optional[str] = Field(None, description="SKU")
    product_name: Optional[str] = Field(None, description="品名")
    quality: Optional[int] = Field(None, description="数量")
    item_unit_price: Optional[float] = Field(None, description="单价")
    currency_code: Optional[str] = Field(None, description="单价币种")
    customization: Optional[str] = Field(None, description="商品备注")
    attachments: Optional[list] = Field(None, description="商品附件")
    new_attachments: Optional[list] = Field(None, description="商品新附件信息")

class OrderOrderGetorderdetailResponse(LingXingModel):
    """查询亚马逊自发货订单详情."""
    order_number: Optional[str] = Field(None, description="系统单号")
    order_status: Optional[str] = Field(None, description="订单状态")
    order_from_name: Optional[str] = Field(None, description="订单类型")
    purchase_time: Optional[str] = Field(None, description="订购时间")
    platform: Optional[str] = Field(None, description="平台")
    shop_name: Optional[str] = Field(None, description="店铺")
    buyer_choose_express: Optional[str] = Field(None, description="客选物流")
    total_shipping_price: Optional[float] = Field(None, description="客付运费")
    buyer_message: Optional[str] = Field(None, description="买家留言")
    customer_comment: Optional[str] = Field(None, description="客服备注")
    warehouse_name: Optional[str] = Field(None, description="发货仓库")
    wid: Optional[int] = Field(None, description="发货仓库id")
    tracking_number: Optional[str] = Field(None, description="跟踪号")
    logistics_type_name: Optional[str] = Field(None, description="物流方式")
    logistics_provider_name: Optional[str] = Field(None, description="物流商")
    logistics_type_id: Optional[int] = Field(None, description="物流方式id")
    logistics_provider_id: Optional[int] = Field(None, description="物流商id")
    logistics_pre_weight: Optional[float] = Field(None, description="估算重量")
    logistics_pre_weight_unit: Optional[str] = Field(None, description="估算重量单位")
    logistics_pre_price: Optional[float] = Field(None, description="预估运费")
    logistics_freight: Optional[str] = Field(None, description="物流运费")
    logistics_freight_currency_code: Optional[str] = Field(None, description="物流运费币种")
    package_length: Optional[float] = Field(None, description="估算尺寸长")
    package_width: Optional[float] = Field(None, description="估算尺寸宽")
    package_height: Optional[float] = Field(None, description="估算尺寸高")
    package_unit: Optional[str] = Field(None, description="估算尺寸单位")
    pkg_real_weight: Optional[float] = Field(None, description="包裹实重")
    pkg_real_weight_unit: Optional[str] = Field(None, description="包裹实重单位")
    pkg_length: Optional[float] = Field(None, description="包裹尺寸长")
    pkg_width: Optional[float] = Field(None, description="包裹尺寸宽")
    pkg_height: Optional[float] = Field(None, description="包裹尺寸高")
    pkg_size_unit: Optional[str] = Field(None, description="包裹尺寸单位")
    order_price_amount: Optional[float] = Field(None, description="订单总金额")
    gross_profit_amount: Optional[float] = Field(None, description="订单毛利润")
    order_item: Optional[List[OrderOrderGetorderdetailOrderItem]] = Field(None, description="是")


class OrderOrderGetorderlistResponse(LingXingModel):
    """查询亚马逊自发货订单列表."""
    order_number: Optional[str] = Field(None, description="系统单号")
    status: Optional[str] = Field(None, description="订单状态")
    order_from: Optional[str] = Field(None, description="订单类型")
    country_code: Optional[str] = Field(None, description="目的国代码")
    purchase_time: Optional[str] = Field(None, description="订购时间")
    logistics_type_id: Optional[str] = Field(None, description="物流方式ID")
    logistics_provider_id: Optional[str] = Field(None, description="物流商ID")
    platform_list: Optional[list] = Field(None, description="平台订单号")
    logistics_type_name: Optional[str] = Field(None, description="物流方式名称")
    logistics_provider_name: Optional[str] = Field(None, description="物理商名称")
    wid: Optional[int] = Field(None, description="发货仓库id")
    warehouse_name: Optional[str] = Field(None, description="发货仓库名称")
    customer_comment: Optional[str] = Field(None, description="客服备注")
    total: Optional[int] = Field(None, description="总数")


class StorageProductLinkResponse(LingXingModel):
    """批量添加/编辑Listing配对."""
    total: Optional[int] = Field(None, description="总配对个数")
    success: Optional[int] = Field(None, description="配对成功数")
    error: Optional[int] = Field(None, description="配对失败数")


class ListingAsinUpdateprincipalResponse(LingXingModel):
    """批量分配Listing负责人."""
    total: Optional[int] = Field(None, description="总数")
    success: Optional[int] = Field(None, description="成功数")
    error: Optional[int] = Field(None, description="失败数")


class ListingListingGetpricesResponse(LingXingModel):
    """批量获取Listing费用."""
    sid: Optional[int] = Field(None, description="店铺id")
    msku: Optional[str] = Field(None, description="MSKU")
    fba_fee: Optional[float] = Field(None, description="FBA预估费")
    fba_fee_currency_code: Optional[str] = Field(None, description="FBA预估费币种符号")
    total: Optional[int] = Field(None, description="总数")


class AmazonProductListResponse(LingXingModel):
    """刊登管理-查询刊登结果."""
    record_unique_id: Optional[float] = Field(None, description="批次唯一ID")
    store_id: Optional[float] = Field(None, description="store_id")
    sku: Optional[str] = Field(None, description="sku")
    status: Optional[float] = Field(None, description="状态： 0 处理中 1 成功 2 失败")
    failure_reason: Optional[str] = Field(None, description="失败原因")
    warning: Optional[str] = Field(None, description="亚马逊返回warning")
    operate_time: Optional[str] = Field(None, description="操作时间")
    finish_time: Optional[str] = Field(None, description="完成时间")


class AmazonProductPublishResponse(LingXingModel):
    """刊登管理-提交商品资料."""
    record_unique_id: Optional[str] = Field(None, description="批次唯一ID")


class AmazonProductSearchResponse(LingXingModel):
    """查询已有商品信息."""
    msku: Optional[str] = Field(None, description="msku")
    info: Optional[dict] = Field(None, description="商品信息")


class AmzodOrderdetailsLogisticsinformationShipmentInfo(LingXingModel):
    """shipment_info sub-structure."""
    amazon_shipment_id: Optional[str] = Field(None, description="货件编号")
    fulfillment_shipment_status: Optional[str] = Field(None, description="ship状态： CANCELLED_BY_FULFILLER CANCELLED_BY_SELLER PENDING PROCESSED SHIPPED")
    estimated_arrival_datetime: Optional[str] = Field(None, description="预计到货时间【站点时间】")
    packages: Optional[list] = Field(None, description="包裹信息")

class AmzodOrderdetailsLogisticsinformationResponse(LingXingModel):
    """查询亚马逊多渠道订单详情-物流信息."""
    remark: Optional[str] = Field(None, description="备注")
    sid: Optional[int] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    amazon_order_id: Optional[str] = Field(None, description="平台订单号")
    seller_fulfillment_order_id: Optional[str] = Field(None, description="卖家订单号")
    displayable_order_comment: Optional[str] = Field(None, description="装箱单备注")
    order_status: Optional[str] = Field(None, description="订单状态")
    sales_channel: Optional[str] = Field(None, description="销售渠道")
    purchase_date_local: Optional[str] = Field(None, description="提交时间")
    ship_date: Optional[str] = Field(None, description="发货时间（北京时间）")
    ship_date_utc: Optional[str] = Field(None, description="发货时间（UTC时间）")
    speed_category: Optional[str] = Field(None, description="配送服务")
    ship_date_locale_norm: Optional[str] = Field(None, description="发货时间（站点时间）")
    ship_date_locale_iso: Optional[str] = Field(None, description="发货时间ISO格式（站点时间）")
    shipment_info: Optional[List[AmzodOrderdetailsLogisticsinformationShipmentInfo]] = Field(None, description="配送详情")


class AmzodOrderdetailsProductinformationListingDetailInfo(LingXingModel):
    """listing_detail_info sub-structure."""
    asin: Optional[str] = Field(None, description="asin")
    fnsku: Optional[str] = Field(None, description="fnsku")
    quantity: Optional[int] = Field(None, description="数量")
    small_image_url: Optional[str] = Field(None, description="图片地址")
    local_name: Optional[str] = Field(None, description="品名")
    local_sku: Optional[str] = Field(None, description="本地产品sku")
    msku: Optional[str] = Field(None, description="msku")
    item_name: Optional[str] = Field(None, description="商品名称")
    cancelled_quantity: Optional[int] = Field(None, description="已取消数量")
    unfulfillable_quantity: Optional[int] = Field(None, description="不可售数量")
    shipped_quantity: Optional[int] = Field(None, description="已发货数量")
    fba_fee: Optional[str] = Field(None, description="FBA费")

class AmzodOrderdetailsProductinformationResponse(LingXingModel):
    """查询亚马逊多渠道订单详情-商品信息."""
    remark: Optional[str] = Field(None, description="备注")
    phone: Optional[str] = Field(None, description="电话")
    sid: Optional[int] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    amazon_order_id: Optional[str] = Field(None, description="平台订单号")
    seller_fulfillment_order_id: Optional[str] = Field(None, description="卖家订单号")
    displayable_order_comment: Optional[str] = Field(None, description="装箱单备注")
    order_status: Optional[str] = Field(None, description="订单状态")
    sales_channel: Optional[str] = Field(None, description="销售渠道")
    purchase_date_local: Optional[str] = Field(None, description="提交时间")
    ship_date: Optional[str] = Field(None, description="发货时间（北京时间）")
    ship_date_utc: Optional[str] = Field(None, description="发货时间（utc时间）")
    speed_category: Optional[str] = Field(None, description="配送服务")
    ship_date_locale_norm: Optional[str] = Field(None, description="发货时间（站点时间）")
    ship_date_locale_iso: Optional[str] = Field(None, description="发货时间ISO格式（站点时间）")
    listing_detail_info: Optional[List[AmzodOrderdetailsProductinformationListingDetailInfo]] = Field(None, description="商品信息")


class AmzodOrderdetailsReturninformationOrderReturnReplaceTab(LingXingModel):
    """order_return_replace_tab sub-structure."""
    return_tab: Optional[list] = Field(None, description="退货信息")
    replace_tab: Optional[list] = Field(None, description="换货信息")

class AmzodOrderdetailsReturninformationResponse(LingXingModel):
    """查询亚马逊多渠道订单详情-退货换货信息."""
    remark: Optional[str] = Field(None, description="备注")
    phone: Optional[str] = Field(None, description="电话")
    sid: Optional[int] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    amazon_order_id: Optional[str] = Field(None, description="平台订单号")
    seller_fulfillment_order_id: Optional[str] = Field(None, description="卖家订单号")
    displayable_order_comment: Optional[str] = Field(None, description="装箱单备注")
    order_status: Optional[str] = Field(None, description="订单状态")
    sales_channel: Optional[str] = Field(None, description="销售渠道")
    purchase_date_local: Optional[str] = Field(None, description="提交时间")
    ship_date: Optional[str] = Field(None, description="发货时间（北京时间）")
    ship_date_utc: Optional[str] = Field(None, description="发货时间（UTC时间）")
    speed_category: Optional[str] = Field(None, description="配送服务")
    ship_date_locale_norm: Optional[str] = Field(None, description="发货时间（站点时间）")
    ship_date_locale_iso: Optional[str] = Field(None, description="发货时间ISO格式（站点时间）")
    order_return_replace_tab: Optional[List[AmzodOrderdetailsReturninformationOrderReturnReplaceTab]] = Field(None, description="是")


class OrderAmzodOrderlistRecords(LingXingModel):
    """records sub-structure."""
    remark: Optional[str] = Field(None, description="备注")
    sid: Optional[int] = Field(None, description="店铺id")
    store_name: Optional[str] = Field(None, description="店铺名称")
    country: Optional[str] = Field(None, description="国家")
    amazon_order_id: Optional[str] = Field(None, description="亚马逊订单号")
    seller_fulfillment_order_id: Optional[str] = Field(None, description="卖家订单号")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    last_update_time: Optional[str] = Field(None, description="最近更新时间")
    order_status: Optional[str] = Field(None, description="订单状态")
    purchase_date_local: Optional[str] = Field(None, description="订购时间")
    ship_date: Optional[str] = Field(None, description="发货时间（站点时间）")
    ship_date_utc: Optional[str] = Field(None, description="发货时间（UTC时间）")
    listing_info: Optional[list] = Field(None, description="商品信息")

class OrderAmzodOrderlistResponse(LingXingModel):
    """查询亚马逊多渠道订单列表-v2."""
    total: Optional[int] = Field(None, description="总数")
    records: Optional[List[OrderAmzodOrderlistRecords]] = Field(None, description="记录")


class MpOrderGetfulfillmentresultResult(LingXingModel):
    """result sub-structure."""
    message_id: Optional[str] = Field(None, description="亚马逊返回，提交过来的记录id")
    result_code: Optional[str] = Field(None, description="亚马逊返回，处理结果code")
    result_message_code: Optional[str] = Field(None, description="亚马逊返回，消息code")
    result_description: Optional[str] = Field(None, description="亚马逊返回，错误描述")

class MpOrderGetfulfillmentresultProcessingSummary(LingXingModel):
    """processing_summary sub-structure."""
    messages_processed: Optional[str] = Field(None, description="亚马逊返回，处理个数")
    messages_successful: Optional[str] = Field(None, description="亚马逊返回，成功个数")
    messages_with_error: Optional[str] = Field(None, description="亚马逊返回，失败个数")
    messages_with_warning: Optional[str] = Field(None, description="亚马逊返回，告警个数")

class MpOrderGetfulfillmentresultResponse(LingXingModel):
    """查询亚马逊标发结果."""
    result: Optional[List[MpOrderGetfulfillmentresultResult]] = Field(None, description="多个订单结果集")
    task_id: Optional[str] = Field(None, description="任务id")
    status_code: Optional[str] = Field(None, description="任务状态")
    ship_time: Optional[str] = Field(None, description="标发时间")
    processing_summary: Optional[List[MpOrderGetfulfillmentresultProcessingSummary]] = Field(None, description="结果汇总")
    failure: Optional[str] = Field(None, description="请求失败原因")


class MpOrderSubmitfulfillmentResponse(LingXingModel):
    """亚马逊订单提交标发."""
    task_id: Optional[str] = Field(None, description="任务id")
    task_status: Optional[str] = Field(None, description="任务状态")
    failure_reason: Optional[str] = Field(None, description="提交失败原因")


class PromotionapiPromotionCouponalldetailbatchCoupon(LingXingModel):
    """coupon sub-structure."""
    promotion_id: Optional[str] = Field(None, description="活动id，唯一标识")
    name: Optional[str] = Field(None, description="名称")
    store_id: Optional[str] = Field(None, description="店铺ID")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    budget: Optional[str] = Field(None, description="预算")
    cost: Optional[float] = Field(None, description="支出")
    discount: Optional[float] = Field(None, description="折扣")
    draw_quantity: Optional[float] = Field(None, description="领取数")
    exchange_quantity: Optional[float] = Field(None, description="兑换数")
    exchange_rate: Optional[float] = Field(None, description="兑换率")
    status: Optional[float] = Field(None, description="状态 0其他 1进行中 2已过期 3未开始 4已取消")
    status_text: Optional[str] = Field(None, description="状态说明")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    promotion_type: Optional[float] = Field(None, description="促销类型")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")

class PromotionapiPromotionCouponalldetailbatchListingpage(LingXingModel):
    """listingPage sub-structure."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[float] = Field(None, description="每页大小")
    page_count: Optional[float] = Field(None, description="总页数")
    current: Optional[float] = Field(None, description="当前页数")
    current_size: Optional[float] = Field(None, description="当前页条数")
    records: Optional[list] = Field(None, description="当前页数据")
    has_next_page: Optional[bool] = Field(None, description="是否有下一页")
    has_previous_page: Optional[bool] = Field(None, description="是否有上一页")

class PromotionapiPromotionCouponalldetailbatchOrderpage(LingXingModel):
    """orderPage sub-structure."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[float] = Field(None, description="每页大小")
    page_count: Optional[float] = Field(None, description="总页数")
    current: Optional[float] = Field(None, description="当前页数")
    current_size: Optional[float] = Field(None, description="当前页条数")
    records: Optional[list] = Field(None, description="当前页数据")
    has_next_page: Optional[bool] = Field(None, description="是否有下一页")
    has_previous_page: Optional[bool] = Field(None, description="是否有上一页")

class PromotionapiPromotionCouponalldetailbatchResponse(LingXingModel):
    """查询优惠券详情+listing+订单(批量)."""
    total: Optional[int] = Field(None, description="是")
    promotion_id: Optional[str] = Field(None, description="活动id")
    store_id: Optional[str] = Field(None, description="店铺id")
    coupon: Optional[List[PromotionapiPromotionCouponalldetailbatchCoupon]] = Field(None, description="优惠券信息")
    listing_page: Optional[List[PromotionapiPromotionCouponalldetailbatchListingpage]] = Field(None, description="优惠券涉及的Listing信息")
    order_page: Optional[List[PromotionapiPromotionCouponalldetailbatchOrderpage]] = Field(None, description="优惠券涉及的订单信息")


class PromotionapiPromotionManagementalldetailbatchManagement(LingXingModel):
    """management sub-structure."""
    store_id: Optional[str] = Field(None, description="店铺ID")
    store_name: Optional[str] = Field(None, description="店铺名称")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    promotion_id: Optional[str] = Field(None, description="活动id")
    name: Optional[str] = Field(None, description="名称")
    status: Optional[float] = Field(None, description="状态 0其他 1进行中 2已过期 3未开始 4已取消")
    status_text: Optional[str] = Field(None, description="状态说明")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    promotion_type: Optional[float] = Field(None, description="活动类型 0未定义 1Best Deal 2Lightning Deal 3买一赠一 4购买折扣 5一口价 6折扣 7金额 8社媒促销 9金额")
    promotion_type_text: Optional[str] = Field(None, description="活动类型说明")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    promotion_code: Optional[str] = Field(None, description="优惠码")
    exchange_limit: Optional[float] = Field(None, description="是否限制兑换，1是0否")
    participate_condition: Optional[str] = Field(None, description="兑换限制条件")
    buyer_gets: Optional[str] = Field(None, description="买家获得")
    purchase_product: Optional[str] = Field(None, description="需购买商品")
    discount_product: Optional[str] = Field(None, description="优惠商品")
    exclude_product: Optional[str] = Field(None, description="排除商品")
    tracking_id: Optional[str] = Field(None, description="追踪编码")
    display_on_detail_page: Optional[float] = Field(None, description="是否显示在详情页，1是0否")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    promotion_page_link: Optional[str] = Field(None, description="营销页面链接")

class PromotionapiPromotionManagementalldetailbatchListingpage(LingXingModel):
    """listingPage sub-structure."""
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    records: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    total: Optional[Any] = Field(None, description="是")

class PromotionapiPromotionManagementalldetailbatchOrderpage(LingXingModel):
    """orderPage sub-structure."""
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    records: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    total: Optional[Any] = Field(None, description="是")

class PromotionapiPromotionManagementalldetailbatchResponse(LingXingModel):
    """查询管理促销详情+listing+订单(批量)."""
    total: Optional[int] = Field(None, description="是")
    promotion_id: Optional[str] = Field(None, description="活动id")
    store_id: Optional[str] = Field(None, description="店铺id")
    management: Optional[List[PromotionapiPromotionManagementalldetailbatchManagement]] = Field(None, description="管理促销信息")
    listing_page: Optional[List[PromotionapiPromotionManagementalldetailbatchListingpage]] = Field(None, description="管理促销涉及的Listing信息")
    order_page: Optional[List[PromotionapiPromotionManagementalldetailbatchOrderpage]] = Field(None, description="管理促销涉及的订单信息")


class PromotionapiPromotionPrimediscountalldetailbatchPrimediscount(LingXingModel):
    """primeDiscount sub-structure."""
    store_id: Optional[str] = Field(None, description="店铺ID")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    promotion_id: Optional[str] = Field(None, description="活动id")
    name: Optional[str] = Field(None, description="名称")
    status: Optional[float] = Field(None, description="状态 0其他 1进行中 2已过期 3未开始 4已取消")
    status_text: Optional[str] = Field(None, description="状态说明")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    customer_target: Optional[Any] = Field(None, description="消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣")
    error_count: Optional[str] = Field(None, description=">0 则 需要注意")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    last_sync_time: Optional[Any] = Field(None, description="最后同步时间")
    pull_detail_status: Optional[Any] = Field(None, description="获取详情状态 0=未获取（获取失败），1=获取中，2=获取成功")

class PromotionapiPromotionPrimediscountalldetailbatchListingpage(LingXingModel):
    """listingPage sub-structure."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[float] = Field(None, description="分页每页size")
    page_count: Optional[float] = Field(None, description="总页数")
    current: Optional[float] = Field(None, description="当前页数")
    current_size: Optional[float] = Field(None, description="当前页数据条数")
    records: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[bool] = Field(None, description="是否有下一页")
    has_previous_page: Optional[bool] = Field(None, description="是否有上一页")

class PromotionapiPromotionPrimediscountalldetailbatchOrderpage(LingXingModel):
    """orderPage sub-structure."""
    total: Optional[float] = Field(None, description="总数")
    size: Optional[float] = Field(None, description="分页每页size")
    page_count: Optional[float] = Field(None, description="总页数")
    current: Optional[float] = Field(None, description="当前页数")
    current_size: Optional[float] = Field(None, description="当前页数据条数")
    records: Optional[Any] = Field(None, description="是")
    has_next_page: Optional[bool] = Field(None, description="是否有下一页")
    has_previous_page: Optional[bool] = Field(None, description="是否有上一页")

class PromotionapiPromotionPrimediscountalldetailbatchResponse(LingXingModel):
    """查询会员折扣or价格折扣详情+listing+订单(批量)."""
    total: Optional[int] = Field(None, description="是")
    promotion_id: Optional[str] = Field(None, description="活动id")
    store_id: Optional[str] = Field(None, description="店铺id")
    customer_target: Optional[Any] = Field(None, description="消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣")
    prime_discount: Optional[List[PromotionapiPromotionPrimediscountalldetailbatchPrimediscount]] = Field(None, description="会员折扣or价格折扣信息")
    listing_page: Optional[List[PromotionapiPromotionPrimediscountalldetailbatchListingpage]] = Field(None, description="会员折扣or价格折扣涉及的Listing信息")
    order_page: Optional[List[PromotionapiPromotionPrimediscountalldetailbatchOrderpage]] = Field(None, description="会员折扣or价格折扣涉及的订单信息")


class PromotionapiPromotionSeckillalldetailbatchSeckill(LingXingModel):
    """secKill sub-structure."""
    store_id: Optional[str] = Field(None, description="店铺ID")
    store_name: Optional[str] = Field(None, description="店铺名")
    region_name: Optional[str] = Field(None, description="国家/地区名")
    currency_icon: Optional[str] = Field(None, description="货币icon")
    promotion_id: Optional[str] = Field(None, description="活动id")
    name: Optional[str] = Field(None, description="名称")
    status: Optional[float] = Field(None, description="状态 0其他 1进行中 2已过期 3未开始 4已取消")
    status_text: Optional[str] = Field(None, description="状态说明")
    origin_status: Optional[str] = Field(None, description="促销活动平台状态")
    promotion_type: Optional[float] = Field(None, description="活动类型 0未定义 1Best Deal 2Lightning Deal 3买一赠一 4购买折扣 5一口价 6折扣 7金额 8社媒促销 9金额")
    promotion_type_text: Optional[str] = Field(None, description="活动类型说明")
    promotion_start_time: Optional[str] = Field(None, description="活动开始时间")
    promotion_end_time: Optional[str] = Field(None, description="活动结束时间")
    description: Optional[str] = Field(None, description="描述")
    seckill_fee: Optional[float] = Field(None, description="秒杀费")
    seckill_fee_min: Optional[float] = Field(None, description="秒杀费，最小值")
    seckill_fee_max: Optional[float] = Field(None, description="秒杀费，最大值")
    waived: Optional[bool] = Field(None, description="是否已豁免")
    sales_amount: Optional[float] = Field(None, description="活动总销售额")
    sales_volume: Optional[float] = Field(None, description="活动总销量")
    sold_rate: Optional[float] = Field(None, description="售出率")
    page_view: Optional[str] = Field(None, description="浏览量")
    exchange_rate: Optional[float] = Field(None, description="转化率")
    pcos: Optional[float] = Field(None, description="pcos(费用除以销售额)")

class PromotionapiPromotionSeckillalldetailbatchListingpage(LingXingModel):
    """listingPage sub-structure."""
    total: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    records: Optional[list] = Field(None, description="当前页数据")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")

class PromotionapiPromotionSeckillalldetailbatchOrderpage(LingXingModel):
    """orderPage sub-structure."""
    total: Optional[Any] = Field(None, description="是")
    size: Optional[Any] = Field(None, description="是")
    page_count: Optional[Any] = Field(None, description="是")
    current: Optional[Any] = Field(None, description="是")
    current_size: Optional[Any] = Field(None, description="是")
    records: Optional[list] = Field(None, description="当前页数据")
    has_next_page: Optional[Any] = Field(None, description="是")
    has_previous_page: Optional[Any] = Field(None, description="是")

class PromotionapiPromotionSeckillalldetailbatchResponse(LingXingModel):
    """查询秒杀详情+listing+订单(批量)."""
    total: Optional[int] = Field(None, description="是")
    promotion_id: Optional[str] = Field(None, description="活动id")
    store_id: Optional[str] = Field(None, description="店铺id")
    sec_kill: Optional[List[PromotionapiPromotionSeckillalldetailbatchSeckill]] = Field(None, description="秒杀信息")
    listing_page: Optional[List[PromotionapiPromotionSeckillalldetailbatchListingpage]] = Field(None, description="秒杀涉及的Listing信息")
    order_page: Optional[List[PromotionapiPromotionSeckillalldetailbatchOrderpage]] = Field(None, description="秒杀涉及的订单信息")

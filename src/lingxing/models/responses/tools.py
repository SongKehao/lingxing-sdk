"""Auto-generated response models for Tools."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class SettingsWarningmessageGoodslistMskuList(LingXingModel):
    """msku_list sub-structure."""
    msku: Optional[str] = Field(None, description="MSKU")

class SettingsWarningmessageGoodslistSkuList(LingXingModel):
    """sku_list sub-structure."""
    local_sku: Optional[str] = Field(None, description="本地产品SKU")
    local_name: Optional[str] = Field(None, description="品名")

class SettingsWarningmessageGoodslistResponse(LingXingModel):
    """查询预警消息列表-商品."""
    total: Optional[int] = Field(None, description="总数")
    message_id: Optional[str] = Field(None, description="用户消息id")
    image_url: Optional[str] = Field(None, description="图片地址")
    asin: Optional[str] = Field(None, description="ASIN【父ASIN变更预警时，该值是父ASIN】")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    msku_list: Optional[List[SettingsWarningmessageGoodslistMskuList]] = Field(None, description="mksu列表")
    title: Optional[str] = Field(None, description="标题")
    sku_list: Optional[List[SettingsWarningmessageGoodslistSkuList]] = Field(None, description="sku列表")
    country: Optional[str] = Field(None, description="国家名称")
    model_id: Optional[str] = Field(None, description="模型id")
    model_name: Optional[str] = Field(None, description="预警模型")
    rule_id: Optional[str] = Field(None, description="规则id")
    rule_name: Optional[str] = Field(None, description="规则名称")
    metric: Optional[str] = Field(None, description="监控指标")
    notify_way_str: Optional[str] = Field(None, description="通知方式说明")
    notify_time: Optional[str] = Field(None, description="提醒时间")
    receive_uid: Optional[str] = Field(None, description="接收人id")
    receiver: Optional[str] = Field(None, description="接收人名称")
    handle_status: Optional[str] = Field(None, description="处理状态： 0 待处理 1 已处理")
    handle_status_str: Optional[str] = Field(None, description="处理状态说明")
    read_status: Optional[str] = Field(None, description="阅读状态： 0 未读 1 已读")
    read_status_str: Optional[str] = Field(None, description="阅读状态说明")
    monitor_time: Optional[str] = Field(None, description="预警时间")


class SettingsWarningmessageInventorylistResponse(LingXingModel):
    """查询预警消息列表-库存."""
    total: Optional[int] = Field(None, description="总数")
    message_id: Optional[str] = Field(None, description="用户消息id")
    model_id: Optional[int] = Field(None, description="预警模型id")
    model_name: Optional[str] = Field(None, description="预警模型名称")
    product_type: Optional[int] = Field(None, description="产品类型： 2 MSKU 3 SKU+仓库+店铺+FNSKU")
    product_type_str: Optional[str] = Field(None, description="产品类型说明")
    monitor_type_str: Optional[str] = Field(None, description="监控指标")
    notify_way_str: Optional[str] = Field(None, description="提醒方式")
    notify_time: Optional[str] = Field(None, description="提醒时间")
    receive_uid: Optional[str] = Field(None, description="接收人id")
    receiver: Optional[str] = Field(None, description="接收人名称")
    handle_status: Optional[int] = Field(None, description="处理状态： 0 待处理 1 已处理")
    handle_status_str: Optional[str] = Field(None, description="处理状态说明")
    read_status: Optional[int] = Field(None, description="阅读状态： 0 未读 1 已读")
    read_status_str: Optional[str] = Field(None, description="阅读状态说明")
    monitor_time: Optional[str] = Field(None, description="预警时间")


class ToolCompetitivemonitorListCategoryList(LingXingModel):
    """category_list sub-structure."""
    category_name: Optional[Any] = Field(None, description="[string]")

class ToolCompetitivemonitorListSmallRanks(LingXingModel):
    """small_ranks sub-structure."""
    small_rank: Optional[Any] = Field(None, description="[int]")
    init_small_rank: Optional[Any] = Field(None, description="[int]")
    small_category_text: Optional[Any] = Field(None, description="[string]")

class ToolCompetitivemonitorListResponse(LingXingModel):
    """查询竞品监控列表."""
    total: Optional[int] = Field(None, description="[int]")
    mid: Optional[Any] = Field(None, description="[int]")
    title: Optional[Any] = Field(None, description="[string]")
    asin: Optional[Any] = Field(None, description="[string]")
    asin_url: Optional[Any] = Field(None, description="[string]")
    price: Optional[Any] = Field(None, description="[string]")
    currency: Optional[Any] = Field(None, description="[string]")
    level_name: Optional[Any] = Field(None, description="[string]")
    category_list: Optional[List[ToolCompetitivemonitorListCategoryList]] = Field(None, description="[array]")
    rating: Optional[Any] = Field(None, description="[string]")
    star: Optional[Any] = Field(None, description="[string]")
    review_num: Optional[Any] = Field(None, description="[string]")
    big_category_rank: Optional[Any] = Field(None, description="[string]")
    big_category: Optional[Any] = Field(None, description="[string]")
    init_big_category_rank: Optional[Any] = Field(None, description="[int]")
    small_ranks: Optional[List[ToolCompetitivemonitorListSmallRanks]] = Field(None, description="[array]")
    monitor_status: Optional[Any] = Field(None, description="[int]")
    creator_uid: Optional[Any] = Field(None, description="[string]")
    monitor_uids: Optional[Any] = Field(None, description="[array]")
    creator: Optional[Any] = Field(None, description="[string]")
    last_update_event: Optional[Any] = Field(None, description="[array]")
    search_term: Optional[Any] = Field(None, description="[string]")
    main_image: Optional[Any] = Field(None, description="[string]")
    thumbnail: Optional[Any] = Field(None, description="[array]")
    featurebullets: Optional[Any] = Field(None, description="[array]")
    item_weight: Optional[Any] = Field(None, description="[string]")
    product_dimensions: Optional[Any] = Field(None, description="[string]")
    init_fbm_seller_num: Optional[Any] = Field(None, description="[int]")
    fbm_seller_num: Optional[Any] = Field(None, description="[int]")
    init_fba_seller_num: Optional[Any] = Field(None, description="[int]")
    fba_seller_num: Optional[Any] = Field(None, description="[int]")
    init_buybox_price: Optional[Any] = Field(None, description="[string]")
    buybox_price: Optional[Any] = Field(None, description="[string]")
    buybox_currency: Optional[Any] = Field(None, description="[string]")
    buybox_usd_price: Optional[Any] = Field(None, description="[string]")
    avg_price: Optional[Any] = Field(None, description="[string]")
    avg_currency: Optional[Any] = Field(None, description="[string]")


class ToolToolkeywordrankGetkeywordlistResponse(LingXingModel):
    """关键词列表."""
    id: Optional[int] = Field(None, description="记录唯一id")
    key_word: Optional[str] = Field(None, description="关键词")
    rank: Optional[float] = Field(None, description="排名")
    page: Optional[float] = Field(None, description="页码")
    create_time: Optional[str] = Field(None, description="开始监控时间")
    monitor_time: Optional[str] = Field(None, description="更新时间")
    keyword_remark: Optional[str] = Field(None, description="关键词备注")
    asin: Optional[str] = Field(None, description="监控的asin")
    parent_asin: Optional[str] = Field(None, description="父asin")
    title: Optional[str] = Field(None, description="标题")
    keyword_num: Optional[float] = Field(None, description="关键词数量")
    asin_remark: Optional[str] = Field(None, description="监控asin的备注")
    country: Optional[str] = Field(None, description="国家")
    creator: Optional[str] = Field(None, description="创建人")
    monitors: Optional[list] = Field(None, description="监控人")
    asin_create_time: Optional[str] = Field(None, description="监控asin的创建时间")
    current_page_rank: Optional[float] = Field(None, description="当前页排名: 0 在获取中 1000 未进前6页")
    sbv_page: Optional[float] = Field(None, description="sbv排名: 0 在获取中 1000 未进前6页 -1 没有sbv排名")
    rank_text: Optional[str] = Field(None, description="排名说明")
    sbv_text: Optional[str] = Field(None, description="sbv排名说明")
    is_sponsored: Optional[float] = Field(None, description="监控范围: 1 广告排名 0 自然排名")
    type: Optional[float] = Field(None, description="监控指标: 1 PC端 2 移动端")
    total: Optional[int] = Field(None, description="是")

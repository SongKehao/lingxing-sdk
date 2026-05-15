"""Auto-generated response models for FBASug."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class FbasugAsinGetconfigInfo(LingXingModel):
    """info sub-structure."""
    days_total: Optional[float] = Field(None, description="总备货时长（普通模式）")
    days_total2: Optional[float] = Field(None, description="总备货时长（海外仓中转模式）")
    days_plan: Optional[float] = Field(None, description="采购计划时长")
    days_purchase: Optional[float] = Field(None, description="采购时长")
    days_qc: Optional[float] = Field(None, description="质检时长")
    days_oversea_to_fba: Optional[float] = Field(None, description="海外仓至FBA天数")
    days_frequency_purchase: Optional[float] = Field(None, description="采购频率")
    days_frequency_local_send: Optional[float] = Field(None, description="本地仓发货频率")
    days_frequency_oversea_send: Optional[float] = Field(None, description="海外仓发货频率")
    safe_day: Optional[float] = Field(None, description="安全天数")
    is_ignore_certainly_short: Optional[int] = Field(None, description="建议量扣除必断货量：0 否，1 是")
    is_ignore_history_out_stock: Optional[int] = Field(None, description="历史销量排除断货数据：0 否，1 是")
    days_oversea: Optional[float] = Field(None, description="已弃用（原本地至海外仓天数-海运）")
    days_toucheng: Optional[float] = Field(None, description="已弃用（原本地至FBA天数-海运）")
    days_toucheng_air: Optional[float] = Field(None, description="已弃用（原本地至FBA天数-空运）")
    days_oversea_air: Optional[float] = Field(None, description="已弃用（原本地至海外仓天数-空运）")
    days_frequancy: Optional[float] = Field(None, description="已弃用（原补货频率）")
    sales_avg_3: Optional[float] = Field(None, description="已弃用（原日均销量：3天）")
    sales_avg_7: Optional[float] = Field(None, description="已弃用（原日均销量：7天）")
    sales_avg_14: Optional[float] = Field(None, description="已弃用（原日均销量：14天）")
    sales_avg_30: Optional[float] = Field(None, description="已弃用（原日均销量：30天）")
    sales_avg_60: Optional[float] = Field(None, description="已弃用（原日均销量：60天）")
    sales_avg_90: Optional[float] = Field(None, description="已弃用（原日均销量：90天）")
    default_type_toucheng: Optional[int] = Field(None, description="已弃用（原默认头程物流类型：0 否，1 是）")
    default_type_oversea: Optional[int] = Field(None, description="已弃用（原默认本地发海外仓物流类型：0 否，1 是）")
    sm_fba_list: Optional[list] = Field(None, description="本地仓至FBA时效")
    sm_oversea_list: Optional[list] = Field(None, description="本地仓至海外仓时效")

class FbasugAsinGetconfigList(LingXingModel):
    """list sub-structure."""
    title: Optional[str] = Field(None, description="配置标题")
    is_default: Optional[int] = Field(None, description="是否默认配置： 0 新增配置， 1 默认配置（动态权重）")
    type: Optional[int] = Field(None, description="【is_default=1时字段生效】： 0 自定义， 1 动态销量")
    date_start: Optional[str] = Field(None, description="配置起始日期")
    date_end: Optional[str] = Field(None, description="配置结束日期")
    weigth_3: Optional[float] = Field(None, description="权重：3天")
    weigth_7: Optional[float] = Field(None, description="权重：7天")
    weigth_14: Optional[float] = Field(None, description="权重：14天")
    weigth_30: Optional[float] = Field(None, description="权重：30天")
    weigth_60: Optional[float] = Field(None, description="权重：60天")
    weigth_90: Optional[float] = Field(None, description="权重：90天")
    volume: Optional[float] = Field(None, description="日销量（四舍五入，保留两位小数）")

class FbasugAsinGetconfigDenoise(LingXingModel):
    """denoise sub-structure."""
    title: Optional[str] = Field(None, description="配置名称")
    date_start: Optional[str] = Field(None, description="配置起始日期")
    date_end: Optional[str] = Field(None, description="配置结束日期")
    type: Optional[int] = Field(None, description="类型：1 固定值去噪，2 百分比去噪")
    percent: Optional[float] = Field(None, description="去噪百分比")
    volume: Optional[float] = Field(None, description="日销量")

class FbasugAsinGetconfigResponse(LingXingModel):
    """查询规则 - ASIN."""
    total: Optional[int] = Field(None, description="总数")
    info: Optional[List[FbasugAsinGetconfigInfo]] = Field(None, description="是")
    list: Optional[List[FbasugAsinGetconfigList]] = Field(None, description="日销量设置")
    denoise: Optional[List[FbasugAsinGetconfigDenoise]] = Field(None, description="日销量去噪设置")


class FbasugAsinGetdailysalesinfofeatureList(LingXingModel):
    """list sub-structure."""
    unnamed_field: Optional[list] = Field(None, description="每日数据，[到货量,当日销量,当时实时库存]")

class FbasugAsinGetdailysalesinfofeatureSugDateLine(LingXingModel):
    """sug_date_line sub-structure."""
    date: Optional[str] = Field(None, description="日期")
    desc: Optional[str] = Field(None, description="上个日期到当前区间描述")
    title: Optional[str] = Field(None, description="标题")
    type: Optional[str] = Field(None, description="日期类型： oversea_arrive_date 海外仓到货日 with_safe_day_date 安全天数日 with_days_frequency_date 补货频率日 local_arrive_date 本地到货日 air_arrive_date 空运到货日 sea_arrive_date 海运到货日")

class FbasugAsinGetdailysalesinfofeatureResponse(LingXingModel):
    """按ASIN查询FBA补货建议图表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[FbasugAsinGetdailysalesinfofeatureList]] = Field(None, description="每日数据信息【按天返回360天的数据】")
    sug_date_line: Optional[List[FbasugAsinGetdailysalesinfofeatureSugDateLine]] = Field(None, description="图表时间线")


class FbasugAsinGetinfoMskuList(LingXingModel):
    """msku_list sub-structure."""
    msku: Optional[str] = Field(None, description="MSKU")
    afn_fulfillable_quantity: Optional[float] = Field(None, description="可售：FBA可售库存")
    reserved_fc_transfers: Optional[float] = Field(None, description="调仓中")
    reserved_fc_processing: Optional[float] = Field(None, description="待调仓")

class FbasugAsinGetinfoSuggestSmList(LingXingModel):
    """suggest_sm_list sub-structure."""
    sm_id: Optional[str] = Field(None, description="运输方式id")
    name: Optional[str] = Field(None, description="运输方式名称")
    quantity_sug_local_to_fba: Optional[float] = Field(None, description="建议本地仓发FBA量")
    quantity_sug_local_to_oversea: Optional[float] = Field(None, description="建议本地仓发海外仓量")
    quantity_sug_purchase: Optional[float] = Field(None, description="建议采购量")

class FbasugAsinGetinfoResponse(LingXingModel):
    """查询建议信息-ASIN."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    asin: Optional[str] = Field(None, description="ASIN")
    mode: Optional[str] = Field(None, description="模式： 0 普通 1 海外仓中转")
    quantity_fba_valid: Optional[float] = Field(None, description="数量：FBA可售")
    msku_list: Optional[List[FbasugAsinGetinfoMskuList]] = Field(None, description="MSKU库存信息")
    quantity_sug_purchase: Optional[float] = Field(None, description="建议采购量")
    quantity_sug_local_to_oversea: Optional[float] = Field(None, description="建议本地发海外仓量（海外仓中转模式）")
    quantity_sug_local_to_fba: Optional[float] = Field(None, description="建议本地发FBA量（普通模式）")
    quantity_sug_oversea_to_fba: Optional[float] = Field(None, description="建议海外仓发FBA量")
    sug_date_send_local: Optional[str] = Field(None, description="建议本地发货日")
    sug_date_send_oversea: Optional[str] = Field(None, description="建议海外仓发货日")
    sug_date_purchase: Optional[str] = Field(None, description="建议采购日")
    sales_avg_3: Optional[float] = Field(None, description="日均：3天")
    sales_avg_7: Optional[float] = Field(None, description="日均：7天")
    sales_avg_14: Optional[float] = Field(None, description="日均：14天")
    sales_avg_30: Optional[float] = Field(None, description="日均：30天")
    sales_avg_60: Optional[float] = Field(None, description="日均：60天")
    sales_avg_90: Optional[float] = Field(None, description="日均：90天")
    sales_total_3: Optional[int] = Field(None, description="3日总销量")
    sales_total_7: Optional[int] = Field(None, description="7日总销量")
    sales_total_14: Optional[int] = Field(None, description="14日总销量")
    sales_total_30: Optional[int] = Field(None, description="30日总销量")
    sales_total_60: Optional[int] = Field(None, description="60日总销量")
    sales_total_90: Optional[int] = Field(None, description="90日总销量")
    suggest_sm_list: Optional[List[FbasugAsinGetinfoSuggestSmList]] = Field(None, description="运输方式列表")
    quantity_sug_purchase_air: Optional[float] = Field(None, description="已弃用（建议采购量（空运））")
    quantity_sug_purchase_sea: Optional[float] = Field(None, description="已弃用（建议采购量（海运））")
    quantity_sug_local_to_oversea_air: Optional[float] = Field(None, description="已弃用（建议本地发海外仓量（空运）（海外仓模式））")
    quantity_sug_local_to_oversea_sea: Optional[float] = Field(None, description="已弃用（建议本地发海外仓量（海运）（海外仓模式））")
    quantity_sug_local_to_fba_air: Optional[float] = Field(None, description="已弃用（建议本地发FBA量（空运））")
    quantity_sug_local_to_fba_sea: Optional[float] = Field(None, description="已弃用（建议本地发FBA量（海运））")


class FbasugAsinGetsourcelistSourceList(LingXingModel):
    """source_list sub-structure."""
    quantity: Optional[dict] = Field(None, description="数量")
    type: Optional[dict] = Field(None, description="数据类型： 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途")
    amazon_sale_date: Optional[str] = Field(None, description="预计FBA可售时间")
    remark: Optional[dict] = Field(None, description="备注")
    expect_arrive_time: Optional[str] = Field(None, description="预计到货时间，仅type=5 或 type=9时")

class FbasugAsinGetsourcelistResponse(LingXingModel):
    """查询报表型数据明细-ASIN."""
    mode: Optional[str] = Field(None, description="补货建议模式： 0 普通模式 1 海外仓中转模式")
    source_list: Optional[List[FbasugAsinGetsourcelistSourceList]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总数")


class FbasugAsinSetconfigsResponse(LingXingModel):
    """批量设置规则 - ASIN."""
    total: Optional[int] = Field(None, description="总数")


class FbasugMskuGetconfigInfo(LingXingModel):
    """info sub-structure."""
    days_total: Optional[float] = Field(None, description="总备货时长（普通模式）")
    days_total2: Optional[float] = Field(None, description="总备货时长（海外仓中转模式）")
    days_plan: Optional[float] = Field(None, description="采购计划时长")
    days_purchase: Optional[float] = Field(None, description="采购时长")
    days_qc: Optional[float] = Field(None, description="质检时长")
    days_oversea_to_fba: Optional[float] = Field(None, description="海外仓至FBA天数")
    days_frequency_purchase: Optional[float] = Field(None, description="采购频率")
    days_frequency_local_send: Optional[float] = Field(None, description="本地仓发货频率")
    days_frequency_oversea_send: Optional[float] = Field(None, description="海外仓发货频率")
    safe_day: Optional[float] = Field(None, description="安全天数")
    is_ignore_certainly_short: Optional[int] = Field(None, description="建议量扣除必断货量：0 否，1 是")
    is_ignore_history_out_stock: Optional[int] = Field(None, description="历史销量排除断货数据：0 否，1 是")
    days_oversea: Optional[float] = Field(None, description="已弃用（原本地至海外仓天数-海运）")
    days_toucheng: Optional[float] = Field(None, description="已弃用（原本地至FBA天数-海运）")
    days_toucheng_air: Optional[float] = Field(None, description="已弃用（原本地至FBA天数-空运）")
    days_oversea_air: Optional[float] = Field(None, description="已弃用（原本地至海外仓天数-空运）")
    days_frequancy: Optional[float] = Field(None, description="已弃用（原补货频率）")
    sales_avg_3: Optional[float] = Field(None, description="已弃用（原日均销量：3天）")
    sales_avg_7: Optional[float] = Field(None, description="已弃用（原日均销量：7天）")
    sales_avg_14: Optional[float] = Field(None, description="已弃用（原日均销量：14天）")
    sales_avg_30: Optional[float] = Field(None, description="已弃用（原日均销量：30天）")
    sales_avg_60: Optional[float] = Field(None, description="已弃用（原日均销量：60天）")
    sales_avg_90: Optional[float] = Field(None, description="已弃用（原日均销量：90天）")
    default_type_toucheng: Optional[int] = Field(None, description="已弃用（原默认头程物流类型：0 否，1 是）")
    default_type_oversea: Optional[int] = Field(None, description="已弃用（原默认本地发海外仓物流类型：0 否，1 是）")
    sm_fba_list: Optional[list] = Field(None, description="本地仓至FBA时效")
    sm_oversea_list: Optional[list] = Field(None, description="本地仓至海外仓时效")

class FbasugMskuGetconfigList(LingXingModel):
    """list sub-structure."""
    title: Optional[str] = Field(None, description="配置标题")
    is_default: Optional[int] = Field(None, description="是否默认配置： 0 新增配置， 1 默认配置（动态权重）")
    type: Optional[int] = Field(None, description="【is_default=1时字段生效】： 0 自定义， 1 动态销量")
    date_start: Optional[str] = Field(None, description="配置起始日期")
    date_end: Optional[str] = Field(None, description="配置结束日期")
    weigth_3: Optional[float] = Field(None, description="权重：3天")
    weigth_7: Optional[float] = Field(None, description="权重：7天")
    weigth_14: Optional[float] = Field(None, description="权重：14天")
    weigth_30: Optional[float] = Field(None, description="权重：30天")
    weigth_60: Optional[float] = Field(None, description="权重：60天")
    weigth_90: Optional[float] = Field(None, description="权重：90天")
    volume: Optional[float] = Field(None, description="日销量（四舍五入，保留两位小数）")

class FbasugMskuGetconfigDenoise(LingXingModel):
    """denoise sub-structure."""
    title: Optional[str] = Field(None, description="配置名称")
    date_start: Optional[str] = Field(None, description="配置起始日期")
    date_end: Optional[str] = Field(None, description="配置结束日期")
    type: Optional[int] = Field(None, description="类型：1 固定值去噪，2 百分比去噪")
    percent: Optional[float] = Field(None, description="去噪百分比")
    volume: Optional[float] = Field(None, description="日销量")

class FbasugMskuGetconfigResponse(LingXingModel):
    """查询规则 - MSKU."""
    total: Optional[int] = Field(None, description="总数")
    info: Optional[List[FbasugMskuGetconfigInfo]] = Field(None, description="是")
    list: Optional[List[FbasugMskuGetconfigList]] = Field(None, description="日销量设置")
    denoise: Optional[List[FbasugMskuGetconfigDenoise]] = Field(None, description="日销量去噪设置")


class FbasugMskuGetdailysalesinfofeatureList(LingXingModel):
    """list sub-structure."""
    unnamed_field: Optional[list] = Field(None, description="每日数据，[到货量,当日销量,当时实时库存]")

class FbasugMskuGetdailysalesinfofeatureSugDateLine(LingXingModel):
    """sug_date_line sub-structure."""
    date: Optional[str] = Field(None, description="日期")
    desc: Optional[str] = Field(None, description="上个日期到当前区间描述")
    title: Optional[str] = Field(None, description="标题")
    type: Optional[str] = Field(None, description="日期类型： oversea_arrive_date 海外仓到货日 with_safe_day_date 安全天数日 with_days_frequency_date 补货频率日 local_arrive_date 本地到货日 air_arrive_date 空运到货日 sea_arrive_date 海运到货日")

class FbasugMskuGetdailysalesinfofeatureResponse(LingXingModel):
    """按MSKU查询FBA补货建议图表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[FbasugMskuGetdailysalesinfofeatureList]] = Field(None, description="每日数据信息【按天返回360天的数据】")
    sug_date_line: Optional[List[FbasugMskuGetdailysalesinfofeatureSugDateLine]] = Field(None, description="图表时间线")


class FbasugMskuGetinfoMskuList(LingXingModel):
    """msku_list sub-structure."""
    msku: Optional[str] = Field(None, description="MSKU")
    afn_fulfillable_quantity: Optional[float] = Field(None, description="可售：FBA可售库存")
    reserved_fc_transfers: Optional[float] = Field(None, description="调仓中")
    reserved_fc_processing: Optional[float] = Field(None, description="待调仓")

class FbasugMskuGetinfoSuggestSmList(LingXingModel):
    """suggest_sm_list sub-structure."""
    sm_id: Optional[str] = Field(None, description="运输方式id")
    name: Optional[str] = Field(None, description="运输方式名称")
    quantity_sug_local_to_fba: Optional[float] = Field(None, description="建议本地仓发FBA量")
    quantity_sug_local_to_oversea: Optional[float] = Field(None, description="建议本地仓发海外仓量")
    quantity_sug_purchase: Optional[float] = Field(None, description="建议采购量")

class FbasugMskuGetinfoResponse(LingXingModel):
    """查询建议信息-MSKU."""
    total: Optional[int] = Field(None, description="总数")
    sid: Optional[int] = Field(None, description="店铺id")
    msku: Optional[str] = Field(None, description="MSKU")
    mode: Optional[float] = Field(None, description="补货建议模式： 0 普通 1 海外仓中转")
    quantity_sug_replenishment: Optional[float] = Field(None, description="建议采购量")
    quantity_sug_send: Optional[float] = Field(None, description="建议发货量")
    quantity_fba_valid: Optional[float] = Field(None, description="数量：FBA可售")
    msku_list: Optional[List[FbasugMskuGetinfoMskuList]] = Field(None, description="MSKU库存信息")
    quantity_sug_purchase: Optional[float] = Field(None, description="建议采购量")
    quantity_sug_local_to_oversea: Optional[float] = Field(None, description="建议本地发海外仓量（海外仓中转模式）")
    quantity_sug_local_to_fba: Optional[float] = Field(None, description="建议本地发FBA量（普通模式）")
    quantity_sug_oversea_to_fba: Optional[float] = Field(None, description="建议海外仓发FBA量")
    sug_date_send_local: Optional[str] = Field(None, description="建议本地发货日")
    sug_date_send_oversea: Optional[str] = Field(None, description="建议海外仓发货日")
    sug_date_purchase: Optional[str] = Field(None, description="建议采购日")
    sales_avg_3: Optional[float] = Field(None, description="日均：3天")
    sales_avg_7: Optional[float] = Field(None, description="日均：7天")
    sales_avg_14: Optional[float] = Field(None, description="日均：14天")
    sales_avg_30: Optional[float] = Field(None, description="日均：30天")
    sales_avg_60: Optional[float] = Field(None, description="日均：60天")
    sales_avg_90: Optional[float] = Field(None, description="日均：90天")
    sales_total_3: Optional[int] = Field(None, description="3日总销量")
    sales_total_7: Optional[int] = Field(None, description="7日总销量")
    sales_total_14: Optional[int] = Field(None, description="14日总销量")
    sales_total_30: Optional[int] = Field(None, description="30日总销量")
    sales_total_60: Optional[int] = Field(None, description="60日总销量")
    sales_total_90: Optional[int] = Field(None, description="90日总销量")
    suggest_sm_list: Optional[List[FbasugMskuGetinfoSuggestSmList]] = Field(None, description="运输方式列表")
    quantity_sug_purchase_air: Optional[float] = Field(None, description="已弃用（建议采购量（空运））")
    quantity_sug_purchase_sea: Optional[float] = Field(None, description="已弃用（建议采购量（海运））")
    quantity_sug_local_to_oversea_air: Optional[float] = Field(None, description="已弃用（建议本地发海外仓量（空运）（海外仓模式））")
    quantity_sug_local_to_oversea_sea: Optional[float] = Field(None, description="已弃用（建议本地发海外仓量（海运）（海外仓模式））")
    quantity_sug_local_to_fba_air: Optional[float] = Field(None, description="已弃用（建议本地发FBA量（空运））")
    quantity_sug_local_to_fba_sea: Optional[float] = Field(None, description="已弃用（建议本地发FBA量（海运））")


class FbasugMskuGetsourcelistSourceList(LingXingModel):
    """source_list sub-structure."""
    quantity: Optional[dict] = Field(None, description="数量")
    type: Optional[dict] = Field(None, description="数据类型： 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途")
    amazon_sale_date: Optional[str] = Field(None, description="预计FBA可售时间")
    remark: Optional[dict] = Field(None, description="备注")
    expect_arrive_time: Optional[str] = Field(None, description="预计到货时间，仅type=5 或 type=9时")

class FbasugMskuGetsourcelistResponse(LingXingModel):
    """查询报表型数据明细-MSKU."""
    mode: Optional[str] = Field(None, description="补货建议模式： 0 普通模式 1 海外仓中转模式")
    source_list: Optional[List[FbasugMskuGetsourcelistSourceList]] = Field(None, description="是")
    total: Optional[int] = Field(None, description="总数")


class FbasugMskuSetconfigsResponse(LingXingModel):
    """批量设置规则 - MSKU."""
    total: Optional[int] = Field(None, description="总数")


class RestockingAnalysisGetsummarylistBasicInfo(LingXingModel):
    """basic_info sub-structure."""
    data_type: Optional[int] = Field(None, description="数据类型： 1 asin，2 msku")
    node_type: Optional[int] = Field(None, description="节点类型： 1 共享库存父行 2 共享库存子行 3 非共享库存 4 ASIN+国家汇总行")
    sid: Optional[str] = Field(None, description="店铺id")
    asin: Optional[str] = Field(None, description="ASIN")
    msku_fnsku_list: Optional[list] = Field(None, description="相关msku和fnsku")
    listing_opentime_list: Optional[list] = Field(None, description="listing创建时间")
    sync_time: Optional[str] = Field(None, description="数据更新时间")
    hash_id: Optional[str] = Field(None, description="唯一标识")

class RestockingAnalysisGetsummarylistAmazonQuantityInfo(LingXingModel):
    """amazon_quantity_info sub-structure."""
    amazon_quantity_valid: Optional[float] = Field(None, description="FBA可售")
    amazon_quantity_shipping: Optional[float] = Field(None, description="FBA在途")
    amazon_quantity_shipping_plan: Optional[float] = Field(None, description="预计发货量")
    afn_fulfillable_quantity: Optional[float] = Field(None, description="FBA可售-可售")
    reserved_fc_transfers: Optional[float] = Field(None, description="FBA可售-待调仓")
    reserved_fc_processing: Optional[float] = Field(None, description="FBA可售-调仓中")

class RestockingAnalysisGetsummarylistScmQuantityInfo(LingXingModel):
    """scm_quantity_info sub-structure."""
    sc_quantity_local_valid: Optional[float] = Field(None, description="scm-本地仓可用")
    sc_quantity_oversea_valid: Optional[float] = Field(None, description="scm-海外仓可用")
    sc_quantity_oversea_shipping: Optional[float] = Field(None, description="scm-海外仓在途")
    sc_quantity_local_qc: Optional[float] = Field(None, description="scm-待检待上架量")
    sc_quantity_purchase_plan: Optional[float] = Field(None, description="scm-采购计划")
    sc_quantity_purchase_shipping: Optional[float] = Field(None, description="scm-待交付")
    sc_quantity_local_shipping: Optional[float] = Field(None, description="scm-本地仓在途")

class RestockingAnalysisGetsummarylistSalesInfo(LingXingModel):
    """sales_info sub-structure."""
    sales_avg_3: Optional[float] = Field(None, description="日均销量-3天")
    sales_avg_7: Optional[float] = Field(None, description="日均销量-7天")
    sales_avg_14: Optional[float] = Field(None, description="日均销量-14天")
    sales_avg_30: Optional[float] = Field(None, description="日均销量-30天")
    sales_avg_60: Optional[float] = Field(None, description="日均销量-60天")
    sales_avg_90: Optional[float] = Field(None, description="日均销量-90天")
    sales_total_3: Optional[float] = Field(None, description="总销量-3天")
    sales_total_7: Optional[float] = Field(None, description="总销量-7天")
    sales_total_14: Optional[float] = Field(None, description="总销量-14天")
    sales_total_30: Optional[float] = Field(None, description="总销量-30天")
    sales_total_60: Optional[float] = Field(None, description="总销量-60天")
    sales_total_90: Optional[float] = Field(None, description="总销量-90天")

class RestockingAnalysisGetsummarylistSuggestInfo(LingXingModel):
    """suggest_info sub-structure."""
    out_stock_flag: Optional[int] = Field(None, description="断货标记：0 不会断货，1 会断货")
    out_stock_date: Optional[str] = Field(None, description="断货日期（最早的）")
    estimated_sale_quantity: Optional[float] = Field(None, description="预测销量")
    estimated_sale_avg_quantity: Optional[float] = Field(None, description="预测日均销量")
    available_sale_days: Optional[float] = Field(None, description="预测可售天数")
    fba_available_sale_days: Optional[float] = Field(None, description="预测可售天数（只考虑FBA库存和FBA在途）")
    quantity_sug_purchase: Optional[float] = Field(None, description="建议采购量")
    quantity_sug_local_to_oversea: Optional[float] = Field(None, description="建议本地发海外仓量")
    quantity_sug_local_to_fba: Optional[float] = Field(None, description="建议本地发FBA量")
    quantity_sug_oversea_to_fba: Optional[float] = Field(None, description="建议海外仓发FBA量")
    out_stock_date_purchase: Optional[str] = Field(None, description="断货时间：采购")
    out_stock_date_local: Optional[str] = Field(None, description="断货时间：本地仓发货")
    out_stock_date_oversea: Optional[str] = Field(None, description="断货时间：海外仓发货")
    sug_date_purchase: Optional[str] = Field(None, description="建议采购日")
    sug_date_send_local: Optional[str] = Field(None, description="建议本地仓发货日")
    sug_date_send_oversea: Optional[str] = Field(None, description="建议海外仓发货日")
    suggest_sm_list: Optional[list] = Field(None, description="多运输方式建议量")

class RestockingAnalysisGetsummarylistExtInfo(LingXingModel):
    """ext_info sub-structure."""
    restock_status: Optional[int] = Field(None, description="无需补货标识：0 需要补货，1 无需补货")
    remark: Optional[str] = Field(None, description="备注")
    star: Optional[int] = Field(None, description="是否关注：0 未关注，1 已关注")
    need_flag: Optional[list] = Field(None, description="已弃用（原采、发标识）")

class RestockingAnalysisGetsummarylistResponse(LingXingModel):
    """查询补货列表."""
    total: Optional[int] = Field(None, description="总数")
    basic_info: Optional[List[RestockingAnalysisGetsummarylistBasicInfo]] = Field(None, description="基础数据")
    amazon_quantity_info: Optional[List[RestockingAnalysisGetsummarylistAmazonQuantityInfo]] = Field(None, description="亚马逊数量")
    scm_quantity_info: Optional[List[RestockingAnalysisGetsummarylistScmQuantityInfo]] = Field(None, description="供应链数量")
    sales_info: Optional[List[RestockingAnalysisGetsummarylistSalesInfo]] = Field(None, description="历史销量数据")
    suggest_info: Optional[List[RestockingAnalysisGetsummarylistSuggestInfo]] = Field(None, description="建议数据")
    ext_info: Optional[List[RestockingAnalysisGetsummarylistExtInfo]] = Field(None, description="附加信息")
    item_list: Optional[list] = Field(None, description="子项-结构同父项")

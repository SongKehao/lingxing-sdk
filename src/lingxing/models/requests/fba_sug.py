"""Request models for FBASug APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class FBASugGetSummaryListRequest(LingXingModel):
    """Request for 查询补货列表.
    
    POST /erp/sc/routing/restocking/analysis/getSummaryList
    """
    sid_list: Optional[list] = None  # 店铺id
    data_type: int  # 查询维度：1 asin，2 msku
    asin_list: Optional[list] = None  # 按传入的asin列表筛选数据
    msku_list: Optional[list] = None  # 按传入的msku列表筛选数据
    mode: Optional[int] = None  # 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式（在补货建议列表可切换）】
    listing_date_range: Optional[list] = None  # listing创建时间范围筛选：[开始日期，结束日期]，必须同时包含两个日期才生效
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页条数，默认20，上限50


class FBASugConfigASINRequest(LingXingModel):
    """Request for 查询规则 - ASIN.
    
    POST /erp/sc/routing/fbaSug/asin/getConfig
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN


class FBASugConfigMSKURequest(LingXingModel):
    """Request for 查询规则 - MSKU.
    
    POST /erp/sc/routing/fbaSug/msku/getConfig
    """
    sid: str  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU


class FBASugInfoASINRequest(LingXingModel):
    """Request for 查询建议信息-ASIN.
    
    POST /erp/sc/routing/fbaSug/asin/getInfo
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN
    mode: Optional[int] = None  # 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式】


class FBASugInfoMSKURequest(LingXingModel):
    """Request for 查询建议信息-MSKU.
    
    POST /erp/sc/routing/fbaSug/msku/getInfo
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    mode: Optional[int] = None  # 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式】


class FBASugSetConfigASINRequestSmFbaListItem(LingXingModel):
    sm_id: str  # 运输方式ID
    days: str  # 天数

class FBASugSetConfigASINRequestSmOverseaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigASINRequestConfigListItem(LingXingModel):
    title: str  # 规则名称
    is_default: int  # 是否默认：0 否，1 是
    type: int  # 类型： 0 固定，1 动态
    weigth_3: float  # 权重：3天
    weigth_7: float  # 权重：7天
    weigth_14: float  # 权重：14天
    weigth_30: float  # 权重：30天
    weigth_60: float  # 权重：60天
    weigth_90: float  # 权重：90天
    volume: str  # 日销量（四舍五入，保留两位小数）
    date_start: str  # 开始日期
    date_end: str  # 结束日期

class FBASugSetConfigASINRequestDenoiseListItem(LingXingModel):
    title: str  # 名称
    date_start: str  # 配置起始日期
    date_end: str  # 配置结束日期
    type: int  # 类型：1 固定值去噪，2 百分比去噪
    percent: float  # 去噪百分比
    volume: float  # 日销量

class FBASugSetConfigASINRequest(LingXingModel):
    """Request for 单个设置规则-ASIN.
    
    POST /erp/sc/routing/fbaSug/asin/setConfig
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN
    days_plan: str  # 采购计划时长
    days_qc: str  # 质检时长
    days_oversea_to_fba: float  # 海外仓至FBA天数
    days_frequency_purchase: float  # 采购频率
    days_frequency_local_send: float  # 本地仓发货频率
    days_frequency_oversea_send: float  # 海外仓发货频率
    safe_day: float  # 安全天数
    is_ignore_certainly_short: float  # 建议量扣除必断货量：0 否，1 是
    is_ignore_history_out_stock: float  # 历史销量排除断货数据：0 否，1 是
    days_toucheng: Optional[float] = None  # 已弃用（原本地至FBA天数-海运）
    days_oversea: Optional[float] = None  # 已弃用（原本地至海外仓天数-海运）
    days_toucheng_air: Optional[float] = None  # 已弃用（原本地至FBA时效-空运）
    days_oversea_air: Optional[float] = None  # 已弃用（原本地至海外仓时效-空运）
    default_type_toucheng: Optional[float] = None  # 已弃用（原默认头程物流类型）
    default_type_oversea: Optional[float] = None  # 已弃用（原默认本地发海外仓物流类型）
    days_frequency: Optional[float] = None  # 已弃用（原补货频率）
    sm_fba_list: List[FBASugSetConfigASINRequestSmFbaListItem]
    sm_oversea_list: List[FBASugSetConfigASINRequestSmOverseaListItem]
    config_list: List[FBASugSetConfigASINRequestConfigListItem]
    denoise_list: List[FBASugSetConfigASINRequestDenoiseListItem]


class FBASugSetConfigMSKURequestSmFbaListItem(LingXingModel):
    sm_id: str  # 运输方式ID
    days: str  # 天数

class FBASugSetConfigMSKURequestSmOverseaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigMSKURequestConfigListItem(LingXingModel):
    title: str  # 规则名称
    is_default: int  # 是否默认：0 否，1 是
    type: int  # 类型： 0 固定，1 动态
    weigth_3: float  # 权重：3天
    weigth_7: float  # 权重：7天
    weigth_14: float  # 权重：14天
    weigth_30: float  # 权重：30天
    weigth_60: float  # 权重：60天
    weigth_90: float  # 权重：90天
    volume: str  # 日销量（四舍五入，保留两位小数）
    date_start: str  # 开始日期
    date_end: str  # 结束日期

class FBASugSetConfigMSKURequestDenoiseListItem(LingXingModel):
    title: str  # 名称
    date_start: str  # 配置起始日期
    date_end: str  # 配置结束日期
    type: int  # 类型：1 固定值去噪，2 百分比去噪
    percent: float  # 去噪百分比
    volume: float  # 日销量

class FBASugSetConfigMSKURequest(LingXingModel):
    """Request for 单个设置规则-MSKU.
    
    POST /erp/sc/routing/fbaSug/msku/setConfig
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    days_plan: str  # 采购计划时长
    days_qc: str  # 质检时长
    days_oversea_to_fba: float  # 海外仓至FBA天数
    days_frequency_purchase: float  # 采购频率
    days_frequency_local_send: float  # 本地仓发货频率
    days_frequency_oversea_send: float  # 海外仓发货频率
    safe_day: float  # 安全天数
    is_ignore_certainly_short: float  # 建议量扣除必断货量：0 否，1 是
    is_ignore_history_out_stock: float  # 历史销量排除断货数据：0 否，1 是
    days_toucheng: Optional[float] = None  # 已弃用（原本地至FBA天数-海运）
    days_oversea: Optional[float] = None  # 已弃用（原本地至海外仓天数-海运）
    days_toucheng_air: Optional[float] = None  # 已弃用（原本地至FBA时效-空运）
    days_oversea_air: Optional[float] = None  # 已弃用（原本地至海外仓时效-空运）
    default_type_toucheng: Optional[float] = None  # 已弃用（原默认头程物流类型）
    default_type_oversea: Optional[float] = None  # 已弃用（原默认本地发海外仓物流类型）
    days_frequency: Optional[float] = None  # 已弃用（原补货频率）
    sm_fba_list: List[FBASugSetConfigMSKURequestSmFbaListItem]
    sm_oversea_list: List[FBASugSetConfigMSKURequestSmOverseaListItem]
    config_list: List[FBASugSetConfigMSKURequestConfigListItem]
    denoise_list: List[FBASugSetConfigMSKURequestDenoiseListItem]


class FBASugSetConfigsASINRequestAsinListItem(LingXingModel):
    sid: float  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN

class FBASugSetConfigsASINRequestSmFbaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigsASINRequestSmOverseaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigsASINRequestConfigListItem(LingXingModel):
    title: str  # 规则名称
    is_default: int  # 是否默认：0 否，1 是
    type: int  # 类型： 0 自定义，1 动态销量
    weigth_3: float  # 权重：3天
    weigth_7: float  # 权重：7天
    weigth_14: float  # 权重：14天
    weigth_30: float  # 权重：30天
    weigth_60: float  # 权重：60天
    weigth_90: float  # 权重：90天
    volume: str  # 日销量（四舍五入，保留两位小数）
    date_start: str  # 开始日期
    date_end: str  # 结束日期

class FBASugSetConfigsASINRequestDenoiseListItem(LingXingModel):
    title: str  # 名称
    date_start: str  # 配置起始日期
    date_end: str  # 配置结束日期
    type: int  # 类型：1 固定值去噪，2 百分比去噪
    percent: float  # 去噪百分比
    volume: float  # 日销量

class FBASugSetConfigsASINRequest(LingXingModel):
    """Request for 批量设置规则 - ASIN.
    
    POST /erp/sc/routing/fbaSug/asin/setConfigs
    """
    days_plan: str  # 采购计划时长
    days_qc: str  # 质检时长
    days_oversea_to_fba: float  # 海外仓至FBA天数
    days_frequency_purchase: float  # 采购频率
    days_frequency_local_send: float  # 本地仓发货频率
    days_frequency_oversea_send: float  # 海外仓发货频率
    safe_day: float  # 安全天数
    is_ignore_certainly_short: float  # 建议量扣除必断货量：0 否，1 是
    is_ignore_history_out_stock: float  # 历史销量排除断货数据：0 否，1 是
    days_toucheng: Optional[float] = None  # 已弃用（原本地至FBA天数-海运）
    days_oversea: Optional[float] = None  # 已弃用（原本地至海外仓天数-海运）
    days_toucheng_air: Optional[float] = None  # 已弃用（原本地至FBA时效-空运）
    days_oversea_air: Optional[float] = None  # 已弃用（原本地至海外仓时效-空运）
    default_type_toucheng: Optional[float] = None  # 已弃用（原默认头程物流类型）
    default_type_oversea: Optional[float] = None  # 已弃用（原默认本地发海外仓物流类型 ）
    days_frequency: Optional[float] = None  # 已弃用（原补货频率）
    asin_list: List[FBASugSetConfigsASINRequestAsinListItem]
    sm_fba_list: List[FBASugSetConfigsASINRequestSmFbaListItem]
    sm_oversea_list: List[FBASugSetConfigsASINRequestSmOverseaListItem]
    config_list: List[FBASugSetConfigsASINRequestConfigListItem]
    denoise_list: Optional[List[FBASugSetConfigsASINRequestDenoiseListItem]] = None


class FBASugSetConfigsMSKURequestMskuListItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU

class FBASugSetConfigsMSKURequestSmFbaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigsMSKURequestSmOverseaListItem(LingXingModel):
    sm_id: str  # 运输方式id
    days: str  # 天数

class FBASugSetConfigsMSKURequestConfigListItem(LingXingModel):
    title: str  # 规则名称
    is_default: int  # 是否默认：0 否，1 是
    type: int  # 类型： 0 自定义，1 动态销量
    weigth_3: float  # 权重：3天
    weigth_7: float  # 权重：7天
    weigth_14: float  # 权重：14天
    weigth_30: float  # 权重：30天
    weigth_60: float  # 权重：60天
    weigth_90: float  # 权重：90天
    volume: str  # 日销量（四舍五入，保留两位小数）
    date_start: str  # 开始日期
    date_end: str  # 结束日期

class FBASugSetConfigsMSKURequestDenoiseListItem(LingXingModel):
    title: str  # 名称
    date_start: str  # 配置起始日期
    date_end: str  # 配置结束日期
    type: int  # 类型：1 固定值去噪，2 百分比去噪
    percent: float  # 去噪百分比
    volume: float  # 日销量

class FBASugSetConfigsMSKURequest(LingXingModel):
    """Request for 批量设置规则 - MSKU.
    
    POST /erp/sc/routing/fbaSug/msku/setConfigs
    """
    days_plan: str  # 采购计划时长
    days_qc: str  # 质检时长
    days_oversea_to_fba: float  # 海外仓至FBA天数
    days_frequency_purchase: float  # 采购频率
    days_frequency_local_send: float  # 本地仓发货频率
    days_frequency_oversea_send: float  # 海外仓发货频率
    safe_day: float  # 安全天数
    is_ignore_certainly_short: float  # 建议量扣除必断货量：0 否，1 是
    is_ignore_history_out_stock: float  # 历史销量排除断货数据：0 否，1 是
    days_toucheng: Optional[float] = None  # 已弃用（原本地至FBA天数-海运）
    days_oversea: Optional[float] = None  # 已弃用（原本地至海外仓天数-海运）
    days_toucheng_air: Optional[float] = None  # 已弃用（原本地至FBA时效-空运）
    days_oversea_air: Optional[float] = None  # 已弃用（原本地至海外仓时效-空运）
    default_type_toucheng: Optional[float] = None  # 已弃用（原默认头程物流类型）
    default_type_oversea: Optional[float] = None  # 已弃用（原默认本地发海外仓物流类型 ）
    days_frequency: Optional[float] = None  # 已弃用（原补货频率）
    msku_list: List[FBASugSetConfigsMSKURequestMskuListItem]
    sm_fba_list: List[FBASugSetConfigsMSKURequestSmFbaListItem]
    sm_oversea_list: List[FBASugSetConfigsMSKURequestSmOverseaListItem]
    config_list: List[FBASugSetConfigsMSKURequestConfigListItem]
    denoise_list: List[FBASugSetConfigsMSKURequestDenoiseListItem]


class FBASugSourceListASINRequest(LingXingModel):
    """Request for 查询报表型数据明细-ASIN.
    
    POST /erp/sc/routing/fbaSug/asin/getSourceList
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN
    type: Optional[str] = None  # 数据类型：【默认1】 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途
    mode: Optional[str] = None  # 补货建议模式： 0 普通模式 1 海外仓中转模式 不传默认取erp当前设置模式（在补货建议列表可切换）


class FBASugSourceListMSKURequest(LingXingModel):
    """Request for 查询报表型数据明细-MSKU.
    
    POST /erp/sc/routing/fbaSug/msku/getSourceList
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    type: Optional[str] = None  # 数据类型：【默认1】 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途
    mode: Optional[str] = None  # 补货建议模式： 0 普通模式 1 海外仓中转模式 不传默认取erp当前设置模式（在补货建议列表可切换）


class FBASugDailySalesInfoFeatureASINRequest(LingXingModel):
    """Request for 按ASIN查询FBA补货建议图表.
    
    POST /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin: str  # ASIN
    sug_type: int  # 建议类型： 1 建议采购量 2 建议本地仓发货量 3 建议海外仓发货量
    mode: Optional[int] = None  # 补货建议模式： 0=普通模式 1=海外仓中转模式 不传默认取系统当前设置模式


class FBASugDailySalesInfoFeatureMSKURequest(LingXingModel):
    """Request for 按MSKU查询FBA补货建议图表.
    
    POST /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    msku: str  # MSKU
    sug_type: int  # 建议类型： 1 建议采购量 2 建议本地仓发货量 3 建议海外仓发货量
    mode: Optional[int] = None  # 补货建议模式： 0=普通模式 1=海外仓中转模式 不传默认取系统当前设置模式

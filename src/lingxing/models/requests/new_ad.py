"""Request models for newAd APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class NewadReportSpcampaignreportsRequest(LingXingModel):
    """Request for SP广告活动报表.
    
    POST /pb/openapi/newad/spCampaignReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportCampaignplacementreportsRequest(LingXingModel):
    """Request for SP广告位报告.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSpadgroupreportsRequest(LingXingModel):
    """Request for SP广告组报表.
    
    POST /pb/openapi/newad/spAdGroupReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSpproductadreportsRequest(LingXingModel):
    """Request for SP广告商品报表.
    
    POST /pb/openapi/newad/spProductAdReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSpkeywordreportsRequest(LingXingModel):
    """Request for SP关键词报表.
    
    POST /pb/openapi/newad/spKeywordReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSptargetreportsRequest(LingXingModel):
    """Request for SP商品定位报表.
    
    POST /pb/openapi/newad/spTargetReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportAsinreportsRequest(LingXingModel):
    """Request for SP已购买商品报表.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】，sid跟profile_id其中一个必填
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportQuerywordreportsRequest(LingXingModel):
    """Request for SP用户搜索词报表.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    target_type: str  # 投放类型【默认 keyword】： keyword 关键词 target 商品投放
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页条数，默认15


class NewadReportHsacampaignreportsRequest(LingXingModel):
    """Request for SB广告活动报表.
    
    POST /pb/openapi/newad/hsaCampaignReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportHsacampaignplacementreportsRequest(LingXingModel):
    """Request for SB广告活动-广告位报告.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportHsaadgroupreportsRequest(LingXingModel):
    """Request for SB广告组报表.
    
    POST /pb/openapi/newad/hsaAdGroupReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportListhsatargetingreportRequest(LingXingModel):
    """Request for SB广告的投放报告.
    
    POST /pb/openapi/newad/listHsaTargetingReport
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    sponsored_type: str  # 广告类型： ALL
    target_type: str  # 投放类型： keyword producttarget ALL
    report_date: str  # 报告日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认10


class NewadReportHsaquerywordreportsRequest(LingXingModel):
    """Request for SB用户搜索词报表.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期
    target_type: str  # 投放类型【默认 keyword】：keyword 关键词
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页条数，默认15


class NewadReportHsapurchasedasinreportsRequest(LingXingModel):
    """Request for SB广告归因于广告的购买报告.
    
    POST /pb/openapi/newad/hsaPurchasedAsinReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportListhsakeywordplacementreportRequest(LingXingModel):
    """Request for SB关键词-广告位报告.
    
    POST /pb/openapi/newad/listHsaKeywordPlacementReport
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    sponsored_type: str  # 广告类型： ALL
    target_type: str  # 投放类型： keyword
    report_date: str  # 报告日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdcampaignreportsRequest(LingXingModel):
    """Request for SD广告活动报表.
    
    POST /pb/openapi/newad/sdCampaignReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdadgroupreportsRequest(LingXingModel):
    """Request for SD广告组报表.
    
    POST /pb/openapi/newad/sdAdGroupReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdproductadreportsRequest(LingXingModel):
    """Request for SD广告商品报表.
    
    POST /pb/openapi/newad/sdProductAdReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdtargetreportsRequest(LingXingModel):
    """Request for SD商品定位报表.
    
    POST /pb/openapi/newad/sdTargetReports
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报告日期，格式：Y-m-d
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdasinreportsRequest(LingXingModel):
    """Request for SD已购买商品报表.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期，格式：Y-m-d
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportSdmatchtargetreportsRequest(LingXingModel):
    """Request for SD匹配的目标报表.
    
    POST 
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    report_date: str  # 报表日期
    show_detail: Optional[int] = None  # 是否展示完整归因期信息【默认0】：0 否，1 是
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页条数，默认15


class NewadReportSpcampaignhourdataRequest(LingXingModel):
    """Request for SP广告活动小时数据.
    
    POST /pb/openapi/newad/spCampaignHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSpadgrouphourdataRequest(LingXingModel):
    """Request for SP广告组小时数据.
    
    POST /pb/openapi/newad/spAdGroupHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSpadvertisehourdataRequest(LingXingModel):
    """Request for SP广告小时数据.
    
    POST /pb/openapi/newad/spAdvertiseHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id
    agg_dimension: str  # 聚合维度:  ad  广告维度  both_ad_target  广告+投放维度


class NewadReportSptargethourdataRequest(LingXingModel):
    """Request for SP投放小时数据.
    
    POST /pb/openapi/newad/spTargetHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id
    agg_dimension: str  # 聚合维度: target  投放维度 both_ad_target  广告+投放维度   both_target_placement 投放+广告位placement维度


class NewadReportSbcampaignhourdataRequest(LingXingModel):
    """Request for SB广告活动小时数据.
    
    POST /pb/openapi/newad/sbCampaignHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSbadgrouphourdataRequest(LingXingModel):
    """Request for SB广告组小时数据.
    
    POST /pb/openapi/newad/sbAdGroupHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSbtargethourdataRequest(LingXingModel):
    """Request for SB投放小时数据.
    
    POST /pb/openapi/newad/sbTargetHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id
    agg_dimension: str  # 聚合维度： target  投放


class NewadReportSbadplacementhourdataRequest(LingXingModel):
    """Request for SB广告位小时数据.
    
    POST /pb/openapi/newad/sbAdPlacementHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSdcampaignhourdataRequest(LingXingModel):
    """Request for SD广告活动小时数据.
    
    POST /pb/openapi/newad/sdCampaignHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSdadgrouphourdataRequest(LingXingModel):
    """Request for SD广告组小时数据.
    
    POST /pb/openapi/newad/sdAdGroupHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id


class NewadReportSdadvertisehourdataRequest(LingXingModel):
    """Request for SD广告小时数据.
    
    POST /pb/openapi/newad/sdAdvertiseHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id
    agg_dimension: str  # 聚合维度: ad  广告维度 both_ad_target  广告+投放维度


class NewadReportSdtargethourdataRequest(LingXingModel):
    """Request for SD投放小时数据.
    
    POST /pb/openapi/newad/sdTargetHourData
    """
    report_date: str  # 报告日期，格式：Y-m-d 只能查询最近60天
    campaign_id: float  # 广告活动id
    agg_dimension: str  # 聚合维度: target  投放维度 both_ad_target  广告+投放维度


class NewadReportDspreportorderlistRequest(LingXingModel):
    """Request for 查询DSP报告列表-订单.
    
    POST /basicOpen/dspReport/order/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20
    profile_id: str  # 亚马逊店铺数字id，查询广告账号列表接口对应字段【profile_id】
    start_date: str  # 报告开始日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: str  # 报告结束日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天


class NewadReportProductAnalysisListRequest(LingXingModel):
    """Request for 出单时段分析（产品）.
    
    POST /basicOpen/adReport/productOrderAnalysis/list
    """
    sid: str  # sid
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    sku: List  # msku最多10个
    start_date: str  # 开始日期，格式：Y-m-d
    end_date: str  # 结束日期，格式：Y-m-d
    group_type: str  # 时间维度 hourly 按小时 weekly 按周
    sponsored_type: Optional[list] = None  # 广告类型  sp   sd


class NewadBasedataNewadsbdivideasinreportsRequest(LingXingModel):
    """Request for SB分摊.
    
    POST /pb/openapi/newad/sbDivideAsinReports
    """
    profile_id: int  # 店铺profile_id
    report_date: str  # 报告日期
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token和offset同时存在时以next_token为主


class NewadBasedataPortfoliosRequest(LingXingModel):
    """Request for 广告组合.
    
    POST /pb/openapi/newad/portfolios
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSpcampaignsRequest(LingXingModel):
    """Request for SP广告活动.
    
    POST /pb/openapi/newad/spCampaigns
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSpadgroupsRequest(LingXingModel):
    """Request for SP广告组.
    
    POST /pb/openapi/newad/spAdGroups
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSpproductadsRequest(LingXingModel):
    """Request for SP广告商品.
    
    POST /pb/openapi/newad/spProductAds
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSpkeywordsRequest(LingXingModel):
    """Request for SP关键词.
    
    POST /pb/openapi/newad/spKeywords
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSptargetsRequest(LingXingModel):
    """Request for SP商品定位.
    
    POST /pb/openapi/newad/spTargets
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSpnegativetargetsorkeywordsRequest(LingXingModel):
    """Request for SP否定投放.
    
    POST /pb/openapi/newad/spNegativeTargetsOrKeywords
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    campaign_id: Optional[float] = None  # 广告活动id
    target_type: str  # 投放类型：keyword target
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataHsacampaignsRequest(LingXingModel):
    """Request for SB广告活动.
    
    POST /pb/openapi/newad/hsaCampaigns
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataHsaadgroupsRequest(LingXingModel):
    """Request for SB广告组.
    
    POST /pb/openapi/newad/hsaAdGroups
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态:状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSbtargetingRequest(LingXingModel):
    """Request for SB广告的投放.
    
    POST /pb/openapi/newad/sbTargeting
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    ads_type: str  # 广告类型： SB 返回SB广告数据 SBV 返回SBV广告数据 ALL 同时返回SB和SBV广告数据
    targeting_type: str  # 投放类型： keyword 返回关键词数据 producttarget 返回商品定位数据 ALL：同时返回关键词和商品定位数据
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataHsanegativekeywordsRequest(LingXingModel):
    """Request for SB否定关键词.
    
    POST /pb/openapi/newad/hsaNegativeKeywords
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataHsanegativetargetsRequest(LingXingModel):
    """Request for SB否定商品投放.
    
    POST /pb/openapi/newad/hsaNegativeTargets
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSdcampaignsRequest(LingXingModel):
    """Request for SD广告活动.
    
    POST /pb/openapi/newad/sdCampaigns
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSdadgroupsRequest(LingXingModel):
    """Request for SD广告组.
    
    POST /pb/openapi/newad/sdAdGroups
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSdproductadsRequest(LingXingModel):
    """Request for SD广告商品.
    
    POST /pb/openapi/newad/sdProductAds
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSdtargetsRequest(LingXingModel):
    """Request for SD商品定位.
    
    POST /pb/openapi/newad/sdTargets
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataSdnegativetargetsRequest(LingXingModel):
    """Request for SD否定商品定位.
    
    POST /pb/openapi/newad/sdNegativeTargets
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    profile_id: int  # VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填
    state: Optional[str] = None  # 状态：【不传默认为所有】 enabled paused archived
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15
    next_token: Optional[str] = None  # 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主


class NewadBasedataDspaccountlistRequest(LingXingModel):
    """Request for 查询广告账号列表.
    
    POST /basicOpen/baseData/account/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20
    type: str  # 类型：  dsp   seller   vendor


class NewadReportdownloadAbareportRequest(LingXingModel):
    """Request for ABA搜索词报告-按周维度.
    
    POST /pb/openapi/newad/abaReport
    """
    country: str  # 国家代码：如US
    data_start_time: str  # 报表开始日期：每周周日的日期，仅支持最近45天


class NewadApilogstandardRequest(LingXingModel):
    """Request for 操作日志（新）.
    
    POST /pb/openapi/newad/apiLogStandard
    """
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    log_source: str  # 日志来源： all 包括ERP和亚马逊后台的操作 erp 仅ERP中调整广告的日志 amazon 亚马逊后台的日志
    sponsored_type: str  # 广告类型： sp 返回sp操作日志 sb 返回sb操作日志 sd 返回sd操作日志
    operate_type: str  # 对象类型: campaigns 广告活动 adGroups 广告组 productAds 广告 keywords 关键词 negativeKeywords 否定关键词 targets 商品投放 neg
    start_date: str  # 起始时间，格式：Y-m-d【日期间隔不能超过一个月】
    end_date: str  # 结束时间，格式：Y-m-d【日期间隔不能超过一个月】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15


class NewadReportWalmartQueryAdvertiserListRequest(LingXingModel):
    """Request for 查询沃尔玛广告主列表.
    
    POST /basicOpen/adReport/advertiser/list
    """
    searchText: Optional[str] = None  # 广告主名称模糊搜索
    paging: str  # 不分页传false  分页传true
    limit: Optional[int] = None  # 分页条数
    page: Optional[int] = None  # 页码

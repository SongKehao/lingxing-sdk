"""Request models for MultiPlatform APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class MultiPlatformAdvertisementTiktokAdGroupList12Request(LingXingModel):
    """Request for 查询TikTok-推广广告-广告组.
    
    POST /basicOpen/multiplatform/ads/queryTiktokAdGroupList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号Id列表，Long数组
    bidStrategies: Optional[list] = None  # 出价策略列表，String数组
    budgetTypes: Optional[list] = None  # 预算类型列表，String数组
    campaignIds: Optional[list] = None  # 广告活动id列表，Long数组
    currencies: Optional[list] = None  # 币种列表，String数组
    objectiveType: Optional[list] = None  # 推广目标列表，String数组，枚举值：REACH-覆盖人数, TRAFFIC-访问量, VIDEO_VIEWS-视频播放量, LEAD_GENERATION-线索收集, ENGAGEMENT-社区互
    orderField: Optional[str] = None  # 排序字段（驼峰）
    orderType: Optional[str] = None  # 排序方式
    ownerBcIds: Optional[list] = None  # 广告主BusinessId列表，Long数组
    searchType: Optional[str] = None  # 搜索字段，当字段searchValue有值时，该字段也必须有值，且根据报告类型填写对应的值(advertiser_name-广告账号,ad_group_name-广告组,campaign_name推广
    searchValue: Optional[list] = None  # 搜索值，String数组
    serviceStatus: Optional[list] = None  # 服务状态列表，String数组
    status: Optional[list] = None  # 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS
    summaryCurrency: Optional[str] = None  # 汇总币种


class MultiPlatformAdvertisementTiktokAdList13Request(LingXingModel):
    """Request for 查询TikTok-推广广告-广告.
    
    POST /basicOpen/multiplatform/ads/queryTiktokAdList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    adIds: Optional[list] = None  # 广告id列表，Long数组
    adStyles: Optional[list] = None  # 广告样式列表，String数组
    adgroupIds: Optional[list] = None  # 广告组id列表，String数组
    advertiserIds: Optional[list] = None  # 广告账号Id列表，Long数组
    bidStrategies: Optional[list] = None  # 出价策略列表，String数组
    budgetTypes: Optional[list] = None  # 预算类型列表，String数组
    campaignIds: Optional[list] = None  # 推广系列id列表，String数组
    creativeMaterialTypes: Optional[list] = None  # 创意素材类型列表，String数组
    currencies: Optional[list] = None  # 币种列表，String数组
    orderField: Optional[str] = None  # 排序字段（驼峰）
    orderType: Optional[str] = None  # 排序方式，枚举值：ASC-升序, DESC-降序
    ownerBcIds: Optional[list] = None  # 广告主BusinessId列表，Long数组
    searchType: Optional[str] = None  # 搜索字段，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告
    searchValue: Optional[list] = None  # 搜索值，String数组
    serviceStatus: Optional[list] = None  # 服务状态列表，String数组
    status: Optional[list] = None  # 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS
    summaryCurrency: Optional[str] = None  # 汇总币种
    videoTypes: Optional[list] = None  # 视频类型列表，String数组


class MultiPlatformAdvertisementTiktokAdvertiserList2Request(LingXingModel):
    """Request for 查询TikTok-推广广告-广告帐号.
    
    POST /basicOpen/multiplatform/ads/queryAdvertiserList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号Id列表，Long数组
    advertiserType: Optional[list] = None  # 广告主类型列表，String数组
    bidStrategies: Optional[list] = None  # 出价策略列表，String数组
    budgetTypes: Optional[list] = None  # 预算类型列表，String数组
    currencies: Optional[list] = None  # 币种列表，String数组
    displayTimezones: Optional[list] = None  # 地区时区列表，String数组
    orderField: Optional[str] = None  # 排序字段（驼峰格式）
    orderType: Optional[str] = None  # 排序方式
    ownerBcIds: Optional[list] = None  # 广告主BusinessId列表，Long数组
    searchType: Optional[str] = None  # 搜索字段，当字段searchValue有值时该字段也必须有值，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_n
    searchValue: Optional[list] = None  # 搜索值列表
    serviceStatus: Optional[list] = None  # 服务状态列表，String数组
    status: Optional[list] = None  # 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS
    summaryCurrency: Optional[str] = None  # 汇总币种


class MultiPlatformAdvertisementTiktokCampaignList14Request(LingXingModel):
    """Request for 查询TikTok-推广广告-广告系列.
    
    POST /basicOpen/multiplatform/ads/queryTiktokCampaignList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号Id列表，Long数组
    bidStrategies: Optional[list] = None  # 出价策略列表，String数组
    budgetTypes: Optional[list] = None  # 预算类型列表，String数组
    campaignIds: Optional[list] = None  # 广告活动id列表，Long数组
    currencies: Optional[list] = None  # 币种列表，String数组
    objectiveType: Optional[list] = None  # 推广目标列表，String数组，枚举值：REACH-覆盖人数, TRAFFIC-访问量, VIDEO_VIEWS-视频播放量, LEAD_GENERATION-线索收集, ENGAGEMENT-社区互
    orderField: Optional[str] = None  # 排序字段（驼峰格式）
    orderType: Optional[str] = None  # 排序方式，枚举值：ASC-升序, DESC-降序
    ownerBcIds: Optional[list] = None  # 广告主BusinessId列表，Long数组
    searchType: Optional[str] = None  # 搜索字段，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告。当字段searchValue有值时，该
    searchValue: Optional[list] = None  # 搜索值，String数组
    serviceStatus: Optional[list] = None  # 服务状态列表，String数组
    status: Optional[list] = None  # 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS
    summaryCurrency: Optional[str] = None  # 汇总币种


class MultiPlatformAdvertisementTiktokCommonAdvertiserList4Request(LingXingModel):
    """Request for 查询TikTok-推广广告-广告帐号.
    
    POST /basicOpen/multiplatform/ads/queryCommonAdvertiserList
    """
    internalStatus: Optional[str] = None  # 内部状态，枚举值：ENABLE-启用, DISABLE-禁用, DELETE-删除。用于过滤授权信息表中的状态，不传则返回所有状态的广告账号
    hasGmvStore: Optional[int] = None  # 是否有GMV店铺，枚举值：1-只返回有GMV店铺的广告账号，不传或传其他值则不过滤


class MultiPlatformAdvertisementTiktokGmvAdvertiserReportList5Request(LingXingModel):
    """Request for 查询TikTok-GMV MAX-广告帐号.
    
    POST /basicOpen/multiplatform/ads/queryGmvAdvertiserReportList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填，从1开始
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号ID列表，Long数组，用于筛选特定广告账号
    gmvMaxPromotionTypeCodes: Optional[list] = None  # GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV
    orderField: Optional[str] = None  # 排序字段名称，如：cost, orders, roi
    orderType: Optional[str] = None  # 排序方式，枚举值：ASC-升序, DESC-降序
    ownerBcIds: Optional[list] = None  # 广告主账号ID列表，Long数组，业务负责人的BC ID列表
    status: Optional[list] = None  # 广告账号状态编码列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, 
    storeIds: Optional[list] = None  # 店铺ID列表，Long数组，用于筛选特定店铺的数据
    summaryCurrency: Optional[str] = None  # 汇总币种编码，默认USD，用于统一汇总不同币种的数据


class MultiPlatformAdvertisementTiktokGmvCampaignReportList6Request(LingXingModel):
    """Request for 查询TikTok-GMV MAX-推广系列.
    
    POST /basicOpen/multiplatform/ads/queryGmvCampaignReportList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填，从1开始
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号ID列表，Long数组，用于筛选特定广告账号
    bidTypeCodes: Optional[list] = None  # 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量
    campaignId: Optional[int] = None  # 推广系列ID，用于筛选单个推广系列
    campaignIds: Optional[list] = None  # 推广系列ID列表，Long数组，用于查询多个推广系列
    gmvMaxPromotionTypeCodes: Optional[list] = None  # GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV
    itemGroupIds: Optional[list] = None  # 广告商品ID列表，Long数组，用于筛选特定商品
    orderField: Optional[str] = None  # 排序字段名称，如：cost, orders, roi
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序
    ownerBcIds: Optional[list] = None  # 广告主账号ID列表，Long数组，业务负责人的BC ID列表
    scheduleEndDate: Optional[str] = None  # 排期结束日期，格式：yyyy-MM-dd
    scheduleStartDate: Optional[str] = None  # 排期开始日期，格式：yyyy-MM-dd
    status: Optional[list] = None  # 推广系列操作状态编码列表，String数组，枚举值：ENABLE-已开启, DISABLE-已暂停, DELETE-已删除
    storeIds: Optional[list] = None  # 店铺ID列表，Long数组，用于筛选特定店铺的数据
    summaryCurrency: Optional[str] = None  # 汇总币种编码，用于统一汇总不同币种的数据


class MultiPlatformAdvertisementTiktokGmvItemGroupReportList7Request(LingXingModel):
    """Request for 查询TikTok-GMV MAX-广告商品.
    
    POST /basicOpen/multiplatform/ads/queryGmvItemGroupReportList
    """
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天
    length: Optional[int] = None  # 每页条数，必填，小于2000
    page: Optional[int] = None  # 页码，必填
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    advertiserIds: Optional[list] = None  # 广告账号ID列表，Long数组
    bidTypeCodes: Optional[list] = None  # 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量
    campaignIds: Optional[list] = None  # 推广系列ID列表，Long数组
    itemGroupIds: Optional[list] = None  # 广告商品ID列表，Long数组
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式，枚举值：ASC-升序, DESC-降序
    ownerBcIds: Optional[list] = None  # 广告主账号ID列表，Long数组
    status: Optional[list] = None  # 商品状态编码列表，String数组，枚举值：available-可用, unavailable-不可用
    storeIds: Optional[list] = None  # 店铺ID列表，Long数组
    summaryCurrency: Optional[str] = None  # 汇总币种编码


class MultiPlatformAdvertisementWalmartAdGroupSvList1Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 广告组.
    
    POST /basicOpen/multiplatform/ads/queryAdGroupSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), vid
    dateKey: Optional[str] = None  # 天数据聚合维度，枚举值：day-按天, week-按周, month-按月。【仅天维度接口使用】
    endDate: Optional[str] = None  # 结束日期，格式: yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，格式: yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选广告组
    companyId: Optional[int] = None  # 公司ID
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30。默认14天
    operationSourceType: Optional[str] = None  # 操作来源，默认网页操作
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/att
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告组名称（ad_group_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档


class MultiPlatformAdvertisementWalmartCampaignSpList3Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 广告活动.
    
    POST /basicOpen/multiplatform/ads/queryCampaignSpList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), vid
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    operationSourceType: Optional[str] = None  # 操作来源，openapi调用必传gateway，前端传web
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，openapi必传且小于2000
    paging: Optional[bool] = None  # 是否分页，openapi必填true
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attr
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartGroupSpList9Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 广告组.
    
    POST /basicOpen/multiplatform/ads/queryGroupSpList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，必填，BigInteger数组，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，必填，String数组，枚举值：sponsoredProducts-manual-SP手动, sponsoredProducts-auto-SP自动, sba-SB品牌广告, vid
    day: Optional[int] = None  # 归因天数，必填，数据归因天数，枚举值：3, 14, 30
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    operationSourceType: Optional[str] = None  # 操作来源，必填，openapi调用必传gateway，前端传web
    pageNum: Optional[int] = None  # 页码，必填，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，必填，分页时每页显示的记录数，openapi必传且小于2000
    paging: Optional[bool] = None  # 是否分页，必填，openapi必填true
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选广告组
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attr
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告组名称（ad_group_name）
    status: Optional[list] = None  # 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档


class MultiPlatformAdvertisementWalmartPageTypeSPList10Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 页面类型.
    
    POST /basicOpen/multiplatform/ads/queryPageTypeSPList
    """
    orderType: Optional[str] = None  # orderType
    adDatePicker: Optional[list] = None  # adDatePicker（日期格式：yyyy-MM-dd）
    advertiserIds: Optional[list] = None  # advertiserIds列表
    campaignType: Optional[list] = None  # campaignType列表
    endDate: Optional[str] = None  # 结束日期，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    pageSize: Optional[int] = None  # 每页大小
    campaignIds: Optional[list] = None  # campaignIds列表
    orderField: Optional[str] = None  # orderField
    day: Optional[int] = None  # day
    pageNum: Optional[int] = None  # 页码
    startDate: Optional[str] = None  # 开始日期，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天


class MultiPlatformAdvertisementWalmartReportadgroupsblist15Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 广告组.
    
    POST /basicOpen/multiplatform/ads/reportAdGroupSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选广告组
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告组名称（ad_group_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用，delete-归档


class MultiPlatformAdvertisementWalmartReportaditemsblist16Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 广告.
    
    POST /basicOpen/multiplatform/ads/reportAdItemSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告名称（ad_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用


class MultiPlatformAdvertisementWalmartReportaditemsplist17Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 广告.
    
    POST /basicOpen/multiplatform/ads/reportAdItemSpList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告名称（ad_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用


class MultiPlatformAdvertisementWalmartReportaditemsvlist18Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 广告.
    
    POST /basicOpen/multiplatform/ads/reportAdItemSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告名称（ad_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用


class MultiPlatformAdvertisementWalmartReportcampaignsblist19Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 广告活动.
    
    POST /basicOpen/multiplatform/ads/reportCampaignSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    realtime: Optional[int] = None  # 实时数据标识，0-非实时, 1-实时数据
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportcampaignsvlist20Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 广告活动.
    
    POST /basicOpen/multiplatform/ads/reportCampaignSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    day: Optional[int] = None  # 归因天数，必填，数据归因天数，枚举值：3, 14, 30
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    operationSourceType: Optional[str] = None  # 操作来源，必填，openapi调用必传gateway，前端传web
    pageNum: Optional[int] = None  # 页码，必填，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，必填，openapi必传且小于2000
    paging: Optional[bool] = None  # 是否分页，必填，openapi必填true
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/att
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportkeywordsblist21Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 关键词.
    
    POST /basicOpen/multiplatform/ads/reportKeywordSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Integer数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索关键词文本（keyword_text）
    status: Optional[list] = None  # 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停


class MultiPlatformAdvertisementWalmartReportkeywordsplist22Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 关键词.
    
    POST /basicOpen/multiplatform/ads/reportKeywordSpList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Integer数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索关键词文本（keyword_text）
    status: Optional[list] = None  # 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停


class MultiPlatformAdvertisementWalmartReportkeywordsvlist23Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 关键词.
    
    POST /basicOpen/multiplatform/ads/reportKeywordSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Integer数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索关键词文本（keyword_text）
    status: Optional[list] = None  # 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停


class MultiPlatformAdvertisementWalmartReportpagetypesblist24Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 页面类型.
    
    POST /basicOpen/multiplatform/ads/reportPageTypeSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    pageType: Optional[list] = None  # 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportPageTypeSvList11Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 页面类型.
    
    POST /basicOpen/multiplatform/ads/queryReportPageTypeSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    companyId: Optional[int] = None  # 公司ID
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    operationSourceType: Optional[str] = None  # 操作来源，默认网页操作
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    pageType: Optional[list] = None  # 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportplatformsblist25Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SB广告 - 平台.
    
    POST /basicOpen/multiplatform/ads/reportPlatformSbList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportplatformsplist26Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SP广告 - 平台.
    
    POST /basicOpen/multiplatform/ads/reportPlatformSpList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportplatformsvlist27Request(LingXingModel):
    """Request for 查询沃尔玛-广告 - SV广告 - 平台.
    
    POST /basicOpen/multiplatform/ads/reportPlatformSvList
    """
    advertiserIds: Optional[list] = None  # 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺
    campaignType: Optional[list] = None  # 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), 
    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天
    adGroupIds: Optional[list] = None  # 广告组ID列表，Long数组，按广告组ID筛选
    campaignIds: Optional[list] = None  # 广告活动ID列表，Long数组，按广告活动ID筛选
    day: Optional[int] = None  # 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天
    orderField: Optional[str] = None  # 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attribut
    orderType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC
    pageNum: Optional[int] = None  # 页码，分页时的页码，从1开始
    pageSize: Optional[int] = None  # 每页大小，分页时每页显示的记录数，最大200
    paging: Optional[bool] = None  # 是否分页，默认为true
    searchText: Optional[str] = None  # 搜索文本，模糊搜索广告活动名称（campaign_name）
    searchType: Optional[str] = None  # 搜索类型，目前不用传
    status: Optional[list] = None  # 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议,


class MultiPlatformAdvertisementWalmartReportsearchtrendslist28Request(LingXingModel):
    """Request for 查询沃尔玛-词 - 沃尔玛热门搜索词.
    
    POST /basicOpen/multiplatform/ads/reportSearchTrendsList
    """
    reportDate: Optional[str] = None  # 报告日期，必填，格式：yyyy-MM-dd
    pageSize: Optional[int] = None  # 每页大小，必填，不能大于100
    pageNum: Optional[int] = None  # 页码，必填
    orderType: Optional[str] = None  # 排序方向，枚举值：ASC-升序, DESC-降序
    itemBrand: Optional[dict] = None  # 商品品牌(在item_brand_1/2/3中搜索)，模糊搜索请使用String类型，精确搜索请使用数组类型
    itemQueryType: Optional[int] = None  # 字段类型，枚举值：0-模糊搜索, 1-精确搜索
    itemQueryField: Optional[int] = None  # 查询字段，枚举值：0-itemId, 1-itemName
    searchKeywordType: Optional[int] = None  # 搜索关键词类型，枚举值：0-模糊搜索, 1-精确搜索
    orderField: Optional[str] = None  # 排序字段(驼峰格式)，枚举值：searchKeyword-搜索关键词, keywordRank-关键词排名, totalPctClickShare-前3商品点击占比总和, totalPctConvSh
    searchKeyword: Optional[dict] = None  # 搜索关键词，模糊搜索请使用String类型，精确搜索请使用数组类型
    itemQueryValue: Optional[dict] = None  # 文本框中的值，模糊搜索请使用String类型，精确搜索请使用数组类型
    itemBrandType: Optional[int] = None  # 商品品牌类型，枚举值：0-模糊搜索, 1-精确搜索


class MultiPlatformAdvertisementShopeecampaignreportlistRequestPageItem(LingXingModel):
    page: float  # 当前页码，从 `1` 开始
    length: float  # 每页大小
    orderField: str  # 排序字段，按返回字段名称排序
    orderType: str  # 排序类型： `asc` 升序 `desc` 降序

class MultiPlatformAdvertisementShopeecampaignreportlistRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期，格式：`yyyy-MM-dd`
    endDate: str  # 结束日期，格式：`yyyy-MM-dd`

class MultiPlatformAdvertisementShopeecampaignreportlistRequestFilterItem(LingXingModel):
    shopIds: Optional[list] = None  # 店铺ID列表（复选，为空则代表全部）
    campaignIds: Optional[list] = None  # 广告活动ID列表（复选，为空则代表全部）
    campaignName: Optional[str] = None  # 广告活动名称（模糊搜索）
    statusCodes: Optional[list] = None  # 广告活动状态列表（复选，为空时为全部）： `ongoing` 进行中 `scheduled` 已计划 `ended` 已结束 `paused` 已暂停 `deleted` 已删除 `closed` 已
    placementCategories: Optional[list] = None  # 广告位类别列表（复选，为空时为全部）： `search` 搜索 `discovery` 展示 `all` 全部
    itemIds: Optional[list] = None  # 商品ID列表（复选，为空则代表全部）

class MultiPlatformAdvertisementShopeecampaignreportlistRequest(LingXingModel):
    """Request for 分页查询广告活动报告列表.
    
    POST /basicOpen/multiplatform/ads/shopee/campaign/report/list
    """
    page: MultiPlatformAdvertisementShopeecampaignreportlistRequestPageItem
    period: MultiPlatformAdvertisementShopeecampaignreportlistRequestPeriodItem
    filter: Optional[MultiPlatformAdvertisementShopeecampaignreportlistRequestFilterItem] = None


class MultiPlatformAdvertisementShopeestorereportlistRequestPageItem(LingXingModel):
    page: float  # 当前页码，从 `1` 开始
    length: float  # 每页大小
    orderField: str  # 排序字段，按返回字段名称排序
    orderType: str  # 排序类型： `asc` 升序 `desc` 降序

class MultiPlatformAdvertisementShopeestorereportlistRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期，格式：`yyyy-MM-dd`
    endDate: str  # 结束日期，格式：`yyyy-MM-dd`

class MultiPlatformAdvertisementShopeestorereportlistRequestFilterItem(LingXingModel):
    shopIds: Optional[list] = None  # 店铺ID列表（复选，为空则代表全部）
    isSyncList: Optional[list] = None  # 店铺同步状态列表（复选，为空时为全部）： `0` 停用 `1` 启用

class MultiPlatformAdvertisementShopeestorereportlistRequest(LingXingModel):
    """Request for 分页查询店铺报告列表.
    
    POST /basicOpen/multiplatform/ads/shopee/store/report/list
    """
    page: MultiPlatformAdvertisementShopeestorereportlistRequestPageItem
    period: MultiPlatformAdvertisementShopeestorereportlistRequestPeriodItem
    filter: Optional[MultiPlatformAdvertisementShopeestorereportlistRequestFilterItem] = None


class MultiPlatformAdvertisementLazadaAudienceReportListRequestPageItem(LingXingModel):
    page: Optional[float] = None  # 页码, 默认1
    length: Optional[float] = None  # 每页条数, 默认20
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式 (asc/desc)

class MultiPlatformAdvertisementLazadaAudienceReportListRequestComparisonItem(LingXingModel):
    enableComparison: Optional[str] = None  # 是否启用对比
    comparisonPeriod: Optional[dict] = None  # 对比时间段
    comparisonPeriod__comparisonStartDate: Optional[dict] = None  # 对比开始日期
    comparisonPeriod__comparisonEndDate: Optional[dict] = None  # 对比结束日期

class MultiPlatformAdvertisementLazadaAudienceReportListRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期
    endDate: str  # 结束日期

class MultiPlatformAdvertisementLazadaAudienceReportListRequestConfigItem(LingXingModel):
    summaryCurrencyCode: Optional[str] = None  # 汇总币种代码
    providedSummary: Optional[str] = None  # 提供的汇总方式

class MultiPlatformAdvertisementLazadaAudienceReportListRequestFilterItem(LingXingModel):
    storeIds: Optional[list] = None  # 店铺ID列表
    campaignIds: Optional[list] = None  # 广告活动ID列表
    itemIds: Optional[list] = None  # 商品ID列表
    audienceGroups: Optional[list] = None  # 受众分组列表1=过去15天访问, 2=浏览相似商品, 3=店铺触达受众, 4=店铺兴趣受众, 5=DMP受众, 6=性别, 7=年龄
    audienceFakeIds: Optional[list] = None  # 受众ID列表

class MultiPlatformAdvertisementLazadaAudienceReportListRequest(LingXingModel):
    """Request for Lazada广告-受众报告.
    
    POST /basicOpen/lazadaAd/audience/report/list
    """
    page: MultiPlatformAdvertisementLazadaAudienceReportListRequestPageItem
    comparison: Optional[MultiPlatformAdvertisementLazadaAudienceReportListRequestComparisonItem] = None
    period: MultiPlatformAdvertisementLazadaAudienceReportListRequestPeriodItem
    config: Optional[MultiPlatformAdvertisementLazadaAudienceReportListRequestConfigItem] = None
    filter: Optional[MultiPlatformAdvertisementLazadaAudienceReportListRequestFilterItem] = None


class MultiPlatformAdvertisementLazadaCampaignInfoRequest(LingXingModel):
    """Request for Lazada广告-获取广告活动信息.
    
    POST /basicOpen/lazadaAd/campaign/info
    """
    storeIds: Optional[list] = None  # 店铺ID列表；为空时按当前用户有权限的店铺查询
    campaignName: Optional[str] = None  # 广告活动名称（模糊匹配）
    page: Optional[float] = None  # 页码，从1开始
    length: Optional[float] = None  # 每页条数


class MultiPlatformAdvertisementLazadaCampaignReportListRequestPageItem(LingXingModel):
    page: Optional[float] = None  # 页码, 默认1
    length: Optional[float] = None  # 每页条数, 默认20
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式 (asc/desc)

class MultiPlatformAdvertisementLazadaCampaignReportListRequestComparisonItem(LingXingModel):
    enableComparison: Optional[str] = None  # 是否启用对比
    comparisonPeriod: Optional[dict] = None  # 对比时间段
    comparisonPeriod__comparisonStartDate: Optional[dict] = None  # 对比开始日期
    comparisonPeriod__comparisonEndDate: Optional[dict] = None  # 对比结束日期

class MultiPlatformAdvertisementLazadaCampaignReportListRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期
    endDate: str  # 结束日期

class MultiPlatformAdvertisementLazadaCampaignReportListRequestConfigItem(LingXingModel):
    summaryCurrencyCode: Optional[str] = None  # 汇总币种代码
    providedSummary: Optional[str] = None  # 提供的汇总方式

class MultiPlatformAdvertisementLazadaCampaignReportListRequestFilterItem(LingXingModel):
    storeIds: Optional[list] = None  # 店铺ID列表
    campaignType: Optional[str] = None  # 广告活动类型manual=手动, auto=自动
    statusList: Optional[list] = None  # 状态列表1=开启, 0=关闭
    isAccountBalanceEnough: Optional[float] = None  # 账户余额是否充足0=否 1=是
    isDailyBudgetEnough: Optional[float] = None  # 日预算是否充足0=否 1=是
    campaignName: Optional[str] = None  # 广告活动名称
    campaignIds: Optional[list] = None  # 广告活动ID列表

class MultiPlatformAdvertisementLazadaCampaignReportListRequest(LingXingModel):
    """Request for Lazada广告-广告活动报告.
    
    POST /basicOpen/lazadaAd/campaign/report/list
    """
    page: MultiPlatformAdvertisementLazadaCampaignReportListRequestPageItem
    comparison: Optional[MultiPlatformAdvertisementLazadaCampaignReportListRequestComparisonItem] = None
    period: MultiPlatformAdvertisementLazadaCampaignReportListRequestPeriodItem
    config: Optional[MultiPlatformAdvertisementLazadaCampaignReportListRequestConfigItem] = None
    filter: Optional[MultiPlatformAdvertisementLazadaCampaignReportListRequestFilterItem] = None


class MultiPlatformAdvertisementLazadaItemInfoRequest(LingXingModel):
    """Request for Lazada广告-获取广告商品信息.
    
    POST /basicOpen/lazadaAd/item/info
    """
    storeIds: Optional[list] = None  # 店铺ID列表；为空时按当前用户有权限的店铺查询
    campaignIds: Optional[list] = None  # 广告活动ID列表
    adgroupName: Optional[str] = None  # 广告商品名称（模糊匹配）
    page: Optional[float] = None  # 页码，从1开始
    length: Optional[float] = None  # 每页条数


class MultiPlatformAdvertisementLazadaItemReportListRequestPageItem(LingXingModel):
    page: Optional[float] = None  # 页码, 默认1
    length: Optional[float] = None  # 每页条数, 默认20
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式 (asc/desc)

class MultiPlatformAdvertisementLazadaItemReportListRequestComparisonItem(LingXingModel):
    enableComparison: Optional[str] = None  # 是否启用对比
    comparisonPeriod: Optional[dict] = None  # 对比时间段
    comparisonPeriod__comparisonStartDate: Optional[dict] = None  # 对比开始日期
    comparisonPeriod__comparisonEndDate: Optional[dict] = None  # 对比结束日期

class MultiPlatformAdvertisementLazadaItemReportListRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期
    endDate: str  # 结束日期

class MultiPlatformAdvertisementLazadaItemReportListRequestConfigItem(LingXingModel):
    summaryCurrencyCode: Optional[str] = None  # 汇总币种代码
    providedSummary: Optional[str] = None  # 提供的汇总方式

class MultiPlatformAdvertisementLazadaItemReportListRequestFilterItem(LingXingModel):
    storeIds: Optional[list] = None  # 店铺ID列表
    campaignIds: Optional[list] = None  # 广告活动ID列表
    isProductStockEnough: Optional[float] = None  # 商品库存是否充足0=否 1=是
    isAutoCreative: Optional[float] = None  # 是否自动创意0=否 1=是
    adgroupName: Optional[str] = None  # 广告组名称
    itemIds: Optional[list] = None  # 广告商品ID列表

class MultiPlatformAdvertisementLazadaItemReportListRequest(LingXingModel):
    """Request for Lazada广告-广告商品报告.
    
    POST /basicOpen/lazadaAd/item/report/list
    """
    page: MultiPlatformAdvertisementLazadaItemReportListRequestPageItem
    comparison: Optional[MultiPlatformAdvertisementLazadaItemReportListRequestComparisonItem] = None
    period: MultiPlatformAdvertisementLazadaItemReportListRequestPeriodItem
    config: Optional[MultiPlatformAdvertisementLazadaItemReportListRequestConfigItem] = None
    filter: Optional[MultiPlatformAdvertisementLazadaItemReportListRequestFilterItem] = None


class MultiPlatformAdvertisementLazadaKeywordReportListRequestPageItem(LingXingModel):
    page: Optional[float] = None  # 页码, 默认1
    length: Optional[float] = None  # 每页条数, 默认20
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式 (asc/desc)

class MultiPlatformAdvertisementLazadaKeywordReportListRequestComparisonItem(LingXingModel):
    enableComparison: Optional[str] = None  # 是否启用对比
    comparisonPeriod: Optional[dict] = None  # 对比时间段
    comparisonPeriod__comparisonStartDate: Optional[dict] = None  # 对比开始日期
    comparisonPeriod__comparisonEndDate: Optional[dict] = None  # 对比结束日期

class MultiPlatformAdvertisementLazadaKeywordReportListRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期
    endDate: str  # 结束日期

class MultiPlatformAdvertisementLazadaKeywordReportListRequestConfigItem(LingXingModel):
    summaryCurrencyCode: Optional[str] = None  # 汇总币种代码
    providedSummary: Optional[str] = None  # 提供的汇总方式

class MultiPlatformAdvertisementLazadaKeywordReportListRequestFilterItem(LingXingModel):
    storeIds: Optional[list] = None  # 店铺ID列表
    campaignIds: Optional[list] = None  # 广告活动ID列表
    itemIds: Optional[list] = None  # 商品ID列表
    keyword: Optional[str] = None  # 关键词（模糊搜索 / 单词搜索时使用）
    keywords: Optional[list] = None  # 关键词列表（精确比较时使用，支持批量）
    searchType: Optional[float] = None  # 搜索类型：0-模糊查询（默认），1-精确比较，2-单词搜索
    keywordIds: Optional[list] = None  # 关键词ID列表

class MultiPlatformAdvertisementLazadaKeywordReportListRequest(LingXingModel):
    """Request for Lazada广告-关键词报告.
    
    POST /basicOpen/lazadaAd/keyword/report/list
    """
    page: MultiPlatformAdvertisementLazadaKeywordReportListRequestPageItem
    comparison: Optional[MultiPlatformAdvertisementLazadaKeywordReportListRequestComparisonItem] = None
    period: MultiPlatformAdvertisementLazadaKeywordReportListRequestPeriodItem
    config: Optional[MultiPlatformAdvertisementLazadaKeywordReportListRequestConfigItem] = None
    filter: Optional[MultiPlatformAdvertisementLazadaKeywordReportListRequestFilterItem] = None


class MultiPlatformAdvertisementLazadaStoreReportListRequestPageItem(LingXingModel):
    page: Optional[float] = None  # 页码, 默认1
    length: Optional[float] = None  # 每页条数, 默认20
    orderField: Optional[str] = None  # 排序字段
    orderType: Optional[str] = None  # 排序方式 (asc/desc)

class MultiPlatformAdvertisementLazadaStoreReportListRequestComparisonItem(LingXingModel):
    enableComparison: Optional[str] = None  # 是否启用对比
    comparisonPeriod: Optional[dict] = None  # 对比时间段
    comparisonPeriod__comparisonStartDate: Optional[dict] = None  # 对比开始日期
    comparisonPeriod__comparisonEndDate: Optional[dict] = None  # 对比结束日期

class MultiPlatformAdvertisementLazadaStoreReportListRequestPeriodItem(LingXingModel):
    startDate: str  # 开始日期
    endDate: str  # 结束日期

class MultiPlatformAdvertisementLazadaStoreReportListRequestConfigItem(LingXingModel):
    summaryCurrencyCode: Optional[str] = None  # 汇总币种代码
    providedSummary: Optional[str] = None  # 提供的汇总方式

class MultiPlatformAdvertisementLazadaStoreReportListRequestFilterItem(LingXingModel):
    storeIds: Optional[list] = None  # 店铺ID列表
    isSyncStatusList: Optional[list] = None  # 同步状态列表0=停用, 1=启用

class MultiPlatformAdvertisementLazadaStoreReportListRequest(LingXingModel):
    """Request for Lazada广告-店铺报告.
    
    POST /basicOpen/lazadaAd/store/report/list
    """
    page: MultiPlatformAdvertisementLazadaStoreReportListRequestPageItem
    comparison: Optional[MultiPlatformAdvertisementLazadaStoreReportListRequestComparisonItem] = None
    period: MultiPlatformAdvertisementLazadaStoreReportListRequestPeriodItem
    config: Optional[MultiPlatformAdvertisementLazadaStoreReportListRequestConfigItem] = None
    filter: Optional[MultiPlatformAdvertisementLazadaStoreReportListRequestFilterItem] = None


class MultiPlatformV2ProfitreportmskuRequest(LingXingModel):
    """Request for 查询结算利润（利润报表）-msku.
    
    POST /basicOpen/multiplatform/profit/report/msku
    """
    offset: float  # 分页偏移量，默认0
    length: float  # 分页长度，默认20，最大200
    platformCodeS: Optional[list] = None  # 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein
    mids: Optional[str] = None  # 国家id，多个使用英文逗号分隔
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】
    currencyCode: Optional[str] = None  # 币种code： 原币种 USD EUR GBP CNY
    startDate: str  # 开始时间【结算日期】，闭区间，格式：Y-m-d
    endDate: str  # 结束时间【结算日期】，闭区间，格式：Y-m-d
    searchField: Optional[str] = None  # 搜索值类型： msku MSKU local_sku SKU platform_order_no 平台单号
    searchValue: Optional[str] = None  # 搜索值
    developers: Optional[list] = None  # 开发人
    cids: Optional[list] = None  # 分类
    bids: Optional[list] = None  # 品牌


class MultiPlatformV2ProfitreportskuRequest(LingXingModel):
    """Request for 查询结算利润（利润报表）-sku.
    
    POST /basicOpen/multiplatform/profit/report/sku
    """
    offset: float  # 分页偏移量，默认0
    length: float  # 分页长度，默认1000
    platformCodeS: Optional[list] = None  # 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein
    mids: str  # 国家id，多个使用英文逗号分隔
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】
    currencyCode: Optional[str] = None  # 币种code： 原币种 USD EUR GBP CNY
    startDate: str  # 开始时间【结算日期】，闭区间，格式：Y-m-d
    endDate: str  # 结束时间【结算日期】，闭区间，格式：Y-m-d
    searchField: Optional[str] = None  # 搜索值类型： local_sku SKU platform_order_no 平台单号
    searchValue: Optional[str] = None  # 搜索值
    developers: Optional[list] = None  # 开发人
    cids: Optional[list] = None  # 分类
    bids: Optional[list] = None  # 品牌


class MultiPlatformV2ProfitreportsellerRequest(LingXingModel):
    """Request for 查询结算利润（利润报表）-店铺.
    
    POST /basicOpen/multiplatform/profit/report/seller
    """
    offset: float  # 分页偏移量，默认0
    length: float  # 分页长度，默认1000
    platformCodeS: Optional[list] = None  # 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein
    mids: Optional[str] = None  # 国家id，多个使用英文逗号分隔
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】
    currencyCode: Optional[str] = None  # 币种code： 原币种 USD EUR GBP CNY
    startDate: str  # 开始时间【结算日期】，闭区间，格式：Y-m-d
    endDate: str  # 结束时间【结算日期】，闭区间，格式：Y-m-d


class MultiPlatformV2ProfitreportorderRequest(LingXingModel):
    """Request for 查询结算利润（利润报表）-订单.
    
    POST /basicOpen/multiplatform/profit/report/order
    """
    offset: float  # 分页偏移量，默认0
    length: float  # 分页长度，默认200
    platformCodeS: Optional[list] = None  # 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee 10007 Lazada  10008 walmart 10011 Tikto
    mids: Optional[str] = None  # 国家id，多个使用英文逗号分隔
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】
    transactionTypeS: Optional[list] = None  # 交易类型：0 销售，2 退货，4 退款，5 补发，6 调整，7 其他
    currencyCode: Optional[str] = None  # 币种code：原币种，USD，EUR，GBP，CNY
    searchDateType: Optional[str] = None  # 时间筛选方式：1 下单时间，2 结算日期【默认】，3 发货日期
    startDate: str  # 开始时间【结算日期】，闭区间，格式：Y-m-d
    endDate: str  # 结束时间【结算日期】，闭区间，格式：Y-m-d
    searchField: Optional[str] = None  # 搜索值类型：msku MSKU，local_sku SKU，product_name，品名，platform_order_no 平台单号
    searchValue: Optional[str] = None  # 搜索值


class MultiPlatformV2StoreInfoV2Request(LingXingModel):
    """Request for 查询多平台店铺信息.
    
    POST 
    """
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限200
    platform_code: Optional[list] = None  # 平台code： 10001 AMAZON 10002 Shopify 10003 eBay 10004 Wish 10005 AliExpress 10006 Shopee 10007 Lazada 
    is_sync: Optional[int] = None  # 店铺同步状态： 1 启用 0 停用
    status: Optional[int] = None  # 店铺授权状态： 1 正常授权 0 授权失败


class MultiPlatformV2MultiPlatOrderV2Request(LingXingModel):
    """Request for 查询订单管理订单列表.
    
    POST 
    """
    offset: int  # 分页偏移量
    length: int  # 分页长度，上限500
    date_type: Optional[str] = None  # 时间类型： 更新时间 update_time  订购时间 global_purchase_time  发货时间 global_delivery_time 付款时间 global_payment_tim
    start_time: Optional[int] = None  # 开始时间，时间戳格式【单位：秒】，双开区间 **当且仅当传入平台单号或平台单名称查询时可不必传，查询时间跨度不能超过31天**
    end_time: Optional[int] = None  # 结束时间，时间戳格式【单位：秒】，双开区间 **当且仅当传入平台单号或平台单名称查询时可不必传，查询时间跨度不能超过31天**
    store_id: Optional[list] = None  # 店铺id，取值等同于查询多平台店铺信息返回结果的store_id
    platform_code: Optional[list] = None  # 平台code： 10001 AMAZON 10002 Shopify 10003 eBay 10004 Wish 10005 AliExpress 10006 Shopee 10007 Lazada 
    platform_order_nos: Optional[list] = None  # 平台单号列表 ，元素不超过200个 **以下平台不可用，需要用platform_order_names查询：** **10003-ebay 10014-newegg 10020-coupang 100
    platform_order_names: Optional[list] = None  # 特定平台单号列表 ，元素不超过200个 **10003-ebay 10014-newegg 10020-coupang 10002-shopify 10012-美客多 10016-shopline，使
    order_status: Optional[int] = None  # 订单状态： 1 同步中 2 已同步 3 待付款 4 待审核 5 待发货 6 已发货 7 已取消/不发货 8 不显示 9 平台发货
    platform_shipping_status: Optional[list] = None  # 平台单发货状态 **Shopify**状态枚举值: fulfilled：已发货，并且全部发货 null：未发货 partial：部分发货 restocked：已退货
    platform_payment_status: Optional[list] = None  # 平台单支付状态 **Shopify**状态枚举值: pending：待支付 authorized：买家信用卡支付，并且已经确认授权，但是卖家并未收款 partially_paid：已完成部分款项支付 
    include_delete: Optional[bool] = None  # 是否包含已删除订单 true 包含 false 不包含


class MultiPlatformV2PairListV2Request(LingXingModel):
    """Request for 查询多平台配对列表.
    
    POST 
    """
    length: Optional[int] = None  # 分页条数
    offset: Optional[int] = None  # 分页偏移量
    msku: Optional[list] = None  # MSKU
    sku: Optional[list] = None  # 本地SKU
    start_time: Optional[str] = None  # 操作开始时间，闭区间
    end_time: Optional[str] = None  # 操作结束时间，开区间
    platform_codes: Optional[list] = None  # 平台码
    store_ids: Optional[list] = None  # 店铺id
    use_cursor: Optional[bool] = None  # 分页游标，默认为fasle，如配对数据多时，强烈建议您使用分页游标的方式分页，可加快接口响应速度
    cursor_id: Optional[bool] = None  # 游标id, 当分页游标为true时，该字段必填


class MultiPlatformV2Pairmultiplatformv2RequestPairMultiPlatformListItem(LingXingModel):
    msku: str  # msku
    store_id: str  # 店铺id
    sku: str  # sku

class MultiPlatformV2Pairmultiplatformv2Request(LingXingModel):
    """Request for 批量添加、编辑多平台配对关系.
    
    POST 
    """
    pair_multi_platform_list: List[MultiPlatformV2Pairmultiplatformv2RequestPairMultiPlatformListItem]


class MultiPlatformPreShipmentRequest(LingXingModel):
    """Request for 预发货.
    
    POST /basicOpen/openapi/multiplatform/order/preShipment
    """
    global_order_no: List  # 系统单号列表


class MultiPlatformBatchReviewRequest(LingXingModel):
    """Request for 审核发货.
    
    POST /basicOpen/openapi/multiplatform/order/review
    """
    global_order_no: List  # 系统单号列表


class MultiPlatformV2CreateOrdersV2RequestOrdersItem(LingXingModel):
    platform_order_no: str  # 平台单号【同一店铺不支持重复】
    site_code: Optional[str] = None  # 站点
    buyer_note: Optional[str] = None  # 买家留言
    receiver_country_code: str  # 国家/地区二字简码
    customer_shipping_amount: Optional[float] = None  # 客付运费【币种默认为店铺币种】
    customer_tax_amount: Optional[float] = None  # 客付税费【币种默认为店铺币种】
    order_total_amount: Optional[float] = None  # 订单金额【币种默认为店铺币种】
    wid: Optional[str] = None  # 仓库id ，【当填写了该字段，则logistics_type_id 必填】
    global_purchase_time: Optional[float] = None  # 订购时间(秒级时间戳)
    global_payment_time: Optional[float] = None  # 付款时间(秒级时间戳)
    remark: Optional[str] = None  # 客服备注
    logistics_type_id: Optional[str] = None  # 物流方式id， 【当填写了该字段，则wid必填】
    receiver_name: str  # 收件人
    address_type: Optional[int] = None  # 地址类型  1:住宅地址” 2:“商业地址”
    buyer_choose_express: Optional[str] = None  # 客选物流
    receiver_company_name: Optional[str] = None  # 公司名
    city: str  # 城市
    address_line1: str  # 地址1
    amount_currency: Optional[str] = None  # 币种，默认与店铺的币种一致，ISO 4217标准码
    order_custom_fields: Optional[dict] = None  # 订单自定义字段
    items: List  # 订单产品信息
    items__sku: Optional[str] = None  # 本地SKU（SKU和MSKU必填其中一个）
    items__quantity: int  # 数量
    items__unit_price: float  # 单价【币种默认为店铺币种】
    items__msku: Optional[str] = None  # MSKU（SKU和MSKU必填其中一个）
    items__stock_deduction_type: Optional[str] = None  # 库存扣减类型 1表示“空”， 2表示“SKU+订单店铺”
    items__item_custom_fields: Optional[dict] = None  # 订单产品自定义字段
    shipping_info: Optional[dict] = None  # 物流信息（传则下层全必填）
    shipping_info__tms_waybill_no: str  # 物流号
    shipping_info__tms_tracking_no: str  # 追踪号
    shipping_info__file_name: str  # 面单文件名
    shipping_info__base64File: str  # 面单base64
    sender_tax_type: Optional[int] = None  # "税号类型: 1=>IOSS编号 2=>VAT税号 3=>CPF税号 4=>EORI号码 5=>收件人税号 7=>VOEC税号"
    sender_tax_no: Optional[str] = None  # 税号

class MultiPlatformV2CreateOrdersV2Request(LingXingModel):
    """Request for 创建订单.
    
    POST 
    """
    platform_code: int  # 平台code
    store_id: str  # 店铺id
    orders: List[MultiPlatformV2CreateOrdersV2RequestOrdersItem]


class MultiPlatformV2MergeOrderRequest(LingXingModel):
    """Request for 合并订单.
    
    POST /pb/mp/order/v2/mergeOrder
    """
    platform_code: str  # 平台code【不支持10007 Lazada、10011 TikTok、10012 MERCADO】
    order_list: List  # 系统单号


class MultiPlatformV2SplitOrderRequestOrderItemItem(LingXingModel):
    item_id: str  # 商品行主键id【拆分模式split_mod = 1 时必填】
    quantity: str  # 数量【拆分模式split_mod = 1 时必填】
    pid: str  # 本地商品id【拆分模式split_mod = 2 时必填，没有值传空字符串】
    order_item_no: str  # 订单明细单号【拆分模式split_mod = 2 时必填，没有值传空字符串】
    msku: str  # 平台msku【拆分模式split_mod = 2 时必填，没有值传空字符串】
    platform_order_no: str  # 平台单号【拆分模式split_mod = 2 时必填，没有值传空字符串】

class MultiPlatformV2SplitOrderRequest(LingXingModel):
    """Request for 拆分订单.
    
    POST /pb/mp/order/v2/splitOrder
    """
    split_mod: int  # 拆分模式：1 按商品拆分，2 按捆绑商品拆分
    global_order_no: str  # 系统单号
    order_item: List[MultiPlatformV2SplitOrderRequestOrderItemItem]


class MultiPlatformV2CancelOrderRequest(LingXingModel):
    """Request for 标记订单不发货.
    
    POST /pb/mp/order/v2/cancelOrder
    """
    order_list: List  # 系统单号列表


class MultiPlatformV2SelfshipmentorderdeliverygoodsRequest(LingXingModel):
    """Request for 订单发货.
    
    POST /basicOpen/selfShipmentOrder/deliveryGoods
    """
    order_number_list: str  # 系统单号列表，多个使用英文逗号分隔，上限100


class MultiPlatformV2SetorderweighedRequest(LingXingModel):
    """Request for 订单称重.
    
    POST /erp/sc/routing/wms/order/setOrderWeighed
    """
    order_number: Optional[str] = None  # 系统单号 与销售出库单二选一
    wo_number: Optional[str] = None  # 销售出库单 与系统单号二选一
    pkg_real_weight: str  # 重量
    pkg_real_weight_unit: str  # 单位 支持 g,kg,oz,lb
    sync_product_gross_weight: Optional[str] = None  # 一单一件同步重量到产品模块 0:否,1:是  默认否


class MultiPlatformV2EditOrderV2RequestOrderListItem(LingXingModel):
    global_order_no: int  # 系统单号
    logistics: dict  # 物流信息
    logistics__logistics_type_id: int  # 物流方式id，对应 查询已启用的自发货物流方式 接口字段【type_id】
    logistics__sys_wid: int  # 仓库id，对应 查询仓库列表 接口字段【wid】

class MultiPlatformV2EditOrderV2Request(LingXingModel):
    """Request for 编辑订单.
    
    POST 
    """
    order_list: List[MultiPlatformV2EditOrderV2RequestOrderListItem]


class MultiPlatformV2UpdateOrderV2RequestOrderListItem(LingXingModel):
    address_info: Optional[dict] = None  # 收货信息
    address_info__address_line1: Optional[str] = None  # 详细地址1
    address_info__address_line2: Optional[str] = None  # 详细地址2
    address_info__address_line3: Optional[str] = None  # 详细地址3
    address_info__city: Optional[str] = None  # 城市
    address_info__district: Optional[str] = None  # 区/县
    address_info__doorplate_no: Optional[str] = None  # 门牌号
    address_info__postal_code: Optional[str] = None  # 邮编
    address_info__receiver_company_name: Optional[str] = None  # 公司名
    address_info__receiver_country_code: Optional[str] = None  # 国家/地区二字码
    address_info__receiver_mobile: Optional[str] = None  # 手机
    address_info__receiver_name: Optional[str] = None  # 收件人
    address_info__receiver_tel: Optional[str] = None  # 电话
    address_info__state_or_region: Optional[str] = None  # 省/州
    global_order_no: Optional[int] = None  # 全局系统单号
    logistics: Optional[dict] = None  # 物流信息
    logistics__cod_type: Optional[str] = None  # 是否COD订单（是 or 否）
    logistics__sender_tax_no: Optional[str] = None  # 税号
    logistics__sender_tax_type: Optional[str] = None  # 税号类型（VAT/CPF/IOSS/EORI/收件人税号）
    order_item_list: List  # 商品信息 备注：【可以传空列表】,不传空列表时order_list>>order_item_list>>type必传
    order_item_list__mark: Optional[str] = None  # 商品备注
    order_item_list__msku: Optional[str] = None  # msku
    order_item_list__price: Optional[Any] = None  # 单价
    order_item_list__quantity: Optional[int] = None  # 数量
    order_item_list__sku: Optional[str] = None  # sku
    order_item_list__type: Optional[int] = None  # 编辑类型： 1 新增 2 删除 3 覆盖
    order_item_list__id: Optional[str] = None  # 系统订单商品ID
    order_item_list__platformOrderNo: Optional[str] = None  # 平台单号，该字段在type=1 新增时生效

class MultiPlatformV2UpdateOrderV2Request(LingXingModel):
    """Request for 编辑/更新自发货订单.
    
    POST 
    """
    order_list: List[MultiPlatformV2UpdateOrderV2RequestOrderListItem]


class MultiPlatformV2Mporderupdatev2RequestOrdersItem(LingXingModel):
    global_order_no: str  # 系统单号
    remark: str  # 客服备注文本
    remark_is_append: Optional[str] = None  # 是否追加原有备注：【默认true】 true 追加客服备注 false 替换客服备注

class MultiPlatformV2Mporderupdatev2Request(LingXingModel):
    """Request for 更新订单客服备注.
    
    POST 
    """
    orders: List[MultiPlatformV2Mporderupdatev2RequestOrdersItem]


class MultiPlatformV2FastOutboundV2RequestPackageItem(LingXingModel):
    global_order_no: str  # 系统单号
    wid: float  # 出库仓库ID，可通过查询本地仓库接口获得
    logistics_type_id: str  # 物流商ID-物流方式ID， 物流商ID对应 查询已启用的自发货物流方式 接口字段【logistics_provider_id】 物流方式ID对应 查询已启用的自发货物流方式 接口字段【type_id】
    waybill_no: str  # 运单号
    tracking_no: Optional[str] = None  # 跟踪号
    weight_unit: Optional[str] = None  # 重量单位，可选g、kg，默认g
    real_weight: Optional[str] = None  # 包裹重量
    size_unit: Optional[str] = None  # 尺寸单位，可选mm、cm，默认cm
    length: Optional[str] = None  # 包裹尺寸长
    width: Optional[str] = None  # 包裹尺寸宽
    height: Optional[str] = None  # 包裹尺寸高
    fee_weight: Optional[str] = None  # 包裹计费重
    logistics_freight: Optional[str] = None  # 物流运费
    logistics_freight_currency_code: Optional[str] = None  # 物流运费币种代码，默认 CNY

class MultiPlatformV2FastOutboundV2Request(LingXingModel):
    """Request for 快速出库.
    
    POST /pb/mp/order/v2/fastOutbound
    """
    package: List[MultiPlatformV2FastOutboundV2RequestPackageItem]


class MultiPlatformV2GetFastOutboundResultV2Request(LingXingModel):
    """Request for 获取快速出库结果.
    
    POST /pb/mp/order/v2/getFastOutboundResult
    """
    global_order_no: List  # 系统单号数组，最大1000单


class MultiPlatformV2WalmartPaymentQueryReportRequest(LingXingModel):
    """Request for 查询可用报告列表 - Walmart Payment.
    
    POST /cepf/fms/openapi/walmartPayment/queryReport
    """
    new_report: int  # 是否查询最新的报告：1 是，2 否
    store_id: List  # 店铺id


class MultiPlatformV2WalmartPaymentQueryPageRequest(LingXingModel):
    """Request for 查询报告详情 - Walmart Payment.
    
    POST /cepf/fms/openapi/walmartPayment/queryPage
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15，上限200
    store_id: List  # 店铺id
    report_id: Optional[str] = None  # 报告id 【时间范围 与 报告id 二选一必填】
    transaction_posted_timestamp_start: Optional[str] = None  # 开始时间，格式：Y-m-d 【时间范围 与 报告id 二选一必填】
    transaction_posted_timestamp_end: Optional[str] = None  # 结束时间，格式：Y-m-d 【时间范围 与 报告id 二选一必填】


class MultiPlatformV2QueryShippingListPageRequest(LingXingModel):
    """Request for 查询平台仓发货单列表.
    
    POST /cepf/warehouse/api/openApi/queryShippingListPage
    """
    store_id: Optional[list] = None  # 店铺id
    cargo_code: Optional[str] = None  # 货件单号
    shipping_list_codes: Optional[list] = None  # 发货单编号，上限100
    shipping_list_status: Optional[int] = None  # 发货单状态： 0 待配货  1 待发货 2 已发货 3 已作废
    start_time: Optional[str] = None  # 开始时间【创建时间】，格式：Y-m-d，双闭区间
    end_time: Optional[str] = None  # 结束时间【创建时间】，格式：Y-m-d，双闭区间
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15，上限200


class MultiPlatformV2QueryShippingListV2Request(LingXingModel):
    """Request for 查询平台仓发货单列表v2.
    
    POST /basicOpen/multiplatform/query/shippingList
    """
    platformCodes: List  # 平台代码 Walmart 10008 TikTok 10011 Temu 10022 Shein 10027
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度
    timeField: Optional[int] = None  # 时间维度 1 创建时间 2 发货时间 3 开船时间 4 预计到港时间 5 实际妥投时间 6 实际发货时间
    startTime: Optional[str] = None  # 开始时间
    endTime: Optional[str] = None  # 结束时间
    pickingStatus: Optional[str] = None  # 拣货状态 1 已拣货 0 待拣货
    shippingListStatus: Optional[int] = None  # 发货单状态 0 待配货 1 待发货 2 已发货 3 已作废
    searchField: Optional[int] = None  # 搜索维度 1 MSKU 2 发货单号 7 货件单号 8 商品条码
    searchSingleValue: Optional[str] = None  # 模糊搜索值
    storeIds: Optional[list] = None  # 店铺id列表，对应查询多平台店铺信息接口对应字段【store_id】
    updateStartTime: Optional[str] = None  # 修改开始时间
    updateEndTime: Optional[str] = None  # 修改结束时间
    isDelete: Optional[int] = None  # 是否删除 0 未删除（默认） 1 已删除


class MultiPlatformV2ModifyPlatformRemarkRequest(LingXingModel):
    """Request for 修改平台仓发货单备注.
    
    POST /cepf/warehouse/api/openApi/editPlatfromShippingRemark
    """
    remarkContent: str  # 备注内容
    shippingListCode: str  # 平台单号


class MultiPlatformV2QueryWFSCargoPageRequest(LingXingModel):
    """Request for 查询WFS货件列表.
    
    POST /cepf/warehouse/api/openApi/queryWFSCargoPage
    """
    store_id: Optional[list] = None  # 店铺id
    cargo_status_list: Optional[list] = None  # 货件平台状态： 0 PENDING_SHIPMENT_DETAILS 1 AWAITING_DELIVERY 2 RECEIVING_IN_PROGRESS 3 CLOSED 4 CANCELLED
    inbound_order_id: Optional[str] = None  # 入库订单编号
    start_time: Optional[str] = None  # 开始时间【创建时间】，格式：Y-m-d，双闭区间
    end_time: Optional[str] = None  # 结束时间【创建时间】，格式：Y-m-d，双闭区间
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15，上限200
    update_time_ge: Optional[str] = None  # 货件更新开始时间，格式：yyyy-MM-dd HH:mm:SS
    update_time_le: Optional[str] = None  # 货件更新结束时间，格式：yyyy-MM-dd HH:mm:SS
    cargo_update_time_ge: Optional[str] = None  # 货件平台更新时间开始 格式:yyyy-MM-dd HH:mm:ss
    cargo_update_time_le: Optional[str] = None  # 货件平台更新时间结束 格式:yyyy-MM-dd HH:mm:ss


class MultiPlatformV2QueryWFSInventionPageRequest(LingXingModel):
    """Request for 查询WFS库存列表.
    
    POST /cepf/warehouse/api/openApi/queryWFSInventionPage
    """
    store_id: List  # 店铺id
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认15，上限200


class MultiPlatformV2FbtStockSearchRequest(LingXingModel):
    """Request for 查询Temu库存.
    
    POST /basicOpen/multiplatform/fbt/stockSearch
    """
    length: Optional[int] = None  # 每页条数
    offset: Optional[int] = None  # 偏移量
    storeIdList: List  # 店铺Id集合


class MultiPlatformV2TemuCargoRequest(LingXingModel):
    """Request for 查询Temu货件.
    
    POST /basicOpen/multiplatform/temu/cargo
    """
    endTime: str  # yyyy-MM-dd
    length: Optional[int] = None  # 每页条数
    offset: Optional[int] = None  # 偏移量
    startTime: str  # yyyy-MM-dd
    statusList: List  # 待发货：0 ；待收货：1 ；已收货：2 ；已入库：3 ；已退货：4 ；已取消：5 ；部分收货：6 ;待申报（本地状态）7
    timeType: int  # 1:创建时间  2：发货时间 3：收货时间  4：入库时间


class MultiPlatformV2FullListRequestCustomItem(LingXingModel):
    likeContent: Optional[str] = None  # 搜索内容
    type: Optional[int] = None  # 搜索类型，枚举值：0-货品标题, 1-商品参考编码, 2-货品id

class MultiPlatformV2FullListRequest(LingXingModel):
    """Request for 查询FULL库存.
    
    POST /basicOpen/multiplatform/full/stockSearch
    """
    length: Optional[int] = None  # 每页条数，必填，最大200条
    offset: Optional[int] = None  # 分页偏移量，必填，从0开始
    selectTypeEnum: Optional[str] = None  # 数据维度，COUNT_TYPE-数量 PRICE_TYPE-成本（必填）
    hideZeroStorage: Optional[int] = None  # 是否隐藏0库存，0不隐藏，1隐藏
    storeIdList: Optional[list] = None  # 店铺ID列表
    custom: Optional[MultiPlatformV2FullListRequestCustomItem] = None


class MultiPlatformV2CoupangStockListRequest(LingXingModel):
    """Request for 多平台-查询Coupang库存.
    
    POST /basicOpen/multiplatform/coupang/stockSearch
    """
    length: Optional[int] = None  # 每页条数，必填
    offset: Optional[int] = None  # 偏移量，必填
    storeIds: Optional[list] = None  # 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】


class MultiPlatformV2FbsStockListRequest(LingXingModel):
    """Request for 多平台-查询FBS库存.
    
    POST /basicOpen/multiplatform/fbs/stockSearch
    """
    length: Optional[int] = None  # 每页条数，必填，最大200
    offset: Optional[int] = None  # 偏移量，必填
    storeIds: Optional[list] = None  # 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】
    hideZeroStorage: Optional[int] = None  # 是否隐藏0库存，默认0，枚举值：0-不隐藏，1-隐藏
    whsIdList: Optional[list] = None  # 仓库ID列表


class MultiPlatformV2FbtStockListRequest(LingXingModel):
    """Request for 多平台-查询FBT库存.
    
    POST /basicOpen/multiplatform/fbt/stockSearch/v2
    """
    length: Optional[int] = None  # 每页条数，必填，最大200
    offset: Optional[int] = None  # 偏移量，必填，最小0
    storeIds: Optional[list] = None  # 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】


class MultiPlatformV2WayfairStockListRequest(LingXingModel):
    """Request for 多平台-查询wayfair库存.
    
    POST /basicOpen/multiplatform/wayfair/stockSearch
    """
    length: Optional[int] = None  # 每页条数，必填，最大200
    offset: Optional[int] = None  # 偏移量，必填，表示从第几条开始，最小为0
    storeIds: Optional[list] = None  # 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】
    warehouseIds: Optional[list] = None  # 仓库ID列表


class MultiPlatformV2AddressreturnaddresslistRequest(LingXingModel):
    """Request for 查询退件地址列表.
    
    POST /basicOpen/multiplatform/address/returnAddressList
    """
    store_id: str  # 店铺id


class MultiPlatformV2AddcargogoodslistRequest(LingXingModel):
    """Request for 查询WFS货件可添加商品列表.
    
    POST /basicOpen/multiplatform/cargo/addCargoGoods/list
    """
    store_id: str  # 店铺id
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class MultiPlatformV2MultiplatformcargostorageRequestCargoGoodsListItem(LingXingModel):
    box_num: str  # 箱子数量
    single_box_num: str  # 单箱商品数量
    declare_num: str  # 货件初始申报量
    expected_arrival_time: str  # 预估到货时间
    msku: str  # MSKU，查询添加商品列表接口对应的字段【msku】
    picture_url: str  # 图片地址，查询添加商品列表接口对应的字段【picture_url】
    product_desc: str  # 商品描述
    product_id: str  # 商品id，查询添加商品列表接口对应的字段【item_id】
    product_name: str  # 商品名字，查询添加商品列表接口对应的字段【local_name】
    sku: str  # SKU，查询添加商品列表接口对应的字段【local_sku】
    product_type: str  # 商品类型：  GTIN GTIN  UPC UPC   EAN EAN
    gtin: str  # GTIN，查询添加商品列表接口对应的字段【gtin】
    value_added_service: str  # 增值服务类型：  1 需要 0 不需要

class MultiPlatformV2MultiplatformcargostorageRequestReturnAddressItem(LingXingModel):
    address_alias: str  # 地址别名
    address_id: str  # 地址id
    city: str  # 城市
    mobile: str  # 电话
    postal_code: str  # 邮政编码
    province: str  # 州/省/地区
    receive_or_delivery_country: str  # 发货方/收货方所属国家(或地区)编码
    receive_or_delivery_country_name: str  # 发货方/收货方所属国家(或地区)名称
    street_detail: str  # 街道详细地址

class MultiPlatformV2MultiplatformcargostorageRequest(LingXingModel):
    """Request for WFS货件暂存.
    
    POST /basicOpen/multiplatform/cargo/storage
    """
    store_id: str  # 店铺id
    cargo_remark: Optional[str] = None  # 货件备注
    inbound_order_id: Optional[str] = None  # 入库订单id
    cargo_goods_list: List[MultiPlatformV2MultiplatformcargostorageRequestCargoGoodsListItem]
    return_address: MultiPlatformV2MultiplatformcargostorageRequestReturnAddressItem


class MultiPlatformV2DeleteCargoStorageRequest(LingXingModel):
    """Request for 删除暂存货件.
    
    POST /basicOpen/multiplatform/deleteCargoStorage
    """
    id: str  # WFS货件id，查询WFS货件列表 接口对应字段【id】


class MultiPlatformV2ShopifyVariantListRequest(LingXingModel):
    """Request for 查询Shopify在线商品.
    
    POST /basicOpen/multiplatform/shopify/variantList
    """
    store_ids: Optional[list] = None  # 店铺Id
    status: Optional[list] = None  # 状态 1、Active 2、Draft 3、Archived 4、Deleted
    inventory_policy: Optional[list] = None  # 库存策略 1、不跟踪库存 2、缺货停止销售 3、缺货继续销售
    type_id: Optional[list] = None  # 分类Id
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限1000
    search_field: Optional[int] = None  # 搜索维度
    search_single_value: Optional[str] = None  # 模糊搜索值
    search_values: Optional[list] = None  # 精确搜索列表，上限200个
    quantity: Optional[str] = None  # 库存数量
    quantity_condition: Optional[int] = None  # 库存数量大于或小于 1、大于 2、小于
    price: Optional[int] = None  # 售价
    price_condition: Optional[int] = None  # 售价大于或小于 1、大于 2、小于
    listing_time_field: Optional[int] = None  # 时间维度
    listing_start_time: Optional[str] = None  # 开始时间
    listing_end_time: Optional[str] = None  # 结束时间


class MultiPlatformV2SheinListRequest(LingXingModel):
    """Request for 查询Shein在线商品.
    
    POST /basicOpen/multiplatform/shein/list
    """
    brandIds: Optional[list] = None  # 品牌ID列表
    categoryIds: Optional[list] = None  # 分类ID列表
    offset: Optional[int] = None  # 偏移量
    length: Optional[int] = None  # 分页长度，上限1000
    pairingStatus: Optional[int] = None  # 配对状态 0、未配对 1、已配对
    searchField: Optional[str] = None  # 搜索字段 1、标题 2、品名 3、SPU货号 4、SKC货号 5、平台SPU 6、平台SKC 7、MSKU ID 8、SKU 9、MSKU
    status: Optional[int] = None  # 状态 0、删除 1、在售 2、停售
    storeIds: Optional[list] = None  # 店铺ID列表
    searchSingleValue: Optional[str] = None  # 单一值搜索
    searchValues: Optional[list] = None  # 精确搜索值列表


class MultiPlatformV2TikTokListRequest(LingXingModel):
    """Request for 查询TikTok在线商品.
    
    POST /basicOpen/multiplatform/tiktok/list
    """
    brandIds: Optional[list] = None  # 品牌id列表
    categoryIds: Optional[list] = None  # 分类id列表
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限1000
    pairingStatus: Optional[int] = None  # 配对状态
    searchField: Optional[str] = None  # 搜索维度 1、标题 2、品名 5、平台SPU 7、MSKU ID 8、SKU 9、MSKU 10、SPU货号
    platformStatus: Optional[list] = None  # 状态 DRAFT PENDING FAILED ACTIVATE SELLER_DEACTIVATED PLATFORM_DEACTIVATED FREEZE DELETED
    storeIds: Optional[list] = None  # 店铺id列表
    searchSingleValue: Optional[str] = None  # 搜索值
    searchValues: Optional[list] = None  # 搜索值列表


class MultiPlatformV2TemuListRequest(LingXingModel):
    """Request for 查询Temu在线商品.
    
    POST /basicOpen/multiplatform/temu/list
    """
    brandIds: Optional[list] = None  # 品牌id列表
    categoryIds: Optional[list] = None  # 分类id列表
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限1000
    pairingStatus: Optional[int] = None  # 配对状态 0、未配对 1、已配对
    searchField: str  # 搜索维度 1、标题 2、品名 4、SKC货号 5、平台SPU 6、平台SKC 7、MSKU ID 8、SKU 9、MSKU
    status: Optional[int] = None  # 状态 0、删除 2、正常
    storeIds: Optional[list] = None  # 店铺id列表
    searchValues: Optional[list] = None  # 精确搜索值列表
    searchSingleValue: Optional[str] = None  # 模糊搜索值


class MultiPlatformV2LineListRequest(LingXingModel):
    """Request for 多平台-查询Line在线商品.
    
    POST /basicOpen/multiplatform/line/list
    """
    isParent: Optional[int] = None  # 是否父体，枚举值：1-父体, 0-子体
    availableNumber: Optional[str] = None  # 可用库存数，用于库存筛选
    availableNumberCondition: Optional[int] = None  # 库存筛选条件，枚举值：1-大于, 2-小于
    brandIds: Optional[list] = None  # 品牌ID列表
    categoryIds: Optional[list] = None  # 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来
    length: Optional[int] = None  # 分页长度，每页条数，最大200
    offset: Optional[int] = None  # 分页偏移量，从0开始
    pairingStatus: Optional[int] = None  # 配对状态，枚举值：0-未配对, 1-配对, null-全部
    parentUniqueIds: Optional[list] = None  # 父体全局唯一ID列表
    price: Optional[str] = None  # 金额，用于价格筛选
    priceCondition: Optional[int] = None  # 金额筛选条件，枚举值：1-大于, 2-小于
    principalUids: Optional[list] = None  # 商品负责人UID列表
    productUniqueId: Optional[int] = None  # 商品全局唯一ID
    searchField: Optional[str] = None  # 搜索类型，枚举值：1-msku, 2-msku ID, 3-SKU, 4-品名
    searchSingleValue: Optional[str] = None  # 搜索值，单个模糊搜索，字符串类型
    searchValues: Optional[list] = None  # 搜索值，数组类型，多个精确搜索
    sortField: Optional[str] = None  # 排序字段，直接传返参的字段名
    sortType: Optional[str] = None  # 排序类型，枚举值：asc-升序, desc-降序
    statusList: Optional[list] = None  # 状态列表，枚举值：0-正常, 1-已删除
    storeIds: Optional[list] = None  # 店铺ID列表


class MultiPlatformV2EbaylistRequest(LingXingModel):
    """Request for 查询eBay在线商品列表.
    
    POST /basicOpen/multiplatform/ebay/list
    """
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，默认20，最大上限200
    store_ids: Optional[list] = None  # 店铺id
    site_code: Optional[list] = None  # 站点code
    listing_status: Optional[list] = None  # 销售状态
    auto_restocks: Optional[list] = None  # 是否自动补货： 0 无补货规则 1 启用 2 停用
    listing_type: Optional[list] = None  # 销售类型： 1 拍卖 2 固价 3 多属性
    search_field: Optional[int] = None  # 查询字段类型： 1 msku 2 商品ID 3 sku 4 标题 5 品名 6 walmart gtin码
    search_single_value: Optional[str] = None  # 搜索值(字符串,单个模糊搜索)
    listing_time_field: Optional[int] = None  # 查询时间类型： 1 创建时间 2 结束时间
    listing_start_time: Optional[str] = None  # 开始时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】
    listing_end_time: Optional[str] = None  # 结束时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】


class MultiPlatformV2WalmartlistRequest(LingXingModel):
    """Request for 查询Walmart在线商品.
    
    POST /basicOpen/multiplatform/walmart/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    store_ids: Optional[list] = None  # 店铺id
    status: Optional[list] = None  # 状态： 0 PUBLISHED 1 READY TO PUBLISH 2 IN PROGRESS 3 UNPUBLISHED 4 STAGE 5 SYSTEM PROBLEM
    fulfillment_types: Optional[list] = None  # 发货方式： 0 WFS Eligible 1 Walmart Fulfilled 2 Seller Fulfilled
    listing_time_field: Optional[int] = None  # 搜索时间类型： 1 创建时间 2 更新时间
    listing_start_time: Optional[str] = None  # 开始日期，Y-m-d，闭区间【开始结束时间不超过31天】
    listing_end_time: Optional[str] = None  # 结束日期，Y-m-d，闭区间【开始结束时间不超过31天】
    search_field: Optional[int] = None  # 搜索字段类型： 1 MSKU 2 商品ID 3 SKU 4 标题
    search_single_value: Optional[str] = None  # 搜索值(字符串,单个模糊搜索)


class MultiPlatformV2AliexpresslistRequest(LingXingModel):
    """Request for 查询AliExpress在线商品 - 自运营.
    
    POST /basicOpen/multiplatform/aliExpress/list
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    store_ids: Optional[list] = None  # 店铺id
    status: Optional[list] = None  # 状态： 1 正在销售 2 已下架 3 审核中 4 审核不通过
    listing_time_field: Optional[int] = None  # 查询时间类型： 1 创建时间 2 结束时间
    listing_start_time: Optional[str] = None  # 开始日期，Y-m-d，闭区间【开始结束时间不超过31天】
    listing_end_time: Optional[str] = None  # 结束日期，Y-m-d，闭区间【开始结束时间不超过31天】
    search_field: Optional[int] = None  # 搜索字段类型： 1 MSKU 2 商品ID 3 SKU 4 标题
    search_single_value: Optional[str] = None  # 搜索值(字符串,单个模糊搜索）


class MultiPlatformV2AliexpressListV2Request(LingXingModel):
    """Request for 查询AliExpress在线商品 - 托管模式.
    
    POST /basicOpen/multiplatform/aliexpress/list/v2
    """
    isParent: Optional[int] = None  # 是否父体，必填，枚举值：1-父体, 0-子体
    length: Optional[int] = None  # 分页长度，必填，每页条数
    brandIds: Optional[list] = None  # 品牌ID列表
    categoryIds: Optional[list] = None  # 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来
    end: Optional[str] = None  # 结束时间，格式：yyyy-MM-dd
    offset: Optional[int] = None  # 分页偏移量，必填，从0开始
    pairingStatus: Optional[int] = None  # 配对状态，枚举值：0-未配对, 1-配对, null-全部
    platformCodeList: Optional[list] = None  # 平台编码列表
    price: Optional[int] = None  # 供货价金额
    priceCondition: Optional[int] = None  # 供货价金额筛选条件，枚举值：1-大于, 2-小于
    principalUids: Optional[list] = None  # 商品负责人UID列表
    productTypeList: Optional[list] = None  # 发货模式列表，枚举值：0-仓发, 1-JIT, 2-海外备仓
    productUniqueId: Optional[int] = None  # 商品全局唯一ID
    productUniqueIdList: Optional[list] = None  # 父体唯一ID列表
    quantity: Optional[int] = None  # 库存数
    quantityCondition: Optional[int] = None  # 库存筛选条件，枚举值：1-大于, 2-小于
    searchField: Optional[int] = None  # 搜索类型，枚举值：1-msku, 2-商品ID, 3-SKU, 4-品名, 5-SKU, 6-品名, 7-标题
    searchSingleValue: Optional[str] = None  # 搜索值，单个模糊搜索
    searchValues: Optional[list] = None  # 搜索值，数组，多个精确搜索
    sortField: Optional[str] = None  # 排序字段，直接传返参的字段名
    sortType: Optional[str] = None  # 排序类型，枚举值：asc-升序, desc-降序
    start: Optional[str] = None  # 开始时间，格式：yyyy-MM-dd
    statusList: Optional[list] = None  # 状态列表，枚举值：S1-待售, S2-可售
    storeIds: Optional[list] = None  # 店铺ID列表
    storeType: Optional[int] = None  # 店铺类型，枚举值：半托管, 全托管, 海外托管


class MultiPlatformV2BatchTemuAddressDecryptRequest(LingXingModel):
    """Request for 批量TEMU地址解密.
    
    POST /basicOpen/temu/temuAddressDecrypt
    """
    decryptSnList: List  # 系统单号数组


class MultiPlatformV2ShippingorderallocateRequest(LingXingModel):
    """Request for 平台仓发货单分配库存.
    
    POST /basicOpen/multiplatform/allocate/stock
    """
    shippingIdList: Optional[list] = None  # 发货单ID列表，对应查询平台仓发货单列表v2接口出参id


class MultiPlatformV2ShippingorderpickingRequest(LingXingModel):
    """Request for 平台仓发货单拣货.
    
    POST /basicOpen/multiplatform/shippingList/picking
    """
    shippingIdList: Optional[list] = None  # 发货单ID列表，对应查询平台仓发货单列表v2接口出参id


class MultiPlatformV2ShippingorderdeliveryRequest(LingXingModel):
    """Request for 平台仓发货单发货.
    
    POST /basicOpen/multiplatform/shippingList/delivery
    """
    shippingIdList: Optional[list] = None  # 发货单ID列表，对应查询平台仓发货单列表v2接口出参id


class MultiPlatformWalmartCommentListRequest(LingXingModel):
    """Request for 查询Walmart Review列表.
    
    POST /basicOpen/multiplatform/walmart/queryCommentList
    """
    endDate: str  # 结束日期
    pageNum: Optional[int] = None  # 页码
    pageSize: Optional[int] = None  # 每页大小
    ratings: Optional[list] = None  # 评分列表
    searchDateField: Optional[str] = None  # 搜索日期字段
    searchField: Optional[str] = None  # 搜索字段
    searchValue: Optional[list] = None  # 搜索值列表
    startDate: str  # 开始日期
    storeIds: Optional[list] = None  # 店铺ID列表


class MultiPlatformV2NewplatformorderlistRequest(LingXingModel):
    """Request for 查询平台订单列表.
    
    POST /cepfPlatformOrder/open-api/newPlatformOrder/list
    """
    dateType: int  # 时间类型 0.平台数据变动时间 1.订购时间 2.订购时间-北京 3.支付时间 4.支付时间-北京 5.发货时间 6.发货时间-北京
    deliveryTypeList: Optional[list] = None  # 发货类型: 0-自发货 1-平台发货 2-部分自发货
    pageNum: Optional[int] = None  # 查询起始位置
    pageSize: Optional[int] = None  # 分页大小
    platformCodeList: Optional[list] = None  # 平台CODE，目前仅支持 TikTok、TEMU 半托管、Line Shopping、Lazada、Shopee、Shopify、Walmart、Wayfair 平台
    searchMultiValue: Optional[list] = None  # 多个精确搜索查询值
    searchSingleValue: Optional[str] = None  # 单个模糊搜索查询值
    searchType: Optional[int] = None  # 搜索查询类型：1：sku，2：品名，3：msku 4.商品id 5.平台单号 6.参考号 7.商品标题
    siteCodeList: Optional[list] = None  # 站点列表
    sortField: Optional[str] = None  # 排序字段列表字段支持：purchaseTime，paymentTime，platformOrderModifiedTime,deliveryTime
    sortType: Optional[str] = None  # 升降序 asc desc
    startDate: str  # 开始时间，闭区间 格式：2025-10-22 00:00:01
    endDate: str  # 结束时间，闭区间  格式：2025-10-22 20:00:01
    statusList: Optional[list] = None  # 平台单状态的编码  平台订单状态枚举
    storeIdList: Optional[list] = None  # 店铺唯一标识


class MultiPlatformV2ShippingdetailbycodeRequest(LingXingModel):
    """Request for 查询平台仓发货单详情.
    
    POST /basicOpen/multiplatform/query/shippingDetail
    """
    shippingListCode: str  # 发货单编号


class MultiPlatformV2TemustockorderquerypageRequest(LingXingModel):
    """Request for 查询Temu平台仓备货单列表.
    
    POST /basicOpen/stockOrder/temu/queryPage
    """
    length: float  # 每页条数，最小 20，最大 500
    offset: float  # 分页偏移量，最小 0
    current: Optional[float] = None  # 当前页码
    storeIdList: Optional[list] = None  # 店铺 ID 列表，可多选
    statusList: Optional[list] = None  # 备货单时效状态列表。 0 发货即将逾期 1 发货已逾期 2 到货即将逾期 3 到货已逾期
    bizStatusList: Optional[list] = None  # 单据状态列表。 0 待接单 1 待发货 2 已送货 3 已收货 5 质检全部退回 6 已验收 7 已入库 8 已作废 9 已超时
    settlementType: Optional[float] = None  # VMI 单标识。 0 非 VMI(采购) 1 VMI(备货)
    urgencyType: Optional[float] = None  # 紧急备货单标识。 0 否 1 是
    timeType: Optional[float] = None  # 日期类型。 0 下单时间 1 发货时间 2 收货时间 3 最晚发货时间 4 最晚到货时间
    startTime: Optional[str] = None  # 开始日期，格式 `yyyy-MM-dd`
    endTime: Optional[str] = None  # 结束日期，格式 `yyyy-MM-dd`
    searchType: Optional[float] = None  # 搜索类型。 0 备货单号 1 货件号 2 SKC 3 MSKU 4 SPU 5 SKU 6 品名 7 备注 8 MSKU_CODE。当传入 `searchValueList` 时，`searchTyp
    fuzzySearchValue: Optional[str] = None  # 模糊搜索值，多个值时以下游要求的换行符拼接
    searchValueList: Optional[list] = None  # 批量搜索值列表。传入后系统会自动以换行符拼接。当传入 `searchValueList` 时，`searchType` 必传。
    receivingWarehouseList: Optional[list] = None  # 收货仓库列表
    joinPlatformStatus: Optional[float] = None  # 发货台状态。 0 不可加入发货台 1 已加入发货台 2 可以加入发货台
    isGenerateCargo: Optional[float] = None  # 是否已经生成货件。 0 未生成 1 已生成
    isJitOrder: Optional[float] = None  # 是否 JIT 订单。 0 否 1 是
    isFirst: Optional[bool] = None  # 是否首单
    ids: Optional[list] = None  # ID 列表筛选

"""多平台广告 API endpoints."""

from __future__ import annotations

from typing import Any, TypedDict

from ..models.responses.multi_platform import (
    AudienceReportListResponse,
    CampaignReportList2Response,
    CampaignReportListResponse,
    ItemReportListResponse,
    KeywordReportListResponse,
    LazadaadCampaignInfoResponse,
    LazadaadItemInfoResponse,
    LazadaadSellerInfoResponse,
    MultiplatformAdsQueryadgroupsvlistResponse,
    MultiplatformAdsQueryadvertiserlistResponse,
    MultiplatformAdsQuerycampaignsplistResponse,
    MultiplatformAdsQuerycommonadvertiserlistResponse,
    MultiplatformAdsQuerygmvadvertiserreportlistResponse,
    MultiplatformAdsQuerygmvcampaignreportlistResponse,
    MultiplatformAdsQuerygmvitemgroupreportlistResponse,
    MultiplatformAdsQuerygmvstorelistResponse,
    MultiplatformAdsQuerygroupsplistResponse,
    MultiplatformAdsQuerypagetypesplistResponse,
    MultiplatformAdsQueryreportpagetypesvlistResponse,
    MultiplatformAdsQuerytiktokadgrouplistResponse,
    MultiplatformAdsQuerytiktokadlistResponse,
    MultiplatformAdsQuerytiktokcampaignlistResponse,
    MultiplatformAdsReportadgroupsblistResponse,
    MultiplatformAdsReportaditemsblistResponse,
    MultiplatformAdsReportaditemsplistResponse,
    MultiplatformAdsReportaditemsvlistResponse,
    MultiplatformAdsReportcampaignsblistResponse,
    MultiplatformAdsReportcampaignsvlistResponse,
    MultiplatformAdsReportkeywordsblistResponse,
    MultiplatformAdsReportkeywordsplistResponse,
    MultiplatformAdsReportkeywordsvlistResponse,
    MultiplatformAdsReportpagetypesblistResponse,
    MultiplatformAdsReportplatformsblistResponse,
    MultiplatformAdsReportplatformsplistResponse,
    MultiplatformAdsReportplatformsvlistResponse,
    MultiplatformAdsReportsearchtrendslistResponse,
    StoreReportList2Response,
    StoreReportListResponse,
)
from ._base import BaseEndpoint


class ReportPageReq(TypedDict, total=False):
    """广告报表分页参数（page/length/orderField/orderType，字段源自 OpenAPI 请求模型）."""

    page: float
    length: float
    orderField: str
    orderType: str


class ReportPeriodReq(TypedDict, total=False):
    """广告报表时间范围（startDate/endDate，格式 yyyy-MM-dd）."""

    startDate: str
    endDate: str


class ReportFilterReq(TypedDict, total=False):
    """广告报表筛选条件（各平台通用字段并集，均为可选）."""

    shopIds: list
    campaignIds: list
    campaignName: str
    statusCodes: list
    placementCategories: list
    itemIds: list
    isSyncList: list


class MultiplatformAdsEndpoints(BaseEndpoint):
    """领星多平台广告 API (38个接口)."""

    async def lazada_audience_report_list(
        self,
        page: ReportPageReq | None = None,
        comparison: dict[str, Any] | None = None,
        period: ReportPeriodReq | None = None,
        config: dict[str, Any] | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[AudienceReportListResponse]:
        """Lazada广告-受众报告.

        POST /basicOpen/lazadaAd/audience/report/list

        Args:
            page: 分页参数 (required), object.
            comparison: 【不参与Openapi转发】对比参数, object.
            period: 报表时间范围 (required), object.
            config: 【不参与Openapi转发】报表配置, object.
            filter: 筛选条件, object."""
        resp = await self._post(
            "/basicOpen/lazadaAd/audience/report/list",
            {
                k: v
                for k, v in {
                    "page": page,
                    "comparison": comparison,
                    "period": period,
                    "config": config,
                    "filter": filter,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, AudienceReportListResponse)

    async def lazada_campaign_info(
        self, storeIds: list = None, campaignName: str = None, page: float = None, length: float = None
    ) -> list[LazadaadCampaignInfoResponse]:
        """Lazada广告-获取广告活动信息.

        POST /basicOpen/lazadaAd/campaign/info

        Args:
            storeIds: 店铺ID列表；为空时按当前用户有权限的店铺查询, array.
            campaignName: 广告活动名称（模糊匹配）, string.
            page: 页码，从1开始, double.
            length: 每页条数, double."""
        resp = await self._post(
            "/basicOpen/lazadaAd/campaign/info",
            {
                k: v
                for k, v in {"storeIds": storeIds, "campaignName": campaignName, "page": page, "length": length}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, LazadaadCampaignInfoResponse)

    async def lazada_campaign_report_list(
        self,
        page: ReportPageReq | None = None,
        comparison: dict[str, Any] | None = None,
        period: ReportPeriodReq | None = None,
        config: dict[str, Any] | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[CampaignReportListResponse]:
        """Lazada广告-广告活动报告.

        POST /basicOpen/lazadaAd/campaign/report/list

        Args:
            page: 分页参数 (required), object.
            comparison: 【不参与Openapi转发】对比参数, object.
            period: 报表时间范围 (required), object.
            config: 【不参与Openapi转发】报表配置, object.
            filter: 筛选条件, object."""
        resp = await self._post(
            "/basicOpen/lazadaAd/campaign/report/list",
            {
                k: v
                for k, v in {
                    "page": page,
                    "comparison": comparison,
                    "period": period,
                    "config": config,
                    "filter": filter,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, CampaignReportListResponse)

    async def lazada_item_info(
        self,
        storeIds: list = None,
        campaignIds: list = None,
        adgroupName: str = None,
        page: float = None,
        length: float = None,
    ) -> list[LazadaadItemInfoResponse]:
        """Lazada广告-获取广告商品信息.

        POST /basicOpen/lazadaAd/item/info

        Args:
            storeIds: 店铺ID列表；为空时按当前用户有权限的店铺查询, array.
            campaignIds: 广告活动ID列表, array.
            adgroupName: 广告商品名称（模糊匹配）, string.
            page: 页码，从1开始, double.
            length: 每页条数, double."""
        resp = await self._post(
            "/basicOpen/lazadaAd/item/info",
            {
                k: v
                for k, v in {
                    "storeIds": storeIds,
                    "campaignIds": campaignIds,
                    "adgroupName": adgroupName,
                    "page": page,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, LazadaadItemInfoResponse)

    async def lazada_item_report_list(
        self,
        page: ReportPageReq | None = None,
        comparison: dict[str, Any] | None = None,
        period: ReportPeriodReq | None = None,
        config: dict[str, Any] | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[ItemReportListResponse]:
        """Lazada广告-广告商品报告.

        POST /basicOpen/lazadaAd/item/report/list

        Args:
            page: 分页参数 (required), object.
            comparison: 【不参与Openapi转发】对比参数, object.
            period: 报表时间范围 (required), object.
            config: 【不参与Openapi转发】报表配置, object.
            filter: 筛选条件, object."""
        resp = await self._post(
            "/basicOpen/lazadaAd/item/report/list",
            {
                k: v
                for k, v in {
                    "page": page,
                    "comparison": comparison,
                    "period": period,
                    "config": config,
                    "filter": filter,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ItemReportListResponse)

    async def lazada_keyword_report_list(
        self,
        page: ReportPageReq | None = None,
        comparison: dict[str, Any] | None = None,
        period: ReportPeriodReq | None = None,
        config: dict[str, Any] | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[KeywordReportListResponse]:
        """Lazada广告-关键词报告.

        POST /basicOpen/lazadaAd/keyword/report/list

        Args:
            page: 分页参数 (required), object.
            comparison: 【不参与Openapi转发】对比参数, object.
            period: 报表时间范围 (required), object.
            config: 【不参与Openapi转发】报表配置, object.
            filter: 筛选条件, object."""
        resp = await self._post(
            "/basicOpen/lazadaAd/keyword/report/list",
            {
                k: v
                for k, v in {
                    "page": page,
                    "comparison": comparison,
                    "period": period,
                    "config": config,
                    "filter": filter,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, KeywordReportListResponse)

    async def lazada_seller_info(self, **kwargs: Any) -> LazadaadSellerInfoResponse | None:
        """Lazada广告-获取店铺信息.

        POST /basicOpen/lazadaAd/seller/info"""
        resp = await self._post("/basicOpen/lazadaAd/seller/info", kwargs if kwargs else None)
        return self._parse_one(resp.data, LazadaadSellerInfoResponse)

    async def lazada_store_report_list(
        self,
        page: ReportPageReq | None = None,
        comparison: dict[str, Any] | None = None,
        period: ReportPeriodReq | None = None,
        config: dict[str, Any] | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[StoreReportListResponse]:
        """Lazada广告-店铺报告.

        POST /basicOpen/lazadaAd/store/report/list

        Args:
            page: 分页参数 (required), object.
            comparison: 【不参与Openapi转发】对比参数, object.
            period: 报表时间范围 (required), object.
            config: 【不参与Openapi转发】报表配置, object.
            filter: 筛选条件, object."""
        resp = await self._post(
            "/basicOpen/lazadaAd/store/report/list",
            {
                k: v
                for k, v in {
                    "page": page,
                    "comparison": comparison,
                    "period": period,
                    "config": config,
                    "filter": filter,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, StoreReportListResponse)

    async def tiktok_common_advertiser_list(
        self, internalStatus: str = None, hasGmvStore: int = None
    ) -> list[MultiplatformAdsQuerycommonadvertiserlistResponse]:
        """查询TikTok-推广广告-广告帐号.

        POST /basicOpen/multiplatform/ads/queryCommonAdvertiserList

        Args:
            internalStatus: 内部状态，枚举值：ENABLE-启用, DISABLE-禁用, DELETE-删除。用于过滤授权信息表中的状态，不传则返回所有状态的广告账号, string.
            hasGmvStore: 是否有GMV店铺，枚举值：1-只返回有GMV店铺的广告账号，不传或传其他值则不过滤, int."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryCommonAdvertiserList",
            {k: v for k, v in {"internalStatus": internalStatus, "hasGmvStore": hasGmvStore}.items() if v is not None},
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerycommonadvertiserlistResponse)

    async def tiktok_gmv_store_list(self, **kwargs: Any) -> list[MultiplatformAdsQuerygmvstorelistResponse]:
        """查询TikTok-GMV MAX-店铺列表.

        POST /basicOpen/multiplatform/ads/queryGmvStoreList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGmvStoreList", kwargs if kwargs else None)
        return self._parse_list(resp.data, MultiplatformAdsQuerygmvstorelistResponse)

    async def shopee_campaign_report_list(
        self,
        page: ReportPageReq | None = None,
        period: ReportPeriodReq | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[CampaignReportList2Response]:
        """分页查询广告活动报告列表.

        POST /basicOpen/multiplatform/ads/shopee/campaign/report/list

        Args:
            page: 分页参数对象 (required), object.
            period: 时间范围对象 (required), object.
            filter: 筛选条件对象, object."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/shopee/campaign/report/list",
            {k: v for k, v in {"page": page, "period": period, "filter": filter}.items() if v is not None},
        )
        return self._parse_list(resp.data, CampaignReportList2Response)

    async def shopee_store_report_list(
        self,
        page: ReportPageReq | None = None,
        period: ReportPeriodReq | None = None,
        filter: ReportFilterReq | None = None,
    ) -> list[StoreReportList2Response]:
        """分页查询店铺报告列表.

        POST /basicOpen/multiplatform/ads/shopee/store/report/list

        Args:
            page: 分页参数对象 (required), object.
            period: 时间范围对象 (required), object.
            filter: 筛选条件对象, object."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/shopee/store/report/list",
            {k: v for k, v in {"page": page, "period": period, "filter": filter}.items() if v is not None},
        )
        return self._parse_list(resp.data, StoreReportList2Response)

    async def tiktok_ad_group_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        bidStrategies: list = None,
        budgetTypes: list = None,
        campaignIds: list = None,
        currencies: list = None,
        objectiveType: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        searchType: str = None,
        searchValue: list = None,
        serviceStatus: list = None,
        status: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQuerytiktokadgrouplistResponse]:
        """查询TikTok-推广广告-广告组.

        POST /basicOpen/multiplatform/ads/queryTiktokAdGroupList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号Id列表，Long数组, array.
            bidStrategies: 出价策略列表，String数组, array.
            budgetTypes: 预算类型列表，String数组, array.
            campaignIds: 广告活动id列表，Long数组, array.
            currencies: 币种列表，String数组, array.
            objectiveType: 推广目标列表，String数组，枚举值：REACH-覆盖人数, TRAFFIC-访问量, VIDEO_VIEWS-视频播放量, LEAD_GENERATION-线索收集, ENGAGEMENT-社区互动, APP_PROMOTION-应用推广, WEB_CONVERSIONS-网站转化量, PRODUCT_SALES-商品销量, array.
            orderField: 排序字段（驼峰）, string.
            orderType: 排序方式, string.
            ownerBcIds: 广告主BusinessId列表，Long数组, array.
            searchType: 搜索字段，当字段searchValue有值时，该字段也必须有值，且根据报告类型填写对应的值(advertiser_name-广告账号,ad_group_name-广告组,campaign_name推广系列,ad_name-广告), string.
            searchValue: 搜索值，String数组, array.
            serviceStatus: 服务状态列表，String数组, array.
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户, array.
            summaryCurrency: 汇总币种, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryTiktokAdGroupList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "bidStrategies": bidStrategies,
                    "budgetTypes": budgetTypes,
                    "campaignIds": campaignIds,
                    "currencies": currencies,
                    "objectiveType": objectiveType,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "searchType": searchType,
                    "searchValue": searchValue,
                    "serviceStatus": serviceStatus,
                    "status": status,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerytiktokadgrouplistResponse)

    async def tiktok_ad_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        adIds: list = None,
        adStyles: list = None,
        adgroupIds: list = None,
        advertiserIds: list = None,
        bidStrategies: list = None,
        budgetTypes: list = None,
        campaignIds: list = None,
        creativeMaterialTypes: list = None,
        currencies: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        searchType: str = None,
        searchValue: list = None,
        serviceStatus: list = None,
        status: list = None,
        summaryCurrency: str = None,
        videoTypes: list = None,
    ) -> list[MultiplatformAdsQuerytiktokadlistResponse]:
        """查询TikTok-推广广告-广告.

        POST /basicOpen/multiplatform/ads/queryTiktokAdList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            adIds: 广告id列表，Long数组, array.
            adStyles: 广告样式列表，String数组, array.
            adgroupIds: 广告组id列表，String数组, array.
            advertiserIds: 广告账号Id列表，Long数组, array.
            bidStrategies: 出价策略列表，String数组, array.
            budgetTypes: 预算类型列表，String数组, array.
            campaignIds: 推广系列id列表，String数组, array.
            creativeMaterialTypes: 创意素材类型列表，String数组, array.
            currencies: 币种列表，String数组, array.
            orderField: 排序字段（驼峰）, string.
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序, string.
            ownerBcIds: 广告主BusinessId列表，Long数组, array.
            searchType: 搜索字段，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告, string.
            searchValue: 搜索值，String数组, array.
            serviceStatus: 服务状态列表，String数组, array.
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户, array.
            summaryCurrency: 汇总币种, string.
            videoTypes: 视频类型列表，String数组, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryTiktokAdList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "adIds": adIds,
                    "adStyles": adStyles,
                    "adgroupIds": adgroupIds,
                    "advertiserIds": advertiserIds,
                    "bidStrategies": bidStrategies,
                    "budgetTypes": budgetTypes,
                    "campaignIds": campaignIds,
                    "creativeMaterialTypes": creativeMaterialTypes,
                    "currencies": currencies,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "searchType": searchType,
                    "searchValue": searchValue,
                    "serviceStatus": serviceStatus,
                    "status": status,
                    "summaryCurrency": summaryCurrency,
                    "videoTypes": videoTypes,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerytiktokadlistResponse)

    async def tiktok_advertiser_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        advertiserType: list = None,
        bidStrategies: list = None,
        budgetTypes: list = None,
        currencies: list = None,
        displayTimezones: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        searchType: str = None,
        searchValue: list = None,
        serviceStatus: list = None,
        status: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQueryadvertiserlistResponse]:
        """查询TikTok-推广广告-广告帐号.

        POST /basicOpen/multiplatform/ads/queryAdvertiserList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号Id列表，Long数组, array.
            advertiserType: 广告主类型列表，String数组, array.
            bidStrategies: 出价策略列表，String数组, array.
            budgetTypes: 预算类型列表，String数组, array.
            currencies: 币种列表，String数组, array.
            displayTimezones: 地区时区列表，String数组, array.
            orderField: 排序字段（驼峰格式）, string.
            orderType: 排序方式, string.
            ownerBcIds: 广告主BusinessId列表，Long数组, array.
            searchType: 搜索字段，当字段searchValue有值时该字段也必须有值，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告, string.
            searchValue: 搜索值列表, array.
            serviceStatus: 服务状态列表，String数组, array.
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户, array.
            summaryCurrency: 汇总币种, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryAdvertiserList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "advertiserType": advertiserType,
                    "bidStrategies": bidStrategies,
                    "budgetTypes": budgetTypes,
                    "currencies": currencies,
                    "displayTimezones": displayTimezones,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "searchType": searchType,
                    "searchValue": searchValue,
                    "serviceStatus": serviceStatus,
                    "status": status,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQueryadvertiserlistResponse)

    async def tiktok_campaign_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        bidStrategies: list = None,
        budgetTypes: list = None,
        campaignIds: list = None,
        currencies: list = None,
        objectiveType: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        searchType: str = None,
        searchValue: list = None,
        serviceStatus: list = None,
        status: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQuerytiktokcampaignlistResponse]:
        """查询TikTok-推广广告-广告系列.

        POST /basicOpen/multiplatform/ads/queryTiktokCampaignList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号Id列表，Long数组, array.
            bidStrategies: 出价策略列表，String数组, array.
            budgetTypes: 预算类型列表，String数组, array.
            campaignIds: 广告活动id列表，Long数组, array.
            currencies: 币种列表，String数组, array.
            objectiveType: 推广目标列表，String数组，枚举值：REACH-覆盖人数, TRAFFIC-访问量, VIDEO_VIEWS-视频播放量, LEAD_GENERATION-线索收集, ENGAGEMENT-社区互动, APP_PROMOTION-应用推广, WEB_CONVERSIONS-网站转化量, PRODUCT_SALES-商品销量, array.
            orderField: 排序字段（驼峰格式）, string.
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序, string.
            ownerBcIds: 广告主BusinessId列表，Long数组, array.
            searchType: 搜索字段，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告。当字段searchValue有值时，该字段也必须有值, string.
            searchValue: 搜索值，String数组, array.
            serviceStatus: 服务状态列表，String数组, array.
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户, array.
            summaryCurrency: 汇总币种, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryTiktokCampaignList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "bidStrategies": bidStrategies,
                    "budgetTypes": budgetTypes,
                    "campaignIds": campaignIds,
                    "currencies": currencies,
                    "objectiveType": objectiveType,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "searchType": searchType,
                    "searchValue": searchValue,
                    "serviceStatus": serviceStatus,
                    "status": status,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerytiktokcampaignlistResponse)

    async def tiktok_gmv_advertiser_report_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        gmvMaxPromotionTypeCodes: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        status: list = None,
        storeIds: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQuerygmvadvertiserreportlistResponse]:
        """查询TikTok-GMV MAX-广告帐号.

        POST /basicOpen/multiplatform/ads/queryGmvAdvertiserReportList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填，从1开始, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号ID列表，Long数组，用于筛选特定广告账号, array.
            gmvMaxPromotionTypeCodes: GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV, array.
            orderField: 排序字段名称，如：cost, orders, roi, string.
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序, string.
            ownerBcIds: 广告主账号ID列表，Long数组，业务负责人的BC ID列表, array.
            status: 广告账号状态编码列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户, array.
            storeIds: 店铺ID列表，Long数组，用于筛选特定店铺的数据, array.
            summaryCurrency: 汇总币种编码，默认USD，用于统一汇总不同币种的数据, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryGmvAdvertiserReportList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "gmvMaxPromotionTypeCodes": gmvMaxPromotionTypeCodes,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "status": status,
                    "storeIds": storeIds,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerygmvadvertiserreportlistResponse)

    async def tiktok_gmv_campaign_report_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        bidTypeCodes: list = None,
        campaignId: int = None,
        campaignIds: list = None,
        gmvMaxPromotionTypeCodes: list = None,
        itemGroupIds: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        scheduleEndDate: str = None,
        scheduleStartDate: str = None,
        status: list = None,
        storeIds: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQuerygmvcampaignreportlistResponse]:
        """查询TikTok-GMV MAX-推广系列.

        POST /basicOpen/multiplatform/ads/queryGmvCampaignReportList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填，从1开始, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号ID列表，Long数组，用于筛选特定广告账号, array.
            bidTypeCodes: 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量, array.
            campaignId: 推广系列ID，用于筛选单个推广系列, long.
            campaignIds: 推广系列ID列表，Long数组，用于查询多个推广系列, array.
            gmvMaxPromotionTypeCodes: GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV, array.
            itemGroupIds: 广告商品ID列表，Long数组，用于筛选特定商品, array.
            orderField: 排序字段名称，如：cost, orders, roi, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序, string.
            ownerBcIds: 广告主账号ID列表，Long数组，业务负责人的BC ID列表, array.
            scheduleEndDate: 排期结束日期，格式：yyyy-MM-dd, string.
            scheduleStartDate: 排期开始日期，格式：yyyy-MM-dd, string.
            status: 推广系列操作状态编码列表，String数组，枚举值：ENABLE-已开启, DISABLE-已暂停, DELETE-已删除, array.
            storeIds: 店铺ID列表，Long数组，用于筛选特定店铺的数据, array.
            summaryCurrency: 汇总币种编码，用于统一汇总不同币种的数据, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryGmvCampaignReportList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "bidTypeCodes": bidTypeCodes,
                    "campaignId": campaignId,
                    "campaignIds": campaignIds,
                    "gmvMaxPromotionTypeCodes": gmvMaxPromotionTypeCodes,
                    "itemGroupIds": itemGroupIds,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "scheduleEndDate": scheduleEndDate,
                    "scheduleStartDate": scheduleStartDate,
                    "status": status,
                    "storeIds": storeIds,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerygmvcampaignreportlistResponse)

    async def tiktok_gmv_item_group_report_list(
        self,
        endDate: str = None,
        length: int = None,
        page: int = None,
        startDate: str = None,
        advertiserIds: list = None,
        bidTypeCodes: list = None,
        campaignIds: list = None,
        itemGroupIds: list = None,
        orderField: str = None,
        orderType: str = None,
        ownerBcIds: list = None,
        status: list = None,
        storeIds: list = None,
        summaryCurrency: str = None,
    ) -> list[MultiplatformAdsQuerygmvitemgroupreportlistResponse]:
        """查询TikTok-GMV MAX-广告商品.

        POST /basicOpen/multiplatform/ads/queryGmvItemGroupReportList

        Args:
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天, string.
            length: 每页条数，必填，小于2000, int.
            page: 页码，必填, int.
            startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
            advertiserIds: 广告账号ID列表，Long数组, array.
            bidTypeCodes: 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量, array.
            campaignIds: 推广系列ID列表，Long数组, array.
            itemGroupIds: 广告商品ID列表，Long数组, array.
            orderField: 排序字段, string.
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序, string.
            ownerBcIds: 广告主账号ID列表，Long数组, array.
            status: 商品状态编码列表，String数组，枚举值：available-可用, unavailable-不可用, array.
            storeIds: 店铺ID列表，Long数组, array.
            summaryCurrency: 汇总币种编码, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryGmvItemGroupReportList",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "page": page,
                    "startDate": startDate,
                    "advertiserIds": advertiserIds,
                    "bidTypeCodes": bidTypeCodes,
                    "campaignIds": campaignIds,
                    "itemGroupIds": itemGroupIds,
                    "orderField": orderField,
                    "orderType": orderType,
                    "ownerBcIds": ownerBcIds,
                    "status": status,
                    "storeIds": storeIds,
                    "summaryCurrency": summaryCurrency,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerygmvitemgroupreportlistResponse)

    async def walmart_ad_group_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        dateKey: str = None,
        endDate: str = None,
        startDate: str = None,
        campaignIds: list = None,
        companyId: int = None,
        day: int = None,
        operationSourceType: str = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsQueryadgroupsvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 广告组.

        POST /basicOpen/multiplatform/ads/queryAdGroupSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。不传时默认查询所有类型, array.
            dateKey: 天数据聚合维度，枚举值：day-按天, week-按周, month-按月。【仅天维度接口使用】, string.
            endDate: 结束日期，格式: yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，格式: yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组, array.
            companyId: 公司ID, int.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30。默认14天, int.
            operationSourceType: 操作来源，默认网页操作, string.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryAdGroupSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "dateKey": dateKey,
                    "endDate": endDate,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "companyId": companyId,
                    "day": day,
                    "operationSourceType": operationSourceType,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQueryadgroupsvlistResponse)

    async def walmart_campaign_sp_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        day: int = None,
        endDate: str = None,
        operationSourceType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        startDate: str = None,
        campaignIds: list = None,
        orderField: str = None,
        orderType: str = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsQuerycampaignsplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 广告活动.

        POST /basicOpen/multiplatform/ads/queryCampaignSpList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：1.查询sp广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto；2.查询sb广告报告必须且只能携带sba；3.查询sv广告报告必须且只能携带video, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30, int.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            operationSourceType: 操作来源，openapi调用必传gateway，前端传web, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，openapi必传且小于2000, int.
            paging: 是否分页，openapi必填true, boolean.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询, array.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC, string.
            searchText: 搜索文本，模糊搜索广告活动名称, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryCampaignSpList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "day": day,
                    "endDate": endDate,
                    "operationSourceType": operationSourceType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "orderField": orderField,
                    "orderType": orderType,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerycampaignsplistResponse)

    async def walmart_group_sp_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        day: int = None,
        endDate: str = None,
        operationSourceType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        startDate: str = None,
        campaignIds: list = None,
        orderField: str = None,
        orderType: str = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsQuerygroupsplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 广告组.

        POST /basicOpen/multiplatform/ads/queryGroupSpList

        Args:
            advertiserIds: 广告账号ID列表，必填，BigInteger数组，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，必填，String数组，枚举值：sponsoredProducts-manual-SP手动, sponsoredProducts-auto-SP自动, sba-SB品牌广告, video-SV视频广告。注意：1.查询sp广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto；2.查询sb广告报告必须且只能携带sba；3.查询sv广告报告必须且只能携带video, array.
            day: 归因天数，必填，数据归因天数，枚举值：3, 14, 30, int.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            operationSourceType: 操作来源，必填，openapi调用必传gateway，前端传web, string.
            pageNum: 页码，必填，分页时的页码，从1开始, int.
            pageSize: 每页大小，必填，分页时每页显示的记录数，openapi必传且小于2000, int.
            paging: 是否分页，必填，openapi必填true, boolean.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组, array.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC, string.
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name）, string.
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryGroupSpList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "day": day,
                    "endDate": endDate,
                    "operationSourceType": operationSourceType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "orderField": orderField,
                    "orderType": orderType,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerygroupsplistResponse)

    async def walmart_page_type_sp_list(
        self,
        orderType: str = None,
        adDatePicker: list = None,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        pageSize: int = None,
        campaignIds: list = None,
        orderField: str = None,
        day: int = None,
        pageNum: int = None,
        startDate: str = None,
    ) -> list[MultiplatformAdsQuerypagetypesplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 页面类型.

        POST /basicOpen/multiplatform/ads/queryPageTypeSPList

        Args:
            orderType: orderType, string.
            adDatePicker: adDatePicker（日期格式：yyyy-MM-dd）, array.
            advertiserIds: advertiserIds列表, array.
            campaignType: campaignType列表, array.
            endDate: 结束日期，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            pageSize: 每页大小, int.
            campaignIds: campaignIds列表, array.
            orderField: orderField, string.
            day: day, int.
            pageNum: 页码, int.
            startDate: 开始日期，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryPageTypeSPList",
            {
                k: v
                for k, v in {
                    "orderType": orderType,
                    "adDatePicker": adDatePicker,
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "pageSize": pageSize,
                    "campaignIds": campaignIds,
                    "orderField": orderField,
                    "day": day,
                    "pageNum": pageNum,
                    "startDate": startDate,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQuerypagetypesplistResponse)

    async def walmart_report_page_type_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        companyId: int = None,
        day: int = None,
        operationSourceType: str = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        pageType: list = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsQueryreportpagetypesvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 页面类型.

        POST /basicOpen/multiplatform/ads/queryReportPageTypeSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            companyId: 公司ID, int.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            operationSourceType: 操作来源，默认网页操作, string.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            pageType: 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他, array.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/queryReportPageTypeSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "companyId": companyId,
                    "day": day,
                    "operationSourceType": operationSourceType,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "pageType": pageType,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsQueryreportpagetypesvlistResponse)

    async def walmart_report_ad_group_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportadgroupsblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 广告组.

        POST /basicOpen/multiplatform/ads/reportAdGroupSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用，delete-归档, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportAdGroupSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportadgroupsblistResponse)

    async def walmart_report_ad_item_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportaditemsblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 广告.

        POST /basicOpen/multiplatform/ads/reportAdItemSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告名称（ad_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportAdItemSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportaditemsblistResponse)

    async def walmart_report_ad_item_sp_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportaditemsplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 广告.

        POST /basicOpen/multiplatform/ads/reportAdItemSpList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告名称（ad_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportAdItemSpList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportaditemsplistResponse)

    async def walmart_report_ad_item_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportaditemsvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 广告.

        POST /basicOpen/multiplatform/ads/reportAdItemSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告名称（ad_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportAdItemSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportaditemsvlistResponse)

    async def walmart_report_campaign_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        realtime: int = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportcampaignsblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 广告活动.

        POST /basicOpen/multiplatform/ads/reportCampaignSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            realtime: 实时数据标识，0-非实时, 1-实时数据, int.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportCampaignSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "realtime": realtime,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportcampaignsblistResponse)

    async def walmart_report_campaign_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        day: int = None,
        endDate: str = None,
        operationSourceType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        startDate: str = None,
        campaignIds: list = None,
        orderField: str = None,
        orderType: str = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportcampaignsvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 广告活动.

        POST /basicOpen/multiplatform/ads/reportCampaignSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video, array.
            day: 归因天数，必填，数据归因天数，枚举值：3, 14, 30, int.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            operationSourceType: 操作来源，必填，openapi调用必传gateway，前端传web, string.
            pageNum: 页码，必填，分页时的页码，从1开始, int.
            pageSize: 每页大小，必填，openapi必传且小于2000, int.
            paging: 是否分页，必填，openapi必填true, boolean.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            campaignIds: 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询, array.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            searchText: 搜索文本，模糊搜索广告活动名称, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportCampaignSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "day": day,
                    "endDate": endDate,
                    "operationSourceType": operationSourceType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "startDate": startDate,
                    "campaignIds": campaignIds,
                    "orderField": orderField,
                    "orderType": orderType,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportcampaignsvlistResponse)

    async def walmart_report_keyword_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportkeywordsblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 关键词.

        POST /basicOpen/multiplatform/ads/reportKeywordSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text）, string.
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportKeywordSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportkeywordsblistResponse)

    async def walmart_report_keyword_sp_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportkeywordsplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 关键词.

        POST /basicOpen/multiplatform/ads/reportKeywordSpList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text）, string.
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportKeywordSpList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportkeywordsplistResponse)

    async def walmart_report_keyword_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportkeywordsvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 关键词.

        POST /basicOpen/multiplatform/ads/reportKeywordSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text）, string.
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportKeywordSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportkeywordsvlistResponse)

    async def walmart_report_page_type_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        pageType: list = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportpagetypesblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 页面类型.

        POST /basicOpen/multiplatform/ads/reportPageTypeSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            pageType: 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他, array.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportPageTypeSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "pageType": pageType,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportpagetypesblistResponse)

    async def walmart_report_platform_sb_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportplatformsblistResponse]:
        """查询沃尔玛-广告 - SB广告 - 平台.

        POST /basicOpen/multiplatform/ads/reportPlatformSbList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportPlatformSbList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportplatformsblistResponse)

    async def walmart_report_platform_sp_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportplatformsplistResponse]:
        """查询沃尔玛-广告 - SP广告 - 平台.

        POST /basicOpen/multiplatform/ads/reportPlatformSpList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportPlatformSpList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportplatformsplistResponse)

    async def walmart_report_platform_sv_list(
        self,
        advertiserIds: list = None,
        campaignType: list = None,
        endDate: str = None,
        startDate: str = None,
        adGroupIds: list = None,
        campaignIds: list = None,
        day: int = None,
        orderField: str = None,
        orderType: str = None,
        pageNum: int = None,
        pageSize: int = None,
        paging: bool = None,
        searchText: str = None,
        searchType: str = None,
        status: list = None,
    ) -> list[MultiplatformAdsReportplatformsvlistResponse]:
        """查询沃尔玛-广告 - SV广告 - 平台.

        POST /basicOpen/multiplatform/ads/reportPlatformSvList

        Args:
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺, array.
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video, array.
            endDate: 结束日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            startDate: 开始日期，必填，格式：yyyy-MM-dd，且 startDate 和 endDate 间隔不能超过31天, string.
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选, array.
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选, array.
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天, int.
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序, string.
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC, string.
            pageNum: 页码，分页时的页码，从1开始, int.
            pageSize: 每页大小，分页时每页显示的记录数，最大200, int.
            paging: 是否分页，默认为true, boolean.
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name）, string.
            searchType: 搜索类型，目前不用传, string.
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成, array."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportPlatformSvList",
            {
                k: v
                for k, v in {
                    "advertiserIds": advertiserIds,
                    "campaignType": campaignType,
                    "endDate": endDate,
                    "startDate": startDate,
                    "adGroupIds": adGroupIds,
                    "campaignIds": campaignIds,
                    "day": day,
                    "orderField": orderField,
                    "orderType": orderType,
                    "pageNum": pageNum,
                    "pageSize": pageSize,
                    "paging": paging,
                    "searchText": searchText,
                    "searchType": searchType,
                    "status": status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportplatformsvlistResponse)

    async def walmart_report_search_trends_list(
        self,
        reportDate: str = None,
        pageSize: int = None,
        pageNum: int = None,
        orderType: str = None,
        itemBrand: dict = None,
        itemQueryType: int = None,
        itemQueryField: int = None,
        searchKeywordType: int = None,
        orderField: str = None,
        searchKeyword: dict = None,
        itemQueryValue: dict = None,
        itemBrandType: int = None,
    ) -> list[MultiplatformAdsReportsearchtrendslistResponse]:
        """查询沃尔玛-词 - 沃尔玛热门搜索词.

        POST /basicOpen/multiplatform/ads/reportSearchTrendsList

        Args:
            reportDate: 报告日期，必填，格式：yyyy-MM-dd, string.
            pageSize: 每页大小，必填，不能大于100, int.
            pageNum: 页码，必填, int.
            orderType: 排序方向，枚举值：ASC-升序, DESC-降序, string.
            itemBrand: 商品品牌(在item_brand_1/2/3中搜索)，模糊搜索请使用String类型，精确搜索请使用数组类型, object.
            itemQueryType: 字段类型，枚举值：0-模糊搜索, 1-精确搜索, int.
            itemQueryField: 查询字段，枚举值：0-itemId, 1-itemName, int.
            searchKeywordType: 搜索关键词类型，枚举值：0-模糊搜索, 1-精确搜索, int.
            orderField: 排序字段(驼峰格式)，枚举值：searchKeyword-搜索关键词, keywordRank-关键词排名, totalPctClickShare-前3商品点击占比总和, totalPctConvShare-前3商品转化占比总和, string.
            searchKeyword: 搜索关键词，模糊搜索请使用String类型，精确搜索请使用数组类型, object.
            itemQueryValue: 文本框中的值，模糊搜索请使用String类型，精确搜索请使用数组类型, object.
            itemBrandType: 商品品牌类型，枚举值：0-模糊搜索, 1-精确搜索, int."""
        resp = await self._post(
            "/basicOpen/multiplatform/ads/reportSearchTrendsList",
            {
                k: v
                for k, v in {
                    "reportDate": reportDate,
                    "pageSize": pageSize,
                    "pageNum": pageNum,
                    "orderType": orderType,
                    "itemBrand": itemBrand,
                    "itemQueryType": itemQueryType,
                    "itemQueryField": itemQueryField,
                    "searchKeywordType": searchKeywordType,
                    "orderField": orderField,
                    "searchKeyword": searchKeyword,
                    "itemQueryValue": itemQueryValue,
                    "itemBrandType": itemBrandType,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MultiplatformAdsReportsearchtrendslistResponse)

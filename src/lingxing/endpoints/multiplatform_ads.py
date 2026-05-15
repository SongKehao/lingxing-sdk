"""Auto-generated MultiplatformAdsEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class MultiplatformAdsEndpoints:
    """领星API - MultiplatformAdsEndpoints (38个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def lazada_audience_report_list(self, **kwargs) -> dict:
        """LazadaAudienceReportList.
        
        POST /basicOpen/lazadaAd/audience/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/audience/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_campaign_info(self, **kwargs) -> dict:
        """LazadaCampaignInfo.
        
        POST /basicOpen/lazadaAd/campaign/info
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/campaign/info",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_campaign_report_list(self, **kwargs) -> dict:
        """LazadaCampaignReportList.
        
        POST /basicOpen/lazadaAd/campaign/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/campaign/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_item_info(self, **kwargs) -> dict:
        """LazadaItemInfo.
        
        POST /basicOpen/lazadaAd/item/info
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/item/info",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_item_report_list(self, **kwargs) -> dict:
        """LazadaItemReportList.
        
        POST /basicOpen/lazadaAd/item/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/item/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_keyword_report_list(self, **kwargs) -> dict:
        """LazadaKeywordReportList.
        
        POST /basicOpen/lazadaAd/keyword/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/keyword/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_seller_info(self, **kwargs) -> dict:
        """LazadaSellerInfo.
        
        POST /basicOpen/lazadaAd/seller/info
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/seller/info",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_store_report_list(self, **kwargs) -> dict:
        """LazadaStoreReportList.
        
        POST /basicOpen/lazadaAd/store/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/lazadaAd/store/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_common_advertiser_list(self, **kwargs) -> dict:
        """Tiktok-CommonAdvertiserList_4.
        
        POST /basicOpen/multiplatform/ads/queryCommonAdvertiserList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryCommonAdvertiserList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_gmv_store_list(self, **kwargs) -> dict:
        """Tiktok-GmvStoreList_8.
        
        POST /basicOpen/multiplatform/ads/queryGmvStoreList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryGmvStoreList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopee_campaign_report_list(self, **kwargs) -> dict:
        """shopeeCampaignReportList.
        
        POST /basicOpen/multiplatform/ads/shopee/campaign/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/shopee/campaign/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopee_store_report_list(self, **kwargs) -> dict:
        """shopeeStoreReportList.
        
        POST /basicOpen/multiplatform/ads/shopee/store/report/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/shopee/store/report/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_ad_group_list(self, **kwargs) -> dict:
        """tiktok-AdGroupList_12.
        
        POST /basicOpen/multiplatform/ads/queryTiktokAdGroupList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryTiktokAdGroupList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_ad_list(self, **kwargs) -> dict:
        """tiktok-AdList_13.
        
        POST /basicOpen/multiplatform/ads/queryTiktokAdList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryTiktokAdList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_advertiser_list(self, **kwargs) -> dict:
        """tiktok-AdvertiserList_2.
        
        POST /basicOpen/multiplatform/ads/queryAdvertiserList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryAdvertiserList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_campaign_list(self, **kwargs) -> dict:
        """tiktok-CampaignList_14.
        
        POST /basicOpen/multiplatform/ads/queryTiktokCampaignList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryTiktokCampaignList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_gmv_advertiser_report_list(self, **kwargs) -> dict:
        """tiktok-GmvAdvertiserReportList_5.
        
        POST /basicOpen/multiplatform/ads/queryGmvAdvertiserReportList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryGmvAdvertiserReportList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_gmv_campaign_report_list(self, **kwargs) -> dict:
        """tiktok-GmvCampaignReportList_6.
        
        POST /basicOpen/multiplatform/ads/queryGmvCampaignReportList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryGmvCampaignReportList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tiktok_gmv_item_group_report_list(self, **kwargs) -> dict:
        """tiktok-GmvItemGroupReportList_7.
        
        POST /basicOpen/multiplatform/ads/queryGmvItemGroupReportList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryGmvItemGroupReportList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_ad_group_sv_list(self, **kwargs) -> dict:
        """walmart-AdGroupSvList_1.
        
        POST /basicOpen/multiplatform/ads/queryAdGroupSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryAdGroupSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_campaign_sp_list(self, **kwargs) -> dict:
        """walmart-CampaignSpList_3.
        
        POST /basicOpen/multiplatform/ads/queryCampaignSpList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryCampaignSpList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_group_sp_list(self, **kwargs) -> dict:
        """walmart-GroupSpList_9.
        
        POST /basicOpen/multiplatform/ads/queryGroupSpList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryGroupSpList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_page_type_splist(self, **kwargs) -> dict:
        """walmart-PageTypeSPList_10.
        
        POST /basicOpen/multiplatform/ads/queryPageTypeSPList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryPageTypeSPList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_page_type_sv_list(self, **kwargs) -> dict:
        """walmart-ReportPageTypeSvList_11.
        
        POST /basicOpen/multiplatform/ads/queryReportPageTypeSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/queryReportPageTypeSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_ad_group_sb_list(self, **kwargs) -> dict:
        """walmart-reportAdGroupSbList_15.
        
        POST /basicOpen/multiplatform/ads/reportAdGroupSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportAdGroupSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_ad_item_sb_list(self, **kwargs) -> dict:
        """walmart-reportAdItemSbList_16.
        
        POST /basicOpen/multiplatform/ads/reportAdItemSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportAdItemSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_ad_item_sp_list(self, **kwargs) -> dict:
        """walmart-reportAdItemSpList_17.
        
        POST /basicOpen/multiplatform/ads/reportAdItemSpList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportAdItemSpList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_ad_item_sv_list(self, **kwargs) -> dict:
        """walmart-reportAdItemSvList_18.
        
        POST /basicOpen/multiplatform/ads/reportAdItemSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportAdItemSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_campaign_sb_list(self, **kwargs) -> dict:
        """walmart-reportCampaignSbList_19.
        
        POST /basicOpen/multiplatform/ads/reportCampaignSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportCampaignSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_campaign_sv_list(self, **kwargs) -> dict:
        """walmart-reportCampaignSvList_20.
        
        POST /basicOpen/multiplatform/ads/reportCampaignSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportCampaignSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_keyword_sb_list(self, **kwargs) -> dict:
        """walmart-reportKeywordSbList_21.
        
        POST /basicOpen/multiplatform/ads/reportKeywordSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportKeywordSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_keyword_sp_list(self, **kwargs) -> dict:
        """walmart-reportKeywordSpList_22.
        
        POST /basicOpen/multiplatform/ads/reportKeywordSpList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportKeywordSpList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_keyword_sv_list(self, **kwargs) -> dict:
        """walmart-reportKeywordSvList_23.
        
        POST /basicOpen/multiplatform/ads/reportKeywordSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportKeywordSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_page_type_sb_list(self, **kwargs) -> dict:
        """walmart-reportPageTypeSbList_24.
        
        POST /basicOpen/multiplatform/ads/reportPageTypeSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportPageTypeSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_platform_sb_list(self, **kwargs) -> dict:
        """walmart-reportPlatformSbList_25.
        
        POST /basicOpen/multiplatform/ads/reportPlatformSbList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportPlatformSbList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_platform_sp_list(self, **kwargs) -> dict:
        """walmart-reportPlatformSpList_26.
        
        POST /basicOpen/multiplatform/ads/reportPlatformSpList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportPlatformSpList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_platform_sv_list(self, **kwargs) -> dict:
        """walmart-reportPlatformSvList_27.
        
        POST /basicOpen/multiplatform/ads/reportPlatformSvList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportPlatformSvList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_report_search_trends_list(self, **kwargs) -> dict:
        """walmart-reportSearchTrendsList_28.
        
        POST /basicOpen/multiplatform/ads/reportSearchTrendsList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ads/reportSearchTrendsList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

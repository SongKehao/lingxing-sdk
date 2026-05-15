"""多平台广告 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class MultiplatformAdsEndpoints(BaseEndpoint):
    """领星多平台广告 API (38个接口)."""

    async def lazada_audience_report_list(self, **kwargs) -> list | dict:
        """LazadaAudienceReportList. POST /basicOpen/lazadaAd/audience/report/list"""
        resp = await self._post("/basicOpen/lazadaAd/audience/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_campaign_info(self, **kwargs) -> list | dict:
        """LazadaCampaignInfo. POST /basicOpen/lazadaAd/campaign/info"""
        resp = await self._post("/basicOpen/lazadaAd/campaign/info", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_campaign_report_list(self, **kwargs) -> list | dict:
        """LazadaCampaignReportList. POST /basicOpen/lazadaAd/campaign/report/list"""
        resp = await self._post("/basicOpen/lazadaAd/campaign/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_item_info(self, **kwargs) -> list | dict:
        """LazadaItemInfo. POST /basicOpen/lazadaAd/item/info"""
        resp = await self._post("/basicOpen/lazadaAd/item/info", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_item_report_list(self, **kwargs) -> list | dict:
        """LazadaItemReportList. POST /basicOpen/lazadaAd/item/report/list"""
        resp = await self._post("/basicOpen/lazadaAd/item/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_keyword_report_list(self, **kwargs) -> list | dict:
        """LazadaKeywordReportList. POST /basicOpen/lazadaAd/keyword/report/list"""
        resp = await self._post("/basicOpen/lazadaAd/keyword/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_seller_info(self, **kwargs) -> list | dict:
        """LazadaSellerInfo. POST /basicOpen/lazadaAd/seller/info"""
        resp = await self._post("/basicOpen/lazadaAd/seller/info", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_store_report_list(self, **kwargs) -> list | dict:
        """LazadaStoreReportList. POST /basicOpen/lazadaAd/store/report/list"""
        resp = await self._post("/basicOpen/lazadaAd/store/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_common_advertiser_list(self, **kwargs) -> list | dict:
        """Tiktok-CommonAdvertiserList_4. POST /basicOpen/multiplatform/ads/queryCommonAdvertiserList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryCommonAdvertiserList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_gmv_store_list(self, **kwargs) -> list | dict:
        """Tiktok-GmvStoreList_8. POST /basicOpen/multiplatform/ads/queryGmvStoreList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGmvStoreList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_campaign_report_list(self, **kwargs) -> list | dict:
        """shopeeCampaignReportList. POST /basicOpen/multiplatform/ads/shopee/campaign/report/list"""
        resp = await self._post("/basicOpen/multiplatform/ads/shopee/campaign/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_store_report_list(self, **kwargs) -> list | dict:
        """shopeeStoreReportList. POST /basicOpen/multiplatform/ads/shopee/store/report/list"""
        resp = await self._post("/basicOpen/multiplatform/ads/shopee/store/report/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_ad_group_list(self, **kwargs) -> list | dict:
        """tiktok-AdGroupList_12. POST /basicOpen/multiplatform/ads/queryTiktokAdGroupList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryTiktokAdGroupList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_ad_list(self, **kwargs) -> list | dict:
        """tiktok-AdList_13. POST /basicOpen/multiplatform/ads/queryTiktokAdList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryTiktokAdList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_advertiser_list(self, **kwargs) -> list | dict:
        """tiktok-AdvertiserList_2. POST /basicOpen/multiplatform/ads/queryAdvertiserList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryAdvertiserList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_campaign_list(self, **kwargs) -> list | dict:
        """tiktok-CampaignList_14. POST /basicOpen/multiplatform/ads/queryTiktokCampaignList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryTiktokCampaignList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_gmv_advertiser_report_list(self, **kwargs) -> list | dict:
        """tiktok-GmvAdvertiserReportList_5. POST /basicOpen/multiplatform/ads/queryGmvAdvertiserReportList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGmvAdvertiserReportList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_gmv_campaign_report_list(self, **kwargs) -> list | dict:
        """tiktok-GmvCampaignReportList_6. POST /basicOpen/multiplatform/ads/queryGmvCampaignReportList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGmvCampaignReportList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tiktok_gmv_item_group_report_list(self, **kwargs) -> list | dict:
        """tiktok-GmvItemGroupReportList_7. POST /basicOpen/multiplatform/ads/queryGmvItemGroupReportList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGmvItemGroupReportList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_ad_group_sv_list(self, **kwargs) -> list | dict:
        """walmart-AdGroupSvList_1. POST /basicOpen/multiplatform/ads/queryAdGroupSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryAdGroupSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_campaign_sp_list(self, **kwargs) -> list | dict:
        """walmart-CampaignSpList_3. POST /basicOpen/multiplatform/ads/queryCampaignSpList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryCampaignSpList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_group_sp_list(self, **kwargs) -> list | dict:
        """walmart-GroupSpList_9. POST /basicOpen/multiplatform/ads/queryGroupSpList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryGroupSpList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_page_type_sp_list(self, **kwargs) -> list | dict:
        """walmart-PageTypeSPList_10. POST /basicOpen/multiplatform/ads/queryPageTypeSPList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryPageTypeSPList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_page_type_sv_list(self, **kwargs) -> list | dict:
        """walmart-ReportPageTypeSvList_11. POST /basicOpen/multiplatform/ads/queryReportPageTypeSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/queryReportPageTypeSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_ad_group_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportAdGroupSbList_15. POST /basicOpen/multiplatform/ads/reportAdGroupSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportAdGroupSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_ad_item_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportAdItemSbList_16. POST /basicOpen/multiplatform/ads/reportAdItemSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportAdItemSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_ad_item_sp_list(self, **kwargs) -> list | dict:
        """walmart-reportAdItemSpList_17. POST /basicOpen/multiplatform/ads/reportAdItemSpList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportAdItemSpList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_ad_item_sv_list(self, **kwargs) -> list | dict:
        """walmart-reportAdItemSvList_18. POST /basicOpen/multiplatform/ads/reportAdItemSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportAdItemSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_campaign_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportCampaignSbList_19. POST /basicOpen/multiplatform/ads/reportCampaignSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportCampaignSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_campaign_sv_list(self, **kwargs) -> list | dict:
        """walmart-reportCampaignSvList_20. POST /basicOpen/multiplatform/ads/reportCampaignSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportCampaignSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_keyword_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportKeywordSbList_21. POST /basicOpen/multiplatform/ads/reportKeywordSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportKeywordSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_keyword_sp_list(self, **kwargs) -> list | dict:
        """walmart-reportKeywordSpList_22. POST /basicOpen/multiplatform/ads/reportKeywordSpList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportKeywordSpList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_keyword_sv_list(self, **kwargs) -> list | dict:
        """walmart-reportKeywordSvList_23. POST /basicOpen/multiplatform/ads/reportKeywordSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportKeywordSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_page_type_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportPageTypeSbList_24. POST /basicOpen/multiplatform/ads/reportPageTypeSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportPageTypeSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_platform_sb_list(self, **kwargs) -> list | dict:
        """walmart-reportPlatformSbList_25. POST /basicOpen/multiplatform/ads/reportPlatformSbList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportPlatformSbList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_platform_sp_list(self, **kwargs) -> list | dict:
        """walmart-reportPlatformSpList_26. POST /basicOpen/multiplatform/ads/reportPlatformSpList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportPlatformSpList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_platform_sv_list(self, **kwargs) -> list | dict:
        """walmart-reportPlatformSvList_27. POST /basicOpen/multiplatform/ads/reportPlatformSvList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportPlatformSvList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_report_search_trends_list(self, **kwargs) -> list | dict:
        """walmart-reportSearchTrendsList_28. POST /basicOpen/multiplatform/ads/reportSearchTrendsList"""
        resp = await self._post("/basicOpen/multiplatform/ads/reportSearchTrendsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

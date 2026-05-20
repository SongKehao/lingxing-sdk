#!/usr/bin/env python3
"""Script to bind response models to endpoint methods that currently return raw list | dict."""
import re

# ===== Mapping: endpoint method -> (ResponseClass, parse_mode) =====
# parse_mode: "list" -> _parse_list, "one" -> _parse_one

# --- restocking.py -> fba_sug.py ---
RESTOCKING_BINDINGS = {
    "config_asin": ("FbasugAsinGetconfigResponse", "one"),
    "config_msku": ("FbasugMskuGetconfigResponse", "one"),
    "daily_sales_info_feature_asin": ("FbasugAsinGetdailysalesinfofeatureResponse", "one"),
    "daily_sales_info_feature_msku": ("FbasugMskuGetdailysalesinfofeatureResponse", "one"),
    "get_summary_list": ("RestockingAnalysisGetsummarylistResponse", "list"),
    "info_asin": ("FbasugAsinGetinfoResponse", "one"),
    "info_msku": ("FbasugMskuGetinfoResponse", "one"),
    "set_config_asin": ("FbasugAsinGetconfigResponse", "one"),
    "set_config_msku": ("FbasugMskuGetconfigResponse", "one"),
    "set_configs_asin": ("FbasugAsinSetconfigsResponse", "one"),
    "set_configs_msku": ("FbasugMskuSetconfigsResponse", "one"),
    "source_list_asin": ("FbasugAsinGetsourcelistResponse", "one"),
    "source_list_msku": ("FbasugMskuGetsourcelistResponse", "one"),
}

# --- multiplatform_ads.py -> multi_platform.py ---
MP_ADS_BINDINGS = {
    "lazada_audience_report_list": ("AudienceReportListResponse", "list"),
    "lazada_campaign_info": ("LazadaadCampaignInfoResponse", "list"),
    "lazada_campaign_report_list": ("CampaignReportListResponse", "list"),
    "lazada_item_info": ("LazadaadItemInfoResponse", "list"),
    "lazada_item_report_list": ("ItemReportListResponse", "list"),
    "lazada_keyword_report_list": ("KeywordReportListResponse", "list"),
    "lazada_seller_info": ("LazadaadSellerInfoResponse", "one"),
    "lazada_store_report_list": ("StoreReportListResponse", "list"),
    "tiktok_common_advertiser_list": ("MultiplatformAdsQuerycommonadvertiserlistResponse", "list"),
    "tiktok_gmv_store_list": ("MultiplatformAdsQuerygmvstorelistResponse", "list"),
    "shopee_campaign_report_list": ("CampaignReportList2Response", "list"),
    "shopee_store_report_list": ("StoreReportList2Response", "list"),
    "tiktok_ad_group_list": ("MultiplatformAdsQuerytiktokadgrouplistResponse", "list"),
    "tiktok_ad_list": ("MultiplatformAdsQuerytiktokadlistResponse", "list"),
    "tiktok_advertiser_list": ("MultiplatformAdsQueryadvertiserlistResponse", "list"),
    "tiktok_campaign_list": ("MultiplatformAdsQuerytiktokcampaignlistResponse", "list"),
    "tiktok_gmv_advertiser_report_list": ("MultiplatformAdsQuerygmvadvertiserreportlistResponse", "list"),
    "tiktok_gmv_campaign_report_list": ("MultiplatformAdsQuerygmvcampaignreportlistResponse", "list"),
    "tiktok_gmv_item_group_report_list": ("MultiplatformAdsQuerygmvitemgroupreportlistResponse", "list"),
    "walmart_ad_group_sv_list": ("MultiplatformAdsQueryadgroupsvlistResponse", "list"),
    "walmart_campaign_sp_list": ("MultiplatformAdsQuerycampaignsplistResponse", "list"),
    "walmart_group_sp_list": ("MultiplatformAdsQuerygroupsplistResponse", "list"),
    "walmart_page_type_sp_list": ("MultiplatformAdsQuerypagetypesplistResponse", "list"),
    "walmart_report_page_type_sv_list": ("MultiplatformAdsQueryreportpagetypesvlistResponse", "list"),
    "walmart_report_ad_group_sb_list": ("MultiplatformAdsReportadgroupsblistResponse", "list"),
    "walmart_report_ad_item_sb_list": ("MultiplatformAdsReportaditemsblistResponse", "list"),
    "walmart_report_ad_item_sp_list": ("MultiplatformAdsReportaditemsplistResponse", "list"),
    "walmart_report_ad_item_sv_list": ("MultiplatformAdsReportaditemsvlistResponse", "list"),
    "walmart_report_campaign_sb_list": ("MultiplatformAdsReportcampaignsblistResponse", "list"),
    "walmart_report_campaign_sv_list": ("MultiplatformAdsReportcampaignsvlistResponse", "list"),
    "walmart_report_keyword_sb_list": ("MultiplatformAdsReportkeywordsblistResponse", "list"),
    "walmart_report_keyword_sp_list": ("MultiplatformAdsReportkeywordsplistResponse", "list"),
    "walmart_report_keyword_sv_list": ("MultiplatformAdsReportkeywordsvlistResponse", "list"),
    "walmart_report_page_type_sb_list": ("MultiplatformAdsReportpagetypesblistResponse", "list"),
    "walmart_report_platform_sb_list": ("MultiplatformAdsReportplatformsblistResponse", "list"),
    "walmart_report_platform_sp_list": ("MultiplatformAdsReportplatformsplistResponse", "list"),
    "walmart_report_platform_sv_list": ("MultiplatformAdsReportplatformsvlistResponse", "list"),
    "walmart_report_search_trends_list": ("MultiplatformAdsReportsearchtrendslistResponse", "list"),
}

# --- multiplatform_other.py -> multi_platform.py ---
MP_OTHER_BINDINGS = {
    "batch_review": ("MultiplatformOrderReviewResponse", "one"),
    "pre_shipment": ("MultiplatformOrderPreshipmentResponse", "list"),
    "walmart_comment_list": ("MultiplatformWalmartQuerycommentlistResponse", "list"),
}

# --- multiplatform_platforms.py -> multi_platform.py ---
MP_PLATFORMS_BINDINGS = {
    "aliexpress_list_v2": ("AliexpressListV2Response", "list"),
    "batch_temu_address_decrypt": ("TemuTemuaddressdecryptResponse", "one"),
    "coupang_stock_list": ("MultiplatformCoupangStocksearchResponse", "list"),
    "delete_cargo_storage": ("MultiplatformDeletecargostorageResponse", "one"),
    "fbs_stock_list": ("MultiplatformFbsStocksearchResponse", "list"),
    "fbt_stock_list": ("FbtStocksearchV2Response", "list"),
    "fbt_stock_search": ("MultiplatformFbtStocksearchResponse", "list"),
    "full_list": ("MultiplatformFullStocksearchResponse", "list"),
    "line_list": ("MultiplatformLineListResponse", "list"),
    "query_shipping_list_v2": ("MultiplatformQueryShippinglistResponse", "list"),
    "shein_list": ("MultiplatformSheinListResponse", "list"),
    "shopify_variant_list": ("MultiplatformShopifyVariantlistResponse", "list"),
    "temu_cargo": ("MultiplatformTemuCargoResponse", "list"),
    "temu_list": ("MultiplatformTemuListResponse", "list"),
    "tik_tok_list": ("MultiplatformTiktokListResponse", "list"),
    "wayfair_stock_list": ("MultiplatformWayfairStocksearchResponse", "list"),
    "add_cargo_goods_list": ("CargoAddcargogoodsListResponse", "list"),
    "address_return_address_list": ("MultiplatformAddressReturnaddresslistResponse", "one"),
    "aliexpress_list": ("MultiplatformAliexpressListResponse", "list"),
    "e_bay_list": ("MultiplatformEbayListResponse", "list"),
    "multiplatform_cargo_storage": ("MultiplatformCargoStorageResponse", "one"),
    "profit_report_msku": ("ProfitReportMskuResponse", "list"),
    "profit_report_order": ("ProfitReportOrderResponse", "list"),
    "profit_report_seller": ("ProfitReportSellerResponse", "list"),
    "profit_report_sku": ("ProfitReportSkuResponse", "list"),
    "self_shipment_order_delivery_goods": ("SelfshipmentorderDeliverygoodsResponse", "list"),
    "set_order_weighed": ("MultiplatformCargoStorageResponse", "list"),  # closest match
    "shipping_detail_by_code": ("MultiplatformQueryShippingdetailResponse", "list"),
    "shipping_order_allocate": ("MultiplatformAllocateStockResponse", "one"),
    "shipping_order_delivery": ("MultiplatformShippinglistDeliveryResponse", "list"),
    "shipping_order_picking": ("MultiplatformShippinglistPickingResponse", "list"),
    "temu_stock_order_query_page": ("StockorderTemuQuerypageResponse", "list"),
    "walmart_list": ("MultiplatformWalmartListResponse", "list"),
}


def process_file(filepath, bindings, import_module, import_classes):
    """Process a single endpoint file to bind response models."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Add import block
    import_block = "from " + import_module + " import (\n"
    for cls in sorted(import_classes):
        import_block += f"    {cls},\n"
    import_block += ")\n"

    # Check if there's already an import from this module
    if import_module in content:
        # Replace existing import
        old_import = re.search(rf'from {re.escape(import_module)} import \([^)]+\)', content)
        if old_import:
            content = content[:old_import.start()] + import_block + content[old_import.end():]
    else:
        # Insert after __future__ import
        future_match = re.search(r'from __future__ import annotations\n', content)
        if future_match:
            content = content[:future_match.end()] + "\n" + import_block + content[future_match.end():]
        else:
            content = import_block + content

    # Process each method binding
    for method_name, (response_class, parse_mode) in bindings.items():
        # Pattern for "list | dict" return type methods
        if parse_mode == "list":
            # Replace return type annotation: list | dict -> list[ResponseClass]
            content = re.sub(
                rf'(async def {method_name}\([^)]*\)) -> list \| dict',
                rf'\1 -> list[{response_class}]',
                content
            )
            # Replace the response parsing block
            # Pattern: resp = await self._post(...)
            #          if isinstance(resp.data, list):
            #              return resp.data
            #          return resp.data or {}
            old_pattern = (
                r'(resp = await self\._post\([^)]+\))\n'
                rf'(\s+)if isinstance\(resp\.data, list\):\n'
                rf'\2\s+return resp\.data\n'
                rf'\2\s+return resp\.data or {{}}'
            )
            new_pattern = rf'\1\n\2return self._parse_list(resp.data, {response_class})'
            content = re.sub(old_pattern, new_pattern, content)
        else:  # "one"
            # For methods returning dict -> ResponseClass | None
            # Pattern: return resp.data or {}
            old_pattern_1 = (
                r'(resp = await self\._post\([^)]+\))\n'
                rf'(\s+)if isinstance\(resp\.data, list\):\n'
                rf'\2\s+return resp\.data\n'
                rf'\2\s+return resp\.data or {{}}'
            )
            new_pattern_1 = rf'\1\n\2return self._parse_one(resp.data, {response_class})'
            content = re.sub(old_pattern_1, new_pattern_1, content)

            # Also handle simple dict return: return resp.data or {}
            old_pattern_2 = (
                r'(resp = await self\._post\([^)]+\))\n'
                rf'(\s+)return resp\.data or {{}}'
            )
            new_pattern_2 = rf'\1\n\2return self._parse_one(resp.data, {response_class})'
            content = re.sub(old_pattern_2, new_pattern_2, content)

            # Replace return type annotation: dict -> ResponseClass | None
            content = re.sub(
                rf'(async def {method_name}\([^)]*\)) -> list \| dict',
                rf'\1 -> {response_class} | None',
                content
            )
            content = re.sub(
                rf'(async def {method_name}\([^)]*\)) -> dict',
                rf'\1 -> {response_class} | None',
                content
            )

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Processed {filepath}")


if __name__ == "__main__":
    base = "/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing"

    # Collect all unique response classes needed per file
    restocking_classes = {cls for cls, _ in RESTOCKING_BINDINGS.values()}
    mp_ads_classes = {cls for cls, _ in MP_ADS_BINDINGS.values()}
    mp_other_classes = {cls for cls, _ in MP_OTHER_BINDINGS.values()}
    mp_platforms_classes = {cls for cls, _ in MP_PLATFORMS_BINDINGS.values()}

    # Process restocking.py
    process_file(
        f"{base}/endpoints/restocking.py",
        RESTOCKING_BINDINGS,
        "..models.responses.fba_sug",
        restocking_classes,
    )

    # Process multiplatform_ads.py
    process_file(
        f"{base}/endpoints/multiplatform_ads.py",
        MP_ADS_BINDINGS,
        "..models.responses.multi_platform",
        mp_ads_classes,
    )

    # Process multiplatform_other.py
    process_file(
        f"{base}/endpoints/multiplatform_other.py",
        MP_OTHER_BINDINGS,
        "..models.responses.multi_platform",
        mp_other_classes,
    )

    # Process multiplatform_platforms.py
    process_file(
        f"{base}/endpoints/multiplatform_platforms.py",
        MP_PLATFORMS_BINDINGS,
        "..models.responses.multi_platform",
        mp_platforms_classes,
    )

    print("Done! All files processed.")

#!/usr/bin/env python3
"""Script to bind response models to endpoint methods - v2 with line-based replacement."""
import re

BASE = "/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing"

# ===== Mapping: endpoint method -> (ResponseClass, parse_mode) =====
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

MP_OTHER_BINDINGS = {
    "batch_review": ("MultiplatformOrderReviewResponse", "one"),
    "pre_shipment": ("MultiplatformOrderPreshipmentResponse", "list"),
    "walmart_comment_list": ("MultiplatformWalmartQuerycommentlistResponse", "list"),
}

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
    "set_order_weighed": ("MultiplatformCargoStorageResponse", "list"),
    "shipping_detail_by_code": ("MultiplatformQueryShippingdetailResponse", "list"),
    "shipping_order_allocate": ("MultiplatformAllocateStockResponse", "one"),
    "shipping_order_delivery": ("MultiplatformShippinglistDeliveryResponse", "list"),
    "shipping_order_picking": ("MultiplatformShippinglistPickingResponse", "list"),
    "temu_stock_order_query_page": ("StockorderTemuQuerypageResponse", "list"),
    "walmart_list": ("MultiplatformWalmartListResponse", "list"),
}


def process_file(filepath, bindings):
    """Process a single endpoint file - line-based replacement."""
    with open(filepath, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    i = 0
    changed = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a "resp = await self._post(..." line
        stripped = line.strip()
        if stripped.startswith('resp = await self._post('):
            # Look backward to find the method definition to know which binding to apply
            # Find the method name by looking at preceding lines
            method_name = None
            for j in range(i - 1, max(i - 30, -1), -1):
                m = re.match(r'\s+async def (\w+)\(', lines[j])
                if m:
                    method_name = m.group(1)
                    break

            if method_name and method_name in bindings:
                response_class, parse_mode = bindings[method_name]
                indent = len(line) - len(line.lstrip())
                indent_str = ' ' * indent

                # Keep the resp = line, then check next lines
                new_lines.append(line)
                i += 1

                # Collect the block that follows (isinstance check pattern or dict return)
                block_lines = []
                while i < len(lines):
                    next_stripped = lines[i].strip()
                    if next_stripped == '':
                        break
                    if next_stripped.startswith('if isinstance(resp.data, list):'):
                        block_lines.append(lines[i])
                        i += 1
                        continue
                    if next_stripped == 'return resp.data' or next_stripped == 'return resp.data or {}':
                        block_lines.append(lines[i])
                        i += 1
                        continue
                    break

                # Replace the block with the appropriate parse call
                if parse_mode == "list":
                    new_lines.append(f'{indent_str}return self._parse_list(resp.data, {response_class})')
                else:
                    new_lines.append(f'{indent_str}return self._parse_one(resp.data, {response_class})')
                changed += 1
                continue

        new_lines.append(line)
        i += 1

    result = '\n'.join(new_lines)

    with open(filepath, 'w') as f:
        f.write(result)

    print(f"Processed {filepath}: {changed} methods rebound")


if __name__ == "__main__":
    process_file(f"{BASE}/endpoints/restocking.py", RESTOCKING_BINDINGS)
    process_file(f"{BASE}/endpoints/multiplatform_ads.py", MP_ADS_BINDINGS)
    process_file(f"{BASE}/endpoints/multiplatform_other.py", MP_OTHER_BINDINGS)
    process_file(f"{BASE}/endpoints/multiplatform_platforms.py", MP_PLATFORMS_BINDINGS)
    print("Done!")

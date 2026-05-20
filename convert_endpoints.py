#!/usr/bin/env python3
"""Transform endpoint files to bind response models.

Reads existing endpoint files, maps methods to response models, and writes updated files.
"""

import re
from pathlib import Path

BASE = Path("/Users/a1/PycharmProjects/lingxing-sdk/src/lingxing")


def read_file(path):
    return path.read_text()


def write_file(path, content):
    path.write_text(content)
    print(f"  Written: {path}")


# ── Manual mapping: method_name -> response_class_name ──
# These are carefully verified mappings from method to Response class

FBA_MAPPING = {
    # Methods already using old models from models.fba - need to switch to response models
    'get_fba_product_list': ('FbaShipmentGetfbaproductlistResponse', 'list'),
    'get_head_logistics_fee_types': ('FbaShipmentGetheadlogisticsfeetypesResponse', 'list'),
    'get_inbound_shipment_list': ('StorageShipmentGetinboundshipmentlistResponse', 'page'),
    'get_sea_track_supplier_carriers': ('FbaShipmentGetseatracksuppliercarriersResponse', 'list'),
    'shipment_plan_lists': ('FbaReportShipmentplanlistsResponse', 'list'),
    # Methods currently returning list|dict or dict that have response models
    'box_info': ('FbaShipmentBoxinfoResponse', 'one_or_list'),
    'create_sended_order': ('StorageShipmentCreatesendedorderResponse', 'one'),
    'create_ship_from_address': ('FbaShipmentCreateshipfromaddressResponse', 'one'),
    'create_shipment_plan': ('StorageShipmentCreateshipmentplanResponse', 'one'),
    'fba_received_inventory': ('FbaReportReceivedinventoryResponse', 'one'),
    'fba_shipment_list': ('FbaReportShipmentlistResponse', 'one_or_list'),
    'ship_from_address_list': ('FbaShipmentShipfromaddresslistResponse', 'one'),
    'shopping_address': ('OpenapiFbashipmentShoppingaddressResponse', 'one'),
    'sync_shipment': ('FbaShipmentSyncshipmentResponse', 'one'),
    'create_ready_send_order': ('StorageShipmentCreatereadysendorderResponse', 'one'),
    'get_inbound_shipment_list_mws_detail': ('StorageShipmentGetinboundshipmentlistmwsdetailResponse', 'one_or_list'),
    'get_inbound_shipment_list_mws_detail_list': ('StorageShipmentGetinboundshipmentlistmwsdetaillistResponse', 'one_or_list'),
    'print_fba_labels': ('StorageShipmentPrintfbalabelsResponse', 'one'),
    'print_fnsku_labels': ('StorageShipmentPrintfnskulabelsResponse', 'one'),
    'search_process_result': ('StorageShipmentSearchprocessresultResponse', 'one_or_list'),
    'vc_batch_send_goods': ('GetinvoiceInvoiceBatchsendgoodsResponse', 'one'),
    # NO MATCH - keep as dict
    # 'invalid_shipment_sn', 'send_goods', 'shipment_lock_stock', 
    # 'update_custom_cost', 'update_plan_lists', 'update_ship_from_address',
    # 'update_shipment_actual_status', 'outbound_order_release_stock',
    # 'update_inbound_shipment_list_mws', 'update_list_logistics'
}

FINANCE_MAPPING = {
    'fiance_profit_msku': ('FinanceProfitstateProfitmskuResponse', 'one_or_list'),
    'order_profit_list_msku': ('FinanceMreportOrderprofitResponse', 'one_or_list'),
    'query_receipt_funds_list': ('FinanceQueryreceiptfundslistResponse', 'one_or_list'),
    'request_funds_order_list': ('RequestfundsOrderListResponse', 'one_or_list'),
    'lazada_payout_list': ('LazadaPayoutListResponse', 'one_or_list'),
    'lazada_settlement_list': ('LazadaSettlementListResponse', 'one_or_list'),
    'profit_asin': ('FinanceProfitstateProfitasinResponse', 'one_or_list'),
    'profit_asin_son': ('FinanceProfitstateProfitasinsonResponse', 'one_or_list'),
    'profit_report_order_transcation_list': ('OrderTranscationListResponse', 'one_or_list'),
    'profit_settlement': ('FinanceProfitstateProfitsettlementResponse', 'one_or_list'),
    'request_funds_pool_custom_fee_list': ('RequestfundspoolCustomfeeListResponse', 'one_or_list'),
    'request_funds_pool_inbound_list': ('RequestfundspoolInboundListResponse', 'one_or_list'),
    'request_funds_pool_logistics_list': ('RequestfundspoolLogisticsListResponse', 'one_or_list'),
    'request_funds_pool_other_fee_list': ('RequestfundspoolOtherfeeListResponse', 'one_or_list'),
    'request_funds_pool_prepay_list': ('RequestfundspoolPrepayListResponse', 'one_or_list'),
    'request_funds_pool_purchase_list': ('RequestfundspoolPurchaseListResponse', 'one_or_list'),
    'shopee_adjustment_list': ('ShopeeAdjustmentListResponse', 'one_or_list'),
    'shopee_income_list': ('ShopeeIncomeListResponse', 'one_or_list'),
    'shopee_payout_list': ('ShopeePayoutListResponse', 'one_or_list'),
    'fee_management_list': ('FeemanagementOtherfeeListResponse', 'one_or_list'),
    'bd_profit_asin': ('ReportAsinListResponse', 'one_or_list'),
    'bd_profit_parent_asin': ('ParentAsinListResponse', 'one_or_list'),
    'bd_profit_sku': ('ReportSkuListResponse', 'one_or_list'),
    'bd_profit_seller': ('ReportSellerListResponse', 'one_or_list'),
    'bd_profit_seller_summary': ('SellerSummaryListResponse', 'one_or_list'),
    'bd_profit_order': ('ReportOrderListResponse', 'one_or_list'),
    'settlement_summary_list': ('SettlementSummaryListResponse', 'one_or_list'),
    'settlement_transaction_list': ('TransactionDetailListResponse', 'one_or_list'),
    'receivable_report_list': ('ReceivableReportListResponse', 'one_or_list'),
    'report_list_detail': ('ReportListDetailResponse', 'one_or_list'),
    'reportlistdetailinfo': ('ListDetailInfoResponse', 'one'),
    # NO MATCH:
    # 'fee_management_create', 'fee_management_edit', 'fee_management_discard', 'fee_management_delete'
    # 'bd_profit_msku', 'settle_detail_query', 'summary_query', 'settlement_report',
    # 'settlement_export_url_get', 'cost_stream', 'invoice_list', 'invoice_campaign_list',
    # 'invoice_detail', 'compute_manual'
}

SALE_MAPPING = {
    'fbm_order_detail': ('OrderOrderGetorderdetailResponse', 'one_or_list'),
    'fbm_order_list': ('OrderOrderGetorderlistResponse', 'one_or_list'),
    'get_merchant_shipping_group': ('PublishManageGetmerchantshippinggroupResponse', 'one_or_list'),
    'listing': ('MwsListingResponse', 'one_or_list'),
    'order_detail': ('MwsOrderdetailResponse', 'one_or_list'),
    'orderlists': ('MwsOrdersResponse', 'one_or_list'),
    'product_list': ('AmazonProductListResponse', 'one_or_list'),
    'product_publish': ('AmazonProductPublishResponse', 'one_or_list'),
    'productlink': ('StorageProductLinkResponse', 'one_or_list'),
    'publish_helper_v2': ('PublishManageCategoryrootResponse', 'one_or_list'),
    'publish_manage_category_children': ('PublishManageCategorychildrenResponse', 'one_or_list'),
    'publish_manage_category_root': ('PublishManageCategoryrootResponse', 'one_or_list'),
    'publish_manage_get_product_type': ('PublishManageGetproducttypeResponse', 'one_or_list'),
    'query_product_list': ('AmazonProductSearchResponse', 'one_or_list'),
    'update_fbm_inventory': ('FbmmanagementModifyfbminventoryResponse', 'one'),
    'adjust_price_adjust_price_manual': ('ModuleAdjustpriceAdjustpricemanualResponse', 'one_or_list'),
    'b2b_price_modify_price': ('B2bpriceModifypriceResponse', 'one_or_list'),
    'fba_fee_difference_list': ('FbafeedifferenceOrderListResponse', 'one_or_list'),
    'fba_fee_difference_msku_list': ('FbafeedifferenceMskuListResponse', 'one_or_list'),
    'global_tag_page_list': ('ListingPageListResponse', 'one_or_list'),
    'listing_operate_log_page_list': ('ListingmanageListingoperatelogPagelistResponse', 'one_or_list'),
    'pricing_submit': ('ListingProductpricingPricingsubmitResponse', 'one'),
    'promotion_listing_detail_coupon': ('PromotionListingdetailcouponResponse', 'one_or_list'),
    'promotion_listing_detail_manage': ('PromotionListingdetailmanageResponse', 'one_or_list'),
    'promotion_listing_detail_prime_discount': ('PromotionListingdetailprimediscountResponse', 'one_or_list'),
    'promotion_listing_detail_sec_kill': ('PromotionListingdetailseckillResponse', 'one_or_list'),
    'promotion_listing_list': ('PromotionListinglistResponse', 'one_or_list'),
    'promotional_activities_coupon_list': ('PromotionalactivitiesCouponListResponse', 'one_or_list'),
    'promotional_activities_manage_list': ('PromotionalactivitiesManageListResponse', 'one_or_list'),
    'promotional_activities_sec_kill_list': ('PromotionalactivitiesSeckillListResponse', 'one_or_list'),
    'promotional_activities_vip_discount_list': ('PromotionalactivitiesVipdiscountListResponse', 'one_or_list'),
    # NO MATCH: 'add_goods_tag', 'delete_goods_tag', 'get_prices', 'refund_order',
    # 'sc_order_set_remark', 'unlink_listing', 'update_principal', 'upload_tracking',
    # 'after_sale_list', 'global_tag_add_tag', 'global_tag_remove_tag',
    # 'product_relationbatch_link', 'query_listing_relation_tag_list'
}

WAREHOUSE_MAPPING = {
    # Already using old models - switch to response models
    'purchase_receipt_order_list': ('DeliveryreceiptPurchasereceiptorderGetorderlistResponse', 'page'),
    'fba_stock': ('FbaFbastockFbalistResponse', 'one_or_list'),
    'fba_stock_v2': ('OpenapiStorageFbawarehousedetailResponse', 'one_or_list'),
    'wms_order_list': ('WmsOrderWmsorderlistResponse', 'one_or_list'),
    'warehouse_statement_new': ('InventorylogWarehouseinventoryWarehousecenterstatementResponse', 'one_or_list'),
    'get_process_order_lists': ('InventoryreceiptStorageprocessGetorderlistsResponse', 'one_or_list'),
    'get_storage_adjust_order_list': ('InventoryreceiptStorageadjustmentGetstorageadjustorderlistResponse', 'one_or_list'),
    'get_storage_allocation_list': ('InventoryreceiptStorageallocationGetstorageallocationlistResponse', 'one_or_list'),
    'inbound_get_custom_types': ('StorageInboundGetcustomtypesResponse', 'page'),
    'inboundget_orders': ('StorageInboundGetordersResponse', 'one_or_list'),
    'outbound_get_custom_types': ('StorageOutboundGetcustomtypesResponse', 'page'),
    'outboundget_orders': ('StorageOutboundGetordersResponse', 'one_or_list'),
    'removal_inbound_list': ('OwmsRemovalinboundListResponse', 'one_or_list'),
    # Methods currently returning list|dict or dict that have response models
    'add_allocation_order': ('InventoryreceiptStorageallocationAddallocationorderResponse', 'one'),
    'adjust_order_confirm': ('AdjustorderAdjustSetadjustResponse', 'one'),
    'create_inbound': ('OwmsInboundCreateinboundResponse', 'one'),
    'get_adjust_order_confirm_result': ('AdjustorderAdjustGetadjuststatusResponse', 'one'),
    'get_receive_good_records': ('OwmsInboundGetreceivegoodrecordsResponse', 'one'),
    'inbound_order_confirm': ('InboundorderInboundSetinboundResponse', 'one'),
    'order_add': ('StorageStorageOrderaddResponse', 'one'),
    'order_add_out': ('StorageStorageOrderaddoutResponse', 'one'),
    'outbound_order_confirm': ('OutboundorderOutboundSetoutboundResponse', 'one'),
    'over_seas_stock_detail': ('OverseawarehouseStockorderDetailResponse', 'one_or_list'),
    'oversea_warehouse_match_list': ('OverseawarehousesettingMatchlistResponse', 'one_or_list'),
    'quality_inspection_order_detail': ('QualityinspectionorderDetailResponse', 'one_or_list'),
    'wms_order_detail': ('WmsorderGetwmsordersbyordernumbersResponse', 'one_or_list'),
    'add_adjustment_order': ('InventoryreceiptStorageadjustmentAddadjustmentorderResponse', 'one'),
    'add_rebrand_adjustment_order': ('InventoryreceiptStorageadjustmentAddrebrandadjustmentorderResponse', 'one'),
    'add_sku_adjustment_order': ('InventoryreceiptStorageadjustmentAddskuadjustmentorderResponse', 'one'),
    'add_storage_process_order': ('InventoryreceiptStorageprocessAddstorageprocessorderResponse', 'one'),
    'cancel_wms_order': ('WmsorderCancelResponse', 'one'),
    'check_add_order': ('InventoryreceiptInventorycheckAddorderResponse', 'one'),
    'check_get_order_detail': ('InventoryreceiptInventorycheckGetorderdetailResponse', 'one_or_list'),
    'check_get_order_list': ('InventoryreceiptInventorycheckGetorderlistResponse', 'one_or_list'),
    'get_packing_data': ('OwmsInboundGetpackingdataResponse', 'one_or_list'),
    'inbound_complete_receipt': ('OwmsInboundGetreceivegoodrecordsResponse', 'one_or_list'),
    'list_inbound': ('OwmsInboundListinboundResponse', 'one_or_list'),
    'list_order_nos': ('OwmsInboundListordernosResponse', 'one_or_list'),
    'match_sku_list': ('OwmsInboundMatchskulistResponse', 'one_or_list'),
    'outbound_order_delete': ('OutboundorderOutboundDeleteResponse', 'one'),
    'package_label': ('OwmsInboundPackagelabelResponse', 'one_or_list'),
    'submit_allocation_order': ('InventoryreceiptStorageallocationSubmitallocationorderResponse', 'one'),
    'switch_status': ('StorageWarehousebinSwitchstatusResponse', 'one'),
    'wms_order_get_wms_logistics_labels': ('WmsOrderGetwmslogisticslabelsResponse', 'one_or_list'),
    # NO MATCH: many write operations and some reads without response models
}


def transform_endpoint_file(name, mapping, class_name):
    """Transform an endpoint file to use response models."""
    endpoint_path = BASE / f"endpoints/{name}.py"
    content = read_file(endpoint_path)
    
    # Collect all needed response classes
    needed_classes = set()
    for method_name, (resp_class, parse_type) in mapping.items():
        needed_classes.add(resp_class)
    
    # Sort them for consistent import
    needed_classes = sorted(needed_classes)
    
    # Build the new import block
    import_line = f"from ..models.responses.{name} import (\n"
    for cls in needed_classes:
        import_line += f"    {cls},\n"
    import_line += ")\n"
    
    # Replace existing imports
    # For fba.py - replace from ..models.fba import ...
    # For warehouse.py - replace from ..models.warehouse import ...
    # For finance.py and sale.py - just add the new import
    
    if name in ('fba', 'warehouse'):
        # Remove old model import
        old_pattern = rf"from \.\.models\.{name} import \([^)]*\)\n"
        content = re.sub(old_pattern, '', content)
    
    # Add new import after the typing import
    if f"from ..models.responses.{name}" not in content:
        # Find the line "from ._base import BaseEndpoint"
        content = content.replace(
            "from ._base import BaseEndpoint\n",
            f"{import_line}\nfrom ._base import BaseEndpoint\n"
        )
    
    # Now transform each method
    for method_name, (resp_class, parse_type) in mapping.items():
        content = transform_method(content, method_name, resp_class, parse_type)
    
    write_file(endpoint_path, content)


def transform_method(content, method_name, resp_class, parse_type):
    """Transform a single method in the endpoint file content."""
    
    if parse_type == 'list':
        # Return type: list[RespClass], body: return self._parse_list(resp.data, RespClass)
        # Match the method - find async def method_name...-> ...:
        # Need to handle both old-style (with model) and new-style (list | dict)
        
        # Pattern for methods already using old models: list[OldModel]
        old_return_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*)list\[\w+\]'
        new_return = f'list[{resp_class}]'
        content = re.sub(old_return_pattern, rf'\g<1>{new_return}', content)
        
        # Pattern for methods returning list | dict
        old_return_pattern2 = rf'(async def {method_name}\([^)]*\)\s*->\s*)list\s*\|\s*dict'
        content = re.sub(old_return_pattern2, rf'\g<1>{new_return}', content)
        
        # Replace the return body
        # Old: return self._parse_list(resp.data, OldModel) or the if isinstance pattern
        # Replace the if isinstance pattern + return resp.data or {}
        content = replace_return_body(content, method_name, f'return self._parse_list(resp.data, {resp_class})')
        
    elif parse_type == 'page':
        # Return type: tuple[list[RespClass], int], body: return self._parse_page(resp.data, RespClass)
        old_return_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*)tuple\[list\[\w+\],\s*int\]'
        new_return = f'tuple[list[{resp_class}], int]'
        content = re.sub(old_return_pattern, rf'\g<1>{new_return}', content)
        
        # For page methods, body should already have _parse_page with old model
        content = replace_return_body(content, method_name, f'return self._parse_page(resp.data, {resp_class})')
        
    elif parse_type == 'one':
        # Return type: RespClass, body: return self._parse_one(resp.data, RespClass)
        old_return_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*)dict'
        new_return = resp_class
        content = re.sub(old_return_pattern, rf'\g<1>{new_return}', content)
        
        # Replace body
        content = replace_return_body(content, method_name, f'return self._parse_one(resp.data, {resp_class})')
        
    elif parse_type == 'one_or_list':
        # Return type: RespClass | list[RespClass], body varies
        # For methods that could return either a single object or a list
        old_return_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*)list\s*\|\s*dict'
        new_return = f'{resp_class} | list[{resp_class}]'
        content = re.sub(old_return_pattern, rf'\g<1>{new_return}', content)
        
        # Replace body - use _parse_one_or_list pattern
        content = replace_return_body(content, method_name, f'return self._parse_one_or_list(resp.data, {resp_class})')
    
    return content


def replace_return_body(content, method_name, new_return_line):
    """Replace the return statement in a method body."""
    # Find the method and replace its return pattern
    # Pattern: after the POST call, there's either:
    # 1. if isinstance(resp.data, list):\n    return resp.data\n   return resp.data or {}
    # 2. return self._parse_list(resp.data, OldModel)
    # 3. return resp.data or {}
    # 4. return self._parse_page(resp.data, OldModel)
    
    # Strategy: Find the method, then find and replace its return block
    
    # Find method start
    method_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*[^:]+:[\s\S]*?resp = await self\._post\([^)]+\)[^\n]*\n)'
    match = re.search(method_pattern, content)
    if not match:
        # Try without explicit resp assignment  
        method_pattern = rf'(async def {method_name}\([^)]*\)\s*->\s*[^:]+:[\s\S]*?await self\._post\([^)]+\)[^\n]*\n)'
        match = re.search(method_pattern, content)
    
    if match:
        method_start = match.group(1)
        rest = content[match.end():]
        
        # Check what follows - replace the old return pattern
        # Pattern 1: if isinstance block
        if_block = re.match(r'(\s+)if isinstance\(resp\.data, list\):\s*\n\s+return resp\.data\s*\n\s+return resp\.data or \{\}\s*\n', rest)
        if if_block:
            indent = if_block.group(1)
            old_block = if_block.group(0)
            new_block = f'{indent}{new_return_line}\n'
            content = content[:match.end()] + rest.replace(old_block, new_block, 1)
            return content
        
        # Pattern 2: return self._parse_list(resp.data, OldModel)
        parse_pattern = re.match(r'(\s+)return self\._parse_(?:list|page|one)\(resp\.data, \w+\)\s*\n', rest)
        if parse_pattern:
            indent = parse_pattern.group(1)
            old_block = parse_pattern.group(0)
            new_block = f'{indent}{new_return_line}\n'
            content = content[:match.end()] + rest.replace(old_block, new_block, 1)
            return content
        
        # Pattern 3: return resp.data or {}
        simple_return = re.match(r'(\s+)return resp\.data or \{\}\s*\n', rest)
        if simple_return:
            indent = simple_return.group(1)
            old_block = simple_return.group(0)
            new_block = f'{indent}{new_return_line}\n'
            content = content[:match.end()] + rest.replace(old_block, new_block, 1)
            return content
    
    return content


def main():
    print("Transforming endpoint files...")
    
    for name, mapping, class_name in [
        ('fba', FBA_MAPPING, 'FBA'),
        ('finance', FINANCE_MAPPING, 'Finance'),
        ('sale', SALE_MAPPING, 'Sale'),
        ('warehouse', WAREHOUSE_MAPPING, 'Warehouse'),
    ]:
        print(f"\nProcessing {name}.py ({len(mapping)} methods)...")
        transform_endpoint_file(name, mapping, class_name)
    
    print("\nDone!")


if __name__ == '__main__':
    main()

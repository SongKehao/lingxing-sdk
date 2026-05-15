"""Auto-generated Pydantic models from API fixtures."""

from typing import Optional
from pydantic import Field

from .common import LingXingModel


class GetBatchDetailListItem(LingXingModel):
    """Warehouse/GetBatchDetailList 响应数据项."""

    amount: Optional[str] = None
    bad_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    balance_num: Optional[int] = None
    batch_no: Optional[str] = None
    batch_time: Optional[str] = None
    delivery_order_sns: Optional[list] = None
    fee: Optional[str] = None
    fnsku: Optional[str] = None
    good_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[str] = None
    inventory_age: Optional[str] = None
    msku: Optional[str] = None
    order_sn: Optional[str] = None
    plan_sn: Optional[list] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    purchase_in_time: Optional[str] = None
    purchase_order_sns: Optional[list] = None
    qc_num: Optional[int] = None
    sku: Optional[str] = None
    source_batch_no: Optional[list] = None
    stock_cost: Optional[str] = None
    store_id: Optional[str] = None
    store_name: Optional[str] = None
    supplier_ids: Optional[list] = None
    supplier_names: Optional[list] = None
    total: Optional[int] = None
    transit_balance_num: Optional[int] = None
    type: Optional[int] = None
    type_name: Optional[str] = None
    update_time: Optional[str] = None
    wh_name: Optional[str] = None
    wid: Optional[int] = None

class GetBatchStatementListItem(LingXingModel):
    """Warehouse/GetBatchStatementList 响应数据项."""

    amount: Optional[str] = None
    bad_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    balance_num: Optional[int] = None
    batch_no: Optional[str] = None
    batch_state_id: Optional[str] = None
    delivery_order_sns: Optional[list] = None
    fee: Optional[str] = None
    fnsku: Optional[str] = None
    good_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[str] = None
    msku: Optional[str] = None
    order_sn: Optional[str] = None
    plan_sn: Optional[list] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    purchase_order_sns: Optional[list] = None
    qc_num: Optional[int] = None
    sku: Optional[str] = None
    source_batch_no: Optional[list] = None
    source_order_sn: Optional[list] = None
    stock_cost: Optional[str] = None
    store_id: Optional[str] = None
    store_name: Optional[str] = None
    supplier_ids: Optional[list] = None
    supplier_names: Optional[list] = None
    transit_balance_num: Optional[int] = None
    type: Optional[str] = None
    type_name: Optional[str] = None
    wh_name: Optional[str] = None
    wid: Optional[int] = None

class InventoryDetailsItem(LingXingModel):
    """Warehouse/InventoryDetails 响应数据项."""

    available_inventory_box_qty: Optional[int] = None
    average_age: Optional[int] = None
    bad_lock_num: Optional[int] = None
    fnsku: Optional[str] = None
    good_lock_num: Optional[int] = None
    head_stock_price: Optional[str] = None
    price: Optional[str] = None
    product_bad_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_num: Optional[int] = None
    product_onway: Optional[int] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    product_valid_num: Optional[int] = None
    purchase_price: Optional[str] = None
    quantity_receive: Optional[str] = None
    seller_id: Optional[str] = None
    sku: Optional[str] = None
    stock_age_list: Optional[list] = None
    stock_cost: Optional[str] = None
    stock_cost_total: Optional[str] = None
    stock_price: Optional[str] = None
    third_inventory: Optional[dict] = None
    transit_head_cost: Optional[str] = None
    wid: Optional[int] = None

class PurchaseReceiptOrderListItem(LingXingModel):
    """Warehouse/PurchaseReceiptOrderList 响应数据项."""

    business_order_sn: Optional[str] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    expect_arrival_time: Optional[str] = None
    inbound_order_sns: Optional[list] = None
    item_list: Optional[list] = None
    logistics_company: Optional[str] = None
    logistics_order_no: Optional[str] = None
    opt_realname: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    order_type: Optional[str] = None
    other_currency: Optional[str] = None
    other_fee: Optional[str] = None
    qc_type: Optional[int] = None
    receive_realname: Optional[str] = None
    receive_time: Optional[str] = None
    receive_uid: Optional[int] = None
    remark: Optional[str] = None
    shipping_cost: Optional[str] = None
    shipping_currency: Optional[str] = None
    status: Optional[int] = None
    supplier_id: Optional[int] = None
    update_time: Optional[str] = None
    wid: Optional[int] = None

class WarehouseListsItem(LingXingModel):
    """Warehouse/WarehouseLists 响应数据项."""

    country_code: Optional[str] = None
    is_delete: Optional[int] = None
    name: Optional[str] = None
    sub_type: Optional[int] = None
    t_country_area_name: Optional[str] = None
    t_status: Optional[str] = None
    t_warehouse_code: Optional[str] = None
    t_warehouse_name: Optional[str] = None
    type: Optional[int] = None
    wid: Optional[int] = None
    wp_id: Optional[int] = None
    wp_name: Optional[str] = None

class WarehouseStatementItem(LingXingModel):
    """Warehouse/WarehouseStatement 响应数据项."""

    amount: Optional[str] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    cancel_time: Optional[str] = None
    fee_cost: Optional[str] = None
    fnsku: Optional[str] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    price: Optional[str] = None
    product_amounts: Optional[str] = None
    product_bad_num: Optional[int] = None
    product_good_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_num: Optional[int] = None
    product_name: Optional[str] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    ref_order_sn: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[str] = None
    single_cg_price: Optional[str] = None
    single_fee_cost: Optional[str] = None
    sku: Optional[str] = None
    statement_id: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class WarehouseStatementNewItem(LingXingModel):
    """Warehouse/WarehouseStatementNew 响应数据项."""

    bad_balance_num: Optional[int] = None
    bad_lock_balance_num: Optional[int] = None
    bad_transit_balance_num: Optional[int] = None
    bad_transit_num: Optional[int] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    fee_cost: Optional[str] = None
    fnsku: Optional[str] = None
    good_balance_num: Optional[int] = None
    good_lock_balance_num: Optional[int] = None
    good_transit_balance_num: Optional[int] = None
    good_transit_num: Optional[int] = None
    head_stock_cost: Optional[str] = None
    head_stock_price: Optional[str] = None
    opt_real_name: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    product_amounts: Optional[str] = None
    product_bad_num: Optional[int] = None
    product_good_num: Optional[int] = None
    product_id: Optional[int] = None
    product_lock_bad_num: Optional[int] = None
    product_lock_good_num: Optional[int] = None
    product_name: Optional[str] = None
    product_qc_num: Optional[int] = None
    product_total: Optional[int] = None
    qc_balance_num: Optional[int] = None
    ref_order_sn: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[str] = None
    single_cg_price: Optional[str] = None
    single_fee_cost: Optional[str] = None
    single_stock_price: Optional[str] = None
    sku: Optional[str] = None
    statement_id: Optional[str] = None
    stock_cost: Optional[str] = None
    sub_type: Optional[str] = None
    sub_type_text: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class WmsOrderListItem(LingXingModel):
    """Warehouse/WmsOrderList 响应数据项."""

    actual_carrier: Optional[str] = None
    apportion_message: Optional[str] = None
    apportion_status: Optional[int] = None
    auto_allocate_status: Optional[int] = None
    auto_complete: Optional[int] = None
    batch_no: Optional[str] = None
    cancel_message: Optional[str] = None
    cancel_status: Optional[int] = None
    consignee: Optional[str] = None
    consignee_address: Optional[str] = None
    consignee_full_address: Optional[str] = None
    consignee_phone: Optional[str] = None
    consignee_postcode: Optional[str] = None
    create_at: Optional[str] = None
    deliver_deadline: Optional[str] = None
    delivered_at: Optional[str] = None
    deliverer: Optional[str] = None
    delivery_message: Optional[str] = None
    delivery_status: Optional[int] = None
    district: Optional[str] = None
    documents_file_id: Optional[int] = None
    email: Optional[str] = None
    first_mile_status: Optional[int] = None
    gross_profit_amount: Optional[str] = None
    gross_profit_rate: Optional[str] = None
    invoice_status: Optional[int] = None
    is_advance_delivery: Optional[int] = None
    is_check: Optional[int] = None
    is_lock_storage: Optional[int] = None
    is_order_print: Optional[int] = None
    is_surface_print: Optional[int] = None
    is_weigh: Optional[int] = None
    logistics_estimated_freight: Optional[str] = None
    logistics_estimated_freight_currency_code: Optional[str] = None
    logistics_freight: Optional[str] = None
    logistics_freight_currency_code: Optional[str] = None
    logistics_message: Optional[str] = None
    logistics_provider_id: Optional[int] = None
    logistics_provider_name: Optional[str] = None
    logistics_status: Optional[int] = None
    logistics_status_name: Optional[str] = None
    logistics_success_time: Optional[str] = None
    logistics_type_id: Optional[int] = None
    logistics_type_name: Optional[str] = None
    logistics_way: Optional[int] = None
    mark_label_file_id: Optional[int] = None
    mark_label_status: Optional[int] = None
    need_invoice: Optional[int] = None
    noShippingProductList: Optional[list] = None
    omsAttachments: Optional[dict] = None
    order_buyer_notes: Optional[str] = None
    order_currency_code: Optional[str] = None
    order_customer_service_notes: Optional[str] = None
    order_from: Optional[str] = None
    order_number: Optional[str] = None
    order_origin_amount: Optional[str] = None
    order_print_time: Optional[str] = None
    order_sns: Optional[list] = None
    order_tags: Optional[list] = None
    order_type: Optional[int] = None
    owms_waybill_no: Optional[str] = None
    package_delivered_data: Optional[list] = None
    package_no: Optional[str] = None
    payment_time: Optional[str] = None
    pick_index: Optional[int] = None
    picker: Optional[str] = None
    pkg_fee_weight: Optional[str] = None
    pkg_fee_weight_unit: Optional[str] = None
    pkg_height: Optional[str] = None
    pkg_length: Optional[str] = None
    pkg_real_weight: Optional[str] = None
    pkg_real_weight_unit: Optional[str] = None
    pkg_size_unit: Optional[str] = None
    pkg_volume: Optional[str] = None
    pkg_weight: Optional[str] = None
    pkg_weight_unit: Optional[str] = None
    pkg_width: Optional[str] = None
    platform_name: Optional[str] = None
    platform_order_no: Optional[list] = None
    platform_payment_time: Optional[str] = None
    process_sn: Optional[str] = None
    product_info: Optional[list] = None
    purchase_time: Optional[str] = None
    recipient_tax_no: Optional[str] = None
    reference_no: Optional[str] = None
    remark_attachment: Optional[str] = None
    report_message: Optional[str] = None
    report_status: Optional[int] = None
    seller_name: Optional[str] = None
    sender_tax_no: Optional[str] = None
    sid: Optional[int] = None
    site_text: Optional[str] = None
    split_num: Optional[int] = None
    status: Optional[int] = None
    status_name: Optional[str] = None
    stock_delivered_at: Optional[str] = None
    surface_file: Optional[dict] = None
    surface_file_id: Optional[int] = None
    surface_file_type: Optional[str] = None
    surface_print_time: Optional[str] = None
    tag_names: Optional[list] = None
    target_country: Optional[str] = None
    track_record: Optional[str] = None
    tracking_no: Optional[str] = None
    transfer_logistics_company_code: Optional[str] = None
    transfer_logistics_company_id: Optional[str] = None
    transfer_tracking_no: Optional[str] = None
    update_at: Optional[str] = None
    warehouse_name: Optional[str] = None
    warehouse_type: Optional[int] = None
    waybill_no: Optional[str] = None
    wid: Optional[int] = None
    wo_id: Optional[int] = None
    wo_number: Optional[str] = None

class GetProcessOrderListsItem(LingXingModel):
    """Warehouse/getProcessOrderLists 响应数据项."""

    create_by: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    finish_realname: Optional[str] = None
    finish_time: Optional[str] = None
    finish_uid: Optional[int] = None
    process_sn: Optional[str] = None
    product_list: Optional[list] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    type: Optional[int] = None
    update_time: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class GetStorageAdjustOrderListItem(LingXingModel):
    """Warehouse/getStorageAdjustOrderList 响应数据项."""

    adjustment_realname: Optional[str] = None
    adjustment_time: Optional[str] = None
    adjustment_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    company_id: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class InboundGetCustomTypesData(LingXingModel):
    """Warehouse/inboundGetCustomTypes 响应数据项."""

    list: Optional[list] = None
    total: Optional[int] = None

class InboundgetOrdersItem(LingXingModel):
    """Warehouse/inboundgetOrders 响应数据项."""

    cg_realname: Optional[str] = None
    cg_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    currency: Optional[str] = None
    custom_fields: Optional[list] = None
    custom_type_id: Optional[int] = None
    custom_type_name: Optional[str] = None
    fee_part_type: Optional[int] = None
    fee_part_type_text: Optional[str] = None
    inbound_idempotent_code: Optional[str] = None
    inbound_time: Optional[str] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_amount: Optional[str] = None
    order_sn: Optional[str] = None
    origin_purchase_rate: Optional[str] = None
    origin_shipping_currency: Optional[str] = None
    origin_shipping_fee: Optional[str] = None
    other_fee: Optional[str] = None
    purchase_order_sn: Optional[str] = None
    receipt_order_sn: Optional[str] = None
    remark: Optional[str] = None
    return_price: Optional[str] = None
    revoke_realname: Optional[str] = None
    revoke_time: Optional[str] = None
    revoke_uid: Optional[int] = None
    source_sn: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class InventoryBinDetailsItem(LingXingModel):
    """Warehouse/inventoryBinDetails 响应数据项."""

    fnsku: Optional[str] = None
    lockNum: Optional[int] = None
    msku: Optional[str] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    sku: Optional[str] = None
    store_id: Optional[str] = None
    third_inventory: Optional[dict] = None
    total: Optional[int] = None
    validNum: Optional[int] = None
    wh_name: Optional[str] = None
    whb_id: Optional[int] = None
    whb_name: Optional[str] = None
    whb_type: Optional[int] = None
    whb_type_name: Optional[str] = None
    wid: Optional[int] = None

class OutboundGetCustomTypesData(LingXingModel):
    """Warehouse/outboundGetCustomTypes 响应数据项."""

    list: Optional[list] = None
    total: Optional[int] = None

class OutboundgetOrdersItem(LingXingModel):
    """Warehouse/outboundgetOrders 响应数据项."""

    cg_realname: Optional[str] = None
    cg_uid: Optional[int] = None
    commit_realname: Optional[str] = None
    commit_time: Optional[str] = None
    commit_uid: Optional[int] = None
    create_realname: Optional[str] = None
    create_time: Optional[str] = None
    create_uid: Optional[int] = None
    currency: Optional[str] = None
    custom_fields: Optional[list] = None
    custom_type_id: Optional[int] = None
    custom_type_name: Optional[str] = None
    fee_part_type: Optional[int] = None
    fee_part_type_text: Optional[str] = None
    idempotent_code: Optional[str] = None
    increment_time: Optional[str] = None
    item_list: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_amount: Optional[str] = None
    order_sn: Optional[str] = None
    other_fee: Optional[str] = None
    outbound_time: Optional[str] = None
    purchase_order_sn: Optional[str] = None
    remark: Optional[str] = None
    return_price: Optional[str] = None
    revoke_realname: Optional[str] = None
    revoke_time: Optional[str] = None
    revoke_uid: Optional[int] = None
    source_sn: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    to_ware_house_name: Optional[str] = None
    to_wid: Optional[int] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class RemovalInboundListItem(LingXingModel):
    """Warehouse/removalInboundList 响应数据项."""

    address: Optional[dict] = None
    delivery_no: Optional[str] = None
    estimated_arrival_time: Optional[str] = None
    id: Optional[int] = None
    inbound_order_sns: Optional[list] = None
    order_no: Optional[str] = None
    order_status: Optional[int] = None
    product: Optional[list] = None
    remark: Optional[str] = None
    removal_order_no: Optional[str] = None
    shipper: Optional[str] = None
    shippment_time: Optional[str] = None
    sid: Optional[int] = None
    sid_name: Optional[str] = None
    submit: Optional[int] = None
    submiter: Optional[str] = None
    uid: Optional[int] = None
    uid_name: Optional[str] = None
    wid: Optional[int] = None
    wid_name: Optional[str] = None

class WareHouseBinStatementItem(LingXingModel):
    """Warehouse/wareHouseBinStatement 响应数据项."""

    fnsku: Optional[str] = None
    num: Optional[int] = None
    opt_realname: Optional[str] = None
    opt_time: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    remark: Optional[str] = None
    seller_id: Optional[str] = None
    sku: Optional[str] = None
    type: Optional[int] = None
    type_text: Optional[str] = None
    ware_house_name: Optional[str] = None
    whb_id: Optional[int] = None
    whb_name: Optional[str] = None
    whb_type_name: Optional[str] = None
    wid: Optional[int] = None

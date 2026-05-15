"""Pydantic models for FBA APIs."""
from typing import Optional

from .common import LingXingModel


class GetFbaProductListItem(LingXingModel):
    """Response item for GetFbaProductList."""

    asin: Optional[str] = None
    asin_url: Optional[str] = None
    fnsku: Optional[str] = None
    image: Optional[str] = None
    local_name: Optional[str] = None
    msku: Optional[str] = None
    parent_asin: Optional[str] = None
    product_id: Optional[int] = None
    sid: Optional[int] = None
    sku: Optional[str] = None
    title: Optional[str] = None

class GetHeadLogisticsFeeTypesItem(LingXingModel):
    """Response item for GetHeadLogisticsFeeTypes."""

    created_at: Optional[str] = None
    fee_type_id: Optional[int] = None
    name: Optional[str] = None
    remark: Optional[str] = None

class GetInboundShipmentListItem(LingXingModel):
    """Response item for GetInboundShipmentList."""

    actual_shipment_time: Optional[str] = None
    audit_status: Optional[int] = None
    create_time: Optional[str] = None
    create_user: Optional[str] = None
    custom_fields: Optional[list] = None
    delivery_date: Optional[str] = None
    destination_fulfillment_center_id: Optional[str] = None
    eta_date: Optional[str] = None
    etd_date: Optional[str] = None
    expected_arrival_date: Optional[str] = None
    fileList: Optional[list] = None
    file_id: Optional[str] = None
    gmt_create: Optional[str] = None
    head_fee_type: Optional[int] = None
    head_fee_type_name: Optional[str] = None
    head_fee_type_name_new: Optional[str] = None
    id: Optional[int] = None
    is_custom_shipment_time: Optional[int] = None
    is_delete: Optional[int] = None
    is_exist_clearance: Optional[int] = None
    is_exist_declaration: Optional[int] = None
    is_pick: Optional[int] = None
    is_print: Optional[int] = None
    is_return_stock: Optional[int] = None
    last_update_time: Optional[str] = None
    logistics: Optional[list] = None
    logistics_channel_name: Optional[str] = None
    logistics_list: Optional[list] = None
    logistics_provider_id: Optional[str] = None
    logistics_provider_name: Optional[str] = None
    logistics_tracking_number: Optional[str] = None
    method_id: Optional[str] = None
    method_name: Optional[str] = None
    not_relate_list: Optional[list] = None
    pay_status: Optional[int] = None
    pick_time: Optional[str] = None
    principal_user: Optional[list] = None
    print_num: Optional[int] = None
    relate_list: Optional[list] = None
    remark: Optional[str] = None
    shipment_sn: Optional[str] = None
    shipment_time: Optional[str] = None
    shipment_time_second: Optional[str] = None
    shipment_user: Optional[str] = None
    status: Optional[int] = None
    status_name: Optional[str] = None
    third_party_order_mode: Optional[int] = None
    third_party_order_status: Optional[int] = None
    update_time: Optional[str] = None
    vat_code: Optional[str] = None
    wid: Optional[int] = None
    wname: Optional[str] = None

class GetSeaTrackSupplierCarriersItem(LingXingModel):
    """Response item for GetSeaTrackSupplierCarriers."""

    home_page: Optional[str] = None
    name: Optional[str] = None
    shippers: Optional[str] = None

class ShipFromAddressListItem(LingXingModel):
    """Response item for ShipFromAddressList."""

    alias_name: Optional[str] = None
    city: Optional[str] = None
    company_name: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    email: Optional[str] = None
    id: Optional[int] = None
    is_default: Optional[int] = None
    phone: Optional[int] = None
    province: Optional[str] = None
    region: Optional[str] = None
    seller_country_name: Optional[str] = None
    seller_name: Optional[str] = None
    sender_name: Optional[str] = None
    sid: Optional[int] = None
    street_detail1: Optional[str] = None
    street_detail2: Optional[str] = None
    type: Optional[int] = None
    zip_code: Optional[int] = None

class ShipmentPlanListsItem(LingXingModel):
    """Response item for ShipmentPlanLists."""

    create_time: Optional[str] = None
    create_user: Optional[str] = None
    custom_fields: Optional[list] = None
    ispg_id: Optional[int] = None
    list: Optional[list] = None
    remark: Optional[str] = None
    seq: Optional[str] = None

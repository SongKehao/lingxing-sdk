"""Auto-generated Pydantic models from API fixtures."""

from typing import Optional
from pydantic import Field

from .common import LingXingModel


class PurchaseOrderListItem(LingXingModel):
    """Purchase/PurchaseOrderList 响应数据项."""

    alibaba_order_sn: Optional[str] = None
    amount_total: Optional[str] = None
    audit_uids: Optional[list] = None
    auditor_realname: Optional[str] = None
    auditor_time: Optional[str] = None
    auditor_uid: Optional[int] = None
    contact_number: Optional[str] = None
    contact_person: Optional[str] = None
    create_time: Optional[str] = None
    custom_fields: Optional[list] = None
    custom_order_sn: Optional[str] = None
    fee_part_type: Optional[int] = None
    icon: Optional[str] = None
    is_tax: Optional[int] = None
    item_list: Optional[list] = None
    last_realname: Optional[str] = None
    last_time: Optional[str] = None
    last_uid: Optional[int] = None
    logistics_info: Optional[list] = None
    opt_realname: Optional[str] = None
    opt_uid: Optional[int] = None
    order_sn: Optional[str] = None
    order_time: Optional[str] = None
    other_currency: Optional[str] = None
    other_fee: Optional[str] = None
    pay_status: Optional[int] = None
    pay_status_text: Optional[str] = None
    payment: Optional[str] = None
    payment_method: Optional[int] = None
    principal_uids: Optional[list] = None
    purchase_currency: Optional[str] = None
    purchase_rate: Optional[str] = None
    purchase_type: Optional[int] = None
    purchase_type_text: Optional[str] = None
    purchaser_id: Optional[int] = None
    qc_type: Optional[int] = None
    quantity_entry: Optional[int] = None
    quantity_real: Optional[int] = None
    quantity_receive: Optional[int] = None
    quantity_total: Optional[int] = None
    reason: Optional[str] = None
    remark: Optional[str] = None
    settlement_description: Optional[str] = None
    settlement_method: Optional[int] = None
    shipping_currency: Optional[str] = None
    shipping_price: Optional[str] = None
    status: Optional[int] = None
    status_shipped: Optional[int] = None
    status_shipped_text: Optional[str] = None
    status_text: Optional[str] = None
    sub_status: Optional[int] = None
    sub_status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    total_price: Optional[str] = None
    update_time: Optional[str] = None
    ware_house_bak_name: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None

class SupplierItem(LingXingModel):
    """Purchase/Supplier 响应数据项."""

    account_name: Optional[str] = None
    address_full: Optional[str] = None
    bank_card_number: Optional[str] = None
    contact_number: Optional[str] = None
    contact_person: Optional[str] = None
    credit_code: Optional[str] = None
    customer_supplier_id: Optional[str] = None
    email: Optional[str] = None
    employees: Optional[int] = None
    employees_text: Optional[str] = None
    fax: Optional[str] = None
    is_delete: Optional[int] = None
    level_text: Optional[str] = None
    open_bank: Optional[str] = None
    payment_account_group: Optional[list] = None
    payment_method_text: Optional[str] = None
    pc_name: Optional[str] = None
    period_config_key: Optional[str] = None
    period_config_text: Optional[str] = None
    prepay_percent: Optional[str] = None
    purchaser: Optional[str] = None
    purchaser_id: Optional[int] = None
    purchaser_id_text: Optional[str] = None
    qq: Optional[str] = None
    receipt_wid: Optional[int] = None
    receipt_wid_text: Optional[str] = None
    remark: Optional[str] = None
    settlement_description: Optional[str] = None
    settlement_method_text: Optional[str] = None
    supplier_code: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    template_id: Optional[str] = None
    template_name: Optional[str] = None
    url: Optional[str] = None
    w_name: Optional[str] = None
    wid: Optional[int] = None

class GetPurchasePlansItem(LingXingModel):
    """Purchase/getPurchasePlans 响应数据项."""

    attribute: Optional[list] = None
    audit_uids: Optional[list] = None
    cg_box_pcs: Optional[int] = None
    cg_opt_username: Optional[str] = None
    cg_uid: Optional[int] = None
    create_time: Optional[str] = None
    creator_real_name: Optional[str] = None
    creator_uid: Optional[int] = None
    custom_fields: Optional[list] = None
    expect_arrive_time: Optional[str] = None
    file: Optional[list] = None
    fnsku: Optional[str] = None
    gmt_modified: Optional[str] = None
    group_id: Optional[int] = None
    is_aux: Optional[int] = None
    is_combo: Optional[int] = None
    is_related_process_plan: Optional[int] = None
    list: Optional[list] = None
    marketplace: Optional[str] = None
    msku: Optional[list] = None
    perm_username: Optional[list] = None
    pic_url: Optional[str] = None
    plan_remark: Optional[str] = None
    plan_sn: Optional[str] = None
    ppg_sn: Optional[str] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    purchaser_id: Optional[int] = None
    purchaser_name: Optional[str] = None
    quantity_plan: Optional[int] = None
    remark: Optional[str] = None
    seller_name: Optional[str] = None
    sid: Optional[int] = None
    sku: Optional[str] = None
    spu: Optional[str] = None
    spu_name: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    update_time: Optional[str] = None
    warehouse_name: Optional[str] = None
    wid: Optional[int] = None

class PurchaserListsItem(LingXingModel):
    """Purchase/purchaserLists 响应数据项."""

    address: Optional[str] = None
    contact_phone: Optional[str] = None
    contacter: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    purchaser_id: Optional[int] = None

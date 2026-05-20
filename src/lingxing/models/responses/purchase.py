"""Auto-generated response models for Purchase."""
from typing import List, Optional

from pydantic import Field

from ..common import LingXingModel


class LocalInventorySupplierPaymentAccountGroup(LingXingModel):
    """payment_account_group sub-structure."""
    name: Optional[str] = Field(None, description="账户名称")
    account_name: Optional[str] = Field(None, description="户名")
    bank_name: Optional[str] = Field(None, description="开户行")
    account_id: Optional[str] = Field(None, description="账号")
    remark: Optional[str] = Field(None, description="备注")
    is_default: Optional[int] = Field(None, description="是否默认账户")
    is_open: Optional[int] = Field(None, description="是否启用账户")
    key: Optional[str] = Field(None, description="功能")
    version: Optional[str] = Field(None, description="功能版本")

class LocalInventorySupplierResponse(LingXingModel):
    """查询供应商列表."""
    customer_supplier_id: Optional[str] = Field(None, description="客户供应商id【已停用】")
    supplier_id: Optional[int] = Field(None, description="系统供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    supplier_code: Optional[str] = Field(None, description="供应商编码【供应商代码只支持数字、英文字母、英文句号、-】")
    employees: Optional[int] = Field(None, description="规模：员工数")
    url: Optional[str] = Field(None, description="供应商网址")
    contact_person: Optional[str] = Field(None, description="联系人")
    contact_number: Optional[str] = Field(None, description="联系电话")
    qq: Optional[str] = Field(None, description="qq")
    email: Optional[str] = Field(None, description="邮箱")
    fax: Optional[str] = Field(None, description="传真")
    account_name: Optional[str] = Field(None, description="户名")
    open_bank: Optional[str] = Field(None, description="开户行")
    bank_card_number: Optional[str] = Field(None, description="银行卡号")
    remark: Optional[str] = Field(None, description="备注")
    purchaser: Optional[str] = Field(None, description="跟进人")
    is_delete: Optional[int] = Field(None, description="是否已删除：0 否，1 是")
    address_full: Optional[str] = Field(None, description="详细地址")
    payment_method_text: Optional[str] = Field(None, description="支付方式")
    pc_name: Optional[str] = Field(None, description="采购合同名称")
    settlement_method_text: Optional[str] = Field(None, description="结算方式")
    settlement_description: Optional[str] = Field(None, description="结算描述")
    employees_text: Optional[str] = Field(None, description="规模大小")
    level_text: Optional[str] = Field(None, description="级别")
    credit_code: Optional[str] = Field(None, description="统一社会信用代码")
    prepay_percent: Optional[str] = Field(None, description="预付比例")
    payment_account_group: Optional[List[LocalInventorySupplierPaymentAccountGroup]] = Field(None, description="收款账户")
    period_config_key: Optional[str] = Field(None, description="结算账期")
    period_config_text: Optional[str] = Field(None, description="结算账期文本")
    wid: Optional[int] = Field(None, description="仓库id")
    w_name: Optional[str] = Field(None, description="仓库名称")
    template_id: Optional[str] = Field(None, description="新采购合同模板id")
    template_name: Optional[str] = Field(None, description="新采购合同模板名称")
    purchaser_id: Optional[int] = Field(None, description="采购方id")
    purchaser_id_text: Optional[str] = Field(None, description="采购方")
    receipt_wid: Optional[int] = Field(None, description="采购收货仓库id")
    receipt_wid_text: Optional[str] = Field(None, description="采购收货仓库")
    total: Optional[int] = Field(None, description="总数")


class LocalInventoryCreatepurchaseplanResponse(LingXingModel):
    """创建待采购的采购计划."""
    plan_sn: Optional[list] = Field(None, description="计划编号")
    ppg_sn: Optional[str] = Field(None, description="计划批次号")


class LocalInventoryGetpurchaseplansFile(LingXingModel):
    """file sub-structure."""
    name: Optional[str] = Field(None, description="附件名")
    url: Optional[str] = Field(None, description="附件url")

class LocalInventoryGetpurchaseplansResponse(LingXingModel):
    """查询采购计划列表."""
    total: Optional[int] = Field(None, description="总数")
    plan_sn: Optional[str] = Field(None, description="采购计划编号")
    ppg_sn: Optional[str] = Field(None, description="采购计划批次号")
    status_text: Optional[str] = Field(None, description="状态说明")
    status: Optional[int] = Field(None, description="状态值")
    creator_real_name: Optional[str] = Field(None, description="创建人名称")
    creator_uid: Optional[int] = Field(None, description="创建人id")
    create_time: Optional[str] = Field(None, description="创建时间")
    file: Optional[List[LocalInventoryGetpurchaseplansFile]] = Field(None, description="附件")
    plan_remark: Optional[str] = Field(None, description="备注")
    pic_url: Optional[str] = Field(None, description="产品图片")
    spu_name: Optional[str] = Field(None, description="款名")
    spu: Optional[str] = Field(None, description="SPU")
    product_name: Optional[str] = Field(None, description="品名")
    product_id: Optional[int] = Field(None, description="商品id")
    sku: Optional[str] = Field(None, description="SKU")
    attribute: Optional[list] = Field(None, description="属性")
    sid: Optional[int] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    marketplace: Optional[str] = Field(None, description="国家")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    msku: Optional[list] = Field(None, description="MSKU")
    supplier_id: Optional[dict] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    wid: Optional[int] = Field(None, description="仓库id")
    warehouse_name: Optional[str] = Field(None, description="仓库名称")
    purchaser_id: Optional[int] = Field(None, description="采购方id")
    purchaser_name: Optional[str] = Field(None, description="采购方名称")
    cg_box_pcs: Optional[int] = Field(None, description="单箱数量")
    quantity_plan: Optional[int] = Field(None, description="计划采购量")
    expect_arrive_time: Optional[str] = Field(None, description="期望到货时间")
    cg_uid: Optional[int] = Field(None, description="采购员id")
    cg_opt_username: Optional[str] = Field(None, description="采购员名称")
    remark: Optional[str] = Field(None, description="产品备注")
    is_combo: Optional[int] = Field(None, description="是否为组合商品：0 否，1 是")
    is_aux: Optional[int] = Field(None, description="是否为辅料：0 否，1 是")
    is_related_process_plan: Optional[int] = Field(None, description="是否关联了加工计划：0 否，1 是")
    perm_uid: Optional[list] = Field(None, description="单据负责人uid")
    perm_username: Optional[dict] = Field(None, description="单据负责人名称")


class LocalInventoryPurchaseorderlistPrincipalUids(LingXingModel):
    """principal_uids sub-structure."""
    id: Optional[str] = Field(None, description="单据负责人UID")
    name: Optional[str] = Field(None, description="单据负责人名称")

class LocalInventoryPurchaseorderlistItemList(LingXingModel):
    """item_list sub-structure."""
    id: Optional[int] = Field(None, description="采购单子项id")
    wid: Optional[int] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名称")
    relation_purchase_plan: Optional[list] = Field(None, description="更多采购计划号")
    plan_sn: Optional[str] = Field(None, description="采购计划号")
    product_id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="SKU")
    fnsku: Optional[str] = Field(None, description="FNSKU")
    sid: Optional[str] = Field(None, description="店铺id")
    model: Optional[str] = Field(None, description="型号")
    price: Optional[float] = Field(None, description="含税单价")
    amount: Optional[float] = Field(None, description="价税合计")
    quantity_plan: Optional[int] = Field(None, description="计划采购量")
    quantity_real: Optional[int] = Field(None, description="实际采购量")
    quantity_entry: Optional[int] = Field(None, description="到货入库量")
    quantity_receive: Optional[int] = Field(None, description="待到货量")
    quantity_return: Optional[int] = Field(None, description="退货数")
    quantity_exchange: Optional[int] = Field(None, description="换货量")
    quantity_qc: Optional[int] = Field(None, description="质检量")
    quantity_qc_prepare: Optional[int] = Field(None, description="待质检量")
    expect_arrive_time: Optional[str] = Field(None, description="期待到货时间")
    remark: Optional[str] = Field(None, description="备注")
    cases_num: Optional[int] = Field(None, description="箱数")
    quantity_per_case: Optional[int] = Field(None, description="单箱数量")
    is_delete: Optional[int] = Field(None, description="是否删除：0 否，1 是")
    msku: Optional[list] = Field(None, description="MSKU")
    attribute: Optional[str] = Field(None, description="属性")
    tax_rate: Optional[str] = Field(None, description="税率")
    spu: Optional[str] = Field(None, description="spu")
    spu_name: Optional[str] = Field(None, description="款名")
    custom_fields: Optional[list] = Field(None, description="自定义字段")

class LocalInventoryPurchaseorderlistLogisticsInfo(LingXingModel):
    """logistics_info sub-structure."""
    logistics_company: Optional[str] = Field(None, description="物流公司")
    logistics_order_no: Optional[str] = Field(None, description="物流单号")
    pol_id: Optional[str] = Field(None, description="物流信息记录id")
    purchase_order_id: Optional[str] = Field(None, description="采购订单唯一id")
    purchase_order_sn: Optional[str] = Field(None, description="采购订单号（order_sn）")

class LocalInventoryPurchaseorderlistResponse(LingXingModel):
    """查询采购单列表."""
    order_sn: Optional[str] = Field(None, description="采购单号")
    custom_order_sn: Optional[str] = Field(None, description="自定义单号")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商")
    opt_uid: Optional[int] = Field(None, description="采购员id")
    principal_uids: Optional[List[LocalInventoryPurchaseorderlistPrincipalUids]] = Field(None, description="单据负责人信息")
    auditor_realname: Optional[str] = Field(None, description="审核人姓名")
    opt_realname: Optional[str] = Field(None, description="操作人姓名")
    last_realname: Optional[str] = Field(None, description="最后操作人姓名")
    create_time: Optional[str] = Field(None, description="创建时间")
    order_time: Optional[str] = Field(None, description="下单时间")
    payment: Optional[str] = Field(None, description="应付货款（手工）")
    auditor_uid: Optional[int] = Field(None, description="审核人员id")
    auditor_time: Optional[str] = Field(None, description="审核时间")
    last_uid: Optional[int] = Field(None, description="最后操作人员id")
    last_time: Optional[str] = Field(None, description="最后操作时间")
    reason: Optional[str] = Field(None, description="作废原因")
    is_tax: Optional[int] = Field(None, description="是否含税：0 否，1 是")
    status: Optional[int] = Field(None, description="采购单状态： -1 作废 3 待提交 1 待下单 - 已审核 2 待签收(待到货) - 已下单 9 完成 121 (审批流)待审核 122 (审批流)驳回 124 (审批流)作废")
    status_text: Optional[str] = Field(None, description="状态说明")
    pay_status_text: Optional[str] = Field(None, description="支付状态说明")
    status_shipped: Optional[int] = Field(None, description="到货状态： 1 未到货 2 部分到货 3 全部到货")
    status_shipped_text: Optional[str] = Field(None, description="到货状态说明")
    amount_total: Optional[float] = Field(None, description="货物总价")
    total_price: Optional[float] = Field(None, description="总金额")
    icon: Optional[str] = Field(None, description="币种符号")
    pay_status: Optional[int] = Field(None, description="付款状态： 0 未申请 1 已申请 2 部分付款 3 已付款")
    remark: Optional[str] = Field(None, description="备注")
    other_fee: Optional[float] = Field(None, description="其他费用")
    other_currency: Optional[str] = Field(None, description="其他费用币种")
    fee_part_type: Optional[int] = Field(None, description="费用分摊方式： 0 不分摊 1 按金额 2 按数量")
    shipping_price: Optional[float] = Field(None, description="运费")
    shipping_currency: Optional[str] = Field(None, description="运费币种")
    purchase_currency: Optional[str] = Field(None, description="采购币种")
    purchase_rate: Optional[float] = Field(None, description="采购汇率")
    quantity_total: Optional[float] = Field(None, description="采购总量")
    wid: Optional[int] = Field(None, description="仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库名")
    ware_house_bak_name: Optional[str] = Field(None, description="仓库名(备份)")
    quantity_entry: Optional[int] = Field(None, description="入库量")
    quantity_real: Optional[int] = Field(None, description="实际采购量")
    quantity_receive: Optional[int] = Field(None, description="待到货量")
    update_time: Optional[str] = Field(None, description="采购单更新时间")
    purchaser_id: Optional[int] = Field(None, description="采购方id")
    contact_person: Optional[str] = Field(None, description="联系人")
    contact_number: Optional[str] = Field(None, description="联系方式")
    settlement_method: Optional[int] = Field(None, description="结算方式： 7 现结 8 月结")
    settlement_description: Optional[str] = Field(None, description="结算描述")
    purchase_type: Optional[str] = Field(None, description="采购类型 1:普通采购；2:1688采购")
    purchase_type_text: Optional[str] = Field(None, description="采购类型文本")
    alibaba_order_sn: Optional[str] = Field(None, description="1688订单号")
    sub_status: Optional[str] = Field(None, description="1688订单状态，1：待1688下单，2：等待买家付款，3：等待买家")
    sub_status_text: Optional[str] = Field(None, description="1688订单状态文本")
    custom_fields: Optional[list] = Field(None, description="自定义字段")
    payment_method: Optional[int] = Field(None, description="支付方式")
    item_list: Optional[List[LocalInventoryPurchaseorderlistItemList]] = Field(None, description="采购单子项")
    logistics_info: Optional[List[LocalInventoryPurchaseorderlistLogisticsInfo]] = Field(None, description="物流信息")


class PurchaserListsList(LingXingModel):
    """list sub-structure."""
    purchaser_id: Optional[int] = Field(None, description="采购方id")
    name: Optional[str] = Field(None, description="采购方名称")
    address: Optional[str] = Field(None, description="地址")
    contact_phone: Optional[str] = Field(None, description="联系方式")
    contacter: Optional[str] = Field(None, description="联系人")
    email: Optional[str] = Field(None, description="邮箱")

class PurchaserListsResponse(LingXingModel):
    """查询采购方列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[PurchaserListsList]] = Field(None, description="列表")


class PurchasePurchaseCreatepurchaseorderResponse(LingXingModel):
    """创建待到货的采购单."""
    order_sn: Optional[str] = Field(None, description="采购单号")
    custom_order_sn: Optional[str] = Field(None, description="自定义采购单号")


class PurchasePurchasechangeorderChangeorderlistList(LingXingModel):
    """list sub-structure."""
    order_sn: Optional[str] = Field(None, description="变更单号")
    create_time: Optional[str] = Field(None, description="创建时间")
    supplier_name: Optional[str] = Field(None, description="供应商")
    old_supplier_name: Optional[str] = Field(None, description="旧供应商")
    wid: Optional[str] = Field(None, description="仓库id")
    old_wid: Optional[str] = Field(None, description="旧仓库id")
    ware_house_name: Optional[str] = Field(None, description="仓库")
    old_ware_house_name: Optional[str] = Field(None, description="旧仓库")
    create_realname: Optional[str] = Field(None, description="创建人")
    opt_realname: Optional[str] = Field(None, description="采购员")
    remark: Optional[str] = Field(None, description="备注")
    status: Optional[int] = Field(None, description="状态标识码： -1 已驳回 0 待审核 1 已处理")
    status_text: Optional[str] = Field(None, description="状态文本")
    icon: Optional[str] = Field(None, description="货币符号")
    amount: Optional[float] = Field(None, description="金额")
    old_amount: Optional[float] = Field(None, description="旧金额")
    item_list: Optional[list] = Field(None, description="变更单商品子项")

class PurchasePurchasechangeorderChangeorderlistResponse(LingXingModel):
    """查询采购变更单列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[PurchasePurchasechangeorderChangeorderlistList]] = Field(None, description="列表数据")


class PurchasePurchasechangeorderCreatepurchasechangeorderResponse(LingXingModel):
    """创建已完成的采购变更单."""
    order_sn: Optional[str] = Field(None, description="采购变更单号")


class PurchasePurchaseoutsourceorderGetordersList(LingXingModel):
    """list sub-structure."""
    order_sn: Optional[str] = Field(None, description="单号")
    warehouse_name: Optional[str] = Field(None, description="仓库名")
    outsource_warehouse_name: Optional[str] = Field(None, description="加工仓库名")
    supplier_name: Optional[str] = Field(None, description="加工商名")
    create_time: Optional[str] = Field(None, description="创建时间")
    status_text: Optional[str] = Field(None, description="单据状态")
    create_realname: Optional[str] = Field(None, description="创建人")
    ptp_sn: Optional[str] = Field(None, description="加工计划单号")
    product_name: Optional[str] = Field(None, description="品名")
    sku: Optional[str] = Field(None, description="sku")
    fnsku: Optional[str] = Field(None, description="fnsku")
    outsource_quantity: Optional[float] = Field(None, description="委外数量")
    receive_quantity: Optional[float] = Field(None, description="已收货量")
    expect_arrive_time: Optional[str] = Field(None, description="预计到货时间")
    msku: Optional[list] = Field(None, description="MSKU数组")
    plan_sn: Optional[list] = Field(None, description="采购计划单号数组")
    seller_name: Optional[str] = Field(None, description="店铺")
    item: Optional[list] = Field(None, description="子项")

class PurchasePurchaseoutsourceorderGetordersResponse(LingXingModel):
    """查询委外订单列表."""
    list: Optional[List[PurchasePurchaseoutsourceorderGetordersList]] = Field(None, description="数据列表")
    total: Optional[int] = Field(None, description="数量总计")


class PurchasePurchaseReturnOrderCreatepurchasereturnorderResponse(LingXingModel):
    """创建已完成的采购退货单."""
    order_sn: Optional[str] = Field(None, description="采购退货单号")


class PurchasePurchaseReturnOrderGetpurchasereturnorderlistList(LingXingModel):
    """list sub-structure."""
    wid: Optional[int] = Field(None, description="仓库id")
    order_sn: Optional[str] = Field(None, description="退货单号")
    create_uid: Optional[int] = Field(None, description="创建人id")
    create_realname: Optional[str] = Field(None, description="创建人名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    last_time: Optional[str] = Field(None, description="更新时间")
    buyer_uid: Optional[int] = Field(None, description="采购员id")
    buyer_realname: Optional[str] = Field(None, description="采购员名称")
    purchase_order_sn: Optional[str] = Field(None, description="采购单号")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    return_method: Optional[int] = Field(None, description="退货方式：1 退货扣款，2 退货补货")
    replenish_method: Optional[int] = Field(None, description="补货方式：1 源单补货")
    receipt_funds_order_sn: Optional[str] = Field(None, description="收款单号")
    status: Optional[int] = Field(None, description="状态： 121 待审批 122 已驳回 124 已作废（审批作废） 10 已处理 20 已作废（单据作废）")
    purchase_currency: Optional[str] = Field(None, description="采购币种")
    purchase_currency_icon: Optional[str] = Field(None, description="采购币种符号")
    fee_part_type: Optional[int] = Field(None, description="费用分配方式： 0 不分配 1 按金额 2 按数量")
    shipping_currency: Optional[str] = Field(None, description="运费币种")
    shipping_price: Optional[float] = Field(None, description="退货运费")
    other_currency: Optional[str] = Field(None, description="其他费用币种")
    other_fee: Optional[float] = Field(None, description="其他费用")
    return_reason: Optional[str] = Field(None, description="退货原因")
    return_amount_total: Optional[str] = Field(None, description="退货总金额")
    remark: Optional[str] = Field(None, description="单据备注")
    item_list: Optional[list] = Field(None, description="子项列表")

class PurchasePurchaseReturnOrderGetpurchasereturnorderlistResponse(LingXingModel):
    """查询采购退货单列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[PurchasePurchaseReturnOrderGetpurchasereturnorderlistList]] = Field(None, description="列表")


class StorageSupplierEditResponse(LingXingModel):
    """添加/修改供应商."""
    customer_supplier_id: Optional[int] = Field(None, description="客户供应商ID【已停用】")
    erp_supplier_id: Optional[int] = Field(None, description="系统供应商ID")


class PurchasePurchaseCancelResponse(LingXingModel):
    """作废采购单."""


class PurchaseCancelPurchaseReturnOrderResponse(LingXingModel):
    """作废采购/委外退货单."""


class PurchaseOrderModifyRemarkResponse(LingXingModel):
    """编辑采购单备注."""


class PurchasePlanCancelResponse(LingXingModel):
    """作废采购计划."""


class PurchaseSetOrdersResponse(LingXingModel):
    """采购单下单."""


class PurchaseAddLogisticsResponse(LingXingModel):
    """添加采购单物流信息."""


class PurchaseSetOrderFinishResponse(LingXingModel):
    """采购单整单结束到货."""


# Migrated from old models/
class GetPurchasePlansItem(LingXingModel):
    """Response item for getPurchasePlans."""

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
    is_aux: Optional[str] = None
    is_combo: Optional[str] = None
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


class PurchaseOrderListItem(LingXingModel):
    """Response item for PurchaseOrderList."""

    alibaba_order_sn: Optional[int] = None
    amount_total: Optional[float] = None
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
    other_fee: Optional[float] = None
    pay_status: Optional[int] = None
    pay_status_text: Optional[str] = None
    payment: Optional[float] = None
    payment_method: Optional[int] = None
    principal_uids: Optional[list] = None
    purchase_currency: Optional[str] = None
    purchase_rate: Optional[float] = None
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
    shipping_price: Optional[float] = None
    status: Optional[int] = None
    status_shipped: Optional[int] = None
    status_shipped_text: Optional[str] = None
    status_text: Optional[str] = None
    sub_status: Optional[int] = None
    sub_status_text: Optional[str] = None
    supplier_id: Optional[int] = None
    supplier_name: Optional[str] = None
    total_price: Optional[float] = None
    update_time: Optional[str] = None
    ware_house_bak_name: Optional[str] = None
    ware_house_name: Optional[str] = None
    wid: Optional[int] = None


class PurchaserListsItem(LingXingModel):
    """Response item for purchaserLists."""

    address: Optional[str] = None
    contact_phone: Optional[str] = None
    contacter: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    purchaser_id: Optional[int] = None


class SupplierItem(LingXingModel):
    """Response item for Supplier."""

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
    period_config_key: Optional[int] = None
    period_config_text: Optional[str] = None
    prepay_percent: Optional[float] = None
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
    template_id: Optional[int] = None
    template_name: Optional[str] = None
    url: Optional[str] = None
    w_name: Optional[str] = None
    wid: Optional[int] = None

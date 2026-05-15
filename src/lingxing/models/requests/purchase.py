"""Request models for Purchase APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class PurchaseSupplierRequest(LingXingModel):
    """Request for 查询供应商列表.
    
    POST /erp/sc/data/local_inventory/supplier
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class PurchaseSupplierEditRequestPaymentAccountGroupItem(LingXingModel):
    name: str  # 账户名称
    account_name: str  # 户名
    bank_name: str  # 开户行
    account_id: str  # 账号
    is_default: Optional[int] = None  # 是否默认 0=>否 1=>是
    is_open: Optional[int] = None  # 是否开启 0=>否 1=>是
    remark: Optional[str] = None  # 备注
    key: Optional[str] = None  # 编辑时必须
    version: Optional[str] = None  # 编辑时必须

class PurchaseSupplierEditRequest(LingXingModel):
    """Request for 添加/修改供应商.
    
    POST /erp/sc/routing/storage/supplier/edit
    """
    supplier_id: Optional[str] = None  # 客户供应商id,为空或者对应的值不存在时，取sys_supplier_id【已停用】
    sys_supplier_id: Optional[int] = None  # 系统供应商id，取该值且该值为空时，新增供应商
    supplier_name: str  # 供应商名称
    supplier_code: Optional[str] = None  # 供应商编码【供应商代码只支持数字、英文字母、英文句号、-】
    employees: Optional[int] = None  # 员工数： 1=>少于50人 2=>50-150人 3=>150-500人 4=>500-1000人 5 =>1000人以上
    url: Optional[str] = None  # 供应商网址
    contact_person: str  # 联系人 备注：支持传空值
    contact_number: str  # 联系电话 备注：支持传空值
    qq: Optional[str] = None  # QQ
    email: Optional[str] = None  # email
    fax: Optional[str] = None  # 传真
    account_name: Optional[str] = None  # 户名
    open_bank: Optional[str] = None  # 开户行
    bank_card_number: Optional[str] = None  # 银行卡号
    address: Optional[str] = None  # 详细地址
    remark: Optional[str] = None  # 备注
    level: Optional[int] = None  # 级别： 1=>★ 2=>★★ 3=>★★★ 4=>★★★★ 5=>★★★★★,
    settlement_method: int  # 结算方式： 7 现结 8 月结
    settlement_description: Optional[str] = None  # 结算描述
    payment_method: Optional[int] = None  # 支付方式： 1=>网银转账 2=>网上支付
    purchaser: Optional[list] = None  # 跟进人uid，最多支持10个
    credit_code: Optional[str] = None  # 统一社会信用代码
    prepay_percent: Optional[str] = None  # 预付比例
    payment_account_group: Optional[List[PurchaseSupplierEditRequestPaymentAccountGroupItem]] = None


class PurchasePurchaserlistsRequest(LingXingModel):
    """Request for 查询采购方列表.
    
    POST /erp/sc/routing/data/purchaser/lists
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认500


class PurchaseGetpurchaseplansRequest(LingXingModel):
    """Request for 查询采购计划列表.
    
    POST /erp/sc/routing/data/local_inventory/getPurchasePlans
    """
    search_field_time: str  # 时间搜索维度： creator_time 创建时间 expect_arrive_time 预计到货时间 update_time 更新时间
    start_date: str  # 开始日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s
    end_date: str  # 结束日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s
    plan_sns: Optional[list] = None  # 采购计划编号
    is_combo: Optional[int] = None  # 是否为组合商品：0 否，1 是
    is_related_process_plan: Optional[int] = None  # 是否关联加工计划，0：否，1：是
    status: Optional[list] = None  # 状态： 2 待采购 -2 已完成 121 待审批 122 已驳回 -3、124 已作废
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认500，上限500


class PurchaseCreatepurchaseplanRequestDataItem(LingXingModel):
    sid: Optional[str] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    supplier_id: Optional[int] = None  # 供应商id
    sku: str  # sku
    fnsku: Optional[str] = None  # fnsku
    wid: Optional[int] = None  # 仓库id
    purchaser_id: Optional[int] = None  # 采购方id
    expect_arrive_time: Optional[str] = None  # 期望到货时间，格式：Y-m-d
    cg_uid: Optional[int] = None  # 采购员id
    quantity_plan: int  # 计划采购量
    remark: Optional[str] = None  # 产品备注
    options: Optional[dict] = None  # 可选参数
    options__is_auto_fill_fnsku: Optional[int] = None  # 是否自动FNSKU：【默认0】 0 否，1 是
    options__is_auto_fill_store: Optional[int] = None  # 是否自动填充店铺：【默认0】 0 否，1 是

class PurchaseCreatepurchaseplanRequest(LingXingModel):
    """Request for 创建待采购的采购计划.
    
    POST /erp/sc/routing/data/local_inventory/createPurchasePlan
    """
    remark: Optional[str] = None  # 计划备注
    data: List[PurchaseCreatepurchaseplanRequestDataItem]


class PurchasePurchaseOrderListRequest(LingXingModel):
    """Request for 查询采购单列表.
    
    POST /erp/sc/routing/data/local_inventory/purchaseOrderList
    """
    start_date: str  # 开始时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    end_date: str  # 结束时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    search_field_time: Optional[str] = None  # 时间搜索维度： create_time 创建时间【默认值】 expect_arrive_time 预计到货时间 update_time 更新时间
    order_sn: Optional[list] = None  # 采购单号，上限500
    custom_order_sn: Optional[list] = None  # 自定义采购单号，上限500
    purchase_type: Optional[int] = None  # 采购类型，1：普通采购，2:1688采购
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认500，上限500


class PurchaseSetOrdersRequest(LingXingModel):
    """Request for 采购单下单.
    
    POST /erp/sc/routing/purchase/purchase/setOrders
    """
    order_sn: List  # 采购单，对应查询采购单列表接口字段data>>order_sn


class PurchaseCancelRequest(LingXingModel):
    """Request for 作废采购单.
    
    POST /erp/sc/routing/purchase/purchase/cancel
    """
    order_sn: str  # 采购单系统单号
    reason: str  # 作废原因，长度不超过80
    is_cancel_relation: int  # 是否取消关联采购计划：0 否【默认】，1 是


class PurchaseCreatePurchaseOrderRequestProductListItem(LingXingModel):
    sid: Optional[int] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_id: Optional[str] = None  # 亚马逊店铺id【建议使用sid替换】
    marketplace_id: Optional[str] = None  # marketplace_id【建议使用sid替换】
    sku: str  # sku
    fnsku: Optional[str] = None  # fnsku
    price: str  # 单价
    tax_rate: Optional[str] = None  # 税率，范围为[0,100)【当含税为1时，tax_rate为必传字段】
    cases_num: Optional[int] = None  # 箱数
    quantity_per_case: Optional[int] = None  # 单箱数量
    quantity_real: str  # 实际采购量
    expect_arrive_time: Optional[str] = None  # 预计到货时间，格式：Y-m-d
    remark: Optional[str] = None  # 备注
    plan_sn: Optional[str] = None  # 采购计划编号

class PurchaseCreatePurchaseOrderRequestOptionsItem(LingXingModel):
    is_auto_fill_store: Optional[int] = None  # 是否自动填充店铺：【默认0】 0 否，1 是
    is_auto_fill_fnsku: Optional[int] = None  # 是否自动填充fnsku：【默认0】0 否，1 是

class PurchaseCreatePurchaseOrderRequest(LingXingModel):
    """Request for 创建待到货的采购单.
    
    POST /erp/sc/routing/purchase/purchase/createPurchaseOrder
    """
    wid: Optional[int] = None  # 客户仓库id
    sys_wid: Optional[int] = None  # 系统仓库id【与客户仓库id 二选一必填】
    supplier_id: Optional[int] = None  # 客户供应商id
    sys_supplier_id: Optional[int] = None  # 系统供应商id【与客户供应商id 二选一必填】
    custom_order_sn: Optional[str] = None  # 自定义采购单号【不传此字段则系统自动生成采购单号】
    contact_person: Optional[str] = None  # 联系人
    contact_number: Optional[str] = None  # 联系电话
    settlement_method: Optional[int] = None  # 结算方式：7 现结，8 月结
    prepay_percent: Optional[float] = None  # 预付比例（%）
    period_config_key: Optional[str] = None  # 账期配置key
    settlement_description: Optional[str] = None  # 结算描述
    payment_method: Optional[int] = None  # 支付方式：1 网银转账，2 网上支付
    purchase_currency: Optional[str] = None  # 采购币种
    rate: Optional[float] = None  # 汇率
    shipping_currency: Optional[str] = None  # 运费币种
    shipping_price: Optional[float] = None  # 运费
    other_currency: Optional[str] = None  # 其它费用币种
    other_fee: Optional[float] = None  # 其它费用
    fee_part_type: Optional[int] = None  # 费用分摊方式：0 不分摊，1 按金额，2 按数量
    is_tax: Optional[int] = None  # 是否含税：0 否，1 是【当含税为1时，tax_rate为必传字段】
    remark: Optional[str] = None  # 备注
    opt_uid: int  # 采购员uid
    purchaser_id: int  # 采购方id，查询采购方列表 接口对应字段【purchaser_id】
    product_list: PurchaseCreatePurchaseOrderRequestProductListItem
    options: Optional[PurchaseCreatePurchaseOrderRequestOptionsItem] = None


class PurchaseGetpurchasereturnorderlistRequest(LingXingModel):
    """Request for 查询采购退货单列表.
    
    POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList
    """
    search_field_time: Optional[str] = None  # 时间搜索维度： create_time 创建时间【默认值】 last_time 更新时间
    start_date: Optional[str] = None  # 开始时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    end_date: Optional[str] = None  # 结束时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s
    status: Optional[list] = None  # 状态： 121 待审批 122 已驳回 124 已作废（审批作废） 10 已处理 20 已作废（单据作废） 5 待退货
    offset: int  # 分页偏移量
    length: int  # 分页长度，上限500


class PurchaseCreatepurchasereturnorderRequestItemListItem(LingXingModel):
    purchase_order_item_id: int  # 采购单子项id
    return_good_num: Optional[int] = None  # 良品退货量，良品退货量和次品退货量不可同时为空
    return_bad_num: Optional[int] = None  # 次品退货量，良品退货量和次品退货量不可同时为空
    expect_arrive_time: Optional[str] = None  # 预计到货时间，退货补货可设置该字段
    deduction_amount: Optional[float] = None  # 退货金额，退货方式为退货扣款时必填，填写值不可大于扣款数量*含税单价
    remark: Optional[str] = None  # 备注

class PurchaseCreatepurchasereturnorderRequest(LingXingModel):
    """Request for 创建已完成的采购退货单.
    
    POST /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder
    """
    purchase_order_sn: str  # 采购单号
    return_method: int  # 退货方式，1：退货扣款 2：退货补货
    replenish_method: Optional[int] = None  # 补货方式，1：源单补货【退货方式为2时必填】
    fee_part_type: int  # 分摊方式，0：不分摊 1：按金额 2：按数量
    shipping_currency: str  # 退货运费币种，支持CNY、USD，当源单币种为CNY时，运费币种只能为CNY
    shipping_price: Optional[float] = None  # 退货运费
    other_currency: str  # 其他费用币种，支持CNY、USD，当源单币种为CNY时，其他费用币种只能为CNY
    other_fee: Optional[float] = None  # 其他费用
    return_reason: Optional[str] = None  # 退货原因
    remark: Optional[str] = None  # 单据备注
    item_list: List[PurchaseCreatepurchasereturnorderRequestItemListItem]


class PurchaseCancelPurchaseReturnOrderRequest(LingXingModel):
    """Request for 作废采购/委外退货单.
    
    POST /basicOpen/purchase/cancelPurchaseReturnOrder
    """
    order_sn: List  # 采购/委外退货单号
    cancel_reason: str  # 作废原因


class PurchaseChangeorderlistRequest(LingXingModel):
    """Request for 查询采购变更单列表.
    
    POST /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList
    """
    search_field_time: Optional[str] = None  # 筛选时间类型，创建时间:create_time, 更新时间：update_time，不填时默认创建时间
    start_date: Optional[str] = None  # 开始时间
    end_date: Optional[str] = None  # 结束时间
    offset: int  # 分页偏移量
    length: int  # 分页长度
    multi_search_field: Optional[str] = None  # 搜索单号字段，变更单号：order_sn；采购单号：purchase_order_sn
    multi_search_value: Optional[list] = None  # 批量搜索的单号值


class PurchaseCreatepurchasechangeorderRequestProductListItem(LingXingModel):
    id: int  # 采购单子项id
    quantity_real: str  # 实际采购量
    remark: Optional[str] = None  # 备注
    fnsku: Optional[str] = None  # FNSKU
    sid: Optional[int] = None  # 店铺 ，对应查询亚马逊店铺列表接口对应字段【sid】
    quantity_per_case: Optional[int] = None  # 单箱数量
    cases_num: Optional[int] = None  # 箱数
    price: float  # 含税单价
    tax_rate: Optional[float] = None  # 税率
    product_id: int  # 产品
    expect_arrive_time: Optional[str] = None  # 预计到货时间，格式："Y-m-d"

class PurchaseCreatepurchasechangeorderRequestNewProductListItem(LingXingModel):
    quantity_real: int  # 实际采购量
    remark: Optional[str] = None  # 备注
    fnsku: Optional[str] = None  # FNSKU
    sid: Optional[int] = None  # 店铺 ，对应查询亚马逊店铺列表接口对应字段【sid】
    quantity_per_case: Optional[int] = None  # 单箱数量
    cases_num: Optional[int] = None  # 箱数
    price: float  # 含税单价
    tax_rate: Optional[float] = None  # 税率
    product_id: int  # 本地产品id

class PurchaseCreatepurchasechangeorderRequest(LingXingModel):
    """Request for 创建已完成的采购变更单.
    
    POST /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder
    """
    wid: int  # 系统仓库id
    supplier_id: int  # 系统供应商id
    order_sn: str  # 采购单号
    contact_person: Optional[str] = None  # 联系人
    contact_number: Optional[str] = None  # 联系方式
    settlement_method: int  # 结算方式：7 现结，8 月结
    settlement_description: Optional[str] = None  # 结算描述
    shipping_price: Optional[float] = None  # 运费
    payment_method: Optional[int] = None  # 支付方式：1 网银转账，2 网上支付
    purchase_currency: str  # 采购币种
    shipping_currency: str  # 运费币种
    other_currency: str  # 其他费用币种
    rate: float  # 汇率
    other_fee: Optional[float] = None  # 其他费用
    fee_part_type: int  # 费用分配方式：0 不分配，1 按金额，2 按数量
    remark: Optional[str] = None  # 变更单备注
    prepay_percent: Optional[float] = None  # 预付比例
    is_tax: Optional[int] = None  # 是否含税：0 否，1 是
    opt_uid: int  # 采购员U
    product_list: List[PurchaseCreatepurchasechangeorderRequestProductListItem]
    new_product_list: Optional[List[PurchaseCreatepurchasechangeorderRequestNewProductListItem]] = None


class PurchaseGetordersRequest(LingXingModel):
    """Request for 查询委外订单列表.
    
    POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders
    """
    search_field_time: Optional[str] = None  # 日期搜索类型 create_time:创建日期 expect_arrive_time:结束日期
    start_date: Optional[str] = None  # 开始日期（闭区间）
    end_date: Optional[str] = None  # 结束日期（闭区间）
    offset: int  # 分页偏移量
    length: int  # 分页长度，上限500


class PurchaseAddlogisticsRequestItemsItem(LingXingModel):
    logistics_company: str  # 物流商
    logistics_order_no: str  # 物流单号（支持字母、数字、下划线、短划线）

class PurchaseAddlogisticsRequest(LingXingModel):
    """Request for 添加采购单物流信息.
    
    POST /erp/sc/routing/purchase/purchase/addLogistics
    """
    order_sn: str  # 采购单号（待到货或已完成状态）
    items: List[PurchaseAddlogisticsRequestItemsItem]


class PurchasePurchasePlanCancelRequest(LingXingModel):
    """Request for 作废采购计划.
    
    POST /basicOpen/purchase/planCancel
    """
    plan_sn: List  # 计划编号
    reason: str  # 作废原因


class PurchaseOrderModifyRemarkRequest(LingXingModel):
    """Request for 编辑采购单备注.
    
    POST /basicOpen/purchase/orderModifyRemark
    """
    order_sns: List  # 采购单号
    value: str  # 备注内容


class PurchaseSetorderfinishRequest(LingXingModel):
    """Request for 采购单整单结束到货.
    
    POST /basicOpen/purchase/setOrderFinish
    """
    orderSn: List  # 仅支持系统单号，不支持自定义采购单号

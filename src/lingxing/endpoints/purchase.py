"""采购 API endpoints."""
from __future__ import annotations

from ..models.purchase import GetPurchasePlansItem, PurchaseOrderListItem, PurchaserListsItem, SupplierItem
from ._base import BaseEndpoint


class PurchaseEndpoints(BaseEndpoint):
    """领星采购 API (19个接口)."""

    async def cancel(self, **kwargs) -> dict:
        """作废采购单.

POST /erp/sc/routing/purchase/purchase/cancel

Args:
    order_sn: 采购单系统单号 (required), string.
    reason: 作废原因，长度不超过80 (required), string.
    is_cancel_relation: 是否取消关联采购计划：0 否【默认】，1 是 (required), int."""
        resp = await self._post("/erp/sc/routing/purchase/purchase/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_purchase_return_order(self, **kwargs) -> dict:
        """作废采购/委外退货单.

POST /basicOpen/purchase/cancelPurchaseReturnOrder

Args:
    order_sn: 采购/委外退货单号 (required), array.
    cancel_reason: 作废原因 (required), string."""
        resp = await self._post("/basicOpen/purchase/cancelPurchaseReturnOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_order(self, **kwargs) -> dict:
        """创建待到货的采购单.

POST /erp/sc/routing/purchase/purchase/createPurchaseOrder

Args:
    wid: 客户仓库id, int.
    sys_wid: 系统仓库id【与客户仓库id 二选一必填】, int.
    supplier_id: 客户供应商id, int.
    sys_supplier_id: 系统供应商id【与客户供应商id 二选一必填】, int.
    custom_order_sn: 自定义采购单号【不传此字段则系统自动生成采购单号】, string.
    contact_person: 联系人, string.
    contact_number: 联系电话, string.
    settlement_method: 结算方式：7 现结，8 月结, int.
    prepay_percent: 预付比例（%）, double.
    period_config_key: 账期配置key, string.
    settlement_description: 结算描述, string.
    payment_method: 支付方式：1 网银转账，2 网上支付, int.
    purchase_currency: 采购币种, string.
    rate: 汇率, number.
    shipping_currency: 运费币种, string.
    shipping_price: 运费, number.
    other_currency: 其它费用币种, string.
    other_fee: 其它费用, number.
    fee_part_type: 费用分摊方式：0 不分摊，1 按金额，2 按数量, int.
    is_tax: 是否含税：0 否，1 是【当含税为1时，tax_rate为必传字段】, int.
    remark: 备注, string.
    opt_uid: 采购员uid (required), int.
    purchaser_id: 采购方id，查询采购方列表 接口对应字段【purchaser_id】 (required), int.
    options: 创建选项, object."""
        resp = await self._post("/erp/sc/routing/purchase/purchase/createPurchaseOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def order_modify_remark(self, **kwargs) -> list | dict:
        """编辑采购单备注.

POST /basicOpen/purchase/orderModifyRemark

Args:
    order_sns: 采购单号 (required), array.
    value: 备注内容 (required), string."""
        resp = await self._post("/basicOpen/purchase/orderModifyRemark", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_order_list(self, **kwargs) -> list[PurchaseOrderListItem]:
        """查询采购单列表.

POST /erp/sc/routing/data/local_inventory/purchaseOrderList

Args:
    start_date: 开始时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s (required), string.
    end_date: 结束时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s (required), string.
    search_field_time: 时间搜索维度： create_time 创建时间【默认值】 expect_arrive_time 预计到货时间 update_time 更新时间, string.
    order_sn: 采购单号，上限500, array.
    custom_order_sn: 自定义采购单号，上限500, array.
    purchase_type: 采购类型，1：普通采购，2:1688采购, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认500，上限500, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/purchaseOrderList", kwargs if kwargs else None)
        return self._parse_list(resp.data, PurchaseOrderListItem)
    async def purchase_plan_cancel(self, **kwargs) -> dict:
        """作废采购计划.

POST /basicOpen/purchase/planCancel

Args:
    plan_sn: 计划编号 (required), array.
    reason: 作废原因 (required), string."""
        resp = await self._post("/basicOpen/purchase/planCancel", kwargs if kwargs else None)
        return resp.data or {}
    async def set_orders(self, **kwargs) -> list | dict:
        """采购单下单.

POST /erp/sc/routing/purchase/purchase/setOrders

Args:
    order_sn: 采购单，对应查询采购单列表接口字段data>>order_sn (required), array."""
        resp = await self._post("/erp/sc/routing/purchase/purchase/setOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def supplier(self, **kwargs) -> list[SupplierItem]:
        """查询供应商列表.

POST /erp/sc/data/local_inventory/supplier

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int."""
        resp = await self._post("/erp/sc/data/local_inventory/supplier", kwargs if kwargs else None)
        return self._parse_list(resp.data, SupplierItem)
    async def supplier_edit(self, **kwargs) -> dict:
        """添加/修改供应商.

POST /erp/sc/routing/storage/supplier/edit

Args:
    supplier_id: 客户供应商id,为空或者对应的值不存在时，取sys_supplier_id【已停用】, string.
    sys_supplier_id: 系统供应商id，取该值且该值为空时，新增供应商, int.
    supplier_name: 供应商名称 (required), string.
    supplier_code: 供应商编码【供应商代码只支持数字、英文字母、英文句号、-】, string.
    employees: 员工数： 1=>少于50人 2=>50-150人 3=>150-500人 4=>500-1000人 5 =>1000人以上, int.
    url: 供应商网址, string.
    contact_person: 联系人 备注：支持传空值 (required), string.
    contact_number: 联系电话 备注：支持传空值 (required), string.
    qq: QQ, string.
    email: email, string.
    fax: 传真, string.
    account_name: 户名, string.
    open_bank: 开户行, string.
    bank_card_number: 银行卡号, string.
    address: 详细地址, string.
    remark: 备注, string.
    level: 级别： 1=>★ 2=>★★ 3=>★★★ 4=>★★★★ 5=>★★★★★,, int.
    settlement_method: 结算方式： 7 现结 8 月结 (required), int.
    settlement_description: 结算描述, string.
    payment_method: 支付方式： 1=>网银转账 2=>网上支付, int.
    purchaser: 跟进人uid，最多支持10个, array.
    credit_code: 统一社会信用代码, string.
    prepay_percent: 预付比例, string.
    payment_account_group: 收款账户列表, array."""
        resp = await self._post("/erp/sc/routing/storage/supplier/edit", kwargs if kwargs else None)
        return resp.data or {}
    async def add_logistics(self, **kwargs) -> dict:
        """添加采购单物流信息.

POST /erp/sc/routing/purchase/purchase/addLogistics

Args:
    order_sn: 采购单号（待到货或已完成状态） (required), string.
    items: 物流信息 (required), array."""
        resp = await self._post("/erp/sc/routing/purchase/purchase/addLogistics", kwargs if kwargs else None)
        return resp.data or {}
    async def change_order_list(self, **kwargs) -> list | dict:
        """查询采购变更单列表.

POST /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList

Args:
    search_field_time: 筛选时间类型，创建时间:create_time, 更新时间：update_time，不填时默认创建时间, string.
    start_date: 开始时间, string.
    end_date: 结束时间, string.
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int.
    multi_search_field: 搜索单号字段，变更单号：order_sn；采购单号：purchase_order_sn, string.
    multi_search_value: 批量搜索的单号值, array."""
        resp = await self._post("/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_purchase_change_order(self, **kwargs) -> dict:
        """创建已完成的采购变更单.

POST /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder

Args:
    wid: 系统仓库id (required), int.
    supplier_id: 系统供应商id (required), int.
    order_sn: 采购单号 (required), string.
    contact_person: 联系人, string.
    contact_number: 联系方式, string.
    settlement_method: 结算方式：7 现结，8 月结 (required), int.
    settlement_description: 结算描述, string.
    shipping_price: 运费, number.
    payment_method: 支付方式：1 网银转账，2 网上支付, int.
    purchase_currency: 采购币种 (required), string.
    shipping_currency: 运费币种 (required), string.
    other_currency: 其他费用币种 (required), string.
    rate: 汇率 (required), number.
    other_fee: 其他费用, number.
    fee_part_type: 费用分配方式：0 不分配，1 按金额，2 按数量 (required), int.
    remark: 变更单备注, string.
    prepay_percent: 预付比例, number.
    is_tax: 是否含税：0 否，1 是, int.
    opt_uid: 采购员U (required), int.
    product_list: 采购单子项 (required), array.
    new_product_list: 新增采购单子项, array."""
        resp = await self._post("/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_plan(self, **kwargs) -> dict:
        """创建待采购的采购计划.

POST /erp/sc/routing/data/local_inventory/createPurchasePlan

Args:
    remark: 计划备注, string.
    data: 产品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/createPurchasePlan", kwargs if kwargs else None)
        return resp.data or {}
    async def create_purchase_return_order(self, **kwargs) -> dict:
        """创建已完成的采购退货单.

POST /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder

Args:
    purchase_order_sn: 采购单号 (required), string.
    return_method: 退货方式，1：退货扣款 2：退货补货 (required), int.
    replenish_method: 补货方式，1：源单补货【退货方式为2时必填】, int.
    fee_part_type: 分摊方式，0：不分摊 1：按金额 2：按数量 (required), int.
    shipping_currency: 退货运费币种，支持CNY、USD，当源单币种为CNY时，运费币种只能为CNY (required), string.
    shipping_price: 退货运费, number.
    other_currency: 其他费用币种，支持CNY、USD，当源单币种为CNY时，其他费用币种只能为CNY (required), string.
    other_fee: 其他费用, number.
    return_reason: 退货原因, string.
    remark: 单据备注, string.
    item_list: 退货产品 (required), array."""
        resp = await self._post("/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_orders(self, **kwargs) -> list | dict:
        """查询委外订单列表.

POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders

Args:
    search_field_time: 日期搜索类型 create_time:创建日期 expect_arrive_time:结束日期, string.
    start_date: 开始日期（闭区间）, string.
    end_date: 结束日期（闭区间）, string.
    offset: 分页偏移量 (required), int.
    length: 分页长度，上限500 (required), int."""
        resp = await self._post("/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_purchase_plans(self, **kwargs) -> list[GetPurchasePlansItem]:
        """查询采购计划列表.

POST /erp/sc/routing/data/local_inventory/getPurchasePlans

Args:
    search_field_time: 时间搜索维度： creator_time 创建时间 expect_arrive_time 预计到货时间 update_time 更新时间 (required), string.
    start_date: 开始日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s (required), string.
    end_date: 结束日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s (required), string.
    plan_sns: 采购计划编号, array.
    is_combo: 是否为组合商品：0 否，1 是, int.
    is_related_process_plan: 是否关联加工计划，0：否，1：是, int.
    status: 状态： 2 待采购 -2 已完成 121 待审批 122 已驳回 -3、124 已作废, array.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认500，上限500, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getPurchasePlans", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetPurchasePlansItem)
    async def get_purchase_return_order_list(self, **kwargs) -> list | dict:
        """查询采购退货单列表.

POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList

Args:
    search_field_time: 时间搜索维度： create_time 创建时间【默认值】 last_time 更新时间, string.
    start_date: 开始时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 结束时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    status: 状态： 121 待审批 122 已驳回 124 已作废（审批作废） 10 已处理 20 已作废（单据作废） 5 待退货, array.
    offset: 分页偏移量 (required), int.
    length: 分页长度，上限500 (required), int."""
        resp = await self._post("/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchaser_lists(self, **kwargs) -> tuple[list[PurchaserListsItem], int]:
        """查询采购方列表.

POST /erp/sc/routing/data/purchaser/lists

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认500, int."""
        resp = await self._post("/erp/sc/routing/data/purchaser/lists", kwargs if kwargs else None)
        return self._parse_page(resp.data, PurchaserListsItem)
    async def set_order_finish(self, **kwargs) -> list | dict:
        """采购单整单结束到货.

POST /basicOpen/purchase/setOrderFinish

Args:
    orderSn: 仅支持系统单号，不支持自定义采购单号 (required), array."""
        resp = await self._post("/basicOpen/purchase/setOrderFinish", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

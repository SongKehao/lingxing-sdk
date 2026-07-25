"""采购 API endpoints."""

from __future__ import annotations

from typing import Any

from ..models.responses.purchase import (
    GetPurchasePlansItem,
    LocalInventoryCreatepurchaseplanResponse,
    PurchaseAddLogisticsResponse,
    PurchaseCancelPurchaseReturnOrderResponse,
    PurchaseOrderListItem,
    PurchaseOrderModifyRemarkResponse,
    PurchasePlanCancelResponse,
    PurchasePurchaseCancelResponse,
    PurchasePurchasechangeorderChangeorderlistResponse,
    PurchasePurchasechangeorderCreatepurchasechangeorderResponse,
    PurchasePurchaseCreatepurchaseorderResponse,
    PurchasePurchaseoutsourceorderGetordersResponse,
    PurchasePurchaseReturnOrderCreatepurchasereturnorderResponse,
    PurchasePurchaseReturnOrderGetpurchasereturnorderlistResponse,
    PurchaserListsItem,
    PurchaseSetOrderFinishResponse,
    PurchaseSetOrdersResponse,
    StorageSupplierEditResponse,
    SupplierItem,
)
from ._base import BaseEndpoint


class PurchaseEndpoints(BaseEndpoint):
    """领星采购 API (19个接口)."""

    async def cancel(
        self, order_sn: str = None, reason: str = None, is_cancel_relation: int = None
    ) -> PurchasePurchaseCancelResponse | None:
        """作废采购单.

        POST /erp/sc/routing/purchase/purchase/cancel

        Args:
            order_sn: 采购单系统单号 (required), string.
            reason: 作废原因，长度不超过80 (required), string.
            is_cancel_relation: 是否取消关联采购计划：0 否【默认】，1 是 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase/cancel",
            {
                k: v
                for k, v in {"order_sn": order_sn, "reason": reason, "is_cancel_relation": is_cancel_relation}.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, PurchasePurchaseCancelResponse)

    async def cancel_purchase_return_order(
        self, order_sn: list[str] | None = None, cancel_reason: str = None
    ) -> PurchaseCancelPurchaseReturnOrderResponse | None:
        """作废采购/委外退货单.

        POST /basicOpen/purchase/cancelPurchaseReturnOrder

        Args:
            order_sn: 采购/委外退货单号 (required), array.
            cancel_reason: 作废原因 (required), string."""
        resp = await self._post(
            "/basicOpen/purchase/cancelPurchaseReturnOrder",
            {k: v for k, v in {"order_sn": order_sn, "cancel_reason": cancel_reason}.items() if v is not None},
        )
        return self._parse_one(resp.data, PurchaseCancelPurchaseReturnOrderResponse)

    async def create_purchase_order(
        self,
        wid: int = None,
        sys_wid: int = None,
        supplier_id: int = None,
        sys_supplier_id: int = None,
        custom_order_sn: str = None,
        contact_person: str = None,
        contact_number: str = None,
        settlement_method: int = None,
        prepay_percent: float = None,
        period_config_key: str = None,
        settlement_description: str = None,
        payment_method: int = None,
        purchase_currency: str = None,
        rate: float = None,
        shipping_currency: str = None,
        shipping_price: float = None,
        other_currency: str = None,
        other_fee: float = None,
        fee_part_type: int = None,
        is_tax: int = None,
        remark: str = None,
        opt_uid: int = None,
        purchaser_id: int = None,
        product_list: list[dict[str, Any]] | None = None,
        options: dict[str, Any] | None = None,
    ) -> PurchasePurchaseCreatepurchaseorderResponse | None:
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
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase/createPurchaseOrder",
            {
                k: v
                for k, v in {
                    "wid": wid,
                    "sys_wid": sys_wid,
                    "supplier_id": supplier_id,
                    "sys_supplier_id": sys_supplier_id,
                    "custom_order_sn": custom_order_sn,
                    "contact_person": contact_person,
                    "contact_number": contact_number,
                    "settlement_method": settlement_method,
                    "prepay_percent": prepay_percent,
                    "period_config_key": period_config_key,
                    "settlement_description": settlement_description,
                    "payment_method": payment_method,
                    "purchase_currency": purchase_currency,
                    "rate": rate,
                    "shipping_currency": shipping_currency,
                    "shipping_price": shipping_price,
                    "other_currency": other_currency,
                    "other_fee": other_fee,
                    "fee_part_type": fee_part_type,
                    "is_tax": is_tax,
                    "remark": remark,
                    "opt_uid": opt_uid,
                    "purchaser_id": purchaser_id,
                    "product_list": product_list,
                    "options": options,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, PurchasePurchaseCreatepurchaseorderResponse)

    async def order_modify_remark(
        self, order_sns: list[str] | None = None, value: str = None
    ) -> PurchaseOrderModifyRemarkResponse | list[PurchaseOrderModifyRemarkResponse]:
        """编辑采购单备注.

        POST /basicOpen/purchase/orderModifyRemark

        Args:
            order_sns: 采购单号 (required), array.
            value: 备注内容 (required), string."""
        resp = await self._post(
            "/basicOpen/purchase/orderModifyRemark",
            {k: v for k, v in {"order_sns": order_sns, "value": value}.items() if v is not None},
        )
        return self._parse_one_or_list(resp.data, PurchaseOrderModifyRemarkResponse)

    async def purchase_order_list(
        self,
        start_date: str = None,
        end_date: str = None,
        search_field_time: str = None,
        order_sn: list = None,
        custom_order_sn: list = None,
        purchase_type: int = None,
        offset: int = None,
        length: int = None,
    ) -> list[PurchaseOrderListItem]:
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
        resp = await self._post(
            "/erp/sc/routing/data/local_inventory/purchaseOrderList",
            {
                k: v
                for k, v in {
                    "start_date": start_date,
                    "end_date": end_date,
                    "search_field_time": search_field_time,
                    "order_sn": order_sn,
                    "custom_order_sn": custom_order_sn,
                    "purchase_type": purchase_type,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchaseOrderListItem)

    async def purchase_plan_cancel(
        self, plan_sn: list[str] | None = None, reason: str = None
    ) -> PurchasePlanCancelResponse | None:
        """作废采购计划.

        POST /basicOpen/purchase/planCancel

        Args:
            plan_sn: 计划编号 (required), array.
            reason: 作废原因 (required), string."""
        resp = await self._post(
            "/basicOpen/purchase/planCancel",
            {k: v for k, v in {"plan_sn": plan_sn, "reason": reason}.items() if v is not None},
        )
        return self._parse_one(resp.data, PurchasePlanCancelResponse)

    async def set_orders(
        self, order_sn: list[str] | None = None
    ) -> PurchaseSetOrdersResponse | list[PurchaseSetOrdersResponse]:
        """采购单下单.

        POST /erp/sc/routing/purchase/purchase/setOrders

        Args:
            order_sn: 采购单，对应查询采购单列表接口字段data>>order_sn (required), array."""
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase/setOrders",
            {k: v for k, v in {"order_sn": order_sn}.items() if v is not None},
        )
        return self._parse_one_or_list(resp.data, PurchaseSetOrdersResponse)

    async def supplier(self, offset: int = None, length: int = None) -> list[SupplierItem]:
        """查询供应商列表.

        POST /erp/sc/data/local_inventory/supplier

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/local_inventory/supplier",
            {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_list(resp.data, SupplierItem)

    async def supplier_edit(
        self,
        supplier_id: str = None,
        sys_supplier_id: int = None,
        supplier_name: str = None,
        supplier_code: str = None,
        employees: int = None,
        url: str = None,
        contact_person: str = None,
        contact_number: str = None,
        qq: str = None,
        email: str = None,
        fax: str = None,
        account_name: str = None,
        open_bank: str = None,
        bank_card_number: str = None,
        address: str = None,
        remark: str = None,
        level: int = None,
        settlement_method: int = None,
        settlement_description: str = None,
        payment_method: int = None,
        purchaser: list = None,
        credit_code: str = None,
        prepay_percent: str = None,
        payment_account_group: list = None,
    ) -> StorageSupplierEditResponse | None:
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
        resp = await self._post(
            "/erp/sc/routing/storage/supplier/edit",
            {
                k: v
                for k, v in {
                    "supplier_id": supplier_id,
                    "sys_supplier_id": sys_supplier_id,
                    "supplier_name": supplier_name,
                    "supplier_code": supplier_code,
                    "employees": employees,
                    "url": url,
                    "contact_person": contact_person,
                    "contact_number": contact_number,
                    "qq": qq,
                    "email": email,
                    "fax": fax,
                    "account_name": account_name,
                    "open_bank": open_bank,
                    "bank_card_number": bank_card_number,
                    "address": address,
                    "remark": remark,
                    "level": level,
                    "settlement_method": settlement_method,
                    "settlement_description": settlement_description,
                    "payment_method": payment_method,
                    "purchaser": purchaser,
                    "credit_code": credit_code,
                    "prepay_percent": prepay_percent,
                    "payment_account_group": payment_account_group,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, StorageSupplierEditResponse)

    async def add_logistics(self, order_sn: str = None, items: list = None) -> PurchaseAddLogisticsResponse | None:
        """添加采购单物流信息.

        POST /erp/sc/routing/purchase/purchase/addLogistics

        Args:
            order_sn: 采购单号（待到货或已完成状态） (required), string.
            items: 物流信息 (required), array."""
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase/addLogistics",
            {k: v for k, v in {"order_sn": order_sn, "items": items}.items() if v is not None},
        )
        return self._parse_one(resp.data, PurchaseAddLogisticsResponse)

    async def change_order_list(
        self,
        search_field_time: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
        multi_search_field: str = None,
        multi_search_value: list = None,
    ) -> list[PurchasePurchasechangeorderChangeorderlistResponse]:
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
        resp = await self._post(
            "/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList",
            {
                k: v
                for k, v in {
                    "search_field_time": search_field_time,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                    "multi_search_field": multi_search_field,
                    "multi_search_value": multi_search_value,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchasePurchasechangeorderChangeorderlistResponse)

    async def create_purchase_change_order(
        self,
        wid: int = None,
        supplier_id: int = None,
        order_sn: str = None,
        contact_person: str = None,
        contact_number: str = None,
        settlement_method: int = None,
        settlement_description: str = None,
        shipping_price: float = None,
        payment_method: int = None,
        purchase_currency: str = None,
        shipping_currency: str = None,
        other_currency: str = None,
        rate: float = None,
        other_fee: float = None,
        fee_part_type: int = None,
        remark: str = None,
        prepay_percent: float = None,
        is_tax: int = None,
        opt_uid: int = None,
        product_list: list = None,
        new_product_list: list = None,
    ) -> PurchasePurchasechangeorderCreatepurchasechangeorderResponse | None:
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
        resp = await self._post(
            "/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder",
            {
                k: v
                for k, v in {
                    "wid": wid,
                    "supplier_id": supplier_id,
                    "order_sn": order_sn,
                    "contact_person": contact_person,
                    "contact_number": contact_number,
                    "settlement_method": settlement_method,
                    "settlement_description": settlement_description,
                    "shipping_price": shipping_price,
                    "payment_method": payment_method,
                    "purchase_currency": purchase_currency,
                    "shipping_currency": shipping_currency,
                    "other_currency": other_currency,
                    "rate": rate,
                    "other_fee": other_fee,
                    "fee_part_type": fee_part_type,
                    "remark": remark,
                    "prepay_percent": prepay_percent,
                    "is_tax": is_tax,
                    "opt_uid": opt_uid,
                    "product_list": product_list,
                    "new_product_list": new_product_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, PurchasePurchasechangeorderCreatepurchasechangeorderResponse)

    async def create_purchase_plan(
        self, remark: str = None, data: list = None
    ) -> LocalInventoryCreatepurchaseplanResponse | None:
        """创建待采购的采购计划.

        POST /erp/sc/routing/data/local_inventory/createPurchasePlan

        Args:
            remark: 计划备注, string.
            data: 产品信息 (required), array."""
        resp = await self._post(
            "/erp/sc/routing/data/local_inventory/createPurchasePlan",
            {k: v for k, v in {"remark": remark, "data": data}.items() if v is not None},
        )
        return self._parse_one(resp.data, LocalInventoryCreatepurchaseplanResponse)

    async def create_purchase_return_order(
        self,
        purchase_order_sn: str = None,
        return_method: int = None,
        replenish_method: int = None,
        fee_part_type: int = None,
        shipping_currency: str = None,
        shipping_price: float = None,
        other_currency: str = None,
        other_fee: float = None,
        return_reason: str = None,
        remark: str = None,
        item_list: list = None,
    ) -> PurchasePurchaseReturnOrderCreatepurchasereturnorderResponse | None:
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
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder",
            {
                k: v
                for k, v in {
                    "purchase_order_sn": purchase_order_sn,
                    "return_method": return_method,
                    "replenish_method": replenish_method,
                    "fee_part_type": fee_part_type,
                    "shipping_currency": shipping_currency,
                    "shipping_price": shipping_price,
                    "other_currency": other_currency,
                    "other_fee": other_fee,
                    "return_reason": return_reason,
                    "remark": remark,
                    "item_list": item_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, PurchasePurchaseReturnOrderCreatepurchasereturnorderResponse)

    async def get_orders(
        self,
        search_field_time: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[PurchasePurchaseoutsourceorderGetordersResponse]:
        """查询委外订单列表.

        POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders

        Args:
            search_field_time: 日期搜索类型 create_time:创建日期 expect_arrive_time:结束日期, string.
            start_date: 开始日期（闭区间）, string.
            end_date: 结束日期（闭区间）, string.
            offset: 分页偏移量 (required), int.
            length: 分页长度，上限500 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders",
            {
                k: v
                for k, v in {
                    "search_field_time": search_field_time,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchasePurchaseoutsourceorderGetordersResponse)

    async def get_purchase_plans(
        self,
        search_field_time: str = None,
        start_date: str = None,
        end_date: str = None,
        plan_sns: list = None,
        is_combo: int = None,
        is_related_process_plan: int = None,
        status: list = None,
        sids: list = None,
        offset: int = None,
        length: int = None,
    ) -> list[GetPurchasePlansItem]:
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
        resp = await self._post(
            "/erp/sc/routing/data/local_inventory/getPurchasePlans",
            {
                k: v
                for k, v in {
                    "search_field_time": search_field_time,
                    "start_date": start_date,
                    "end_date": end_date,
                    "plan_sns": plan_sns,
                    "is_combo": is_combo,
                    "is_related_process_plan": is_related_process_plan,
                    "status": status,
                    "sids": sids,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, GetPurchasePlansItem)

    async def get_purchase_return_order_list(
        self,
        search_field_time: str = None,
        start_date: str = None,
        end_date: str = None,
        status: list = None,
        offset: int = None,
        length: int = None,
    ) -> list[PurchasePurchaseReturnOrderGetpurchasereturnorderlistResponse]:
        """查询采购退货单列表.

        POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList

        Args:
            search_field_time: 时间搜索维度： create_time 创建时间【默认值】 last_time 更新时间, string.
            start_date: 开始时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
            end_date: 结束时间，格式：Y-m-d，双闭区间 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
            status: 状态： 121 待审批 122 已驳回 124 已作废（审批作废） 10 已处理 20 已作废（单据作废） 5 待退货, array.
            offset: 分页偏移量 (required), int.
            length: 分页长度，上限500 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList",
            {
                k: v
                for k, v in {
                    "search_field_time": search_field_time,
                    "start_date": start_date,
                    "end_date": end_date,
                    "status": status,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchasePurchaseReturnOrderGetpurchasereturnorderlistResponse)

    async def purchaser_lists(self, offset: int = None, length: int = None) -> tuple[list[PurchaserListsItem], int]:
        """查询采购方列表.

        POST /erp/sc/routing/data/purchaser/lists

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认500, int."""
        resp = await self._post(
            "/erp/sc/routing/data/purchaser/lists",
            {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_page(resp.data, PurchaserListsItem)

    async def set_order_finish(
        self, orderSn: list[str] | None = None
    ) -> PurchaseSetOrderFinishResponse | list[PurchaseSetOrderFinishResponse]:
        """采购单整单结束到货.

        POST /basicOpen/purchase/setOrderFinish

        Args:
            orderSn: 仅支持系统单号，不支持自定义采购单号 (required), array."""
        resp = await self._post(
            "/basicOpen/purchase/setOrderFinish", {k: v for k, v in {"orderSn": orderSn}.items() if v is not None}
        )
        return self._parse_one_or_list(resp.data, PurchaseSetOrderFinishResponse)

"""Purchase API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class PurchaseEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def create(
        self,
        access_token: str,
        opt_uid: int,
        purchaser_id: int,
        product_list: list[Any],
        wid: int | None = None,
        sys_wid: int | None = None,
        supplier_id: int | None = None,
        sys_supplier_id: int | None = None,
        custom_order_sn: str | None = None,
        contact_person: str | None = None,
        contact_number: str | None = None,
        settlement_method: int | None = None,
        prepay_percent: float | None = None,
        period_config_key: str | None = None,
        settlement_description: str | None = None,
        payment_method: int | None = None,
        purchase_currency: str | None = None,
        rate: Any | None = None,
        shipping_currency: str | None = None,
        shipping_price: Any | None = None,
        other_currency: str | None = None,
        other_fee: Any | None = None,
        fee_part_type: int | None = None,
        is_tax: int | None = None,
        remark: str | None = None,
        options: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        创建待到货的采购单

        API: /erp/sc/routing/purchase/purchase/createPurchaseOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 客户仓库id (Optional)
            sys_wid: 系统仓库id【与客户仓库id 二选一必填】 (Optional)
            supplier_id: 客户供应商id (Optional)
            sys_supplier_id: 系统供应商id【与客户供应商id 二选一必填】 (Optional)
            custom_order_sn: 自定义采购单号【不传此字段则系统自动生成采购单号】 (Optional)
            contact_person: 联系人 (Optional)
            contact_number: 联系电话 (Optional)
            settlement_method: 结算方式：7 现结，8 月结 (Optional)
            prepay_percent: 预付比例（%） (Optional)
            period_config_key: 账期配置key (Optional)
            settlement_description: 结算描述 (Optional)
            payment_method: 支付方式：1 网银转账，2 网上支付 (Optional)
            purchase_currency: 采购币种 (Optional)
            rate: 汇率 (Optional)
            shipping_currency: 运费币种 (Optional)
            shipping_price: 运费 (Optional)
            other_currency: 其它费用币种 (Optional)
            other_fee: 其它费用 (Optional)
            fee_part_type: 费用分摊方式：0 不分摊，1 按金额，2 按数量 (Optional)
            is_tax: 是否含税：0 否，1 是【当含税为1时，tax_rate为必传字段】 (Optional)
            remark: 备注 (Optional)
            opt_uid: 采购员uid (Required)
            purchaser_id: 采购方id，查询采购方列表 接口对应字段【purchaser_id】 (Required)
            product_list:  (Required)
            options: 创建选项 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
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
            "options": options
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase/createPurchaseOrder",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        plan_sns: list[Any] | None = None,
        is_combo: int | None = None,
        is_related_process_plan: int | None = None,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询采购计划列表

        API: /erp/sc/routing/data/local_inventory/getPurchasePlans
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s (Required)
            end_date: 结束日期，Y-m-d，闭区间，当筛选update_time时，格式为：Y-m-d H:i:s (Required)
            plan_sns: 采购计划编号 (Optional)
            is_combo: 是否为组合商品：0 否，1 是 (Optional)
            is_related_process_plan: 是否关联加工计划，0：否，1：是 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认500，上限500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "plan_sns": plan_sns,
            "is_combo": is_combo,
            "is_related_process_plan": is_related_process_plan,
            "sids": sids,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/getPurchasePlans",
            method="GET",
            req_body=params
        )



    async def purchase_planCancel(
        self,
        access_token: str,
        plan_sn: list[Any],
        reason: str
    ) -> dict[str, Any]:
        """
        作废采购计划

        API: /basicOpen/purchase/planCancel
        Method: POST

        Args:
            access_token: Access token for authentication
            plan_sn: 计划编号 (Required)
            reason: 作废原因 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_planCancel(token, ...)
            >>> print(result)
        """
        params = {
            "plan_sn": plan_sn,
            "reason": reason
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/purchase/planCancel",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int,
        search_field_time: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        multi_search_field: str | None = None,
        multi_search_value: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询采购变更单列表

        API: /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList
        Method: POST

        Args:
            access_token: Access token for authentication
            search_field_time: 筛选时间类型，创建时间:create_time, 更新时间：update_time，不填时默认创建时间 (Optional)
            start_date: 开始时间 (Optional)
            end_date: 结束时间 (Optional)
            offset: 分页偏移量 (Required)
            length: 分页长度 (Required)
            multi_search_field: 搜索单号字段，变更单号：order_sn；采购单号：purchase_order_sn (Optional)
            multi_search_value: 批量搜索的单号值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "search_field_time": search_field_time,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            "multi_search_field": multi_search_field,
            "multi_search_value": multi_search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList",
            method="POST",
            req_body=params
        )



    async def purchase_orderModifyRemark(
        self,
        access_token: str,
        order_sns: list[Any],
        value: str
    ) -> dict[str, Any]:
        """
        编辑采购单备注

        API: /basicOpen/purchase/orderModifyRemark
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sns: 采购单号 (Required)
            value: 备注内容 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_orderModifyRemark(token, ...)
            >>> print(result)
        """
        params = {
            "order_sns": order_sns,
            "value": value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/purchase/orderModifyRemark",
            method="POST",
            req_body=params
        )



    async def purchase_setOrders(
        self,
        access_token: str,
        order_sn: list[Any]
    ) -> dict[str, Any]:
        """
        采购单下单

        API: /erp/sc/routing/purchase/purchase/setOrders
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 采购单，对应查询采购单列表接口字段data>>order_sn (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_setOrders(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase/setOrders",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        data: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建待采购的采购计划

        API: /erp/sc/routing/data/local_inventory/createPurchasePlan
        Method: POST

        Args:
            access_token: Access token for authentication
            remark: 计划备注 (Optional)
            data: 产品信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "remark": remark,
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/createPurchasePlan",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询采购方列表

        API: /erp/sc/routing/data/purchaser/lists
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/purchaser/lists",
            method="POST",
            req_body=params
        )



    async def purchase_cancel(
        self,
        access_token: str,
        order_sn: str,
        reason: str,
        is_cancel_relation: int
    ) -> dict[str, Any]:
        """
        作废采购单

        API: /erp/sc/routing/purchase/purchase/cancel
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 采购单系统单号 (Required)
            reason: 作废原因，长度不超过80 (Required)
            is_cancel_relation: 是否取消关联采购计划：0 否【默认】，1 是 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_cancel(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "reason": reason,
            "is_cancel_relation": is_cancel_relation
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase/cancel",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询采购退货单列表

        API: /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度，上限500 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList",
            method="GET",
            req_body=params
        )



    async def create_info(
        self,
        access_token: str,
        order_sn: str,
        items: list[Any]
    ) -> dict[str, Any]:
        """
        添加采购单物流信息

        API: /erp/sc/routing/purchase/purchase/addLogistics
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 采购单号（待到货或已完成状态） (Required)
            items: 物流信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_info(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "items": items
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase/addLogistics",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        wid: int,
        supplier_id: int,
        order_sn: str,
        settlement_method: int,
        purchase_currency: str,
        shipping_currency: str,
        other_currency: str,
        rate: Any,
        fee_part_type: int,
        opt_uid: int,
        product_list: list[Any],
        contact_person: str | None = None,
        contact_number: str | None = None,
        settlement_description: str | None = None,
        shipping_price: Any | None = None,
        payment_method: int | None = None,
        other_fee: Any | None = None,
        remark: str | None = None,
        prepay_percent: Any | None = None,
        is_tax: int | None = None,
        new_product_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的采购变更单

        API: /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 系统仓库id (Required)
            supplier_id: 系统供应商id (Required)
            order_sn: 采购单号 (Required)
            contact_person: 联系人 (Optional)
            contact_number: 联系方式 (Optional)
            settlement_method: 结算方式：7 现结，8 月结 (Required)
            settlement_description: 结算描述 (Optional)
            shipping_price: 运费 (Optional)
            payment_method: 支付方式：1 网银转账，2 网上支付 (Optional)
            purchase_currency: 采购币种 (Required)
            shipping_currency: 运费币种 (Required)
            other_currency: 其他费用币种 (Required)
            rate: 汇率 (Required)
            other_fee: 其他费用 (Optional)
            fee_part_type: 费用分配方式：0 不分配，1 按金额，2 按数量 (Required)
            remark: 变更单备注 (Optional)
            prepay_percent: 预付比例 (Optional)
            is_tax: 是否含税：0 否，1 是 (Optional)
            opt_uid: 采购员U (Required)
            product_list: 采购单子项 (Required)
            new_product_list: 新增采购单子项 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
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
            "new_product_list": new_product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder",
            method="POST",
            req_body=params
        )



    async def get_orderlist(
        self,
        access_token: str,
        offset: int,
        length: int,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询委外订单列表

        API: /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期（闭区间） (Optional)
            end_date: 结束日期（闭区间） (Optional)
            offset: 分页偏移量 (Required)
            length: 分页长度，上限500 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderlist(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders",
            method="GET",
            req_body=params
        )



    async def purchase_setOrderFinish(
        self,
        access_token: str,
        orderSn: list[Any]
    ) -> dict[str, Any]:
        """
        采购单整单结束到货

        API: /basicOpen/purchase/setOrderFinish
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 仅支持系统单号，不支持自定义采购单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_setOrderFinish(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/purchase/setOrderFinish",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        supplier_name: str,
        supplier_id: str | None = None,
        sys_supplier_id: int | None = None,
        supplier_code: str | None = None,
        url: str | None = None,
        qq: str | None = None,
        email: str | None = None,
        fax: str | None = None,
        account_name: str | None = None,
        open_bank: str | None = None,
        bank_card_number: str | None = None,
        address: str | None = None,
        remark: str | None = None,
        settlement_description: str | None = None,
        purchaser: list[Any] | None = None,
        credit_code: str | None = None,
        prepay_percent: str | None = None,
        payment_account_group: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        添加修改供应商

        API: /erp/sc/routing/storage/supplier/edit
        Method: POST

        Args:
            access_token: Access token for authentication
            supplier_id: 客户供应商id,为空或者对应的值不存在时，取sys_supplier_id【已停用】 (Optional)
            sys_supplier_id: 系统供应商id，取该值且该值为空时，新增供应商 (Optional)
            supplier_name: 供应商名称 (Required)
            supplier_code: 供应商编码【供应商代码只支持数字、英文字母、英文句号、-】 (Optional)
            url: 供应商网址 (Optional)
            qq: QQ (Optional)
            email: email (Optional)
            fax: 传真 (Optional)
            account_name: 户名 (Optional)
            open_bank: 开户行 (Optional)
            bank_card_number: 银行卡号 (Optional)
            address: 详细地址 (Optional)
            remark: 备注 (Optional)
            settlement_description: 结算描述 (Optional)
            purchaser: 跟进人uid，最多支持10个 (Optional)
            credit_code: 统一社会信用代码 (Optional)
            prepay_percent: 预付比例 (Optional)
            payment_account_group: 收款账户列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "supplier_id": supplier_id,
            "sys_supplier_id": sys_supplier_id,
            "supplier_name": supplier_name,
            "supplier_code": supplier_code,
            "url": url,
            "qq": qq,
            "email": email,
            "fax": fax,
            "account_name": account_name,
            "open_bank": open_bank,
            "bank_card_number": bank_card_number,
            "address": address,
            "remark": remark,
            "settlement_description": settlement_description,
            "purchaser": purchaser,
            "credit_code": credit_code,
            "prepay_percent": prepay_percent,
            "payment_account_group": payment_account_group
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/supplier/edit",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        order_sn: list[Any] | None = None,
        custom_order_sn: list[Any] | None = None,
        purchase_type: int | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询采购单列表

        API: /erp/sc/routing/data/local_inventory/purchaseOrderList
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 采购单号，上限500 (Optional)
            custom_order_sn: 自定义采购单号，上限500 (Optional)
            purchase_type: 采购类型，1：普通采购，2:1688采购 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认500，上限500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "custom_order_sn": custom_order_sn,
            "purchase_type": purchase_type,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/purchaseOrderList",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        purchase_order_sn: str,
        return_method: int,
        fee_part_type: int,
        shipping_currency: str,
        other_currency: str,
        item_list: list[Any],
        replenish_method: int | None = None,
        shipping_price: Any | None = None,
        other_fee: Any | None = None,
        return_reason: str | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的采购退货单

        API: /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            purchase_order_sn: 采购单号 (Required)
            return_method: 退货方式，1：退货扣款 2：退货补货 (Required)
            replenish_method: 补货方式，1：源单补货【退货方式为2时必填】 (Optional)
            fee_part_type: 分摊方式，0：不分摊 1：按金额 2：按数量 (Required)
            shipping_currency: 退货运费币种，支持CNY、USD，当源单币种为CNY时，运费币种只能为CNY (Required)
            shipping_price: 退货运费 (Optional)
            other_currency: 其他费用币种，支持CNY、USD，当源单币种为CNY时，其他费用币种只能为CNY (Required)
            other_fee: 其他费用 (Optional)
            return_reason: 退货原因 (Optional)
            remark: 单据备注 (Optional)
            item_list: 退货产品 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
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
            "item_list": item_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder",
            method="POST",
            req_body=params
        )



    async def purchase_cancelPurchaseReturnOrder(
        self,
        access_token: str,
        order_sn: list[Any],
        cancel_reason: str
    ) -> dict[str, Any]:
        """
        作废采购委外退货单

        API: /basicOpen/purchase/cancelPurchaseReturnOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 采购/委外退货单号 (Required)
            cancel_reason: 作废原因 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.purchase_cancelPurchaseReturnOrder(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "cancel_reason": cancel_reason
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/purchase/cancelPurchaseReturnOrder",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询供应商列表

        API: /erp/sc/data/local_inventory/supplier
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/local_inventory/supplier",
            method="POST",
            req_body=params
        )


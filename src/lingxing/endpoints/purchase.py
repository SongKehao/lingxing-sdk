"""采购管理API端点封装"""

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase

logger = logging.getLogger(__name__)


class PurchaseEndpoints:
    """
    采购管理API端点封装

    封装领星ERP采购管理的API调用，提供简洁的接口方法。

    API端点列表：
    采购单管理:
    - get_purchase_orders: 查询采购单列表
    - create_purchase_order: 创建待到货的采购单
    - set_purchase_orders: 采购单下单（待下单->待到货）
    - update_purchase_order_remark: 编辑采购单备注
    - cancel_purchase_order: 作废采购单
    - add_purchase_order_logistics: 添加采购单物流信息
    - set_purchase_order_finish: 采购单整单结束到货

    采购计划管理:
    - get_purchase_plans: 查询采购计划列表
    - create_purchase_plan: 创建待采购的采购计划
    - cancel_purchase_plan: 作废采购计划

    采购变更单管理:
    - get_purchase_change_orders: 查询采购变更单列表
    - create_purchase_change_order: 创建已完成的采购变更单

    采购退货管理:
    - get_purchase_return_orders: 查询采购退货单列表
    - create_purchase_return_order: 创建已完成的采购退货单
    - cancel_purchase_return_order: 作废采购委外退货单

    委外订单管理:
    - get_outsource_orders: 查询委外订单列表

    采购方管理:
    - get_purchasers: 查询采购方列表

    供应商管理:
    - get_suppliers: 查询供应商列表
    - edit_supplier: 添加修改供应商

    使用示例:
        >>> from lingxing.openapi import OpenApiBase
        >>> from lingxing.endpoints.purchase import PurchaseEndpoints
        >>>
        >>> openapi = OpenApiBase(host, app_id, app_secret)
        >>> token = await openapi.generate_access_token()
        >>> purchase = PurchaseEndpoints(openapi)
        >>> orders = await purchase.get_purchase_orders(token.access_token, start_date, end_date)
    """

    # API路径 - 采购单管理
    PURCHASE_ORDER_LIST = "/erp/sc/routing/data/local_inventory/purchaseOrderList"
    PURCHASE_ORDER_CREATE = "/erp/sc/routing/purchase/purchase/createPurchaseOrder"
    PURCHASE_ORDER_SET_ORDERS = "/erp/sc/routing/purchase/purchase/setOrders"
    PURCHASE_ORDER_MODIFY_REMARK = "/basicOpen/purchase/orderModifyRemark"
    PURCHASE_ORDER_CANCEL = "/erp/sc/routing/purchase/purchase/cancel"
    PURCHASE_ORDER_ADD_LOGISTICS = "/erp/sc/routing/purchase/purchase/addLogistics"
    PURCHASE_ORDER_SET_FINISH = "/basicOpen/purchase/setOrderFinish"

    # API路径 - 采购计划管理
    PURCHASE_PLAN_LIST = "/erp/sc/routing/data/local_inventory/getPurchasePlans"
    PURCHASE_PLAN_CREATE = "/erp/sc/routing/data/local_inventory/createPurchasePlan"
    PURCHASE_PLAN_CANCEL = "/basicOpen/purchase/planCancel"

    # API路径 - 采购变更单管理
    PURCHASE_CHANGE_ORDER_LIST = "/erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList"
    PURCHASE_CHANGE_ORDER_CREATE = "/erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder"

    # API路径 - 采购退货管理
    PURCHASE_RETURN_ORDER_LIST = "/erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList"
    PURCHASE_RETURN_ORDER_CREATE = "/erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder"
    PURCHASE_RETURN_ORDER_CANCEL = "/basicOpen/purchase/cancelPurchaseReturnOrder"

    # API路径 - 委外订单管理
    OUTSOURCE_ORDER_LIST = "/erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders"

    # API路径 - 采购方管理
    PURCHASER_LIST = "/erp/sc/routing/data/purchaser/lists"

    # API路径 - 供应商管理
    SUPPLIER_LIST = "/erp/sc/data/local_inventory/supplier"
    SUPPLIER_EDIT = "/erp/sc/routing/storage/supplier/edit"

    def __init__(self, client: 'OpenApiBase'):
        """
        初始化采购管理端点

        Args:
            client: OpenAPI客户端实例
        """
        self._client = client

    async def get_purchase_orders(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        search_field_time: str = "create_time",
        offset: int = 0,
        length: int = 100,
        order_sn: list[str] | None = None,
        custom_order_sn: list[str] | None = None,
        purchase_type: int | None = None,
        wid: int | None = None,
    ) -> dict[str, Any]:
        """
        查询采购单列表

        API: POST /erp/sc/routing/data/local_inventory/purchaseOrderList

        Args:
            access_token: 访问令牌
            start_date: 开始时间，格式：Y-m-d
            end_date: 结束时间，格式：Y-m-d
            search_field_time: 时间搜索维度：
                - create_time: 创建时间【默认值】
                - expect_arrive_time: 预计到货时间
                - update_time: 更新时间
            offset: 分页偏移量，默认0
            length: 分页长度，默认100，最大500
            order_sn: 采购单号列表，上限500（可选）
            custom_order_sn: 自定义采购单号列表，上限500（可选）
            purchase_type: 采购类型，1=普通采购，2=1688采购（可选）
            wid: 仓库ID（可选）

        Returns:
            Dict包含:
            - records: 采购单列表
            - total: 总数

        采购单字段:
            - purchase_sn: 采购单号
            - custom_purchase_sn: 自定义采购单号
            - wid: 仓库ID
            - wname: 仓库名称
            - supplier_id: 供应商ID
            - supplier_name: 供应商名称
            - purchase_type: 采购类型(1=普通采购,2=1688采购)
            - purchase_type_text: 采购类型文本
            - alibaba_order_sn: 1688订单号
            - sub_status: 子状态
            - sub_status_text: 子状态文本
            - status_id: 单据状态ID
            - status: 单据状态说明
            - total_price: 采购单总金额
            - item_list: 商品明细列表
        """
        logger.debug("Fetching purchase orders: %s ~ %s, offset=%s", start_date, end_date, offset)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "search_field_time": search_field_time,
            "offset": offset,
            "length": length,
        }

        if order_sn:
            req_body["order_sn"] = order_sn
        if custom_order_sn:
            req_body["custom_order_sn"] = custom_order_sn
        if purchase_type is not None:
            req_body["purchase_type"] = purchase_type
        if wid is not None:
            req_body["wid"] = wid

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase orders: %s", resp_result.message)
            return {"records": [], "total": 0}

        # 官方API返回 data 为数组，total 为总数
        data = resp_result.data
        if isinstance(data, list):
            # 直接返回数组
            total = resp_result.raw.get("total", len(data)) if hasattr(resp_result, 'raw') else len(data)
            return {"records": data, "total": total}
        if isinstance(data, dict):
            # 兼容嵌套格式
            return {
                "records": data.get("records", data.get("data", [])),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    async def get_all_purchase_orders(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        search_field_time: str = "create_time",
        **kwargs,
    ) -> list[dict[str, Any]]:
        """
        获取所有采购单（自动分页）

        Args:
            access_token: 访问令牌
            start_date: 开始时间
            end_date: 结束时间
            search_field_time: 搜索时间类型
            **kwargs: 其他筛选参数

        Returns:
            所有采购单列表
        """
        all_records = []
        offset = 0
        page_size = 500

        while True:
            result = await self.get_purchase_orders(
                access_token=access_token,
                start_date=start_date,
                end_date=end_date,
                search_field_time=search_field_time,
                offset=offset,
                length=page_size,
                **kwargs,
            )

            records = result.get("records", [])
            if not records:
                break

            all_records.extend(records)
            logger.info("获取采购单 offset=%s, 累计 %s/%s 条", offset, len(all_records), result.get('total', 0))

            if len(records) < page_size:
                break

            offset += page_size

        return all_records

    # ==================== 采购单管理 ====================

    async def create_purchase_order(  # noqa: PLR0912
        self,
        access_token: str,
        opt_uid: int,
        purchaser_id: int,
        product_list: list[dict[str, Any]],
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
        rate: float | None = None,
        shipping_currency: str | None = None,
        shipping_price: float | None = None,
        other_currency: str | None = None,
        other_fee: float | None = None,
        fee_part_type: int | None = None,
        is_tax: int | None = None,
        remark: str | None = None,
        options: dict[str, int] | None = None,
    ) -> dict[str, Any]:
        """
        创建采购单，状态为"待到货"

        API: POST /erp/sc/routing/purchase/purchase/createPurchaseOrder

        Args:
            access_token: 访问令牌
            opt_uid: 采购员uid（必填）
            purchaser_id: 采购方id（必填）
            product_list: 产品列表（必填），每个产品包含:
                - sku: SKU（必填）
                - price: 单价（必填）
                - quantity_real: 实际采购量（必填）
                - sid: 店铺id（可选）
                - fnsku: FNSKU（可选）
                - tax_rate: 税率（含税时必填）
                - cases_num: 箱数（可选）
                - quantity_per_case: 单箱数量（可选）
                - expect_arrive_time: 预计到货时间 Y-m-d（可选）
                - remark: 备注（可选）
                - plan_sn: 采购计划编号（可选）
            wid: 客户仓库id（与sys_wid二选一）
            sys_wid: 系统仓库id（与wid二选一）
            supplier_id: 客户供应商id（与sys_supplier_id二选一）
            sys_supplier_id: 系统供应商id（与supplier_id二选一）
            custom_order_sn: 自定义采购单号
            contact_person: 联系人
            contact_number: 联系电话
            settlement_method: 结算方式：7 现结，8 月结
            prepay_percent: 预付比例（%）
            period_config_key: 账期配置key
            settlement_description: 结算描述
            payment_method: 支付方式：1 网银转账，2 网上支付
            purchase_currency: 采购币种
            rate: 汇率
            shipping_currency: 运费币种
            shipping_price: 运费
            other_currency: 其它费用币种
            other_fee: 其它费用
            fee_part_type: 费用分摊方式：0 不分摊，1 按金额，2 按数量
            is_tax: 是否含税：0 否，1 是
            remark: 备注
            options: 创建选项，包含:
                - is_auto_fill_store: 是否自动填充店铺 0/1
                - is_auto_fill_fnsku: 是否自动填充fnsku 0/1

        Returns:
            Dict包含:
            - order_sn: 采购单号
            - custom_order_sn: 自定义采购单号
        """
        logger.debug("Creating purchase order for purchaser_id=%s", purchaser_id)

        req_body = {
            "opt_uid": opt_uid,
            "purchaser_id": purchaser_id,
            "product_list": product_list,
        }

        if wid is not None:
            req_body["wid"] = wid
        if sys_wid is not None:
            req_body["sys_wid"] = sys_wid
        if supplier_id is not None:
            req_body["supplier_id"] = supplier_id
        if sys_supplier_id is not None:
            req_body["sys_supplier_id"] = sys_supplier_id
        if custom_order_sn:
            req_body["custom_order_sn"] = custom_order_sn
        if contact_person:
            req_body["contact_person"] = contact_person
        if contact_number:
            req_body["contact_number"] = contact_number
        if settlement_method is not None:
            req_body["settlement_method"] = settlement_method
        if prepay_percent is not None:
            req_body["prepay_percent"] = prepay_percent
        if period_config_key:
            req_body["period_config_key"] = period_config_key
        if settlement_description:
            req_body["settlement_description"] = settlement_description
        if payment_method is not None:
            req_body["payment_method"] = payment_method
        if purchase_currency:
            req_body["purchase_currency"] = purchase_currency
        if rate is not None:
            req_body["rate"] = rate
        if shipping_currency:
            req_body["shipping_currency"] = shipping_currency
        if shipping_price is not None:
            req_body["shipping_price"] = shipping_price
        if other_currency:
            req_body["other_currency"] = other_currency
        if other_fee is not None:
            req_body["other_fee"] = other_fee
        if fee_part_type is not None:
            req_body["fee_part_type"] = fee_part_type
        if is_tax is not None:
            req_body["is_tax"] = is_tax
        if remark:
            req_body["remark"] = remark
        if options:
            req_body["options"] = options

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_CREATE,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to create purchase order: %s", resp_result.message)
            return {"order_sn": None, "custom_order_sn": None}

        return resp_result.data or {}

    async def set_purchase_orders(
        self,
        access_token: str,
        order_sns: list[str],
    ) -> dict[str, Any]:
        """
        采购单下单（将"待下单"状态变更为"待到货"状态）

        API: POST /erp/sc/routing/purchase/purchase/setOrders

        Args:
            access_token: 访问令牌
            order_sns: 采购单号列表

        Returns:
            Dict包含操作结果
        """
        logger.debug("Setting purchase orders: %s", order_sns)

        req_body = {"order_sn": order_sns}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_SET_ORDERS,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to set purchase orders: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True, "data": resp_result.data}

    async def update_purchase_order_remark(
        self,
        access_token: str,
        order_sns: list[str],
        value: str,
    ) -> dict[str, Any]:
        """
        编辑采购单备注

        API: POST /basicOpen/purchase/orderModifyRemark

        Args:
            access_token: 访问令牌
            order_sns: 采购单号列表
            value: 备注内容

        Returns:
            Dict包含操作结果
        """
        logger.debug("Updating purchase order remark for: %s", order_sns)

        req_body = {
            "order_sns": order_sns,
            "value": value,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_MODIFY_REMARK,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to update purchase order remark: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True}

    async def cancel_purchase_order(
        self,
        access_token: str,
        order_sn: str,
        reason: str,
        is_cancel_relation: int = 0,
    ) -> dict[str, Any]:
        """
        作废采购单

        支持作废处于"待审核"、"待下单"、"待到货"、"已完成"状态下的采购单

        API: POST /erp/sc/routing/purchase/purchase/cancel

        Args:
            access_token: 访问令牌
            order_sn: 采购单系统单号
            reason: 作废原因，长度不超过80
            is_cancel_relation: 是否取消关联采购计划：0 否（默认），1 是

        Returns:
            Dict包含操作结果
        """
        logger.debug("Cancelling purchase order: %s", order_sn)

        req_body = {
            "order_sn": order_sn,
            "reason": reason,
            "is_cancel_relation": is_cancel_relation,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_CANCEL,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to cancel purchase order: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True}

    async def add_purchase_order_logistics(
        self,
        access_token: str,
        order_sn: str,
        items: list[dict[str, str]],
    ) -> dict[str, Any]:
        """
        添加采购单物流信息

        支持对"待到货"或"已完成"状态的采购单添加物流信息

        API: POST /erp/sc/routing/purchase/purchase/addLogistics

        Args:
            access_token: 访问令牌
            order_sn: 采购单号（待到货或已完成状态）
            items: 物流信息列表，每项包含:
                - logistics_company: 物流商
                - logistics_order_no: 物流单号

        Returns:
            Dict包含操作结果
        """
        logger.debug("Adding logistics to purchase order: %s", order_sn)

        req_body = {
            "order_sn": order_sn,
            "items": items,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_ADD_LOGISTICS,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to add logistics: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True}

    async def set_purchase_order_finish(
        self,
        access_token: str,
        order_sns: list[str],
    ) -> dict[str, Any]:
        """
        采购单整单结束到货

        API: POST /basicOpen/purchase/setOrderFinish

        Args:
            access_token: 访问令牌
            order_sns: 采购单系统单号列表（不支持自定义采购单号）

        Returns:
            Dict包含操作结果
        """
        logger.debug("Setting purchase order finish: %s", order_sns)

        req_body = {"order_sn": order_sns}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_ORDER_SET_FINISH,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to set purchase order finish: %s", resp_result.message)
            return {"success": False, "message": resp_result.message, "error_details": resp_result.error_details}

        return {"success": True}

    # ==================== 采购计划管理 ====================

    async def get_purchase_plans(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        search_field_time: str = "creator_time",
        plan_sns: list[str] | None = None,
        is_combo: int | None = None,
        is_related_process_plan: int | None = None,
        status: list[int] | None = None,
        sids: list[int] | None = None,
        offset: int = 0,
        length: int = 500,
    ) -> dict[str, Any]:
        """
        查询采购计划列表

        API: POST /erp/sc/routing/data/local_inventory/getPurchasePlans

        Args:
            access_token: 访问令牌
            start_date: 开始日期 Y-m-d
            end_date: 结束日期 Y-m-d
            search_field_time: 时间搜索维度：creator_time(创建时间)、expect_arrive_time(预计到货时间)、update_time(更新时间)
            plan_sns: 采购计划编号列表
            is_combo: 是否为组合商品：0 否，1 是
            is_related_process_plan: 是否关联加工计划：0 否，1 是
            status: 状态列表：2 待采购，-2 已完成，121 待审批，122 已驳回，-3/124 已作废
            sids: 店铺id列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认500，上限500

        Returns:
            Dict包含:
            - records: 采购计划列表
            - total: 总数
        """
        logger.debug("Fetching purchase plans: %s ~ %s", start_date, end_date)

        req_body = {
            "search_field_time": search_field_time,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
        }

        if plan_sns:
            req_body["plan_sns"] = plan_sns
        if is_combo is not None:
            req_body["is_combo"] = is_combo
        if is_related_process_plan is not None:
            req_body["is_related_process_plan"] = is_related_process_plan
        if status:
            req_body["status"] = status
        if sids:
            req_body["sids"] = sids

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_PLAN_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase plans: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("list", data.get("records", [])),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    async def create_purchase_plan(
        self,
        access_token: str,
        data: list[dict[str, Any]],
        remark: str | None = None,
    ) -> dict[str, Any]:
        """
        创建采购计划，状态为"待采购"

        API: POST /erp/sc/routing/data/local_inventory/createPurchasePlan

        Args:
            access_token: 访问令牌
            data: 产品信息列表，每个产品包含:
                - sku: SKU（必填）
                - quantity_plan: 计划采购量（必填）
                - sid: 店铺id（可选）
                - supplier_id: 供应商id（可选）
                - fnsku: FNSKU（可选）
                - wid: 仓库id（可选）
                - purchaser_id: 采购方id（可选）
                - expect_arrive_time: 期望到货时间 Y-m-d（可选）
                - cg_uid: 采购员id（可选）
                - remark: 产品备注（可选）
                - options: 可选参数（is_auto_fill_fnsku, is_auto_fill_store）
            remark: 计划备注

        Returns:
            Dict包含:
            - plan_sn: 计划编号列表
            - ppg_sn: 计划批次号
        """
        logger.debug("Creating purchase plan with %s products", len(data))

        req_body = {"data": data}
        if remark:
            req_body["remark"] = remark

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_PLAN_CREATE,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to create purchase plan: %s", resp_result.message)
            return {"plan_sn": [], "ppg_sn": None}

        return resp_result.data or {}

    async def cancel_purchase_plan(
        self,
        access_token: str,
        plan_sns: list[str],
        reason: str,
    ) -> dict[str, Any]:
        """
        作废采购计划

        支持作废处于"待审批"、"待采购"状态下的采购计划

        API: POST /basicOpen/purchase/planCancel

        Args:
            access_token: 访问令牌
            plan_sns: 计划编号列表
            reason: 作废原因

        Returns:
            Dict包含操作结果
        """
        logger.debug("Cancelling purchase plans: %s", plan_sns)

        req_body = {
            "plan_sn": plan_sns,
            "reason": reason,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_PLAN_CANCEL,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to cancel purchase plan: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True}

    # ==================== 采购变更单管理 ====================

    async def get_purchase_change_orders(
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field_time: str = "create_time",
        multi_search_field: str | None = None,
        multi_search_value: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询采购变更单列表

        API: POST /erp/sc/routing/purchase/purchaseChangeOrder/changeOrderList

        Args:
            access_token: 访问令牌
            start_date: 开始时间 Y-m-d
            end_date: 结束时间 Y-m-d
            search_field_time: 筛选时间类型：create_time(创建时间), update_time(更新时间)
            multi_search_field: 搜索单号字段：order_sn(变更单号), purchase_order_sn(采购单号)
            multi_search_value: 批量搜索的单号值列表
            offset: 分页偏移量
            length: 分页长度

        Returns:
            Dict包含:
            - records: 变更单列表
            - total: 总数
        """
        logger.debug("Fetching purchase change orders")

        req_body = {
            "search_field_time": search_field_time,
            "offset": offset,
            "length": length,
        }

        if start_date:
            req_body["start_date"] = start_date
        if end_date:
            req_body["end_date"] = end_date
        if multi_search_field and multi_search_value:
            req_body["multi_search_field"] = multi_search_field
            req_body["multi_search_value"] = multi_search_value

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_CHANGE_ORDER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase change orders: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("list", data.get("records", [])),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    async def create_purchase_change_order(
        self,
        access_token: str,
        wid: int,
        supplier_id: int,
        order_sn: str,
        settlement_method: int,
        purchase_currency: str,
        shipping_currency: str,
        other_currency: str,
        rate: float,
        fee_part_type: int,
        opt_uid: int,
        product_list: list[dict[str, Any]],
        contact_person: str | None = None,
        contact_number: str | None = None,
        settlement_description: str | None = None,
        shipping_price: float | None = None,
        payment_method: int | None = None,
        other_fee: float | None = None,
        remark: str | None = None,
        prepay_percent: float | None = None,
        is_tax: int | None = None,
        new_product_list: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        创建已完成状态的采购变更单

        创建成功后采购单立即变更

        API: POST /erp/sc/routing/purchase/purchaseChangeOrder/createPurchaseChangeOrder

        Args:
            access_token: 访问令牌
            wid: 系统仓库id（必填）
            supplier_id: 系统供应商id（必填）
            order_sn: 采购单号（必填）
            settlement_method: 结算方式：7 现结，8 月结（必填）
            purchase_currency: 采购币种（必填）
            shipping_currency: 运费币种（必填）
            other_currency: 其他费用币种（必填）
            rate: 汇率（必填）
            fee_part_type: 费用分配方式：0 不分配，1 按金额，2 按数量（必填）
            opt_uid: 采购员UID（必填）
            product_list: 采购单子项列表（必填），每项包含:
                - id: 采购单子项id（必填）
                - quantity_real: 实际采购量（必填）
                - price: 含税单价（必填）
                - product_id: 产品id（必填）
            contact_person: 联系人
            contact_number: 联系方式
            settlement_description: 结算描述
            shipping_price: 运费
            payment_method: 支付方式：1 网银转账，2 网上支付
            other_fee: 其他费用
            remark: 变更单备注
            prepay_percent: 预付比例
            is_tax: 是否含税：0 否，1 是
            new_product_list: 新增采购单子项列表

        Returns:
            Dict包含:
            - order_sn: 采购变更单号
        """
        logger.debug("Creating purchase change order for: %s", order_sn)

        req_body = {
            "wid": wid,
            "supplier_id": supplier_id,
            "order_sn": order_sn,
            "settlement_method": settlement_method,
            "purchase_currency": purchase_currency,
            "shipping_currency": shipping_currency,
            "other_currency": other_currency,
            "rate": rate,
            "fee_part_type": fee_part_type,
            "opt_uid": opt_uid,
            "product_list": product_list,
        }

        if contact_person:
            req_body["contact_person"] = contact_person
        if contact_number:
            req_body["contact_number"] = contact_number
        if settlement_description:
            req_body["settlement_description"] = settlement_description
        if shipping_price is not None:
            req_body["shipping_price"] = shipping_price
        if payment_method is not None:
            req_body["payment_method"] = payment_method
        if other_fee is not None:
            req_body["other_fee"] = other_fee
        if remark:
            req_body["remark"] = remark
        if prepay_percent is not None:
            req_body["prepay_percent"] = prepay_percent
        if is_tax is not None:
            req_body["is_tax"] = is_tax
        if new_product_list:
            req_body["new_product_list"] = new_product_list

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_CHANGE_ORDER_CREATE,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to create purchase change order: %s", resp_result.message)
            return {"order_sn": None}

        return resp_result.data or {}

    # ==================== 采购退货管理 ====================

    async def get_purchase_return_orders(
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field_time: str = "create_time",
        status: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询采购退货单列表

        API: POST /erp/sc/routing/purchase/purchase_return_order/getPurchaseReturnOrderList

        Args:
            access_token: 访问令牌
            start_date: 开始时间 Y-m-d
            end_date: 结束时间 Y-m-d
            search_field_time: 时间搜索维度：create_time(创建时间), last_time(更新时间)
            status: 状态列表：5 待退货，10 已处理，20 已作废，121 待审批，122 已驳回，124 已作废（审批）
            offset: 分页偏移量
            length: 分页长度，上限500

        Returns:
            Dict包含:
            - records: 退货单列表
            - total: 总数
        """
        logger.debug("Fetching purchase return orders")

        req_body = {
            "search_field_time": search_field_time,
            "offset": offset,
            "length": length,
        }

        if start_date:
            req_body["start_date"] = start_date
        if end_date:
            req_body["end_date"] = end_date
        if status:
            req_body["status"] = status

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_RETURN_ORDER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase return orders: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, dict):
            return {
                "records": data.get("list", []),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    async def create_purchase_return_order(
        self,
        access_token: str,
        purchase_order_sn: str,
        return_method: int,
        fee_part_type: int,
        shipping_currency: str,
        other_currency: str,
        item_list: list[dict[str, Any]],
        replenish_method: int | None = None,
        shipping_price: float | None = None,
        other_fee: float | None = None,
        return_reason: str | None = None,
        remark: str | None = None,
    ) -> dict[str, Any]:
        """
        创建采购退货单，状态为"已完成"

        API: POST /erp/sc/routing/purchase/purchase_return_order/createPurchaseReturnOrder

        Args:
            access_token: 访问令牌
            purchase_order_sn: 采购单号（必填）
            return_method: 退货方式：1 退货扣款，2 退货补货（必填）
            fee_part_type: 分摊方式：0 不分摊，1 按金额，2 按数量（必填）
            shipping_currency: 退货运费币种（必填）
            other_currency: 其他费用币种（必填）
            item_list: 退货产品列表（必填），每项包含:
                - purchase_order_item_id: 采购单子项id（必填）
                - return_good_num: 良品退货量（可选，与次品退货量不可同时为空）
                - return_bad_num: 次品退货量（可选）
                - deduction_amount: 退货金额（退货扣款时必填）
                - expect_arrive_time: 预计到货时间（退货补货时可设置）
                - remark: 备注
            replenish_method: 补货方式：1 源单补货（退货方式为2时必填）
            shipping_price: 退货运费
            other_fee: 其他费用
            return_reason: 退货原因
            remark: 单据备注

        Returns:
            Dict包含:
            - order_sn: 采购退货单号
        """
        logger.debug("Creating purchase return order for: %s", purchase_order_sn)

        req_body = {
            "purchase_order_sn": purchase_order_sn,
            "return_method": return_method,
            "fee_part_type": fee_part_type,
            "shipping_currency": shipping_currency,
            "other_currency": other_currency,
            "item_list": item_list,
        }

        if replenish_method is not None:
            req_body["replenish_method"] = replenish_method
        if shipping_price is not None:
            req_body["shipping_price"] = shipping_price
        if other_fee is not None:
            req_body["other_fee"] = other_fee
        if return_reason:
            req_body["return_reason"] = return_reason
        if remark:
            req_body["remark"] = remark

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_RETURN_ORDER_CREATE,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to create purchase return order: %s", resp_result.message)
            return {"order_sn": None}

        return resp_result.data or {}

    async def cancel_purchase_return_order(
        self,
        access_token: str,
        order_sns: list[str],
        cancel_reason: str,
    ) -> dict[str, Any]:
        """
        作废采购/委外退货单

        API: POST /basicOpen/purchase/cancelPurchaseReturnOrder

        Args:
            access_token: 访问令牌
            order_sns: 采购/委外退货单号列表
            cancel_reason: 作废原因

        Returns:
            Dict包含操作结果
        """
        logger.debug("Cancelling purchase return orders: %s", order_sns)

        req_body = {
            "order_sn": order_sns,
            "cancel_reason": cancel_reason,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_RETURN_ORDER_CANCEL,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to cancel purchase return order: %s", resp_result.message)
            return {"success": False, "message": resp_result.message}

        return {"success": True}

    # ==================== 委外订单管理 ====================

    async def get_outsource_orders(
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field_time: str = "create_time",
        offset: int = 0,
        length: int = 500,
    ) -> dict[str, Any]:
        """
        查询委外订单列表

        API: POST /erp/sc/routing/purchase/purchaseOutsourceOrder/getOrders

        Args:
            access_token: 访问令牌
            start_date: 开始日期（闭区间）Y-m-d
            end_date: 结束日期（闭区间）Y-m-d
            search_field_time: 日期搜索类型：create_time(创建日期), expect_arrive_time(结束日期)
            offset: 分页偏移量
            length: 分页长度，上限500

        Returns:
            Dict包含:
            - records: 委外订单列表
            - total: 总数
        """
        logger.debug("Fetching outsource orders")

        req_body = {
            "search_field_time": search_field_time,
            "offset": offset,
            "length": length,
        }

        if start_date:
            req_body["start_date"] = start_date
        if end_date:
            req_body["end_date"] = end_date

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.OUTSOURCE_ORDER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch outsource orders: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, dict):
            return {
                "records": data.get("list", []),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    # ==================== 采购方管理 ====================

    async def get_purchasers(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 500,
    ) -> dict[str, Any]:
        """
        查询采购方列表

        API: POST /erp/sc/routing/data/purchaser/lists

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认500

        Returns:
            Dict包含:
            - records: 采购方列表
            - total: 总数
        """
        logger.debug("Fetching purchasers")

        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchasers: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, dict):
            return {
                "records": data.get("list", []),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    # ==================== 供应商管理 ====================

    async def get_suppliers(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 1000,
    ) -> dict[str, Any]:
        """
        查询供应商列表

        API: POST /erp/sc/data/local_inventory/supplier

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000

        Returns:
            Dict包含:
            - records: 供应商列表
            - total: 总数
        """
        logger.debug("Fetching suppliers")

        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.SUPPLIER_LIST,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch suppliers: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("list", data.get("records", [])),
                "total": data.get("total", 0),
            }

        return {"records": [], "total": 0}

    async def edit_supplier(  # noqa: PLR0912
        self,
        access_token: str,
        supplier_name: str,
        contact_person: str,
        contact_number: str,
        settlement_method: int,
        sys_supplier_id: int | None = None,
        supplier_code: str | None = None,
        employees: int | None = None,
        url: str | None = None,
        qq: str | None = None,
        email: str | None = None,
        fax: str | None = None,
        account_name: str | None = None,
        open_bank: str | None = None,
        bank_card_number: str | None = None,
        address: str | None = None,
        remark: str | None = None,
        level: int | None = None,
        settlement_description: str | None = None,
        payment_method: int | None = None,
        purchaser: list[int] | None = None,
        credit_code: str | None = None,
        prepay_percent: str | None = None,
        payment_account_group: list[dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """
        添加/修改供应商信息

        API: POST /erp/sc/routing/storage/supplier/edit

        Args:
            access_token: 访问令牌
            supplier_name: 供应商名称（必填）
            contact_person: 联系人（必填，支持传空值）
            contact_number: 联系电话（必填，支持传空值）
            settlement_method: 结算方式：7 现结，8 月结（必填）
            sys_supplier_id: 系统供应商id（修改时必填，新增时不传）
            supplier_code: 供应商编码（只支持数字、英文字母、英文句号、-）
            employees: 员工数：1 少于50人，2 50-150人，3 150-500人，4 500-1000人，5 1000人以上
            url: 供应商网址
            qq: QQ
            email: 邮箱
            fax: 传真
            account_name: 户名
            open_bank: 开户行
            bank_card_number: 银行卡号
            address: 详细地址
            remark: 备注
            level: 级别：1-5星
            settlement_description: 结算描述
            payment_method: 支付方式：1 网银转账，2 网上支付
            purchaser: 跟进人uid列表，最多10个
            credit_code: 统一社会信用代码
            prepay_percent: 预付比例
            payment_account_group: 收款账户列表

        Returns:
            Dict包含:
            - erp_supplier_id: 系统供应商ID
        """
        logger.debug("Editing supplier: %s", supplier_name)

        req_body = {
            "supplier_name": supplier_name,
            "contact_person": contact_person,
            "contact_number": contact_number,
            "settlement_method": settlement_method,
        }

        if sys_supplier_id is not None:
            req_body["sys_supplier_id"] = sys_supplier_id
        if supplier_code:
            req_body["supplier_code"] = supplier_code
        if employees is not None:
            req_body["employees"] = employees
        if url:
            req_body["url"] = url
        if qq:
            req_body["qq"] = qq
        if email:
            req_body["email"] = email
        if fax:
            req_body["fax"] = fax
        if account_name:
            req_body["account_name"] = account_name
        if open_bank:
            req_body["open_bank"] = open_bank
        if bank_card_number:
            req_body["bank_card_number"] = bank_card_number
        if address:
            req_body["address"] = address
        if remark:
            req_body["remark"] = remark
        if level is not None:
            req_body["level"] = level
        if settlement_description:
            req_body["settlement_description"] = settlement_description
        if payment_method is not None:
            req_body["payment_method"] = payment_method
        if purchaser:
            req_body["purchaser"] = purchaser
        if credit_code:
            req_body["credit_code"] = credit_code
        if prepay_percent:
            req_body["prepay_percent"] = prepay_percent
        if payment_account_group:
            req_body["payment_account_group"] = payment_account_group

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.SUPPLIER_EDIT,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to edit supplier: %s", resp_result.message)
            return {"erp_supplier_id": None, "error": resp_result.message}

        return resp_result.data or {}


__all__ = ['PurchaseEndpoints']

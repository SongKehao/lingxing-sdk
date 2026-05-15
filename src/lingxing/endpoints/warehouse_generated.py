"""Warehouse API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class WarehouseEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def create(
        self,
        access_token: str,
        type: int,
        wid: int,
        remark: str,
        list: list[Any]
    ) -> dict[str, Any]:
        """
        创建已完成的成本补录单

        API: /erp/sc/routing/inventoryReceipt/CostChangeOrder/finishCostChangeOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            type: 补录类型—只支持入库成本(1) (Required)
            wid: 仓库ID (Required)
            remark: 备注 (Required)
            list: 成本补录子项 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "type": type,
            "wid": wid,
            "remark": remark,
            "list": list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/CostChangeOrder/finishCostChangeOrder",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        wid: str | None = None,
        to_wid: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int | None = None,
        page_size: int | None = None
    ) -> dict[str, Any]:
        """
        查询调拨单列表

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList
        Method: GET

        Args:
            access_token: Access token for authentication
            wid: 出库仓库id，多个以英文逗号分隔 (Optional)
            to_wid: 入库仓库id，多个以英文逗号分隔 (Optional)
            start_date: 开始日期，格式：Y-m-d，只有和结束日期同时有值才会生效 (Optional)
            end_date: 结束日期，格式：Y-m-d，只有和开始日期同时有值才会生效 (Optional)
            page: 当前页码，默认1 (Optional)
            page_size: 分页条数，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "to_wid": to_wid,
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList",
            method="GET",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        taskNo: str | None = None
    ) -> dict[str, Any]:
        """
        查询调整单确认调整异步结果

        API: /basicOpen/adjustOrder/adjust/getAdjustStatus
        Method: GET

        Args:
            access_token: Access token for authentication
            taskNo: 异步任务编号 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "taskNo": taskNo
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/adjustOrder/adjust/getAdjustStatus",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        product_list: list[Any],
        wid: int | None = None,
        sys_wid: int | None = None,
        to_wid: int | None = None,
        sys_to_wid: int | None = None,
        freight_fee: str | None = None,
        other_fee: str | None = None,
        remark: str | None = None,
        predict_time: str | None = None,
        out_available_bin: list[Any] | None = None,
        out_inferior_bin: list[Any] | None = None,
        to_available_bin: list[Any] | None = None,
        to_inferior_bin: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        创建待收货已完成的调拨单

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 客户出库仓库id（与系统仓库出库id任一必填，优先取客户出库仓库id） (Optional)
            sys_wid: 系统仓库出库id（与客户仓库出库id任一必填，优先取客户出库仓库id） (Optional)
            to_wid: 客户入库仓库id（与系统仓库入库id任一必填，优先取客户入库仓库id） (Optional)
            sys_to_wid: 系统仓库入库id（与客户仓库入库id任一必填，优先取客户入库仓库id） (Optional)
            freight_fee: 运费 (Optional)
            other_fee: 其他费用 (Optional)
            remark: 备注 (Optional)
            predict_time: 预计到货时间，格式：Y-m-d (Optional)
            product_list:  (Required)
            out_available_bin: 出库可用仓位列表 (Optional)
            out_inferior_bin: 出库次品仓位列表 (Optional)
            to_available_bin: 入库可用仓位列表 (Optional)
            to_inferior_bin: 入库次品仓位列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "sys_wid": sys_wid,
            "to_wid": to_wid,
            "sys_to_wid": sys_to_wid,
            "freight_fee": freight_fee,
            "other_fee": other_fee,
            "remark": remark,
            "predict_time": predict_time,
            "product_list": product_list,
            "out_available_bin": out_available_bin,
            "out_inferior_bin": out_inferior_bin,
            "to_available_bin": to_available_bin,
            "to_inferior_bin": to_inferior_bin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder",
            method="POST",
            req_body=params
        )



    async def adjust_setAdjust(
        self,
        access_token: str,
        orderSn: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        调整单确认调整

        API: /basicOpen/adjustOrder/adjust/setAdjust
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 调整单单号 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.adjust_setAdjust(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/adjustOrder/adjust/setAdjust",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        sys_wid: int,
        sys_to_wid: int,
        out_bin_type: str,
        product_list: list[Any],
        freight_fee: str | None = None,
        other_fee: str | None = None,
        fee_part_type: int | None = None,
        remark: str | None = None,
        predict_time: str | None = None,
        type: str | None = None
    ) -> dict[str, Any]:
        """
        创建待调拨的调拨单

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            sys_wid: 系统出库仓库ID (Required)
            sys_to_wid: 系统入库仓库ID (Required)
            freight_fee: 运费 (Optional)
            other_fee: 其他费用 (Optional)
            fee_part_type: 费用分摊方式：0 不分摊【默认值】，2 按sku数量分摊，3 按重量，4 按体积，5 按自定义 (Optional)
            remark: 备注 (Optional)
            predict_time: 预计到货时间 (Optional)
            type: 默认为2-标准调拨 (Optional)
            out_bin_type: 默认0 出库仓位不为空时必传1 (Required)
            product_list: 产品明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "sys_to_wid": sys_to_wid,
            "freight_fee": freight_fee,
            "other_fee": other_fee,
            "fee_part_type": fee_part_type,
            "remark": remark,
            "predict_time": predict_time,
            "type": type,
            "out_bin_type": out_bin_type,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        wid: int | None = None,
        order_sn: str | None = None,
        inbound_idempotent_code: str | None = None
    ) -> dict[str, Any]:
        """
        查询入库单列表

        API: /erp/sc/routing/storage/inbound/getOrders
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            wid: 系统仓库id (Optional)
            order_sn: 入库单单号，多个使用英文逗号分隔 (Optional)
            inbound_idempotent_code: 客户参考单号，多个使用英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "wid": wid,
            "order_sn": order_sn,
            "inbound_idempotent_code": inbound_idempotent_code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/inbound/getOrders",
            method="GET",
            req_body=params
        )



    async def delete(
        self,
        access_token: str,
        orderSn: list[Any]
    ) -> dict[str, Any]:
        """
        删除调拨单

        API: /basicOpen/storageAllocationList/delete
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 调拨单单号，对应查询调拨单列表接口字段【order_sn】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/storageAllocationList/delete",
            method="POST",
            req_body=params
        )



    async def inbound_setInbound(
        self,
        access_token: str,
        orderSn: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        入库单确认入库

        API: /basicOpen/inboundOrder/inbound/setInbound
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 入库单单号 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_setInbound(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/inboundOrder/inbound/setInbound",
            method="POST",
            req_body=params
        )



    async def delete(  # noqa: F811
        self,
        access_token: str,
        orderSn: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        删除出库单

        API: /basicOpen/outboundOrder/outbound/delete
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 出库单单号 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/outboundOrder/outbound/delete",
            method="POST",
            req_body=params
        )



    async def inbound_setOrderRevoke(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        撤销入库单

        API: /basicOpen/inboundOrder/inbound/setOrderRevoke
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_setOrderRevoke(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/inboundOrder/inbound/setOrderRevoke",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        order_sn: str | None = None,
        wid: str | None = None,
        page: int | None = None,
        page_size: int | None = None
    ) -> dict[str, Any]:
        """
        查询调整单列表

        API: /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期，格式：Y-m-d (Optional)
            end_date: 结束日期，格式：Y-m-d (Optional)
            order_sn: 调整单号，多个使用英文逗号分隔 (Optional)
            wid: 系统仓库id，多个使用英文逗号分隔 (Optional)
            page: 当前页码，默认1 (Optional)
            page_size: 分页条数，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "order_sn": order_sn,
            "wid": wid,
            "page": page,
            "page_size": page_size
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        sys_wid: int,
        product_list: list[Any],
        wid: str | None = None,
        supplier_id: str | None = None,
        sys_supplier_id: int | None = None,
        order_sn: str | None = None,
        remark: str | None = None,
        ship_fee: str | None = None,
        other_fee: str | None = None,
        inbound_time: str | None = None,
        inbound_idempotent_code: str | None = None
    ) -> dict[str, Any]:
        """
        添加入库单

        API: /erp/sc/routing/storage/storage/orderAdd
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid (Optional)
            sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (Required)
            supplier_id: 自定义供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】 (Optional)
            sys_supplier_id: 系统供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】 (Optional)
            order_sn: 采购单号【对此采购单执行快捷入库】，不支持自定义采购单号 (Optional)
            remark: 单据备注 (Optional)
            ship_fee: 运费 (Optional)
            other_fee: 其它费用 (Optional)
            inbound_time: 自定义入库时间，格式：Y-m-d (Optional)
            inbound_idempotent_code: （入库单）客户参考号, 该字段校验唯一不可重复 (Optional)
            product_list: 产品明细 (Required)

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
            "order_sn": order_sn,
            "remark": remark,
            "ship_fee": ship_fee,
            "other_fee": other_fee,
            "inbound_time": inbound_time,
            "inbound_idempotent_code": inbound_idempotent_code,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/storage/orderAdd",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        wid: str | None = None,
        order_sn: str | None = None,
        idempotent_code: str | None = None
    ) -> dict[str, Any]:
        """
        查询出库单列表

        API: /erp/sc/routing/storage/outbound/getOrders
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            wid: 系统仓库id (Optional)
            order_sn: 出库单单号，多个使用英文逗号分隔 (Optional)
            idempotent_code: 客户参考号，多个使用英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "wid": wid,
            "order_sn": order_sn,
            "idempotent_code": idempotent_code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/outbound/getOrders",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        wid: int,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的换标调整单

        API: /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 系统仓库id (Required)
            remark: 单据备注 (Optional)
            product_list: 调整的产品明细数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder",
            method="POST",
            req_body=params
        )



    async def create_sku(
        self,
        access_token: str,
        wid: int,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的SKU调整单

        API: /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 系统仓库id (Required)
            remark: 单据备注 (Optional)
            product_list: 调整的产品明细数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_sku(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder",
            method="POST",
            req_body=params
        )



    async def StorageAllocation_receiveAllocationOrder(
        self,
        access_token: str,
        orderSnMany: str
    ) -> dict[str, Any]:
        """
        调拨单全部收货

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSnMany: 调拨单号，支持多个，英文逗号分隔 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.StorageAllocation_receiveAllocationOrder(token, ...)
            >>> print(result)
        """
        params = {
            "orderSnMany": orderSnMany
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        获取自定义出库类型

        API: /erp/sc/routing/storage/outbound/getCustomTypes
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/outbound/getCustomTypes",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        wid: int,
        is_display_check: int,
        check_uid: int,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的盘点单

        API: /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 盘点仓库id,对应领星系统的仓库id (Required)
            is_display_check: 是否明盘：0 否，1 是【默认值】 (Required)
            check_uid: 盘点人id (Required)
            remark: 单据备注 (Optional)
            product_list: 盘点明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "is_display_check": is_display_check,
            "check_uid": check_uid,
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder",
            method="POST",
            req_body=params
        )



    async def StorageAllocation_finishReceiveAllocationOrder(
        self,
        access_token: str,
        order_sn: str
    ) -> dict[str, Any]:
        """
        调拨单结束到货

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 调拨单单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.StorageAllocation_finishReceiveAllocationOrder(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        wid: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        search_value: str | None = None,
        page: int | None = None,
        page_size: int | None = None
    ) -> dict[str, Any]:
        """
        查询盘点单列表

        API: /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            wid: 盘点仓库id，多个使用英文逗号分隔 (Optional)
            start_date: 开始日期，格式：Y-m-d (Optional)
            end_date: 结束日期，格式：Y-m-d (Optional)
            search_value: 搜索值 (Optional)
            page: 分页页码，默认1 (Optional)
            page_size: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "start_date": start_date,
            "end_date": end_date,
            "search_value": search_value,
            "page": page,
            "page_size": page_size
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        加工单列表

        API: /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        sys_wid: int,
        product_list: list[Any],
        wid: str | None = None,
        status: int | None = None,
        sys_supplier_id: int | None = None,
        supplier_id: str | None = None,
        idempotent_code: str | None = None,
        remark: str | None = None,
        return_price: Any | None = None,
        other_fee: Any | None = None,
        sys_to_wid: int | None = None,
        to_wid: str | None = None,
        outbound_time: str | None = None
    ) -> dict[str, Any]:
        """
        添加出库单

        API: /erp/sc/routing/storage/storage/orderAddOut
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 自定义仓库ID，wid和sys_wid其中一项必填，都填则优先wid (Optional)
            sys_wid: 系统仓库ID，sys_wid和wid其中一项必填，都填则优先wid (Required)
            status: 新建单据状态：10：待提交，40：已完成【默认值】 (Optional)
            sys_supplier_id: 系统客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id） (Optional)
            supplier_id: 客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id） (Optional)
            idempotent_code: 客户参考号, 该字段校验唯一不可重复 (Optional)
            remark: 单据备注 (Optional)
            return_price: 退货费（退货出库） (Optional)
            other_fee: 其它费用（退货出库） (Optional)
            sys_to_wid: 系统客户目的仓库ID（非退货出库） (Optional)
            to_wid: 客户目的仓库ID（非退货出库） (Optional)
            outbound_time: 自定义出库时间，格式：Y-m-d (Optional)
            product_list: 产品明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "sys_wid": sys_wid,
            "status": status,
            "sys_supplier_id": sys_supplier_id,
            "supplier_id": supplier_id,
            "idempotent_code": idempotent_code,
            "remark": remark,
            "return_price": return_price,
            "other_fee": other_fee,
            "sys_to_wid": sys_to_wid,
            "to_wid": to_wid,
            "outbound_time": outbound_time,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/storage/orderAddOut",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        isPrintCenter: int,
        orderNumbers: str
    ) -> dict[str, Any]:
        """
        查询销售出库单详情

        API: /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers
        Method: GET

        Args:
            access_token: Access token for authentication
            isPrintCenter: 是否需要拣货信息，枚举值：1-是, 0-否 (Required)
            orderNumbers: 系统单号，必填，多个以逗号连接 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "isPrintCenter": isPrintCenter,
            "orderNumbers": orderNumbers
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/wmsOrder/getWmsOrdersByOrderNumbers",
            method="GET",
            req_body=params
        )



    async def outbound_setOrderRevoke(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        撤销出库单

        API: /basicOpen/outboundOrder/outbound/setOrderRevoke
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.outbound_setOrderRevoke(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/outboundOrder/outbound/setOrderRevoke",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        type: int,
        wid: int,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建加工单拆分单

        API: /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            type: 单据类型：1 加工单，2 拆分单 (Required)
            wid: 系统仓库id (Required)
            remark: 备注 (Optional)
            product_list: 产品信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "type": type,
            "wid": wid,
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        撤销调拨单

        API: /basicOpen/storageAllocationList/cancel
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/storageAllocationList/cancel",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        获取自定义入库类型

        API: /erp/sc/routing/storage/inbound/getCustomTypes
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/inbound/getCustomTypes",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        wid: int,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建已完成的数量调整单

        API: /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 系统仓库id (Required)
            remark: 单据备注 (Optional)
            product_list: 调整的产品明细数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder",
            method="POST",
            req_body=params
        )



    async def StorageAllocation_partlyReceiveAllocationOrder(
        self,
        access_token: str,
        order_sn: str,
        product_list: list[Any]
    ) -> dict[str, Any]:
        """
        调拨单分批收货

        API: /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 调拨单单号 (Required)
            product_list: 本次收货的调拨单单据明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.StorageAllocation_partlyReceiveAllocationOrder(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder",
            method="POST",
            req_body=params
        )



    async def outbound_setOutbound(
        self,
        access_token: str,
        orderSn: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        出库单确认出库

        API: /basicOpen/outboundOrder/outbound/setOutbound
        Method: POST

        Args:
            access_token: Access token for authentication
            orderSn: 出库单单号 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.outbound_setOutbound(token, ...)
            >>> print(result)
        """
        params = {
            "orderSn": orderSn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/outboundOrder/outbound/setOutbound",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        order_sn: str,
        search_value: str | None = None,
        sort_type: str | None = None,
        page: int | None = None,
        page_size: int | None = None
    ) -> dict[str, Any]:
        """
        查询盘点单详情

        API: /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail
        Method: GET

        Args:
            access_token: Access token for authentication
            order_sn: 盘点单号 (Required)
            search_value: 搜索值 (Optional)
            sort_type: 排序规则：desc 降序【默认】，asc 升序 (Optional)
            page: 分页页码，默认1【控制 product_list 返回数目】 (Optional)
            page_size: 分页长度，默认20【控制 product_list 返回数目】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "search_value": search_value,
            "sort_type": sort_type,
            "page": page,
            "page_size": page_size
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail",
            method="GET",
            req_body=params
        )



    async def PurchaseReceiptOrder_receive(
        self,
        access_token: str,
        order_sn: str,
        item_list: list[Any],
        expect_arrival_time: str | None = None,
        custom_receive_time: str | None = None,
        logistics_company: str | None = None,
        logistics_order_no: str | None = None,
        shipping_cost: Any | None = None,
        other_fee: Any | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        收货单到货

        API: /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 收货单号 (Required)
            expect_arrival_time: 预计收货时间，不传时默认取自收货单 (Optional)
            custom_receive_time: 自定义收货时间， 自定义日期须早于请求当天日期 (Optional)
            logistics_company: 物流商，不传时默认取自收货单 (Optional)
            logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单 (Optional)
            shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单 (Optional)
            other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单 (Optional)
            remark: 备注，最大支持255个字符，不传时默认取自收货单 (Optional)
            item_list: 收货明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.PurchaseReceiptOrder_receive(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "expect_arrival_time": expect_arrival_time,
            "custom_receive_time": custom_receive_time,
            "logistics_company": logistics_company,
            "logistics_order_no": logistics_order_no,
            "shipping_cost": shipping_cost,
            "other_fee": other_fee,
            "remark": remark,
            "item_list": item_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive",
            method="POST",
            req_body=params
        )



    async def order(
        self,
        access_token: str,
        sid: Any,
        amazonOrderId: str,
        purchaseDateLocal: str,
        data: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        订单退款

        API: /basicOpen/openapi/salesOrder/refundOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id (Required)
            amazonOrderId: 亚马逊订单ID (Required)
            purchaseDateLocal: 订购时间 (Required)
            data:  (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "amazonOrderId": amazonOrderId,
            "purchaseDateLocal": purchaseDateLocal,
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/salesOrder/refundOrder",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        length: int,
        start_time: str,
        end_time: str,
        time_type: str | None = None,
        platform_code: list[Any] | None = None,
        sales_type: int | None = None,
        store_id: list[Any] | None = None,
        wid: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询销售退货单列表

        API: /pb/mp/returns/v2/list
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页记录数 (Required)
            time_type: 搜索时间类型：updateTime 更新时间【不传默认为创建时间】 (Optional)
            start_time: 开始时间，格式：Y-m-d H:i:s (Required)
            end_time: 结束时间，格式：Y-m-d H:i:s (Required)
            platform_code: 平台code (Optional)
            sales_type: 退货类型：1 买家退货，2 物流商退货 (Optional)
            store_id: 店铺id (Optional)
            wid: 系统仓库id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "time_type": time_type,
            "start_time": start_time,
            "end_time": end_time,
            "platform_code": platform_code,
            "sales_type": sales_type,
            "store_id": store_id,
            "wid": wid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/returns/v2/list",
            method="POST",
            req_body=params
        )



    async def PurchaseReceiptOrder_fastReceive(
        self,
        access_token: str,
        order_sn: str,
        item_list: list[Any],
        expect_arrival_time: str | None = None,
        custom_receive_time: str | None = None,
        logistics_company: str | None = None,
        logistics_order_no: str | None = None,
        shipping_cost: Any | None = None,
        other_fee: Any | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        收货单快捷入库

        API: /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 收货单号 (Required)
            expect_arrival_time: 预计收货时间，不传时默认取自收货单 (Optional)
            custom_receive_time: 自定义收货时间， 自定义日期须早于请求当天日期 (Optional)
            logistics_company: 物流商，不传时默认取自收货单 (Optional)
            logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单 (Optional)
            shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单 (Optional)
            other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单 (Optional)
            remark: 备注，最大支持255个字符，不传时默认取自收货单 (Optional)
            item_list: 收货明细 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.PurchaseReceiptOrder_fastReceive(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "expect_arrival_time": expect_arrival_time,
            "custom_receive_time": custom_receive_time,
            "logistics_company": logistics_company,
            "logistics_order_no": logistics_order_no,
            "shipping_cost": shipping_cost,
            "other_fee": other_fee,
            "remark": remark,
            "item_list": item_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        date_type: int | None = None,
        order_sns: str | None = None,
        status: int | None = None,
        wid: str | None = None,
        order_type: int | None = None,
        qc_status: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询收货单列表

        API: /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            date_type: 查询时间类型：1 预计到货时间，2 收货时间，3 创建时间，4 更新时间 (Optional)
            order_sns: 收货单号，多个使用英文逗号分隔 (Optional)
            status: 状态：10 待收货，40 已完成 (Optional)
            wid: 仓库id，多个使用英文逗号分隔 (Optional)
            order_type: 收货类型：1 采购订单，2 委外订单 (Optional)
            qc_status: 质检状态，多个使用英文逗号分隔：0 未质检，1 部分质检，2 完成质检 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认200，上限500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "date_type": date_type,
            "order_sns": order_sns,
            "status": status,
            "wid": wid,
            "order_type": order_type,
            "qc_status": qc_status,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        date_type: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        qc_sns: str | None = None,
        wid: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询质检单列表

        API: /erp/sc/routing/deliveryReceipt/ReceiptOrderQc/getOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            date_type: 查询时间类型：1 质检时间，2 收货时间，3 创建时间 (Optional)
            start_date: 开始时间 (Optional)
            end_date: 结束时间 (Optional)
            qc_sns: 质检单号，多个使用英文逗号分隔 (Optional)
            wid: 仓库id，多个用英文逗号分隔 (Optional)
            offset: 分页偏移量，默认为0 (Optional)
            length: 分页长度，默认为200，上限500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
            "qc_sns": qc_sns,
            "wid": wid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/deliveryReceipt/ReceiptOrderQc/getOrderList",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        list: list[Any]
    ) -> dict[str, Any]:
        """
        创建待收货的收货单

        API: /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            list: 收货数据，支持批量 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "list": list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        qc_sn: str
    ) -> dict[str, Any]:
        """
        查询质检单详情

        API: /basicOpen/qualityInspectionOrder/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            qc_sn: 质检单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "qc_sn": qc_sn
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/qualityInspectionOrder/detail",
            method="POST",
            req_body=params
        )



    async def order_fastStorageIn(
        self,
        access_token: str,
        reqs: list[Any]
    ) -> dict[str, Any]:
        """
        待收货退货单快捷入库

        API: /basicOpen/return/order/fastStorageIn
        Method: POST

        Args:
            access_token: Access token for authentication
            reqs:  (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order_fastStorageIn(token, ...)
            >>> print(result)
        """
        params = {
            "reqs": reqs
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/return/order/fastStorageIn",
            method="POST",
            req_body=params
        )



    async def get_inventorydetail(
        self,
        access_token: str,
        wid: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        sku: str | None = None
    ) -> dict[str, Any]:
        """
        查询仓库库存明细

        API: /erp/sc/routing/data/local_inventory/inventoryDetails
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库id，多个使用英文逗号分隔 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限800 (Optional)
            sku: SKU，单个,（模糊搜索） (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventorydetail(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "offset": offset,
            "length": length,
            "sku": sku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/inventoryDetails",
            method="POST",
            req_body=params
        )



    async def get_fbainventorylist(
        self,
        access_token: str,
        sid: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA库存列表

        API: /erp/sc/routing/fba/fbaStock/fbaList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbainventorylist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/fbaStock/fbaList",
            method="POST",
            req_body=params
        )



    async def get_detail(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        show_zero_stock: int | None = None,
        wids: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询批次明细

        API: /erp/sc/routing/data/local_inventory/getBatchDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限400 (Optional)
            show_zero_stock: 是否显示0库存信息：0 不显示，1 显示 (Optional)
            wids: 仓库id，多个使用英文逗号分隔 (Optional)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_detail(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "show_zero_stock": show_zero_stock,
            "wids": wids,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/getBatchDetailList",
            method="GET",
            req_body=params
        )



    async def get_awdinventorylist(
        self,
        access_token: str,
        search_field: str,
        wids: str | None = None,
        cid: str | None = None,
        bid: str | None = None,
        attribute: int | None = None,
        asin_principal: str | None = None,
        search_value: str | None = None,
        status: str | None = None,
        is_hide_zero_stock: Any | None = None,
        offset: Any | None = None,
        length: Any | None = None
    ) -> dict[str, Any]:
        """
        查询AWD库存列表

        API: /basicOpen/openapi/storage/awdWarehouseDetail
        Method: POST

        Args:
            access_token: Access token for authentication
            wids: 仓库ID列表，使用逗号分隔 (Optional)
            cid: 分类ID列表，使用逗号分隔 (Optional)
            bid: 品牌ID列表，使用逗号分隔 (Optional)
            attribute: 属性值 (Optional)
            asin_principal: ASIN负责人UID列表，使用逗号分隔 * 0、负责人为空 (Optional)
            search_field: 搜索字段，指定进行搜索的列 sku product_name seller_sku fnsku asin parent_asin spu spu_name (Required)
            search_value: 搜索值 (Optional)
            status: 状态列表，使用逗号分隔 0、停售 1、在售 (Optional)
            is_hide_zero_stock: 是否隐藏零库存 0、不隐藏 1、隐藏 (Optional)
            offset: 分页偏移量 (Optional)
            length: 分页长度 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_awdinventorylist(token, ...)
            >>> print(result)
        """
        params = {
            "wids": wids,
            "cid": cid,
            "bid": bid,
            "attribute": attribute,
            "asin_principal": asin_principal,
            "search_field": search_field,
            "search_value": search_value,
            "status": status,
            "is_hide_zero_stock": is_hide_zero_stock,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/storage/awdWarehouseDetail",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        wid: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询仓位流水

        API: /erp/sc/routing/data/local_inventory/wareHouseBinStatement
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库ID，多个仓库ID用英文逗号,分隔，传或者传空则默认所有仓库 (Optional)
            start_date: 操作开始时间，Y-m-d，闭区间，联合结束时间使用 (Optional)
            end_date: 操作结束时间，Y-m-d，开区间，联合开始时间使用 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/wareHouseBinStatement",
            method="POST",
            req_body=params
        )



    async def get_fbainventorylist_v2(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        search_value: str | None = None,
        cid: str | None = None,
        bid: str | None = None,
        attribute: str | None = None,
        senior_search_list: str | None = None,
        query_fba_storage_quantity_list: bool | None = None
    ) -> dict[str, Any]:
        """
        查询FBA库存列表-v2

        API: /basicOpen/openapi/storage/fbaWarehouseDetail
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20,取值范围[20,200] (Optional)
            search_value: 搜索值 (Optional)
            cid: 分类 (Optional)
            bid: 品牌 (Optional)
            attribute: 属性 (Optional)
            senior_search_list: 高级搜索列表，详情见附加说明 (Optional)
            query_fba_storage_quantity_list: true 是、false 否；默认false，如果传入true,则出参数据中的欧洲共享仓会将出参字段-fba_storage_quantity_list的值返回 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbainventorylist_v2(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "search_value": search_value,
            "cid": cid,
            "bid": bid,
            "attribute": attribute,
            "senior_search_list": senior_search_list,
            "query_fba_storage_quantity_list": query_fba_storage_quantity_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/storage/fbaWarehouseDetail",
            method="POST",
            req_body=params
        )



    async def get_inventorydetail(  # noqa: F811
        self,
        access_token: str,
        wid: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询仓位库存明细

        API: /erp/sc/routing/data/local_inventory/inventoryBinDetails
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库id，多个仓库用英文逗号分隔，默认所有仓库 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 ，上限500 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventorydetail(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/inventoryBinDetails",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        search_value: str | None = None,
        wid_list: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询批次流水

        API: /erp/sc/routing/data/local_inventory/getBatchStatementList
        Method: GET

        Args:
            access_token: Access token for authentication
            search_value: 搜索值 (Optional)
            wid_list: 仓库id，多个使用英文逗号分隔 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限400 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "search_value": search_value,
            "wid_list": wid_list,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/getBatchStatementList",
            method="GET",
            req_body=params
        )



    async def wareHouseBin_switchStatus(
        self,
        access_token: str,
        wid: str,
        whbCode: str,
        status: int
    ) -> dict[str, Any]:
        """
        启用、禁用仓位

        API: /erp/sc/routing/storage/wareHouseBin/switchStatus
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库id (Required)
            whbCode: 仓位名称 (Required)
            status: 仓位状态：0 禁用，1 启用 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.wareHouseBin_switchStatus(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "whbCode": whbCode,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/wareHouseBin/switchStatus",
            method="POST",
            req_body=params
        )



    async def sku(
        self,
        access_token: str,
        wpId: str,
        wpmId: str
    ) -> dict[str, Any]:
        """
        海外仓sku取消配对

        API: /basicOpen/overseaWarehouseSetting/productUnMatch
        Method: POST

        Args:
            access_token: Access token for authentication
            wpId: 三方服务商id (Required)
            wpmId: 配对id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sku(token, ...)
            >>> print(result)
        """
        params = {
            "wpId": wpId,
            "wpmId": wpmId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/overseaWarehouseSetting/productUnMatch",
            method="POST",
            req_body=params
        )



    async def sku(  # noqa: F811
        self,
        access_token: str,
        twId: int,
        twpId: int,
        wpId: int,
        productId: int,
        matchNum: int,
        matchAll: int | None = None,
        fnsku: str | None = None,
        sellerId: str | None = None
    ) -> dict[str, Any]:
        """
        海外仓sku配对

        API: /basicOpen/overseaWarehouseSetting/productMatch
        Method: POST

        Args:
            access_token: Access token for authentication
            twId: 三方仓id (Required)
            twpId: 三方商品id (Required)
            wpId: 三方服务商id (Required)
            productId: 商品id (Required)
            matchNum: 整箱配对数量 (Required)
            matchAll: 是否配对海外仓所有仓库，0否；1是，默认0 (Optional)
            fnsku: fnsku (Optional)
            sellerId: 店铺id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sku(token, ...)
            >>> print(result)
        """
        params = {
            "twId": twId,
            "twpId": twpId,
            "wpId": wpId,
            "productId": productId,
            "matchNum": matchNum,
            "matchAll": matchAll,
            "fnsku": fnsku,
            "sellerId": sellerId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/overseaWarehouseSetting/productMatch",
            method="POST",
            req_body=params
        )



    async def get_productlist(
        self,
        access_token: str,
        list: dict[str, Any],
        withHistory: bool | None = None
    ) -> dict[str, Any]:
        """
        查询产品仓位列表

        API: /basicOpen/warehouseConfig/warehouseBin/getEntryRecommendBinList
        Method: GET

        Args:
            access_token: Access token for authentication
            list:  (Required)
            withHistory: 是否查询历史仓位，false-否true-是;默认否 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "list": list,
            "withHistory": withHistory
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/warehouseConfig/warehouseBin/getEntryRecommendBinList",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        name: str,
        sys_wid: int | None = None,
        wid: str | None = None,
        contact: str | None = None,
        telephone: str | None = None,
        address: str | None = None,
        remark: str | None = None,
        type: int | None = None
    ) -> dict[str, Any]:
        """
        添加修改仓库

        API: /erp/sc/storage/wareHouse/edit
        Method: POST

        Args:
            access_token: Access token for authentication
            sys_wid: 领星系统仓库id，编辑时必传 (Optional)
            wid: 客户自定义仓库id【非领星系统ERP内仓库id】 (Optional)
            name: 仓库名称 (Required)
            contact: 负责人 (Optional)
            telephone: 联系电话 (Optional)
            address: 仓库地址 (Optional)
            remark: 备注 (Optional)
            type: 仓库属性：1 -本地仓 3 -海外自建仓，不传默认 1 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "wid": wid,
            "name": name,
            "contact": contact,
            "telephone": telephone,
            "address": address,
            "remark": remark,
            "type": type
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/wareHouse/edit",
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
        查询仓库列表

        API: /erp/sc/data/local_inventory/warehouse
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000条 (Optional)

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
            route_name="/erp/sc/data/local_inventory/warehouse",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        wid: str | None = None,
        id: str | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> dict[str, Any]:
        """
        查询本地仓位列表

        API: /erp/sc/routing/data/local_inventory/warehouseBin
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库ID，字符串id，多个使用英文逗号分隔 (Optional)
            id: 仓位ID，字符串id，多个使用英文逗号分隔 (Optional)
            offset: 分页偏移量，默认为0 (Optional)
            limit: 限制条数，默认20条 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "id": id,
            "offset": offset,
            "limit": limit
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/warehouseBin",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        wid: int,
        code: str
    ) -> dict[str, Any]:
        """
        添加仓位

        API: /erp/sc/routing/storage/wareHouseBin/create
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 仓库id (Required)
            code: 仓位名称 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "code": code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/wareHouseBin/create",
            method="POST",
            req_body=params
        )



    async def logisticsOrdering_setTrackingNo(
        self,
        access_token: str,
        waybill_no: str,
        wo_number: str,
        tracking_no: str | None = None,
        logistics_freight: str | None = None,
        pkg_fee_weight: str | None = None
    ) -> dict[str, Any]:
        """
        物流下单 - 编辑运单号跟踪号

        API: /basicOpen/logisticsOrdering/setTrackingNo
        Method: POST

        Args:
            access_token: Access token for authentication
            waybill_no: 运单号 (Required)
            wo_number: 销售出库单号 (Required)
            tracking_no: 跟踪号 (Optional)
            logistics_freight: 物流运费 (Optional)
            pkg_fee_weight: 计费重 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.logisticsOrdering_setTrackingNo(token, ...)
            >>> print(result)
        """
        params = {
            "waybill_no": waybill_no,
            "wo_number": wo_number,
            "tracking_no": tracking_no,
            "logistics_freight": logistics_freight,
            "pkg_fee_weight": pkg_fee_weight
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/logisticsOrdering/setTrackingNo",
            method="POST",
            req_body=params
        )



    async def wmsOrder_cancel(
        self,
        access_token: str,
        tagType: str,
        orderComment: str | None = None
    ) -> dict[str, Any]:
        """
        销售出库单截单

        API: /basicOpen/wmsOrder/cancel
        Method: POST

        Args:
            access_token: Access token for authentication
            tagType: 截单标签，3-5：待人工审核；3-17：其他 (Required)
            orderComment: 截单备注 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.wmsOrder_cancel(token, ...)
            >>> print(result)
        """
        params = {
            "tagType": tagType,
            "orderComment": orderComment
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/wmsOrder/cancel",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        wo_number_arr: list[Any] | None = None,
        order_number_arr: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询销售出库单物流面单

        API: /erp/sc/routing/wms/order/getWmsLogisticsLabels
        Method: GET

        Args:
            access_token: Access token for authentication
            wo_number_arr: 销售出库单号,上限50【销售出库单号与系统单号二选一必填】 (Optional)
            order_number_arr: 系统单号,上限50【销售出库单号与系统单号二选一必填】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "wo_number_arr": wo_number_arr,
            "order_number_arr": order_number_arr
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/wms/order/getWmsLogisticsLabels",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        page: int | None = None,
        page_size: int | None = None,
        sid_arr: list[Any] | None = None,
        platform_order_no_arr: list[Any] | None = None,
        order_number_arr: list[Any] | None = None,
        wo_number_arr: list[Any] | None = None,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询销售出库单列表

        API: /erp/sc/routing/wms/order/wmsOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            page: 分页页码，默认1 (Optional)
            page_size: 分页长度，默认20，上限200 (Optional)
            sid_arr: 店铺id (Optional)
            platform_order_no_arr: 平台单号 (Optional)
            order_number_arr: 系统单号 (Optional)
            wo_number_arr: 销售出库单号 (Optional)
            start_date: 开始日期，格式：Y-m-d，默认为最近1个月 (Optional)
            end_date: 结束日期，格式：Y-m-d，默认为最近1个月 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "page": page,
            "page_size": page_size,
            "sid_arr": sid_arr,
            "platform_order_no_arr": platform_order_no_arr,
            "order_number_arr": order_number_arr,
            "wo_number_arr": wo_number_arr,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/wms/order/wmsOrderList",
            method="GET",
            req_body=params
        )


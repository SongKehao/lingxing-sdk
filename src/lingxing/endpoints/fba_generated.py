"""FBA API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class FBAEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def create(
        self,
        access_token: str,
        list: list[Any],
        box_list: list[Any],
        head_logistics_list: dict[str, Any],
        wid: int | None = None,
        sys_wid: int | None = None,
        expected_arrival_date: str | None = None,
        etd_date: str | None = None,
        eta_date: str | None = None,
        delivery_date: str | None = None,
        actual_shipment_time: str | None = None,
        is_points_behind: int | None = None,
        points_behind_coeffient: int | None = None,
        vat_code: str | None = None,
        remark: str | None = None,
        ship_mode: int | None = None,
        hand_pick_purchase: int | None = None,
        box_type: str | None = None,
        box_remark: str | None = None,
        logistics_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        生成待发货的发货单

        API: /erp/sc/routing/storage/shipment/createReadySendOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 自定义仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。 (Optional)
            sys_wid: 系统仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。多仓库发货时传 -1。 (Optional)
            expected_arrival_date: 预计到达时间，格式：Y-m-d (Optional)
            etd_date: 开船时间，格式：Y-m-d (Optional)
            eta_date: 预计到港时间，格式：Y-m-d (Optional)
            delivery_date: 实际妥投时间，格式：Y-m-d (Optional)
            actual_shipment_time: 实际发货时间，格式：Y-m-d (Optional)
            is_points_behind: 是否分抛计算：0 否，1 是；头程分摊方式为按计费重时用 (Optional)
            points_behind_coeffient: 分抛系数：0~100,分抛计算选是时必填 (Optional)
            vat_code: 店铺VAT税号 (Optional)
            remark: 备注 (Optional)
            ship_mode: 发货方式：1-默认，2-工厂直发 (Optional)
            hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是 (Optional)
            list:  (Required)
            box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU (Optional)
            box_remark: 装箱备注 (Optional)
            box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填 (Required)
            head_logistics_list: 新版头程物流信息 (Required)
            logistics_list: 旧版物流信息，即将下线 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "sys_wid": sys_wid,
            "expected_arrival_date": expected_arrival_date,
            "etd_date": etd_date,
            "eta_date": eta_date,
            "delivery_date": delivery_date,
            "actual_shipment_time": actual_shipment_time,
            "is_points_behind": is_points_behind,
            "points_behind_coeffient": points_behind_coeffient,
            "vat_code": vat_code,
            "remark": remark,
            "ship_mode": ship_mode,
            "hand_pick_purchase": hand_pick_purchase,
            "list": list,
            "box_type": box_type,
            "box_remark": box_remark,
            "box_list": box_list,
            "head_logistics_list": head_logistics_list,
            "logistics_list": logistics_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/createReadySendOrder",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        shipment_sn_arr: list[Any],
        return_deleted: bool | None = None
    ) -> dict[str, Any]:
        """
        批量查询发货单详情

        API: /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            shipment_sn_arr: 发货单号数组，上限50 (Required)
            return_deleted: 是否返回已删除数据: false-否(默认)，true-是 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_sn_arr": shipment_sn_arr,
            "return_deleted": return_deleted
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList",
            method="GET",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        sys_wid: int,
        list: list[Any],
        head_logistics_list: dict[str, Any],
        wid: int | None = None,
        expected_arrival_date: str | None = None,
        etd_date: str | None = None,
        eta_date: str | None = None,
        delivery_date: str | None = None,
        actual_shipment_time: str | None = None,
        is_points_behind: int | None = None,
        points_behind_coeffient: int | None = None,
        request_flag: str | None = None,
        ship_mode: int | None = None,
        hand_pick_purchase: int | None = None,
        remark: str | None = None,
        box_remark: str | None = None,
        box_list: list[Any] | None = None,
        logistics_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        生成已发货的发货单

        API: /erp/sc/storage/shipment/createSendedOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid (Optional)
            sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (Required)
            expected_arrival_date: 预计到达时间：Y-m-d (Optional)
            etd_date: 开船时间，格式：Y-m-d (Optional)
            eta_date: 预计到港时间，格式：Y-m-d (Optional)
            delivery_date: 实际妥投时间，格式：Y-m-d (Optional)
            actual_shipment_time: 实际发货时间，格式：Y-m-d (Optional)
            is_points_behind: 是否分抛计算：0 否，1 是，头程分摊方式为按计费重时用 (Optional)
            points_behind_coeffient: 分抛系数：0~100，分抛计算选是时必填 (Optional)
            request_flag: 自定义请求标识，本次请求超时后可根据此标识查询此次请求的结果，由请求方保持标识唯一性 (Optional)
            ship_mode: 发货方式：1-默认，2-工厂直发 (Optional)
            hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是 (Optional)
            remark: 备注 (Optional)
            list:  (Required)
            box_remark: 装箱备注 (Optional)
            box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填 (Optional)
            head_logistics_list: 新版头程物流信息 (Required)
            logistics_list: 旧版物流信息，即将下线 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "wid": wid,
            "sys_wid": sys_wid,
            "expected_arrival_date": expected_arrival_date,
            "etd_date": etd_date,
            "eta_date": eta_date,
            "delivery_date": delivery_date,
            "actual_shipment_time": actual_shipment_time,
            "is_points_behind": is_points_behind,
            "points_behind_coeffient": points_behind_coeffient,
            "request_flag": request_flag,
            "ship_mode": ship_mode,
            "hand_pick_purchase": hand_pick_purchase,
            "remark": remark,
            "list": list,
            "box_remark": box_remark,
            "box_list": box_list,
            "head_logistics_list": head_logistics_list,
            "logistics_list": logistics_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/shipment/createSendedOrder",
            method="POST",
            req_body=params
        )



    async def fba(
        self,
        access_token: str,
        shipment_nos: list[Any]
    ) -> dict[str, Any]:
        """
        FBA发货单发货

        API: /erp/sc/storage/shipment/sendGoods
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_nos: 发货单号列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.fba(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_nos": shipment_nos
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/shipment/sendGoods",
            method="POST",
            req_body=params
        )



    async def inventory(
        self,
        access_token: str,
        shipment_nos: list[Any],
        is_auto_batch: int | None = None
    ) -> dict[str, Any]:
        """
        发货单分配库存

        API: /erp/sc/routing/storage/shipment/lockStock
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (Required)
            is_auto_batch: 是否锁定至批次，1：是，0：否，默认为否，否：只锁定库存数量，发货时按先进先出规则匹配出库批次；是：按先进先锁规则自动指定批次并锁定，发货时按锁定批次出库；分配库存后，可在【查询发货单详情】接口的采购信息中查看锁定的批次 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventory(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_nos": shipment_nos,
            "is_auto_batch": is_auto_batch
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/lockStock",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        request_flag: str
    ) -> dict[str, Any]:
        """
        发货单创建接口结果查询

        API: /erp/sc/routing/storage/shipment/searchProcessResult
        Method: POST

        Args:
            access_token: Access token for authentication
            request_flag: 生成单据时传的请求标识 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "request_flag": request_flag
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/searchProcessResult",
            method="POST",
            req_body=params
        )



    async def inventory(  # noqa: F811
        self,
        access_token: str,
        shipment_nos: list[Any]
    ) -> dict[str, Any]:
        """
        发货单释放库存

        API: /erp/sc/routing/storage/shipment/releaseStock
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_nos: 发货单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventory(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_nos": shipment_nos
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/releaseStock",
            method="POST",
            req_body=params
        )



    async def update_info(
        self,
        access_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        更新发货单物流信息

        API: /erp/sc/routing/storage/shipment/updateListLogistics
        Method: POST

        Args:
            access_token: Access token for authentication
            data: 参数数组 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_info(token, ...)
            >>> print(result)
        """
        params = {
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/updateListLogistics",
            method="POST",
            req_body=params
        )



    async def fba(  # noqa: F811
        self,
        access_token: str,
        shipmentNos: list[Any],
        isReturnStock: int,
        isReturnStockAux: int,
        cancelReason: str | None = None
    ) -> dict[str, Any]:
        """
        FBA-作废发货单

        API: /basicOpen/openapi/fbaShipment/shipmentSn/invalid
        Method: POST

        Args:
            access_token: Access token for authentication
            shipmentNos: 发货单号 (Required)
            isReturnStock: 产品库存是否恢复 1恢复 0不恢复 (Required)
            isReturnStockAux: 辅料库存是否恢复 1恢复 0不恢复 (Required)
            cancelReason: 作废原因 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.fba(token, ...)
            >>> print(result)
        """
        params = {
            "shipmentNos": shipmentNos,
            "isReturnStock": isReturnStock,
            "isReturnStockAux": isReturnStockAux,
            "cancelReason": cancelReason
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/fbaShipment/shipmentSn/invalid",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        shipment_sn: str,
        return_deleted: bool | None = None
    ) -> dict[str, Any]:
        """
        查询发货单详情

        API: /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail
        Method: GET

        Args:
            access_token: Access token for authentication
            shipment_sn: 发货单号 (Required)
            return_deleted: 是否返回已删除数据: false-否(默认)，true-是 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_sn": shipment_sn,
            "return_deleted": return_deleted
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail",
            method="GET",
            req_body=params
        )



    async def update(
        self,
        access_token: str,
        shipment_sn: str,
        is_custom_cost: int,
        list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        更新发货单自定义成本

        API: /erp/sc/routing/storage/shipment/updateCustomCost
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_sn: 发货单号 (Required)
            is_custom_cost: 是否自定义成本 (Required)
            list: 自定义成本信息数组 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_sn": shipment_sn,
            "is_custom_cost": is_custom_cost,
            "list": list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/updateCustomCost",
            method="POST",
            req_body=params
        )



    async def update(  # noqa: F811
        self,
        access_token: str,
        shipment_sn: str,
        remark: str | None = None,
        items: list[Any] | None = None,
        box_type: str | None = None,
        box_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        编辑发货单

        API: /erp/sc/routing/storage/shipment/updateInboundShipmentListMws
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_sn: 发货单号 (Required)
            remark: 备注 (Optional)
            items: 发货商品 (Optional)
            box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU (Optional)
            box_list: 装箱数据 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_sn": shipment_sn,
            "remark": remark,
            "items": items,
            "box_type": box_type,
            "box_list": box_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/updateInboundShipmentListMws",
            method="POST",
            req_body=params
        )



    async def get_info_info(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        获取发货单头程物流信息-承运商信息

        API: /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info_info(token, ...)
            >>> print(result)
        """
        params = {

        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers",
            method="GET",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        offset: int,
        length: int,
        search_value: str | None = None,
        sids: str | None = None,
        mids: str | None = None,
        wid: str | None = None,
        logistics_type: list[Any] | None = None,
        print_status: str | None = None,
        pick_status: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        is_delete: Any | None = None
    ) -> dict[str, Any]:
        """
        查询发货单列表

        API: /erp/sc/routing/storage/shipment/getInboundShipmentList
        Method: GET

        Args:
            access_token: Access token for authentication
            search_value: 搜索的值 (Optional)
            sids: 店铺id,多个时通过英文逗号分隔,如1,2,3，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            mids: 国家id,多个时通过英文逗号分隔,如1,2,3 (Optional)
            wid: 仓库id,多个时通过英文逗号分隔,如1,2,3 (Optional)
            logistics_type: 物流方式id (Optional)
            print_status: 打印状态 0未打印 1 已打印 (Optional)
            pick_status: 拣货状态 0 未拣货 1已拣货 (Optional)
            start_date: 开始日期 (Optional)
            end_date: 结束日期 (Optional)
            offset: 偏移量=（currentPage -1）*length (Required)
            length: 长度 (Required)
            is_delete: 是否删除：0 未删除【默认】 1 已删除 2 全部 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "search_value": search_value,
            "sids": sids,
            "mids": mids,
            "wid": wid,
            "logistics_type": logistics_type,
            "print_status": print_status,
            "pick_status": pick_status,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            "is_delete": is_delete
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentList",
            method="GET",
            req_body=params
        )



    async def delete(
        self,
        access_token: str,
        shipment_nos: list[Any]
    ) -> dict[str, Any]:
        """
        删除发货单

        API: /basicOpen/openapi/fbaShipment/deleteShipmentList
        Method: POST

        Args:
            access_token: Access token for authentication
            shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "shipment_nos": shipment_nos
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/fbaShipment/deleteShipmentList",
            method="POST",
            req_body=params
        )



    async def update_fba(
        self,
        access_token: str,
        order_sn: str,
        shipment_time: str | None = None,
        packing_type: int | None = None,
        logistics_provider_id: int | None = None,
        logistics_channel_id: int | None = None,
        shipment_plan_quantity: int | None = None,
        quantity_in_case: int | None = None,
        box_num: int | None = None,
        sys_wid: int | None = None,
        cg_package_length: Any | None = None,
        cg_package_width: Any | None = None,
        cg_package_height: Any | None = None,
        cg_box_length: Any | None = None,
        cg_box_width: Any | None = None,
        cg_box_height: Any | None = None,
        nw: Any | None = None,
        gw: Any | None = None,
        cg_box_weight: Any | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        编辑FBA发货计划

        API: /erp/sc/routing/storage/shipment/updateShipmentPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            order_sn: 发货计划单号 (Required)
            shipment_time: 发货时间，格式：Y-m-d (Optional)
            packing_type: 包装类型： 1 混装，2 原厂 (Optional)
            logistics_provider_id: 物流商id (Optional)
            logistics_channel_id: 物流渠道id (Optional)
            shipment_plan_quantity: 计划发货量 (Optional)
            quantity_in_case: 单箱数量（PCS） (Optional)
            box_num: 箱数 (Optional)
            sys_wid: 系统仓库id【发货仓库】 (Optional)
            cg_package_length: 包装规格长（cm）【保留两位小数】 (Optional)
            cg_package_width: 包装规格宽（cm）【保留两位小数】 (Optional)
            cg_package_height: 包装规格高（cm）【保留两位小数】 (Optional)
            cg_box_length: 箱规长（cm）【保留两位小数】 (Optional)
            cg_box_width: 箱规宽（cm）【保留两位小数】 (Optional)
            cg_box_height: 箱规高（cm）【保留两位小数】 (Optional)
            nw: 单品净重（g）【保留两位小数】 (Optional)
            gw: 单品毛重（g）【保留两位小数】 (Optional)
            cg_box_weight: 单箱重量（kg）【保留两位小数】 (Optional)
            remark: 备注 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_fba(token, ...)
            >>> print(result)
        """
        params = {
            "order_sn": order_sn,
            "shipment_time": shipment_time,
            "packing_type": packing_type,
            "logistics_provider_id": logistics_provider_id,
            "logistics_channel_id": logistics_channel_id,
            "shipment_plan_quantity": shipment_plan_quantity,
            "quantity_in_case": quantity_in_case,
            "box_num": box_num,
            "sys_wid": sys_wid,
            "cg_package_length": cg_package_length,
            "cg_package_width": cg_package_width,
            "cg_package_height": cg_package_height,
            "cg_box_length": cg_box_length,
            "cg_box_width": cg_box_width,
            "cg_box_height": cg_box_height,
            "nw": nw,
            "gw": gw,
            "cg_box_weight": cg_box_weight,
            "remark": remark
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/updateShipmentPlan",
            method="POST",
            req_body=params
        )



    async def get_fba(
        self,
        access_token: str,
        sids: str | None = None,
        wid: str | None = None,
        packing_type: str | None = None,
        search_field_time: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        status: str | None = None,
        mids: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询FBA发货计划

        API: /erp/sc/data/fba_report/shipmentPlanLists
        Method: POST

        Args:
            access_token: Access token for authentication
            sids: 店铺ids，12,13组成，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            wid: 仓库id (Optional)
            packing_type: 包装类型2原装 1混装 (Optional)
            search_field_time: 查找时间字段(gmt_create-创建时间,estimated_delivery_time-计划发货时间)，不传该字段默认为gmt_create (Optional)
            search_field: 查找字段 order_sn发货计划单号 (Optional)
            search_value: 查找值 (Optional)
            status: 状态 (Optional)
            mids: 国家id (Optional)
            offset: 偏移量 0 偏移量 (currentPage -1) * length (Optional)
            length: 长度 默认20 (Optional)
            start_date: 开始日期 如:2021-09-07 (Optional)
            end_date: 结束日期 如:2021-09-08 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba(token, ...)
            >>> print(result)
        """
        params = {
            "sids": sids,
            "wid": wid,
            "packing_type": packing_type,
            "search_field_time": search_field_time,
            "search_field": search_field,
            "search_value": search_value,
            "status": status,
            "mids": mids,
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/shipmentPlanLists",
            method="POST",
            req_body=params
        )



    async def create_fba(
        self,
        access_token: str,
        product_list: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建FBA发货计划

        API: /erp/sc/routing/storage/shipment/createShipmentPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            remark: 批次信息备注 (Optional)
            product_list: 商品信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_fba(token, ...)
            >>> print(result)
        """
        params = {
            "remark": remark,
            "product_list": product_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/createShipmentPlan",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询承运方式

        API: /amzStaServer/openapi/inbound-shipment/getTransportList
        Method: GET

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentId: 货件id，对应查询货件方案接口对应字段【shipmentId】 (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/getTransportList",
            method="GET",
            req_body=params
        )



    async def update_awd(
        self,
        access_token: str,
        orderId: str,
        shipmentId: str,
        sid: Any,
        trackingId: str
    ) -> dict[str, Any]:
        """
        更新AWD货件跟踪编号

        API: /amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo
        Method: POST

        Args:
            access_token: Access token for authentication
            orderId: STA任务编号 (Required)
            shipmentId: 货件号 (Required)
            sid: 领星店铺ID 对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            trackingId: 跟踪编号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_awd(token, ...)
            >>> print(result)
        """
        params = {
            "orderId": orderId,
            "shipmentId": shipmentId,
            "sid": sid,
            "trackingId": trackingId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-shipment/updateShipmentInfo",
            method="POST",
            req_body=params
        )



    async def sta(
        self,
        access_token: str,
        inboundPlanId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        取消STA任务

        API: /amzStaServer/openapi/inbound-plan/cancelInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sta(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/cancelInboundPlan",
            method="POST",
            req_body=params
        )



    async def awd(
        self,
        access_token: str,
        orderId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        取消AWD入库任务

        API: /amzStaServer/openapi/awd/inbound-plan/cancel
        Method: POST

        Args:
            access_token: Access token for authentication
            orderId: AWD任务编号 (Required)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.awd(token, ...)
            >>> print(result)
        """
        params = {
            "orderId": orderId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/cancel",
            method="POST",
            req_body=params
        )



    async def awd(  # noqa: F811
        self,
        access_token: str,
        orderId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        确认AWD入库任务

        API: /amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            orderId: AWD任务编号 (Required)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.awd(token, ...)
            >>> print(result)
        """
        params = {
            "orderId": orderId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/confirmInboundPlan",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        alias_name: str,
        country_name: str,
        sender_name: str,
        street_detail1: str,
        city: str,
        province: str,
        zip_code: str,
        street_detail2: str | None = None,
        region: str | None = None,
        phone: str | None = None
    ) -> dict[str, Any]:
        """
        地址簿-发货地址创建

        API: /erp/sc/routing/fba/shipment/createShipFromAddress
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            alias_name: 地址簿别名，店铺内唯一 (Required)
            country_name: 发货国家/地区 (Required)
            sender_name: 发货方名称 (Required)
            street_detail1: 街道地址1 (Required)
            street_detail2: 街道地址2 (Optional)
            city: 城市 (Required)
            region: 区 (Optional)
            province: 省/州/地区，美国发货地址限制长度为2位 (Required)
            zip_code: 邮政编码 (Required)
            phone: 电话号码 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "alias_name": alias_name,
            "country_name": country_name,
            "sender_name": sender_name,
            "street_detail1": street_detail1,
            "street_detail2": street_detail2,
            "city": city,
            "region": region,
            "province": province,
            "zip_code": zip_code,
            "phone": phone
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/shipment/createShipFromAddress",
            method="POST",
            req_body=params
        )



    async def get_awdlist(
        self,
        access_token: str,
        page: Any,
        dateType: int,
        endDateTime: Any,
        length: Any,
        startDateTime: Any,
        orderId: str | None = None,
        shipmentId: str | None = None,
        sidList: list[Any] | None = None,
        statusList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询AWD入库任务列表

        API: /amzStaServer/openapi/awd/inbound-plan/page
        Method: POST

        Args:
            access_token: Access token for authentication
            page: 分页页码 (Required)
            dateType: 时间类型 1:创建 2更新 (Required)
            endDateTime: 结束时间，格式：YYYY-MM-DD 双闭区间 (Required)
            orderId: awd入库任务编号 (Optional)
            shipmentId: awd货件单号 (Optional)
            sidList: 店铺id列表 (Optional)
            length: 分页大小，上限 (Required)
            startDateTime: 开始时间，格式：YYYY-MM-DD 双闭区间 (Required)
            statusList: 任务状态：LOCALDRAFT：草稿；DRAFT：待确认；VALIDATING：更新中；CONFIRMED：已确认；CLOSED： 已关闭；EXPIRED：已过期；CANCELLED：已取消 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_awdlist(token, ...)
            >>> print(result)
        """
        params = {
            "page": page,
            "dateType": dateType,
            "endDateTime": endDateTime,
            "orderId": orderId,
            "shipmentId": shipmentId,
            "sidList": sidList,
            "length": length,
            "startDateTime": startDateTime,
            "statusList": statusList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/page",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentIds: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        查询货件详情

        API: /amzStaServer/openapi/inbound-shipment/shipmentDetailList
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentIds: 货件id (Required)
            sid: 店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentIds": shipmentIds,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/shipmentDetailList",
            method="POST",
            req_body=params
        )



    async def get_fba(  # noqa: F811
        self,
        access_token: str,
        data: list[Any],
        type: str,
        hide_ship_from_company_name: int | None = None,
        hide_ship_to_company_name: int | None = None,
        print_sta_name_page: int | None = None,
        sort_label: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA货件箱子、卡板标签

        API: /erp/sc/storage/shipment/printFbaLabels
        Method: POST

        Args:
            access_token: Access token for authentication
            data: 请求数据 (Required)
            hide_ship_from_company_name: 隐藏ship from公司名,默认不隐藏,非必填,传值1为开启 (Optional)
            hide_ship_to_company_name: 传值1为隐藏ship to公司名,默认不隐藏,非必填,传值1为开启 (Optional)
            print_sta_name_page: 传值1为新增任务名称页,默认不新增,非必填,仅打印box箱子标签时生效,传值1为开启 (Optional)
            sort_label: 传值1为按箱子顺序重排,默认不按箱子顺序重排,仅打印box箱子子标签时生效(说明:不按箱子顺序重排时,打印文件... (Optional)
            type: 打印类型：box 箱子标签，card 卡板标签 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba(token, ...)
            >>> print(result)
        """
        params = {
            "data": data,
            "hide_ship_from_company_name": hide_ship_from_company_name,
            "hide_ship_to_company_name": hide_ship_to_company_name,
            "print_sta_name_page": print_sta_name_page,
            "sort_label": sort_label,
            "type": type
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/shipment/printFbaLabels",
            method="POST",
            req_body=params
        )



    async def fbaShipment_shoppingAddress(
        self,
        access_token: str,
        id: int
    ) -> dict[str, Any]:
        """
        地址簿-配送地址详情

        API: /basicOpen/openapi/fbaShipment/shoppingAddress
        Method: POST

        Args:
            access_token: Access token for authentication
            id: 唯一记录id，查询FBA列表接口对应字段【id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.fbaShipment_shoppingAddress(token, ...)
            >>> print(result)
        """
        params = {
            "id": id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/fbaShipment/shoppingAddress",
            method="POST",
            req_body=params
        )



    async def get_fbadetail(
        self,
        access_token: str,
        sid: int,
        event_date: str,
        fba_shipment_id: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA到货接收明细

        API: /erp/sc/data/fba_report/receivedInventory
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            event_date: 签收日期，格式：Y-m-d，未填写fba_shipment_id时必填 (Required)
            fba_shipment_id: 货件单号，未填写event_date时必填 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbadetail(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "event_date": event_date,
            "fba_shipment_id": fba_shipment_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/receivedInventory",
            method="POST",
            req_body=params
        )



    async def get_stalist(
        self,
        access_token: str,
        page: Any,
        length: Any,
        dateType: int,
        planName: str | None = None,
        shipmentIdList: list[Any] | None = None,
        sids: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        ERRORED: Any | None = None
    ) -> dict[str, Any]:
        """
        查询STA任务列表

        API: /amzStaServer/openapi/inbound-plan/page
        Method: POST

        Args:
            access_token: Access token for authentication
            page: 分页页码 (Required)
            length: 分页大小，上限200 (Required)
            dateType: 时间类型 1:创建 2更新 (Required)
            planName: STA任务名称(模糊搜索) (Optional)
            shipmentIdList: 货件id或者货件单号(精确搜索) (Optional)
            sids: 领星店铺ID 列表，对应查询亚马逊店铺列表 (Optional)
            sortField:  (Optional)
            sortType:  (Optional)
            ERRORED: 否 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_stalist(token, ...)
            >>> print(result)
        """
        params = {
            "page": page,
            "length": length,
            "dateType": dateType,
            "planName": planName,
            "shipmentIdList": shipmentIdList,
            "sids": sids,
            "sortField": sortField,
            "sortType": sortType,
            "ERRORED": ERRORED
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/page",
            method="POST",
            req_body=params
        )



    async def inbound_shipment_confirmPlacementOption(
        self,
        access_token: str,
        inboundPlanId: str,
        placementOptionId: str,
        shipmentIds: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        确认货件方案

        API: /amzStaServer/openapi/inbound-shipment/confirmPlacementOption
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            placementOptionId: 货件方案id (Required)
            shipmentIds: 货件列表：传入对应货件方案id下的所有货件id (Required)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_shipment_confirmPlacementOption(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "placementOptionId": placementOptionId,
            "shipmentIds": shipmentIds,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/confirmPlacementOption",
            method="POST",
            req_body=params
        )



    async def update(  # noqa: F811
        self,
        access_token: str,
        billOfLadingNumber: str | None = None,
        freightBillNumber: str | None = None,
        inboundPlanId: str | None = None,
        shipmentConfirmationId: str | None = None,
        shipmentId: str | None = None,
        sid: Any | None = None,
        trackBOList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        上传货件跟踪号

        API: /amzStaServer/openapi/inbound-shipment/updateShipmentTrack
        Method: POST

        Args:
            access_token: Access token for authentication
            billOfLadingNumber: 提货单号,LTL建议填写,非必填 (Optional)
            freightBillNumber: LTL跟踪编号(LTL必填) (Optional)
            inboundPlanId: STA任务编号 (Optional)
            shipmentConfirmationId: 货件单号 (Optional)
            shipmentId: 货件id (Optional)
            sid: 领星店铺ID (Optional)
            trackBOList: 跟踪编号列表,SPD必填 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "billOfLadingNumber": billOfLadingNumber,
            "freightBillNumber": freightBillNumber,
            "inboundPlanId": inboundPlanId,
            "shipmentConfirmationId": shipmentConfirmationId,
            "shipmentId": shipmentId,
            "sid": sid,
            "trackBOList": trackBOList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/updateShipmentTrack",
            method="POST",
            req_body=params
        )



    async def update_info(  # noqa: F811
        self,
        access_token: str,
        boxes: list[Any],
        inboundPlanId: str | None = None,
        items: list[Any] | None = None,
        shipmentId: str | None = None,
        sid: Any | None = None
    ) -> dict[str, Any]:
        """
        修改货件装箱信息

        API: /amzStaServer/openapi/inbound-packing/updateShipmentPacking
        Method: POST

        Args:
            access_token: Access token for authentication
            boxes: 装箱明细数据 (Required)
            inboundPlanId: 任务编号 (Optional)
            items:  (Optional)
            shipmentId: 货件号 (Optional)
            sid: 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_info(token, ...)
            >>> print(result)
        """
        params = {
            "boxes": boxes,
            "inboundPlanId": inboundPlanId,
            "items": items,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/updateShipmentPacking",
            method="POST",
            req_body=params
        )



    async def create_awd(
        self,
        access_token: str,
        awdDeliveredGoodsBOS: list[Any],
        awdShippingAddressBO: dict[str, Any],
        sid: Any,
        destinationRegion: str | None = None
    ) -> dict[str, Any]:
        """
        创建AWD入库任务

        API: /amzStaServer/openapi/awd/inbound-plan/createInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            awdDeliveredGoodsBOS: 发货商品 (Required)
            awdShippingAddressBO: 发货地址 (Required)
            destinationRegion: 地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-southeast：美国东南部（南卡罗来纳州分拨中心）；null：亚马逊分配（亚马逊将为您的货件分配最佳分拨中心） (Optional)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_awd(token, ...)
            >>> print(result)
        """
        params = {
            "awdDeliveredGoodsBOS": awdDeliveredGoodsBOS,
            "awdShippingAddressBO": awdShippingAddressBO,
            "destinationRegion": destinationRegion,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/createInboundPlan",
            method="POST",
            req_body=params
        )



    async def get_fbafnsku(
        self,
        access_token: str,
        data: list[Any],
        custom_content: str | None = None
    ) -> dict[str, Any]:
        """
        查询FBA货件商品FNSKU标签

        API: /erp/sc/storage/shipment/printFnskuLabels
        Method: POST

        Args:
            access_token: Access token for authentication
            data:  (Required)
            custom_content: 自定义内容，默认MADE IN CHINA (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbafnsku(token, ...)
            >>> print(result)
        """
        params = {
            "data": data,
            "custom_content": custom_content
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/shipment/printFnskuLabels",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sid: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None,
        shipment_id: str | None = None,
        start_extra_date: str | None = None,
        end_extra_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询货件列表

        API: /erp/sc/data/fba_report/shipmentList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，多个以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 货件创建开始日期，格式：Y-m-d，左闭右开 (Required)
            end_date: 货件创建截止日期，格式：Y-m-d，左闭右开 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)
            shipment_id: 货件单号，多个以英文逗号隔开，仅支持精确搜索 (Optional)
            start_extra_date: 开始日期，格式：Y-m-d，左闭右开 (Optional)
            end_extra_date: 结束日期，格式：Y-m-d，左闭右开 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            "shipment_id": shipment_id,
            "start_extra_date": start_extra_date,
            "end_extra_date": end_extra_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/shipmentList",
            method="POST",
            req_body=params
        )



    async def get_info(
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentIdList: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        查询货件装箱信息

        API: /amzStaServer/openapi/inbound-shipment/listShipmentBoxes
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentIdList: 货件id (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentIdList": shipmentIdList,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/listShipmentBoxes",
            method="POST",
            req_body=params
        )



    async def update(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        alias_name: str,
        country_name: str,
        sender_name: str,
        street_detail1: str,
        city: str,
        province: str,
        zip_code: str,
        id: int,
        street_detail2: str | None = None,
        region: str | None = None,
        phone: str | None = None
    ) -> dict[str, Any]:
        """
        地址簿-发货地址修改

        API: /erp/sc/routing/fba/shipment/updateShipFromAddress
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            alias_name: 地址簿别名，店铺内唯一 (Required)
            country_name: 发货国家/地区 (Required)
            sender_name: 发货方名称 (Required)
            street_detail1: 街道地址1 (Required)
            street_detail2: 街道地址2 (Optional)
            city: 城市 (Required)
            region: 区 (Optional)
            province: 省/州/地区，美国发货地址限制长度为2位 (Required)
            zip_code: 邮政编码 (Required)
            phone: 电话号码 (Optional)
            id: 地址簿-发货地址列表接口返回id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "alias_name": alias_name,
            "country_name": country_name,
            "sender_name": sender_name,
            "street_detail1": street_detail1,
            "street_detail2": street_detail2,
            "city": city,
            "region": region,
            "province": province,
            "zip_code": zip_code,
            "phone": phone,
            "id": id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/shipment/updateShipFromAddress",
            method="POST",
            req_body=params
        )



    async def get_awd(
        self,
        access_token: str,
        orderId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询AWD入库任务详情

        API: /amzStaServer/openapi/awd/inbound-plan/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            orderId: STA任务编号 (Required)
            sid: 领星店铺ID 列表，对应查询亚马逊店铺列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_awd(token, ...)
            >>> print(result)
        """
        params = {
            "orderId": orderId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/detail",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询包装组

        API: /amzStaServer/openapi/inbound-packing/listPackingGroupItems
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号,，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/listPackingGroupItems",
            method="POST",
            req_body=params
        )



    async def get_stainfo(
        self,
        access_token: str,
        inboundPlanId: str,
        packingGroupIdList: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        查询STA任务包装组装箱信息

        API: /amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            packingGroupIdList: 包装组id (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_stainfo(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "packingGroupIdList": packingGroupIdList,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking",
            method="POST",
            req_body=params
        )



    async def inbound_shipment_generatePlacementOptions(
        self,
        access_token: str,
        inboundPlanId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        生成货件方案

        API: /amzStaServer/openapi/inbound-shipment/generatePlacementOptions
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_shipment_generatePlacementOptions(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/generatePlacementOptions",
            method="POST",
            req_body=params
        )



    async def get_sta(
        self,
        access_token: str,
        inboundPlanId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询STA任务详情

        API: /amzStaServer/openapi/inbound-plan/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sta(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/detail",
            method="POST",
            req_body=params
        )



    async def info(
        self,
        access_token: str,
        inboundPlanId: str,
        packageGroupings: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        提交装箱信息

        API: /amzStaServer/openapi/inbound-packing/setPackingInformation
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            packageGroupings: 分组装箱数据 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.info(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "packageGroupings": packageGroupings,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/setPackingInformation",
            method="POST",
            req_body=params
        )



    async def get_info(  # noqa: F811
        self,
        access_token: str,
        sid: Any,
        msku: list[Any]
    ) -> dict[str, Any]:
        """
        获取商品预处理信息

        API: /amzStaServer/openapi/inbound-packing/getPrepDetails
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: sid店铺id (Required)
            msku: 商品MSKU: 最多不超过100个 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/getPrepDetails",
            method="GET",
            req_body=params
        )



    async def info(  # noqa: F811
        self,
        access_token: str,
        boxes: list[Any],
        inboundPlanId: str,
        sid: str,
        packingGroupId: str | None = None,
        shipmentId: str | None = None
    ) -> dict[str, Any]:
        """
        保存装箱信息

        API: /amzStaServer/openapi/inbound-packing/setLocalPackingInformation
        Method: POST

        Args:
            access_token: Access token for authentication
            boxes: 箱子信息 (Required)
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            packingGroupId: 包装组id：先装箱后分仓方式时必填；先分仓后装箱方式时无需填写 (Optional)
            shipmentId: 货件id：先分仓后装箱方式时必填；分装箱后分仓方式时无需填写 (Optional)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.info(token, ...)
            >>> print(result)
        """
        params = {
            "boxes": boxes,
            "inboundPlanId": inboundPlanId,
            "packingGroupId": packingGroupId,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/setLocalPackingInformation",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sid: list[Any] | None = None,
        search_value: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        地址簿-发货地址列表

        API: /erp/sc/routing/fba/shipment/shipFromAddressList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_value: 对应搜索字段模糊搜索值 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "search_value": search_value,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/shipment/shipFromAddressList",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentIdList: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        生成承运方式

        API: /amzStaServer/openapi/inbound-shipment/generateTransportList
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentIdList: 发货信息：array，注意需提供所有货件单号的发货时间，生成所有货件的承运方式 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentIdList": shipmentIdList,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/generateTransportList",
            method="POST",
            req_body=params
        )



    async def update_awd(  # noqa: F811
        self,
        access_token: str,
        awdDeliveredGoodsBOS: list[Any],
        awdShippingAddressBO: dict[str, Any],
        orderId: str,
        sid: Any,
        createBy: str | None = None,
        destinationRegion: str | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        更新AWD入库任务

        API: /amzStaServer/openapi/awd/inbound-plan/updateInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            awdDeliveredGoodsBOS: 发货商品 (Required)
            awdShippingAddressBO: 发货地址 (Required)
            createBy: 创建人id，默认API账号id (Optional)
            destinationRegion: 地区偏好：us-east：美国东海岸（马里兰州和宾夕法尼亚分拨中心）；us-west：美国西海岸（加利福尼亚州分拨中心）；us-southcentral：美国中南部（德克萨斯州分拨中心）；us-southeast：美国东南部（南卡罗来纳州分拨中心）；null：亚马逊分配（亚马逊将为您的货件分配最佳分拨中心） (Optional)
            orderId: STA任务编号 (Required)
            remark: 备注 (Optional)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_awd(token, ...)
            >>> print(result)
        """
        params = {
            "awdDeliveredGoodsBOS": awdDeliveredGoodsBOS,
            "awdShippingAddressBO": awdShippingAddressBO,
            "createBy": createBy,
            "destinationRegion": destinationRegion,
            "orderId": orderId,
            "remark": remark,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-plan/updateInboundPlan",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询可选送达时间

        API: /amzStaServer/openapi/inbound-shipment/getDeliveryDateList
        Method: GET

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentId: 货件id，对应查询货件方案接口对应字段【shipmentId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/getDeliveryDateList",
            method="GET",
            req_body=params
        )



    async def erp(
        self,
        access_token: str,
        sid: int,
        shipment_ids: list[Any]
    ) -> dict[str, Any]:
        """
        同步亚马逊货件到ERP

        API: /erp/sc/routing/fba/shipment/syncShipment
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            shipment_ids: 货件编号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.erp(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "shipment_ids": shipment_ids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/shipment/syncShipment",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        生成可选送达时间

        API: /amzStaServer/openapi/inbound-shipment/generateDeliveryDateList
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentId: 货件id，对应查询货件方案接口对应字段【shipmentId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/generateDeliveryDateList",
            method="POST",
            req_body=params
        )



    async def inbound_shipment_commitStaDeliverTime(
        self,
        access_token: str,
        deliveryWindowOptionId: str,
        inboundPlanId: str,
        shipmentId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        提交送达时间

        API: /amzStaServer/openapi/inbound-shipment/commitStaDeliverTime
        Method: POST

        Args:
            access_token: Access token for authentication
            deliveryWindowOptionId: 送达时间id (Required)
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentId: 货件id，对应查询货件方案接口对应字段【shipmentId】 (Required)
            sid: 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_shipment_commitStaDeliverTime(token, ...)
            >>> print(result)
        """
        params = {
            "deliveryWindowOptionId": deliveryWindowOptionId,
            "inboundPlanId": inboundPlanId,
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/commitStaDeliverTime",
            method="POST",
            req_body=params
        )



    async def create_sta(
        self,
        access_token: str,
        addressLine1: str,
        city: str,
        countryCode: str,
        inboundPlanItems: list[Any],
        phoneNumber: str,
        positionType: str,
        postalCode: str,
        shipperName: str,
        sid: Any,
        stateOrProvinceCode: str,
        addressLine2: str | None = None,
        companyName: str | None = None,
        email: str | None = None,
        planName: str | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建STA任务

        API: /amzStaServer/openapi/inbound-plan/createInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            addressLine1: 详细街道地址1 (Required)
            addressLine2: 详细街道地址2 (Optional)
            city: 城市 (Required)
            companyName: 公司名称 (Optional)
            countryCode: 国家(地区） (Required)
            email: 邮箱 (Optional)
            inboundPlanItems: 计划明细列表 (Required)
            phoneNumber: 电话号码 (Required)
            planName: 计划名称 (Optional)
            positionType: 分仓方式(1-先装箱再分仓，2-先分仓再装箱) (Required)
            postalCode: 邮政编码 (Required)
            remark: 备注 (Optional)
            shipperName: 发货方名称 (Required)
            sid: 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            stateOrProvinceCode: 州/省/地区 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_sta(token, ...)
            >>> print(result)
        """
        params = {
            "addressLine1": addressLine1,
            "addressLine2": addressLine2,
            "city": city,
            "companyName": companyName,
            "countryCode": countryCode,
            "email": email,
            "inboundPlanItems": inboundPlanItems,
            "phoneNumber": phoneNumber,
            "planName": planName,
            "positionType": positionType,
            "postalCode": postalCode,
            "remark": remark,
            "shipperName": shipperName,
            "sid": sid,
            "stateOrProvinceCode": stateOrProvinceCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/createInboundPlan",
            method="POST",
            req_body=params
        )



    async def get_info(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str | None = None,
        sid: Any | None = None
    ) -> dict[str, Any]:
        """
        查询货件方案的装箱信息

        API: /amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo
        Method: GET

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Optional)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo",
            method="GET",
            req_body=params
        )



    async def inbound_shipment_setDeliveryService(
        self,
        access_token: str,
        inboundPlanId: str,
        shipmentDistributionInfo: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        提交货件配送服务

        API: /amzStaServer/openapi/inbound-shipment/setDeliveryService
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            shipmentDistributionInfo: 货件配送信息 (Required)
            sid: 领星店铺ID，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inbound_shipment_setDeliveryService(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "shipmentDistributionInfo": shipmentDistributionInfo,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/setDeliveryService",
            method="POST",
            req_body=params
        )



    async def get_awd(  # noqa: F811
        self,
        access_token: str,
        shipmentId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询AWD入库货件详情

        API: /amzStaServer/openapi/awd/inbound-shipment/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            shipmentId: AWD入库货件单号 (Required)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_awd(token, ...)
            >>> print(result)
        """
        params = {
            "shipmentId": shipmentId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-shipment/detail",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        taskId: str
    ) -> dict[str, Any]:
        """
        查询异步任务状态

        API: /amzStaServer/openapi/task-plan/operate
        Method: POST

        Args:
            access_token: Access token for authentication
            taskId: 操作任务号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "taskId": taskId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/task-plan/operate",
            method="POST",
            req_body=params
        )



    async def update(  # noqa: F811
        self,
        access_token: str,
        is_closed: int,
        list: list[Any]
    ) -> dict[str, Any]:
        """
        修改货件实际状态

        API: /erp/sc/routing/storage/shipment/updateShipmentActualStatus
        Method: POST

        Args:
            access_token: Access token for authentication
            is_closed: 货件状态：0 进行中，1 已完成 (Required)
            list: 货件信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "is_closed": is_closed,
            "list": list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/updateShipmentActualStatus",
            method="POST",
            req_body=params
        )



    async def staerp(
        self,
        access_token: str,
        inboundPlanIdList: list[Any],
        sid: Any
    ) -> dict[str, Any]:
        """
        同步STA任务到ERP

        API: /amzStaServer/openapi/inbound-plan/gatherInboundPlan
        Method: POST

        Args:
            access_token: Access token for authentication
            inboundPlanIdList: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.staerp(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanIdList": inboundPlanIdList,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-plan/gatherInboundPlan",
            method="POST",
            req_body=params
        )



    async def get_awdlist(  # noqa: F811
        self,
        access_token: str,
        page: Any,
        dateType: int,
        endDateTime: Any,
        length: Any,
        startDateTime: Any,
        shipmentId: str | None = None,
        sidList: list[Any] | None = None,
        statusList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询AWD入库货件列表

        API: /amzStaServer/openapi/awd/inbound-shipment/page
        Method: POST

        Args:
            access_token: Access token for authentication
            page: 分页页码 (Required)
            dateType: 时间类型 1:创建 2更新 (Required)
            endDateTime: 结束时间，格式：YYYY-MM-DD 双闭区间 (Required)
            shipmentId: 货件单号 (Optional)
            sidList: 店铺id列表 (Optional)
            length: 分页大小，上限 (Required)
            startDateTime: 开始时间，格式：YYYY-MM-DD 双闭区间 (Required)
            statusList: 任务状态：CREATED：已创建；SHIPPED：已发货；IN_TRANSIT：运输中；RECEIVING：接收中；DELIVERED：已送达；CLOSED：已关闭；CANCELLED：已取消 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_awdlist(token, ...)
            >>> print(result)
        """
        params = {
            "page": page,
            "dateType": dateType,
            "endDateTime": endDateTime,
            "shipmentId": shipmentId,
            "sidList": sidList,
            "length": length,
            "startDateTime": startDateTime,
            "statusList": statusList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/awd/inbound-shipment/page",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        inboundPlanId: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询货件方案

        API: /amzStaServer/openapi/inbound-shipment/shipmentPreView
        Method: GET

        Args:
            access_token: Access token for authentication
            inboundPlanId: STA任务编号，对应创建STA任务接口对应字段【inboundPlanId】 (Required)
            sid: 亚马逊店铺sid，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "inboundPlanId": inboundPlanId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/amzStaServer/openapi/inbound-shipment/shipmentPreView",
            method="GET",
            req_body=params
        )


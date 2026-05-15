"""领星ERP仓库物流API端点封装"""

import logging
from typing import Any

logger = logging.getLogger(__name__)


class WarehouseEndpoints:

    def __init__(self, openapi_client):
        self._openapi = openapi_client

    async def get_warehouses(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询仓库列表

        API: POST /erp/sc/routing/data/local_inventory/warehouseLists

        Args:
            access_token: 访问令牌
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: 仓库列表

        Example:
            warehouses = await endpoint.get_warehouses(token, offset=0, length=50)
        """
        logger.debug("Fetching warehouses: offset=%s, length=%s", offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/warehouseLists",
            method="POST",
            req_body={
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch warehouses: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    async def get_warehouse_inventory(
        self,
        access_token: str,
        warehouse_id: int | None = None,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> dict[str, Any]:
        """
        查询仓库库存

        API: POST /erp/sc/routing/data/local_inventory/warehouseInventory

        Args:
            access_token: 访问令牌
            warehouse_id: 仓库ID（可选，不传则查询所有仓库）
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数

        Returns:
            Dict[str, Any]: 包含list（库存列表）和total（总数）的字典

        Example:
            inventory = await endpoint.get_warehouse_inventory(token, warehouse_id=123)
        """
        logger.debug("Fetching warehouse inventory: warehouse_id=%s, offset=%s, length=%s", warehouse_id, offset, length)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }
        if warehouse_id is not None:
            req_body["wid"] = warehouse_id

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/warehouseInventory",
            method="POST",
            req_body=req_body
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch warehouse inventory: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 返回完整响应数据（包含list和total）
        data = response.data or {}
        if isinstance(data, dict):
            return {
                "list": data.get("list", data.get("data", [])),
                "total": data.get("total", 0)
            }
        return {"list": data if isinstance(data, list) else [], "total": 0}

    async def get_batch_statement(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询库存流水

        API: POST /erp/sc/routing/data/local_inventory/getBatchStatementList

        Args:
            access_token: 访问令牌
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数（如start_date, end_date, wid等）

        Returns:
            List[Dict[str, Any]]: 库存流水列表

        Example:
            statements = await endpoint.get_batch_statement(
                token,
                start_date="2026-01-01",
                end_date="2026-01-31"
            )
        """
        logger.debug("Fetching batch statement: offset=%s, length=%s", offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/getBatchStatementList",
            method="POST",
            req_body={
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch batch statement: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    async def get_receipt_dispatch_lists(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询出入库单

        API: POST /erp/sc/routing/data/local_inventory/receiptDispatchLists

        Args:
            access_token: 访问令牌
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数（如start_date, end_date, wid, type等）

        Returns:
            List[Dict[str, Any]]: 出入库单列表

        Example:
            # 查询入库单
            receipts = await endpoint.get_receipt_dispatch_lists(token, type="receipt")
            # 查询出库单
            dispatches = await endpoint.get_receipt_dispatch_lists(token, type="dispatch")
        """
        logger.debug("Fetching receipt/dispatch lists: offset=%s, length=%s", offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/receiptDispatchLists",
            method="POST",
            req_body={
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch receipt/dispatch lists: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    async def get_allocation_lists(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询调拨单

        API: POST /erp/sc/routing/data/local_inventory/allocationLists

        Args:
            access_token: 访问令牌
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数（如start_date, end_date, status等）

        Returns:
            List[Dict[str, Any]]: 调拨单列表

        Example:
            allocations = await endpoint.get_allocation_lists(
                token,
                start_date="2026-01-01",
                end_date="2026-01-31",
                status=1  # 状态筛选
            )
        """
        logger.debug("Fetching allocation lists: offset=%s, length=%s", offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/allocationLists",
            method="POST",
            req_body={
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch allocation lists: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    # ========== FBA管理 ==========

    async def get_fba_inventory(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询FBA库存

        API: POST /erp/sc/routing/data/local_inventory/fbaInventory

        Args:
            access_token: 访问令牌
            sid: 店铺ID（必填）
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: FBA库存列表

        Example:
            fba_inventory = await endpoint.get_fba_inventory(token, sid=123456)
        """
        logger.debug("Fetching FBA inventory: sid=%s, offset=%s, length=%s", sid, offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/fbaInventory",
            method="POST",
            req_body={
                "sid": sid,
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch FBA inventory: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    async def get_shipment_plans(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> dict[str, Any]:
        """
        查询FBA发货计划

        API: POST /erp/sc/data/fba_report/shipmentPlanLists

        注意: 此接口使用page/page_size分页，而非offset/length

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认100）
            **kwargs: 其他查询参数（如sid, status等）

        Returns:
            Dict[str, Any]: 包含list（发货计划列表）和total（总数）的字典

        Example:
            plans = await endpoint.get_shipment_plans(token, page=1, page_size=50)
        """
        logger.debug("Fetching shipment plans: page=%s, page_size=%s", page, page_size)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/shipmentPlanLists",
            method="POST",
            req_body={
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch shipment plans: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 返回完整响应数据（包含list和total）
        data = response.data or {}
        if isinstance(data, dict):
            return {
                "list": data.get("list", data.get("data", [])),
                "total": data.get("total", 0)
            }
        return {"list": data if isinstance(data, list) else [], "total": 0}

    async def get_replenish_suggestions(
        self,
        access_token: str,
        data_type: int = 2,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询补货建议

        API: POST /erp/sc/routing/restocking/analysis/getSummaryList

        Args:
            access_token: 访问令牌
            data_type: 数据类型（1=asin维度, 2=msku维度，默认2）
            offset: 偏移量（默认0）
            length: 返回数量（默认100，最大100）
            **kwargs: 其他查询参数（如sid等）

        Returns:
            List[Dict[str, Any]]: 补货建议列表

        Example:
            # MSKU维度
            suggestions = await endpoint.get_replenish_suggestions(token, data_type=2)
            # ASIN维度
            suggestions = await endpoint.get_replenish_suggestions(token, data_type=1)
        """
        logger.debug("Fetching replenish suggestions: data_type=%s, offset=%s, length=%s", data_type, offset, length)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            method="POST",
            req_body={
                "data_type": data_type,
                "offset": offset,
                "length": length,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch replenish suggestions: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 解析响应数据
        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

    async def get_inbound_shipments(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> dict[str, Any]:
        """
        查询入库货件列表

        API: POST /erp/sc/routing/storage/shipment/getInboundShipmentList

        Args:
            access_token: 访问令牌
            start_date: 开始日期（格式：YYYY-MM-DD）
            end_date: 结束日期（格式：YYYY-MM-DD）
            page: 页码（默认1）
            page_size: 每页数量（默认100）
            **kwargs: 其他查询参数（如sid, shipment_status等）

        Returns:
            Dict[str, Any]: 包含list（入库货件列表）和total（总数）的字典

        Example:
            shipments = await endpoint.get_inbound_shipments(
                token,
                start_date="2026-01-01",
                end_date="2026-01-31"
            )
        """
        logger.debug("Fetching inbound shipments: start=%s, end=%s, page=%s", start_date, end_date, page)

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentList",
            method="POST",
            req_body={
                "start_date": start_date,
                "end_date": end_date,
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if response.code not in [200, "200"]:
            logger.error("Failed to fetch inbound shipments: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 返回完整响应数据（包含list和total）
        data = response.data or {}
        if isinstance(data, dict):
            return {
                "list": data.get("list", data.get("data", [])),
                "total": data.get("total", 0)
            }
        return {"list": data if isinstance(data, list) else [], "total": 0}

    async def get_fba_warehouse_detail(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        sid: int | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        查询FBA库存明细

        API: POST /basicOpen/openapi/storage/fbaWarehouseDetail

        对应系统【仓库】>【FBA库存明细】数据,数量维度展示

        Args:
            access_token: 访问令牌
            offset: 分页偏移量（默认0）
            length: 分页长度（默认100，取值范围[20,200]）
            sid: 店铺ID（可选）
            **kwargs: 其他查询参数（如search_field, search_value, cid, bid等）

        Returns:
            Dict[str, Any]: 包含list（FBA库存列表）和total（总数）的字典

        Example:
            # 查询所有FBA库存
            inventory = await endpoint.get_fba_warehouse_detail(token)

            # 按店铺查询
            inventory = await endpoint.get_fba_warehouse_detail(token, sid=123)

            # 按SKU搜索
            inventory = await endpoint.get_fba_warehouse_detail(
                token,
                search_field="seller_sku",
                search_value="MSKUFDA5E30"
            )
        """
        logger.debug("Fetching FBA warehouse detail: offset=%s, length=%s, sid=%s", offset, length, sid)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }
        if sid is not None:
            req_body["sid"] = sid

        response = await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/storage/fbaWarehouseDetail",
            method="POST",
            req_body=req_body
        )

        if response.code not in [0, 200, "0", "200"]:
            logger.error("Failed to fetch FBA warehouse detail: %s", response.message)
            raise Exception(f"API error: {response.message}")

        # 返回完整响应数据（包含list和total）
        data = response.data or {}
        if isinstance(data, list):
            return {
                "list": data,
                "total": response.data.get("total", len(data)) if isinstance(response.data, dict) else len(data)
            }
        if isinstance(data, dict):
            return {
                "list": data.get("data", data.get("list", [])),
                "total": data.get("total", 0)
            }
        return {"list": [], "total": 0}


__all__ = [
    "WarehouseEndpoints",
]

"""
领星ERP客户端高级封装

提供领星API的高级访问接口，委托 OpenApiBase 进行 token 管理和请求发送。
Author: AI Platform Team
Date: 2026-02-17
"""

import logging
from datetime import datetime
from typing import Any

from .config import LingXingConfig, get_config
from .models.business import (
    AllocationOrderInfo,
    FBAShipment,
    InboundShipmentInfo,
    InventoryInfo,
    LingXingResponse,
    LogisticsChannelInfo,
    LogisticsProviderInfo,
    MSKUProfitInfo,
    OrderInfo,
    OrderProfitInfo,
    ProductInfo,
    PurchaseOrderInfo,
    PurchasePlanInfo,
    PurchaseReturnInfo,
    SettlementInfo,
    SettlementSummaryInfo,
    ShipmentDetailInfo,
    StoreInfo,
    SupplierInfo,
    WarehouseInfo,
    WarehouseInventoryInfo,
    WarehouseStatementInfo,
)

logger = logging.getLogger(__name__)

from .core.openapi import OpenApiBase  # noqa: E402
from .core.param_builder import APIParamBuilder  # noqa: E402


class LingXingClient:
    """
    领星ERP客户端

    提供统一的领星API访问接口，自动处理token管理和请求重试。
    Token管理完全委托给 OpenApiBase，不再重复维护。
    """

    def __init__(self, config: LingXingConfig | None = None):
        """
        初始化客户端

        Args:
            config: 领星配置，如果为None则使用默认配置
        """
        self.config = config or get_config()

        # 创建OpenAPI基础客户端（负责token管理、限流、请求发送）
        self._openapi = OpenApiBase(
            host=self.config.host,
            app_id=self.config.app_id,
            app_secret=self.config.app_secret,
        )

        # 参数构建器
        self._param_builder = APIParamBuilder()

    def set_default_sids(self, sids: list[int]) -> None:
        """
        设置默认店铺ID列表

        Args:
            sids: 店铺ID列表
        """
        self._param_builder = APIParamBuilder(default_sids=sids)

    @property
    def openapi(self) -> OpenApiBase:
        """直接访问底层 OpenApiBase 实例，用于 endpoint 模式。"""
        return self._openapi

    async def connect(self) -> bool:
        """
        建立连接并验证访问令牌

        Returns:
            bool: 连接是否成功
        """
        try:
            logger.info("Connecting to LingXing ERP: %s", self.config.host)
            # 触发 token 获取，验证凭据有效
            await self._openapi.get_valid_token()
            logger.info("Connected to LingXing ERP successfully")
        except Exception:
            logger.exception("Failed to connect to LingXing ERP")
            return False
        else:
            return True

    async def disconnect(self) -> None:
        """断开连接，清除缓存的token"""
        self._openapi._access_token = None
        self._openapi._refresh_token = None
        self._openapi._token_expires_at = None
        logger.info("Disconnected from LingXing ERP")

    async def health_check(self) -> bool:
        """
        检查连接健康状态

        Returns:
            bool: 是否健康
        """
        try:
            await self.get_stores(limit=1)
            return True
        except Exception as e:
            logger.debug("Health check failed: %s", e)
            return False

    async def execute(
        self,
        operation: str,
        **kwargs
    ) -> dict[str, Any]:
        """
        执行操作

        Args:
            operation: 操作名称
            **kwargs: 操作参数

        Returns:
            Dict[str, Any]: 操作结果
        """
        if operation == "get_products":
            return await self.get_products(**kwargs)
        if operation == "get_orders":
            return await self.get_orders(**kwargs)
        if operation == "get_inventory":
            return await self.get_inventory(**kwargs)
        if operation == "get_fba_shipments":
            return await self.get_fba_shipments(**kwargs)
        if operation == "get_stores":
            return await self.get_stores(**kwargs)
        msg = f"Unknown operation: {operation}"
        raise ValueError(msg)

    # ==================== API请求封装 ====================

    async def _request(
        self,
        route_name: str,
        method: str = "GET",
        req_params: dict[str, Any] | None = None,
        req_body: dict[str, Any] | None = None,
        **kwargs
    ) -> LingXingResponse:
        """
        发起API请求 — 委托 OpenApiBase 处理token和限流

        Args:
            route_name: API路由名称
            method: HTTP方法
            req_params: 查询参数
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            LingXingResponse: API响应
        """
        resp_result = await self._openapi.request_with_auto_token(
            route_name=route_name,
            method=method,
            req_params=req_params,
            req_body=req_body,
        )

        return LingXingResponse(
            code=resp_result.code,
            message=resp_result.message,
            data=resp_result.data,
            request_id=resp_result.request_id,
        )


    async def call_api(
        self,
        api_path: str,
        method: str = "POST",
        params: dict[str, Any] | None = None,
        param_names: set | None = None,
        **kwargs
    ) -> LingXingResponse:
        """
        调用API（使用参数构建器自动补全参数）

        Args:
            api_path: API路径
            method: HTTP方法
            params: 原始参数
            param_names: 参数名称集合（从API文档解析，如不提供则不自动补全）
            **kwargs: 其他参数

        Returns:
            LingXingResponse: API响应

        Example:
            # 使用参数构建器
            response = await client.call_api(
                api_path="/bd/profit/report/open/report/msku/list",
                params={"sids": [4661]},
                param_names={"sids", "startDate", "endDate", "offset", "length"}
            )
        """
        params = params or {}

        # 如果提供了param_names，使用参数构建器
        if param_names:
            params = self._param_builder.build_params(api_path, params, param_names)

        # 根据方法类型选择参数位置
        if method.upper() == "GET":
            return await self._request(
                route_name=api_path,
                method="GET",
                req_params=params,
                **kwargs
            )
        return await self._request(
            route_name=api_path,
            method="POST",
            req_body=params,
            **kwargs
        )

    # ==================== 产品API ====================

    async def get_products(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[ProductInfo]:
        """
        获取产品列表

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[ProductInfo]: 产品列表
        """
        logger.debug("Fetching products: page=%s, page_size=%s", page, page_size)

        # 根据实际API路径调整, 基于SDK测试和API文档
        response = await self._request(
            route_name="/erp/sc/routing/data/local_inventory/productList",
            method="POST",
            req_body={
                "offset": (page - 1) * page_size,
                "length": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch products: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        products = []
        data = response.data or {}

        if isinstance(data, list):
            products = [ProductInfo(**item) for item in data]
        elif isinstance(data, dict) and "data" in data:
            products = [ProductInfo(**item) for item in data["data"]]

        return products

    # ==================== 订单API ====================

    async def get_orders(
        self,
        page: int = 1,
        page_size: int = 100,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
        **kwargs
    ) -> list[OrderInfo]:
        """
        获取订单列表

        Args:
            page: 页码
            page_size: 每页数量
            start_date: 开始日期
            end_date: 结束日期
            **kwargs: 其他查询参数

        Returns:
            List[OrderInfo]: 订单列表
        """
        logger.debug("Fetching orders: page=%s, page_size=%s", page, page_size)

        req_params = {
            "page": page,
            "pageSize": page_size,
            **kwargs
        }

        if start_date:
            req_params["startDate"] = start_date.isoformat()
        if end_date:
            req_params["endDate"] = end_date.isoformat()

        response = await self._request(
            route_name="/erp/sc/data/order/lists",
            method="GET",
            req_params=req_params
        )

        if not response.is_success:
            logger.error("Failed to fetch orders: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        orders = []
        data = response.data or {}

        if isinstance(data, list):
            orders = [OrderInfo(**item) for item in data]
        elif isinstance(data, dict) and "data" in data:
            orders = [OrderInfo(**item) for item in data["data"]]

        return orders

    # ==================== 库存API ====================

    async def get_inventory(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[InventoryInfo]:
        """
        获取库存列表

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[InventoryInfo]: 库存列表
        """
        logger.debug("Fetching inventory: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/data/local_inventory/lists",
            method="GET",
            req_params={
                "page": page,
                "pageSize": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch inventory: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        inventory_items = []
        data = response.data or {}

        if isinstance(data, list):
            inventory_items = [InventoryInfo(**item) for item in data]
        elif isinstance(data, dict) and "data" in data:
            inventory_items = [InventoryInfo(**item) for item in data["data"]]

        return inventory_items

    # ==================== FBA API ====================

    async def get_fba_shipments(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[FBAShipment]:
        """
        获取FBA发货计划列表

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[FBAShipment]: 发货计划列表
        """
        logger.debug("Fetching FBA shipments: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/basicOpen/openapi/storage/fbaWarehouseDetail",
            method="POST",
            req_body={
                "page": page,
                "pageSize": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch FBA shipments: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        shipments = []
        data = response.data or {}

        if isinstance(data, list):
            shipments = [FBAShipment(**item) for item in data]
        elif isinstance(data, dict) and "data" in data:
            shipments = [FBAShipment(**item) for item in data["data"]]

        return shipments

    # ==================== 店铺API ====================

    async def get_stores(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[StoreInfo]:
        """
        获取店铺列表

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[StoreInfo]: 店铺列表
        """
        logger.debug("Fetching stores: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/data/seller/lists",
            method="GET",
            req_params={
                "page": page,
                "pageSize": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch stores: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        stores = []
        data = response.data or {}

        if isinstance(data, list):
            stores = [StoreInfo(**item) for item in data]
        elif isinstance(data, dict) and "data" in data:
            stores = [StoreInfo(**item) for item in data["data"]]

        return stores

    async def get_sellers(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        获取店铺列表（返回原始字典，用于ETL）

        Note: 与 get_stores() 调用相同的API，但返回原始字典而非StoreInfo对象

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: 店铺列表（原始字典格式）
        """
        logger.debug("Fetching sellers: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/data/seller/lists",
            method="GET",
            req_params={
                "page": page,
                "pageSize": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch sellers: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 返回原始字典数据（用于ETL场景）
        data = response.data or {}

        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]

        return []

    # ==================== 仓库/本地库存API ====================

    async def get_warehouse_list(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[WarehouseInfo]:
        """
        获取仓库列表

        API: /erp/sc/data/local_inventory/warehouse (POST)

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[WarehouseInfo]: 仓库列表
        """
        logger.debug("Fetching warehouse list: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/data/local_inventory/warehouse",
            method="POST",
            req_body={
                "offset": (page - 1) * page_size,
                "length": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch warehouse list: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        warehouses = []
        data = response.data or {}

        if isinstance(data, list):
            warehouses = [WarehouseInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            warehouses = [WarehouseInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            warehouses = [WarehouseInfo(**item) for item in data["data"]]

        return warehouses

    async def get_warehouse_inventory(
        self,
        warehouse_id: str | None = None,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[WarehouseInventoryInfo]:
        """
        获取仓库库存明细

        API: /erp/sc/routing/data/local_inventory/inventoryDetails (POST)

        Args:
            warehouse_id: 仓库ID（可选，不传则获取所有仓库）
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[WarehouseInventoryInfo]: 仓库库存明细列表
        """
        logger.debug("Fetching warehouse inventory: warehouse_id=%s, page=%s, page_size=%s", warehouse_id, page, page_size)

        req_body = {
            "offset": (page - 1) * page_size,
            "length": page_size,
            **kwargs
        }
        if warehouse_id:
            req_body["wid"] = warehouse_id

        response = await self._request(
            route_name="/erp/sc/routing/data/local_inventory/inventoryDetails",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch warehouse inventory: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        inventory_items = []
        data = response.data or {}

        if isinstance(data, list):
            inventory_items = [WarehouseInventoryInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            inventory_items = [WarehouseInventoryInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            inventory_items = [WarehouseInventoryInfo(**item) for item in data["data"]]

        return inventory_items

    async def get_inventory_statement(
        self,
        start_date: datetime,
        end_date: datetime,
        warehouse_id: str | None = None,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[WarehouseStatementInfo]:
        """
        获取库存流水

        API: /erp/sc/routing/data/local_inventory/getBatchStatementList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            warehouse_id: 仓库ID（可选）
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[WarehouseStatementInfo]: 库存流水列表
        """
        logger.debug("Fetching inventory statement: start=%s, end=%s, page=%s", start_date, end_date, page)

        req_body = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "offset": (page - 1) * page_size,
            "length": page_size,
            **kwargs
        }
        if warehouse_id:
            req_body["wid"] = warehouse_id

        response = await self._request(
            route_name="/erp/sc/routing/data/local_inventory/getBatchStatementList",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch inventory statement: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        statements = []
        data = response.data or {}

        if isinstance(data, list):
            statements = [WarehouseStatementInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            statements = [WarehouseStatementInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            statements = [WarehouseStatementInfo(**item) for item in data["data"]]

        return statements

    async def get_allocation_orders(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[AllocationOrderInfo]:
        """
        获取调拨单列表

        API: /erp/sc/data/wms/allocation/getStorageAllocationList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[AllocationOrderInfo]: 调拨单列表
        """
        logger.debug("Fetching allocation orders: start=%s, end=%s, page=%s", start_date, end_date, page)

        response = await self._request(
            route_name="/erp/sc/data/wms/allocation/getStorageAllocationList",
            method="POST",
            req_body={
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch allocation orders: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        orders = []
        data = response.data or {}

        if isinstance(data, list):
            orders = [AllocationOrderInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            orders = [AllocationOrderInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            orders = [AllocationOrderInfo(**item) for item in data["data"]]

        return orders

    # ==================== 头程物流API ====================

    async def get_inbound_shipments(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[InboundShipmentInfo]:
        """
        获取FBA发货单列表 - 包含头程费用信息

        API: /erp/sc/routing/storage/shipment/getInboundShipmentList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[InboundShipmentInfo]: 发货单列表
        """
        logger.debug("Fetching inbound shipments: start=%s, end=%s, page=%s", start_date, end_date, page)

        offset = (page - 1) * page_size
        response = await self._request(
            route_name="/erp/sc/routing/storage/shipment/getInboundShipmentList",
            method="POST",
            req_body={
                "time_type": 2,  # 创建时间
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "offset": offset,
                "length": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch inbound shipments: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        shipments = []
        data = response.data or {}

        if isinstance(data, list):
            shipments = [InboundShipmentInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            shipments = [InboundShipmentInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            shipments = [InboundShipmentInfo(**item) for item in data["data"]]

        return shipments

    async def get_shipment_details(
        self,
        shipment_id: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[ShipmentDetailInfo]:
        """
        获取发货单详情 - SKU级别的运费分配

        API: /basicOpen/openapi/fba/getInboundShipmentListMwsDetail

        Args:
            shipment_id: 发货单ID
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[ShipmentDetailInfo]: 发货单明细列表
        """
        logger.debug("Fetching shipment details: shipment_id=%s, page=%s", shipment_id, page)

        response = await self._request(
            route_name="/basicOpen/openapi/fba/getInboundShipmentListMwsDetail",
            method="POST",
            req_body={
                "shipment_id": shipment_id,
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch shipment details: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        details = []
        data = response.data or {}

        if isinstance(data, list):
            details = [ShipmentDetailInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            details = [ShipmentDetailInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            details = [ShipmentDetailInfo(**item) for item in data["data"]]

        return details

    async def get_logistics_providers(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[LogisticsProviderInfo]:
        """
        获取头程物流商列表

        API: /basicOpen/logistics/headLogisticsProvider/query/list

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[LogisticsProviderInfo]: 物流商列表
        """
        logger.debug("Fetching logistics providers: page=%s", page)

        response = await self._request(
            route_name="/basicOpen/logistics/headLogisticsProvider/query/list",
            method="POST",
            req_body={
                "search": {
                    "page": page,
                    "length": page_size,
                    **kwargs
                }
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch logistics providers: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        providers = []
        data = response.data or {}

        # 新 API 格式: {"data": {"providers": [...], "total": N}}
        if isinstance(data, dict) and "providers" in data:
            providers = [LogisticsProviderInfo(**item) for item in data["providers"]]
        elif isinstance(data, list):
            providers = [LogisticsProviderInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            providers = [LogisticsProviderInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            providers = [LogisticsProviderInfo(**item) for item in data["data"]]

        return providers

    async def get_logistics_channels(
        self,
        provider_id: str | None = None,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[LogisticsChannelInfo]:
        """
        获取头程物流渠道列表

        API: /erp/sc/data/local_inventory/channelList

        Args:
            provider_id: 物流商ID（可选）
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[LogisticsChannelInfo]: 物流渠道列表
        """
        logger.debug("Fetching logistics channels: provider_id=%s, page=%s", provider_id, page)

        offset = (page - 1) * page_size
        req_body = {
            "offset": offset,
            "length": page_size,
            **kwargs
        }
        if provider_id:
            req_body["provider_id"] = provider_id

        response = await self._request(
            route_name="/erp/sc/data/local_inventory/channelList",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch logistics channels: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        channels = []
        data = response.data or {}

        if isinstance(data, list):
            channels = [LogisticsChannelInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            channels = [LogisticsChannelInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            channels = [LogisticsChannelInfo(**item) for item in data["data"]]

        return channels

    # ==================== 采购/1688 API ====================

    async def get_purchase_orders(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[PurchaseOrderInfo]:
        """
        获取采购单列表 - 包含1688采购订单

        API: /erp/sc/purchase/order/lists

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[PurchaseOrderInfo]: 采购单列表
        """
        logger.debug("Fetching purchase orders: start=%s, end=%s, page=%s", start_date, end_date, page)

        response = await self._request(
            route_name="/erp/sc/purchase/order/lists",
            method="POST",
            req_body={
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch purchase orders: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        orders = []
        data = response.data or {}

        if isinstance(data, list):
            orders = [PurchaseOrderInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            orders = [PurchaseOrderInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            orders = [PurchaseOrderInfo(**item) for item in data["data"]]

        return orders

    async def get_suppliers(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[SupplierInfo]:
        """
        获取供应商列表

        API: /erp/sc/purchase/supplier/lists

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[SupplierInfo]: 供应商列表
        """
        logger.debug("Fetching suppliers: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/purchase/supplier/lists",
            method="GET",
            req_params={
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch suppliers: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        suppliers = []
        data = response.data or {}

        if isinstance(data, list):
            suppliers = [SupplierInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            suppliers = [SupplierInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            suppliers = [SupplierInfo(**item) for item in data["data"]]

        return suppliers

    async def get_purchase_plans(
        self,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[PurchasePlanInfo]:
        """
        获取采购计划列表

        API: /erp/sc/purchase/plan/getPurchasePlans

        Args:
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[PurchasePlanInfo]: 采购计划列表
        """
        logger.debug("Fetching purchase plans: page=%s, page_size=%s", page, page_size)

        response = await self._request(
            route_name="/erp/sc/purchase/plan/getPurchasePlans",
            method="GET",
            req_params={
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch purchase plans: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        plans = []
        data = response.data or {}

        if isinstance(data, list):
            plans = [PurchasePlanInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            plans = [PurchasePlanInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            plans = [PurchasePlanInfo(**item) for item in data["data"]]

        return plans

    async def get_purchase_returns(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[PurchaseReturnInfo]:
        """
        获取采购退货单列表

        API: /erp/sc/purchase/return/getPurchaseReturnOrderList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[PurchaseReturnInfo]: 采购退货单列表
        """
        logger.debug("Fetching purchase returns: start=%s, end=%s, page=%s", start_date, end_date, page)

        response = await self._request(
            route_name="/erp/sc/purchase/return/getPurchaseReturnOrderList",
            method="POST",
            req_body={
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "page": page,
                "page_size": page_size,
                **kwargs
            }
        )

        if not response.is_success:
            logger.error("Failed to fetch purchase returns: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        returns = []
        data = response.data or {}

        if isinstance(data, list):
            returns = [PurchaseReturnInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            returns = [PurchaseReturnInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            returns = [PurchaseReturnInfo(**item) for item in data["data"]]

        return returns

    # ==================== 财务利润API ====================

    async def get_order_profit(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[OrderProfitInfo]:
        """
        获取订单维度利润数据

        API: /erp/sc/data/finance/bdOrder

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[OrderProfitInfo]: 订单利润列表
        """
        logger.debug("Fetching order profit: start=%s, end=%s, page=%s", start_date, end_date, page)

        # 使用参数构建器构建请求参数
        param_names: set[str] = {'start_date', 'end_date', 'page', 'page_size'}
        params = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'page': page,
            'page_size': page_size,
            **kwargs
        }
        req_body = self._param_builder.build_params(
            "/erp/sc/data/finance/bdOrder",
            params,
            param_names
        )

        response = await self._request(
            route_name="/erp/sc/data/finance/bdOrder",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch order profit: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        profits = []
        data = response.data or {}

        if isinstance(data, list):
            profits = [OrderProfitInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            profits = [OrderProfitInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            profits = [OrderProfitInfo(**item) for item in data["data"]]

        return profits

    async def get_msku_profit(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[MSKUProfitInfo]:
        """
        获取MSKU维度利润数据

        API: /erp/sc/data/finance/bdMSKU

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[MSKUProfitInfo]: MSKU利润列表
        """
        logger.debug("Fetching MSKU profit: start=%s, end=%s, page=%s", start_date, end_date, page)

        # 使用参数构建器构建请求参数
        param_names: set[str] = {'start_date', 'end_date', 'page', 'page_size'}
        params = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'page': page,
            'page_size': page_size,
            **kwargs
        }
        req_body = self._param_builder.build_params(
            "/erp/sc/data/finance/bdMSKU",
            params,
            param_names
        )

        response = await self._request(
            route_name="/erp/sc/data/finance/bdMSKU",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch MSKU profit: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        profits = []
        data = response.data or {}

        if isinstance(data, list):
            profits = [MSKUProfitInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            profits = [MSKUProfitInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            profits = [MSKUProfitInfo(**item) for item in data["data"]]

        return profits

    async def get_settlement_detail(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[SettlementInfo]:
        """
        获取结算明细/亚马逊回款数据

        API: /erp/sc/data/finance/settlementTransactionList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[SettlementInfo]: 结算明细列表
        """
        logger.debug("Fetching settlement detail: start=%s, end=%s, page=%s", start_date, end_date, page)

        # 使用参数构建器构建请求参数
        param_names: set[str] = {'start_date', 'end_date', 'page', 'page_size'}
        params = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'page': page,
            'page_size': page_size,
            **kwargs
        }
        req_body = self._param_builder.build_params(
            "/erp/sc/data/finance/settlementTransactionList",
            params,
            param_names
        )

        response = await self._request(
            route_name="/erp/sc/data/finance/settlementTransactionList",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch settlement detail: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        settlements = []
        data = response.data or {}

        if isinstance(data, list):
            settlements = [SettlementInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            settlements = [SettlementInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            settlements = [SettlementInfo(**item) for item in data["data"]]

        return settlements

    async def get_settlement_summary(
        self,
        start_date: datetime,
        end_date: datetime,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[SettlementSummaryInfo]:
        """
        获取结算汇总数据

        API: /erp/sc/data/finance/settlementSummaryList

        Args:
            start_date: 开始日期
            end_date: 结束日期
            page: 页码
            page_size: 每页数量
            **kwargs: 其他查询参数

        Returns:
            List[SettlementSummaryInfo]: 结算汇总列表
        """
        logger.debug("Fetching settlement summary: start=%s, end=%s, page=%s", start_date, end_date, page)

        # 使用参数构建器构建请求参数
        param_names: set[str] = {'start_date', 'end_date', 'page', 'page_size'}
        params = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d"),
            'page': page,
            'page_size': page_size,
            **kwargs
        }
        req_body = self._param_builder.build_params(
            "/erp/sc/data/finance/settlementSummaryList",
            params,
            param_names
        )

        response = await self._request(
            route_name="/erp/sc/data/finance/settlementSummaryList",
            method="POST",
            req_body=req_body
        )

        if not response.is_success:
            logger.error("Failed to fetch settlement summary: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        # 解析响应数据
        summaries = []
        data = response.data or {}

        if isinstance(data, list):
            summaries = [SettlementSummaryInfo(**item) for item in data]
        elif isinstance(data, dict) and "list" in data:
            summaries = [SettlementSummaryInfo(**item) for item in data["list"]]
        elif isinstance(data, dict) and "data" in data:
            summaries = [SettlementSummaryInfo(**item) for item in data["data"]]

        return summaries

    async def get_product_performance(
        self,
        sid: Any,
        start_date: str,
        end_date: str,
        summary_field: str = "msku",
        offset: int = 0,
        length: int = 10000,
        sort_field: str = "volume",
        sort_type: str = "desc",
        is_recently_enum: bool = True,
        **kwargs
    ) -> dict[str, Any]:
        """
        获取产品表现数据

        API: /bd/productPerformance/openApi/asinList

        Args:
            sid: 店铺ID，单店铺传字符串，多店铺传数组
            start_date: 开始日期，格式：YYYY-MM-DD
            end_date: 结束日期，格式：YYYY-MM-DD
            summary_field: 汇总维度，可选：asin, parent_asin, msku, sku
            offset: 分页偏移量
            length: 分页长度，最大10000
            sort_field: 排序字段，默认按volume排序
            sort_type: 排序方式，desc降序/asc升序
            is_recently_enum: 是否仅查询活跃商品，true仅活跃/false全部
            **kwargs: 其他查询参数

        Returns:
            Dict[str, Any]: 产品表现数据

        Note:
            - 限流要求：串行调用，单店铺间隔1s，多店铺间隔10s
            - 时间范围不能超过92天
            - summary_field为asin时，search_field不可为parent_asin
        """
        logger.debug("Fetching product performance: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        # 构建请求参数
        params = {
            'offset': offset,
            'length': length,
            'sort_field': sort_field,
            'sort_type': sort_type,
            'sid': sid,
            'start_date': start_date,
            'end_date': end_date,
            'summary_field': summary_field,
            'is_recently_enum': is_recently_enum,
            **kwargs
        }

        # 定义参数名称集合（用于参数构建器）
        param_names = {
            'offset', 'length', 'sort_field', 'sort_type', 'sid',
            'start_date', 'end_date', 'summary_field', 'is_recently_enum',
            'search_field', 'search_value', 'mid', 'extend_search',
            'currency_code', 'purchase_status'
        }

        # 调用API（使用参数构建器）
        response = await self.call_api(
            api_path='/bd/productPerformance/openApi/asinList',
            method='POST',
            params=params,
            param_names=param_names
        )

        # 检查响应
        if not response.is_success:
            logger.error("Product performance API failed: %s", response.message)
            msg = f"API error: {response.message}"
            raise Exception(msg)

        return response.data if isinstance(response.data, dict) else {}


__all__ = [
    "LingXingClient",
]

"""多平台API端点封装"""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class MultiPlatformEndpoints:
    """
    多平台API端点封装

    封装领星ERP多平台集成相关的所有API接口，支持Temu、Shein、TikTok等平台。

    使用示例:
        >>> openapi = OpenApiBase(host, app_id, app_secret)
        >>> multi = MultiPlatformEndpoints(openapi)
        >>> temu_products = await multi.get_temu_products(
        ...     access_token,
        ...     page=1,
        ...     page_size=20
        ... )
    """

    def __init__(self, openapi: OpenApiBase):
        """
        初始化多平台端点

        Args:
            openapi: OpenAPI基础客户端实例
        """
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== Temu 平台 ====================

    async def get_temu_products(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询Temu在线商品列表

        API: POST /basicOpen/multiplatform/temu/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: Temu商品列表

        Example:
            >>> result = await multi.get_temu_products(token)
            >>> for product in result.data.get('list', []):
            ...     print(f"商品: {product.get('title')}")
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/temu/list",
            req_body
        )

    async def get_temu_inventory(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询Temu库存(FBT)

        API: POST /basicOpen/multiplatform/fbt/stockSearch
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: Temu库存列表

        Example:
            >>> result = await multi.get_temu_inventory(token)
            >>> for item in result.data.get('list', []):
            ...     print(f"SKU: {item.get('sku')}, 库存: {item.get('quantity')}")
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/fbt/stockSearch",
            req_body
        )

    # ==================== Shein 平台 ====================

    async def get_shein_products(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询Shein在线商品列表

        API: POST /basicOpen/multiplatform/shein/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: Shein商品列表

        Example:
            >>> result = await multi.get_shein_products(token)
            >>> for product in result.data.get('list', []):
            ...     print(f"商品: {product.get('title')}")
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/shein/list",
            req_body
        )

    # ==================== TikTok 平台 ====================

    async def get_tiktok_products(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询TikTok在线商品列表

        API: POST /basicOpen/multiplatform/tiktok/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: TikTok商品列表

        Example:
            >>> result = await multi.get_tiktok_products(token)
            >>> for product in result.data.get('list', []):
            ...     print(f"商品: {product.get('title')}")
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/tiktok/list",
            req_body
        )

    # ==================== 平台订单 ====================

    async def get_platform_orders(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        platform: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        查询平台订单列表

        API: POST /cepfPlatformOrder/open-api/newPlatformOrder/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            platform: 平台类型（可选）
            **kwargs: 其他参数

        Returns:
            ResponseResult: 平台订单列表

        Example:
            >>> result = await multi.get_platform_orders(token)
            >>> for order in result.data.get('list', []):
            ...     print(f"订单号: {order.get('order_id')}")
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        if platform:
            req_body["platform"] = platform

        return await self._request_with_token(
            access_token,
            "/cepfPlatformOrder/open-api/newPlatformOrder/list",
            req_body
        )

    # ==================== 通用库存查询 ====================

    async def get_fbs_inventory(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        多平台-查询FBS库存

        API: POST /basicOpen/multiplatform/fbs/stockSearch

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: FBS库存列表
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/fbs/stockSearch",
            req_body
        )

    async def get_coupang_inventory(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        多平台-查询Coupang库存

        API: POST /basicOpen/multiplatform/coupang/stockSearch

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认20）
            **kwargs: 其他参数

        Returns:
            ResponseResult: Coupang库存列表
        """
        req_body = {
            "page": page,
            "page_size": page_size,
            **kwargs
        }
        return await self._request_with_token(
            access_token,
            "/basicOpen/multiplatform/coupang/stockSearch",
            req_body
        )

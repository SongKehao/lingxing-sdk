"""Auto-generated ProductEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class ProductEndpoints:
    """领星API - ProductEndpoints (23个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def add_commodity_code(self, **kwargs) -> dict:
        """AddCommodityCode.
        
        POST /listing/publish/api/upc/addCommodityCode
        """
        return await self._request_with_token(
            route_name="/listing/publish/api/upc/addCommodityCode",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def brand(self, **kwargs) -> dict:
        """Brand.
        
        POST /erp/sc/data/local_inventory/brand
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/local_inventory/brand",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def category(self, **kwargs) -> dict:
        """Category.
        
        POST /erp/sc/routing/data/local_inventory/category
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/category",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_paging_log_lists(self, **kwargs) -> dict:
        """GetPagingLogLists.
        
        POST /basicOpen/product/getPagingLogLists
        """
        return await self._request_with_token(
            route_name="/basicOpen/product/getPagingLogLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_details(self, **kwargs) -> dict:
        """ProductDetails.
        
        POST /erp/sc/routing/data/local_inventory/productInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/productInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_lists(self, **kwargs) -> dict:
        """ProductLists.
        
        POST /erp/sc/routing/data/local_inventory/productList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/productList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_brand(self, **kwargs) -> dict:
        """SetBrand.
        
        POST /erp/sc/storage/brand/set
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/brand/set",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_bundled(self, **kwargs) -> dict:
        """SetBundled.
        
        POST /erp/sc/routing/storage/product/setBundled
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/product/setBundled",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_category(self, **kwargs) -> dict:
        """SetCategory.
        
        POST /erp/sc/routing/storage/category/set
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/category/set",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_product(self, **kwargs) -> dict:
        """SetProduct.
        
        POST /erp/sc/routing/storage/product/set
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/product/set",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def upc_list(self, **kwargs) -> dict:
        """UpcList.
        
        POST /listing/publish/api/upc/upcList
        """
        return await self._request_with_token(
            route_name="/listing/publish/api/upc/upcList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def upload_pictures(self, **kwargs) -> dict:
        """UploadPictures.
        
        POST /erp/sc/routing/storage/product/uploadPictures
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/product/uploadPictures",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def attribute_list(self, **kwargs) -> dict:
        """attributeList.
        
        POST /erp/sc/routing/storage/attribute/attributeList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/attribute/attributeList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def attribute_set(self, **kwargs) -> dict:
        """attributeSet.
        
        POST /erp/sc/routing/storage/attribute/set
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/attribute/set",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def batch_get_product_info(self, **kwargs) -> dict:
        """batchGetProductInfo.
        
        POST /erp/sc/routing/data/local_inventory/batchGetProductInfo
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/batchGetProductInfo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def bundled_product_list(self, **kwargs) -> dict:
        """bundledProductList.
        
        POST /erp/sc/routing/data/local_inventory/bundledProductList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/bundledProductList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_transparency_product_list(self, **kwargs) -> dict:
        """getTransparencyProductList.
        
        POST /basicOpen/product/getTransparencyProductList
        """
        return await self._request_with_token(
            route_name="/basicOpen/product/getTransparencyProductList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_aux_list(self, **kwargs) -> dict:
        """productAuxList.
        
        POST /erp/sc/routing/data/local_inventory/productAuxList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/data/local_inventory/productAuxList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_operate_batch(self, **kwargs) -> dict:
        """productOperateBatch.
        
        POST /basicOpen/product/productManager/product/operate/batch
        """
        return await self._request_with_token(
            route_name="/basicOpen/product/productManager/product/operate/batch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_aux(self, **kwargs) -> dict:
        """setAux.
        
        POST /erp/sc/routing/storage/product/setAux
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/product/setAux",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def spu_info(self, **kwargs) -> dict:
        """spuInfo.
        
        POST /erp/sc/routing/storage/spu/info
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/spu/info",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def spu_list(self, **kwargs) -> dict:
        """spuList.
        
        POST /erp/sc/routing/storage/spu/spuList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/spu/spuList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def spu_set(self, **kwargs) -> dict:
        """spuSet.
        
        POST /erp/sc/routing/storage/spu/set
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/storage/spu/set",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

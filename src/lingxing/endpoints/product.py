"""产品 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class ProductEndpoints(BaseEndpoint):
    """领星产品 API (23个接口)."""

    async def add_commodity_code(self, **kwargs) -> list | dict:
        """AddCommodityCode. POST /listing/publish/api/upc/addCommodityCode"""
        resp = await self._post("/listing/publish/api/upc/addCommodityCode", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def brand(self, **kwargs) -> list | dict:
        """Brand. POST /erp/sc/data/local_inventory/brand"""
        resp = await self._post("/erp/sc/data/local_inventory/brand", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def category(self, **kwargs) -> list | dict:
        """Category. POST /erp/sc/routing/data/local_inventory/category"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/category", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_paging_log_lists(self, **kwargs) -> list | dict:
        """GetPagingLogLists. POST /basicOpen/product/getPagingLogLists"""
        resp = await self._post("/basicOpen/product/getPagingLogLists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_details(self, **kwargs) -> list | dict:
        """ProductDetails. POST /erp/sc/routing/data/local_inventory/productInfo"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_lists(self, **kwargs) -> list | dict:
        """ProductLists. POST /erp/sc/routing/data/local_inventory/productList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_brand(self, **kwargs) -> list | dict:
        """SetBrand. POST /erp/sc/storage/brand/set"""
        resp = await self._post("/erp/sc/storage/brand/set", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_bundled(self, **kwargs) -> list | dict:
        """SetBundled. POST /erp/sc/routing/storage/product/setBundled"""
        resp = await self._post("/erp/sc/routing/storage/product/setBundled", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_category(self, **kwargs) -> list | dict:
        """SetCategory. POST /erp/sc/routing/storage/category/set"""
        resp = await self._post("/erp/sc/routing/storage/category/set", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_product(self, **kwargs) -> list | dict:
        """SetProduct. POST /erp/sc/routing/storage/product/set"""
        resp = await self._post("/erp/sc/routing/storage/product/set", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def upc_list(self, **kwargs) -> list | dict:
        """UpcList. POST /listing/publish/api/upc/upcList"""
        resp = await self._post("/listing/publish/api/upc/upcList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def upload_pictures(self, **kwargs) -> list | dict:
        """UploadPictures. POST /erp/sc/routing/storage/product/uploadPictures"""
        resp = await self._post("/erp/sc/routing/storage/product/uploadPictures", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def attribute_list(self, **kwargs) -> list | dict:
        """attributeList. POST /erp/sc/routing/storage/attribute/attributeList"""
        resp = await self._post("/erp/sc/routing/storage/attribute/attributeList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def attribute_set(self, **kwargs) -> list | dict:
        """attributeSet. POST /erp/sc/routing/storage/attribute/set"""
        resp = await self._post("/erp/sc/routing/storage/attribute/set", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def batch_get_product_info(self, **kwargs) -> list | dict:
        """batchGetProductInfo. POST /erp/sc/routing/data/local_inventory/batchGetProductInfo"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/batchGetProductInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def bundled_product_list(self, **kwargs) -> list | dict:
        """bundledProductList. POST /erp/sc/routing/data/local_inventory/bundledProductList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/bundledProductList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_transparency_product_list(self, **kwargs) -> list | dict:
        """getTransparencyProductList. POST /basicOpen/product/getTransparencyProductList"""
        resp = await self._post("/basicOpen/product/getTransparencyProductList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_aux_list(self, **kwargs) -> list | dict:
        """productAuxList. POST /erp/sc/routing/data/local_inventory/productAuxList"""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productAuxList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_operate_batch(self, **kwargs) -> list | dict:
        """productOperateBatch. POST /basicOpen/product/productManager/product/operate/batch"""
        resp = await self._post("/basicOpen/product/productManager/product/operate/batch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_aux(self, **kwargs) -> list | dict:
        """setAux. POST /erp/sc/routing/storage/product/setAux"""
        resp = await self._post("/erp/sc/routing/storage/product/setAux", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def spu_info(self, **kwargs) -> list | dict:
        """spuInfo. POST /erp/sc/routing/storage/spu/info"""
        resp = await self._post("/erp/sc/routing/storage/spu/info", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def spu_list(self, **kwargs) -> list | dict:
        """spuList. POST /erp/sc/routing/storage/spu/spuList"""
        resp = await self._post("/erp/sc/routing/storage/spu/spuList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def spu_set(self, **kwargs) -> list | dict:
        """spuSet. POST /erp/sc/routing/storage/spu/set"""
        resp = await self._post("/erp/sc/routing/storage/spu/set", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

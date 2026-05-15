"""多平台商品 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class MultiplatformPlatformsEndpoints(BaseEndpoint):
    """领星多平台商品 API (33个接口)."""

    async def aliexpress_list_v2(self, **kwargs) -> list | dict:
        """AliexpressListV2. POST /basicOpen/multiplatform/aliexpress/list/v2"""
        resp = await self._post("/basicOpen/multiplatform/aliexpress/list/v2", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def batch_temu_address_decrypt(self, **kwargs) -> dict:
        """写操作 BatchTemuAddressDecrypt. POST /basicOpen/temu/temuAddressDecrypt"""
        resp = await self._post("/basicOpen/temu/temuAddressDecrypt", kwargs if kwargs else None)
        return resp.data or {}
    async def coupang_stock_list(self, **kwargs) -> list | dict:
        """CoupangStockList. POST /basicOpen/multiplatform/coupang/stockSearch"""
        resp = await self._post("/basicOpen/multiplatform/coupang/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def delete_cargo_storage(self, **kwargs) -> dict:
        """写操作 DeleteCargoStorage. POST /basicOpen/multiplatform/deleteCargoStorage"""
        resp = await self._post("/basicOpen/multiplatform/deleteCargoStorage", kwargs if kwargs else None)
        return resp.data or {}
    async def fbs_stock_list(self, **kwargs) -> list | dict:
        """FbsStockList. POST /basicOpen/multiplatform/fbs/stockSearch"""
        resp = await self._post("/basicOpen/multiplatform/fbs/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbt_stock_list(self, **kwargs) -> list | dict:
        """FbtStockList. POST /basicOpen/multiplatform/fbt/stockSearch/v2"""
        resp = await self._post("/basicOpen/multiplatform/fbt/stockSearch/v2", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbt_stock_search(self, **kwargs) -> list | dict:
        """FbtStockSearch. POST /basicOpen/multiplatform/fbt/stockSearch"""
        resp = await self._post("/basicOpen/multiplatform/fbt/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def full_list(self, **kwargs) -> list | dict:
        """FullList. POST /basicOpen/multiplatform/full/stockSearch"""
        resp = await self._post("/basicOpen/multiplatform/full/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def line_list(self, **kwargs) -> list | dict:
        """LineList. POST /basicOpen/multiplatform/line/list"""
        resp = await self._post("/basicOpen/multiplatform/line/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_shipping_list_v2(self, **kwargs) -> list | dict:
        """QueryShippingListV2. POST /basicOpen/multiplatform/query/shippingList"""
        resp = await self._post("/basicOpen/multiplatform/query/shippingList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shein_list(self, **kwargs) -> list | dict:
        """SheinList. POST /basicOpen/multiplatform/shein/list"""
        resp = await self._post("/basicOpen/multiplatform/shein/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopify_variant_list(self, **kwargs) -> list | dict:
        """ShopifyVariantList. POST /basicOpen/multiplatform/shopify/variantList"""
        resp = await self._post("/basicOpen/multiplatform/shopify/variantList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_cargo(self, **kwargs) -> list | dict:
        """TemuCargo. POST /basicOpen/multiplatform/temu/cargo"""
        resp = await self._post("/basicOpen/multiplatform/temu/cargo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_list(self, **kwargs) -> list | dict:
        """TemuList. POST /basicOpen/multiplatform/temu/list"""
        resp = await self._post("/basicOpen/multiplatform/temu/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tik_tok_list(self, **kwargs) -> list | dict:
        """TikTokList. POST /basicOpen/multiplatform/tiktok/list"""
        resp = await self._post("/basicOpen/multiplatform/tiktok/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wayfair_stock_list(self, **kwargs) -> list | dict:
        """WayfairStockList. POST /basicOpen/multiplatform/wayfair/stockSearch"""
        resp = await self._post("/basicOpen/multiplatform/wayfair/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_cargo_goods_list(self, **kwargs) -> dict:
        """写操作 addCargoGoodsList. POST /basicOpen/multiplatform/cargo/addCargoGoods/list"""
        resp = await self._post("/basicOpen/multiplatform/cargo/addCargoGoods/list", kwargs if kwargs else None)
        return resp.data or {}
    async def address_return_address_list(self, **kwargs) -> dict:
        """写操作 addressReturnAddressList. POST /basicOpen/multiplatform/address/returnAddressList"""
        resp = await self._post("/basicOpen/multiplatform/address/returnAddressList", kwargs if kwargs else None)
        return resp.data or {}
    async def aliexpress_list(self, **kwargs) -> list | dict:
        """aliexpressList. POST /basicOpen/multiplatform/aliExpress/list"""
        resp = await self._post("/basicOpen/multiplatform/aliExpress/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def e_bay_list(self, **kwargs) -> list | dict:
        """eBayList. POST /basicOpen/multiplatform/ebay/list"""
        resp = await self._post("/basicOpen/multiplatform/ebay/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def multiplatform_cargo_storage(self, **kwargs) -> list | dict:
        """multiplatformCargoStorage. POST /basicOpen/multiplatform/cargo/storage"""
        resp = await self._post("/basicOpen/multiplatform/cargo/storage", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_msku(self, **kwargs) -> list | dict:
        """profitReportMsku. POST /basicOpen/multiplatform/profit/report/msku"""
        resp = await self._post("/basicOpen/multiplatform/profit/report/msku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_order(self, **kwargs) -> list | dict:
        """profitReportOrder. POST /basicOpen/multiplatform/profit/report/order"""
        resp = await self._post("/basicOpen/multiplatform/profit/report/order", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_seller(self, **kwargs) -> list | dict:
        """profitReportSeller. POST /basicOpen/multiplatform/profit/report/seller"""
        resp = await self._post("/basicOpen/multiplatform/profit/report/seller", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_sku(self, **kwargs) -> list | dict:
        """profitReportSku. POST /basicOpen/multiplatform/profit/report/sku"""
        resp = await self._post("/basicOpen/multiplatform/profit/report/sku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def self_shipment_order_delivery_goods(self, **kwargs) -> list | dict:
        """selfShipmentOrderDeliveryGoods. POST /basicOpen/selfShipmentOrder/deliveryGoods"""
        resp = await self._post("/basicOpen/selfShipmentOrder/deliveryGoods", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_order_weighed(self, **kwargs) -> list | dict:
        """setOrderWeighed. POST /erp/sc/routing/wms/order/setOrderWeighed"""
        resp = await self._post("/erp/sc/routing/wms/order/setOrderWeighed", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_detail_by_code(self, **kwargs) -> list | dict:
        """shippingDetailByCode. POST /basicOpen/multiplatform/query/shippingDetail"""
        resp = await self._post("/basicOpen/multiplatform/query/shippingDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_order_allocate(self, **kwargs) -> dict:
        """写操作 shippingOrderAllocate. POST /basicOpen/multiplatform/allocate/stock"""
        resp = await self._post("/basicOpen/multiplatform/allocate/stock", kwargs if kwargs else None)
        return resp.data or {}
    async def shipping_order_delivery(self, **kwargs) -> list | dict:
        """shippingOrderDelivery. POST /basicOpen/multiplatform/shippingList/delivery"""
        resp = await self._post("/basicOpen/multiplatform/shippingList/delivery", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_order_picking(self, **kwargs) -> list | dict:
        """shippingOrderPicking. POST /basicOpen/multiplatform/shippingList/picking"""
        resp = await self._post("/basicOpen/multiplatform/shippingList/picking", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_stock_order_query_page(self, **kwargs) -> list | dict:
        """temuStockOrderQueryPage. POST /basicOpen/stockOrder/temu/queryPage"""
        resp = await self._post("/basicOpen/stockOrder/temu/queryPage", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_list(self, **kwargs) -> list | dict:
        """walmartList. POST /basicOpen/multiplatform/walmart/list"""
        resp = await self._post("/basicOpen/multiplatform/walmart/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

"""Auto-generated MultiplatformPlatformsEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class MultiplatformPlatformsEndpoints:
    """领星API - MultiplatformPlatformsEndpoints (33个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def aliexpress_list_v2(self, **kwargs) -> dict:
        """AliexpressListV2.
        
        POST /basicOpen/multiplatform/aliexpress/list/v2
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/aliexpress/list/v2",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def batch_temu_address_decrypt(self, **kwargs) -> dict:
        """BatchTemuAddressDecrypt.
        
        POST /basicOpen/temu/temuAddressDecrypt
        """
        return await self._request_with_token(
            route_name="/basicOpen/temu/temuAddressDecrypt",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def coupang_stock_list(self, **kwargs) -> dict:
        """CoupangStockList.
        
        POST /basicOpen/multiplatform/coupang/stockSearch
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/coupang/stockSearch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def delete_cargo_storage(self, **kwargs) -> dict:
        """DeleteCargoStorage.
        
        POST /basicOpen/multiplatform/deleteCargoStorage
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/deleteCargoStorage",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbs_stock_list(self, **kwargs) -> dict:
        """FbsStockList.
        
        POST /basicOpen/multiplatform/fbs/stockSearch
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/fbs/stockSearch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbt_stock_list(self, **kwargs) -> dict:
        """FbtStockList.
        
        POST /basicOpen/multiplatform/fbt/stockSearch/v2
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/fbt/stockSearch/v2",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbt_stock_search(self, **kwargs) -> dict:
        """FbtStockSearch.
        
        POST /basicOpen/multiplatform/fbt/stockSearch
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/fbt/stockSearch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def full_list(self, **kwargs) -> dict:
        """FullList.
        
        POST /basicOpen/multiplatform/full/stockSearch
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/full/stockSearch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def line_list(self, **kwargs) -> dict:
        """LineList.
        
        POST /basicOpen/multiplatform/line/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/line/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def query_shipping_list_v2(self, **kwargs) -> dict:
        """QueryShippingListV2.
        
        POST /basicOpen/multiplatform/query/shippingList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/query/shippingList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shein_list(self, **kwargs) -> dict:
        """SheinList.
        
        POST /basicOpen/multiplatform/shein/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/shein/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopify_variant_list(self, **kwargs) -> dict:
        """ShopifyVariantList.
        
        POST /basicOpen/multiplatform/shopify/variantList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/shopify/variantList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def temu_cargo(self, **kwargs) -> dict:
        """TemuCargo.
        
        POST /basicOpen/multiplatform/temu/cargo
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/temu/cargo",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def temu_list(self, **kwargs) -> dict:
        """TemuList.
        
        POST /basicOpen/multiplatform/temu/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/temu/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def tik_tok_list(self, **kwargs) -> dict:
        """TikTokList.
        
        POST /basicOpen/multiplatform/tiktok/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/tiktok/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def wayfair_stock_list(self, **kwargs) -> dict:
        """WayfairStockList.
        
        POST /basicOpen/multiplatform/wayfair/stockSearch
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/wayfair/stockSearch",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def add_cargo_goods_list(self, **kwargs) -> dict:
        """addCargoGoodsList.
        
        POST /basicOpen/multiplatform/cargo/addCargoGoods/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/cargo/addCargoGoods/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def address_return_address_list(self, **kwargs) -> dict:
        """addressReturnAddressList.
        
        POST /basicOpen/multiplatform/address/returnAddressList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/address/returnAddressList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def aliexpress_list(self, **kwargs) -> dict:
        """aliexpressList.
        
        POST /basicOpen/multiplatform/aliExpress/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/aliExpress/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def e_bay_list(self, **kwargs) -> dict:
        """eBayList.
        
        POST /basicOpen/multiplatform/ebay/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/ebay/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def multiplatform_cargo_storage(self, **kwargs) -> dict:
        """multiplatformCargoStorage.
        
        POST /basicOpen/multiplatform/cargo/storage
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/cargo/storage",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_report_msku(self, **kwargs) -> dict:
        """profitReportMsku.
        
        POST /basicOpen/multiplatform/profit/report/msku
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/profit/report/msku",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_report_order(self, **kwargs) -> dict:
        """profitReportOrder.
        
        POST /basicOpen/multiplatform/profit/report/order
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/profit/report/order",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_report_seller(self, **kwargs) -> dict:
        """profitReportSeller.
        
        POST /basicOpen/multiplatform/profit/report/seller
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/profit/report/seller",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_report_sku(self, **kwargs) -> dict:
        """profitReportSku.
        
        POST /basicOpen/multiplatform/profit/report/sku
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/profit/report/sku",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def self_shipment_order_delivery_goods(self, **kwargs) -> dict:
        """selfShipmentOrderDeliveryGoods.
        
        POST /basicOpen/selfShipmentOrder/deliveryGoods
        """
        return await self._request_with_token(
            route_name="/basicOpen/selfShipmentOrder/deliveryGoods",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def set_order_weighed(self, **kwargs) -> dict:
        """setOrderWeighed.
        
        POST /erp/sc/routing/wms/order/setOrderWeighed
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/wms/order/setOrderWeighed",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipping_detail_by_code(self, **kwargs) -> dict:
        """shippingDetailByCode.
        
        POST /basicOpen/multiplatform/query/shippingDetail
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/query/shippingDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipping_order_allocate(self, **kwargs) -> dict:
        """shippingOrderAllocate.
        
        POST /basicOpen/multiplatform/allocate/stock
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/allocate/stock",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipping_order_delivery(self, **kwargs) -> dict:
        """shippingOrderDelivery.
        
        POST /basicOpen/multiplatform/shippingList/delivery
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/shippingList/delivery",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shipping_order_picking(self, **kwargs) -> dict:
        """shippingOrderPicking.
        
        POST /basicOpen/multiplatform/shippingList/picking
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/shippingList/picking",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def temu_stock_order_query_page(self, **kwargs) -> dict:
        """temuStockOrderQueryPage.
        
        POST /basicOpen/stockOrder/temu/queryPage
        """
        return await self._request_with_token(
            route_name="/basicOpen/stockOrder/temu/queryPage",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_list(self, **kwargs) -> dict:
        """walmartList.
        
        POST /basicOpen/multiplatform/walmart/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/walmart/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

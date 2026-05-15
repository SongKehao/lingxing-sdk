"""VC卖家 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class VCEndpoints(BaseEndpoint):
    """领星VC卖家 API (10个接口)."""

    async def listing_manage_vc_listing_page_list(self, **kwargs) -> list | dict:
        """listingManageVcListingPageList. POST /basicOpen/listingManage/vcListing/pageList"""
        resp = await self._post("/basicOpen/listingManage/vcListing/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def platform_auth_vc_seller_page_list(self, **kwargs) -> list | dict:
        """platformAuthVcSellerPageList. POST /basicOpen/platformAuth/vcSeller/pageList"""
        resp = await self._post("/basicOpen/platformAuth/vcSeller/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_deliver_detail(self, **kwargs) -> list | dict:
        """vcDeliverDetail. POST /basicOpen/openapi/getInvoice/detail"""
        resp = await self._post("/basicOpen/openapi/getInvoice/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_deliver_page_list(self, **kwargs) -> list | dict:
        """vcDeliverPageList. POST /basicOpen/openapi/getInvoice/page/list"""
        resp = await self._post("/basicOpen/openapi/getInvoice/page/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_confirm_shipment(self, **kwargs) -> dict:
        """写操作 vcOrderDfConfirmShipment. POST /basicOpen/platformOrder/vcOrderDf/confirmShipment"""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/confirmShipment", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_order_df_detail(self, **kwargs) -> list | dict:
        """vcOrderDfDetail. POST /basicOpen/platformOrder/vcOrderDf/detail"""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_get_shipping_label(self, **kwargs) -> list | dict:
        """vcOrderDfGetShippingLabel. POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel"""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/getShippingLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_submit_shipping_label(self, **kwargs) -> dict:
        """写操作 vcOrderDfSubmitShippingLabel. POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel"""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/submitShippingLabel", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_order_page_list(self, **kwargs) -> list | dict:
        """vcOrderPageList. POST /basicOpen/platformOrder/vcOrder/pageList"""
        resp = await self._post("/basicOpen/platformOrder/vcOrder/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_po_detail(self, **kwargs) -> list | dict:
        """vcOrderPoDetail. POST /basicOpen/platformOrder/vcOrderPo/detail"""
        resp = await self._post("/basicOpen/platformOrder/vcOrderPo/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

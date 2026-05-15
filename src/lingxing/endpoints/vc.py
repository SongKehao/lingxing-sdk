"""Auto-generated VCEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class VCEndpoints:
    """领星API - VCEndpoints (10个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def listing_manage_vc_listing_page_list(self, **kwargs) -> dict:
        """listingManageVcListingPageList.
        
        POST /basicOpen/listingManage/vcListing/pageList
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/vcListing/pageList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def platform_auth_vc_seller_page_list(self, **kwargs) -> dict:
        """platformAuthVcSellerPageList.
        
        POST /basicOpen/platformAuth/vcSeller/pageList
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformAuth/vcSeller/pageList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_deliver_detail(self, **kwargs) -> dict:
        """vcDeliverDetail.
        
        POST /basicOpen/openapi/getInvoice/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/getInvoice/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_deliver_page_list(self, **kwargs) -> dict:
        """vcDeliverPageList.
        
        POST /basicOpen/openapi/getInvoice/page/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/getInvoice/page/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_df_confirm_shipment(self, **kwargs) -> dict:
        """vcOrderDfConfirmShipment.
        
        POST /basicOpen/platformOrder/vcOrderDf/confirmShipment
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrderDf/confirmShipment",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_df_detail(self, **kwargs) -> dict:
        """vcOrderDfDetail.
        
        POST /basicOpen/platformOrder/vcOrderDf/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrderDf/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_df_get_shipping_label(self, **kwargs) -> dict:
        """vcOrderDfGetShippingLabel.
        
        POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrderDf/getShippingLabel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_df_submit_shipping_label(self, **kwargs) -> dict:
        """vcOrderDfSubmitShippingLabel.
        
        POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrderDf/submitShippingLabel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_page_list(self, **kwargs) -> dict:
        """vcOrderPageList.
        
        POST /basicOpen/platformOrder/vcOrder/pageList
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrder/pageList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_order_po_detail(self, **kwargs) -> dict:
        """vcOrderPoDetail.
        
        POST /basicOpen/platformOrder/vcOrderPo/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/vcOrderPo/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

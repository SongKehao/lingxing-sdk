"""Auto-generated NewAdEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class NewAdEndpoints:
    """领星API - NewAdEndpoints (4个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def dsp_account_list(self, **kwargs) -> dict:
        """dspAccountList.
        
        POST /basicOpen/baseData/account/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/baseData/account/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_analysis_list(self, **kwargs) -> dict:
        """ProductAnalysisList.
        
        POST /basicOpen/adReport/productOrderAnalysis/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/adReport/productOrderAnalysis/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def walmart_query_advertiser_list(self, **kwargs) -> dict:
        """WalmartQueryAdvertiserList.
        
        POST /basicOpen/adReport/advertiser/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/adReport/advertiser/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def dsp_report_order_list(self, **kwargs) -> dict:
        """dspReportOrderList.
        
        POST /basicOpen/dspReport/order/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/dspReport/order/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

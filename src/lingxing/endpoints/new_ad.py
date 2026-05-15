"""新版广告 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class NewAdEndpoints(BaseEndpoint):
    """领星新版广告 API (4个接口)."""

    async def dsp_account_list(self, **kwargs) -> list | dict:
        """dspAccountList. POST /basicOpen/baseData/account/list"""
        resp = await self._post("/basicOpen/baseData/account/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_analysis_list(self, **kwargs) -> list | dict:
        """ProductAnalysisList. POST /basicOpen/adReport/productOrderAnalysis/list"""
        resp = await self._post("/basicOpen/adReport/productOrderAnalysis/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_query_advertiser_list(self, **kwargs) -> list | dict:
        """WalmartQueryAdvertiserList. POST /basicOpen/adReport/advertiser/list"""
        resp = await self._post("/basicOpen/adReport/advertiser/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def dsp_report_order_list(self, **kwargs) -> list | dict:
        """dspReportOrderList. POST /basicOpen/dspReport/order/list"""
        resp = await self._post("/basicOpen/dspReport/order/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

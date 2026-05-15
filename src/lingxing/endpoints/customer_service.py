"""客服 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class CustomerServiceEndpoints(BaseEndpoint):
    """领星客服 API (16个接口)."""

    async def feedback_list(self, **kwargs) -> list | dict:
        """FeedbackList. POST /erp/sc/cs/feedback/list"""
        resp = await self._post("/erp/sc/cs/feedback/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_list_mws(self, **kwargs) -> list | dict:
        """FeedbackListMws. POST /erp/sc/cs/feedback/listMws"""
        resp = await self._post("/erp/sc/cs/feedback/listMws", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def performance_notice_detail(self, **kwargs) -> list | dict:
        """PerformanceNoticeDetail. POST /basicOpen/customerService/storeTarget/detail"""
        resp = await self._post("/basicOpen/customerService/storeTarget/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def performance_notice_list(self, **kwargs) -> list | dict:
        """PerformanceNoticeList. POST /basicOpen/customerService/performanceNotice/list"""
        resp = await self._post("/basicOpen/customerService/performanceNotice/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def customer_service_crmcustomer_index(self, **kwargs) -> list | dict:
        """customerServiceCrmcustomerIndex. POST /basicOpen/customerService/crm/customer/index"""
        resp = await self._post("/basicOpen/customerService/crm/customer/index", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def customer_service_rma_manage_list(self, **kwargs) -> list | dict:
        """customerServiceRmaManageList. POST /basicOpen/customerService/rmaManage/list"""
        resp = await self._post("/basicOpen/customerService/rmaManage/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def detail(self, **kwargs) -> list | dict:
        """detail. POST /erp/sc/data/mail/detail"""
        resp = await self._post("/erp/sc/data/mail/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_detail(self, **kwargs) -> list | dict:
        """feedbackDetail. POST /erp/sc/cs/feedbackReport/detail"""
        resp = await self._post("/erp/sc/cs/feedbackReport/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_lists(self, **kwargs) -> list | dict:
        """feedbackLists. POST /erp/sc/cs/feedbackReport/lists"""
        resp = await self._post("/erp/sc/cs/feedbackReport/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lists(self, **kwargs) -> list | dict:
        """lists. POST /erp/sc/data/mail/lists"""
        resp = await self._post("/erp/sc/data/mail/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review(self, **kwargs) -> list | dict:
        """review. POST /erp/sc/v2/data/mws/reviews"""
        resp = await self._post("/erp/sc/v2/data/mws/reviews", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_detail(self, **kwargs) -> list | dict:
        """reviewDetail. POST /erp/sc/cs/reviewReport/detail"""
        resp = await self._post("/erp/sc/cs/reviewReport/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_lists(self, **kwargs) -> list | dict:
        """reviewLists. POST /erp/sc/v2/cs/reviewReport/lists"""
        resp = await self._post("/erp/sc/v2/cs/reviewReport/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_v2(self, **kwargs) -> list | dict:
        """reviewV2. POST /basicOpen/openapi/service/v3/data/mws/reviews"""
        resp = await self._post("/basicOpen/openapi/service/v3/data/mws/reviews", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def store_performance_list(self, **kwargs) -> list | dict:
        """storePerformanceList. POST /basicOpen/customerService/storeTarget/list"""
        resp = await self._post("/basicOpen/customerService/storeTarget/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def voice_of_buyer_list(self, **kwargs) -> list | dict:
        """voiceOfBuyerList. POST /basicOpen/customerService/voiceOfBuyer/list"""
        resp = await self._post("/basicOpen/customerService/voiceOfBuyer/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

"""Auto-generated CustomerServiceEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class CustomerServiceEndpoints:
    """领星API - CustomerServiceEndpoints (16个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def feedback_list(self, **kwargs) -> dict:
        """FeedbackList.
        
        POST /erp/sc/cs/feedback/list
        """
        return await self._request_with_token(
            route_name="/erp/sc/cs/feedback/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def feedback_list_mws(self, **kwargs) -> dict:
        """FeedbackListMws.
        
        POST /erp/sc/cs/feedback/listMws
        """
        return await self._request_with_token(
            route_name="/erp/sc/cs/feedback/listMws",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def performance_notice_detail(self, **kwargs) -> dict:
        """PerformanceNoticeDetail.
        
        POST /basicOpen/customerService/storeTarget/detail
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/storeTarget/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def performance_notice_list(self, **kwargs) -> dict:
        """PerformanceNoticeList.
        
        POST /basicOpen/customerService/performanceNotice/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/performanceNotice/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def customer_service_crmcustomer_index(self, **kwargs) -> dict:
        """customerServiceCrmcustomerIndex.
        
        POST /basicOpen/customerService/crm/customer/index
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/crm/customer/index",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def customer_service_rma_manage_list(self, **kwargs) -> dict:
        """customerServiceRmaManageList.
        
        POST /basicOpen/customerService/rmaManage/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/rmaManage/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def detail(self, **kwargs) -> dict:
        """detail.
        
        POST /erp/sc/data/mail/detail
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mail/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def feedback_detail(self, **kwargs) -> dict:
        """feedbackDetail.
        
        POST /erp/sc/cs/feedbackReport/detail
        """
        return await self._request_with_token(
            route_name="/erp/sc/cs/feedbackReport/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def feedback_lists(self, **kwargs) -> dict:
        """feedbackLists.
        
        POST /erp/sc/cs/feedbackReport/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/cs/feedbackReport/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lists(self, **kwargs) -> dict:
        """lists.
        
        POST /erp/sc/data/mail/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mail/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def review(self, **kwargs) -> dict:
        """review.
        
        POST /erp/sc/v2/data/mws/reviews
        """
        return await self._request_with_token(
            route_name="/erp/sc/v2/data/mws/reviews",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def review_detail(self, **kwargs) -> dict:
        """reviewDetail.
        
        POST /erp/sc/cs/reviewReport/detail
        """
        return await self._request_with_token(
            route_name="/erp/sc/cs/reviewReport/detail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def review_lists(self, **kwargs) -> dict:
        """reviewLists.
        
        POST /erp/sc/v2/cs/reviewReport/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/v2/cs/reviewReport/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def review_v2(self, **kwargs) -> dict:
        """reviewV2.
        
        POST /basicOpen/openapi/service/v3/data/mws/reviews
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/service/v3/data/mws/reviews",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def store_performance_list(self, **kwargs) -> dict:
        """storePerformanceList.
        
        POST /basicOpen/customerService/storeTarget/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/storeTarget/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def voice_of_buyer_list(self, **kwargs) -> dict:
        """voiceOfBuyerList.
        
        POST /basicOpen/customerService/voiceOfBuyer/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/customerService/voiceOfBuyer/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

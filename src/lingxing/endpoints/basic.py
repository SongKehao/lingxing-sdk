"""Auto-generated BasicEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class BasicEndpoints:
    """领星API - BasicEndpoints (10个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def accout_lists(self, **kwargs) -> dict:
        """AccoutLists.
        
        POST /erp/sc/data/account/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/account/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def all_marketplace(self, **kwargs) -> dict:
        """AllMarketplace.
        
        POST /erp/sc/data/seller/allMarketplace
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/seller/allMarketplace",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def attachment_download(self, **kwargs) -> dict:
        """AttachmentDownload.
        
        POST /erp/sc/routing/common/file/download
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/common/file/download",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def concept_seller_lists(self, **kwargs) -> dict:
        """ConceptSellerLists.
        
        POST /erp/sc/data/seller/conceptLists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/seller/conceptLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def currency(self, **kwargs) -> dict:
        """Currency.
        
        POST /erp/sc/routing/finance/currency/currencyMonth
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/currency/currencyMonth",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def exchange_rate_update(self, **kwargs) -> dict:
        """ExchangeRateUpdate.
        
        POST /basicOpen/settings/exchangeRate/update
        """
        return await self._request_with_token(
            route_name="/basicOpen/settings/exchangeRate/update",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def seller_batch_rename(self, **kwargs) -> dict:
        """SellerBatchRename.
        
        POST /erp/sc/data/seller/batchEditSellerName
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/seller/batchEditSellerName",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def seller_lists(self, **kwargs) -> dict:
        """SellerLists.
        
        POST /erp/sc/data/seller/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/seller/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def state_list(self, **kwargs) -> dict:
        """StateList.
        
        POST /basicOpen/multiplatform/profit/report/stateList
        """
        return await self._request_with_token(
            route_name="/basicOpen/multiplatform/profit/report/stateList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def world_state_lists(self, **kwargs) -> dict:
        """WorldStateLists.
        
        POST /erp/sc/data/worldState/lists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/worldState/lists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

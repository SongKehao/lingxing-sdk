"""Auto-generated FinanceEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class FinanceEndpoints:
    """领星API - FinanceEndpoints (19个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def fiance_profit_msku(self, **kwargs) -> dict:
        """FianceProfitMsku.
        
        POST /erp/sc/routing/finance/ProfitState/profitMsku
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/ProfitState/profitMsku",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def order_profit_list_msku(self, **kwargs) -> dict:
        """OrderProfitListMSKU.
        
        POST /basicOpen/finance/mreport/OrderProfit
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/mreport/OrderProfit",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def query_receipt_funds_list(self, **kwargs) -> dict:
        """QueryReceiptFundsList.
        
        POST /basicOpen/finance/queryReceiptFundsList
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/queryReceiptFundsList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_order_list(self, **kwargs) -> dict:
        """RequestFundsOrderList.
        
        POST /basicOpen/finance/requestFunds/order/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFunds/order/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_payout_list(self, **kwargs) -> dict:
        """lazadaPayoutList.
        
        POST /basicOpen/finance/lazada/payout/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/lazada/payout/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def lazada_settlement_list(self, **kwargs) -> dict:
        """lazadaSettlementList.
        
        POST /basicOpen/finance/lazada/settlement/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/lazada/settlement/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_asin(self, **kwargs) -> dict:
        """profitAsin.
        
        POST /erp/sc/routing/finance/ProfitState/profitAsin
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/ProfitState/profitAsin",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_asin_son(self, **kwargs) -> dict:
        """profitAsinSon.
        
        POST /erp/sc/routing/finance/ProfitState/profitAsinSon
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/ProfitState/profitAsinSon",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_report_order_transcation_list(self, **kwargs) -> dict:
        """profitReportOrderTranscationList.
        
        POST /basicOpen/finance/profitReport/order/transcation/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/profitReport/order/transcation/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_settlement(self, **kwargs) -> dict:
        """profitSettlement.
        
        POST /erp/sc/routing/finance/ProfitState/profitSettlement
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/ProfitState/profitSettlement",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_custom_fee_list(self, **kwargs) -> dict:
        """requestFundsPoolCustomFeeList.
        
        POST /basicOpen/finance/requestFundsPool/customFee/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/customFee/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_inbound_list(self, **kwargs) -> dict:
        """requestFundsPoolInboundList.
        
        POST /basicOpen/finance/requestFundsPool/inbound/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/inbound/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_logistics_list(self, **kwargs) -> dict:
        """requestFundsPoolLogisticsList.
        
        POST /basicOpen/finance/requestFundsPool/logistics/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/logistics/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_other_fee_list(self, **kwargs) -> dict:
        """requestFundsPoolOtherFeeList.
        
        POST /basicOpen/finance/requestFundsPool/otherFee/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/otherFee/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_prepay_list(self, **kwargs) -> dict:
        """requestFundsPoolPrepayList.
        
        POST /basicOpen/finance/requestFundsPool/prepay/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/prepay/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def request_funds_pool_purchase_list(self, **kwargs) -> dict:
        """requestFundsPoolPurchaseList.
        
        POST /basicOpen/finance/requestFundsPool/purchase/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/requestFundsPool/purchase/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopee_adjustment_list(self, **kwargs) -> dict:
        """shopeeAdjustmentList.
        
        POST /basicOpen/finance/shopee/adjustment/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/shopee/adjustment/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopee_income_list(self, **kwargs) -> dict:
        """shopeeIncomeList.
        
        POST /basicOpen/finance/shopee/income/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/shopee/income/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def shopee_payout_list(self, **kwargs) -> dict:
        """shopeePayoutList.
        
        POST /basicOpen/finance/shopee/payout/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/finance/shopee/payout/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

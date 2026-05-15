"""财务 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class FinanceEndpoints(BaseEndpoint):
    """领星财务 API (19个接口)."""

    async def fiance_profit_msku(self, **kwargs) -> list | dict:
        """FianceProfitMsku. POST /erp/sc/routing/finance/ProfitState/profitMsku"""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitMsku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_profit_list_msku(self, **kwargs) -> list | dict:
        """OrderProfitListMSKU. POST /basicOpen/finance/mreport/OrderProfit"""
        resp = await self._post("/basicOpen/finance/mreport/OrderProfit", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_receipt_funds_list(self, **kwargs) -> list | dict:
        """QueryReceiptFundsList. POST /basicOpen/finance/queryReceiptFundsList"""
        resp = await self._post("/basicOpen/finance/queryReceiptFundsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_order_list(self, **kwargs) -> list | dict:
        """RequestFundsOrderList. POST /basicOpen/finance/requestFunds/order/list"""
        resp = await self._post("/basicOpen/finance/requestFunds/order/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_payout_list(self, **kwargs) -> list | dict:
        """lazadaPayoutList. POST /basicOpen/finance/lazada/payout/list"""
        resp = await self._post("/basicOpen/finance/lazada/payout/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_settlement_list(self, **kwargs) -> list | dict:
        """lazadaSettlementList. POST /basicOpen/finance/lazada/settlement/list"""
        resp = await self._post("/basicOpen/finance/lazada/settlement/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin(self, **kwargs) -> list | dict:
        """profitAsin. POST /erp/sc/routing/finance/ProfitState/profitAsin"""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsin", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin_son(self, **kwargs) -> list | dict:
        """profitAsinSon. POST /erp/sc/routing/finance/ProfitState/profitAsinSon"""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsinSon", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_order_transcation_list(self, **kwargs) -> list | dict:
        """profitReportOrderTranscationList. POST /basicOpen/finance/profitReport/order/transcation/list"""
        resp = await self._post("/basicOpen/finance/profitReport/order/transcation/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_settlement(self, **kwargs) -> list | dict:
        """profitSettlement. POST /erp/sc/routing/finance/ProfitState/profitSettlement"""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitSettlement", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_custom_fee_list(self, **kwargs) -> list | dict:
        """requestFundsPoolCustomFeeList. POST /basicOpen/finance/requestFundsPool/customFee/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/customFee/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_inbound_list(self, **kwargs) -> list | dict:
        """requestFundsPoolInboundList. POST /basicOpen/finance/requestFundsPool/inbound/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/inbound/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_logistics_list(self, **kwargs) -> list | dict:
        """requestFundsPoolLogisticsList. POST /basicOpen/finance/requestFundsPool/logistics/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/logistics/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_other_fee_list(self, **kwargs) -> list | dict:
        """requestFundsPoolOtherFeeList. POST /basicOpen/finance/requestFundsPool/otherFee/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/otherFee/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_prepay_list(self, **kwargs) -> list | dict:
        """requestFundsPoolPrepayList. POST /basicOpen/finance/requestFundsPool/prepay/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/prepay/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_purchase_list(self, **kwargs) -> list | dict:
        """requestFundsPoolPurchaseList. POST /basicOpen/finance/requestFundsPool/purchase/list"""
        resp = await self._post("/basicOpen/finance/requestFundsPool/purchase/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_adjustment_list(self, **kwargs) -> list | dict:
        """shopeeAdjustmentList. POST /basicOpen/finance/shopee/adjustment/list"""
        resp = await self._post("/basicOpen/finance/shopee/adjustment/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_income_list(self, **kwargs) -> list | dict:
        """shopeeIncomeList. POST /basicOpen/finance/shopee/income/list"""
        resp = await self._post("/basicOpen/finance/shopee/income/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_payout_list(self, **kwargs) -> list | dict:
        """shopeePayoutList. POST /basicOpen/finance/shopee/payout/list"""
        resp = await self._post("/basicOpen/finance/shopee/payout/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

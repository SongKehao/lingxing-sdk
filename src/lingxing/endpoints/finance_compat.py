"""Finance Endpoints - Backward Compatibility Wrapper"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase

from .finance.fees import FeeManagementEndpoint
from .finance.inventory_ledger import InventoryLedgerEndpoint
from .finance.profit import ProfitEndpoint
from .finance.receivable import ReceivableEndpoint
from .finance.request_pools import RequestPoolsEndpoint
from .finance.settlement import SettlementEndpoint


class FinanceEndpoints:

    def __init__(self, openapi: "OpenApiBase"):
        self._profit = ProfitEndpoint(openapi)
        self._settlement = SettlementEndpoint(openapi)
        self._fees = FeeManagementEndpoint(openapi)
        self._inventory_ledger = InventoryLedgerEndpoint(openapi)
        self._request_pools = RequestPoolsEndpoint(openapi)
        self._receivable = ReceivableEndpoint(openapi)

    def __getattr__(self, name):
        if 'profit' in name or 'order_transaction' in name:
            return getattr(self._profit, name)
        if 'settlement' in name or 'reimbursement' in name:
            return getattr(self._settlement, name)
        if 'fee' in name and ('create' in name or 'edit' in name or 'delete' in name or 'discard' in name):
            return getattr(self._fees, name)
        if 'inventory_ledger' in name or 'fba_cost_stream' in name:
            return getattr(self._inventory_ledger, name)
        if 'request_pool' in name or 'prepay' in name or 'logistics' in name or 'payable' in name:
            return getattr(self._request_pools, name)
        if 'receivable' in name:
            return getattr(self._receivable, name)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

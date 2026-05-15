"""Statistics Endpoints - Backward Compatibility Wrapper"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase

from .statistics.fba import FBAEndpoint
from .statistics.inventory import InventoryEndpoint
from .statistics.reports import ReportsEndpoint
from .statistics.sales import SalesEndpoint


class StatisticsEndpoints:

    def __init__(self, openapi: "OpenApiBase"):
        self._sales = SalesEndpoint(openapi)
        self._reports = ReportsEndpoint(openapi)
        self._inventory = InventoryEndpoint(openapi)
        self._fba = FBAEndpoint(openapi)

    def __getattr__(self, name):
        if 'product_performance' in name or 'asin_360' in name or 'profit_stat' in name:
            return getattr(self._sales, name)
        if 'order_profit' in name or 'storage_fee' in name or 'purchase_report' in name:
            return getattr(self._reports, name)
        if 'store_sales' in name or 'asin_daily' in name or 'return' in name:
            return getattr(self._inventory, name)
        if 'operate_log' in name or 'fba_stock' in name or 'fba_cost_center' in name:
            return getattr(self._fba, name)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

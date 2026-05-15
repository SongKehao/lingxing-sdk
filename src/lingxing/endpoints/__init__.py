"""
LingXing API Endpoints Package

Provides modular endpoint classes for different LingXing API categories.
"""

from .ads_compat import AdsEndpoints
from .amazon_source import AmazonSourceEndpoints
from .basic import BasicEndpoints
from .customer_service import CustomerServiceEndpoints
from .fba import FBAEndpoints
from .finance_compat import FinanceEndpoints
from .goal import GoalEndpoints
from .inventory_alerts import InventoryAlertsEndpoints
from .logistics import LogisticsEndpoints
from .multiplatform import MultiPlatformEndpoints
from .order import OrderEndpoints
from .product import ProductEndpoints
from .purchase import PurchaseEndpoints
from .restocking import RestockingEndpoints
from .restocking_limit import RestockingLimitEndpoints
from .statistics_compat import StatisticsEndpoints
from .tools import ToolsEndpoints
from .vc import VCEndpoints
from .warehouse import WarehouseEndpoints

__all__ = [
    "AdsEndpoints",
    "AmazonSourceEndpoints",
    "BasicEndpoints",
    "CustomerServiceEndpoints",
    "FBAEndpoints",
    "FinanceEndpoints",
    "GoalEndpoints",
    "InventoryAlertsEndpoints",
    "LogisticsEndpoints",
    "MultiPlatformEndpoints",
    "OrderEndpoints",
    "ProductEndpoints",
    "PurchaseEndpoints",
    "RestockingEndpoints",
    "RestockingLimitEndpoints",
    "StatisticsEndpoints",
    "ToolsEndpoints",
    "VCEndpoints",
    "WarehouseEndpoints",
]

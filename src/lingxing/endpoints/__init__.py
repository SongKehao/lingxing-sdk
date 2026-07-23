"""LingXing API Endpoints Package."""

from .amazon_source import AmazonSourceEndpoints
from .basic import BasicEndpoints
from .customer_service import CustomerServiceEndpoints
from .fba import FBAEndpoints
from .finance import FinanceEndpoints
from .logistics import LogisticsEndpoints
from .multiplatform_ads import MultiplatformAdsEndpoints
from .multiplatform_other import MultiplatformOtherEndpoints
from .multiplatform_platforms import MultiplatformPlatformsEndpoints
from .new_ad import NewAdEndpoints
from .product import ProductEndpoints
from .purchase import PurchaseEndpoints
from .restocking import RestockingEndpoints
from .restocking_limit import RestockingLimitEndpoints
from .sale import SaleEndpoints
from .statistics import StatisticsEndpoints
from .target_manage import TargetManageEndpoints
from .tools import ToolsEndpoints
from .vc import VCEndpoints
from .warehouse import WarehouseEndpoints

__all__ = [
    "BasicEndpoints",
    "FBAEndpoints",
    "RestockingLimitEndpoints",
    "RestockingEndpoints",
    "FinanceEndpoints",
    "LogisticsEndpoints",
    "MultiplatformAdsEndpoints",
    "MultiplatformOtherEndpoints",
    "MultiplatformPlatformsEndpoints",
    "NewAdEndpoints",
    "ProductEndpoints",
    "PurchaseEndpoints",
    "SaleEndpoints",
    "CustomerServiceEndpoints",
    "AmazonSourceEndpoints",
    "StatisticsEndpoints",
    "TargetManageEndpoints",
    "ToolsEndpoints",
    "VCEndpoints",
    "WarehouseEndpoints",
]

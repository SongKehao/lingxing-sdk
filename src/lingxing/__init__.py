"""领星 ERP OpenAPI Python SDK

一个功能完整的领星ERP API Python SDK，支持所有580+个API端点。

Basic usage:
    from lingxing import LingXingConfig, OpenApiBase
    from lingxing.endpoints import SaleEndpoints

    config = LingXingConfig(app_id="...", app_secret="...")
    openapi = OpenApiBase(host=config.host, app_id=config.app_id, app_secret=config.app_secret)
    sale = SaleEndpoints(openapi)
    listings = await sale.listing(sid=123, offset=0, length=20)
"""

__version__ = "0.4.0"

from .client import LingXingClient
from .config import LingXingConfig, get_config, set_config
from .core.openapi import OpenApiBase
from .core.param_builder import (
    DEFAULT_SIDS,
    APIParamBuilder,
    build_api_params,
    get_param_builder,
)
from .core.rate_limiter import (
    RateLimiter,
    check_ip_whitelist,
    detect_current_ip,
    get_rate_limiter,
)
from .core.resp_schema import AccessTokenDto, ResponseResult
from .endpoints._base import BaseEndpoint
from .endpoints import (
    AmazonSourceEndpoints,
    BasicEndpoints,
    CustomerServiceEndpoints,
    FBAEndpoints,
    FinanceEndpoints,
    LogisticsEndpoints,
    MultiplatformAdsEndpoints,
    MultiplatformOtherEndpoints,
    MultiplatformPlatformsEndpoints,
    NewAdEndpoints,
    ProductEndpoints,
    PurchaseEndpoints,
    RestockingEndpoints,
    RestockingLimitEndpoints,
    SaleEndpoints,
    StatisticsEndpoints,
    ToolsEndpoints,
    VCEndpoints,
    WarehouseEndpoints,
)
from .errors import ApiError, AuthenticationError, LingXingError, RateLimitError, ValidationError
from .integration_base import (
    BaseIntegration,
    HTTPIntegration,
    IntegrationHealth,
    IntegrationStatus,
)
from .models.business import (
    FBAShipment,
    InventoryInfo,
    LingXingResponse,
    OrderInfo,
    ProductInfo,
    StoreInfo,
    SyncStatus,
    SyncTask,
)
from .types import DateRangeRequest, PageRequest, PageResult, SellerFilteredRequest

__all__ = [
    # Version
    "__version__",
    # Core
    "LingXingClient",
    "LingXingConfig",
    "OpenApiBase",
    "BaseEndpoint",
    "AccessTokenDto",
    "ResponseResult",
    # Endpoints
    "AmazonSourceEndpoints",
    "BasicEndpoints",
    "CustomerServiceEndpoints",
    "FBAEndpoints",
    "FinanceEndpoints",
    "LogisticsEndpoints",
    "MultiplatformAdsEndpoints",
    "MultiplatformOtherEndpoints",
    "MultiplatformPlatformsEndpoints",
    "NewAdEndpoints",
    "ProductEndpoints",
    "PurchaseEndpoints",
    "RestockingEndpoints",
    "RestockingLimitEndpoints",
    "SaleEndpoints",
    "StatisticsEndpoints",
    "ToolsEndpoints",
    "VCEndpoints",
    "WarehouseEndpoints",
    # Errors
    "ApiError",
    "AuthenticationError",
    "LingXingError",
    "RateLimitError",
    "ValidationError",
    # Types
    "DateRangeRequest",
    "PageRequest",
    "PageResult",
    "SellerFilteredRequest",
    # Business Models
    "FBAShipment",
    "InventoryInfo",
    "LingXingResponse",
    "OrderInfo",
    "ProductInfo",
    "StoreInfo",
    "SyncStatus",
    "SyncTask",
    # Integration
    "BaseIntegration",
    "HTTPIntegration",
    "IntegrationHealth",
    "IntegrationStatus",
    # Utilities
    "APIParamBuilder",
    "DEFAULT_SIDS",
    "RateLimiter",
    "build_api_params",
    "check_ip_whitelist",
    "detect_current_ip",
    "get_config",
    "get_param_builder",
    "get_rate_limiter",
    "set_config",
]

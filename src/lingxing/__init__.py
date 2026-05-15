"""领星 ERP OpenAPI Python SDK"""

__version__ = "0.1.0"

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
from .integration_base import (
    BaseIntegration,
    HTTPIntegration,
    IntegrationHealth,
    IntegrationStatus,
)
from .models import (
    FBAShipment,
    InventoryInfo,
    LingXingResponse,
    OrderInfo,
    ProductInfo,
    StoreInfo,
    SyncStatus,
    SyncTask,
)

__all__ = [
    "DEFAULT_SIDS",
    "APIParamBuilder",
    "AccessTokenDto",
    "BaseIntegration",
    "FBAShipment",
    "HTTPIntegration",
    "IntegrationHealth",
    "IntegrationStatus",
    "InventoryInfo",
    "LingXingClient",
    "LingXingConfig",
    "LingXingResponse",
    "OpenApiBase",
    "OrderInfo",
    "ProductInfo",
    "RateLimiter",
    "ResponseResult",
    "StoreInfo",
    "SyncStatus",
    "SyncTask",
    "build_api_params",
    "check_ip_whitelist",
    "detect_current_ip",
    "get_config",
    "get_param_builder",
    "get_rate_limiter",
    "set_config",
]

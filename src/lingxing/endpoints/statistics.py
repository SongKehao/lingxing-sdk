#!/usr/bin/env python3
"""LingXing Statistics API Endpoints (Backward Compatibility Facade)"""

from .statistics.inventory import InventoryEndpoint
from .statistics.performance import PerformanceEndpoint
from .statistics.sales import SalesEndpoint


# Backward compatibility: expose all methods through a unified class
class StatisticsEndpoints(SalesEndpoint, InventoryEndpoint, PerformanceEndpoint):
    """统计API统一入口（向后兼容）"""

__all__ = ["InventoryEndpoint", "PerformanceEndpoint", "SalesEndpoint", "StatisticsEndpoints"]

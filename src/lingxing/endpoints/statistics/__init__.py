#!/usr/bin/env python3
"""统计API模块"""

from .inventory import InventoryEndpoint
from .performance import PerformanceEndpoint
from .sales import SalesEndpoint


class StatisticsEndpoints(SalesEndpoint, InventoryEndpoint, PerformanceEndpoint):
    """统计端点（向后兼容）"""


__all__ = [
    "InventoryEndpoint",
    "PerformanceEndpoint",
    "SalesEndpoint",
    "StatisticsEndpoints",
]

#!/usr/bin/env python3
"""
LingXing Finance API Endpoints (Backward Compatibility Facade)

This module maintains backward compatibility by re-exporting from sub-modules.
New code should import from finance.transactions, finance.settlements, or finance.reports directly.
"""

from .finance.reports import ReportsEndpoint
from .finance.settlements import SettlementsEndpoint
from .finance.transactions import TransactionsEndpoint


# Backward compatibility: expose all methods through a unified class
class FinanceEndpoints(TransactionsEndpoint, SettlementsEndpoint, ReportsEndpoint):
    """财务API统一入口（向后兼容）"""

__all__ = ["FinanceEndpoints", "ReportsEndpoint", "SettlementsEndpoint", "TransactionsEndpoint"]

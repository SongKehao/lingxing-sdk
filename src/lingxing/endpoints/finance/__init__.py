#!/usr/bin/env python3
"""财务API模块"""

from .reports import ReportsEndpoint
from .settlements import SettlementsEndpoint
from .transactions import TransactionsEndpoint


class FinanceEndpoints(TransactionsEndpoint, SettlementsEndpoint, ReportsEndpoint):
    """财务端点（向后兼容）"""


__all__ = [
    "FinanceEndpoints",
    "ReportsEndpoint",
    "SettlementsEndpoint",
    "TransactionsEndpoint",
]

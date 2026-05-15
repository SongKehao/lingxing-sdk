#!/usr/bin/env python3
"""广告API模块"""

from .campaigns import CampaignsEndpoint
from .keywords import KeywordsEndpoint
from .reports import ReportsEndpoint


class AdsEndpoints(CampaignsEndpoint, KeywordsEndpoint, ReportsEndpoint):
    """广告端点（向后兼容）"""


__all__ = [
    "AdsEndpoints",
    "CampaignsEndpoint",
    "KeywordsEndpoint",
    "ReportsEndpoint",
]

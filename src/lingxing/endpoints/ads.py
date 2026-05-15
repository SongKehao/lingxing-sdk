#!/usr/bin/env python3
"""
LingXing Ads API Endpoints (Backward Compatibility Facade)

This module maintains backward compatibility by re-exporting from sub-modules.
New code should import from ads.campaigns, ads.keywords, or ads.reports directly.
"""

from .ads.campaigns import CampaignsEndpoint
from .ads.keywords import KeywordsEndpoint
from .ads.reports import ReportsEndpoint


# Backward compatibility: expose all methods through a unified class
class AdsEndpoints(CampaignsEndpoint, KeywordsEndpoint, ReportsEndpoint):
    """广告API统一入口（向后兼容）"""

__all__ = ["AdsEndpoints", "CampaignsEndpoint", "KeywordsEndpoint", "ReportsEndpoint"]

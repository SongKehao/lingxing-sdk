"""Ads Endpoints - Backward Compatibility Wrapper"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase

from .ads.sb_ads import SBAdsEndpoint
from .ads.sd_ads import SDAdsEndpoint
from .ads.sp_ads import SPAdsEndpoint
from .ads.sp_reports import SPReportsEndpoint


class AdsEndpoints:

    def __init__(self, openapi: "OpenApiBase"):
        self._sp = SPAdsEndpoint(openapi)
        self._sp_reports = SPReportsEndpoint(openapi)
        self._sb = SBAdsEndpoint(openapi)
        self._sd = SDAdsEndpoint(openapi)

    def __getattr__(self, name):
        """Delegate method calls to appropriate sub-modules"""
        if name.startswith('get_sp_') and 'report' in name:
            return getattr(self._sp_reports, name)
        if name.startswith('get_sp_'):
            return getattr(self._sp, name)
        if name.startswith('get_sb_'):
            return getattr(self._sb, name)
        if name.startswith('get_sd_'):
            return getattr(self._sd, name)
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

"""Request models for Authorization APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class AuthorizationGetTokenRequest(LingXingModel):
    """Request for 获取 access-token和refresh-token.
    
    POST /api/auth-server/oauth/access-token
    """
    appId: str  # AppID，在ERP开放接口菜单中获取
    appSecret: str  # AppSecret，在ERP开放接口菜单中获取


class AuthorizationRefreshTokenRequest(LingXingModel):
    """Request for 续约接口令牌.
    
    POST /api/auth-server/oauth/refresh
    """
    appId: str  # AppID，在ERP开放接口中获取
    refreshToken: str  # refreshToken，获取接口令牌-token 接口对应字段【refresh_token】

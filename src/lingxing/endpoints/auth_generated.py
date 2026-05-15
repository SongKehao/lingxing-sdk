"""Auth API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class AuthEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_access_token(
        self,
        access_token: str,
        appId: str,
        appSecret: str
    ) -> dict[str, Any]:
        """
        获取 access-token和refresh-token

        API: /api/auth-server/oauth/access-token
        Method: POST

        Args:
            access_token: Access token for authentication
            appId: AppID，在ERP开放接口菜单中获取 (Required)
            appSecret: AppSecret，在ERP开放接口菜单中获取 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_access_token(token, ...)
            >>> print(result)
        """
        params = {
            "appId": appId,
            "appSecret": appSecret
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/api/auth-server/oauth/access-token",
            method="POST",
            req_body=params
        )



    async def refresh_token(
        self,
        access_token: str,
        appId: str,
        refreshToken: str
    ) -> dict[str, Any]:
        """
        续约接口令牌

        API: /api/auth-server/oauth/refresh
        Method: POST

        Args:
            access_token: Access token for authentication
            appId: AppID，在ERP开放接口中获取 (Required)
            refreshToken: refreshToken，获取接口令牌-token 接口对应字段【refresh_token】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.refresh_token(token, ...)
            >>> print(result)
        """
        params = {
            "appId": appId,
            "refreshToken": refreshToken
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/api/auth-server/oauth/refresh",
            method="POST",
            req_body=params
        )


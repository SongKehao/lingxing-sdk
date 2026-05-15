"""Base Endpoint Class for LingXing SDK"""

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase
    from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class BaseEndpoint:

    def __init__(self, openapi: "OpenApiBase"):
        self._openapi = openapi

    async def _request(
        self,
        access_token: str,
        route_name: str,
        req_body: dict[str, Any] | None = None,
        **kwargs
    ) -> "ResponseResult":
        """Send HTTP request via OpenAPI client"""
        return await self._openapi.request(
            access_token=access_token,
            route_name=route_name,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    def _parse_response(self, response: "ResponseResult") -> list[dict[str, Any]]:
        """Parse API response and extract data list"""
        if response.code not in [200, "200", 0, "0"]:
            logger.error("API error: %s", response.message)
            raise Exception(f"API error: {response.message}")

        data = response.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("list", data.get("data", []))
        return []

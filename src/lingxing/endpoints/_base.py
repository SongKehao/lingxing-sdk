"""Base endpoint mixin - provides typed request/response handling."""
from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic import BaseModel

from ..errors import ApiError
from ..core.resp_schema import ResponseResult

if TYPE_CHECKING:
    from ..core.openapi import OpenApiBase

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class BaseEndpoint:
    """Base class for all endpoint groups.

    Provides typed _post / _get helpers that:
    1. Send request via OpenApiBase
    2. Check response code
    3. Parse response data into typed Pydantic models
    """

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def _post(self, route: str, body: dict | None = None) -> ResponseResult:
        """Send POST request and check for errors."""
        resp = await self._openapi.request_with_auto_token(
            route_name=route,
            method="POST",
            req_body=body or {},
        )
        self._check_response(resp, route)
        return resp

    async def _get(self, route: str, params: dict | None = None) -> ResponseResult:
        """Send GET request and check for errors."""
        resp = await self._openapi.request_with_auto_token(
            route_name=route,
            method="GET",
            req_params=params,
        )
        self._check_response(resp, route)
        return resp

    def _check_response(self, resp: ResponseResult, route: str) -> None:
        """Raise ApiError if response indicates failure."""
        if resp.code != 0:
            raise ApiError(
                message=resp.message or f"API error code {resp.code}",
                code=resp.code,
                request_id=resp.request_id,
                url=route,
            )

    def _parse_list(self, data: Any, model: type[T]) -> list[T]:
        """Parse a list of dicts into a list of Pydantic models."""
        if data is None:
            return []
        if isinstance(data, list):
            return [model(**item) for item in data if isinstance(item, dict)]
        if isinstance(data, dict):
            # Some APIs return {"list": [...], "total": N}
            items = data.get("list") or data.get("data") or []
            if isinstance(items, list):
                return [model(**item) for item in items if isinstance(item, dict)]
        return []

    def _parse_one(self, data: Any, model: type[T]) -> T | None:
        """Parse a single dict into a Pydantic model."""
        if data is None:
            return None
        if isinstance(data, dict):
            return model(**data)
        return None

    def _parse_page(self, data: Any, model: type[T]) -> tuple[list[T], int]:
        """Parse paginated response: returns (items, total)."""
        if data is None:
            return [], 0
        if isinstance(data, list):
            items = [model(**item) for item in data if isinstance(item, dict)]
            return items, len(items)
        if isinstance(data, dict):
            total = data.get("total", 0)
            items_raw = data.get("list") or data.get("data") or []
            if isinstance(items_raw, list):
                items = [model(**item) for item in items_raw if isinstance(item, dict)]
                return items, total
        return [], 0

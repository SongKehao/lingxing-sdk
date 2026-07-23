"""Base endpoint mixin - provides typed request/response handling."""
from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any, AsyncIterator, TypeVar

from pydantic import BaseModel, ValidationError

from ..core.resp_schema import ResponseResult
from ..errors import ApiError, RateLimitError

if TYPE_CHECKING:
    from ..core.openapi import OpenApiBase

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)

# Default retry configuration
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_DELAY = 1.0  # seconds
RATE_LIMIT_ERROR_CODE = 3001008


def _run_async(coro):
    """Run an async coroutine synchronously, handling event loop edge cases."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop is None or not loop.is_running():
        return asyncio.run(coro)

    # Loop is already running (Jupyter, etc.)
    try:
        import nest_asyncio
        nest_asyncio.apply()
        return loop.run_until_complete(coro)
    except ImportError:
        raise RuntimeError(
            "Cannot call *_sync methods from a running event loop (e.g., Jupyter). "
            "Install nest-asyncio: pip install nest-asyncio, then call nest_asyncio.apply()"
        )


def _make_sync_wrapper(method_name):
    def sync_wrapper(self, *args, **kwargs):
        async_method = getattr(self, method_name)
        return _run_async(async_method(*args, **kwargs))
    return sync_wrapper


class SyncWrapperMeta(type):
    """Metaclass that auto-generates *_sync() mirror methods for public async methods."""

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if name == "BaseEndpoint":
            return cls
        for attr_name in dir(cls):
            if attr_name.startswith("_"):
                continue
            sync_name = f"{attr_name}_sync"
            if hasattr(cls, sync_name):
                continue
            method = getattr(cls, attr_name)
            if not asyncio.iscoroutinefunction(method):
                continue
            wrapper = _make_sync_wrapper(attr_name)
            wrapper.__name__ = sync_name
            wrapper.__qualname__ = f"{name}.{sync_name}"
            wrapper.__doc__ = f"(Sync) {method.__doc__}" if method.__doc__ else None
            setattr(cls, sync_name, wrapper)
        return cls


class BaseEndpoint(metaclass=SyncWrapperMeta):
    """Base class for all endpoint groups.

    Provides typed _post / _get helpers that:
    1. Send request via OpenApiBase
    2. Check response code
    3. Parse response data into typed Pydantic models (with fallback)
    4. Auto-retry on rate limit errors
    """

    # Retry configuration - can be overridden per subclass
    max_retries: int = DEFAULT_MAX_RETRIES
    retry_delay: float = DEFAULT_RETRY_DELAY

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def _post(
        self, route: str, body: dict | None = None, *, _retry_count: int = 0,
    ) -> ResponseResult:
        """Send POST request with automatic retry on rate limit errors."""
        try:
            resp = await self._openapi.request_with_auto_token(
                route_name=route, method="POST", req_body=body or {},
            )
            # Check for rate limit in response
            if resp.code == RATE_LIMIT_ERROR_CODE:
                if _retry_count < self.max_retries:
                    delay = self.retry_delay * (2 ** _retry_count)
                    logger.warning(
                        "Rate limited on %s, retrying in %.1fs (attempt %d/%d)",
                        route, delay, _retry_count + 1, self.max_retries,
                    )
                    await asyncio.sleep(delay)
                    return await self._post(route, body, _retry_count=_retry_count + 1)
                raise RateLimitError(
                    f"Rate limit exceeded for {route} after {self.max_retries} retries"
                )
            self._check_response(resp, route)
            return resp
        except RateLimitError:
            raise
        except ApiError:
            raise
        except Exception as e:
            # Retry on transient network errors
            if _retry_count < self.max_retries:
                delay = self.retry_delay * (2 ** _retry_count)
                logger.warning(
                    "Request failed for %s (%s), retrying in %.1fs (attempt %d/%d)",
                    route, str(e)[:100], delay, _retry_count + 1, self.max_retries,
                )
                await asyncio.sleep(delay)
                return await self._post(route, body, _retry_count=_retry_count + 1)
            raise

    async def _get(self, route: str, params: dict | None = None) -> ResponseResult:
        """Send GET request and check for errors."""
        resp = await self._openapi.request_with_auto_token(
            route_name=route, method="GET", req_params=params,
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
        """Parse a list of dicts into a list of Pydantic models.

        Falls back to raw dicts if model validation fails for any item.
        """
        if data is None:
            return []
        if isinstance(data, list):
            results: list = []
            for item in data:
                if not isinstance(item, dict):
                    continue
                try:
                    results.append(model(**item))
                except (ValidationError, Exception):
                    # 验证失败时用 model_construct 跳过验证，保留模型对象（字段原始值 + extra 兜底），
                    # 避免因个别字段类型不匹配就 fallback 成原始 dict（用户拿不到类型化模型）。
                    try:
                        results.append(model.model_construct(**item))
                    except Exception:
                        results.append(item)
            return results
        if isinstance(data, dict):
            items = data.get("list") or data.get("data") or data.get("records") or []
            if isinstance(items, list):
                results: list = []
                for item in items:
                    if not isinstance(item, dict):
                        continue
                    try:
                        results.append(model(**item))
                    except (ValidationError, Exception):
                        try:
                            results.append(model.model_construct(**item))
                        except Exception:
                            results.append(item)
                return results
        return []

    def _parse_one(self, data: Any, model: type[T]) -> T | None:
        """Parse a single dict into a Pydantic model."""
        if data is None:
            return None
        if isinstance(data, dict):
            try:
                return model(**data)
            except (ValidationError, Exception):
                try:
                    return model.model_construct(**data)
                except Exception:
                    return None
        return None

    def _parse_one_or_list(self, data: Any, model: type[T]) -> T | list[T]:
        """Parse response that may be a single object or a list of objects.

        Many LingXing APIs return either a list (of dicts) or a single dict
        depending on the query parameters.  This helper handles both cases:
        - If *data* is a list → return ``_parse_list(data, model)``
        - If *data* is a dict → try ``_parse_list`` first (the dict may wrap
          a list under ``list``/``data``/``records``), otherwise ``_parse_one``.
        """
        if data is None:
            return []
        if isinstance(data, list):
            return self._parse_list(data, model)
        if isinstance(data, dict):
            # Check if the dict wraps a list (common pagination pattern)
            items = data.get("list") or data.get("data") or data.get("records")
            if isinstance(items, list):
                return self._parse_list(data, model)
            # Otherwise treat as a single object
            result = self._parse_one(data, model)
            return result if result is not None else model()
        return []

    def _parse_page(self, data: Any, model: type[T]) -> tuple[list[T], int]:
        """Parse paginated response: returns (items, total)."""
        if data is None:
            return [], 0
        if isinstance(data, list):
            items = self._parse_list(data, model)
            return items, len(items)
        if isinstance(data, dict):
            total = data.get("total", 0) or 0
            items_raw = data.get("list") or data.get("data") or data.get("records") or []
            if isinstance(items_raw, list):
                items: list = []
                for item in items_raw:
                    if not isinstance(item, dict):
                        continue
                    try:
                        items.append(model(**item))
                    except (ValidationError, Exception):
                        items.append(item)
                return items, total
        return [], 0

    async def _iter_pages(
        self,
        route: str,
        model: type[T],
        page_size: int = 100,
        base_params: dict | None = None,
        offset_field: str = "offset",
        length_field: str = "length",
        max_pages: int | None = None,
    ) -> AsyncIterator[list[T]]:
        """Iterate over all pages of a paginated API endpoint.

        Yields lists of parsed model instances, one page at a time.

        Args:
            route: API route path.
            model: Pydantic model class to parse items.
            page_size: Number of items per page.
            base_params: Additional request parameters.
            offset_field: Name of the offset parameter.
            length_field: Name of the length parameter.
            max_pages: Maximum number of pages to fetch (None = unlimited).

        Yields:
            List of parsed model instances for each page.
        """
        offset = 0
        pages_fetched = 0

        while True:
            if max_pages is not None and pages_fetched >= max_pages:
                break

            params = dict(base_params or {})
            params[offset_field] = offset
            params[length_field] = page_size

            resp = await self._post(route, params)
            items, total = self._parse_page(resp.data, model)

            if not items:
                break

            yield items
            pages_fetched += 1
            offset += page_size

            if total > 0 and offset >= total:
                break

    async def _collect_all(
        self,
        route: str,
        model: type[T],
        page_size: int = 100,
        base_params: dict | None = None,
        max_items: int | None = None,
    ) -> list[T]:
        """Collect all items from a paginated API endpoint.

        Convenience method that collects all pages into a single list.

        Args:
            route: API route path.
            model: Pydantic model class to parse items.
            page_size: Number of items per page.
            base_params: Additional request parameters.
            max_items: Maximum number of items to collect (None = unlimited).

        Returns:
            List of all parsed model instances.
        """
        all_items: list[T] = []
        async for page_items in self._iter_pages(route, model, page_size, base_params):
            all_items.extend(page_items)
            if max_items is not None and len(all_items) >= max_items:
                return all_items[:max_items]
        return all_items

    # ==================== Public pagination helpers ====================

    async def collect_all(
        self,
        route: str,
        model: type[T],
        page_size: int = 100,
        base_params: dict | None = None,
        max_items: int | None = None,
    ) -> list[T]:
        """Public alias for _collect_all. Collect all items from a paginated endpoint."""
        return await self._collect_all(route, model, page_size, base_params, max_items)

    async def iter_pages(
        self,
        route: str,
        model: type[T],
        page_size: int = 100,
        base_params: dict | None = None,
        offset_field: str = "offset",
        length_field: str = "length",
        max_pages: int | None = None,
    ) -> AsyncIterator[list[T]]:
        """Public alias for _iter_pages. Iterate over pages of a paginated endpoint."""
        async for page in self._iter_pages(route, model, page_size, base_params, offset_field, length_field, max_pages):
            yield page

    async def collect_all_raw(
        self,
        route: str,
        page_size: int = 100,
        base_params: dict | None = None,
        offset_field: str = "offset",
        length_field: str = "length",
        max_pages: int | None = None,
    ) -> list[dict]:
        """Collect all pages from a paginated endpoint, returning raw dicts.

        Unlike collect_all(), this does not require a Pydantic model.
        It auto-detects the pagination structure from response data.
        """
        all_items: list[dict] = []
        offset = 0
        pages = 0
        while True:
            if max_pages is not None and pages >= max_pages:
                break
            params = dict(base_params or {})
            params[offset_field] = offset
            params[length_field] = page_size
            resp = await self._post(route, params)
            data = resp.data
            items: list = []
            total = 0
            if isinstance(data, list):
                items = data
                total = len(data)
            elif isinstance(data, dict):
                items = data.get("list") or data.get("data") or data.get("records") or []
                total = data.get("total", 0) or 0
            if not items:
                break
            all_items.extend(items)
            pages += 1
            offset += page_size
            if total > 0 and offset >= total:
                break
            if len(items) < page_size:
                break
        return all_items

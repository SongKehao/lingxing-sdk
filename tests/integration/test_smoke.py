"""Integration smoke tests.

Exercises the full pipeline the SDK builds on top of ``OpenApiBase``:

    signature (route + request body)
      -> pagination (offset/length across multiple pages)
      -> response parsing into typed Pydantic models
      -> graceful degradation when a single record fails validation.

An offset-aware mock (``PaginatedMockOpenApi``) lets us assert on the recorded
``_calls`` and drive real multi-page collection without hitting the network.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from conftest import MockOpenApi, MockResponseResult

from lingxing.endpoints.basic import BasicEndpoints
from lingxing.models.responses.basic_data import SellerListsResponse


class PaginatedMockOpenApi(MockOpenApi):
    """``MockOpenApi`` that serves successive pages sliced from a full record set.

    Mirrors the real paginated API contract: each request body carries
    ``offset``/``length``, the response returns that slice plus a ``total``, and
    the caller stops paginating once ``offset >= total``. Reuses the parent's
    ``_calls`` / ``call_count`` so call-shape assertions work unchanged.
    """

    def __init__(self, records):
        super().__init__()
        self._records = records

    async def request_with_auto_token(self, route_name, method, req_body=None, req_params=None, **kwargs):
        self._calls.append(
            {"route": route_name, "method": method, "body": req_body, "params": req_params}
        )
        body = req_body or {}
        offset = body.get("offset", 0)
        length = body.get("length", 100)
        page = self._records[offset : offset + length]
        # Real paginated endpoints return {"list": [...], "total": N}; using that
        # shape (not a bare list) is what lets _parse_page/collect_all advance pages.
        return MockResponseResult(code=0, data={"list": page, "total": len(self._records)})


@pytest.mark.asyncio
async def test_collect_all_paginates_signs_and_parses():
    """collect_all must (1) sign every POST with route + offset/length body,
    (2) fetch successive pages until total is reached, and (3) parse every
    record into the typed model."""
    records = [{"sid": i, "name": f"shop-{i}", "country": "US", "status": 1} for i in range(25)]
    route = "/erp/sc/data/seller/lists"
    api = PaginatedMockOpenApi(records)
    endpoint = BasicEndpoints(api)

    result = await endpoint.collect_all(route, SellerListsResponse, page_size=10)

    # (3) parsing: all 25 records become typed models
    assert len(result) == 25
    assert all(isinstance(r, SellerListsResponse) for r in result)
    assert result[0].sid == 0
    assert result[-1].sid == 24

    # (2) pagination: ceil(25 / 10) == 3 pages fetched
    assert api.call_count == 3
    # (1) signature: each call hit the right route/method with advancing offset
    for i, call in enumerate(api._calls):
        assert call["route"] == route
        assert call["method"] == "POST"
        assert call["body"]["offset"] == i * 10
        assert call["body"]["length"] == 10


@pytest.mark.asyncio
async def test_parse_list_retains_invalid_record_via_fallback():
    """A single record that fails model validation must not be dropped.

    The SDK degrades to ``model_construct`` (and ultimately raw dict) so the
    caller still receives every item. Here ``sid`` is ``Optional[int]``; a
    non-numeric value trips validation and exercises the fallback path wired
    through ``BasicEndpoints.list_sellers``.
    """
    api = PaginatedMockOpenApi(
        [
            {"sid": 1, "name": "good-shop", "country": "US"},
            {"sid": "not-an-int", "name": "bad-shop", "country": "UK"},
        ]
    )
    endpoint = BasicEndpoints(api)

    result = await endpoint.list_sellers()

    # both records retained (bad one via model_construct), valid one parsed normally
    assert len(result) == 2
    assert result[0].sid == 1
    assert result[0].name == "good-shop"

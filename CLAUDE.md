# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Lint (ruff)
ruff check src/ tests/

# Run all tests
pytest tests/ -v

# Run single test
pytest tests/test_endpoints_import.py -v

# Run with coverage
pytest --cov=lingxing --cov-report=term-missing
```

Environment variables needed:
```bash
LINGXING_APP_ID=your_app_id
LINGXING_APP_SECRET=your_app_secret
# Optional
LINGXING_HOST=https://openapi.lingxing.com  # default
```

## Architecture

### Two client layers

**`OpenApiBase`** — low-level async HTTP client in `core/openapi.py`. Handles token acquisition/refresh, rate limiting, and MD5 signing. Every business API call goes through here.

**`LingXingClient`** — high-level wrapper in `client.py`. Provides typed business methods (`get_products`, `get_stores`, etc.) that delegate to `OpenApiBase`. Use this for the SDK consumer API.

### Endpoint pattern

20 endpoint modules under `endpoints/` (e.g., `sale.py`, `finance.py`, `target_manage.py`). Each extends `BaseEndpoint` from `_base.py`.

**`BaseEndpoint`** provides:
- `_post(route, body)` / `_get(route, params)` — HTTP with auto-retry on rate limit (code 3001008), exponential backoff, max 3 retries
- `_parse_list` / `_parse_one` / `_parse_page` — Pydantic model parsing with graceful fallback to raw dicts
- `collect_all()` / `iter_pages()` / `collect_all_raw()` — public pagination helpers

**`SyncWrapperMeta`** — metaclass on `BaseEndpoint` auto-generates `*_sync()` mirror methods for every public async method. All async endpoint methods have synchronous counterparts.

### Model layer

- `models/requests/` — one file per endpoint domain, all request Pydantic models
- `models/responses/` — one file per endpoint domain, all response Pydantic models
- `models/common.py` — `LingXingModel` base with `alias_generator=_to_camel`, enabling camelCase ↔ snake_case auto-mapping. `extra="allow"` so unknown API fields don't break parsing.

### Code generation

`scripts/generate_finance_endpoints.py` auto-generates endpoint methods from request model docstrings. It reads `models/requests/finance.py`, extracts docstrings for API routes, and generates method stubs in `endpoints/finance.py`. The `ROUTE_OVERRIDES` dict handles request models whose docstrings lack a route path.

## Financial API routing

LingXing has two parallel profit API systems:

- **Old** (`/erp/sc/routing/finance/`, `/erp/sc/data/finance/`) — used by existing finance endpoint methods
- **New BD** (`/bd/profit/report/open/report/...`) — use for BD profit reports (MSKU, ASIN, parent ASIN, SKU, seller, order)
- **New settlement** (`/bd/sp/api/open/settlement/...`) — use for settlement center APIs

When adding new financial endpoints, distinguish which API path the method should call.

## Important conventions

- `sid` parameter: `bigint` in DB, pass as `int` or `str` in SDK — no coercion needed
- Column naming: `country` (not `marketplace_id`) for country filter in PG queries
- Pagination: `offset` / `length` for most endpoints; some use `page` / `pageSize` — check the request model docstring
- API routes in docstrings use camelCase path segments matching LingXing's OpenAPI spec

## Shared state

`src/lingxing/core/param_builder.py` — `APIParamBuilder` with `DEFAULT_SIDS = [4661, 109]`. This sets default store IDs for ETL scripts. Override with `set_default_sids()` on `LingXingClient` or pass `sids` explicitly.

`src/lingxing/core/rate_limiter.py` — global singleton `RateLimiter`. Token endpoints share a separate limit from business API endpoints.
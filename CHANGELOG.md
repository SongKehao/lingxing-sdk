# Changelog

## v0.5.0 (2026-05-16)

### Major Changes
- **382 endpoint methods converted from `**kwargs` to typed parameters**
  - All parameters have explicit type annotations (str, int, float, list, dict, Any)
  - All parameters default to `None` (optional) for maximum flexibility
  - Dict comprehension filters `None` values before sending to API
- **465 Response models generated** from API documentation
  - 18 model files covering all API categories
  - All fields typed with descriptions from API docs
- **103 ruff lint errors fixed** — All checks passed
- **`from typing import Any` added** to 13 endpoint files
- **13 methods remain with `**kwargs`** (API docs lack parameter definitions for these)

### Stats
- Request models: 795
- Response models: 465
- Typed methods: 387 / 400 total
- Remaining `**kwargs`: 13
- Tests: 135 passed, 4 skipped, 0 failed
- Source lines: ~41,000
- Ruff: All checks passed!

## v0.4.0 (2026-05-16)

### Major Changes
- **All `**kwargs` eliminated** — 396 endpoint methods now have typed parameters
- **795 Pydantic Request models** auto-generated from official API docs (19 files)
- **465 Pydantic Response models** auto-generated from API docs (18 files)
- **395 Chinese docstrings** injected from API docs (title + param descriptions)

### New Features
- **Auto-retry** — exponential backoff on rate limit (code 3001008) and network errors
- **Pagination iterator** — `_iter_pages()` and `_collect_all()` for automatic page traversal
- **RateLimitError** — dedicated exception for rate limit exhaustion after max retries
- **Package exports** — 57 public APIs in `lingxing.__all__`, 19 endpoint classes
- **`from __future__ import annotations`** — Python 3.10+ union syntax throughout

### Test Coverage
- **135 tests passing** (up from 115)
  - 20 new tests: auto-retry (5), pagination (7), response models (3), request models (1), exports (4)
  - All 115 existing tests continue passing

### Version
- Bumped to 0.4.0

## v0.3.0 (2026-05-16)

### Breaking Changes
- `models_legacy.py` removed → use `models.business` instead
- `ResponseResult` migrated from Pydantic V1 `@root_validator` to V2 `@model_validator`
- All endpoint methods now return typed results (list[ModelItem] or dict)

### New Features
- **37 Pydantic response models** auto-generated from real API responses
  - basic: AccoutListsItem, SellerListsItem, AllMarketplaceItem, ConceptSellerListsItem
  - fba: GetFbaProductListItem, ShipmentPlanListsItem, etc. (6 models)
  - product: ProductListsItem, BrandItem, CategoryItem, etc. (5 models)
  - purchase: PurchaseOrderListItem, SupplierItem, etc. (4 models)
  - warehouse: WarehouseListsItem, InventoryDetailsItem, etc. (17 models)
  - statistics: MonthRefundItem (1 model)
- **BaseEndpoint** base class with typed helpers: `_post`, `_get`, `_parse_list`, `_parse_page`
  - Graceful fallback: if Pydantic validation fails for an item, returns raw dict instead of crashing
- **Custom exceptions**: `ApiError`, `AuthenticationError`, `RateLimitError`, `ValidationError`
- **Shared types**: `PageRequest`, `PageResult`, `DateRangeRequest`, `SellerFilteredRequest`
- **51 recorded API fixtures** (8MB) for replay testing

### Test Coverage
- **115 tests passing** (up from 26)
  - 19 module import verification tests
  - 51 fixture replay tests (parametrized)
  - 18 basic endpoint + model tests
  - 4 detailed module tests (warehouse, fba, product)
  - 8 config/sign/client tests
  - 3 integration tests
- **0 warnings** (Pydantic V2 migration complete)

### Bug Fixes
- `AccoutListsItem.mobile` field type: `int` → `str` (API returns empty string)
- `_parse_list` now handles nested list/dict fields gracefully (fallback to raw dict)
- Empty API responses (`[]`) no longer crash model parsing

## v0.2.0 (2026-05-15)

- Initial typed SDK with Pydantic models
- 400 API endpoint methods across 19 modules
- BaseEndpoint base class
- Recorded fixture testing framework

## v0.1.0 (2026-05-14)

- Initial release
- 400 API methods with correct routes from official docs
- Basic client, config, signing, authentication

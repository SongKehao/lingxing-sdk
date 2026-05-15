# Changelog

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

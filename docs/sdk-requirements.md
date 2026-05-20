# lingxing-sdk Enhancement Requirements

## P0 - Must Have (1-2 days)

### 1. Sync call wrappers
SDK is all async, but pipeline/cron needs sync interfaces.
**Solution**: `SyncWrapperMeta` metaclass on `BaseEndpoint` auto-generates `*_sync()` mirror methods for every public async method.
**Status**: DONE

### 2. Public pagination iterator
`_collect_all()` was private.
**Solution**: Added public `collect_all()`, `iter_pages()`, and `collect_all_raw()` (no Pydantic model required).
**Status**: DONE

## P1 - Important (3-5 days)

### 3. Amazon SP advertising API
SDK only had Lazada/TikTok/Shopee/Walmart ads. No Amazon SP (campaign/ad_group/keyword/search_term).
**Solution**: Generated 53 endpoint methods from existing request models. Covers SP/SB/SD reports, base data, hour data, ABA report, API logs.
**Status**: DONE

### 4. Product performance / order profit API params
MCP had `summary_field`, `currency_code` etc that SDK was missing.
**Solution**: Added `product_performance()` method to `StatisticsEndpoints` with full parameter set (summary_field, currency_code, search_field, search_value, extend_search, etc).
**Note**: Profit report endpoints for `/bd/profit/report/open/report/...` routes (7 endpoints) are still missing from the endpoint classes - these exist as request models but no endpoint methods were generated yet. Also settlement center endpoints for `/bd/sp/api/open/...` (2 endpoints) are missing.
**Status**: PARTIALLY DONE

### 5. FBA inventory cost field
MCP has `is_cost_page=1` returning `cg_price`, SDK's `fba_stock_v2` was missing this.
**Solution**: Added `is_cost_page: int = None` parameter to `fba_stock_v2()`.
**Status**: DONE

## P2/P3 - Nice to Have (deferred)

### 6. Pydantic return models for core APIs
Add type hints for listing/orders/fba/profit endpoints.

### 7. Field name standardization
Unify sid/seller_id/sku/seller_sku naming across endpoints.

### 8. Rate limit monitoring + request logging
Enhance observability for API call tracking.

## Audit Findings (from P1-4)

Missing endpoints that need request models but have no endpoint methods:
- `/bd/profit/report/open/report/msku/list` - MSKU profit report
- `/bd/profit/report/open/report/asin/list` - ASIN profit report
- `/bd/profit/report/open/report/parent/asin/list` - Parent ASIN profit report
- `/bd/profit/report/open/report/sku/list` - SKU profit report
- `/bd/profit/report/open/report/seller/list` - Seller profit report
- `/bd/profit/report/open/report/seller/summary/list` - Seller summary
- `/bd/profit/report/open/report/order/list` - Order profit report
- `/bd/sp/api/open/settlement/summary/list` - Settlement summary
- `/bd/sp/api/open/settlement/transaction/detail/list` - Settlement transaction detail

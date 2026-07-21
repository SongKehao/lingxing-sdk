"""Import verification test - ensure all 400 endpoint methods load correctly."""
import asyncio
import pytest


def test_all_endpoints_import():
    """All 19 endpoint classes should import without error."""
    from lingxing.endpoints import (
        AmazonSourceEndpoints,
        BasicEndpoints,
        CustomerServiceEndpoints,
        FBAEndpoints,
        FinanceEndpoints,
        LogisticsEndpoints,
        MultiplatformAdsEndpoints,
        MultiplatformOtherEndpoints,
        MultiplatformPlatformsEndpoints,
        NewAdEndpoints,
        ProductEndpoints,
        PurchaseEndpoints,
        RestockingEndpoints,
        RestockingLimitEndpoints,
        SaleEndpoints,
        StatisticsEndpoints,
        ToolsEndpoints,
        VCEndpoints,
        WarehouseEndpoints,
    )
    classes = [
        AmazonSourceEndpoints, BasicEndpoints, CustomerServiceEndpoints,
        FBAEndpoints, FinanceEndpoints, LogisticsEndpoints,
        MultiplatformAdsEndpoints, MultiplatformOtherEndpoints,
        MultiplatformPlatformsEndpoints, NewAdEndpoints, ProductEndpoints,
        PurchaseEndpoints, RestockingEndpoints, RestockingLimitEndpoints,
        SaleEndpoints, StatisticsEndpoints, ToolsEndpoints, VCEndpoints,
        WarehouseEndpoints,
    ]
    assert len(classes) == 19


def test_total_method_count():
    """Total async endpoint methods should be 400."""
    from lingxing import endpoints as ep
    total = 0
    for name in ep.__all__:
        cls = getattr(ep, name)
        methods = [
            m for m in dir(cls)
            if not m.startswith('_')
            and asyncio.iscoroutinefunction(getattr(cls, m))
        ]
        total += len(methods)
    assert total == 561, f"Expected 561 async methods, got {total}"


def test_sync_wrappers_generated():
    """Every public async method should have a *_sync counterpart."""
    from lingxing import endpoints as ep
    for name in ep.__all__:
        cls = getattr(ep, name)
        async_methods = [
            m for m in dir(cls)
            if not m.startswith('_')
            and asyncio.iscoroutinefunction(getattr(cls, m))
        ]
        for method_name in async_methods:
            sync_name = f"{method_name}_sync"
            assert hasattr(cls, sync_name), f"{name}.{sync_name} missing"
            assert not asyncio.iscoroutinefunction(getattr(cls, sync_name)), f"{name}.{sync_name} should be sync"


def test_sync_wrappers_exclude_private():
    """Private methods should NOT get sync wrappers."""
    from lingxing.endpoints._base import BaseEndpoint
    assert not hasattr(BaseEndpoint, '_post_sync')
    assert not hasattr(BaseEndpoint, '_collect_all_sync')


def test_key_routes_correct():
    """Verify key API routes use correct doc-verified paths."""
    from lingxing.endpoints.sale import SaleEndpoints
    from lingxing.endpoints.warehouse import WarehouseEndpoints
    from lingxing.endpoints.finance import FinanceEndpoints
    import inspect

    # Check that sale module has the correct order listing path
    sale_src = inspect.getsource(SaleEndpoints)
    assert '/erp/sc/data/mws/orders' in sale_src, "Order listing path should use /erp/sc/data/mws/orders"
    assert '/erp/sc/data/mws/listing' in sale_src, "Listing path should use /erp/sc/data/mws/listing"

    # Check warehouse module has correct inventory path
    wh_src = inspect.getsource(WarehouseEndpoints)
    assert '/erp/sc/routing/owms/inbound/listInbound' in wh_src

    # Check finance module has correct paths
    fin_src = inspect.getsource(FinanceEndpoints)
    assert '/basicOpen/finance/shopee/adjustment/list' in fin_src

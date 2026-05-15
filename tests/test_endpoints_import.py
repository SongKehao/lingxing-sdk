"""Import verification test - ensure all 400 endpoint methods load correctly."""
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
    """Total endpoint methods should be 400."""
    from lingxing import endpoints as ep
    total = 0
    for name in ep.__all__:
        cls = getattr(ep, name)
        methods = [m for m in dir(cls) if not m.startswith('_') and callable(getattr(cls, m))]
        total += len(methods)
    assert total == 400, f"Expected 400 methods, got {total}"


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

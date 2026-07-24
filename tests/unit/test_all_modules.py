"""Comprehensive fixture replay tests for all modules with recorded data.

Fixtures are loaded from the committed, desensitized samples in
``tests/api_responses/*.json`` (each file is a single-key dict keyed by
``"<Category>/<Route>"``). They are merged at import time into ALL_FIXTURES,
keeping the original ``"<Category>/"`` prefix so ``_group_by_category()`` works
unchanged. This replaces the previous gitignored 8MB
``tests/fixtures/api_responses.json`` whose absence on CI made the parametrized
replay below collect zero tests and pass vacuously (silent green).
"""

import glob
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from conftest import MockOpenApi, MockResponseResult

# Load committed desensitized fixtures (tests/api_responses/*.json) and merge.
# Each file is a single-key dict; merging preserves the "Category/" prefix used
# by _group_by_category() below.
_API_RESPONSES_DIR = os.path.join(os.path.dirname(__file__), "..", "api_responses")
ALL_FIXTURES: dict = {}
for _path in sorted(glob.glob(os.path.join(_API_RESPONSES_DIR, "*.json"))):
    with open(_path) as _f:
        ALL_FIXTURES.update(json.load(_f))


# Map fixture category -> (endpoint_module, endpoint_class, model_module)
# NOTE: model_module points at the real response-model module
# (lingxing.models.responses.<domain>), not the non-existent lingxing.models.<domain>.
FIXTURE_MODULE_MAP = {
    "BasicData": (
        "lingxing.endpoints.basic",
        "BasicEndpoints",
        "lingxing.models.responses.basic_data",
    ),
    "FBA": ("lingxing.endpoints.fba", "FBAEndpoints", "lingxing.models.fba"),
    "Product": ("lingxing.endpoints.product", "ProductEndpoints", "lingxing.models.product"),
    "Purchase": ("lingxing.endpoints.purchase", "PurchaseEndpoints", "lingxing.models.purchase"),
    "Warehouse": (
        "lingxing.endpoints.warehouse",
        "WarehouseEndpoints",
        "lingxing.models.warehouse",
    ),
    "Statistics": (
        "lingxing.endpoints.statistics",
        "StatisticsEndpoints",
        "lingxing.models.statistics",
    ),
}

# Explicit fixture-name -> endpoint-method overrides.
# get_endpoint_method() infers method names by snake-casing the route segment,
# which is wrong for BasicData: e.g. "SellerLists" -> "seller_lists" but the real
# method is BasicEndpoints.list_sellers. Map these explicitly so the committed
# fixtures actually exercise the endpoint instead of being skipped.
FIXTURE_METHOD_OVERRIDE = {
    "BasicData/SellerLists": "list_sellers",
    "BasicData/AccoutLists": "list_accounts",
    "BasicData/AllMarketplace": "list_marketplaces",
}


def get_endpoint_method(fixture_name):
    """Map fixture name to endpoint method name."""
    import re

    raw = fixture_name.split("/")[-1]
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", raw)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return re.sub(r"[^a-zA-Z0-9]", "_", s2).lower().strip("_")


def make_parametrize_data():
    """Build parametrized test data."""
    tests = []
    for cat, fixtures_data in _group_by_category().items():
        if cat not in FIXTURE_MODULE_MAP:
            continue
        for name, fixture in fixtures_data.items():
            tests.append((cat, name, fixture))
    return tests


def _group_by_category():
    cats = {}
    for name, fixture in ALL_FIXTURES.items():
        cat = name.split("/")[0]
        cats.setdefault(cat, {})[name] = fixture
    return cats


@pytest.mark.asyncio
@pytest.mark.parametrize("cat,name,fixture", make_parametrize_data())
async def test_fixture_replay(cat, name, fixture):
    """Replay each recorded API response and verify parsing."""
    ep_module, ep_class, model_module = FIXTURE_MODULE_MAP[cat]

    # Dynamic import
    ep_mod = __import__(ep_module, fromlist=[ep_class])
    endpoint_cls = getattr(ep_mod, ep_class)

    resp_data = fixture.get("response", {}).get("data")
    api = MockOpenApi(response=MockResponseResult(code=0, data=resp_data))
    endpoint = endpoint_cls(api)

    method_name = FIXTURE_METHOD_OVERRIDE.get(name) or get_endpoint_method(name)
    method = getattr(endpoint, method_name, None)

    if method is None:
        pytest.fail(f"Method {method_name} not found in {ep_class} for fixture {name}")

    result = await method()

    # Verify we got a result (list or dict)
    if isinstance(resp_data, list):
        if len(resp_data) == 0:
            # Empty list response - endpoint may return empty list or empty dict
            assert result is not None, f"Got None for {name}"
        else:
            assert isinstance(result, list), f"Expected list for {name}, got {type(result)}"
            assert len(result) == len(resp_data), f"Length mismatch for {name}"
    elif isinstance(resp_data, dict):
        if isinstance(result, tuple):
            # paginated: (list, total)
            items, total = result
            assert isinstance(items, list), f"Expected list in tuple for {name}"
        elif isinstance(result, dict):
            assert result is not None, f"Got None for {name}"


def test_fixtures_committed():
    """Guard against silent CI green.

    If no fixtures are loaded, the parametrized ``test_fixture_replay`` above
    collects zero tests and the suite passes vacuously. Fail loudly instead so a
    broken checkout / missing ``tests/api_responses/`` directory is caught
    instead of masquerading as a green build.
    """
    if not ALL_FIXTURES:
        pytest.fail(
            "FIXTURES NOT COMMITTED: tests/api_responses/*.json missing or empty "
            "(parametrized fixture replay would collect 0 tests)"
        )


class TestAllModuleImports:
    """Verify every endpoint module and model module can be imported."""

    MODULES = [
        "lingxing.endpoints.basic",
        "lingxing.endpoints.fba",
        "lingxing.endpoints.restocking_limit",
        "lingxing.endpoints.restocking",
        "lingxing.endpoints.finance",
        "lingxing.endpoints.logistics",
        "lingxing.endpoints.multiplatform_ads",
        "lingxing.endpoints.multiplatform_other",
        "lingxing.endpoints.multiplatform_platforms",
        "lingxing.endpoints.new_ad",
        "lingxing.endpoints.product",
        "lingxing.endpoints.purchase",
        "lingxing.endpoints.sale",
        "lingxing.endpoints.customer_service",
        "lingxing.endpoints.amazon_source",
        "lingxing.endpoints.statistics",
        "lingxing.endpoints.tools",
        "lingxing.endpoints.vc",
        "lingxing.endpoints.warehouse",
    ]

    @pytest.mark.parametrize("module", MODULES, ids=lambda m: m.split(".")[-1])
    def test_import(self, module):
        mod = __import__(module, fromlist=[""])
        # Find the endpoint class
        classes = [name for name in dir(mod) if name.endswith("Endpoints")]
        assert len(classes) == 1, f"Expected 1 Endpoints class in {module}, found {classes}"

    @pytest.mark.parametrize("module", MODULES, ids=lambda m: m.split(".")[-1])
    def test_has_methods(self, module):
        mod = __import__(module, fromlist=[""])
        classes = [name for name in dir(mod) if name.endswith("Endpoints")]
        cls = getattr(mod, classes[0])
        methods = [m for m in dir(cls) if not m.startswith("_") and callable(getattr(cls, m))]
        assert len(methods) > 0, f"No methods found in {module}"


class TestWarehouseModuleDetailed:
    """Detailed tests for the largest module (warehouse, 76 methods)."""

    def setup_method(self):
        self.api = MockOpenApi()
        from lingxing.endpoints.warehouse import WarehouseEndpoints

        self.wh = WarehouseEndpoints(self.api)

    @pytest.mark.asyncio
    async def test_warehouse_lists(self):
        """Test warehouse lists with model parsing."""
        from lingxing.models.responses.warehouse import WarehouseListsItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"wid": 1, "name": "深圳仓", "type": 1}],
        )
        result = await self.wh.warehouse_lists()
        assert len(result) == 1
        assert isinstance(result[0], WarehouseListsItem)
        assert result[0].name == "深圳仓"

    @pytest.mark.asyncio
    async def test_warehouse_lists_sends_correct_route(self):
        """Verify correct URL is called."""
        await self.wh.warehouse_lists()
        assert "warehouse" in self.api.last_call["route"]

    @pytest.mark.asyncio
    async def test_inventory_details(self):
        """Test inventory details parsing."""
        from lingxing.models.responses.warehouse import InventoryDetailsItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"sku": "TEST-SKU", "wid": 1, "available_num": 100}],
        )
        result = await self.wh.inventory_details()
        assert len(result) == 1
        assert isinstance(result[0], InventoryDetailsItem)
        assert result[0].sku == "TEST-SKU"


class TestFBAModuleDetailed:
    """Detailed tests for FBA module."""

    def setup_method(self):
        self.api = MockOpenApi()
        from lingxing.endpoints.fba import FBAEndpoints

        self.fba = FBAEndpoints(self.api)

    @pytest.mark.asyncio
    async def test_fba_product_list(self):
        """Test FBA product list with typed model."""
        from lingxing.models.responses.fba import GetFbaProductListItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"msku": "TEST-MSKU", "asin": "B0TEST", "fnsku": "X00TEST"}],
        )
        result = await self.fba.get_fba_product_list()
        assert len(result) == 1
        assert isinstance(result[0], GetFbaProductListItem)
        assert result[0].asin == "B0TEST"

    @pytest.mark.asyncio
    async def test_shipment_plan_lists(self):
        """Test shipment plan lists."""
        from lingxing.models.responses.fba import ShipmentPlanListsItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"shipment_id": "SHP123", "status": 0}],
        )
        result = await self.fba.shipment_plan_lists()
        assert len(result) == 1


class TestProductModuleDetailed:
    """Detailed tests for Product module."""

    def setup_method(self):
        self.api = MockOpenApi()
        from lingxing.endpoints.product import ProductEndpoints

        self.product = ProductEndpoints(self.api)

    @pytest.mark.asyncio
    async def test_product_lists(self):
        """Test product lists with typed model."""
        from lingxing.models.responses.product import ProductListsItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"pid": 1, "name": "Test Product", "sku": "TEST-SKU"}],
        )
        result = await self.product.product_lists()
        assert len(result) == 1
        assert isinstance(result[0], ProductListsItem)

    @pytest.mark.asyncio
    async def test_brand_list(self):
        """Test brand list."""
        from lingxing.models.responses.product import BrandItem

        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"brand_id": 1, "brand_name": "TestBrand"}],
        )
        result = await self.product.brand()
        assert len(result) == 1
        assert isinstance(result[0], BrandItem)

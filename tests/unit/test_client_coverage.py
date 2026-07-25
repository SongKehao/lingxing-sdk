"""Coverage for LingXingClient: business-method delegation, response parsing, and lifecycle.

The real OpenApiBase is replaced with the shared MockOpenApi so we can assert the
route/method/params each method emits and how responses are parsed — no network.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from conftest import MockOpenApi, MockResponseResult  # noqa: E402

from lingxing.client import LingXingClient  # noqa: E402
from lingxing.config import LingXingConfig  # noqa: E402
from lingxing.models.business import (  # noqa: E402
    AllocationOrderInfo,
    FBAShipment,
    InboundShipmentInfo,
    InventoryInfo,
    LogisticsChannelInfo,
    LogisticsProviderInfo,
    MSKUProfitInfo,
    OrderInfo,
    OrderProfitInfo,
    ProductInfo,
    PurchaseOrderInfo,
    PurchasePlanInfo,
    PurchaseReturnInfo,
    SettlementInfo,
    SettlementSummaryInfo,
    ShipmentDetailInfo,
    StoreInfo,
    SupplierInfo,
    WarehouseInfo,
    WarehouseInventoryInfo,
    WarehouseStatementInfo,
)


def _config() -> LingXingConfig:
    return LingXingConfig(app_id="test_id", app_secret="test_secret", host="https://openapi.test")


def _client(data=None, code: int = 0, responses=None) -> LingXingClient:
    client = LingXingClient(_config())
    client._openapi = MockOpenApi(response=MockResponseResult(code=code, data=data), responses=responses)
    return client


# ── _request delegation & LingXingResponse mapping ───────────────────────────


class TestRequestDelegation:
    async def test_request_maps_response_fields(self):
        client = _client()
        client._openapi = MockOpenApi(
            response=MockResponseResult(code=0, data={"k": "v"}, message="ok", request_id="rid")
        )
        resp = await client._request(route_name="/r", method="GET", req_params={"a": 1})
        assert resp.code == 0
        assert resp.message == "ok"
        assert resp.data == {"k": "v"}
        assert resp.request_id == "rid"
        assert resp.is_success is True
        # delegation captured route/method/params
        assert client._openapi.last_call["route"] == "/r"
        assert client._openapi.last_call["method"] == "GET"
        assert client._openapi.last_call["params"] == {"a": 1}


# ── business-method route + parse (parametrized) ─────────────────────────────


def _cases():
    """(name, factory, expected_route, expected_method, expected_item_type)."""
    d0, d1 = datetime(2024, 1, 1), datetime(2024, 1, 31)
    return [
        ("get_products", lambda c: c.get_products(), "/erp/sc/routing/data/local_inventory/productList", "POST", ProductInfo),
        ("get_orders", lambda c: c.get_orders(start_date=d0, end_date=d1), "/erp/sc/data/order/lists", "GET", OrderInfo),
        ("get_inventory", lambda c: c.get_inventory(), "/erp/sc/data/local_inventory/lists", "GET", InventoryInfo),
        ("get_fba_shipments", lambda c: c.get_fba_shipments(), "/basicOpen/openapi/storage/fbaWarehouseDetail", "POST", FBAShipment),
        ("get_stores", lambda c: c.get_stores(), "/erp/sc/data/seller/lists", "GET", StoreInfo),
        ("get_warehouse_list", lambda c: c.get_warehouse_list(), "/erp/sc/data/local_inventory/warehouse", "POST", WarehouseInfo),
        ("get_warehouse_inventory", lambda c: c.get_warehouse_inventory(warehouse_id="w1"), "/erp/sc/routing/data/local_inventory/inventoryDetails", "POST", WarehouseInventoryInfo),
        ("get_inventory_statement", lambda c: c.get_inventory_statement(d0, d1), "/erp/sc/routing/data/local_inventory/getBatchStatementList", "POST", WarehouseStatementInfo),
        ("get_allocation_orders", lambda c: c.get_allocation_orders(d0, d1), "/erp/sc/data/wms/allocation/getStorageAllocationList", "POST", AllocationOrderInfo),
        ("get_inbound_shipments", lambda c: c.get_inbound_shipments(d0, d1), "/erp/sc/routing/storage/shipment/getInboundShipmentList", "POST", InboundShipmentInfo),
        ("get_shipment_details", lambda c: c.get_shipment_details("sh1"), "/basicOpen/openapi/fba/getInboundShipmentListMwsDetail", "POST", ShipmentDetailInfo),
        ("get_logistics_channels", lambda c: c.get_logistics_channels(provider_id="p1"), "/erp/sc/data/local_inventory/channelList", "POST", LogisticsChannelInfo),
        ("get_purchase_orders", lambda c: c.get_purchase_orders(d0, d1), "/erp/sc/purchase/order/lists", "POST", PurchaseOrderInfo),
        ("get_suppliers", lambda c: c.get_suppliers(), "/erp/sc/purchase/supplier/lists", "GET", SupplierInfo),
        ("get_purchase_plans", lambda c: c.get_purchase_plans(), "/erp/sc/purchase/plan/getPurchasePlans", "GET", PurchasePlanInfo),
        ("get_purchase_returns", lambda c: c.get_purchase_returns(d0, d1), "/erp/sc/purchase/return/getPurchaseReturnOrderList", "POST", PurchaseReturnInfo),
        ("get_order_profit", lambda c: c.get_order_profit(d0, d1), "/erp/sc/data/finance/bdOrder", "POST", OrderProfitInfo),
        ("get_msku_profit", lambda c: c.get_msku_profit(d0, d1), "/erp/sc/data/finance/bdMSKU", "POST", MSKUProfitInfo),
        ("get_settlement_detail", lambda c: c.get_settlement_detail(d0, d1), "/erp/sc/data/finance/settlementTransactionList", "POST", SettlementInfo),
        ("get_settlement_summary", lambda c: c.get_settlement_summary(d0, d1), "/erp/sc/data/finance/settlementSummaryList", "POST", SettlementSummaryInfo),
    ]


@pytest.mark.parametrize("name, factory, route, method, item_type", _cases())
async def test_business_method_route_and_parse(name, factory, route, method, item_type):
    client = _client(data=[{"_any": 1}])
    result = await factory(client)
    assert client._openapi.last_call["route"] == route
    assert client._openapi.last_call["method"] == method
    assert len(result) == 1
    assert isinstance(result[0], item_type)


# ── parse branches ───────────────────────────────────────────────────────────


class TestParseBranches:
    async def test_get_products_dict_with_data_key(self):
        client = _client(data={"data": [{"pid": 1}]})
        products = await client.get_products()
        assert len(products) == 1
        assert isinstance(products[0], ProductInfo)

    async def test_get_products_empty_data(self):
        client = _client(data=None)
        assert await client.get_products() == []

    async def test_get_products_error_raises(self):
        client = _client(data=None, code=500)
        client._openapi._default_response = MockResponseResult(code=500, message="boom")
        with pytest.raises(Exception, match="API error: boom"):
            await client.get_products()

    async def test_get_warehouse_list_list_key(self):
        client = _client(data={"list": [{"wid": "x"}]})
        items = await client.get_warehouse_list()
        assert len(items) == 1
        assert isinstance(items[0], WarehouseInfo)

    async def test_get_logistics_providers_providers_key(self):
        client = _client(data={"providers": [{"id": 1}]})
        items = await client.get_logistics_providers()
        assert len(items) == 1
        assert isinstance(items[0], LogisticsProviderInfo)

    async def test_get_sellers_returns_raw_list(self):
        client = _client(data=[{"sid": 1}, {"sid": 2}])
        sellers = await client.get_sellers()
        assert sellers == [{"sid": 1}, {"sid": 2}]

    async def test_get_sellers_returns_nested_list(self):
        client = _client(data={"data": [{"sid": 9}]})
        assert await client.get_sellers() == [{"sid": 9}]

    async def test_get_sellers_empty_when_unknown_shape(self):
        client = _client(data={"unrelated": 1})
        assert await client.get_sellers() == []

    async def test_get_warehouse_inventory_passes_wid(self):
        client = _client(data=[])
        await client.get_warehouse_inventory(warehouse_id="wh9")
        assert client._openapi.last_call["body"]["wid"] == "wh9"

    async def test_get_logistics_channels_offset(self):
        client = _client(data=[])
        await client.get_logistics_channels(page=3, page_size=50)
        body = client._openapi.last_call["body"]
        assert body["offset"] == 100  # (3-1)*50
        assert body["length"] == 50


# ── product performance (dict return) ────────────────────────────────────────


class TestProductPerformance:
    async def test_returns_dict_data(self):
        client = _client(data={"rows": [{"asin": "B00"}]})
        result = await client.get_product_performance(sid=4661, start_date="2024-01-01", end_date="2024-01-31")
        assert result == {"rows": [{"asin": "B00"}]}
        assert client._openapi.last_call["route"] == "/bd/productPerformance/openApi/asinList"

    async def test_non_dict_data_returns_empty(self):
        client = _client(data=[1, 2, 3])
        result = await client.get_product_performance(sid=1, start_date="2024-01-01", end_date="2024-01-31")
        assert result == {}


# ── call_api ─────────────────────────────────────────────────────────────────


class TestCallApi:
    async def test_post_with_param_names(self):
        client = _client(data={"ok": 1})
        resp = await client.call_api(
            api_path="/bd/profit/report/open/report/msku/list",
            method="POST",
            params={"sids": [4661]},
            param_names={"sids", "startDate", "endDate", "offset", "length"},
        )
        assert resp.is_success is True
        assert client._openapi.last_call["method"] == "POST"
        assert client._openapi.last_call["route"] == "/bd/profit/report/open/report/msku/list"
        # param builder should have populated sids default
        assert "sids" in client._openapi.last_call["body"]

    async def test_get_without_param_names(self):
        client = _client(data={"ok": 1})
        resp = await client.call_api(api_path="/some/get", method="GET", params={"q": "v"})
        assert resp.is_success is True
        assert client._openapi.last_call["method"] == "GET"
        assert client._openapi.last_call["params"] == {"q": "v"}

    async def test_default_method_is_post(self):
        client = _client(data={})
        await client.call_api(api_path="/x", params={"a": 1})
        assert client._openapi.last_call["method"] == "POST"


# ── execute dispatch ─────────────────────────────────────────────────────────


class TestExecute:
    @pytest.mark.parametrize(
        "op, route",
        [
            ("get_products", "/erp/sc/routing/data/local_inventory/productList"),
            ("get_orders", "/erp/sc/data/order/lists"),
            ("get_inventory", "/erp/sc/data/local_inventory/lists"),
            ("get_fba_shipments", "/basicOpen/openapi/storage/fbaWarehouseDetail"),
            ("get_stores", "/erp/sc/data/seller/lists"),
        ],
    )
    async def test_known_operations(self, op, route):
        client = _client(data=[])
        await client.execute(op)
        assert client._openapi.last_call["route"] == route

    async def test_unknown_operation_raises(self):
        client = _client(data=[])
        with pytest.raises(ValueError, match="Unknown operation"):
            await client.execute("nope")


# ── lifecycle: connect / disconnect / health_check ───────────────────────────


class TestLifecycle:
    async def test_connect_success(self):
        client = _client(data=[])
        client._openapi.get_valid_token = _async_token
        assert await client.connect() is True

    async def test_connect_failure_returns_false(self):
        client = _client(data=[])

        async def _boom():
            raise RuntimeError("no auth")

        client._openapi.get_valid_token = _boom
        assert await client.connect() is False

    async def test_disconnect_clears_openapi_tokens(self):
        client = _client(data=[])
        client._openapi._access_token = "T"
        client._openapi._refresh_token = "R"
        client._openapi._token_expires_at = datetime(2030, 1, 1)
        await client.disconnect()
        assert client._openapi._access_token is None
        assert client._openapi._refresh_token is None
        assert client._openapi._token_expires_at is None

    async def test_health_check_true(self):
        client = _client(data=[])
        assert await client.health_check() is True
        # health_check calls get_stores(limit=1)
        assert client._openapi.last_call["route"] == "/erp/sc/data/seller/lists"
        assert client._openapi.last_call["params"]["limit"] == 1

    async def test_health_check_false_on_error(self):
        client = _client(data=[], code=500)
        client._openapi._default_response = MockResponseResult(code=500, message="err")
        assert await client.health_check() is False


# small async helper used as get_valid_token stand-in (auto asyncio mode needs a coroutine fn)
async def _async_token():
    return "tok"


# ── misc accessors ───────────────────────────────────────────────────────────


class TestAccessors:
    def test_openapi_property_returns_underlying(self):
        client = _client(data=[])
        assert client.openapi is client._openapi

    def test_set_default_sids_rebuilds_param_builder(self):
        client = _client(data=[])
        old = client._param_builder
        client.set_default_sids([111, 222])
        assert client._param_builder is not old
        assert client._param_builder.default_sids == [111, 222]

    async def test_call_api_propagates_kwargs_method_get(self):
        client = _client(data={"x": 1})
        resp = await client.call_api(api_path="/g", method="get", params={"a": 1})
        assert resp.is_success is True
        assert client._openapi.last_call["method"] == "GET"

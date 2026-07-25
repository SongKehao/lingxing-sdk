"""Smoke tests for Phase 4 batch A: migrated typed params build the correct request body.

Each migrated method constructs its body via ``{k: v for ... if v is not None}``, so
None params are dropped and the surviving keys + values must match exactly. These
tests capture ``MockOpenApi._calls[0]["body"]`` and assert on the concrete keyset
and values (no hollow ``is not None`` checks) across fba / warehouse / sale.
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from conftest import MockOpenApi, MockResponseResult

from lingxing.endpoints.fba import FBAEndpoints
from lingxing.endpoints.sale import SaleEndpoints
from lingxing.endpoints.warehouse import WarehouseEndpoints


class TestEndpointBodyConstruction:
    """Verify request-body keyset + values for migrated Any -> typed params."""

    def setup_method(self):
        self.api = MockOpenApi(response=MockResponseResult(code=0, data=[]))

    @pytest.mark.asyncio
    async def test_fba_send_goods_list_param_keyset_and_values(self):
        fba = FBAEndpoints(self.api)
        await fba.send_goods(shipment_nos=["SHP-1", "SHP-2"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"shipment_nos"}
        assert body["shipment_nos"] == ["SHP-1", "SHP-2"]

    @pytest.mark.asyncio
    async def test_fba_shipment_lock_stock_drops_none_param(self):
        """Omitted (None) params must be filtered out of the body."""
        fba = FBAEndpoints(self.api)
        await fba.shipment_lock_stock(shipment_nos=["A"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"shipment_nos"}
        assert "is_auto_batch" not in body

    @pytest.mark.asyncio
    async def test_warehouse_get_process_order_lists_scalar_keyset(self):
        """9 migrated scalar params: only the 3 non-None survive, rest dropped."""
        wh = WarehouseEndpoints(self.api)
        await wh.get_process_order_lists(type=1, offset=0, length=500)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"type", "offset", "length"}
        assert body["type"] == 1
        assert body["offset"] == 0
        assert body["length"] == 500

    @pytest.mark.asyncio
    async def test_warehouse_delete_fba_shipment_list_array_body(self):
        wh = WarehouseEndpoints(self.api)
        await wh.delete_fba_shipment_list(shipment_nos=["X1", "X2"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"shipment_nos"}
        assert body["shipment_nos"] == ["X1", "X2"]

    @pytest.mark.asyncio
    async def test_sale_query_product_list_keyset_and_values(self):
        sale = SaleEndpoints(self.api)
        await sale.query_product_list(store_id=10, skus=["SKU-A", "SKU-B"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"store_id", "skus"}
        assert body["store_id"] == 10
        assert body["skus"] == ["SKU-A", "SKU-B"]

    @pytest.mark.asyncio
    async def test_sale_global_tag_remove_tag_array_body(self):
        sale = SaleEndpoints(self.api)
        await sale.global_tag_remove_tag(tag_ids=[1, 2, 3])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"tag_ids"}
        assert body["tag_ids"] == [1, 2, 3]

    @pytest.mark.asyncio
    async def test_sale_product_publish_includes_data_payload(self):
        sale = SaleEndpoints(self.api)
        payload = {"sku": "X", "title": "T"}
        await sale.product_publish(store_id=7, data=payload)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"store_id", "data"}
        assert body["store_id"] == 7
        assert body["data"] is payload

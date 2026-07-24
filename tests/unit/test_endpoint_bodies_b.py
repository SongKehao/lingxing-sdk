"""Smoke tests for Phase 4 batch B: migrated typed params build the correct request body.

Each migrated method constructs its body via ``{k: v for ... if v is not None}``, so
None params are dropped and the surviving keys + values must match exactly. These
tests capture ``MockOpenApi._calls[0]["body"]`` and assert on the concrete keyset
and values (no hollow ``is not None`` checks) across purchase / multiplatform_ads /
multiplatform_platforms.

Type coverage:
- array params  -> list[str] / list[int]
- opaque object -> dict[str, Any] (product_list / options / custom / return_address /
  comparison / config, all undocumented passthrough)
- TypedDict     -> ReportPageReq / ReportPeriodReq / ReportFilterReq (multiplatform_ads)
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from conftest import MockOpenApi, MockResponseResult

from lingxing.endpoints.multiplatform_ads import MultiplatformAdsEndpoints
from lingxing.endpoints.multiplatform_platforms import MultiplatformPlatformsEndpoints
from lingxing.endpoints.purchase import PurchaseEndpoints


class TestEndpointBodyConstructionBatchB:
    """Verify request-body keyset + values for migrated Any -> typed params."""

    def setup_method(self):
        self.api = MockOpenApi(response=MockResponseResult(code=0, data=[]))

    # ── purchase: array params (list[str]) ────────────────────────────────

    @pytest.mark.asyncio
    async def test_purchase_cancel_return_order_array_param(self):
        pur = PurchaseEndpoints(self.api)
        await pur.cancel_purchase_return_order(order_sn=["RT-1", "RT-2"], cancel_reason="wrong item")
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"order_sn", "cancel_reason"}
        assert body["order_sn"] == ["RT-1", "RT-2"]
        assert body["cancel_reason"] == "wrong item"

    @pytest.mark.asyncio
    async def test_purchase_set_orders_array_only_key(self):
        pur = PurchaseEndpoints(self.api)
        await pur.set_orders(order_sn=["SO-1", "SO-2"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"order_sn"}
        assert body["order_sn"] == ["SO-1", "SO-2"]

    @pytest.mark.asyncio
    async def test_purchase_set_order_finish_camel_case_key(self):
        pur = PurchaseEndpoints(self.api)
        await pur.set_order_finish(orderSn=["SN-1"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"orderSn"}
        assert body["orderSn"] == ["SN-1"]

    @pytest.mark.asyncio
    async def test_purchase_plan_cancel_array_plus_reason(self):
        pur = PurchaseEndpoints(self.api)
        await pur.purchase_plan_cancel(plan_sn=["PL-1"], reason="dup")
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"plan_sn", "reason"}
        assert body["plan_sn"] == ["PL-1"]

    @pytest.mark.asyncio
    async def test_purchase_order_modify_remark_drops_none(self):
        pur = PurchaseEndpoints(self.api)
        await pur.order_modify_remark(order_sns=["O-1"], value="note")
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"order_sns", "value"}

    # ── purchase: opaque object params (dict[str, Any]) ───────────────────

    @pytest.mark.asyncio
    async def test_purchase_create_order_keeps_only_passed_keys(self):
        """25 params: only the 4 passed survive, the other 21 (None) are dropped."""
        pur = PurchaseEndpoints(self.api)
        products = [{"pid": 1, "qty": 2}]
        opts = {"auto_review": True}
        await pur.create_purchase_order(opt_uid=5, purchaser_id=9, product_list=products, options=opts)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"opt_uid", "purchaser_id", "product_list", "options"}
        assert body["product_list"] is products
        assert body["options"] is opts
        assert body["opt_uid"] == 5

    # ── multiplatform_ads: TypedDict params + None-drop ───────────────────

    @pytest.mark.asyncio
    async def test_ads_lazada_report_keeps_typeddicts_drops_none(self):
        """page/period/filter (TypedDict) survive; comparison/config (None) dropped."""
        ads = MultiplatformAdsEndpoints(self.api)
        page = {"page": 1, "length": 20}
        period = {"startDate": "2026-01-01", "endDate": "2026-01-31"}
        flt = {"shopIds": [101, 102]}
        await ads.lazada_audience_report_list(page=page, period=period, filter=flt)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"page", "period", "filter"}
        assert body["page"] is page
        assert body["period"] is period
        assert body["filter"] is flt

    @pytest.mark.asyncio
    async def test_ads_shopee_report_drops_optional_filter(self):
        ads = MultiplatformAdsEndpoints(self.api)
        await ads.shopee_campaign_report_list(page={"page": 2}, period={"startDate": "s", "endDate": "e"})
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"page", "period"}
        assert body["page"] == {"page": 2}

    # ── multiplatform_platforms: array + opaque params ────────────────────

    @pytest.mark.asyncio
    async def test_platforms_batch_temu_decrypt_array_key(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        await mp.batch_temu_address_decrypt(decryptSnList=["TS-1", "TS-2"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"decryptSnList"}
        assert body["decryptSnList"] == ["TS-1", "TS-2"]

    @pytest.mark.asyncio
    async def test_platforms_fbt_stock_search_int_array(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        await mp.fbt_stock_search(length=20, offset=0, storeIdList=[101, 102])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"length", "offset", "storeIdList"}
        assert body["storeIdList"] == [101, 102]

    @pytest.mark.asyncio
    async def test_platforms_query_shipping_list_v2_int_array(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        await mp.query_shipping_list_v2(platformCodes=[10008, 10011], length=10)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"platformCodes", "length"}
        assert body["platformCodes"] == [10008, 10011]

    @pytest.mark.asyncio
    async def test_platforms_temu_cargo_status_int_array(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        await mp.temu_cargo(statusList=[0, 1], startTime="2026-01-01", endTime="2026-01-31", timeType=1)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"statusList", "startTime", "endTime", "timeType"}
        assert body["statusList"] == [0, 1]

    @pytest.mark.asyncio
    async def test_platforms_full_list_opaque_custom_object(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        custom = {"brand": "Nike"}
        await mp.full_list(custom=custom, length=10, offset=0)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"custom", "length", "offset"}
        assert body["custom"] is custom

    @pytest.mark.asyncio
    async def test_platforms_cargo_storage_opaque_return_address(self):
        mp = MultiplatformPlatformsEndpoints(self.api)
        addr = {"name": "Alice", "phone": "123"}
        await mp.multiplatform_cargo_storage(store_id="s1", return_address=addr)
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"store_id", "return_address"}
        assert body["return_address"] is addr

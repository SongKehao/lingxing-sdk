"""Smoke tests for Phase 4 batch C: migrated Any -> typed params build the correct body.

Covers vc / product / statistics / multiplatform_other / logistics /
customer_service / new_ad / finance (18 methods). Each migrated method builds its
body via ``{k: v for ... if v is not None}``; None params are dropped and the
surviving keys + values must match exactly. Tests capture
``MockOpenApi._calls[i]["body"]`` and assert on the concrete keyset and values
(no hollow ``is not None`` checks).

Type coverage of the migrated params:
- array  -> list  (ids / global_order_no / commodity_codes / custom_fields /
  sku_lis / sids / marketplace_ids / sku / sid(rma) / searchValue(rma) /
  countryCodes / sids(finance))
- object -> dict  (search(logistics) / data(category) / qc_standard /
  product_logistics_list / declaration / clearance / purchase_info / logistics /
  extend_search)
- union  -> str | list (sid in product_performance)
- scalar -> int/str (offset / length / dateType / currencyCode / seller_id /
  financial_event_group_id / ...)
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from conftest import MockOpenApi, MockResponseResult

from lingxing.endpoints.customer_service import CustomerServiceEndpoints
from lingxing.endpoints.finance import FinanceEndpoints
from lingxing.endpoints.logistics import LogisticsEndpoints
from lingxing.endpoints.multiplatform_other import MultiplatformOtherEndpoints
from lingxing.endpoints.new_ad import NewAdEndpoints
from lingxing.endpoints.product import ProductEndpoints
from lingxing.endpoints.statistics import StatisticsEndpoints
from lingxing.endpoints.vc import VCEndpoints


class TestEndpointBodyConstructionBatchC:
    """Verify request-body keyset + values for migrated Any -> typed params."""

    def setup_method(self):
        self.api = MockOpenApi(response=MockResponseResult(code=0, data=[]))

    # ── vc: ids (list), purchase_order_type (list) ────────────────────────

    @pytest.mark.asyncio
    async def test_vc_df_confirm_shipment_ids_array(self):
        vc = VCEndpoints(self.api)
        await vc.vc_order_df_confirm_shipment(ids=[101, 102])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"ids"}
        assert body["ids"] == [101, 102]

    @pytest.mark.asyncio
    async def test_vc_df_get_shipping_label_ids_array(self):
        vc = VCEndpoints(self.api)
        await vc.vc_order_df_get_shipping_label(ids=[201])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"ids"}
        assert body["ids"] == [201]

    @pytest.mark.asyncio
    async def test_vc_df_submit_shipping_label_ids_array(self):
        vc = VCEndpoints(self.api)
        await vc.vc_order_df_submit_shipping_label(ids=[301, 302])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"ids"}
        assert body["ids"] == [301, 302]

    @pytest.mark.asyncio
    async def test_vc_order_page_list_purchase_order_type_array(self):
        vc = VCEndpoints(self.api)
        await vc.vc_order_page_list(
            purchase_order_type=[0, 1],
            offset=0,
            length=20,
            vc_store_ids=["s1"],
            search_field_time="1",
            start_date="2026-01-01",
            end_date="2026-01-31",
            search_field="asin",
            search_value=["A1"],
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "purchase_order_type",
            "offset",
            "length",
            "vc_store_ids",
            "search_field_time",
            "start_date",
            "end_date",
            "search_field",
            "search_value",
        }
        assert body["purchase_order_type"] == [0, 1]

    # ── product: commodity_codes(list) / data(dict) / objects / list ──────

    @pytest.mark.asyncio
    async def test_product_add_commodity_code_array(self):
        prod = ProductEndpoints(self.api)
        await prod.add_commodity_code(commodity_codes=["UPC1", "UPC2"], code_type="UPC")
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"commodity_codes", "code_type"}
        assert body["commodity_codes"] == ["UPC1", "UPC2"]

    @pytest.mark.asyncio
    async def test_product_category_data_dict(self):
        prod = ProductEndpoints(self.api)
        await prod.category(offset=0, length=100, data={"parent_id": 5})
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"offset", "length", "data"}
        assert body["data"] == {"parent_id": 5}

    @pytest.mark.asyncio
    async def test_product_set_object_and_array_params(self):
        prod = ProductEndpoints(self.api)
        await prod.set_product(
            sku="SKU-1",
            product_name="name",
            qc_standard={"mode": "qc"},
            product_logistics_list={"country": "US"},
            declaration={"decl": 1},
            clearance={"clear": 2},
            custom_fields=["f1", "f2"],
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "sku",
            "product_name",
            "qc_standard",
            "product_logistics_list",
            "declaration",
            "clearance",
            "custom_fields",
        }
        assert body["qc_standard"] == {"mode": "qc"}
        assert body["custom_fields"] == ["f1", "f2"]

    @pytest.mark.asyncio
    async def test_product_spu_set_object_and_array_params(self):
        prod = ProductEndpoints(self.api)
        await prod.spu_set(
            spu="SPU-1",
            spu_name="spu name",
            sku_list=[{"sku": "v1"}],
            sku_lis=["extra"],
            purchase_info={"buyer": "u1"},
            logistics={"logistics": "x"},
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "spu",
            "spu_name",
            "sku_list",
            "sku_lis",
            "purchase_info",
            "logistics",
        }
        assert body["sku_lis"] == ["extra"]
        assert body["purchase_info"] == {"buyer": "u1"}

    # ── statistics: sids(list) / marketplace_ids(list) / sid(union) / extend_search(dict)

    @pytest.mark.asyncio
    async def test_statistics_operate_log_list_sids_array(self):
        st = StatisticsEndpoints(self.api)
        await st.operate_log_list(
            sids=[4661, 109],
            search_field="asin",
            search_value="B001",
            date_type="1",
            start_date="2026-01-01",
            end_date="2026-01-31",
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "sids",
            "search_field",
            "search_value",
            "date_type",
            "start_date",
            "end_date",
        }
        assert body["sids"] == [4661, 109]

    @pytest.mark.asyncio
    async def test_statistics_report_create_marketplace_ids_array(self):
        st = StatisticsEndpoints(self.api)
        await st.report_create_report_export_task(
            seller_id="amzn1",
            report_type="GET_FLAT_FILE",
            marketplace_ids=["ATVPDKIKX0", "A2EUQ1WTGCTBG2"],
            region="na",
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"seller_id", "report_type", "marketplace_ids", "region"}
        assert body["marketplace_ids"] == ["ATVPDKIKX0", "A2EUQ1WTGCTBG2"]

    @pytest.mark.asyncio
    async def test_statistics_product_performance_sid_union_and_extend_search_dict(self):
        st = StatisticsEndpoints(self.api)
        await st.product_performance(
            offset=0,
            length=100,
            sort_field="volume",
            sort_type="desc",
            sid=["4661", "109"],
            start_date="2026-01-01",
            end_date="2026-01-31",
            summary_field="asin",
            extend_search={"category": "toy"},
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "offset",
            "length",
            "sort_field",
            "sort_type",
            "sid",
            "start_date",
            "end_date",
            "summary_field",
            "extend_search",
        }
        assert body["sid"] == ["4661", "109"]
        assert body["extend_search"] == {"category": "toy"}

    # ── multiplatform_other: global_order_no (list) ────────────────────────

    @pytest.mark.asyncio
    async def test_multiplatform_batch_review_global_order_no_array(self):
        mp = MultiplatformOtherEndpoints(self.api)
        await mp.batch_review(global_order_no=["G1", "G2"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"global_order_no"}
        assert body["global_order_no"] == ["G1", "G2"]

    @pytest.mark.asyncio
    async def test_multiplatform_pre_shipment_global_order_no_array(self):
        mp = MultiplatformOtherEndpoints(self.api)
        await mp.pre_shipment(global_order_no=["G3"])
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"global_order_no"}
        assert body["global_order_no"] == ["G3"]

    # ── logistics: search (dict) ──────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_logistics_query_head_provider_search_dict(self):
        lg = LogisticsEndpoints(self.api)
        await lg.query_head_logistics_provider(search={"keyword": "dhl"})
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"search"}
        assert body["search"] == {"keyword": "dhl"}

    # ── customer_service: sid(list) + searchValue(list) ───────────────────

    @pytest.mark.asyncio
    async def test_customer_service_rma_manage_sid_and_search_value_arrays(self):
        cs = CustomerServiceEndpoints(self.api)
        await cs.customer_service_rma_manage_list(
            sid=[4661],
            searchValue=["B001", "B002"],
            searchField="asin",
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"sid", "searchValue", "searchField"}
        assert body["sid"] == [4661]
        assert body["searchValue"] == ["B001", "B002"]

    # ── new_ad: sku (list) ────────────────────────────────────────────────

    @pytest.mark.asyncio
    async def test_new_ad_product_analysis_list_sku_array(self):
        ad = NewAdEndpoints(self.api)
        await ad.product_analysis_list(
            profile_id=123,
            sid="4661",
            sku=["MSKU1", "MSKU2"],
            start_date="2026-01-01",
            end_date="2026-01-31",
            group_type="hourly",
            sponsored_type=["sp", "sd"],
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "profile_id",
            "sid",
            "sku",
            "start_date",
            "end_date",
            "group_type",
            "sponsored_type",
        }
        assert body["sku"] == ["MSKU1", "MSKU2"]

    # ── finance: settlement_summary_list (10 typed) / settlement_export_url_get (2)

    @pytest.mark.asyncio
    async def test_finance_settlement_summary_list_full_keyset(self):
        fin = FinanceEndpoints(self.api)
        await fin.settlement_summary_list(
            offset=0,
            length=50,
            countryCodes=["US", "CA"],
            sids=[4661],
            currencyCode="USD",
            dateType=0,
            startDate="2026-01-01",
            endDate="2026-01-31",
            searchField="id",
            searchValue="STT-1",
        )
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {
            "offset",
            "length",
            "countryCodes",
            "sids",
            "currencyCode",
            "dateType",
            "startDate",
            "endDate",
            "searchField",
            "searchValue",
        }
        assert body["countryCodes"] == ["US", "CA"]
        assert body["dateType"] == 0

    @pytest.mark.asyncio
    async def test_finance_settlement_export_url_get_string_params(self):
        fin = FinanceEndpoints(self.api)
        await fin.settlement_export_url_get(seller_id="amzn1", financial_event_group_id="grp-1")
        body = self.api._calls[0]["body"]
        assert set(body.keys()) == {"seller_id", "financial_event_group_id"}
        assert body["seller_id"] == "amzn1"
        assert body["financial_event_group_id"] == "grp-1"

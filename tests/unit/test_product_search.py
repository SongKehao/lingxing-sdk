"""Tests for AmazonProductSearchResponse typed parsing + listing/publish helpers.

Covers:
- Full info structure parsing (summaries/attributes/issues/offers/...)
- Convenience properties (title/bullets/description/search_terms/...)
- _check_response tolerates code=1 for /listing/publish/openapi/ routes
- query_product_list parses code=1 response
- query_product_list_all auto-batches by 20 SKUs
"""
import asyncio

import pytest

from lingxing.endpoints.sale import SaleEndpoints
from lingxing.errors import ApiError
from lingxing.models.responses.sale import AmazonProductSearchResponse

# ---- 文档示例数据（/listing/publish/openapi/amazon/product/search 返回结构）----
SAMPLE_ITEM = {
    "msku": "0Z-WQSX-RMWR",
    "info": {
        "summaries": [{
            "asin": "B0XXX",
            "conditionType": "new_new",
            "createdDate": "2023-07-27T02:53:03.969Z",
            "fnSku": "FNSKU1",
            "itemName": "NP Phone Holder",
            "lastUpdatedDate": "2023-11-23T11:30:22.391Z",
            "mainImage": {"height": 500, "width": 500, "link": "https://img/main.jpg"},
            "marketplaceId": "ATVPDKIKX0DA",
            "productType": "PORTABLE_ELECTRONIC_DEVICE_STAND",
            "status": ["BUYABLE", "DISCOVERABLE"],
        }],
        "attributes": {
            "item_name": [{"language_tag": "en_US", "marketplace_id": "ATVPDKIKX0DA",
                           "value": "Women's Red Plaid A-Line Mini Skirt"}],
            "bullet_point": [
                {"language_tag": "en_US", "marketplace_id": "ATVPDKIKX0DA", "value": "bullet one"},
                {"language_tag": "en_US", "marketplace_id": "ATVPDKIKX0DA", "value": "bullet two"},
            ],
            "product_description": [{"language_tag": "en_US", "marketplace_id": "ATVPDKIKX0DA",
                                     "value": "<p>long desc</p>"}],
            "generic_keyword": [{"language_tag": "en_US", "marketplace_id": "ATVPDKIKX0DA",
                                 "value": "search terms here"}],
            "condition_type": [{"marketplace_id": "ATVPDKIKX0DA", "value": "new_new"}],
            "item_dimensions": [{"height": {"unit": "centimeters", "value": 5},
                                 "length": {"unit": "centimeters", "value": 10},
                                 "width": {"unit": "centimeters", "value": 8},
                                 "marketplace_id": "ATVPDKIKX0DA"}],
            "item_weight": [{"marketplace_id": "ATVPDKIKX0DA", "unit": "kilograms", "value": 0.17}],
            "list_price": [{"currency": "USD", "marketplace_id": "ATVPDKIKX0DA", "value": 103}],
            "main_product_image_locator": [{"marketplace_id": "ATVPDKIKX0DA",
                                            "media_location": "https://img/main.jpg"}],
            "fulfillment_availability": [{"fulfillment_channel_code": "DEFAULT",
                                          "lead_time_to_ship_max_days": 12, "quantity": 333}],
            "purchasable_offer": [
                {"audience": "ALL", "currency": "USD", "marketplace_id": "ATVPDKIKX0DA",
                 "our_price": [{"schedule": [{"value_with_tax": 15.08}]}],
                 "start_at": {"value": "2023-07-27T02:51:53.956Z"}, "end_at": {"value": None}},
                {"audience": "B2B", "currency": "USD", "marketplace_id": "ATVPDKIKX0DA",
                 "our_price": [{"schedule": [{"value_with_tax": 68}]}]},
            ],
        },
        "issues": [{"attributeNames": ["form_factor"], "categories": ["MISSING_ATTRIBUTE"],
                    "code": "18448", "message": "missing", "severity": "WARNING"}],
        "offers": [{"audience": {"displayName": "Sell on Amazon", "value": "ALL"},
                    "marketplaceId": "ATVPDKIKX0DA", "offerType": "B2C",
                    "price": {"amount": "15.08", "currency": "USD", "currencyCode": "USD"}}],
        "fulfillmentAvailability": [{"fulfillmentChannelCode": "DEFAULT", "quantity": 333}],
        "productTypes": [{"marketplaceId": "ATVPDKIKX0DA", "productType": "PORTABLE_ELECTRONIC_DEVICE_STAND"}],
        "procurement": [],
        "relationships": [],
    },
}


class _Resp:
    """Minimal ResponseResult stand-in."""

    def __init__(self, code, data):
        self.code = code
        self.data = data
        self.message = "success"
        self.total = 0
        self.request_id = "rid"


class _FakeOpenApi:
    """Minimal OpenApiBase mock capturing calls."""

    def __init__(self, default=None):
        self._default = default
        self.calls = []

    async def request_with_auto_token(self, route_name, method, req_body=None, req_params=None, **kw):
        self.calls.append({"route": route_name, "body": req_body})
        return self._default


# ---- 模型解析 ----

def test_parse_full_info():
    item = AmazonProductSearchResponse(**SAMPLE_ITEM)
    assert item.msku == "0Z-WQSX-RMWR"
    # 便捷属性
    assert item.title == "Women's Red Plaid A-Line Mini Skirt"
    assert item.bullets == ["bullet one", "bullet two"]
    assert item.description == "<p>long desc</p>"
    assert item.search_terms == "search terms here"
    assert item.asin == "B0XXX"
    assert item.main_image == "https://img/main.jpg"
    assert item.product_type == "PORTABLE_ELECTRONIC_DEVICE_STAND"
    # 完整嵌套结构
    info = item.info
    assert info.attributes.item_dimensions[0].length.value == 10
    assert info.attributes.item_weight[0].value == 0.17
    assert info.attributes.list_price[0].currency == "USD"
    assert info.attributes.fulfillment_availability[0].quantity == 333
    assert info.attributes.purchasable_offer[0].our_price[0].schedule[0].value_with_tax == 15.08
    assert info.attributes.purchasable_offer[1].audience == "B2B"
    assert info.issues[0].severity == "WARNING"
    assert info.issues[0].attribute_names == ["form_factor"]
    assert info.offers[0].price.amount == "15.08"
    assert info.fulfillment_availability[0].fulfillment_channel_code == "DEFAULT"
    assert info.product_types[0].product_type == "PORTABLE_ELECTRONIC_DEVICE_STAND"
    # summaries 的 camelCase 字段也能正确解析（alias 机制）
    assert info.summaries[0].condition_type == "new_new"
    assert info.summaries[0].fn_sku == "FNSKU1"
    assert info.summaries[0].main_image.width == 500


def test_convenience_properties_safe_when_missing():
    item = AmazonProductSearchResponse(msku="x")  # 无 info
    assert item.title is None
    assert item.bullets == []
    assert item.description is None
    assert item.search_terms is None
    assert item.asin is None
    assert item.main_image is None


def test_extra_attributes_allowed():
    """Amazon 新增字段不应导致解析失败（extra='allow'）."""
    data = {"msku": "x", "info": {"attributes": {"some_future_field": [{"value": "z"}]}}}
    item = AmazonProductSearchResponse(**data)
    assert item.msku == "x"


def test_title_falls_back_to_summaries():
    """无 attributes.item_name 时回退 summaries.item_name."""
    data = {"msku": "x", "info": {"summaries": [{"itemName": "From Summary", "asin": "A1"}]}}
    item = AmazonProductSearchResponse(**data)
    assert item.title == "From Summary"
    assert item.asin == "A1"


# ---- _check_response code=1 容忍 ----

def test_check_response_accepts_code1_for_listing_publish():
    sale = SaleEndpoints(_FakeOpenApi())
    sale._check_response(_Resp(1, []), "/listing/publish/openapi/amazon/product/search")  # 不抛即通过


def test_check_response_rejects_code1_for_other_routes():
    sale = SaleEndpoints(_FakeOpenApi())
    with pytest.raises(ApiError):
        sale._check_response(_Resp(1, []), "/erp/sc/data/mws/listing")


def test_check_response_rejects_nonzero_for_listing_publish():
    sale = SaleEndpoints(_FakeOpenApi())
    with pytest.raises(ApiError):
        sale._check_response(_Resp(2, []), "/listing/publish/openapi/amazon/product/search")


# ---- query_product_list / query_product_list_all ----

def test_query_product_list_parses_code1_response():
    api = _FakeOpenApi(default=_Resp(1, [SAMPLE_ITEM]))
    sale = SaleEndpoints(api)
    res = asyncio.run(sale.query_product_list(store_id=34, skus=["0Z-WQSX-RMWR"]))
    assert len(res) == 1
    assert isinstance(res[0], AmazonProductSearchResponse)
    assert res[0].title == "Women's Red Plaid A-Line Mini Skirt"
    assert res[0].bullets == ["bullet one", "bullet two"]


def test_query_product_list_all_batches_by_20():
    captured = []

    async def fake(route_name, method, req_body=None, req_params=None, **kw):
        captured.append(req_body["skus"])
        return _Resp(1, [])

    api = _FakeOpenApi()
    api.request_with_auto_token = fake  # 注入捕获逻辑
    sale = SaleEndpoints(api)
    skus = [f"sku-{i}" for i in range(45)]
    asyncio.run(sale.query_product_list_all(store_id=34, skus=skus))
    assert len(captured) == 3
    assert len(captured[0]) == 20
    assert len(captured[1]) == 20
    assert len(captured[2]) == 5


def test_query_product_list_all_merges_results():
    api = _FakeOpenApi(default=_Resp(1, [SAMPLE_ITEM]))
    sale = SaleEndpoints(api)
    res = asyncio.run(sale.query_product_list_all(store_id=34, skus=["a"] * 45))
    # 每片返回 1 条，3 片共 3 条
    assert len(res) == 3
    assert all(isinstance(r, AmazonProductSearchResponse) for r in res)


def test_query_product_list_all_sync_wrapper_exists():
    """SyncWrapperMeta 应自动生成 _sync 版本."""
    assert hasattr(SaleEndpoints, "query_product_list_all_sync")

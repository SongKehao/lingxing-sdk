"""Unit tests for endpoint request construction and response parsing."""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lingxing.endpoints._base import BaseEndpoint
from lingxing.endpoints.basic import BasicEndpoints
from lingxing.models.basic import SellerListsItem, AccoutListsItem, AllMarketplaceItem

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from conftest import MockOpenApi, MockResponseResult


# ── BasicEndpoints ──

class TestBasicEndpoints:
    """Tests for basic data API endpoints."""

    def setup_method(self):
        self.api = MockOpenApi(response=MockResponseResult(code=0, data=[]))
        self.basic = BasicEndpoints(self.api)

    @pytest.mark.asyncio
    async def test_list_sellers(self):
        """Should parse seller list response correctly."""
        self.api._default_response = MockResponseResult(
            code=0,
            data=[
                {"sid": 102, "name": "凌羽迪", "country": "US", "status": 1},
                {"sid": 103, "name": "Test Shop", "country": "UK", "status": 1},
            ],
        )
        sellers = await self.basic.list_sellers()
        assert len(sellers) == 2
        assert isinstance(sellers[0], SellerListsItem)
        assert sellers[0].sid == 102
        assert sellers[0].name == "凌羽迪"

    @pytest.mark.asyncio
    async def test_list_accounts(self):
        """Should parse account list response correctly."""
        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"uid": 1, "account": "admin", "realname": "Admin User"}],
        )
        accounts = await self.basic.list_accounts()
        assert len(accounts) == 1
        assert accounts[0].uid == 1
        assert accounts[0].account == "admin"

    @pytest.mark.asyncio
    async def test_list_marketplaces(self):
        """Should parse marketplace list response."""
        self.api._default_response = MockResponseResult(
            code=0,
            data=[{"code": "US", "country": "United States", "marketplace_id": "ATVPDKIKX0DER"}],
        )
        markets = await self.basic.list_marketplaces()
        assert len(markets) == 1
        assert markets[0].code == "US"

    @pytest.mark.asyncio
    async def test_list_sellers_sends_correct_route(self):
        """Should call the correct API route."""
        sellers = await self.basic.list_sellers()
        assert self.api.call_count == 1
        assert self.api.last_call['route'] == '/erp/sc/data/seller/lists'
        assert self.api.last_call['method'] == 'POST'

    @pytest.mark.asyncio
    async def test_empty_response(self):
        """Should handle empty data gracefully."""
        self.api._default_response = MockResponseResult(code=0, data=None)
        sellers = await self.basic.list_sellers()
        assert sellers == []

    @pytest.mark.asyncio
    async def test_error_response_raises(self):
        """Should raise ApiError for non-zero response code."""
        from lingxing.errors import ApiError
        self.api._default_response = MockResponseResult(code=400, message="参数有误")
        with pytest.raises(ApiError) as exc_info:
            await self.basic.list_sellers()
        assert exc_info.value.code == 400


class TestBaseEndpoint:
    """Tests for BaseEndpoint._parse_list helper."""

    def setup_method(self):
        self.api = MockOpenApi()
        self.endpoint = BaseEndpoint(self.api)

    def test_parse_list_from_list(self):
        """Should parse list of dicts."""
        data = [{"sid": 1, "name": "A"}, {"sid": 2, "name": "B"}]
        result = self.endpoint._parse_list(data, SellerListsItem)
        assert len(result) == 2
        assert result[0].sid == 1

    def test_parse_list_from_dict_with_list_key(self):
        """Should parse dict with 'list' key."""
        data = {"list": [{"sid": 1}], "total": 1}
        result = self.endpoint._parse_list(data, SellerListsItem)
        assert len(result) == 1

    def test_parse_list_from_dict_with_data_key(self):
        """Should parse dict with 'data' key."""
        data = {"data": [{"sid": 1}], "total": 1}
        result = self.endpoint._parse_list(data, SellerListsItem)
        assert len(result) == 1

    def test_parse_list_none(self):
        """Should handle None data."""
        result = self.endpoint._parse_list(None, SellerListsItem)
        assert result == []

    def test_parse_page(self):
        """Should parse paginated data."""
        data = {"list": [{"sid": 1}], "total": 100}
        items, total = self.endpoint._parse_page(data, SellerListsItem)
        assert len(items) == 1
        assert total == 100


class TestModels:
    """Tests for Pydantic model parsing."""

    def test_seller_lists_item_all_fields(self):
        item = SellerListsItem(sid=102, name="凌羽迪", country="US", status=1)
        assert item.sid == 102
        assert item.name == "凌羽迪"

    def test_seller_lists_item_partial(self):
        """Should allow partial data (all fields Optional)."""
        item = SellerListsItem(sid=102)
        assert item.sid == 102
        assert item.name is None

    def test_extra_fields_allowed(self):
        """Should accept unknown fields from API."""
        item = SellerListsItem(sid=102, unknown_field="hello")
        assert item.sid == 102

    def test_account_item(self):
        item = AccoutListsItem(uid=1, account="admin", realname="Admin")
        assert item.uid == 1
        assert item.realname == "Admin"


class TestRecordedFixtures:
    """Replay recorded API responses to verify parsing."""

    @pytest.fixture(autouse=True)
    def load_fixtures(self):
        fixtures_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'api_responses.json')
        if os.path.exists(fixtures_path):
            with open(fixtures_path) as f:
                self.fixtures = json.load(f)
        else:
            self.fixtures = {}

    @pytest.mark.asyncio
    async def test_seller_lists_from_fixture(self):
        """Should parse real seller lists response."""
        if 'BasicData/SellerLists' not in self.fixtures:
            pytest.skip("No fixture for SellerLists")

        fixture = self.fixtures['BasicData/SellerLists']
        data = fixture['response']['data']

        api = MockOpenApi(response=MockResponseResult(code=0, data=data))
        basic = BasicEndpoints(api)
        sellers = await basic.list_sellers()

        assert len(sellers) > 0
        assert all(isinstance(s, SellerListsItem) for s in sellers)
        # Verify at least one has a sid
        assert any(s.sid is not None for s in sellers)

    @pytest.mark.asyncio
    async def test_account_lists_from_fixture(self):
        """Should parse real account lists response."""
        if 'BasicData/AccoutLists' not in self.fixtures:
            pytest.skip("No fixture for AccoutLists")

        fixture = self.fixtures['BasicData/AccoutLists']
        data = fixture['response']['data']

        api = MockOpenApi(response=MockResponseResult(code=0, data=data))
        basic = BasicEndpoints(api)
        accounts = await basic.list_accounts()

        assert len(accounts) > 0
        assert all(isinstance(a, AccoutListsItem) for a in accounts)

    @pytest.mark.asyncio
    async def test_marketplace_from_fixture(self):
        """Should parse real marketplace response."""
        if 'BasicData/AllMarketplace' not in self.fixtures:
            pytest.skip("No fixture for AllMarketplace")

        fixture = self.fixtures['BasicData/AllMarketplace']
        data = fixture['response']['data']

        api = MockOpenApi(response=MockResponseResult(code=0, data=data))
        basic = BasicEndpoints(api)
        markets = await basic.list_marketplaces()

        assert len(markets) > 0
        assert all(isinstance(m, AllMarketplaceItem) for m in markets)

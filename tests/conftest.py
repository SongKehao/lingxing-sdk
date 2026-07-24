"""Shared test fixtures and mock helpers."""

import json
import os
import sys
from unittest.mock import AsyncMock, MagicMock

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class MockResponseResult:
    """Mock for ResponseResult."""

    def __init__(self, code=0, data=None, message="success", total=None, request_id=None):
        self.code = code
        self.data = data
        self.message = message
        self.total = total
        self.request_id = request_id


class MockOpenApi:
    """Mock for OpenApiBase that returns pre-configured responses."""

    def __init__(self, response=None, responses=None):
        """
        Args:
            response: Default response for any request
            responses: Dict mapping route_name -> response
        """
        self._default_response = response or MockResponseResult()
        self._responses = responses or {}
        self._calls = []  # track all calls for assertions

    async def request_with_auto_token(self, route_name, method, req_body=None, req_params=None, **kwargs):
        self._calls.append(
            {
                "route": route_name,
                "method": method,
                "body": req_body,
                "params": req_params,
            }
        )
        if route_name in self._responses:
            return self._responses[route_name]
        return self._default_response

    async def get_valid_token(self):
        return "mock_token"

    @property
    def last_call(self):
        return self._calls[-1] if self._calls else None

    @property
    def call_count(self):
        return len(self._calls)

    def calls_for_route(self, route):
        return [c for c in self._calls if c["route"] == route]


@pytest.fixture
def mock_api():
    """Create a mock API that returns success by default."""
    return MockOpenApi(response=MockResponseResult(code=0, data=[], message="success"))


@pytest.fixture
def fixtures_dir():
    """Path to recorded API fixtures."""
    return os.path.join(os.path.dirname(__file__), "fixtures")


@pytest.fixture
def api_fixtures(fixtures_dir):
    """Load recorded API fixtures."""
    path = os.path.join(fixtures_dir, "api_responses.json")
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        return json.load(f)

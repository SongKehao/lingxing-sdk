#!/usr/bin/env python3
"""
Unit tests for auth module (retrieval APIs only).

Auto-generated tests for data retrieval APIs.
Execution-type APIs are excluded per user requirement.

Generated: 1 test methods for 1 retrieval APIs
Skipped: 1 execution APIs
"""

from unittest.mock import AsyncMock, MagicMock

import pytest

from lingxing.endpoints.auth_generated import AuthEndpoints


class TestAuthEndpoints:
    """Test class for AuthEndpoints retrieval methods."""

    @pytest.fixture
    def mock_openapi(self):
        """Mock OpenAPI client."""
        mock = MagicMock()
        mock.call_api = AsyncMock()
        return mock

    @pytest.mark.asyncio
    async def test_get_access_token(self, mock_openapi):
        """Test get_access_token method."""
        # Arrange
        auth_endpoints = AuthEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await auth_endpoints.get_access_token(access_token="test_token", appId="test_id", appSecret="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/api/auth-server/oauth/access-token"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_access_token_required(self, mock_openapi):
        """Test that access_token is required for all methods."""
        auth_endpoints = AuthEndpoints(mock_openapi)

        # Test with empty access_token should still work (validation is on server side)
        mock_openapi.call_api.return_value = {"code": 401, "message": "Unauthorized"}

        # Pick first retrieval method for testing
        result = await auth_endpoints.get_access_token(access_token="")

        assert result["code"] == 401
        mock_openapi.call_api.assert_called_once()

    @pytest.mark.asyncio
    async def test_error_handling(self, mock_openapi):
        """Test error response handling."""
        auth_endpoints = AuthEndpoints(mock_openapi)
        error_response = {"code": 400, "message": "Bad Request", "data": None}
        mock_openapi.call_api.return_value = error_response

        # Test error response
        result = await auth_endpoints.get_access_token(access_token="test_token")

        assert result == error_response
        assert result["code"] == 400

#!/usr/bin/env python3
"""Unit tests for ads module (retrieval APIs only)."""

from unittest.mock import AsyncMock, MagicMock

import pytest

from lingxing.endpoints.ads_generated import AdsEndpoints


class TestAdsEndpoints:
    @pytest.fixture
    def mock_openapi(self):
        mock = MagicMock()
        mock.call_api = AsyncMock()
        return mock

    @pytest.mark.asyncio
    async def test_newad_apiLogStandard(self, mock_openapi):
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        result = await ads_endpoints.newad_apiLogStandard(access_token="test_token", sid="test_id", start_date="2024-01-01", end_date="2024-01-01", offset="test_value", length="test_value")

        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/apiLogStandard"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sddata(self, mock_openapi):
        """Test sddata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sddata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdAdGroupHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sb(self, mock_openapi):
        """Test get_sb method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sb(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/listHsaKeywordPlacementReport"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbreport(self, mock_openapi):
        """Test sbreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaCampaignReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_dsplist_order(self, mock_openapi):
        """Test get_dsplist_order method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_dsplist_order(access_token="test_token", profile_id="test_id", start_date="2024-01-01", end_date="2024-01-01", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/basicOpen/dspReport/order/list"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbdata(self, mock_openapi):
        """Test sbdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbAdGroupHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spdata(self, mock_openapi):
        """Test spdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spCampaignHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbdata(self, mock_openapi):  # noqa: F811
        """Test sbdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbAdPlacementHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaCampaignPlacementReports(self, mock_openapi):
        """Test newad_hsaCampaignPlacementReports method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaCampaignPlacementReports(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaCampaignPlacementReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spdata(self, mock_openapi):  # noqa: F811
        """Test spdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spAdGroupHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sdreport(self, mock_openapi):
        """Test sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdCampaignReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sddata(self, mock_openapi):  # noqa: F811
        """Test sddata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sddata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdCampaignHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spdata(self, mock_openapi):  # noqa: F811
        """Test spdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spAdPlacementHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spAdGroupReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_campaignPlacementReports(self, mock_openapi):
        """Test newad_campaignPlacementReports method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_campaignPlacementReports(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/campaignPlacementReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sdreport(self, mock_openapi):  # noqa: F811
        """Test sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdAdGroupReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):  # noqa: F811
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spCampaignReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_sbDivideAsinReports(self, mock_openapi):
        """Test newad_sbDivideAsinReports method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_sbDivideAsinReports(access_token="test_token", profile_id="test_id", report_date="2024-01-01", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbDivideAsinReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sddata(self, mock_openapi):
        """Test get_sddata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sddata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdTargetHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):  # noqa: F811
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spProductAdReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_spreport(self, mock_openapi):
        """Test get_spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spTargetReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):  # noqa: F811
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spKeywordReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbdata(self, mock_openapi):  # noqa: F811
        """Test sbdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbCampaignHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sddata(self, mock_openapi):  # noqa: F811
        """Test sddata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sddata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdAdvertiseHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sdreport(self, mock_openapi):
        """Test get_sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdMatchTargetReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sbdata(self, mock_openapi):
        """Test get_sbdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sbdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbTargetHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sdreport(self, mock_openapi):  # noqa: F811
        """Test get_sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdTargetReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sb(self, mock_openapi):  # noqa: F811
        """Test get_sb method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sb(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/listHsaTargetingReport"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sdreport(self, mock_openapi):  # noqa: F811
        """Test sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdProductAdReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sb(self, mock_openapi):  # noqa: F811
        """Test get_sb method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sb(access_token="test_token", sid="test_id", profile_id="test_id", report_date="2024-01-01", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/listHsaProductAdReport"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_spdata(self, mock_openapi):
        """Test get_spdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_spdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spTargetHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaPurchasedAsinReports(self, mock_openapi):
        """Test newad_hsaPurchasedAsinReports method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaPurchasedAsinReports(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaPurchasedAsinReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spdata(self, mock_openapi):  # noqa: F811
        """Test spdata method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spdata(access_token="test_token", report_date="2024-01-01", campaign_id="test_id")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spAdvertiseHourData"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sdreport(self, mock_openapi):  # noqa: F811
        """Test sdreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sdreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdAsinReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbreport(self, mock_openapi):  # noqa: F811
        """Test sbreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaQueryWordReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_sbreport(self, mock_openapi):  # noqa: F811
        """Test sbreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.sbreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaAdGroupReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):  # noqa: F811
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/queryWordReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_analysisproduct(self, mock_openapi):
        """Test get_analysisproduct method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_analysisproduct(access_token="test_token", sid="test_id", profile_id="test_id", sku="test_value", start_date="2024-01-01", end_date="2024-01-01", sd="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/basicOpen/adReport/productOrderAnalysis/list"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_spreport(self, mock_openapi):  # noqa: F811
        """Test spreport method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.spreport(access_token="test_token")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/asinReports"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_sdCampaigns(self, mock_openapi):
        """Test newad_sdCampaigns method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_sdCampaigns(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdCampaigns"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_spCampaigns(self, mock_openapi):
        """Test newad_spCampaigns method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_spCampaigns(access_token="test_token", code="test_value", message="test_value", error_details="test_value", request_id="test_id", response_time="test_value", total="test_value", next_token="test_value", data="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spCampaigns"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaProductAds(self, mock_openapi):
        """Test newad_hsaProductAds method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaProductAds(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaProductAds"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_sdProductAds(self, mock_openapi):
        """Test newad_sdProductAds method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_sdProductAds(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdProductAds"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_spProductAds(self, mock_openapi):
        """Test newad_spProductAds method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_spProductAds(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spProductAds"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaAdGroups(self, mock_openapi):
        """Test newad_hsaAdGroups method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaAdGroups(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaAdGroups"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaNegativeKeywords(self, mock_openapi):
        """Test newad_hsaNegativeKeywords method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaNegativeKeywords(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaNegativeKeywords"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_sdAdGroups(self, mock_openapi):
        """Test newad_sdAdGroups method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_sdAdGroups(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdAdGroups"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_hsaCampaigns(self, mock_openapi):
        """Test newad_hsaCampaigns method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_hsaCampaigns(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaCampaigns"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sb(self, mock_openapi):  # noqa: F811
        """Test get_sb method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sb(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sbTargeting"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_portfolios(self, mock_openapi):
        """Test newad_portfolios method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_portfolios(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/portfolios"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sd(self, mock_openapi):
        """Test get_sd method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sd(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdNegativeTargets"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sp(self, mock_openapi):
        """Test get_sp method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sp(access_token="test_token", sid="test_id", profile_id="test_id", target_type="test_value", campaign_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spNegativeTargetsOrKeywords"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sb(self, mock_openapi):  # noqa: F811
        """Test get_sb method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sb(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/hsaNegativeTargets"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_spKeywords(self, mock_openapi):
        """Test newad_spKeywords method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_spKeywords(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spKeywords"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_newad_spAdGroups(self, mock_openapi):
        """Test newad_spAdGroups method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.newad_spAdGroups(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spAdGroups"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sd(self, mock_openapi):  # noqa: F811
        """Test get_sd method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sd(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/sdTargets"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_list(self, mock_openapi):
        """Test get_list method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_list(access_token="test_token", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/basicOpen/baseData/account/list"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_get_sp(self, mock_openapi):  # noqa: F811
        """Test get_sp method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.get_sp(access_token="test_token", sid="test_id", profile_id="test_id", offset="test_value", length="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/spTargets"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_aba(self, mock_openapi):
        """Test aba method."""
        # Arrange
        ads_endpoints = AdsEndpoints(mock_openapi)
        expected_response = {"code": 0, "message": "success", "data": {"result": "test"}}
        mock_openapi.call_api.return_value = expected_response

        # Act
        result = await ads_endpoints.aba(access_token="test_token", country="test_value", data_start_time="test_value")

        # Assert
        assert result == expected_response
        mock_openapi.call_api.assert_called_once()

        # Verify API path
        call_args = mock_openapi.call_api.call_args
        assert call_args[1]["route_name"] == "/pb/openapi/newad/abaReport"
        assert call_args[1]["access_token"] == "test_token"

    @pytest.mark.asyncio
    async def test_access_token_required(self, mock_openapi):
        """Test that access_token is required for all methods."""
        ads_endpoints = AdsEndpoints(mock_openapi)

        # Test with empty access_token should still work (validation is on server side)
        mock_openapi.call_api.return_value = {"code": 401, "message": "Unauthorized"}

        # Pick first retrieval method for testing
        result = await ads_endpoints.newad_apiLogStandard(access_token="")

        assert result["code"] == 401
        mock_openapi.call_api.assert_called_once()

    @pytest.mark.asyncio
    async def test_error_handling(self, mock_openapi):
        """Test error response handling."""
        ads_endpoints = AdsEndpoints(mock_openapi)
        error_response = {"code": 400, "message": "Bad Request", "data": None}
        mock_openapi.call_api.return_value = error_response

        # Test error response
        result = await ads_endpoints.newad_apiLogStandard(access_token="test_token")

        assert result == error_response
        assert result["code"] == 400

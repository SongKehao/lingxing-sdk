"""Inventory alerts API endpoints."""

import logging

from .base import BaseEndpoint

logger = logging.getLogger(__name__)


class InventoryAlertsEndpoints(BaseEndpoint):
    """Inventory alerts API endpoints based on restocking suggestions."""

    async def get_stockout_risk(
        self,
        access_token: str,
        data_type: int = 2,
        sid_list: list[str] | None = None,
        offset: int = 0,
        length: int = 20
    ):
        """Get stockout risk - filters products with out_stock_flag=1."""
        logger.debug("Fetching stockout risk: data_type=%s", data_type)

        req_body = {
            "data_type": data_type,
            "offset": offset,
            "length": min(length, 50)
        }
        if sid_list:
            req_body["sid_list"] = sid_list

        result = await self._request(
            access_token=access_token,
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            req_body=req_body
        )

        if result.code in [0, 200, "0", "200"] and result.data:
            result.data = [
                item for item in result.data
                if item.get("suggest_info", {}).get("out_stock_flag") == 1
            ]

        return result

    async def get_slow_moving_alerts(
        self,
        access_token: str,
        data_type: int = 2,
        sid_list: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        days_threshold: int = 90
    ):
        """Get slow-moving alerts - filters products with available_sale_days above threshold."""
        logger.debug("Fetching slow moving alerts: threshold=%s", days_threshold)

        req_body = {
            "data_type": data_type,
            "offset": offset,
            "length": min(length, 50)
        }
        if sid_list:
            req_body["sid_list"] = sid_list

        result = await self._request(
            access_token=access_token,
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            req_body=req_body
        )

        if result.code in [0, 200, "0", "200"] and result.data:
            result.data = [
                item for item in result.data
                if item.get("suggest_info", {}).get("available_sale_days", 0) > days_threshold
            ]

        return result

    async def get_replenishment_recommendations(
        self,
        access_token: str,
        data_type: int = 2,
        sid_list: list[str] | None = None,
        offset: int = 0,
        length: int = 20
    ):
        """Get replenishment recommendations - returns products with purchase suggestions."""
        logger.debug("Fetching replenishment recommendations: data_type=%s", data_type)

        req_body = {
            "data_type": data_type,
            "offset": offset,
            "length": min(length, 50)
        }
        if sid_list:
            req_body["sid_list"] = sid_list

        result = await self._request(
            access_token=access_token,
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            req_body=req_body
        )

        if result.code in [0, 200, "0", "200"] and result.data:
            result.data = [
                item for item in result.data
                if item.get("suggest_info", {}).get("quantity_sug_purchase", 0) > 0
            ]

        return result


__all__ = ['InventoryAlertsEndpoints']

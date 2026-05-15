"""Tools API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class ToolsEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_list_inventory(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询预警消息列表-库存

        API: /basicOpen/settings/warningMessage/inventoryList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，默认50，上限200 (Optional)
            start_date: 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            end_date: 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list_inventory(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/settings/warningMessage/inventoryList",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        update_time_start: str | None = None,
        update_time_end: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询竞品监控列表

        API: /basicOpen/tool/competitiveMonitor/list
        Method: POST

        Args:
            access_token: Access token for authentication
            update_time_start: 开始时间【更新时间】，闭区间，格式：Y-m-d (Optional)
            update_time_end: 结束时间【更新时间】，闭区间，格式：Y-m-d (Optional)
            search_field: 搜索字段：asin ASIN (Optional)
            search_value: 搜索值：多个使用英文逗号分隔，上限200 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "update_time_start": update_time_start,
            "update_time_end": update_time_end,
            "search_field": search_field,
            "search_value": search_value,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/tool/competitiveMonitor/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int,
        mid: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> dict[str, Any]:
        """
        关键词列表

        API: /erp/sc/routing/tool/toolKeywordRank/getKeywordList
        Method: GET

        Args:
            access_token: Access token for authentication
            mid: 国家id (Optional)
            start_date: 开始日期，格式：Y-m-d (Optional)
            end_date: 结束日期，格式：Y-m-d (Optional)
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认20，最大值为2000 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "mid": mid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/tool/toolKeywordRank/getKeywordList",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询预警消息列表-商品

        API: /basicOpen/settings/warningMessage/goodsList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，默认50，上限200 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            start_date: 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            end_date: 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/settings/warningMessage/goodsList",
            method="POST",
            req_body=params
        )


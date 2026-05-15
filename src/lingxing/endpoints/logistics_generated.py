"""Logistics API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class LogisticsEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get(
        self,
        access_token: str,
        param: dict[str, Any]
    ) -> dict[str, Any]:
        """
        查询已启用的自发货物流方式

        API: /erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType
        Method: GET

        Args:
            access_token: Access token for authentication
            param: 查询条件 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "param": param
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType",
            method="GET",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询运输方式列表

        API: /basicOpen/businessConfig/transportMethod/list
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {

        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/businessConfig/transportMethod/list",
            method="POST",
            req_body=params
        )



    async def create(
        self,
        access_token: str,
        providersData: list[Any]
    ) -> dict[str, Any]:
        """
        批量添加头程物流商

        API: /erp/sc/routing/tms/FirstVessel/addProviders
        Method: POST

        Args:
            access_token: Access token for authentication
            providersData: 物流商数据，限制20条 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "providersData": providersData
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/tms/FirstVessel/addProviders",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        search: dict[str, Any]
    ) -> dict[str, Any]:
        """
        查询物流-头程物流商

        API: /basicOpen/logistics/headLogisticsProvider/query/list
        Method: POST

        Args:
            access_token: Access token for authentication
            search: 搜索参数对象 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "search": search
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/logistics/headLogisticsProvider/query/list",
            method="POST",
            req_body=params
        )



    async def create(  # noqa: F811
        self,
        access_token: str,
        channelsData: list[Any]
    ) -> dict[str, Any]:
        """
        批量添加头程物流方式

        API: /erp/sc/routing/tms/FirstVessel/addChannels
        Method: POST

        Args:
            access_token: Access token for authentication
            channelsData: 头程物流方式数据，每次请求限制20条 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "channelsData": channelsData
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/tms/FirstVessel/addChannels",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询头程物流渠道列表

        API: /erp/sc/data/local_inventory/channelList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/local_inventory/channelList",
            method="POST",
            req_body=params
        )


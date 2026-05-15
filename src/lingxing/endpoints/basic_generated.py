"""Basic API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class BasicEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get(
        self,
        access_token: str,
        date: str
    ) -> dict[str, Any]:
        params = {
            "date": date
        }

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/finance/currency/currencyMonth",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str
    ) -> dict[str, Any]:
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/allMarketplace",
            method="GET",
            req_body=params
        )



    async def get_storelist(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询亚马逊店铺列表

        API: /erp/sc/data/seller/lists
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_storelist(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/lists",
            method="GET",
            req_body=params
        )



    async def file_download(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        下载附件

        API: /erp/sc/routing/common/file/download
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.file_download(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/common/file/download",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        country_code: str
    ) -> dict[str, Any]:
        """
        查询亚马逊国家下地区列表

        API: /erp/sc/data/worldState/lists
        Method: POST

        Args:
            access_token: Access token for authentication
            country_code: 国家code，查询亚马逊市场列表 接口对应字段【code】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "country_code": country_code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/worldState/lists",
            method="POST",
            req_body=params
        )



    async def update_store(
        self,
        access_token: str,
        sid_name_list: list[Any]
    ) -> dict[str, Any]:
        """
        批量修改店铺名称

        API: /erp/sc/data/seller/batchEditSellerName
        Method: POST

        Args:
            access_token: Access token for authentication
            sid_name_list: 批量修改店铺数组，最多可批量修改10个 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_store(token, ...)
            >>> print(result)
        """
        params = {
            "sid_name_list": sid_name_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/batchEditSellerName",
            method="POST",
            req_body=params
        )



    async def get_storelist(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询亚马逊概念店铺列表

        API: /erp/sc/data/seller/conceptLists
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_storelist(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/conceptLists",
            method="GET",
            req_body=params
        )



    async def get_erpinfolist(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询ERP用户信息列表

        API: /erp/sc/data/account/lists
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_erpinfolist(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/account/lists",
            method="GET",
            req_body=params
        )



    async def update(
        self,
        access_token: str,
        my_rate: str,
        date: str,
        code: str
    ) -> dict[str, Any]:
        """
        修改我的汇率

        API: /basicOpen/settings/exchangeRate/update
        Method: POST

        Args:
            access_token: Access token for authentication
            my_rate: 我的汇率【小数位数最多10位】，查询汇率列表 接口对应字段【my_rate】 (Required)
            date: 汇率年月，查询汇率列表 接口对应字段【date】 (Required)
            code: 币种，查询汇率列表 接口对应字段【code】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "my_rate": my_rate,
            "date": date,
            "code": code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/settings/exchangeRate/update",
            method="POST",
            req_body=params
        )



    async def file_download(  # noqa: F811
        self,
        access_token: str,
        file_id: str
    ) -> dict[str, Any]:
        """
        定制化附件下载接口

        API: /erp/sc/routing/customized/file/download
        Method: POST

        Args:
            access_token: Access token for authentication
            file_id: 附件文件id(订单详情接口中附件id字段) (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.file_download(token, ...)
            >>> print(result)
        """
        params = {
            "file_id": file_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/customized/file/download",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        countryCode: str
    ) -> dict[str, Any]:
        """
        获取国家下的州、省编码

        API: /basicOpen/multiplatform/profit/report/stateList
        Method: POST

        Args:
            access_token: Access token for authentication
            countryCode: 国家编码，二字码 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "countryCode": countryCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/profit/report/stateList",
            method="POST",
            req_body=params
        )


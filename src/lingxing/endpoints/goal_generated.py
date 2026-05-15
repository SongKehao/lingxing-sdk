"""Goal API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class GoalEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_store(
        self,
        access_token: str,
        assessYear: str
    ) -> dict[str, Any]:
        """
        店铺维度-批量查询目标

        API: /bd/goal/management/open/store/batchSelect
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_store(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/store/batchSelect",
            method="POST",
            req_body=params
        )



    async def delete_store(
        self,
        access_token: str,
        assessYear: int,
        sids: list[Any]
    ) -> dict[str, Any]:
        """
        店铺维度-批量删除目标

        API: /bd/goal/management/open/store/batchDelete
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份【只允许去年、今年、明年】 (Required)
            sids: 需要删除的店铺id列表 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete_store(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/store/batchDelete",
            method="POST",
            req_body=params
        )



    async def update(
        self,
        access_token: str,
        assessYear: int,
        assessType: int,
        currencyCode: str,
        userGoalList: list[Any]
    ) -> dict[str, Any]:
        """
        组织维度-批量新增更新目标

        API: /bd/goal/management/open/user/batchOperate
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份(只允许去年、今年、明年) (Required)
            assessType: 考核指标：1 销售额，2 销量 (Required)
            currencyCode: 币种【仅支持USD、EUR、GBP、CNY、JPY】 (Required)
            userGoalList: 用户目标集合 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear,
            "assessType": assessType,
            "currencyCode": currencyCode,
            "userGoalList": userGoalList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/user/batchOperate",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        assessYear: int,
        assessType: int
    ) -> dict[str, Any]:
        """
        组织维度-批量查询目标

        API: /bd/goal/management/open/user/batchSelect
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份 (Required)
            assessType: 考核指标：1 销售额，2 销量 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear,
            "assessType": assessType
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/user/batchSelect",
            method="POST",
            req_body=params
        )



    async def delete(
        self,
        access_token: str,
        assessYear: int,
        assessType: int,
        uidList: list[Any]
    ) -> dict[str, Any]:
        """
        组织维度-批量删除目标

        API: /bd/goal/management/open/user/batchDelete
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份【只允许去年、今年、明年】 (Required)
            assessType: 考核指标：1 销售额，2 销量 (Required)
            uidList: 用户id集合 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear,
            "assessType": assessType,
            "uidList": uidList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/user/batchDelete",
            method="POST",
            req_body=params
        )



    async def update_store(
        self,
        access_token: str,
        assessYear: int,
        currencyCode: str,
        goalList: list[Any]
    ) -> dict[str, Any]:
        """
        店铺维度-批量新增更新目标

        API: /bd/goal/management/open/store/batchOperate
        Method: POST

        Args:
            access_token: Access token for authentication
            assessYear: 目标年份(只允许去年、今年、明年) (Required)
            currencyCode: 币种【仅支持USD、EUR、GBP、CNY、JPY、原币种】 (Required)
            goalList: 目标列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_store(token, ...)
            >>> print(result)
        """
        params = {
            "assessYear": assessYear,
            "currencyCode": currencyCode,
            "goalList": goalList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/goal/management/open/store/batchOperate",
            method="POST",
            req_body=params
        )


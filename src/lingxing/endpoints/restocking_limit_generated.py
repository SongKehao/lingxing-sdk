"""RestockingLimit API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class RestockingLimitEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_restockinglimitlist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        sids: str | None = None
    ) -> dict[str, Any]:
        """
        查询补货限制列表

        API: /basicOpen/openapi/replenishmentRestriction/page/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            sids: 店铺id，多个用英文逗号隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_restockinglimitlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/replenishmentRestriction/page/list",
            method="POST",
            req_body=params
        )



    async def get_ipiinfo(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        seller_ids: str | None = None,
        mids: str | None = None,
        sids: str | None = None
    ) -> dict[str, Any]:
        """
        查询IPI信息

        API: /erp/sc/routing/fbaLimit/restock/getIpiInfo
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)
            seller_ids: 亚马逊店铺id，多个使用英文逗号分隔 ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Optional)
            mids: 站点id，多个使用英文逗号分隔 (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_ipiinfo(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "seller_ids": seller_ids,
            "mids": mids,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaLimit/restock/getIpiInfo",
            method="GET",
            req_body=params
        )


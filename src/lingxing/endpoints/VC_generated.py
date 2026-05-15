"""VC API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class VCEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_vc(
        self,
        access_token: str,
        orderNoList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        VC发货单-确认发货

        API: /basicOpen/openapi/getInvoice/invoice/batchSendGoods
        Method: GET

        Args:
            access_token: Access token for authentication
            orderNoList: orderNo列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_vc(token, ...)
            >>> print(result)
        """
        params = {
            "orderNoList": orderNoList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/getInvoice/invoice/batchSendGoods",
            method="GET",
            req_body=params
        )



    async def get_vc(  # noqa: F811
        self,
        access_token: str,
        orderNo: str
    ) -> dict[str, Any]:
        """
        查询VC发货单详情

        API: /basicOpen/openapi/getInvoice/detail
        Method: GET

        Args:
            access_token: Access token for authentication
            orderNo: 订单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_vc(token, ...)
            >>> print(result)
        """
        params = {
            "orderNo": orderNo
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/getInvoice/detail",
            method="GET",
            req_body=params
        )



    async def productRelation_batchLink(
        self,
        access_token: str,
        sidAsins: list[Any],
        productId: Any,
        isSyncPic: Any
    ) -> dict[str, Any]:
        """
        配对批量配对

        API: /basicOpen/vcservice/productRelation/batchLink
        Method: POST

        Args:
            access_token: Access token for authentication
            sidAsins: 配对的sid和asin对象数组 (Required)
            productId: 本地商品表主键ID (Required)
            isSyncPic: 是否同步图片到本地商品 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.productRelation_batchLink(token, ...)
            >>> print(result)
        """
        params = {
            "sidAsins": sidAsins,
            "productId": productId,
            "isSyncPic": isSyncPic
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/vcservice/productRelation/batchLink",
            method="POST",
            req_body=params
        )



    async def get_vclist(
        self,
        access_token: str,
        shipmentType: str,
        offset: Any | None = None,
        length: Any | None = None,
        sids: list[Any] | None = None,
        wid: list[Any] | None = None,
        status: Any | None = None,
        createTimeStartTime: str | None = None,
        createTimeEndTime: str | None = None,
        shipmentTimeStartTime: str | None = None,
        shipmentTimeEndTime: str | None = None
    ) -> dict[str, Any]:
        """
        查询VC发货单列表

        API: /basicOpen/openapi/getInvoice/page/list
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 偏移量(默认0) (Optional)
            length: 每页条数(默认20） (Optional)
            sids: 店铺id (Optional)
            wid: 国家id (Optional)
            shipmentType: 出库类型 1:DF 2:PO 3:DI (Required)
            status: 订单状态 0: 全部 5:待配货 10:待出库 15:已完成 100:已作废 (默认0） (Optional)
            createTimeStartTime: 创建日期-开始 (Optional)
            createTimeEndTime: 创建日期-结束 (Optional)
            shipmentTimeStartTime: 出库日期-开始 (Optional)
            shipmentTimeEndTime: 出库日期-结束 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_vclist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "wid": wid,
            "shipmentType": shipmentType,
            "status": status,
            "createTimeStartTime": createTimeStartTime,
            "createTimeEndTime": createTimeEndTime,
            "shipmentTimeStartTime": shipmentTimeStartTime,
            "shipmentTimeEndTime": shipmentTimeEndTime
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/getInvoice/page/list",
            method="GET",
            req_body=params
        )


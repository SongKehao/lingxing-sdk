"""AmazonSource API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class AmazonSourceEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_report(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sid: int | None = None,
        seller_id: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-移除货件（新）

        API: /erp/sc/statistic/removalShipment/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id【seller_id同时传值时，以sid为准】 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Optional)
            start_date: 开始日期【发货日期】，左闭右开 (Required)
            end_date: 结束日期【发货日期】，左闭右开 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "seller_id": seller_id,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/statistic/removalShipment/list",
            method="POST",
            req_body=params
        )



    async def get_report_inventory(
        self,
        access_token: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-预留库存

        API: /erp/sc/data/mws_report/reservedInventory
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_inventory(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/reservedInventory",
            method="POST",
            req_body=params
        )



    async def get_reportinventory_event_detail(
        self,
        access_token: str,
        sid: int,
        snapshot_date_after: str,
        snapshot_date_before: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表——Inventory Event Detail

        API: /erp/sc/data/mws_report/getFbaInventoryEventDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            snapshot_date_after: 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (Required)
            snapshot_date_before: 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportinventory_event_detail(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "snapshot_date_after": snapshot_date_after,
            "snapshot_date_before": snapshot_date_before,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/getFbaInventoryEventDetailList",
            method="GET",
            req_body=params
        )



    async def get_report(  # noqa: F811
        self,
        access_token: str,
        sid: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表—库龄表

        API: /erp/sc/routing/fba/fbaStock/getFbaAgeList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id, 多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/fbaStock/getFbaAgeList",
            method="GET",
            req_body=params
        )



    async def get_report_inventory(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        event_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-每日库存

        API: /erp/sc/data/mws_report/dailyInventory
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id【欧洲传UK下的店铺，美国传US下的店铺】 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            event_date: 报表日期，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_inventory(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "event_date": event_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/dailyInventory",
            method="POST",
            req_body=params
        )



    async def get_report_fbainventory(
        self,
        access_token: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBA库存

        API: /erp/sc/data/mws_report/manageInventory
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbainventory(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/manageInventory",
            method="POST",
            req_body=params
        )



    async def report_amazonReportExportTask(
        self,
        access_token: str,
        seller_id: str,
        report_document_id: str
    ) -> dict[str, Any]:
        """
        报告导出 - 报告下载链接续期

        API: /basicOpen/report/amazonReportExportTask
        Method: POST

        Args:
            access_token: Access token for authentication
            seller_id: 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】 (Required)
            report_document_id: 报告文档Id,报告导出-查询导出任务结果接口对应字段【data>>report_document_id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.report_amazonReportExportTask(token, ...)
            >>> print(result)
        """
        params = {
            "seller_id": seller_id,
            "report_document_id": report_document_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/report/amazonReportExportTask",
            method="POST",
            req_body=params
        )



    async def get_report(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int,
        start_date: str,
        end_date: str,
        sids: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-盘存记录

        API: /basicOpen/openapi/mwsReport/adjustmentList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认20，上限10000 (Required)
            sids: 店铺id，多个店铺以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_value: 搜索值 (Optional)
            start_date: 发货日期开始时间【闭区间】，格式Y-m-d【report_date】 (Required)
            end_date: 发货日期结束时间【闭区间】，格式Y-m-d【report_date】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "search_value": search_value,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/mwsReport/adjustmentList",
            method="POST",
            req_body=params
        )



    async def get_report_fbaorder(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBA订单

        API: /erp/sc/data/mws_report/fbaOrders
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始日期，左闭区间，Y-m-d格式 (Required)
            end_date: 结束日期，右开区间，Y-m-d格式 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbaorder(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/fbaOrders",
            method="POST",
            req_body=params
        )



    async def get_report_fbainventory(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBA可售库存

        API: /erp/sc/data/mws_report/getAfnFulfillableQuantity
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbainventory(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/getAfnFulfillableQuantity",
            method="GET",
            req_body=params
        )



    async def get_report_order(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-移除订单（新）

        API: /erp/sc/routing/data/order/removalOrderListNew
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 查询时间【更新时间】，左闭区间,格式：Y-m-d (Required)
            end_date: 查询时间【更新时间】，右开区间,格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/order/removalOrderListNew",
            method="POST",
            req_body=params
        )



    async def get_report_fbaorder(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBA换货订单

        API: /erp/sc/routing/data/order/fbaExchangeOrderList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始时间，左闭区间，格式：Y-m-d (Required)
            end_date: 结束时间，右开区间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbaorder(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/order/fbaExchangeOrderList",
            method="POST",
            req_body=params
        )



    async def get_reportamazon_fulfilled_shipments_v1(
        self,
        access_token: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表—Amazon Fulfilled Shipments v1

        API: /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportamazon_fulfilled_shipments_v1(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList",
            method="GET",
            req_body=params
        )



    async def create(
        self,
        access_token: str,
        seller_id: str,
        report_type: str,
        marketplace_ids: list[Any],
        data_start_time: str | None = None,
        data_end_time: str | None = None
    ) -> dict[str, Any]:
        """
        报告导出 - 创建导出任务

        API: /basicOpen/report/create/reportExportTask
        Method: GET

        Args:
            access_token: Access token for authentication
            seller_id: 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】 (Required)
            report_type: 亚马逊报表类型【具体类型参看下方附加说明】 (Required)
            data_start_time: 亚马逊报表请求开始时间，时间格式：YYYY-MM-DDTHH:MM:SSZ (Optional)
            data_end_time: 亚马逊报表请求结束时间，时间格式：YYYY-MM-DDTHH:MM:SSZ (Optional)
            marketplace_ids: 亚马逊市场id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "seller_id": seller_id,
            "report_type": report_type,
            "data_start_time": data_start_time,
            "data_end_time": data_end_time,
            "marketplace_ids": marketplace_ids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/report/create/reportExportTask",
            method="GET",
            req_body=params
        )



    async def get_data_inventory_event_detail_v1(
        self,
        access_token: str,
        sid: int,
        snapshot_date_after: str,
        snapshot_date_before: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源表数据--Inventory Event Detail v1

        API: /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            snapshot_date_after: 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (Required)
            snapshot_date_before: 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限10000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_data_inventory_event_detail_v1(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "snapshot_date_after": snapshot_date_after,
            "snapshot_date_before": snapshot_date_before,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList",
            method="GET",
            req_body=params
        )



    async def get_reportamazon_fulfilled_shipments(
        self,
        access_token: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表—Amazon Fulfilled Shipments

        API: /erp/sc/data/mws_report/getAmazonFulfilledShipmentsList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportamazon_fulfilled_shipments(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList",
            method="GET",
            req_body=params
        )



    async def get_report_detail(
        self,
        access_token: str,
        sid: int,
        event_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-交易明细

        API: /erp/sc/data/mws_report/transaction
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            event_date: 报表日期，格式：Y-m-d【每月３日后支持查询上月数据】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "event_date": event_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/transaction",
            method="POST",
            req_body=params
        )



    async def get_report_order(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-所有订单

        API: /erp/sc/data/mws_report/allOrders
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 亚马逊当地下单时间，左闭区间，格式：Y-m-d (Required)
            end_date: 亚马逊当地下单时间，右开区间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws_report/allOrders",
            method="POST",
            req_body=params
        )


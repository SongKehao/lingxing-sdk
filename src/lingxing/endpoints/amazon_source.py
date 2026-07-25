"""亚马逊原始数据 API endpoints."""

from __future__ import annotations

from ..models.responses.source_data import (
    AdjustmentlistResponse,
    DailyinventoryResponse,
    FbaFbastockGetfbaagelistResponse,
    FbaReportRemovallistsResponse,
    GetafnfulfillablequantityResponse,
    ManageinventoryResponse,
    MwsReportAllordersResponse,
    MwsReportFbaordersResponse,
    MwsReportGetamazonfulfilledshipmentslistResponse,
    MwsReportGetfbainventoryeventdetaillistResponse,
    MwsReportTransactionResponse,
    MwsReportV1GetamazonfulfilledshipmentslistResponse,
    MwsReportV1GetfbainventoryeventdetaillistResponse,
    OrderFbaexchangeorderlistResponse,
    OrderFbmreturnorderlistResponse,
    OrderRemovalorderlistnewResponse,
    RefundordersResponse,
    RemovalordersResponse,
    ReservedinventoryResponse,
    StatisticRemovalshipmentListResponse,
)
from ._base import BaseEndpoint


class AmazonSourceEndpoints(BaseEndpoint):
    """领星亚马逊原始数据 API (20个接口)."""

    async def adjustment_list(
        self,
        offset: int = None,
        length: int = None,
        sids: str = None,
        search_field: str = None,
        search_value: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> list[AdjustmentlistResponse]:
        """查询亚马逊源报表-盘存记录.

        POST /basicOpen/openapi/mwsReport/adjustmentList

        Args:
            offset: 分页偏移量，默认0 (required), int.
            length: 分页长度，默认20，上限10000 (required), int.
            sids: 店铺id，多个店铺以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
            search_field: 搜索的字段： asin ASIN msku MSKU fnsku FNSKU item_name 标题 transaction_item_id 交易编号, string.
            search_value: 搜索值, string.
            start_date: 发货日期开始时间【闭区间】，格式Y-m-d【report_date】 (required), string.
            end_date: 发货日期结束时间【闭区间】，格式Y-m-d【report_date】 (required), string."""
        resp = await self._post(
            "/basicOpen/openapi/mwsReport/adjustmentList",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "sids": sids,
                    "search_field": search_field,
                    "search_value": search_value,
                    "start_date": start_date,
                    "end_date": end_date,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, AdjustmentlistResponse)

    async def afn_fulfillable_quantity(
        self, sid: int = None, offset: int = None, length: int = None
    ) -> list[GetafnfulfillablequantityResponse]:
        """查询亚马逊源报表-FBA可售库存.

        POST /erp/sc/data/mws_report/getAfnFulfillableQuantity

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/getAfnFulfillableQuantity",
            {k: v for k, v in {"sid": sid, "offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_list(resp.data, GetafnfulfillablequantityResponse)

    async def all_orders(
        self,
        sid: int = None,
        date_type: int = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportAllordersResponse]:
        """查询亚马逊源报表-所有订单.

        POST /erp/sc/data/mws_report/allOrders

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            date_type: 时间查询类型：【默认1】 1 下单日期 2 亚马逊订单更新时间, int.
            start_date: 亚马逊当地下单时间，左闭区间，格式：Y-m-d (required), string.
            end_date: 亚马逊当地下单时间，右开区间，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/allOrders",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "date_type": date_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportAllordersResponse)

    async def daily_inventory(
        self, sid: int = None, event_date: str = None, offset: int = None, length: int = None
    ) -> list[DailyinventoryResponse]:
        """查询亚马逊源报表-每日库存.

        POST /erp/sc/data/mws_report/dailyInventory

        Args:
            sid: 店铺id【欧洲传UK下的店铺，美国传US下的店铺】 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            event_date: 报表日期，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/dailyInventory",
            {
                k: v
                for k, v in {"sid": sid, "event_date": event_date, "offset": offset, "length": length}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, DailyinventoryResponse)

    async def fba_orders(
        self,
        sid: int = None,
        date_type: int = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportFbaordersResponse]:
        """查询亚马逊源报表-FBA订单.

        POST /erp/sc/data/mws_report/fbaOrders

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            date_type: 日期搜索维度：【默认1】 1 下单日期 2 配送日期, int.
            start_date: 开始日期，左闭区间，Y-m-d格式 (required), string.
            end_date: 结束日期，右开区间，Y-m-d格式 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/fbaOrders",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "date_type": date_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportFbaordersResponse)

    async def manage_inventory(
        self, sid: int = None, offset: int = None, length: int = None
    ) -> list[ManageinventoryResponse]:
        """查询亚马逊源报表-FBA库存.

        POST /erp/sc/data/mws_report/manageInventory

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/manageInventory",
            {k: v for k, v in {"sid": sid, "offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_list(resp.data, ManageinventoryResponse)

    async def refund_orders(
        self,
        sid: int = None,
        date_type: int = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[RefundordersResponse]:
        """查询亚马逊源报表-FBA退货订单.

        POST /erp/sc/data/mws_report/refundOrders

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            date_type: 时间查询类型【默认1】： 1 退货时间【站点时间】 2 更新时间【北京时间】, int.
            start_date: 开始时间，左闭右开，格式：Y-m-d (required), string.
            end_date: 结束时间，左闭右开，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/refundOrders",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "date_type": date_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, RefundordersResponse)

    async def removal_lists(
        self, sid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[FbaReportRemovallistsResponse]:
        """查询亚马逊源报表-移除货件（旧）.

        POST /erp/sc/data/fba_report/removalLists

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 开始时间，格式：Y-m-d，闭区间 (required), string.
            end_date: 结束时间，格式：Y-m-d，开区间 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/fba_report/removalLists",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, FbaReportRemovallistsResponse)

    async def removal_order_list_new(
        self,
        sid: int = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
        search_field_time: str = None,
    ) -> list[OrderRemovalorderlistnewResponse]:
        """查询亚马逊源报表-移除订单（新）.

        POST /erp/sc/routing/data/order/removalOrderListNew

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 查询时间【更新时间】，左闭区间,格式：Y-m-d (required), string.
            end_date: 查询时间【更新时间】，右开区间,格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int.
            search_field_time: 搜索时间类型：【默认 last_updated_date】 last_updated_date 更新时间 request_date 创建时间 (required), string."""
        resp = await self._post(
            "/erp/sc/routing/data/order/removalOrderListNew",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                    "search_field_time": search_field_time,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, OrderRemovalorderlistnewResponse)

    async def removal_shipment_list(
        self,
        sid: int = None,
        seller_id: str = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[StatisticRemovalshipmentListResponse]:
        """查询亚马逊源报表-移除货件（新）.

        POST /erp/sc/statistic/removalShipment/list

        Args:
            sid: 店铺id【seller_id同时传值时，以sid为准】 ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】, string.
            start_date: 开始日期【发货日期】，左闭右开 (required), string.
            end_date: 结束日期【发货日期】，左闭右开 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/statistic/removalShipment/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "seller_id": seller_id,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, StatisticRemovalshipmentListResponse)

    async def reserved_inventory(
        self, sid: int = None, offset: int = None, length: int = None
    ) -> list[ReservedinventoryResponse]:
        """查询亚马逊源报表-预留库存.

        POST /erp/sc/data/mws_report/reservedInventory

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/reservedInventory",
            {k: v for k, v in {"sid": sid, "offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_list(resp.data, ReservedinventoryResponse)

    async def source_removal_orders(
        self, sid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[RemovalordersResponse]:
        """查询亚马逊源报表-移除订单（旧）.

        POST /erp/sc/data/mws_report/removalOrders

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 更新时间，左闭区间，格式：Y-m-d (required), string.
            end_date: 更新时间，右开区间，格式：Y-m-d格式 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/removalOrders",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, RemovalordersResponse)

    async def transaction(
        self, sid: int = None, event_date: str = None, offset: int = None, length: int = None
    ) -> list[MwsReportTransactionResponse]:
        """查询亚马逊源报表-交易明细.

        POST /erp/sc/data/mws_report/transaction

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            event_date: 报表日期，格式：Y-m-d【每月３日后支持查询上月数据】 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/transaction",
            {
                k: v
                for k, v in {"sid": sid, "event_date": event_date, "offset": offset, "length": length}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportTransactionResponse)

    async def fba_exchange_order_list(
        self, sid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[OrderFbaexchangeorderlistResponse]:
        """查询亚马逊源报表-FBA换货订单.

        POST /erp/sc/routing/data/order/fbaExchangeOrderList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 开始时间，左闭区间，格式：Y-m-d (required), string.
            end_date: 结束时间，右开区间，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/routing/data/order/fbaExchangeOrderList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, OrderFbaexchangeorderlistResponse)

    async def fbm_return_order_list(
        self,
        sid: int = None,
        start_date: str = None,
        end_date: str = None,
        date_type: int = None,
        offset: int = None,
        length: int = None,
    ) -> list[OrderFbmreturnorderlistResponse]:
        """查询亚马逊源报表-FBM退货订单.

        POST /erp/sc/routing/data/order/fbmReturnOrderList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 开始时间，左闭区间，格式：Y-m-d (required), string.
            end_date: 结束时间，右开区间，格式：Y-m-d (required), string.
            date_type: 时间查询类型：【默认1】 1 退货日期 2 下单日期, int.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/routing/data/order/fbmReturnOrderList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "date_type": date_type,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, OrderFbmreturnorderlistResponse)

    async def get_amazon_fulfilled_shipments_list(
        self,
        sid: int = None,
        shipment_date_after: str = None,
        shipment_date_before: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportGetamazonfulfilledshipmentslistResponse]:
        """查询亚马逊源报表—Amazon Fulfilled Shipments.

        POST /erp/sc/data/mws_report/getAmazonFulfilledShipmentsList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            shipment_date_after: 快照开始时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天 (required), string.
            shipment_date_before: 快照结束时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "shipment_date_after": shipment_date_after,
                    "shipment_date_before": shipment_date_before,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportGetamazonfulfilledshipmentslistResponse)

    async def get_fba_age_list(
        self, sid: str = None, offset: int = None, length: int = None
    ) -> list[FbaFbastockGetfbaagelistResponse]:
        """查询亚马逊源报表—库龄表.

        POST /erp/sc/routing/fba/fbaStock/getFbaAgeList

        Args:
            sid: 店铺id, 多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
            offset: 分页偏移量, int.
            length: 分页长度，默认20, int."""
        resp = await self._post(
            "/erp/sc/routing/fba/fbaStock/getFbaAgeList",
            {k: v for k, v in {"sid": sid, "offset": offset, "length": length}.items() if v is not None},
        )
        return self._parse_list(resp.data, FbaFbastockGetfbaagelistResponse)

    async def get_fba_inventory_event_detail_list(
        self,
        sid: int = None,
        snapshot_date_after: str = None,
        snapshot_date_before: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportGetfbainventoryeventdetaillistResponse]:
        """查询亚马逊源报表——Inventory Event Detail.

        POST /erp/sc/data/mws_report/getFbaInventoryEventDetailList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            snapshot_date_after: 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (required), string.
            snapshot_date_before: 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report/getFbaInventoryEventDetailList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "snapshot_date_after": snapshot_date_after,
                    "snapshot_date_before": snapshot_date_before,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportGetfbainventoryeventdetaillistResponse)

    async def v1get_amazon_fulfilled_shipments_list(
        self,
        sid: int = None,
        shipment_date_after: str = None,
        shipment_date_before: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportV1GetamazonfulfilledshipmentslistResponse]:
        """查询亚马逊源报表—Amazon Fulfilled Shipments v1.

        POST /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            shipment_date_after: 快照开始时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天 (required), string.
            shipment_date_before: 快照结束时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "shipment_date_after": shipment_date_after,
                    "shipment_date_before": shipment_date_before,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportV1GetamazonfulfilledshipmentslistResponse)

    async def v1get_fba_inventory_event_detail_list(
        self,
        sid: int = None,
        snapshot_date_after: str = None,
        snapshot_date_before: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[MwsReportV1GetfbainventoryeventdetaillistResponse]:
        """查询亚马逊源表数据--Inventory Event Detail v1.

        POST /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            snapshot_date_after: 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (required), string.
            snapshot_date_before: 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000，上限10000, int."""
        resp = await self._post(
            "/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "snapshot_date_after": snapshot_date_after,
                    "snapshot_date_before": snapshot_date_before,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, MwsReportV1GetfbainventoryeventdetaillistResponse)

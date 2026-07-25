"""统计报表 API endpoints."""

from __future__ import annotations

from ..models.responses.statistics import (
    FbaReportStoragefeelongtermResponse,
    FbaReportStoragefeemonthResponse,
    FbaStockReportGetlistResponse,
    FinanceProfitstatisProfitmskuResponse,
    InventorylogWarehousereportGetlocalwarehousedetaillistResponse,
    InventorylogWarehousereportGetlocalwarehousesummarylistResponse,
    InventorylogWarehousereportGetoverseadetaillistResponse,
    InventorylogWarehousereportGetoverseasummarylistResponse,
    InvReportFbaDetailResponse,
    InvReportFbaGatherResponse,
    InvReportLocalAggregateResponse,
    InvReportLocalDetailResponse,
    InvReportOverseasAggregateResponse,
    InvReportOverseasDetailResponse,
    MonthRefundItem,
    OperatemanageOperatelogListResponse,
    ParentAsinListRecords,
    Platformstatisticsv2SalestatPagelistResponse,
    ProductperformanceOpenapiAsinlistResponse,
    PurchaseBuyerListResponse,
    PurchaseProductListResponse,
    PurchaseSupplierListResponse,
    ReimbursementlistResponse,
    ReportAmazonreportexporttaskResponse,
    ReportCreateReportexporttaskResponse,
    ReportInventoryListResponse,
    ReportNppmListResponse,
    ReportQueryReportexporttaskResponse,
    ReportRealtimesalesListResponse,
    ReportSalesListResponse,
    ReportTrafficListResponse,
    SalesanalysisProductperformancePerformancetrendbyhourResponse,
    SalesanalysisReturnorderAnalysislistsResponse,
    SalesReportAsindailylistsResponse,
    SalesReportAsinlistResponse,
    SalesReportSalesResponse,
    StatisticRemovalOrderCreateResponse,
    StatisticsAsinListRecords,
    StatisticsMskuListRecords,
    StatisticsSellerListRecords,
)
from ._base import BaseEndpoint


class StatisticsEndpoints(BaseEndpoint):
    """领星统计报表 API (31个接口)."""

    async def profit_stat_msku(
        self,
        offset: int = None,
        length: int = None,
        mids: list = None,
        sids: list = None,
        start_date: str = None,
        end_date: str = None,
        search_field: str = None,
        search_value: str = None,
        currency_code: str = None,
    ) -> list[StatisticsMskuListRecords]:
        """查询利润统计-MSKU.

        POST /bd/profit/statistics/open/msku/list

        Args:
            offset: see API doc.
            length: see API doc.
            mids: see API doc.
            sids: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            search_field: see API doc.
            search_value: see API doc.
            currency_code: see API doc."""
        resp = await self._post(
            "/bd/profit/statistics/open/msku/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "mids": mids,
                    "sids": sids,
                    "startDate": start_date,
                    "endDate": end_date,
                    "searchField": search_field,
                    "searchValue": search_value,
                    "currencyCode": currency_code,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, StatisticsMskuListRecords)

    async def profit_stat_asin(
        self,
        offset: int = None,
        length: int = None,
        mids: list = None,
        sids: list = None,
        start_date: str = None,
        end_date: str = None,
        search_field: str = None,
        search_value: str = None,
        currency_code: str = None,
    ) -> list[StatisticsAsinListRecords]:
        """查询利润统计-ASIN.

        POST /bd/profit/statistics/open/asin/list

        Args:
            offset: see API doc.
            length: see API doc.
            mids: see API doc.
            sids: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            search_field: see API doc.
            search_value: see API doc.
            currency_code: see API doc."""
        resp = await self._post(
            "/bd/profit/statistics/open/asin/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "mids": mids,
                    "sids": sids,
                    "startDate": start_date,
                    "endDate": end_date,
                    "searchField": search_field,
                    "searchValue": search_value,
                    "currencyCode": currency_code,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, StatisticsAsinListRecords)

    async def profit_stat_parent_asin(
        self,
        offset: int = None,
        length: int = None,
        mids: list = None,
        sids: list = None,
        start_date: str = None,
        end_date: str = None,
        search_field: str = None,
        search_value: str = None,
        currency_code: str = None,
    ) -> list[ParentAsinListRecords]:
        """查询利润统计-父ASIN.

        POST /bd/profit/statistics/open/parent/asin/list

        Args:
            offset: see API doc.
            length: see API doc.
            mids: see API doc.
            sids: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            search_field: see API doc.
            search_value: see API doc.
            currency_code: see API doc."""
        resp = await self._post(
            "/bd/profit/statistics/open/parent/asin/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "mids": mids,
                    "sids": sids,
                    "startDate": start_date,
                    "endDate": end_date,
                    "searchField": search_field,
                    "searchValue": search_value,
                    "currencyCode": currency_code,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ParentAsinListRecords)

    async def profit_stat_seller(
        self,
        offset: int = None,
        length: int = None,
        mids: list = None,
        sids: list = None,
        start_date: str = None,
        end_date: str = None,
        currency_code: str = None,
    ) -> list[StatisticsSellerListRecords]:
        """查询利润统计-店铺.

        POST /bd/profit/statistics/open/seller/list

        Args:
            offset: see API doc.
            length: see API doc.
            mids: see API doc.
            sids: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            currency_code: see API doc."""
        resp = await self._post(
            "/bd/profit/statistics/open/seller/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "mids": mids,
                    "sids": sids,
                    "startDate": start_date,
                    "endDate": end_date,
                    "currencyCode": currency_code,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, StatisticsSellerListRecords)

    async def inv_report_local_aggregate(
        self, start_date: str = None, end_date: str = None, sys_wid: int = None
    ) -> list[InvReportLocalAggregateResponse]:
        """库存报表-本地仓-新报表-汇总.

        POST /inventory/center/openapi/storageReport/local/aggregate/list

        Args:
            start_date: see API doc.
            end_date: see API doc.
            sys_wid: see API doc."""
        resp = await self._post(
            "/inventory/center/openapi/storageReport/local/aggregate/list",
            {
                k: v
                for k, v in {"start_date": start_date, "end_date": end_date, "sys_wid": sys_wid}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportLocalAggregateResponse)

    async def inv_report_local_detail(
        self, offset: int = None, length: int = None, start_date: str = None, end_date: str = None, sys_wid: int = None
    ) -> list[InvReportLocalDetailResponse]:
        """库存报表-本地仓-新报表-明细.

        POST /inventory/center/openapi/storageReport/local/detail/page

        Args:
            offset: see API doc.
            length: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            sys_wid: see API doc."""
        resp = await self._post(
            "/inventory/center/openapi/storageReport/local/detail/page",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "sys_wid": sys_wid,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportLocalDetailResponse)

    async def inv_report_overseas_aggregate(
        self, start_date: str = None, end_date: str = None, sys_wid: int = None
    ) -> list[InvReportOverseasAggregateResponse]:
        """库存报表-海外仓-新报表-汇总.

        POST /inventory/center/openapi/storageReport/overseas/aggregate/list

        Args:
            start_date: see API doc.
            end_date: see API doc.
            sys_wid: see API doc."""
        resp = await self._post(
            "/inventory/center/openapi/storageReport/overseas/aggregate/list",
            {
                k: v
                for k, v in {"start_date": start_date, "end_date": end_date, "sys_wid": sys_wid}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportOverseasAggregateResponse)

    async def inv_report_overseas_detail(
        self, offset: int = None, length: int = None, start_date: str = None, end_date: str = None, sys_wid: int = None
    ) -> list[InvReportOverseasDetailResponse]:
        """库存报表-海外仓-新报表-明细.

        POST /inventory/center/openapi/storageReport/overseas/detail/page

        Args:
            offset: see API doc.
            length: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            sys_wid: see API doc."""
        resp = await self._post(
            "/inventory/center/openapi/storageReport/overseas/detail/page",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "sys_wid": sys_wid,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportOverseasDetailResponse)

    async def inv_report_fba_gather(
        self,
        offset: int = None,
        length: int = None,
        seller_id: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> list[InvReportFbaGatherResponse]:
        """库存报表-FBA-新版-汇总.

        POST /cost/center/openApi/fba/gather/query

        Args:
            offset: see API doc.
            length: see API doc.
            seller_id: see API doc.
            start_date: see API doc.
            end_date: see API doc."""
        resp = await self._post(
            "/cost/center/openApi/fba/gather/query",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "seller_id": seller_id,
                    "start_date": start_date,
                    "end_date": end_date,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportFbaGatherResponse)

    async def inv_report_fba_detail(
        self,
        offset: int = None,
        length: int = None,
        start_date: str = None,
        end_date: str = None,
        seller_id: str = None,
    ) -> list[InvReportFbaDetailResponse]:
        """库存报表-FBA-新版-明细.

        POST /cost/center/openApi/fba/detail/query

        Args:
            offset: see API doc.
            length: see API doc.
            start_date: see API doc.
            end_date: see API doc.
            seller_id: see API doc."""
        resp = await self._post(
            "/cost/center/openApi/fba/detail/query",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "seller_id": seller_id,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InvReportFbaDetailResponse)

    async def amazon_report_export_task(
        self, region: str = None, seller_id: str = None, report_document_id: str = None
    ) -> ReportAmazonreportexporttaskResponse | None:
        """报告导出 - 报告下载链接续期.

        POST /basicOpen/report/amazonReportExportTask

        Args:
            region: 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东 (required), string.
            seller_id: 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】 (required), string.
            report_document_id: 报告文档Id,报告导出-查询导出任务结果接口对应字段【data>>report_document_id】 (required), string."""
        resp = await self._post(
            "/basicOpen/report/amazonReportExportTask",
            {
                k: v
                for k, v in {"region": region, "seller_id": seller_id, "report_document_id": report_document_id}.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, ReportAmazonreportexporttaskResponse)

    async def asin_daily_lists(
        self,
        sid: int = None,
        event_date: str = None,
        asin_type: int = None,
        type: int = None,
        offset: int = None,
        length: int = None,
    ) -> list[SalesReportAsindailylistsResponse]:
        """查询亚马逊销量统计.

        POST /erp/sc/data/sales_report/asinDailyLists

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            event_date: 报表时间【站点时间】，格式：Y-m-d (required), string.
            asin_type: 查询维度：【默认1】 1 asin 2 msku, int.
            type: 类型：【默认1】 1 销售额 2 销量 3 订单量, int.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/sales_report/asinDailyLists",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "event_date": event_date,
                    "asin_type": asin_type,
                    "type": type,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SalesReportAsindailylistsResponse)

    async def asin_list(
        self,
        sid: int = None,
        asin_type: int = None,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[SalesReportAsinlistResponse]:
        """查询产品表现（旧）.

        POST /erp/sc/data/sales_report/asinList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin_type: 产品表现维度：【默认0】 0 asin 1 父asin, int.
            start_date: 报表时间，格式：Y-m-d，闭区间 (required), string.
            end_date: 报表时间，格式：Y-m-d，开区间 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/sales_report/asinList",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "asin_type": asin_type,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SalesReportAsinlistResponse)

    async def create_removal_order(self, lists: list = None) -> StatisticRemovalOrderCreateResponse | None:
        """创建移除订单.

        POST /erp/sc/statistic/removalOrder/createAndCommit

        Args:
            lists: 提交数据，支持批量，上限100个 (required), array."""
        resp = await self._post(
            "/erp/sc/statistic/removalOrder/createAndCommit",
            {k: v for k, v in {"lists": lists}.items() if v is not None},
        )
        return self._parse_one(resp.data, StatisticRemovalOrderCreateResponse)

    async def fba_storage_fee_long_term(
        self, sid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[FbaReportStoragefeelongtermResponse]:
        """查询FBA长期仓储费.

        POST /erp/sc/data/fba_report/storageFeeLongTerm

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 收费日期，左闭区间 (required), string.
            end_date: 收费日期，右开区间 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/fba_report/storageFeeLongTerm",
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
        return self._parse_list(resp.data, FbaReportStoragefeelongtermResponse)

    async def fba_storage_fee_month(
        self, sid: int = None, month: str = None, offset: int = None, length: int = None
    ) -> list[FbaReportStoragefeemonthResponse]:
        """查询FBA月仓储费.

        POST /erp/sc/data/fba_report/storageFeeMonth

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            month: 收费月份，格式：Y-m (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/fba_report/storageFeeMonth",
            {
                k: v
                for k, v in {"sid": sid, "month": month, "offset": offset, "length": length}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, FbaReportStoragefeemonthResponse)

    async def fba_stock_report_list(
        self,
        start_month: str = None,
        end_month: str = None,
        seller_id: str = None,
        dimention: int = None,
        offset: int = None,
        length: int = None,
        attribute: int = None,
    ) -> list[FbaStockReportGetlistResponse]:
        """库存报表-FBA-历史报表-汇总-明细.

        POST /erp/sc/routing/fba/fbaStockReport/getList

        Args:
            start_month: 开始月份，默认当前月份, string.
            end_month: 截至月份，默认当前月份, string.
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】, string.
            dimention: 数据维度： 1 汇总 2 明细【默认值】, int.
            offset: 分页偏移量【dimention=2 明细维度生效】，默认0, int.
            length: 分页长度【dimention=2 明细维度生效】，默认20，上限5000, int.
            attribute: 可售状态：【dimention=2 明细维度生效】 0 不可售 1 可售 2 全部【默认值】, int."""
        resp = await self._post(
            "/erp/sc/routing/fba/fbaStockReport/getList",
            {
                k: v
                for k, v in {
                    "start_month": start_month,
                    "end_month": end_month,
                    "seller_id": seller_id,
                    "dimention": dimention,
                    "offset": offset,
                    "length": length,
                    "attribute": attribute,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, FbaStockReportGetlistResponse)

    async def local_aggregate_list(
        self, sys_wid: int = None, start_date: str = None, end_date: str = None
    ) -> list[InventorylogWarehousereportGetlocalwarehousesummarylistResponse]:
        """库存报表-本地仓-历史报表-汇总.

        POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList

        Args:
            sys_wid: 领星系统仓库id，多个用英文逗号分隔, int.
            start_date: 开始时间，格式：Y-m-d (required), string.
            end_date: 结束时间，格式：Y-m-d (required), string."""
        resp = await self._post(
            "/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList",
            {
                k: v
                for k, v in {"sys_wid": sys_wid, "start_date": start_date, "end_date": end_date}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InventorylogWarehousereportGetlocalwarehousesummarylistResponse)

    async def local_detail_list(
        self, sys_wid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[InventorylogWarehousereportGetlocalwarehousedetaillistResponse]:
        """库存报表-本地仓-历史报表-明细.

        POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList

        Args:
            sys_wid: 系统仓库id，多个用英文逗号分隔, int.
            start_date: 开始时间，格式：Y-m-d (required), string.
            end_date: 结束时间，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0 (required), int.
            length: 分页长度，默认15 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList",
            {
                k: v
                for k, v in {
                    "sys_wid": sys_wid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InventorylogWarehousereportGetlocalwarehousedetaillistResponse)

    async def month_refund(
        self,
        asin_type: str = None,
        offset: int = None,
        length: int = None,
        start_date: str = None,
        end_date: str = None,
        sid: int = None,
        sort_field: str = None,
        sort_type: str = None,
    ) -> tuple[list[MonthRefundItem], int]:
        """查询退款量（旧）.

        POST /erp/sc/routing/finance/Refund/profitMonthRefund

        Args:
            asin_type: 1 asin  2 父asin (required), string.
            offset: 分页偏移量 (required), int.
            length: 分页条数，上限200 (required), int.
            start_date: 起始日期 (required), string.
            end_date: 结束日期 (required), string.
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            sort_field: 排序字段：asin, string.
            sort_type: desc 倒序 asc 顺序, string."""
        resp = await self._post(
            "/erp/sc/routing/finance/Refund/profitMonthRefund",
            {
                k: v
                for k, v in {
                    "asin_type": asin_type,
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "sid": sid,
                    "sort_field": sort_field,
                    "sort_type": sort_type,
                }.items()
                if v is not None
            },
        )
        return self._parse_page(resp.data, MonthRefundItem)

    async def overseas_aggregate_list(
        self, sys_wid: int = None, start_date: str = None, end_date: str = None
    ) -> list[InventorylogWarehousereportGetoverseasummarylistResponse]:
        """库存报表-海外仓-历史报表-汇总.

        POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList

        Args:
            sys_wid: 领星仓库id，多个用英文逗号分隔, int.
            start_date: 开始时间 (required), string.
            end_date: 结束时间 (required), string."""
        resp = await self._post(
            "/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList",
            {
                k: v
                for k, v in {"sys_wid": sys_wid, "start_date": start_date, "end_date": end_date}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InventorylogWarehousereportGetoverseasummarylistResponse)

    async def overseas_detail_list(
        self, sys_wid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[InventorylogWarehousereportGetoverseadetaillistResponse]:
        """库存报表-海外仓-历史报表-明细.

        POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList

        Args:
            sys_wid: 系统仓库id，多个用英文逗号分隔, int.
            start_date: 开始时间，格式：Y-m-d (required), string.
            end_date: 结束时间，格式：Y-m-d (required), string.
            offset: 分页偏移量，默认0 (required), int.
            length: 每页条数，默认15 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList",
            {
                k: v
                for k, v in {
                    "sys_wid": sys_wid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, InventorylogWarehousereportGetoverseadetaillistResponse)

    async def platform_statistics_sale_stat_page_list_v2(
        self,
        start_date: str = None,
        end_date: str = None,
        result_type: str = None,
        date_unit: str = None,
        page: int = None,
        length: int = None,
        data_type: str = None,
        sids: list = None,
    ) -> list[Platformstatisticsv2SalestatPagelistResponse]:
        """查询销量统计列表v2.

        POST /basicOpen/platformStatisticsV2/saleStat/pageList

        Args:
            start_date: 开始日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            end_date: 结束日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            result_type: 汇总类型：  1 销量  2 订单量  3 销售额 (required), string.
            date_unit: 统计时间指标： 1 年  2 月  3 周  4 日 (required), string.
            page: 分页页码，默认1, int.
            length: 分页大小，默认20, int.
            data_type: 统计数据维度：  1 ASIN  2 父体  3 MSKU  4 SKU  5 SPU  6 店铺 (required), string.
            sids: 店铺id，多个使用英文逗号分隔。 如果id属于亚马逊店铺id，则对应查询亚马逊店铺列表接口对应字段【sid】  如果id属于多平台店铺id，则对应查询多平台店铺信息接口对应字段【store_id】, array."""
        resp = await self._post(
            "/basicOpen/platformStatisticsV2/saleStat/pageList",
            {
                k: v
                for k, v in {
                    "start_date": start_date,
                    "end_date": end_date,
                    "result_type": result_type,
                    "date_unit": date_unit,
                    "page": page,
                    "length": length,
                    "data_type": data_type,
                    "sids": sids,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, Platformstatisticsv2SalestatPagelistResponse)

    async def profit_msku(
        self,
        start_date: str = None,
        end_date: str = None,
        offset: int = None,
        length: int = None,
        sids: str = None,
        currency_type: str = None,
        sort_field: str = None,
        sort_type: str = None,
    ) -> list[FinanceProfitstatisProfitmskuResponse]:
        """查询利润统计（旧）-MSKU.

        POST /erp/sc/routing/finance/ProfitStatis/profitMsku

        Args:
            start_date: 起始日期 (required), string.
            end_date: 起始日期 (required), string.
            offset: 分页偏移量 (required), int.
            length: 分页长度，上限200 (required), int.
            sids: 店铺id，通过逗号分隔可以多选，默认返回全部 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
            currency_type: 币种，默认原币种 1 人民币-CNY 2 美元-USD 3 欧元-EUR 4 日元-JPY 5 澳元-AUD 6 加拿大元-CAD 7 墨西哥比索-MXN 8 英镑-GBP 9 印度卢比-INR 10 阿联酋迪拉姆-AED 11 新加坡元-SGD 12 沙特阿拉伯-SAR 13 巴西-BRL 14 瑞典-SEK 15 波兰-PLN 16 土耳其-TRY, string.
            sort_field: 排序字段：asin, string.
            sort_type: desc:倒序   asc:顺序, string."""
        resp = await self._post(
            "/erp/sc/routing/finance/ProfitStatis/profitMsku",
            {
                k: v
                for k, v in {
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                    "sids": sids,
                    "currency_type": currency_type,
                    "sort_field": sort_field,
                    "sort_type": sort_type,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, FinanceProfitstatisProfitmskuResponse)

    async def purchase_report_buyer_list(
        self,
        offset: int = None,
        length: int = None,
        start_date: str = None,
        end_date: str = None,
        time_type: int = None,
        product_type: list = None,
    ) -> list[PurchaseBuyerListResponse]:
        """查询采购报表列表 - 采购员.

        POST /basicOpen/report/purchase/buyer/list

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int.
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            end_date: 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            time_type: 时间类型：1 下单时间，2 到货时间, int.
            product_type: 产品类型： 1 普通产品 2 组合产品 3 辅料, array."""
        resp = await self._post(
            "/basicOpen/report/purchase/buyer/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "time_type": time_type,
                    "product_type": product_type,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchaseBuyerListResponse)

    async def purchase_report_product_list(
        self,
        offset: int = None,
        length: int = None,
        start_date: str = None,
        end_date: str = None,
        time_type: int = None,
        sids: str = None,
        search_field: str = None,
        search_value: str = None,
    ) -> list[PurchaseProductListResponse]:
        """查询采购报表列表 - 产品.

        POST /basicOpen/report/purchase/product/list

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int.
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            end_date: 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            time_type: 时间类型：1 下单时间，2 到货时间, int.
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
            search_field: 搜索字段名： product_name 品名 sku SKU msku MSKU fnsku FNSKU spu_name 款名 spu SPU, string.
            search_value: 搜索值, string."""
        resp = await self._post(
            "/basicOpen/report/purchase/product/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "time_type": time_type,
                    "sids": sids,
                    "search_field": search_field,
                    "search_value": search_value,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchaseProductListResponse)

    async def purchase_report_supplier_list(
        self,
        offset: int = None,
        length: int = None,
        start_date: str = None,
        end_date: str = None,
        time_type: int = None,
        search_field: str = None,
        search_value: str = None,
        product_type: list = None,
    ) -> list[PurchaseSupplierListResponse]:
        """查询采购报表列表 - 供应商.

        POST /basicOpen/report/purchase/supplier/list

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int.
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            end_date: 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            time_type: 时间类型： 1 下单时间 2 到货时间, int.
            search_field: 搜索字段名： order_no 单据号, string.
            search_value: 搜索值, string.
            product_type: 产品类型： 1 普通产品 2 组合产品 3 辅料, array."""
        resp = await self._post(
            "/basicOpen/report/purchase/supplier/list",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "start_date": start_date,
                    "end_date": end_date,
                    "time_type": time_type,
                    "search_field": search_field,
                    "search_value": search_value,
                    "product_type": product_type,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, PurchaseSupplierListResponse)

    async def reimbursement_list(
        self,
        offset: int = None,
        length: int = None,
        search_field: str = None,
        search_value: str = None,
        sids: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> list[ReimbursementlistResponse]:
        """查询亚马逊赔偿报告列表.

        POST /basicOpen/openapi/mwsReport/reimbursementList

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int.
            search_field: 搜索字段： reimbursement_id 赔偿编号 amazon_order_id 订单号 asin ASIN msku MSKU fnsku FNSKU item_name 标题, string.
            search_value: 搜索值, string.
            sids: 店铺id，多个使用英文逗号分割 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
            start_date: 批准日期开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
            end_date: 批准日期结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string."""
        resp = await self._post(
            "/basicOpen/openapi/mwsReport/reimbursementList",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "search_field": search_field,
                    "search_value": search_value,
                    "sids": sids,
                    "start_date": start_date,
                    "end_date": end_date,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReimbursementlistResponse)

    async def return_order_analysis_lists(
        self,
        endDate: str = None,
        length: int = None,
        offset: int = None,
        startDate: str = None,
        asinType: str = None,
        dateType: int = None,
        mids: list = None,
        principalUid: list = None,
        searchField: str = None,
        searchValue: list = None,
        sortField: str = None,
        sortType: str = None,
        storeId: list = None,
    ) -> list[SalesanalysisReturnorderAnalysislistsResponse]:
        """统计-查询退货分析.

        POST /basicOpen/salesAnalysis/returnOrder/analysisLists

        Args:
            endDate: 结束日期，格式：yyyy-MM-dd，与startDate配合使用，最多支持366天范围, string.
            length: 分页长度，每页数据条数, int.
            offset: 分页偏移量，当前页码, int.
            startDate: 开始日期，格式：yyyy-MM-dd，与endDate配合使用，最多支持366天范围, string.
            asinType: 维度类型，枚举值：msku, asin, parentAsin, sku, spu（注意：不支持sid、country、category、band）, string.
            dateType: 时间类型，枚举值：0-退货时间, 1-下单时间, int.
            mids: 国家ID列表（mid）, array.
            principalUid: 负责人ID列表, array.
            searchField: 搜索字段类型，枚举值：msku-MSKU, asin-ASIN, parentAsin-父ASIN, localSku-SKU, localName-品名, spu-SPU, spuName-款名, string.
            searchValue: 搜索值列表，与searchField配合使用, array.
            sortField: 排序字段，枚举值：curReturnGoodsCount-退货量, returnGoodsCountRatio-退货量环比, curVolume-销量, curReturnGoodsVolumeRatio-退货率, returnGoodsVolumeRatioDiff-退货率环比差异, string.
            sortType: 排序类型，枚举值：ASC-升序, DESC-降序, string.
            storeId: 店铺ID列表, array."""
        resp = await self._post(
            "/basicOpen/salesAnalysis/returnOrder/analysisLists",
            {
                k: v
                for k, v in {
                    "endDate": endDate,
                    "length": length,
                    "offset": offset,
                    "startDate": startDate,
                    "asinType": asinType,
                    "dateType": dateType,
                    "mids": mids,
                    "principalUid": principalUid,
                    "searchField": searchField,
                    "searchValue": searchValue,
                    "sortField": sortField,
                    "sortType": sortType,
                    "storeId": storeId,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SalesanalysisReturnorderAnalysislistsResponse)

    async def store_sales(
        self, sid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[SalesReportSalesResponse]:
        """查询店铺汇总销量.

        POST /erp/sc/data/sales_report/sales

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            start_date: 报表时间，格式：Y-m-d，闭区间 (required), string.
            end_date: 报表时间，格式：Y-m-d，闭区间 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认1000, int."""
        resp = await self._post(
            "/erp/sc/data/sales_report/sales",
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
        return self._parse_list(resp.data, SalesReportSalesResponse)

    async def operate_log_list(
        self,
        sids: list = None,
        search_field: str = None,
        search_value: str = None,
        date_type: str = None,
        start_date: str = None,
        end_date: str = None,
    ) -> list[OperatemanageOperatelogListResponse]:
        """查询运营日志.

        POST /basicOpen/operateManage/operateLog/list

        Args:
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), array.
            search_field: 搜索类型： asin  ASIN parent_asin  父ASIN msku  MSKU (required), string.
            search_value: 搜索值 (required), string.
            date_type: 时间类型： 1  日 2  周 3  月 (required), string.
            start_date: 开始时间，闭区间，格式：Y-m-d (required), string.
            end_date: 结束时间，闭区间，格式：Y-m-d (required), string."""
        resp = await self._post(
            "/basicOpen/operateManage/operateLog/list",
            {
                k: v
                for k, v in {
                    "sids": sids,
                    "search_field": search_field,
                    "search_value": search_value,
                    "date_type": date_type,
                    "start_date": start_date,
                    "end_date": end_date,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, OperatemanageOperatelogListResponse)

    async def operate_log_v2_list(
        self,
        offset: float = None,
        length: float = None,
        sids: list = None,
        mids: list = None,
        start_date: str = None,
        end_date: str = None,
        search_field: str = None,
        search_value: list = None,
        summary_type: str = None,
    ) -> list[OperatemanageOperatelogListResponse]:
        """查询运营日志(新).

        POST /basicOpen/operateManage/operateLog/list/v2

        Args:
            offset: 分页偏移量，默认为20, number.
            length: 分页长度，默认为200, number.
            sids: 店铺列表, array.
            mids: 国家列表, array.
            start_date: 开始时间，格式：yyyy-mm-dd (required), string.
            end_date: 结束时间，格式：yyyy-mm-dd (required), string.
            search_field: 搜索条件： asin ASIN parent_asin 父ASIN msku MSKU【默认】, string.
            search_value: 搜索值, array.
            summary_type: 日志维度： asin ASIN parent_asin 父ASIN msku MSKU (required), string."""
        resp = await self._post(
            "/basicOpen/operateManage/operateLog/list/v2",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "sids": sids,
                    "mids": mids,
                    "start_date": start_date,
                    "end_date": end_date,
                    "search_field": search_field,
                    "search_value": search_value,
                    "summary_type": summary_type,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, OperatemanageOperatelogListResponse)

    async def performance_trend_by_hour(
        self,
        sids: str = None,
        date_start: str = None,
        date_end: str = None,
        summary_field: str = None,
        summary_field_value: str = None,
    ) -> list[SalesanalysisProductperformancePerformancetrendbyhourResponse]:
        """查询asin360小时数据.

        POST /basicOpen/salesAnalysis/productPerformance/performanceTrendByHour

        Args:
            sids: 店铺id，多个值使用英文逗号隔开，最大上限为200 (required), string.
            date_start: 开始时间，闭区间，格式：Y-m-d (required), string.
            date_end: 结束时间，闭区间，格式：Y-m-d (required), string.
            summary_field: 查询维度： parent_asin asin msku sku spu (required), string.
            summary_field_value: 查询维度值 (required), string."""
        resp = await self._post(
            "/basicOpen/salesAnalysis/productPerformance/performanceTrendByHour",
            {
                k: v
                for k, v in {
                    "sids": sids,
                    "date_start": date_start,
                    "date_end": date_end,
                    "summary_field": summary_field,
                    "summary_field_value": summary_field_value,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SalesanalysisProductperformancePerformancetrendbyhourResponse)

    async def report_create_report_export_task(
        self,
        seller_id: str = None,
        report_type: str = None,
        data_start_time: str = None,
        data_end_time: str = None,
        marketplace_ids: list = None,
        region: str = None,
    ) -> ReportCreateReportexporttaskResponse | None:
        """报告导出 - 创建导出任务.

        POST /basicOpen/report/create/reportExportTask

        Args:
            seller_id: 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】 (required), string.
            report_type: 亚马逊报表类型【具体类型参看下方附加说明】 (required), string.
            data_start_time: 亚马逊报表请求开始时间，时间格式：YYYY-MM-DDTHH:MM:SSZ, string.
            data_end_time: 亚马逊报表请求结束时间，时间格式：YYYY-MM-DDTHH:MM:SSZ, string.
            marketplace_ids: 亚马逊市场id (required), array.
            region: 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东 (required), string."""
        resp = await self._post(
            "/basicOpen/report/create/reportExportTask",
            {
                k: v
                for k, v in {
                    "seller_id": seller_id,
                    "report_type": report_type,
                    "data_start_time": data_start_time,
                    "data_end_time": data_end_time,
                    "marketplace_ids": marketplace_ids,
                    "region": region,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, ReportCreateReportexporttaskResponse)

    async def report_query_report_export_task(
        self, seller_id: str = None, task_id: str = None, region: str = None
    ) -> ReportQueryReportexporttaskResponse | None:
        """报告导出-查询导出任务结果.

        POST /basicOpen/report/query/reportExportTask

        Args:
            seller_id: 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】 (required), string.
            task_id: 任务id (required), string.
            region: 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东 (required), string."""
        resp = await self._post(
            "/basicOpen/report/query/reportExportTask",
            {k: v for k, v in {"seller_id": seller_id, "task_id": task_id, "region": region}.items() if v is not None},
        )
        return self._parse_one(resp.data, ReportQueryReportexporttaskResponse)

    async def vc_inventory_list(
        self,
        sid: float = None,
        startDate: str = None,
        endDate: str = None,
        offset: float = None,
        length: float = None,
        view: str = None,
        asinList: list = None,
    ) -> list[ReportInventoryListResponse]:
        """VC报表-库存报表.

        POST /basicOpen/vc/report/inventory/list

        Args:
            sid: 店铺id (required), number.
            startDate: 开始时间，格式：`yyyy-MM-dd`, string.
            endDate: 结束时间，格式：`yyyy-MM-dd`, string.
            offset: 偏移量 (required), number.
            length: 长度，最大 `200` (required), number.
            view: 视图： `sourcing` 货源视图 `manufacturing` 生产视图 (required), string.
            asinList: 指定asin列表, array."""
        resp = await self._post(
            "/basicOpen/vc/report/inventory/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "startDate": startDate,
                    "endDate": endDate,
                    "offset": offset,
                    "length": length,
                    "view": view,
                    "asinList": asinList,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReportInventoryListResponse)

    async def vc_nppm_list(
        self,
        sid: int = None,
        startDate: str = None,
        endDate: str = None,
        offset: int = None,
        length: int = None,
        asinList: list = None,
    ) -> list[ReportNppmListResponse]:
        """VC报表-产品利润率报表.

        POST /basicOpen/vc/report/nppm/list

        Args:
            sid: 店铺id (required), long.
            startDate: 开始日期，yyyy-MM-dd, string.
            endDate: 结束日期，yyyy-MM-dd, string.
            offset: 偏移量，默认0 (required), int.
            length: 长度，最大200 (required), int.
            asinList: 指定asin列表, array."""
        resp = await self._post(
            "/basicOpen/vc/report/nppm/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "startDate": startDate,
                    "endDate": endDate,
                    "offset": offset,
                    "length": length,
                    "asinList": asinList,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReportNppmListResponse)

    async def vc_realtime_sales_list(
        self,
        sid: int = None,
        offset: int = None,
        length: int = None,
        startDate: str = None,
        endDate: str = None,
        dateType: int = None,
        asinList: list = None,
    ) -> list[ReportRealtimesalesListResponse]:
        """VC报表-实时销量报表.

        POST /basicOpen/vc/report/realtimeSales/list

        Args:
            sid: 店铺id (required), long.
            offset: 分页偏移量，默认0 (required), int.
            length: 分页长度，默认20，最大200 (required), int.
            startDate: 开始时间，yyyy-MM-dd, string.
            endDate: 结束时间，yyyy-MM-dd, string.
            dateType: 日期类型： 1=站点时间 2=UTC时间 默认1, int.
            asinList: 指定asin列表, array."""
        resp = await self._post(
            "/basicOpen/vc/report/realtimeSales/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "offset": offset,
                    "length": length,
                    "startDate": startDate,
                    "endDate": endDate,
                    "dateType": dateType,
                    "asinList": asinList,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReportRealtimesalesListResponse)

    async def vc_sales_list(
        self,
        sid: int = None,
        view: str = None,
        offset: int = None,
        length: int = None,
        startDate: str = None,
        endDate: str = None,
        asinList: list = None,
    ) -> list[ReportSalesListResponse]:
        """VC报表-销量报表.

        POST /basicOpen/vc/report/sales/list

        Args:
            sid: 店铺id (required), long.
            view: 视图： sourcing manufacturing (required), string.
            offset: 分页偏移量，默认0 (required), int.
            length: 分页长度，默认20，最大200 (required), int.
            startDate: 开始时间，yyyy-MM-dd, string.
            endDate: 结束时间，yyyy-MM-dd, string.
            asinList: 指定asin列表, array."""
        resp = await self._post(
            "/basicOpen/vc/report/sales/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "view": view,
                    "offset": offset,
                    "length": length,
                    "startDate": startDate,
                    "endDate": endDate,
                    "asinList": asinList,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReportSalesListResponse)

    async def vc_traffic_list(
        self,
        sid: int = None,
        startDate: str = None,
        endDate: str = None,
        offset: int = None,
        length: int = None,
        asinList: list = None,
    ) -> list[ReportTrafficListResponse]:
        """VC报表-流量报表.

        POST /basicOpen/vc/report/traffic/list

        Args:
            sid: 店铺id (required), long.
            startDate: 开始日期，yyyy-MM-dd, string.
            endDate: 结束日期，yyyy-MM-dd, string.
            offset: 偏移量，默认0 (required), int.
            length: 长度，最大200 (required), int.
            asinList: 指定asin列表, array."""
        resp = await self._post(
            "/basicOpen/vc/report/traffic/list",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "startDate": startDate,
                    "endDate": endDate,
                    "offset": offset,
                    "length": length,
                    "asinList": asinList,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReportTrafficListResponse)

    async def product_performance(
        self,
        offset: int,
        length: int,
        sort_field: str,
        sort_type: str,
        sid: str | list,
        start_date: str,
        end_date: str,
        summary_field: str,
        search_field: str = None,
        search_value: list = None,
        mid: int = None,
        currency_code: str = None,
        is_recently_enum: bool = None,
        purchase_status: int = None,
        extend_search: dict = None,
    ) -> list[ProductperformanceOpenapiAsinlistResponse]:
        """查询产品表现.

        POST /bd/productPerformance/openApi/asinList

        Args:
            offset: 分页偏移量, int.
            length: 分页长度，最大10000, int.
            sort_field: 排序字段，默认volume, str.
            sort_type: 排序方式：desc/asc, str.
            sid: 店铺id，单店铺传字符串，多店铺传数组, str | list.
            start_date: 开始日期 YYYY-MM-DD, str.
            end_date: 结束日期 YYYY-MM-DD, str.
            summary_field: 汇总维度：asin/parent_asin/msku/sku, str.
            search_field: 搜索字段：asin/parent_asin/msku/local_sku/item_name, str.
            search_value: 搜索值，最多50个, list.
            mid: 站点id, int.
            currency_code: 货币类型，不传原币种，支持USD/CNY, str.
            is_recently_enum: 是否仅查询活跃商品, bool.
            purchase_status: 退货退款统计方式：0按发生时间/1按下单时间, int.
            extend_search: 扩展筛选条件, dict.

        Note:
            时间范围不能超过92天。单店铺间隔1s，多店铺间隔10s。"""
        resp = await self._post(
            "/bd/productPerformance/openApi/asinList",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "sort_field": sort_field,
                    "sort_type": sort_type,
                    "sid": sid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "summary_field": summary_field,
                    "search_field": search_field,
                    "search_value": search_value,
                    "mid": mid,
                    "currency_code": currency_code,
                    "is_recently_enum": is_recently_enum,
                    "purchase_status": purchase_status,
                    "extend_search": extend_search,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ProductperformanceOpenapiAsinlistResponse)

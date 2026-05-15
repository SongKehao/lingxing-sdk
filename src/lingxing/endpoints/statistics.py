"""Auto-generated StatisticsEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class StatisticsEndpoints:
    """领星API - StatisticsEndpoints (30个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def amazon_report_export_task(self, **kwargs) -> dict:
        """AmazonReportExportTask.
        
        POST /basicOpen/report/amazonReportExportTask
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/amazonReportExportTask",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def asin_daily_lists(self, **kwargs) -> dict:
        """AsinDailyLists.
        
        POST /erp/sc/data/sales_report/asinDailyLists
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/sales_report/asinDailyLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def asin_list(self, **kwargs) -> dict:
        """AsinList.
        
        POST /erp/sc/data/sales_report/asinList
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/sales_report/asinList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def create_removal_order(self, **kwargs) -> dict:
        """CreateRemovalOrder.
        
        POST /erp/sc/statistic/removalOrder/createAndCommit
        """
        return await self._request_with_token(
            route_name="/erp/sc/statistic/removalOrder/createAndCommit",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbastorage_fee_long_term(self, **kwargs) -> dict:
        """FBAStorageFeeLongTerm.
        
        POST /erp/sc/data/fba_report/storageFeeLongTerm
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/storageFeeLongTerm",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbastorage_fee_month(self, **kwargs) -> dict:
        """FBAStorageFeeMonth.
        
        POST /erp/sc/data/fba_report/storageFeeMonth
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/fba_report/storageFeeMonth",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fba_stock_report_list(self, **kwargs) -> dict:
        """FbaStockReportList.
        
        POST /erp/sc/routing/fba/fbaStockReport/getList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/fba/fbaStockReport/getList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def local_aggregate_list(self, **kwargs) -> dict:
        """LocalAggregateList.
        
        POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def local_detail_list(self, **kwargs) -> dict:
        """LocalDetailList.
        
        POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def month_refund(self, **kwargs) -> dict:
        """MonthRefund.
        
        POST /erp/sc/routing/finance/Refund/profitMonthRefund
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/Refund/profitMonthRefund",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def overseas_aggregate_list(self, **kwargs) -> dict:
        """OverseasAggregateList.
        
        POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def overseas_detail_list(self, **kwargs) -> dict:
        """OverseasDetailList.
        
        POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def platform_statistics_sale_stat_page_list_v2(self, **kwargs) -> dict:
        """PlatformStatisticsSaleStatPageListV2.
        
        POST /basicOpen/platformStatisticsV2/saleStat/pageList
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformStatisticsV2/saleStat/pageList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def profit_msku(self, **kwargs) -> dict:
        """ProfitMsku.
        
        POST /erp/sc/routing/finance/ProfitStatis/profitMsku
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/finance/ProfitStatis/profitMsku",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_report_buyer_list(self, **kwargs) -> dict:
        """PurchaseReportBuyerList.
        
        POST /basicOpen/report/purchase/buyer/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/purchase/buyer/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_report_product_list(self, **kwargs) -> dict:
        """PurchaseReportProductList.
        
        POST /basicOpen/report/purchase/product/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/purchase/product/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def purchase_report_supplier_list(self, **kwargs) -> dict:
        """PurchaseReportSupplierList.
        
        POST /basicOpen/report/purchase/supplier/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/purchase/supplier/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def reimbursement_list(self, **kwargs) -> dict:
        """ReimbursementList.
        
        POST /basicOpen/openapi/mwsReport/reimbursementList
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/mwsReport/reimbursementList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def return_order_analysis_lists(self, **kwargs) -> dict:
        """ReturnOrderAnalysisLists.
        
        POST /basicOpen/salesAnalysis/returnOrder/analysisLists
        """
        return await self._request_with_token(
            route_name="/basicOpen/salesAnalysis/returnOrder/analysisLists",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def store_sales(self, **kwargs) -> dict:
        """StoreSales.
        
        POST /erp/sc/data/sales_report/sales
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/sales_report/sales",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def operate_log_list(self, **kwargs) -> dict:
        """operateLogList.
        
        POST /basicOpen/operateManage/operateLog/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/operateManage/operateLog/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def operate_log_v2list(self, **kwargs) -> dict:
        """operateLogV2List.
        
        POST /basicOpen/operateManage/operateLog/list/v2
        """
        return await self._request_with_token(
            route_name="/basicOpen/operateManage/operateLog/list/v2",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def performance_trend_by_hour(self, **kwargs) -> dict:
        """performanceTrendByHour.
        
        POST /basicOpen/salesAnalysis/productPerformance/performanceTrendByHour
        """
        return await self._request_with_token(
            route_name="/basicOpen/salesAnalysis/productPerformance/performanceTrendByHour",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def report_create_report_export_task(self, **kwargs) -> dict:
        """reportCreateReportExportTask.
        
        POST /basicOpen/report/create/reportExportTask
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/create/reportExportTask",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def report_query_report_export_task(self, **kwargs) -> dict:
        """reportQueryReportExportTask.
        
        POST /basicOpen/report/query/reportExportTask
        """
        return await self._request_with_token(
            route_name="/basicOpen/report/query/reportExportTask",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_inventory_list(self, **kwargs) -> dict:
        """vcInventoryList.
        
        POST /basicOpen/vc/report/inventory/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/vc/report/inventory/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_nppm_list(self, **kwargs) -> dict:
        """vcNppmList.
        
        POST /basicOpen/vc/report/nppm/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/vc/report/nppm/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_realtime_sales_list(self, **kwargs) -> dict:
        """vcRealtimeSalesList.
        
        POST /basicOpen/vc/report/realtimeSales/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/vc/report/realtimeSales/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_sales_list(self, **kwargs) -> dict:
        """vcSalesList.
        
        POST /basicOpen/vc/report/sales/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/vc/report/sales/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def vc_traffic_list(self, **kwargs) -> dict:
        """vcTrafficList.
        
        POST /basicOpen/vc/report/traffic/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/vc/report/traffic/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

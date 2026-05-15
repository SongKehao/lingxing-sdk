"""统计报表 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class StatisticsEndpoints(BaseEndpoint):
    """领星统计报表 API (30个接口)."""

    async def amazon_report_export_task(self, **kwargs) -> list | dict:
        """AmazonReportExportTask. POST /basicOpen/report/amazonReportExportTask"""
        resp = await self._post("/basicOpen/report/amazonReportExportTask", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def asin_daily_lists(self, **kwargs) -> list | dict:
        """AsinDailyLists. POST /erp/sc/data/sales_report/asinDailyLists"""
        resp = await self._post("/erp/sc/data/sales_report/asinDailyLists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def asin_list(self, **kwargs) -> list | dict:
        """AsinList. POST /erp/sc/data/sales_report/asinList"""
        resp = await self._post("/erp/sc/data/sales_report/asinList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_removal_order(self, **kwargs) -> dict:
        """CreateRemovalOrder. POST /erp/sc/statistic/removalOrder/createAndCommit"""
        resp = await self._post("/erp/sc/statistic/removalOrder/createAndCommit", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_storage_fee_long_term(self, **kwargs) -> list | dict:
        """FBAStorageFeeLongTerm. POST /erp/sc/data/fba_report/storageFeeLongTerm"""
        resp = await self._post("/erp/sc/data/fba_report/storageFeeLongTerm", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_storage_fee_month(self, **kwargs) -> list | dict:
        """FBAStorageFeeMonth. POST /erp/sc/data/fba_report/storageFeeMonth"""
        resp = await self._post("/erp/sc/data/fba_report/storageFeeMonth", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_stock_report_list(self, **kwargs) -> list | dict:
        """FbaStockReportList. POST /erp/sc/routing/fba/fbaStockReport/getList"""
        resp = await self._post("/erp/sc/routing/fba/fbaStockReport/getList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def local_aggregate_list(self, **kwargs) -> list | dict:
        """LocalAggregateList. POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList"""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def local_detail_list(self, **kwargs) -> list | dict:
        """LocalDetailList. POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList"""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def month_refund(self, **kwargs) -> list | dict:
        """MonthRefund. POST /erp/sc/routing/finance/Refund/profitMonthRefund"""
        resp = await self._post("/erp/sc/routing/finance/Refund/profitMonthRefund", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def overseas_aggregate_list(self, **kwargs) -> list | dict:
        """OverseasAggregateList. POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList"""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def overseas_detail_list(self, **kwargs) -> list | dict:
        """OverseasDetailList. POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList"""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def platform_statistics_sale_stat_page_list_v2(self, **kwargs) -> list | dict:
        """PlatformStatisticsSaleStatPageListV2. POST /basicOpen/platformStatisticsV2/saleStat/pageList"""
        resp = await self._post("/basicOpen/platformStatisticsV2/saleStat/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_msku(self, **kwargs) -> list | dict:
        """ProfitMsku. POST /erp/sc/routing/finance/ProfitStatis/profitMsku"""
        resp = await self._post("/erp/sc/routing/finance/ProfitStatis/profitMsku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_report_buyer_list(self, **kwargs) -> list | dict:
        """PurchaseReportBuyerList. POST /basicOpen/report/purchase/buyer/list"""
        resp = await self._post("/basicOpen/report/purchase/buyer/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_report_product_list(self, **kwargs) -> list | dict:
        """PurchaseReportProductList. POST /basicOpen/report/purchase/product/list"""
        resp = await self._post("/basicOpen/report/purchase/product/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_report_supplier_list(self, **kwargs) -> list | dict:
        """PurchaseReportSupplierList. POST /basicOpen/report/purchase/supplier/list"""
        resp = await self._post("/basicOpen/report/purchase/supplier/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def reimbursement_list(self, **kwargs) -> list | dict:
        """ReimbursementList. POST /basicOpen/openapi/mwsReport/reimbursementList"""
        resp = await self._post("/basicOpen/openapi/mwsReport/reimbursementList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def return_order_analysis_lists(self, **kwargs) -> list | dict:
        """ReturnOrderAnalysisLists. POST /basicOpen/salesAnalysis/returnOrder/analysisLists"""
        resp = await self._post("/basicOpen/salesAnalysis/returnOrder/analysisLists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def store_sales(self, **kwargs) -> list | dict:
        """StoreSales. POST /erp/sc/data/sales_report/sales"""
        resp = await self._post("/erp/sc/data/sales_report/sales", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def operate_log_list(self, **kwargs) -> list | dict:
        """operateLogList. POST /basicOpen/operateManage/operateLog/list"""
        resp = await self._post("/basicOpen/operateManage/operateLog/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def operate_log_v2_list(self, **kwargs) -> list | dict:
        """operateLogV2List. POST /basicOpen/operateManage/operateLog/list/v2"""
        resp = await self._post("/basicOpen/operateManage/operateLog/list/v2", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def performance_trend_by_hour(self, **kwargs) -> list | dict:
        """performanceTrendByHour. POST /basicOpen/salesAnalysis/productPerformance/performanceTrendByHour"""
        resp = await self._post("/basicOpen/salesAnalysis/productPerformance/performanceTrendByHour", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def report_create_report_export_task(self, **kwargs) -> dict:
        """reportCreateReportExportTask. POST /basicOpen/report/create/reportExportTask"""
        resp = await self._post("/basicOpen/report/create/reportExportTask", kwargs if kwargs else None)
        return resp.data or {}
    async def report_query_report_export_task(self, **kwargs) -> list | dict:
        """reportQueryReportExportTask. POST /basicOpen/report/query/reportExportTask"""
        resp = await self._post("/basicOpen/report/query/reportExportTask", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_inventory_list(self, **kwargs) -> list | dict:
        """vcInventoryList. POST /basicOpen/vc/report/inventory/list"""
        resp = await self._post("/basicOpen/vc/report/inventory/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_nppm_list(self, **kwargs) -> list | dict:
        """vcNppmList. POST /basicOpen/vc/report/nppm/list"""
        resp = await self._post("/basicOpen/vc/report/nppm/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_realtime_sales_list(self, **kwargs) -> list | dict:
        """vcRealtimeSalesList. POST /basicOpen/vc/report/realtimeSales/list"""
        resp = await self._post("/basicOpen/vc/report/realtimeSales/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_sales_list(self, **kwargs) -> list | dict:
        """vcSalesList. POST /basicOpen/vc/report/sales/list"""
        resp = await self._post("/basicOpen/vc/report/sales/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_traffic_list(self, **kwargs) -> list | dict:
        """vcTrafficList. POST /basicOpen/vc/report/traffic/list"""
        resp = await self._post("/basicOpen/vc/report/traffic/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

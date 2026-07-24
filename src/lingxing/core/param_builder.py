"""领星ERP API参数构建器 - 填充默认请求参数"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Any, ClassVar

logger = logging.getLogger(__name__)

DEFAULT_SIDS = [4661, 109]


class APIParamBuilder:
    """根据API路径和参数定义填充默认请求参数"""

    def __init__(self, default_sids: list[int] | None = None):
        self.default_sids = default_sids or DEFAULT_SIDS

    def build_params(  # noqa: PLR0912
        self,
        api_path: str,
        params: dict[str, Any],
        param_names: set[str],
    ) -> dict[str, Any]:
        body = dict(params)

        self._fill_common_pagination(body, param_names)
        self._fill_common_dates(body, param_names, api_path)
        self._fill_common_stores(body, param_names, api_path)

        # 结算中心API
        if "/settlement/" in api_path:
            if "dateType" not in body:
                body["dateType"] = 1
            if "/transaction/detail/" in api_path:
                if "startDate" not in body and "gmtModifiedStart" not in body:
                    body["startDate"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
                if "endDate" not in body and "gmtModifiedEnd" not in body:
                    body["endDate"] = datetime.now().strftime("%Y-%m-%d")

        # 请款单/请款池API
        if "/requestFunds/" in api_path or "/requestFundsPool/" in api_path:
            body = self._build_request_funds_params(api_path, body, param_names)

        # 应收报告API
        if "/monthly/receivable/" in api_path:
            body = self._build_receivable_params(api_path, body, param_names)

        # 利润报表API
        if "/profit/report/" in api_path:
            body = self._build_profit_report_params(api_path, body, param_names)

        # 广告发票API
        if "/ads/invoice/" in api_path:
            body = self._build_ads_invoice_params(api_path, body, param_names)

        # 客服API
        if "/customerService/" in api_path or "/cs/" in api_path or "/crm/" in api_path:
            body = self._build_customer_service_params(api_path, body, param_names)

        # 统计类API
        if "/profit/statistics/" in api_path or "/productPerformance/" in api_path:
            body = self._build_statistics_params(api_path, body, param_names)

        # 多平台API
        if "/multiplatform/" in api_path or "/pb/mp/" in api_path:
            body = self._build_multiplatform_params(api_path, body, param_names)

        # 亚马逊源表数据API
        if "/mws_report/" in api_path or "/mwsreport/" in api_path:
            body = self._build_mws_report_params(api_path, body, param_names)

        # 补货建议API
        if "/fbaSug/" in api_path or "/restocking/" in api_path:
            body = self._build_restocking_params(api_path, body, param_names)

        # VC类API
        if "/vcOrder/" in api_path or "/vcListing/" in api_path or "/vcSeller/" in api_path:
            body = self._build_vc_params(api_path, body, param_names)

        return body

    def _fill_common_pagination(self, body: dict, param_names: set[str]) -> None:
        if "offset" in param_names and "offset" not in body:
            body["offset"] = 0
        if "length" in param_names and "length" not in body:
            body["length"] = 100
        if "page" in param_names and "page" not in body:
            body["page"] = 1
        if "pageSize" in param_names and "pageSize" not in body:
            body["pageSize"] = 100
        if "pageNum" in param_names and "pageNum" not in body:
            body["pageNum"] = 1

    def _fill_common_dates(self, body: dict, param_names: set[str], api_path: str) -> None:
        _week = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        _today = datetime.now().strftime("%Y-%m-%d")
        _month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")

        if "startDate" in param_names and "startDate" not in body:
            body["startDate"] = _week
        if "endDate" in param_names and "endDate" not in body:
            body["endDate"] = _today
        if "start_date" in param_names and "start_date" not in body:
            body["start_date"] = _week
        if "end_date" in param_names and "end_date" not in body:
            body["end_date"] = _today

        if "startTime" in param_names or "start_time" in param_names:
            key = "startTime" if "startTime" in param_names else "start_time"
            if key not in body:
                body[key] = (
                    _month
                    if "/rmaManage/" in api_path or "/otherFee/" in api_path
                    else (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
                )

        if "endTime" in param_names or "end_time" in param_names:
            key = "endTime" if "endTime" in param_names else "end_time"
            if key not in body:
                body[key] = (
                    _today
                    if "/rmaManage/" in api_path or "/otherFee/" in api_path
                    else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )

    def _fill_common_stores(self, body: dict, param_names: set[str], api_path: str) -> None:
        if "sids" in param_names and "sids" not in body:
            if "/storeTarget/" in api_path:
                body["sids"] = ",".join(map(str, self.default_sids))
            elif "/service/v3/data/mws/reviews" in api_path:
                body["sids"] = str(self.default_sids[0])
            elif "/voiceOfBuyer/" in api_path:
                body["sids"] = self.default_sids[0]
            else:
                body["sids"] = self.default_sids
        elif "sid_list" in param_names and "sid_list" not in body:
            body["sid_list"] = self.default_sids
        elif "sid" in param_names and "sid" not in body:
            if "/fba/" in api_path:
                body["sid"] = str(self.default_sids[0])
            else:
                body["sid"] = self.default_sids[0]

    def _build_request_funds_params(  # noqa: PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建请款单/请款池API参数"""
        # 物流请款
        if "/logistics/" in api_path or "/customFee/" in api_path:
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "create_time"
            if "start_time" in param_names and "start_time" not in body:
                body["start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_time" in param_names and "end_time" not in body:
                body["end_time"] = datetime.now().strftime("%Y-%m-%d")
        # 其他费用 - camelCase
        elif "/otherFee/list" in api_path:
            if "startTime" in param_names and "startTime" not in body:
                body["startTime"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "endTime" in param_names and "endTime" not in body:
                body["endTime"] = datetime.now().strftime("%Y-%m-%d")
            if "searchFieldTime" in param_names and "searchFieldTime" not in body:
                body["searchFieldTime"] = "create_time"
        # 货款预付款、货款现结
        elif "/prepay/" in api_path or "/purchase/" in api_path or "/inbound/" in api_path:
            if "time_field" in param_names and "time_field" not in body:
                body["time_field"] = "create_time"
            if "start_time" in param_names and "start_time" not in body:
                body["start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_time" in param_names and "end_time" not in body:
                body["end_time"] = datetime.now().strftime("%Y-%m-%d")
        # 请款单列表
        elif "/order/list" in api_path:
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "apply_time"
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
        # 通用处理
        else:
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "apply_time"
            if "start_date" not in body and "startDate" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" not in body and "endDate" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")

        return body

    def _build_receivable_params(self, api_path: str, body: dict[str, Any], param_names: set[str]) -> dict[str, Any]:
        """构建应收报告API参数"""
        # 结算月格式 - YYYY-MM
        if "settleMonth" in param_names and "settleMonth" not in body:
            body["settleMonth"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m")
        elif "settlement_month" in param_names and "settlement_month" not in body:
            body["settlement_month"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m")

        # 币种
        if "currencyCode" in param_names and "currencyCode" not in body:
            body["currencyCode"] = "USD"
        elif "currency" in param_names and "currency" not in body:
            body["currency"] = "CNY"

        return body

    def _build_profit_report_params(self, api_path: str, body: dict[str, Any], param_names: set[str]) -> dict[str, Any]:
        """构建利润报表API参数"""
        # 订单维度报表使用 snake_case
        if "/order/list" in api_path:
            if "search_date_field" in param_names and "search_date_field" not in body:
                body["search_date_field"] = "fund_transfer_datetime_locale"
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
        else:
            # 其他利润报表使用 camelCase
            if "startDate" not in body:
                body["startDate"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            if "endDate" not in body:
                body["endDate"] = datetime.now().strftime("%Y-%m-%d")

        # 店铺参数
        if "sids" not in body and "sid" not in body:
            body["sids"] = self.default_sids

        # 币种参数
        if "currencyCode" in param_names and "currencyCode" not in body:
            body["currencyCode"] = "CNY"

        return body

    def _build_ads_invoice_params(self, api_path: str, body: dict[str, Any], param_names: set[str]) -> dict[str, Any]:
        """构建广告发票API参数"""
        # 广告发票列表
        if "/invoice/list" in api_path:
            if "invoice_start_time" in param_names and "invoice_start_time" not in body:
                body["invoice_start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "invoice_end_time" in param_names and "invoice_end_time" not in body:
                body["invoice_end_time"] = datetime.now().strftime("%Y-%m-%d")
            if "sids" in param_names and "sids" not in body:
                body["sids"] = self.default_sids
        # 发票活动列表
        elif "/invoice/campaign/list" in api_path or "/invoice/detail" in api_path:
            if "invoice_id" in param_names and "invoice_id" not in body:
                body["invoice_id"] = ""  # 需要从发票列表获取
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
        else:
            # 通用处理
            if "invoice_start_time" in param_names and "invoice_start_time" not in body:
                body["invoice_start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "invoice_end_time" in param_names and "invoice_end_time" not in body:
                body["invoice_end_time"] = datetime.now().strftime("%Y-%m-%d")

        return body

    def _build_customer_service_params(  # noqa: PLR0915,PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建客服API参数"""
        # RMA管理API
        if "/rmaManage/" in api_path:
            if "searchTimeFiled" in param_names and "searchTimeFiled" not in body:
                body["searchTimeFiled"] = "operationTime"
            if "searchField" in param_names and "searchField" not in body:
                body["searchField"] = "msku"
            if "searchValue" in param_names and "searchValue" not in body:
                body["searchValue"] = ["PEE-618"]
            if "sortColumn" in param_names and "sortColumn" not in body:
                body["sortColumn"] = "operationTime"
            if "sortType" in param_names and "sortType" not in body:
                body["sortType"] = "desc"
            if "pageNum" in param_names and "pageNum" not in body:
                body["pageNum"] = 1
            if "pageSize" in param_names and "pageSize" not in body:
                body["pageSize"] = 20

        # 业绩通知列表API
        elif "/performanceNotice/" in api_path:
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "status" in param_names and "status" not in body:
                body["status"] = [0, 1]

        # 客户列表(新)API
        elif "/crm/customer/index" in api_path:
            if "sids" in param_names and "sids" not in body:
                body["sids"] = str(self.default_sids[0])
            if "date_field" in param_names and "date_field" not in body:
                body["date_field"] = "first_purchase_date"

        # 店铺绩效列表API
        elif "/storeTarget/list" in api_path:
            if "sids" in param_names and "sids" not in body:
                body["sids"] = ",".join(map(str, self.default_sids))
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "pull_date"
            if "search_time" in param_names and "search_time" not in body:
                body["search_time"] = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 店铺绩效详情API
        elif "/storeTarget/detail" in api_path:
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "pullDate" in param_names and "pullDate" not in body:
                body["pullDate"] = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 买家之声API
        elif "/voiceOfBuyer/" in api_path:
            if "sids" in param_names and "sids" not in body:
                body["sids"] = self.default_sids[0]
            if "fulfillment_channel" in param_names and "fulfillment_channel" not in body:
                body["fulfillment_channel"] = "FBA"
            if "search_field" in param_names and "search_field" not in body:
                body["search_field"] = "msku"

        # 售后工单API
        elif "/workOrder/" in api_path:
            if "date_type" in param_names and "date_type" not in body:
                body["date_type"] = "create_time"
            if "start_time" in param_names and "start_time" not in body:
                body["start_time"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
            if "end_time" in param_names and "end_time" not in body:
                body["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 评价管理 Review(新) API
        elif "/service/v3/data/mws/reviews" in api_path:
            if "date_field" in param_names and "date_field" not in body:
                body["date_field"] = "review_time"
            if "search_field" in param_names and "search_field" not in body:
                body["search_field"] = "amazon_order_id"

        return body

    def _build_statistics_params(  # noqa: PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建统计类API参数"""
        # 利润统计API - camelCase
        if "/profit/statistics/open/" in api_path:
            if "startDate" not in body:
                body["startDate"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            if "endDate" not in body:
                body["endDate"] = datetime.now().strftime("%Y-%m-%d")
            if "sids" not in body and "sid" not in body:
                body["sids"] = self.default_sids
            if "currencyCode" in param_names and "currencyCode" not in body:
                body["currencyCode"] = "CNY"

        # 订单利润API
        elif "/basicOpen/finance/mreport/OrderProfit" in api_path:
            if "startDate" not in body:
                body["startDate"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            if "endDate" not in body:
                body["endDate"] = datetime.now().strftime("%Y-%m-%d")
            if "sids" not in body:
                body["sids"] = self.default_sids
            if "currencyCode" in param_names and "currencyCode" not in body:
                body["currencyCode"] = "CNY"

        # 产品表现API - snake_case
        elif "/productPerformance/openApi/asinList" in api_path:
            if "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            if "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
            if "sid" not in body and "sids" not in body:
                body["sid"] = self.default_sids[0]
            if "summary_field" in param_names and "summary_field" not in body:
                body["summary_field"] = "asin"
            if "currency_code" in param_names and "currency_code" not in body:
                body["currency_code"] = "CNY"

        # ASIN360小时数据API
        elif "/salesAnalysis/productPerformance/performanceTrendByHour" in api_path:
            if "sids" not in body:
                body["sids"] = ",".join(map(str, self.default_sids))
            if "date_start" not in body:
                body["date_start"] = datetime.now().strftime("%Y-%m-%d")
            if "date_end" not in body:
                body["date_end"] = datetime.now().strftime("%Y-%m-%d")
            if "summary_field" not in body:
                body["summary_field"] = "spu"

        return body

    # Dispatch table for multiplatform API params
    _MULTIPLATFORM_DISPATCH: ClassVar[dict[str, str]] = {
        "/shop/v2/getSellerList": "_mp_seller_list",
        "/listing/v2/getPairList": "_mp_pair_list",
        "/pb/mp/order/v2/list": "_mp_order_list",
        "/newPlatformOrder/list": "_mp_new_platform_order",
        "/queryWFSInventionPage": "_mp_wfs_inventory",
        "/queryWFSCargoPage": "_mp_wfs_cargo",
        "/multiplatform/temu/list": "_mp_temu",
        "/multiplatform/shopify/variantList": "_mp_shopify",
        "/queryShippingListPage": "_mp_shipping",
    }

    def _build_multiplatform_params(self, api_path: str, body: dict[str, Any], param_names: set[str]) -> dict[str, Any]:
        """构建多平台API参数"""
        for key, method_name in self._MULTIPLATFORM_DISPATCH.items():
            if key in api_path:
                getattr(self, method_name)(body, param_names, api_path)
                break
        return body

    def _mp_seller_list(self, body: dict, param_names: set[str], api_path: str) -> None:
        body.setdefault("offset", 0)
        body.setdefault("length", 200)

    def _mp_pair_list(self, body: dict, param_names: set[str], api_path: str) -> None:
        body.setdefault("offset", 0)
        body.setdefault("length", 20)
        if "start_time" in param_names and "start_time" not in body:
            body["start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
        if "end_time" in param_names and "end_time" not in body:
            body["end_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _mp_order_list(self, body: dict, param_names: set[str], api_path: str) -> None:
        body.setdefault("offset", 0)
        body.setdefault("length", 20)
        if "date_type" in param_names and "date_type" not in body:
            body["date_type"] = "update_time"
        if "start_time" in param_names and "start_time" not in body:
            body["start_time"] = int((datetime.now() - timedelta(days=7)).timestamp())
        if "end_time" in param_names and "end_time" not in body:
            body["end_time"] = int(datetime.now().timestamp())
        if "store_id" in param_names and "store_id" not in body:
            body["store_id"] = [str(self.default_sids[0])]

    def _mp_new_platform_order(self, body: dict, param_names: set[str], api_path: str) -> None:
        for k, v in [("pageNum", 1), ("pageSize", 50), ("dateType", 1)]:
            if k in param_names and k not in body:
                body[k] = v
        if "startDate" in param_names and "startDate" not in body:
            body["startDate"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
        if "endDate" in param_names and "endDate" not in body:
            body["endDate"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if "storeIdList" in param_names and "storeIdList" not in body:
            body["storeIdList"] = [str(self.default_sids[0])]

    def _mp_wfs_inventory(self, body: dict, param_names: set[str], api_path: str) -> None:
        if "store_id" in param_names and "store_id" not in body:
            body["store_id"] = [str(self.default_sids[0])]
        body.setdefault("offset", 0)
        body.setdefault("length", 15)

    def _mp_wfs_cargo(self, body: dict, param_names: set[str], api_path: str) -> None:
        if "store_id" in param_names and "store_id" not in body:
            body["store_id"] = [str(self.default_sids[0])]
        if "start_time" in param_names and "start_time" not in body:
            body["start_time"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        if "end_time" in param_names and "end_time" not in body:
            body["end_time"] = datetime.now().strftime("%Y-%m-%d")
        body.setdefault("offset", 0)
        body.setdefault("length", 15)

    def _mp_temu(self, body: dict, param_names: set[str], api_path: str) -> None:
        body.setdefault("offset", 0)
        body.setdefault("length", 20)
        if "searchField" in param_names and "searchField" not in body:
            body["searchField"] = "9"
        if "storeIds" in param_names and "storeIds" not in body:
            body["storeIds"] = [str(self.default_sids[0])]

    def _mp_shopify(self, body: dict, param_names: set[str], api_path: str) -> None:
        if "store_ids" in param_names and "store_ids" not in body:
            body["store_ids"] = [str(self.default_sids[0])]
        body.setdefault("offset", 0)
        body.setdefault("length", 20)
        if "listing_start_time" in param_names and "listing_start_time" not in body:
            body["listing_start_time"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
        if "listing_end_time" in param_names and "listing_end_time" not in body:
            body["listing_end_time"] = datetime.now().strftime("%Y-%m-%d")

    def _mp_shipping(self, body: dict, param_names: set[str], api_path: str) -> None:
        if "store_id" in param_names and "store_id" not in body:
            body["store_id"] = [str(self.default_sids[0])]
        if "start_time" in param_names and "start_time" not in body:
            body["start_time"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
        if "end_time" in param_names and "end_time" not in body:
            body["end_time"] = datetime.now().strftime("%Y-%m-%d")
        body.setdefault("offset", 0)
        body.setdefault("length", 15)

    def _build_mws_report_params(  # noqa: PLR0915,PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建亚马逊源表数据API参数"""
        api_path_lower = api_path.lower()

        # FBA库存API
        if api_path_lower.endswith(("/manageinventory", "/getafnfulfillablequantity")):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]

        # FBA订单API
        elif api_path_lower.endswith(("/fbaorders", "/allorders")):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "date_type" in param_names and "date_type" not in body:
                body["date_type"] = 1
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")

        # 每日库存API
        elif api_path_lower.endswith("/dailyinventory"):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "event_date" in param_names and "event_date" not in body:
                body["event_date"] = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 预留库存API
        elif api_path_lower.endswith("/reservedinventory"):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]

        # 盘存记录API
        elif api_path_lower.endswith("/adjustmentlist"):
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
            if "sids" in param_names and "sids" not in body:
                body["sids"] = ",".join(map(str, self.default_sids))

        # 交易明细API
        elif api_path_lower.endswith("/transaction") and "/mws_report/" in api_path:
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "event_date" in param_names and "event_date" not in body:
                body["event_date"] = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        # 移除货件API
        elif api_path_lower.endswith("/removalshipment/list"):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")

        # 移除订单API
        elif api_path_lower.endswith("/removalorderlistnew"):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "last_updated_date"

        # FBA换货订单API
        elif api_path_lower.endswith("/fbaexchangeorderlist"):
            if "sid" in param_names and "sid" not in body:
                body["sid"] = self.default_sids[0]
            if "start_date" in param_names and "start_date" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" in param_names and "end_date" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")

        # 库龄表API
        elif api_path_lower.endswith("/getfbfagelist") and "sid" in param_names and "sid" not in body:
            body["sid"] = str(self.default_sids[0])

        return body

    def _build_restocking_params(  # noqa: PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建补货建议API参数"""
        # 添加店铺参数
        if "sid" not in body and "sids" not in body and "sid_list" not in body:
            if "/restocking/analysis/getSummaryList" in api_path:
                body["sid_list"] = self.default_sids
            elif "/getConfig" in api_path and "msku" in api_path:
                body["sid"] = str(self.default_sids[0])
            else:
                body["sid"] = self.default_sids[0]

        # 按ASIN/MSKU查询FBA补货建议图表
        if "/getDailySalesInfoFeature" in api_path:
            if "sug_type" not in body:
                body["sug_type"] = 1
            if "mode" not in body:
                body["mode"] = 1

        # 查询报表型数据明细
        if "/getSourceList" in api_path:
            if "type" not in body:
                body["type"] = "3"
            if "mode" not in body:
                body["mode"] = "1"

        # 查询补货列表
        if "/restocking/analysis/getSummaryList" in api_path:
            if "data_type" not in body:
                body["data_type"] = 1
            if "mode" not in body:
                body["mode"] = 0

        # 查询建议信息
        if "/getInfo" in api_path and "mode" not in body:
            body["mode"] = 0

        return body

    def _build_vc_params(  # noqa: PLR0912
        self, api_path: str, body: dict[str, Any], param_names: set[str]
    ) -> dict[str, Any]:
        """构建VC类API参数"""
        # VC订单列表
        if "/vcOrder/pageList" in api_path:
            if "purchase_order_type" in param_names and "purchase_order_type" not in body:
                body["purchase_order_type"] = ["0", "1"]
            if "start_date" not in body and "startDate" not in body:
                body["start_date"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "end_date" not in body and "endDate" not in body:
                body["end_date"] = datetime.now().strftime("%Y-%m-%d")
            if "search_field_time" in param_names and "search_field_time" not in body:
                body["search_field_time"] = "1"

        # VC订单详情 DF
        elif "/vcOrderDf/detail" in api_path:
            if "vc_store_id" in param_names and "vc_store_id" not in body:
                body["vc_store_id"] = str(self.default_sids[0])
            if "purchase_order_number" in param_names and "purchase_order_number" not in body:
                body["purchase_order_number"] = ""

        # VC订单详情 PO
        elif "/vcOrderPo/detail" in api_path:
            if "local_po_number" in param_names and "local_po_number" not in body:
                body["local_po_number"] = ""

        # VC发货单列表
        elif "/getInvoice/page/list" in api_path:
            if "shipmentType" in param_names and "shipmentType" not in body:
                body["shipmentType"] = "1"
            if "createTimeStartTime" in param_names and "createTimeStartTime" not in body:
                body["createTimeStartTime"] = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
            if "createTimeEndTime" in param_names and "createTimeEndTime" not in body:
                body["createTimeEndTime"] = datetime.now().strftime("%Y-%m-%d")

        # VC发货单详情
        elif "/getInvoice/detail" in api_path:
            if "orderNo" in param_names and "orderNo" not in body:
                body["orderNo"] = ""

        # VC Listing列表
        elif "/vcListing/pageList" in api_path:
            if "vc_store_ids" in param_names and "vc_store_ids" not in body:
                body["vc_store_ids"] = [str(sid) for sid in self.default_sids]

        return body


# 全局单例
_param_builder: APIParamBuilder | None = None


def get_param_builder(default_sids: list[int] | None = None) -> APIParamBuilder:
    global _param_builder
    if _param_builder is None or default_sids is not None:
        _param_builder = APIParamBuilder(default_sids)
    return _param_builder


def build_api_params(
    api_path: str,
    params: dict[str, Any],
    param_names: set[str],
    default_sids: list[int] | None = None,
) -> dict[str, Any]:
    builder = get_param_builder(default_sids)
    return builder.build_params(api_path, params, param_names)


__all__ = [
    "DEFAULT_SIDS",
    "APIParamBuilder",
    "build_api_params",
    "get_param_builder",
]

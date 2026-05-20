"""财务 API endpoints."""
from __future__ import annotations

from typing import Any

from ._base import BaseEndpoint


class FinanceEndpoints(BaseEndpoint):
    """领星财务 API (47个接口)."""

    async def fiance_profit_msku(self, offset: int = None, length: int = None, currency_type: int = None, sids: str = None, month: str = None) -> list | dict:
        """查询利润报表（旧） - MSKU.

POST /erp/sc/routing/finance/ProfitState/profitMsku

Args:
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int.
    currency_type: 币种 :  1 CNY  2 USD  3 EUR  4 JPY  5 AUD  6 CAD  7 MXN  8 GBP  9 INR  10 AED  11 SGD  12 SAR  13 BRL  14 SEK  15 PLN  16 TRY (required), int.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    month: 月份 (required), string."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitMsku", {k: v for k, v in {"offset": offset, "length": length, "currency_type": currency_type, "sids": sids, "month": month}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_profit_list_msku(self, offset: int = None, length: int = None, sids: list = None, startDate: str = None, endDate: str = None, searchField: str = None, searchValue: list = None, currencyCode: str = None) -> list | dict:
        """查询订单利润-MSKU.

POST /basicOpen/finance/mreport/OrderProfit

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限5000, int.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    startDate: 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s (required), string.
    endDate: 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s (required), string.
    searchField: 搜索值类型, 可选值:seller_sku,asin,local_name, local_sku, string.
    searchValue: 搜索的值, array.
    currencyCode: 币种code【默认原币种】, 可选值：原币种,CNY,USD,EUR,JPY,AUD,CAD,MXN,GBP,INR,AED,SGD,SAR,BRL,SEK,PLN,TRY,HKD, string."""
        resp = await self._post("/basicOpen/finance/mreport/OrderProfit", {k: v for k, v in {"offset": offset, "length": length, "sids": sids, "startDate": startDate, "endDate": endDate, "searchField": searchField, "searchValue": searchValue, "currencyCode": currencyCode}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_receipt_funds_list(self, endDate: str = None, length: int = None, offset: int = None, searchField: str = None, searchFieldTime: str = None, searchValue: str = None, seniorSearchList: str = None, startDate: str = None, status: list = None) -> list | dict:
        """查询收款单列表.

POST /basicOpen/finance/queryReceiptFundsList

Args:
    endDate: 结束日期，必填，格式：yyyy-MM-dd, string.
    length: 分页长度，默认20，最大200, int.
    offset: 分页偏移量，默认0, int.
    searchField: 搜索字段，必填，枚举值：supplier_name-供应商, order_sn-收款单号, purchase_order_sn-采购单号, purchase_return_order_sn-退货单号, create_user-创建人, remark-备注, string.
    searchFieldTime: 搜索时间字段，枚举值：create_time-申请时间, receipt_time-收款时间, string.
    searchValue: 搜索值，搜索字段对应的值, string.
    seniorSearchList: 高级筛选，JSON字符串格式, string.
    startDate: 开始日期，必填，格式：yyyy-MM-dd, string.
    status: 状态筛选，String数组，枚举值：1-待收款, 2-已完成, 3-已作废, 121-待审批, 122-已驳回, 124-已作废, array."""
        resp = await self._post("/basicOpen/finance/queryReceiptFundsList", {k: v for k, v in {"endDate": endDate, "length": length, "offset": offset, "searchField": searchField, "searchFieldTime": searchFieldTime, "searchValue": searchValue, "seniorSearchList": seniorSearchList, "startDate": startDate, "status": status}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_order_list(self, offset: int = None, length: int = None, status: int = None, search_field_time: str = None, start_date: str = None, end_date: str = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询请款单列表.

POST /basicOpen/finance/requestFunds/order/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    status: 状态： 1  待付款 2 已完成 3 已作废 121 待审批 122 已驳回 124 已作废, int.
    search_field_time: 搜索时间类型： apply_time 申请时间 real_pay_time 实际付款时间 prepay_time 预计付款时间, string.
    start_date: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_date: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    search_field: 搜索字段：purchase_order_sn 关联单据，order_sn  请款单号, string.
    search_value: 搜索值, string."""
        resp = await self._post("/basicOpen/finance/requestFunds/order/list", {k: v for k, v in {"offset": offset, "length": length, "status": status, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_payout_list(self, compareLogic: str = None, currencyCode: str = None, endDate: str = None, envKey: str = None, exportFields: list = None, fieldCompares: list = None, hasDifference: bool = None, length: float = None, offset: float = None, paid: float = None, platformCode: str = None, searchExactly: bool = None, searchMultiValue: list = None, searchSingleValue: str = None, searchType: float = None, sids: list = None, sites: list = None, sortField: str = None, sortType: str = None, startDate: str = None, storeTypes: list = None, timeType: float = None) -> list | dict:
        """回款明细-LazadaPayout.

POST /basicOpen/finance/lazada/payout/list

Args:
    compareLogic: 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`, string.
    currencyCode: 目标货币代码（为空则使用原币种）, string.
    endDate: 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59`, string.
    envKey: 环境标识, string.
    exportFields: 导出字段值, array.
    fieldCompares: 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）, array.
    hasDifference: 是否有差额：`true`=有差额，`false`=无差额，`null`=全部, boolean.
    length: 分页大小，默认 `20`，最大不超过 `200` (required), number.
    offset: 分页偏移，默认 `0` (required), number.
    paid: 支付标志： `0` 未支付 `1` 已支付, number.
    platformCode: 平台码, string.
    searchExactly: 是否精确匹配, boolean.
    searchMultiValue: 多个搜索值（精确匹配）, array.
    searchSingleValue: 单个搜索值（支持模糊匹配，多个值用逗号分隔）, string.
    searchType: 搜索类型： `1` 回款编号, number.
    sids: 店铺 ID 数组（全部店铺/指定店铺）, array.
    sites: 站点数组, array.
    sortField: 排序字段, string.
    sortType: 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`, string.
    startDate: 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00`, string.
    storeTypes: 店铺类型数组： `1` 跨境店 `2` 本土店, array.
    timeType: 时间类型： `1` 回款时间 `2` 结算周期 默认 `1`, number."""
        resp = await self._post("/basicOpen/finance/lazada/payout/list", {k: v for k, v in {"compareLogic": compareLogic, "currencyCode": currencyCode, "endDate": endDate, "envKey": envKey, "exportFields": exportFields, "fieldCompares": fieldCompares, "hasDifference": hasDifference, "length": length, "offset": offset, "paid": paid, "platformCode": platformCode, "searchExactly": searchExactly, "searchMultiValue": searchMultiValue, "searchSingleValue": searchSingleValue, "searchType": searchType, "sids": sids, "sites": sites, "sortField": sortField, "sortType": sortType, "startDate": startDate, "storeTypes": storeTypes, "timeType": timeType}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_settlement_list(self, compareLogic: str = None, currencyCode: str = None, endDate: str = None, envKey: str = None, exportFields: list = None, feeNames: list = None, fieldCompares: list = None, isInSettlement: float = None, length: float = None, offset: float = None, paidStatuses: list = None, platformCode: str = None, searchExactly: bool = None, searchExactly1: bool = None, searchMultiValue: list = None, searchMultiValue1: list = None, searchSingleValue: str = None, searchSingleValue1: str = None, searchType: float = None, searchType1: float = None, sids: list = None, sites: list = None, sortField: str = None, sortType: str = None, startDate: str = None, storeTypes: list = None, timeType: float = None, transactionTypes: list = None) -> list | dict:
        """账单明细-LazadaSettlement.

POST /basicOpen/finance/lazada/settlement/list

Args:
    compareLogic: 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`, string.
    currencyCode: 目标货币代码（为空则使用原币种）, string.
    endDate: 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59`, string.
    envKey: 环境标识, string.
    exportFields: 导出字段值, array.
    feeNames: 费用名称数组, array.
    fieldCompares: 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）, array.
    isInSettlement: 是否计入结算： `0` 否 `1` 是 `null` 全部, number.
    length: 分页大小，默认 `20`，最大不超过 `200` (required), number.
    offset: 分页偏移，默认 `0` (required), number.
    paidStatuses: 回款状态数组, array.
    platformCode: 平台码, string.
    searchExactly: 是否精确匹配, boolean.
    searchExactly1: 商品搜索是否精确匹配, boolean.
    searchMultiValue: 多个搜索值（精确匹配）, array.
    searchMultiValue1: 商品搜索值（多个，精确匹配）, array.
    searchSingleValue: 单个搜索值（支持模糊匹配，多个值用逗号分隔）, string.
    searchSingleValue1: 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔）, string.
    searchType: 搜索类型： `1` 平台单号 `2` 平台子单号 `3` 交易编号 `4` 支付参考编号 `5` 参考单号, number.
    searchType1: 商品搜索类型： `11` MSKU ID `12` MSKU `13` 商品名称, number.
    sids: 店铺 ID 数组, array.
    sites: 站点数组, array.
    sortField: 排序字段, string.
    sortType: 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`, string.
    startDate: 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00`, string.
    storeTypes: 店铺类型数组： `1` 跨境店 `2` 本土店, array.
    timeType: 时间类型： `1` 结算日期 `2` 结算周期 默认 `1`, number.
    transactionTypes: 交易类型数组, array."""
        resp = await self._post("/basicOpen/finance/lazada/settlement/list", {k: v for k, v in {"compareLogic": compareLogic, "currencyCode": currencyCode, "endDate": endDate, "envKey": envKey, "exportFields": exportFields, "feeNames": feeNames, "fieldCompares": fieldCompares, "isInSettlement": isInSettlement, "length": length, "offset": offset, "paidStatuses": paidStatuses, "platformCode": platformCode, "searchExactly": searchExactly, "searchExactly1": searchExactly1, "searchMultiValue": searchMultiValue, "searchMultiValue1": searchMultiValue1, "searchSingleValue": searchSingleValue, "searchSingleValue1": searchSingleValue1, "searchType": searchType, "searchType1": searchType1, "sids": sids, "sites": sites, "sortField": sortField, "sortType": sortType, "startDate": startDate, "storeTypes": storeTypes, "timeType": timeType, "transactionTypes": transactionTypes}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin(self, month: str = None, sids: str = None, currency_type: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询利润报表（旧） - ASIN（父级）.

POST /erp/sc/routing/finance/ProfitState/profitAsin

Args:
    month: 月份 (required), string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    currency_type: 币种： 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN 16 TRY (required), string.
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsin", {k: v for k, v in {"month": month, "sids": sids, "currency_type": currency_type, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin_son(self, month: str = None, sids: str = None, currency_type: str = None, asin: str = None, version: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询利润报表（旧） - ASIN（子级）.

POST /erp/sc/routing/finance/ProfitState/profitAsinSon

Args:
    month: 月份 (required), string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    currency_type: 币种： 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN 16 TRY (required), string.
    asin: 父级展开查询子级列表时的参数，取值 父级asin (required), string.
    version: 版本号，没有则传空 (required), string.
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsinSon", {k: v for k, v in {"month": month, "sids": sids, "currency_type": currency_type, "asin": asin, "version": version, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_order_transcation_list(self, offset: int = None, length: int = None, mids: list = None, sids: list = None, searchDateField: str = None, startDate: str = None, endDate: str = None, gmtModifiedStartDate: str = None, gmtModifiedEndDate: str = None, currencyCode: str = None, searchField: str = None, searchValue: list = None, sortField: str = None, sortType: str = None, settlementStatus: list = None, fundTransferStatus: list = None, accountType: list = None, eventSource: list = None, fulfillment: list = None, principalUids: list = None, productDeveloperUids: list = None, orderStatus: str = None) -> list | dict:
        """查询利润报表 - 订单维度transaction视图.

POST /basicOpen/finance/profitReport/order/transcation/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int.
    mids: 站点id, array.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    searchDateField: 时间筛选类型: posted_date_locale 结算时间【默认】 fund_transfer_datetime_locale 转账时间 shipment_datetime_locale 发货时间 order_datetime_locale 下单时间 accounting_time 入账时间, string.
    startDate: 开始时间 (required), string.
    endDate: 结束时间 (required), string.
    gmtModifiedStartDate: 修改开始时间，格式：yyyy-MM-dd HH:mm:ss, string.
    gmtModifiedEndDate: 修改结束时间，格式：yyyy-MM-dd HH:mm:ss, string.
    currencyCode: 货币种类: 原币种【默认】 CNY USD EUR JPY AUD CAD MXN GBP INR AED SGD SAR BRL SEK PLN TRY HKD, string.
    searchField: 查询索引字段: order_id 订单号【默认】 seller_sku MSKU asin ASIN parent_asin 父ASIN local_sku SKU local_name 品名gmt_modified 修改时间【不再建议使用】settlement_id Settlement ID description 描述 fid 结算编号, string.
    searchValue: 查询索引字段值, array.
    sortField: 参与排序字段, string.
    sortType: 排序方式, string.
    settlementStatus: 结算状态 Open 待结算 Pending 结算中 Closed 已结算 Reconciled 已对账, array.
    fundTransferStatus: 转账状态: Succeeded 已转账 Processing 转帐中 Failed 失败 Unknown 未知, array.
    accountType: 账单类型: Standard Invoiced Electronic COD PayWithAmazon, array.
    eventSource: 费用类型: Transfer Adjustment Debt Refund FBA Inventory Fee Service Fee Order, array.
    fulfillment: 订单类型: FBA FBA FBM FBM, array.
    principalUids: listing负责人, array.
    productDeveloperUids: 开发负责人, array.
    orderStatus: 交易状态 Deferred 已推迟（结束时间必须要今天才能获取已推迟数据） Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含`预结`算） All 全部, string."""
        resp = await self._post("/basicOpen/finance/profitReport/order/transcation/list", {k: v for k, v in {"offset": offset, "length": length, "mids": mids, "sids": sids, "searchDateField": searchDateField, "startDate": startDate, "endDate": endDate, "gmtModifiedStartDate": gmtModifiedStartDate, "gmtModifiedEndDate": gmtModifiedEndDate, "currencyCode": currencyCode, "searchField": searchField, "searchValue": searchValue, "sortField": sortField, "sortType": sortType, "settlementStatus": settlementStatus, "fundTransferStatus": fundTransferStatus, "accountType": accountType, "eventSource": eventSource, "fulfillment": fulfillment, "principalUids": principalUids, "productDeveloperUids": productDeveloperUids, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_settlement(self, sids: str = None, start_date: str = None, end_date: str = None, currency_type: int = None, send_date_start: str = None, send_date_end: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询利润报表（旧）-结算明细.

POST /erp/sc/routing/finance/ProfitState/profitSettlement

Args:
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    start_date: 结算开始时间筛选 (required), string.
    end_date: 结算结束时间筛选 (required), string.
    currency_type: 币种： 0原币种 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN 16 TRY (required), int.
    send_date_start: 发货日期开始筛选时间，大于等于结算开始时间, string.
    send_date_end: 发货日期结束筛选时间，小于等于结算结束时间, string.
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitSettlement", {k: v for k, v in {"sids": sids, "start_date": start_date, "end_date": end_date, "currency_type": currency_type, "send_date_start": send_date_start, "send_date_end": send_date_end, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_custom_fee_list(self, offset: int = None, length: int = None, pay_status: str = None, search_field_time: str = None, start_time: str = None, end_time: str = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询请款池-其他应付款.

POST /basicOpen/finance/requestFundsPool/customFee/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    pay_status: 支付状态【多个状态用英文逗号分隔】： 0 未申请 1 已申请 2 部分付款 3 已付清, string.
    search_field_time: 时间搜索类型： create_time   创建时间   close_time     付清时间, string.
    start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    search_field: 搜索类型： business_sn   费用单号 custom_fee_sn   其他应付单号, string.
    search_value: 搜索值, string."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/customFee/list", {k: v for k, v in {"offset": offset, "length": length, "pay_status": pay_status, "search_field_time": search_field_time, "start_time": start_time, "end_time": end_time, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_inbound_list(self, pay_status: str = None, time_field: str = None, start_time: str = None, end_time: str = None, search_field: str = None, search_value: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询请款池 - 货款月结.

POST /basicOpen/finance/requestFundsPool/inbound/list

Args:
    pay_status: 状态： 0 未申请 10 已申请 20 已付清, string.
    time_field: 时间搜索类型： create_time 入库时间 prepay_time 应付款日, string.
    start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    search_field: 搜索类型： order_sn 入库单号 purchase_order_sn 采购单号 sku SKU, string.
    search_value: 搜索值, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/inbound/list", {k: v for k, v in {"pay_status": pay_status, "time_field": time_field, "start_time": start_time, "end_time": end_time, "search_field": search_field, "search_value": search_value, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_logistics_list(self, offset: int = None, length: int = None, search_field_time: str = None, start_time: str = None, end_time: str = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询请款池-物流请款.

POST /basicOpen/finance/requestFundsPool/logistics/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    search_field_time: 时间搜索类型： create_time  费用录入时间   delivery_create_time  发货单创建时间  shipment_time  发货时间  close_time  付清时间, string.
    start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    search_field: 搜索类型： order_sn  发货单号  logistics_center_code  物流中心编码, string.
    search_value: 搜索值, string."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/logistics/list", {k: v for k, v in {"offset": offset, "length": length, "search_field_time": search_field_time, "start_time": start_time, "end_time": end_time, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_other_fee_list(self, endTime: str = None, startTime: str = None, length: int = None, offset: int = None, purchaserIds: list = None, searchField: str = None, searchFieldTime: str = None, searchValue: str = None, status: int = None, supplierIds: list = None) -> list | dict:
        """查询请款池-其他费用.

POST /basicOpen/finance/requestFundsPool/otherFee/list

Args:
    endTime: 结束时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度, string.
    startTime: 开始时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度, string.
    length: 分页长度, int.
    offset: 分页偏移量, int.
    purchaserIds: 采购方ID列表，筛选指定采购方的其他费用, array.
    searchField: 搜索字段，枚举值：order_sn-采购单号, create_username-采购员，配合searchValue使用, string.
    searchFieldTime: 时间维度，枚举值：create_time-创建时间, close_time-付清时间，默认create_time, string.
    searchValue: 搜索值，根据searchField字段进行搜索，支持模糊查询, string.
    status: 付款状态，枚举值：0-查询未付清, 1-查询已付清，不传默认查询全部, int.
    supplierIds: 应付对象ID列表，筛选指定供应商的其他费用, array."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/otherFee/list", {k: v for k, v in {"endTime": endTime, "startTime": startTime, "length": length, "offset": offset, "purchaserIds": purchaserIds, "searchField": searchField, "searchFieldTime": searchFieldTime, "searchValue": searchValue, "status": status, "supplierIds": supplierIds}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_prepay_list(self, offset: int = None, length: int = None, pay_status: str = None, start_time: str = None, end_time: str = None, time_field: str = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询请款池 - 货款预付款.

POST /basicOpen/finance/requestFundsPool/prepay/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    pay_status: 支付状态：  0  未申请 1  已申请 2  部分付款 3  已付清, string.
    start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    time_field: 时间搜索类型： create_time  创建时间, string.
    search_field: 搜索类型： purchase_order_sn  采购单号 order_sn  预付款单号, string.
    search_value: 搜索值, string."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/prepay/list", {k: v for k, v in {"offset": offset, "length": length, "pay_status": pay_status, "start_time": start_time, "end_time": end_time, "time_field": time_field, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_purchase_list(self, pay_status: str = None, time_field: str = None, start_time: str = None, end_time: str = None, search_field: str = None, search_value: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询请款池 - 货款现结.

POST /basicOpen/finance/requestFundsPool/purchase/list

Args:
    pay_status: 支付状态【多个使用英文逗号分隔】： 0 未申请 1 已申请 2 部分付款 3 已付清, string.
    time_field: 时间搜索类型： create_time 创建时间, string.
    start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d, string.
    search_field: 搜索类型： sku SKU order_sn 采购单号, string.
    search_value: 查询值, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/finance/requestFundsPool/purchase/list", {k: v for k, v in {"pay_status": pay_status, "time_field": time_field, "start_time": start_time, "end_time": end_time, "search_field": search_field, "search_value": search_value, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_adjustment_list(self, adjDimensions: list = None, adjTypes: list = None, compareLogic: str = None, currencyCode: str = None, endDate: str = None, envKey: str = None, exportFields: list = None, fieldCompares: list = None, length: float = None, offset: float = None, platformCode: str = None, searchExactly: bool = None, searchMultiValue: list = None, searchSingleValue: str = None, searchType: float = None, sids: list = None, sites: list = None, sortField: str = None, sortType: str = None, startDate: str = None, storeTypes: list = None) -> list | dict:
        """账单明细-ShopeeAdjustment.

POST /basicOpen/finance/shopee/adjustment/list

Args:
    adjDimensions: 调整维度数组（下拉多选）： `Order` `Shop` `other` 其他维度, array.
    adjTypes: 调整类型数组（下拉多选）： `Refund Amount` `Marketing Fee` `Warehouse Fee` `Other` 其他类型, array.
    compareLogic: 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`, string.
    currencyCode: 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）, string.
    endDate: 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期, string.
    envKey: 环境标识, string.
    exportFields: 导出字段值, array.
    fieldCompares: 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）, array.
    length: 分页大小，默认 `20`，最大不超过 `200` (required), number.
    offset: 分页偏移，默认 `0` (required), number.
    platformCode: 平台码, string.
    searchExactly: 是否精确匹配, boolean.
    searchMultiValue: 多个搜索值（精确匹配）, array.
    searchSingleValue: 单个搜索值（支持模糊匹配，多个值用逗号分隔）, string.
    searchType: 搜索类型： `1` 平台单号, number.
    sids: 店铺 ID 数组, array.
    sites: 站点数组, array.
    sortField: 排序字段, string.
    sortType: 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`, string.
    startDate: 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天, string.
    storeTypes: 店铺类型数组： `1` 跨境店(CB) `2` 本土店(Local), array."""
        resp = await self._post("/basicOpen/finance/shopee/adjustment/list", {k: v for k, v in {"adjDimensions": adjDimensions, "adjTypes": adjTypes, "compareLogic": compareLogic, "currencyCode": currencyCode, "endDate": endDate, "envKey": envKey, "exportFields": exportFields, "fieldCompares": fieldCompares, "length": length, "offset": offset, "platformCode": platformCode, "searchExactly": searchExactly, "searchMultiValue": searchMultiValue, "searchSingleValue": searchSingleValue, "searchType": searchType, "sids": sids, "sites": sites, "sortField": sortField, "sortType": sortType, "startDate": startDate, "storeTypes": storeTypes}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_income_list(self, compareLogic: str = None, currencyCode: str = None, endDate: str = None, envKey: str = None, expandChildren: bool = None, exportFields: list = None, fieldCompares: list = None, length: float = None, offset: float = None, platformCode: str = None, searchExactly: bool = None, searchExactly1: bool = None, searchMultiValue: list = None, searchMultiValue1: list = None, searchSingleValue: str = None, searchSingleValue1: str = None, searchType: float = None, searchType1: float = None, sids: list = None, sites: list = None, sortField: str = None, sortType: str = None, startDate: str = None, storeTypes: list = None) -> list | dict:
        """账单明细-ShopeeIncome.

POST /basicOpen/finance/shopee/income/list

Args:
    compareLogic: 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`, string.
    currencyCode: 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）, string.
    endDate: 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期, string.
    envKey: 环境标识, string.
    expandChildren: 是否展开子项（商品明细），默认 `true` 展开树形结构, boolean.
    exportFields: 导出字段值, array.
    fieldCompares: 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）, array.
    length: 分页大小，默认 `20`，最大不超过 `200` (required), number.
    offset: 分页偏移，默认 `0` (required), number.
    platformCode: 平台码, string.
    searchExactly: 是否精确匹配, boolean.
    searchExactly1: 商品搜索是否精确匹配, boolean.
    searchMultiValue: 多个搜索值（精确匹配）, array.
    searchMultiValue1: 商品搜索值（多个，精确匹配）, array.
    searchSingleValue: 单个搜索值（支持模糊匹配，多个值用逗号分隔）, string.
    searchSingleValue1: 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔）, string.
    searchType: 搜索类型： `1` 平台单号, number.
    searchType1: 商品搜索类型： `11` MSKU ID `12` MSKU `13` MSKU 名称 `14` 商品ID `15` 全球商品货号 `16` 商品名称, number.
    sids: 店铺 ID 数组, array.
    sites: 站点数组, array.
    sortField: 排序字段, string.
    sortType: 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`, string.
    startDate: 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天, string.
    storeTypes: 店铺类型数组： `1` 跨境店(CB) `2` 本土店(Local), array."""
        resp = await self._post("/basicOpen/finance/shopee/income/list", {k: v for k, v in {"compareLogic": compareLogic, "currencyCode": currencyCode, "endDate": endDate, "envKey": envKey, "expandChildren": expandChildren, "exportFields": exportFields, "fieldCompares": fieldCompares, "length": length, "offset": offset, "platformCode": platformCode, "searchExactly": searchExactly, "searchExactly1": searchExactly1, "searchMultiValue": searchMultiValue, "searchMultiValue1": searchMultiValue1, "searchSingleValue": searchSingleValue, "searchSingleValue1": searchSingleValue1, "searchType": searchType, "searchType1": searchType1, "sids": sids, "sites": sites, "sortField": sortField, "sortType": sortType, "startDate": startDate, "storeTypes": storeTypes}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_payout_list(self, compareLogic: str = None, currencyCode: str = None, endDate: str = None, envKey: str = None, exportFields: list = None, fieldCompares: list = None, length: float = None, offset: float = None, platformCode: str = None, searchExactly: bool = None, searchMultiValue: list = None, searchSingleValue: str = None, searchType: str = None, sids: list = None, sites: list = None, sortField: str = None, sortType: str = None, startDate: str = None, storeType: float = None) -> list | dict:
        """回款明细-ShopeePayout.

POST /basicOpen/finance/shopee/payout/list

Args:
    compareLogic: 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`, string.
    currencyCode: 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）, string.
    endDate: 结束时间（拨款时间），格式 `yyyy-MM-dd`，默认当前日期, string.
    envKey: 环境标识, string.
    exportFields: 导出字段值, array.
    fieldCompares: 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）, array.
    length: 分页大小，默认 `20`，最大不超过 `200` (required), number.
    offset: 分页偏移，默认 `0` (required), number.
    platformCode: 平台码, string.
    searchExactly: 是否精确匹配, boolean.
    searchMultiValue: 多个搜索值（精确匹配）, array.
    searchSingleValue: 单个搜索值（支持模糊匹配，多个值用逗号分隔）, string.
    searchType: 搜索类型： `1` 付款ID, string.
    sids: 店铺 ID 数组, array.
    sites: 站点数组, array.
    sortField: 排序字段, string.
    sortType: 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`, string.
    startDate: 开始时间（拨款时间），格式 `yyyy-MM-dd`，默认当前月份第一天, string.
    storeType: 店铺类型： `1` 跨境店(CB), number."""
        resp = await self._post("/basicOpen/finance/shopee/payout/list", {k: v for k, v in {"compareLogic": compareLogic, "currencyCode": currencyCode, "endDate": endDate, "envKey": envKey, "exportFields": exportFields, "fieldCompares": fieldCompares, "length": length, "offset": offset, "platformCode": platformCode, "searchExactly": searchExactly, "searchMultiValue": searchMultiValue, "searchSingleValue": searchSingleValue, "searchType": searchType, "sids": sids, "sites": sites, "sortField": sortField, "sortType": sortType, "startDate": startDate, "storeType": storeType}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}


    async def fee_management_list(self, offset: int, length: int, date_type: str, start_date: str, end_date: str, sids: list = None, other_fee_type_ids: list = None, status_order: int = None, dimensions: list = None, apportion_status: list = None, status_merge: int = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询费用明细列表.

POST /bd/fee/management/open/feeManagement/otherFee/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    date_type: 时间类型：gmt_create 创建日期，date 分摊日期, str.
    start_date: 开始时间，格式：Y-m-d, str.
    end_date: 结束时间，格式：Y-m-d, str.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    other_fee_type_ids: 费用类型id, list.
    status_order: 单据状态： 1 待提交 2 待审批 3 已处理 4 已驳回 5 已作废, int.
    dimensions: 分摊维度id： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业, list.
    apportion_status: 分摊状态【未设置新利润报表启用月使用该入参】： 1 未分摊 2 已分摊-新 3 已分摊-旧 4 已分摊, list.
    status_merge: 分摊状态【已设置新利润报表启用月使用该入参】： 1 未分摊 2 已分摊, int.
    search_field: 搜索类型： number 单据编号 msku MSKU asin ASIN create_name 创建人 remark_order 单据备注 remark_item 明细备注, str.
    search_value: 搜索值, str."""
        resp = await self._post("/bd/fee/management/open/feeManagement/otherFee/list", {k: v for k, v in {"offset": offset, "length": length, "date_type": date_type, "start_date": start_date, "end_date": end_date, "sids": sids, "other_fee_type_ids": other_fee_type_ids, "status_order": status_order, "dimensions": dimensions, "apportion_status": apportion_status, "status_merge": status_merge, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def fee_management_create(self, submit_type: int, dimension: int, apportion_rule: int, is_request_pool: int, remark: str, fee_items: list) -> list | dict:
        """创建费用单.

POST /bd/fee/management/open/feeManagement/otherFee/create

Args:
    submit_type: 提交类型：1 暂存，2 提交, int.
    dimension: 分摊维度： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业, int.
    apportion_rule: 分摊规则： 0 无 1 按销售额 2 按销量 3 店铺均摊后按销售额占比分摊 4 店铺均摊后按销量占比分摊, int.
    is_request_pool: 是否请款：0 否，1 是, int.
    remark: 费用单备注, str.
    fee_items: , list."""
        resp = await self._post("/bd/fee/management/open/feeManagement/otherFee/create", {k: v for k, v in {"submit_type": submit_type, "dimension": dimension, "apportion_rule": apportion_rule, "is_request_pool": is_request_pool, "remark": remark, "fee_items": fee_items}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def fee_management_edit(self, id: str, submit_type: int, dimension: int, apportion_rule: int, date: str, currency_code: str, other_fee_type_id: int, is_request_pool: int, fee_items: list, remark: str = None) -> list | dict:
        """编辑费用单.

POST /bd/fee/management/open/feeManagement/otherFee/edit

Args:
    id: 费用单id，查询费用明细列表 接口对应字段【records>>id】, str.
    submit_type: 提交类型：1 暂存，2 提交, int.
    dimension: 分摊维度： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业, int.
    apportion_rule: 分摊规则： 0 无 1 按销售额 2 按销量 3 店铺均摊后按销售额占比分摊  4 店铺均摊后按销量占比分摊, int.
    date: 分摊日期，格式：Y-m-d 或 Y-m, str.
    currency_code: 币种代码, str.
    other_fee_type_id: 费用类型id，查询费用类型列表 接口对应字段【id】, int.
    is_request_pool: 是否请款：0 否，1 是, int.
    fee_items: , list.
    remark: 单据备注, str."""
        resp = await self._post("/bd/fee/management/open/feeManagement/otherFee/edit", {k: v for k, v in {"id": id, "submit_type": submit_type, "dimension": dimension, "apportion_rule": apportion_rule, "date": date, "currency_code": currency_code, "other_fee_type_id": other_fee_type_id, "is_request_pool": is_request_pool, "fee_items": fee_items, "remark": remark}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def fee_management_discard(self, numbers: list) -> list | dict:
        """作废费用单.

POST /bd/fee/management/open/feeManagement/otherFee/discard

Args:
    numbers: 费用单号，上限200, list."""
        resp = await self._post("/bd/fee/management/open/feeManagement/otherFee/discard", {k: v for k, v in {"numbers": numbers}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def fee_management_delete(self, numbers: list) -> list | dict:
        """删除费用单.

POST /bd/fee/management/open/feeManagement/otherFee/delete

Args:
    numbers: 费用单号，上限200, list."""
        resp = await self._post("/bd/fee/management/open/feeManagement/otherFee/delete", {k: v for k, v in {"numbers": numbers}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_msku(self, startDate: str, endDate: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, monthlyQuery: bool = None, searchField: str = None, searchValue: list = None, currencyCode: str = None, summaryEnabled: bool = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-MSKU.

POST /bd/profit/report/open/report/msku/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    searchField: 搜索值类型，seller_sku, str.
    searchValue: 搜索的值, list.
    currencyCode: 币种code【默认原币种】, str.
    summaryEnabled: 是否按msku汇总返回： false 默认值  true, bool.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部（不包含已发放预结算数据）, str."""
        resp = await self._post("/bd/profit/report/open/report/msku/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "offset": offset, "length": length, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "searchField": searchField, "searchValue": searchValue, "currencyCode": currencyCode, "summaryEnabled": summaryEnabled, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_asin(self, startDate: str, endDate: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, monthlyQuery: bool = None, searchField: str = None, searchValue: list = None, currencyCode: str = None, summaryEnabled: bool = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-ASIN.

POST /bd/profit/report/open/report/asin/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    searchField: 搜索值类型，ASIN, str.
    searchValue: 搜索的值, list.
    currencyCode: 币种code, str.
    summaryEnabled: 是否按asin汇总返回： false 默认值  true, bool.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部, str."""
        resp = await self._post("/bd/profit/report/open/report/asin/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "offset": offset, "length": length, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "searchField": searchField, "searchValue": searchValue, "currencyCode": currencyCode, "summaryEnabled": summaryEnabled, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_parent_asin(self, startDate: str, endDate: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, monthlyQuery: bool = None, searchField: str = None, searchValue: list = None, currencyCode: str = None, summaryEnabled: bool = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-父ASIN.

POST /bd/profit/report/open/report/parent/asin/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    searchField: 搜索值类型，parent_asin, str.
    searchValue: 搜索的值, list.
    currencyCode: 币种code, str.
    summaryEnabled: 是否按父asin汇总返回： false 默认值  true, bool.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部, str."""
        resp = await self._post("/bd/profit/report/open/report/parent/asin/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "offset": offset, "length": length, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "searchField": searchField, "searchValue": searchValue, "currencyCode": currencyCode, "summaryEnabled": summaryEnabled, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_sku(self, startDate: str, endDate: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, monthlyQuery: bool = None, searchField: str = None, searchValue: list = None, currencyCode: str = None, summaryEnabled: bool = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-SKU.

POST /bd/profit/report/open/report/sku/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    searchField: 搜索值类型，local_sku, str.
    searchValue: 搜索的值, list.
    currencyCode: 币种code, str.
    summaryEnabled: 是否按sku汇总返回： false 默认值  true, bool.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部, str."""
        resp = await self._post("/bd/profit/report/open/report/sku/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "offset": offset, "length": length, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "searchField": searchField, "searchValue": searchValue, "currencyCode": currencyCode, "summaryEnabled": summaryEnabled, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_seller(self, startDate: str, endDate: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, monthlyQuery: bool = None, currencyCode: str = None, summaryEnabled: bool = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-店铺.

POST /bd/profit/report/open/report/seller/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    currencyCode: 币种code【默认原币种】, str.
    summaryEnabled: 是否按店铺汇总返回： false 默认值  true, bool.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部, str."""
        resp = await self._post("/bd/profit/report/open/report/seller/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "offset": offset, "length": length, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "currencyCode": currencyCode, "summaryEnabled": summaryEnabled, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_seller_summary(self, startDate: str, endDate: str, mids: list = None, sids: list = None, monthlyQuery: bool = None, currencyCode: str = None, orderStatus: str = None) -> list | dict:
        """查询利润报表-店铺月度汇总.

POST /bd/profit/report/open/report/seller/summary/list

Args:
    startDate: 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    endDate: 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m, str.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    monthlyQuery: 是否按月查询： false 按天【默认值】 true 按月, bool.
    currencyCode: 币种code, str.
    orderStatus: 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部, str."""
        resp = await self._post("/bd/profit/report/open/report/seller/summary/list", {k: v for k, v in {"startDate": startDate, "endDate": endDate, "mids": mids, "sids": sids, "monthlyQuery": monthlyQuery, "currencyCode": currencyCode, "orderStatus": orderStatus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def bd_profit_order(self, search_date_field: str, start_date: str, end_date: str, offset: int = None, length: int = None, mids: list = None, sids: list = None, search_field: str = None, search_value: list = None, currency_code: str = None, account_type: str = None, settlement_status: list = None, fund_transfer_status: list = None, event_source: list = None, description: list = None) -> list | dict:
        """查询利润报表-订单.

POST /bd/profit/report/open/report/order/list

Args:
    search_date_field: 时间类型： posted_date_locale 结算时间 fund_transfer_datetime_locale 转账时间 shipment_datetime_locale 发货时间, str.
    start_date: 开始时间, str.
    end_date: 结束时间, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，上限10000, int.
    mids: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    search_field: 搜索值类型： 亚马逊订单号：order_id MSKU：seller_sku Asin：asin 父asin：parent_asin SKU：local_sku 品名：local_name, str.
    search_value: 搜索的值, list.
    currency_code: 币种code, str.
    account_type: 报告类型： Standard Invoiced Electronic COD PayWithAmazon, str.
    settlement_status: 结算状态： 待结算：["Open", "Pending"] 已结算：["Closed"], list.
    fund_transfer_status: 转账状态： 已转帐 Succeeded 转帐中 Processing 失败 Failed 未知 Unknown, list.
    event_source: 来源： SellerDealPayment ServiceFee Adjustment Refund SellerReviewEnrollmentPayment RemovalShipmentAdju, list.
    description: 描述, list."""
        resp = await self._post("/bd/profit/report/open/report/order/list", {k: v for k, v in {"search_date_field": search_date_field, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length, "mids": mids, "sids": sids, "search_field": search_field, "search_value": search_value, "currency_code": currency_code, "account_type": account_type, "settlement_status": settlement_status, "fund_transfer_status": fund_transfer_status, "event_source": event_source, "description": description}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def settlement_summary_list(self, offset: Any = None, length: Any = None, countryCodes: Any = None, sids: Any = None, currencyCode: Any = None, dateType: Any = None, startDate: Any = None, endDate: Any = None, searchField: Any = None, searchValue: Any = None) -> list | dict:
        """查询结算中心 - 结算汇总.

POST /bd/sp/api/open/settlement/summary/list

Args:
    offset: 分页偏移量, Any.
    length: 分页长度, Any.
    countryCodes: 国家，查询亚马逊市场列表接口对应字段mid, Any.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, Any.
    currencyCode: 币种, Any.
    dateType: 时间类型： 0 结算开始时间 1 结算结束时间 2 转账时间, Any.
    startDate: 开始时间【时间间隔最长不得超过90天】, Any.
    endDate: 结束时间【时间间隔最长不得超过90天】, Any.
    searchField: 搜索字段：  id 结算编号 settlement_id 账单编号, Any.
    searchValue: 搜索值, Any."""
        resp = await self._post("/bd/sp/api/open/settlement/summary/list", {k: v for k, v in {"offset": offset, "length": length, "countryCodes": countryCodes, "sids": sids, "currencyCode": currencyCode, "dateType": dateType, "startDate": startDate, "endDate": endDate, "searchField": searchField, "searchValue": searchValue}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def settlement_transaction_list(self, offset: int = None, length: int = None, countryCodes: list = None, sids: list = None, startDate: str = None, endDate: str = None, eventType: str = None, type: str = None, searchField: str = None, searchValue: list = None, gmtModifiedStart: str = None, gmtModifiedEnd: str = None) -> list | dict:
        """查询结算中心 - 交易明细.

POST /bd/sp/api/open/settlement/transaction/detail/list

Args:
    offset: 分页偏移量, int.
    length: 分页长度，上限10000, int.
    countryCodes: 站点id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    startDate: 开始时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d 【无搜索值时，结算时间、修改时间二选一必填】, str.
    endDate: 结束时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d 【无搜索值时，结算时间、修改时间二选一必填】, str.
    eventType: 来源，多个英文用逗号隔开，枚举见附加说明, str.
    type: 交易类型, str.
    searchField: 搜索字段： id 结算编号 amazon_order_id 订单编号 primary_id 主键编号【对应本接口返回id值】 settlement_id 账单编号【此项下，结算时间或更新时间必填】, str.
    searchValue: 搜索值, list.
    gmtModifiedStart: 修改开始时间（北京时间），格式：Y-m-d H:i:s 【无搜索值时，结算时间、修改时间二选一必填】, str.
    gmtModifiedEnd: 修改结束时间（北京时间），格式：Y-m-d H:i:s 【无搜索值时，结算时间、修改时间二选一必填】, str."""
        resp = await self._post("/bd/sp/api/open/settlement/transaction/detail/list", {k: v for k, v in {"offset": offset, "length": length, "countryCodes": countryCodes, "sids": sids, "startDate": startDate, "endDate": endDate, "eventType": eventType, "type": type, "searchField": searchField, "searchValue": searchValue, "gmtModifiedStart": gmtModifiedStart, "gmtModifiedEnd": gmtModifiedEnd}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def settle_detail_query(self, sellerIds: list, startDate: str, endDate: str, fnskus: list = None, asins: list = None, mskus: list = None, eventTypes: list = None, referenceId: str = None, disposition: str = None, locations: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询库存分类账detail数据.

POST /bd/profit/report/open/report/settle/compute/manual

Args:
    sellerIds: 亚马逊店铺id, list.
    startDate: 统计起始日期 Y-m-d 闭区间, str.
    endDate: 统计结束日期 Y-m-d 闭区间, str.
    fnskus: fnsku列表, list.
    asins: asin列表, list.
    mskus: msku列表, list.
    eventTypes: 事件类型，支持传多值： 01 Shipments 02 CustomerReturns 03 WhseTransfers 04 Receipts 05 VendorReturns 06 Adjustm, list.
    referenceId: 引用id，支持模糊搜索, str.
    disposition: 库存类型： 01 SELLABLE 02 UNSELLABLE 03 ALL, str.
    locations: 国家编码列表, list.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int."""
        resp = await self._post("/bd/profit/report/open/report/settle/compute/manual", {k: v for k, v in {"sellerIds": sellerIds, "startDate": startDate, "endDate": endDate, "fnskus": fnskus, "asins": asins, "mskus": mskus, "eventTypes": eventTypes, "referenceId": referenceId, "disposition": disposition, "locations": locations, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def summary_query(self, sellerIds: list, queryType: int, startDate: str, endDate: str, fnskus: list = None, asins: list = None, mskus: list = None, disposition: str = None, locations: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询库存分类账summary数据.

POST /bd/profit/report/open/report/summary/query

Args:
    sellerIds: 亚马逊店铺id, list.
    queryType: 查询维度：1 按月，2 按天, int.
    startDate: 统计起始日期：月维度：Y-m ，天维度：Y-m-d，闭区间, str.
    endDate: 统计结束日期：月维度：Y-m ，天维度：Y-m-d，闭区间, str.
    fnskus: fnsku列表, list.
    asins: asin列表, list.
    mskus: msku列表, list.
    disposition: 库存属性：01 SELLABLE，02 UNSELLABLE，03 ALL, str.
    locations: 国家编码列表, list.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int."""
        resp = await self._post("/bd/profit/report/open/report/summary/query", {k: v for k, v in {"sellerIds": sellerIds, "queryType": queryType, "startDate": startDate, "endDate": endDate, "fnskus": fnskus, "asins": asins, "mskus": mskus, "disposition": disposition, "locations": locations, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def settlement_report(self, amazonSellerIds: list, sids: list, timeType: str, filterBeginDate: str, filterEndDate: str, countryCodes: list = None, orderNumbers: list = None, shipmentNumbers: list = None, customNumbers: list = None, mskus: list = None, skus: list = None, productNames: list = None, trackCodes: list = None, fulfillmentType: str = None, offset: int = None, length: int = None) -> list | dict:
        """查询发货结算报告.

POST /bd/sp/api/open/settlement/report

Args:
    amazonSellerIds: 亚马逊店铺id, list.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    timeType: 时间类型： 01 下单时间 02 付款时间 03 发货时间 04 结算时间 05 转账时间 06 更新时间, str.
    filterBeginDate: 开始日期，格式：Y-m-d，双闭区间, str.
    filterEndDate: 结束日期，格式：Y-m-d，双闭区间, str.
    countryCodes: 国家编码, list.
    orderNumbers: 订单编号, list.
    shipmentNumbers: 配送编号, list.
    customNumbers: 自定义编号, list.
    mskus: msku, list.
    skus: sku, list.
    productNames: 品名, list.
    trackCodes: 物流追踪编码, list.
    fulfillmentType: 配送方式【不传默认全部】：   01 FBA, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int."""
        resp = await self._post("/bd/sp/api/open/settlement/report", {k: v for k, v in {"amazonSellerIds": amazonSellerIds, "sids": sids, "timeType": timeType, "filterBeginDate": filterBeginDate, "filterEndDate": filterEndDate, "countryCodes": countryCodes, "orderNumbers": orderNumbers, "shipmentNumbers": shipmentNumbers, "customNumbers": customNumbers, "mskus": mskus, "skus": skus, "productNames": productNames, "trackCodes": trackCodes, "fulfillmentType": fulfillmentType, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def settlement_export_url_get(self, seller_id: Any = None, financial_event_group_id: Any = None) -> list | dict:
        """查询settlement下载URL.

POST /bd/sp/api/open/settlement/export/url/get

Args:
    seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】, Any.
    financial_event_group_id: 结算汇总财务事件组ID【结算汇总->financialEventGroupId】, Any."""
        resp = await self._post("/bd/sp/api/open/settlement/export/url/get", {k: v for k, v in {"seller_id": seller_id, "financial_event_group_id": financial_event_group_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def cost_stream(self, business_types: list, query_type: str, start_date: str, end_date: str, wh_names: list = None, shop_names: list = None, skus: list = None, mskus: list = None, disposition_types: list = None, business_numbers: list = None, origin_accounts: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询FBA成本计价流水.

POST /bd/profit/report/open/report/cost/stream

Args:
    business_types: 出入库类型： 1 期初库存-FBA上月结存 10 调拨入库-FBA补货入库 11 调拨入库-FBA途损补回 12 调拨入库-FBA超签入库 13 调拨入库-FBA超签入库（close后） 14 调拨入, list.
    query_type: 日期查询类型： 01 库存动作日期【对应成本计价详情页面单据日期，即在FBA仓库内发生各项库存动作的日期】 02 结算日期【仅销售、退货场景会存在结算日期，其他库存动作结算日期为空】, str.
    start_date: 起始日期，Y-m-d，不允许跨月, str.
    end_date: 结束日期，Y-m-d，不允许跨月, str.
    wh_names: 仓库名, list.
    shop_names: 店铺名, list.
    skus: sku, list.
    mskus: msku, list.
    disposition_types: 库存属性： 1 可用在途 2 可用 3 次品, list.
    business_numbers: 业务编号, list.
    origin_accounts: 源头单据号, list.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认200条, int."""
        resp = await self._post("/bd/profit/report/open/report/cost/stream", {k: v for k, v in {"business_types": business_types, "query_type": query_type, "start_date": start_date, "end_date": end_date, "wh_names": wh_names, "shop_names": shop_names, "skus": skus, "mskus": mskus, "disposition_types": disposition_types, "business_numbers": business_numbers, "origin_accounts": origin_accounts, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def invoice_list(self, invoice_start_time: str, invoice_end_time: str, offset: int = None, length: int = None, sids: list = None, mids: list = None, ads_type: list = None, search_type: str = None, search_value: str = None) -> list | dict:
        """查询广告发票列表.

POST /bd/profit/report/open/report/invoice/list

Args:
    invoice_start_time: 开始时间【发票开具时间】, str.
    invoice_end_time: 结束时间【发票开具时间】, str.
    offset: 分页偏移量，默认值0, int.
    length: 分页大小，默认20, int.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    mids: 国家id, list.
    ads_type: 广告类型： SPONSORED PRODUCTS SPONSORED DISPLAY SPONSORED BRANDS SPONSORED BRANDS VIDEO, list.
    search_type: 搜索类型： ads_campaign【对应页面广告活动】 invoice_id【对应发票编号】 msku asin, str.
    search_value: 搜索值, str."""
        resp = await self._post("/bd/profit/report/open/report/invoice/list", {k: v for k, v in {"invoice_start_time": invoice_start_time, "invoice_end_time": invoice_end_time, "offset": offset, "length": length, "sids": sids, "mids": mids, "ads_type": ads_type, "search_type": search_type, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def invoice_campaign_list(self, invoice_id: str, sid: int, offset: int = None, length: int = None, ads_type: list = None, search_type: str = None, search_value: str = None) -> list | dict:
        """查询广告发票活动列表.

POST /bd/profit/report/open/report/invoice/campaign/list

Args:
    invoice_id: 广告发票编号, str.
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    offset: 分页偏移量，默认值0, int.
    length: 分页大小，默认20, int.
    ads_type: 广告类型： SPONSORED PRODUCTS SPONSORED DISPLAY SPONSORED BRANDS SPONSORED BRANDS VIDEO, list.
    search_type: 搜索类型： ads_campaign【对应页面广告活动】 item【对应页面承担商品】, str.
    search_value: 搜索值, str."""
        resp = await self._post("/bd/profit/report/open/report/invoice/campaign/list", {k: v for k, v in {"invoice_id": invoice_id, "sid": sid, "offset": offset, "length": length, "ads_type": ads_type, "search_type": search_type, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def invoice_detail(self, invoice_id: str, sid: int) -> list | dict:
        """查询广告发票基本信息.

POST /bd/profit/report/open/report/invoice/detail

Args:
    invoice_id: 广告发票编号, str.
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int."""
        resp = await self._post("/bd/profit/report/open/report/invoice/detail", {k: v for k, v in {"invoice_id": invoice_id, "sid": sid}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def compute_manual(self, date_month: str) -> list | dict:
        """立即重算-利润报表数据.

POST /bd/profit/report/open/report/settle/compute/manual

Args:
    date_month: 重算月份，格式：yyyy-MM, str."""
        resp = await self._post("/bd/profit/report/open/report/settle/compute/manual", {k: v for k, v in {"date_month": date_month}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def receivable_report_list(self, settleMonth: str, sids: list = None, mids: list = None, currencyCode: str = None, archiveStatus: int = None, sortField: str = None, sortType: str = None, receivedState: int = None, offset: int = None, length: int = None) -> list | dict:
        """应收报告-列表查询.

POST /bd/sp/api/open/monthly/receivable/report/list

Args:
    settleMonth: 结算月,格式：Y-m, str.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, list.
    mids: 国家id, list.
    currencyCode: 币种code, str.
    archiveStatus: 对账状态 ： 1   已对账， 0   未对账, int.
    sortField: 排序字段： beginningBalanceCurrencyAmount 期初余额 incomeAmount 收入 refundAmount 退款 spendAmount 支出 other 其他, str.
    sortType: 排序规则： asc  升序 desc  降序, str.
    receivedState: 转账/到账金额:  0  不相符 1  相符, int.
    offset: 分页偏移量， 默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/bd/sp/api/open/monthly/receivable/report/list", {k: v for k, v in {"settleMonth": settleMonth, "sids": sids, "mids": mids, "currencyCode": currencyCode, "archiveStatus": archiveStatus, "sortField": sortField, "sortType": sortType, "receivedState": receivedState, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def report_list_detail(self, sid: int, currencyCode: str, settleMonth: str, searchField: str = None, searchValue: str = None, offset: int = None, length: int = None) -> list | dict:
        """应收报告-详情-列表.

POST /bd/sp/api/open/monthly/receivable/report/list/detail

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    currencyCode: 币种code, str.
    settleMonth: 结算月, str.
    searchField: 搜索值类型： fid 结算编号  settlementId settlementId  sellerSku Msku  localSku sku localName 品名  abstractName, str.
    searchValue: 搜索值, str.
    offset: 偏移量, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/bd/sp/api/open/monthly/receivable/report/list/detail", {k: v for k, v in {"sid": sid, "currencyCode": currencyCode, "settleMonth": settleMonth, "searchField": searchField, "searchValue": searchValue, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def reportlistdetailinfo(self, sid: int, currencyCode: str, settleMonth: str) -> list | dict:
        """应收报告-详情-基础信息.

POST /bd/sp/api/open/monthly/receivable/report/list/detail/info

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    currencyCode: 币种code, str.
    settleMonth: 结算月, str."""
        resp = await self._post("/bd/sp/api/open/monthly/receivable/report/list/detail/info", {k: v for k, v in {"sid": sid, "currencyCode": currencyCode, "settleMonth": settleMonth}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

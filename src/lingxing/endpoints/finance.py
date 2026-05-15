"""财务 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class FinanceEndpoints(BaseEndpoint):
    """领星财务 API (19个接口)."""

    async def fiance_profit_msku(self, **kwargs) -> list | dict:
        """查询利润报表（旧） - MSKU.

POST /erp/sc/routing/finance/ProfitState/profitMsku

Args:
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int.
    currency_type: 币种 :  1 CNY  2 USD  3 EUR  4 JPY  5 AUD  6 CAD  7 MXN  8 GBP  9 INR  10 AED  11 SGD  12 SAR  13 BRL  14 SEK  15 PLN  16 TRY (required), int.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    month: 月份 (required), string."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitMsku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_profit_list_msku(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/mreport/OrderProfit", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_receipt_funds_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/queryReceiptFundsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_order_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFunds/order/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_payout_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/lazada/payout/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lazada_settlement_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/lazada/settlement/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin(self, **kwargs) -> list | dict:
        """查询利润报表（旧） - ASIN（父级）.

POST /erp/sc/routing/finance/ProfitState/profitAsin

Args:
    month: 月份 (required), string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    currency_type: 币种： 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN 16 TRY (required), string.
    offset: 分页偏移量 (required), int.
    length: 分页长度 (required), int."""
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsin", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_asin_son(self, **kwargs) -> list | dict:
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
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitAsinSon", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_order_transcation_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/profitReport/order/transcation/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_settlement(self, **kwargs) -> list | dict:
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
        resp = await self._post("/erp/sc/routing/finance/ProfitState/profitSettlement", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_custom_fee_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/customFee/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_inbound_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/inbound/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_logistics_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/logistics/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_other_fee_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/otherFee/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_prepay_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/prepay/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def request_funds_pool_purchase_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/requestFundsPool/purchase/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_adjustment_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/shopee/adjustment/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_income_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/shopee/income/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopee_payout_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/finance/shopee/payout/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

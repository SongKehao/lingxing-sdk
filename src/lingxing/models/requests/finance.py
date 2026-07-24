"""Request models for Finance APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class FinanceFeemanagementlistRequest(LingXingModel):
    """Request for 查询费用明细列表.

    POST /bd/fee/management/open/feeManagement/otherFee/list
    """

    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20
    date_type: str  # 时间类型：gmt_create 创建日期，date 分摊日期
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    other_fee_type_ids: Optional[list] = None  # 费用类型id
    status_order: Optional[int] = None  # 单据状态： 1 待提交 2 待审批 3 已处理 4 已驳回 5 已作废
    dimensions: Optional[list] = None  # 分摊维度id： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业
    apportion_status: Optional[list] = (
        None  # 分摊状态【未设置新利润报表启用月使用该入参】： 1 未分摊 2 已分摊-新 3 已分摊-旧 4 已分摊
    )
    status_merge: Optional[int] = None  # 分摊状态【已设置新利润报表启用月使用该入参】： 1 未分摊 2 已分摊
    search_field: Optional[str] = (
        None  # 搜索类型： number 单据编号 msku MSKU asin ASIN create_name 创建人 remark_order 单据备注 remark_item 明细备注
    )
    search_value: Optional[str] = None  # 搜索值


class FinanceFeemanagementcreateRequestFeeItemsItem(LingXingModel):
    sids: List  # 店铺id： 单选店铺传店铺id 全部店铺传[99999999] 企业费用传[88888888] 多选店铺传[77777777] ，对应查询亚马逊店铺列表接口对应字段【sid】
    dimension_value: str  # 纬度值，例如ASIN值
    date: str  # 分摊日期，格式：Y-m-d 或 Y-m
    other_fee_type_id: float  # 费用类型id，查询费用类型列表 接口对应字段【id】
    fee: float  # 金额
    fee: float  # 原币金额（注意正负数）
    currency_code: str  # 币种代码
    remark: str  # 费用子项备注


class FinanceFeemanagementcreateRequest(LingXingModel):
    """Request for 创建费用单.

    POST /bd/fee/management/open/feeManagement/otherFee/create
    """

    submit_type: int  # 提交类型：1 暂存，2 提交
    dimension: int  # 分摊维度： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业
    apportion_rule: int  # 分摊规则： 0 无 1 按销售额 2 按销量 3 店铺均摊后按销售额占比分摊 4 店铺均摊后按销量占比分摊
    is_request_pool: int  # 是否请款：0 否，1 是
    remark: str  # 费用单备注
    fee_items: List[FinanceFeemanagementcreateRequestFeeItemsItem]


class FinanceFeemanagementeditRequestFeeItemsItem(LingXingModel):
    fof_id: str  # 费用单子项id，查询费用明细列表 接口对应字段【fof_id】
    sids: List  # 店铺id，全部店铺传[99999999] ，对应查询亚马逊店铺列表接口对应字段【sid】
    dimension_value: str  # 纬度值，例如ASIN值
    fee: float  # 金额
    remark: Optional[str] = None  # 备注


class FinanceFeemanagementeditRequest(LingXingModel):
    """Request for 编辑费用单.

    POST /bd/fee/management/open/feeManagement/otherFee/edit
    """

    id: str  # 费用单id，查询费用明细列表 接口对应字段【records>>id】
    submit_type: int  # 提交类型：1 暂存，2 提交
    dimension: int  # 分摊维度： 1 msku 2 asin 3 店铺 4 父asin 5 sku 6 企业
    apportion_rule: int  # 分摊规则： 0 无 1 按销售额 2 按销量 3 店铺均摊后按销售额占比分摊  4 店铺均摊后按销量占比分摊
    date: str  # 分摊日期，格式：Y-m-d 或 Y-m
    currency_code: str  # 币种代码
    other_fee_type_id: int  # 费用类型id，查询费用类型列表 接口对应字段【id】
    is_request_pool: int  # 是否请款：0 否，1 是
    remark: Optional[str] = None  # 单据备注
    fee_items: List[FinanceFeemanagementeditRequestFeeItemsItem]


class FinanceFeemanagementdiscardRequest(LingXingModel):
    """Request for 作废费用单.

    POST /bd/fee/management/open/feeManagement/otherFee/discard
    """

    numbers: List  # 费用单号，上限200


class FinanceFeemanagementdeleteRequest(LingXingModel):
    """Request for 删除费用单.

    POST /bd/fee/management/open/feeManagement/otherFee/delete
    """

    numbers: List  # 费用单号，上限200


class FinanceBdmskuRequest(LingXingModel):
    """Request for 查询利润报表-MSKU.

    POST
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    searchField: Optional[str] = None  # 搜索值类型，seller_sku
    searchValue: Optional[list] = None  # 搜索的值
    currencyCode: Optional[str] = None  # 币种code【默认原币种】
    summaryEnabled: Optional[bool] = None  # 是否按msku汇总返回： false 默认值  true
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部（不包含已发放预结算数据）
    )


class FinanceBdasinRequest(LingXingModel):
    """Request for 查询利润报表-ASIN.

    POST /bd/profit/report/open/report/asin/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    searchField: Optional[str] = None  # 搜索值类型，ASIN
    searchValue: Optional[list] = None  # 搜索的值
    currencyCode: Optional[str] = None  # 币种code
    summaryEnabled: Optional[bool] = None  # 是否按asin汇总返回： false 默认值  true
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部
    )


class FinanceBdparentasinRequest(LingXingModel):
    """Request for 查询利润报表-父ASIN.

    POST /bd/profit/report/open/report/parent/asin/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    searchField: Optional[str] = None  # 搜索值类型，parent_asin
    searchValue: Optional[list] = None  # 搜索的值
    currencyCode: Optional[str] = None  # 币种code
    summaryEnabled: Optional[bool] = None  # 是否按父asin汇总返回： false 默认值  true
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部
    )


class FinanceBdskuRequest(LingXingModel):
    """Request for 查询利润报表-SKU.

    POST /bd/profit/report/open/report/sku/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    searchField: Optional[str] = None  # 搜索值类型，local_sku
    searchValue: Optional[list] = None  # 搜索的值
    currencyCode: Optional[str] = None  # 币种code
    summaryEnabled: Optional[bool] = None  # 是否按sku汇总返回： false 默认值  true
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部
    )


class FinanceBdsellerRequest(LingXingModel):
    """Request for 查询利润报表-店铺.

    POST /bd/profit/report/open/report/seller/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    currencyCode: Optional[str] = None  # 币种code【默认原币种】
    summaryEnabled: Optional[bool] = None  # 是否按店铺汇总返回： false 默认值  true
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部
    )


class FinanceBdsellersummaryRequest(LingXingModel):
    """Request for 查询利润报表-店铺月度汇总.

    POST /bd/profit/report/open/report/seller/summary/list
    """

    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    monthlyQuery: Optional[bool] = None  # 是否按月查询： false 按天【默认值】 true 按月
    startDate: str  # 开始时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    endDate: str  # 结束时间【结算时间，双闭区间】 按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d 按月：开始结束时间年月相同，格式：Y-m
    currencyCode: Optional[str] = None  # 币种code
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟 Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含预结算） All 全部
    )


class FinanceProfitreportordertranscationlistRequest(LingXingModel):
    """Request for 查询利润报表 - 订单维度transaction视图.

    POST /basicOpen/finance/profitReport/order/transcation/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限1000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    searchDateField: Optional[str] = (
        None  # 时间筛选类型: posted_date_locale 结算时间【默认】 fund_transfer_datetime_locale 转账时间 shipment_datetime_locale 发货时间
    )
    startDate: str  # 开始时间
    endDate: str  # 结束时间
    gmtModifiedStartDate: Optional[str] = None  # 修改开始时间，格式：yyyy-MM-dd HH:mm:ss
    gmtModifiedEndDate: Optional[str] = None  # 修改结束时间，格式：yyyy-MM-dd HH:mm:ss
    currencyCode: Optional[str] = (
        None  # 货币种类: 原币种【默认】 CNY USD EUR JPY AUD CAD MXN GBP INR AED SGD SAR BRL SEK PLN TRY HKD
    )
    searchField: Optional[str] = (
        None  # 查询索引字段: order_id 订单号【默认】 seller_sku MSKU asin ASIN parent_asin 父ASIN local_sku SKU local_name 品名gmt_
    )
    searchValue: Optional[list] = None  # 查询索引字段值
    sortField: Optional[str] = None  # 参与排序字段
    sortType: Optional[str] = None  # 排序方式
    settlementStatus: Optional[list] = None  # 结算状态 Open 待结算 Pending 结算中 Closed 已结算 Reconciled 已对账
    fundTransferStatus: Optional[list] = None  # 转账状态: Succeeded 已转账 Processing 转帐中 Failed 失败 Unknown 未知
    accountType: Optional[list] = None  # 账单类型: Standard Invoiced Electronic COD PayWithAmazon
    eventSource: Optional[list] = None  # 费用类型: Transfer Adjustment Debt Refund FBA Inventory Fee Service Fee Order
    fulfillment: Optional[list] = None  # 订单类型: FBA FBA FBM FBM
    principalUids: Optional[list] = None  # listing负责人
    productDeveloperUids: Optional[list] = None  # 开发负责人
    orderStatus: Optional[str] = (
        None  # 交易状态 Deferred 已推迟（结束时间必须要今天才能获取已推迟数据） Disbursed 已发放【默认】 DisbursedAndPreSettled 已发放（含`预结`算） All 全部
    )


class FinanceBdorderRequest(LingXingModel):
    """Request for 查询利润报表-订单.

    POST /bd/profit/report/open/report/order/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_date_field: str  # 时间类型： posted_date_locale 结算时间 fund_transfer_datetime_locale 转账时间 shipment_datetime_locale 发货时间
    start_date: str  # 开始时间
    end_date: str  # 结束时间
    search_field: Optional[str] = (
        None  # 搜索值类型： 亚马逊订单号：order_id MSKU：seller_sku Asin：asin 父asin：parent_asin SKU：local_sku 品名：local_name
    )
    search_value: Optional[list] = None  # 搜索的值
    currency_code: Optional[str] = None  # 币种code
    account_type: Optional[str] = None  # 报告类型： Standard Invoiced Electronic COD PayWithAmazon
    settlement_status: Optional[list] = None  # 结算状态： 待结算：["Open", "Pending"] 已结算：["Closed"]
    fund_transfer_status: Optional[list] = (
        None  # 转账状态： 已转帐 Succeeded 转帐中 Processing 失败 Failed 未知 Unknown
    )
    event_source: Optional[list] = (
        None  # 来源： SellerDealPayment ServiceFee Adjustment Refund SellerReviewEnrollmentPayment RemovalShipmentAdju
    )
    description: Optional[list] = None  # 描述


class FinanceFianceProfitMskuRequest(LingXingModel):
    """Request for 查询利润报表（旧） - MSKU.

    POST /erp/sc/routing/finance/ProfitState/profitMsku
    """

    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20
    currency_type: (
        int  # 币种 :  1 CNY  2 USD  3 EUR  4 JPY  5 AUD  6 CAD  7 MXN  8 GBP  9 INR  10 AED  11 SGD  12 SAR  13 BRL
    )
    sids: str  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    month: str  # 月份


class FinanceProfitasinRequest(LingXingModel):
    """Request for 查询利润报表（旧） - ASIN（父级）.

    POST /erp/sc/routing/finance/ProfitState/profitAsin
    """

    month: str  # 月份
    sids: str  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    currency_type: (
        str  # 币种： 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN
    )
    offset: int  # 分页偏移量
    length: int  # 分页长度


class FinanceProfitasinsonRequest(LingXingModel):
    """Request for 查询利润报表（旧） - ASIN（子级）.

    POST /erp/sc/routing/finance/ProfitState/profitAsinSon
    """

    month: str  # 月份
    sids: str  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    currency_type: (
        str  # 币种： 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15 PLN
    )
    asin: str  # 父级展开查询子级列表时的参数，取值 父级asin
    version: str  # 版本号，没有则传空
    offset: int  # 分页偏移量
    length: int  # 分页长度


class FinanceProfitsettlementRequest(LingXingModel):
    """Request for 查询利润报表（旧）-结算明细.

    POST /erp/sc/routing/finance/ProfitState/profitSettlement
    """

    sids: str  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 结算开始时间筛选
    end_date: str  # 结算结束时间筛选
    currency_type: int  # 币种： 0原币种 1 CNY 2 USD 3 EUR 4 JPY 5 AUD 6 CAD 7 MXN 8 GBP 9 INR 10 AED 11 SGD 12 SAR 13 BRL 14 SEK 15
    send_date_start: Optional[str] = None  # 发货日期开始筛选时间，大于等于结算开始时间
    send_date_end: Optional[str] = None  # 发货日期结束筛选时间，小于等于结算结束时间
    offset: int  # 分页偏移量
    length: int  # 分页长度


class FinanceSettlementsummarylistRequest(LingXingModel):
    """Request for 查询结算中心 - 结算汇总.

    POST /bd/sp/api/open/settlement/summary/list
    """

    offset: Optional[Any] = None  # 分页偏移量
    length: Optional[Any] = None  # 分页长度
    countryCodes: Optional[Any] = None  # 国家，查询亚马逊市场列表接口对应字段mid
    sids: Optional[Any] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    currencyCode: Optional[Any] = None  # 币种
    dateType: Optional[Any] = None  # 时间类型： 0 结算开始时间 1 结算结束时间 2 转账时间
    startDate: Optional[Any] = None  # 开始时间【时间间隔最长不得超过90天】
    endDate: Optional[Any] = None  # 结束时间【时间间隔最长不得超过90天】
    searchField: Optional[Any] = None  # 搜索字段：  id 结算编号 settlement_id 账单编号
    searchValue: Optional[Any] = None  # 搜索值


class FinanceSettlementtransactionlistRequest(LingXingModel):
    """Request for 查询结算中心 - 交易明细.

    POST /bd/sp/api/open/settlement/transaction/detail/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    countryCodes: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: Optional[str] = (
        None  # 开始时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d 【无搜索值时，结算时间、修改时间二选一必填】
    )
    endDate: Optional[str] = (
        None  # 结束时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d 【无搜索值时，结算时间、修改时间二选一必填】
    )
    eventType: Optional[str] = None  # 来源，多个英文用逗号隔开，枚举见附加说明
    type: Optional[str] = None  # 交易类型
    searchField: Optional[str] = (
        None  # 搜索字段： id 结算编号 amazon_order_id 订单编号 primary_id 主键编号【对应本接口返回id值】 settlement_id 账单编号【此项下，结算时间或更新时间必填】
    )
    searchValue: Optional[list] = None  # 搜索值
    gmtModifiedStart: Optional[str] = (
        None  # 修改开始时间（北京时间），格式：Y-m-d H:i:s 【无搜索值时，结算时间、修改时间二选一必填】
    )
    gmtModifiedEnd: Optional[str] = (
        None  # 修改结束时间（北京时间），格式：Y-m-d H:i:s 【无搜索值时，结算时间、修改时间二选一必填】
    )


class FinanceCenterodsdetailqueryRequest(LingXingModel):
    """Request for 查询库存分类账detail数据.

    POST
    """

    sellerIds: List  # 亚马逊店铺id
    startDate: str  # 统计起始日期 Y-m-d 闭区间
    endDate: str  # 统计结束日期 Y-m-d 闭区间
    fnskus: Optional[list] = None  # fnsku列表
    asins: Optional[list] = None  # asin列表
    mskus: Optional[list] = None  # msku列表
    eventTypes: Optional[list] = (
        None  # 事件类型，支持传多值： 01 Shipments 02 CustomerReturns 03 WhseTransfers 04 Receipts 05 VendorReturns 06 Adjustm
    )
    referenceId: Optional[str] = None  # 引用id，支持模糊搜索
    disposition: Optional[str] = None  # 库存类型： 01 SELLABLE 02 UNSELLABLE 03 ALL
    locations: Optional[list] = None  # 国家编码列表
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限1000


class FinanceSummaryqueryRequest(LingXingModel):
    """Request for 查询库存分类账summary数据.

    POST
    """

    sellerIds: List  # 亚马逊店铺id
    queryType: int  # 查询维度：1 按月，2 按天
    startDate: str  # 统计起始日期：月维度：Y-m ，天维度：Y-m-d，闭区间
    endDate: str  # 统计结束日期：月维度：Y-m ，天维度：Y-m-d，闭区间
    fnskus: Optional[list] = None  # fnsku列表
    asins: Optional[list] = None  # asin列表
    mskus: Optional[list] = None  # msku列表
    disposition: Optional[str] = None  # 库存属性：01 SELLABLE，02 UNSELLABLE，03 ALL
    locations: Optional[list] = None  # 国家编码列表
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限1000


class FinanceSettlementReportRequest(LingXingModel):
    """Request for 查询发货结算报告.

    POST
    """

    amazonSellerIds: List  # 亚马逊店铺id
    sids: List  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    timeType: str  # 时间类型： 01 下单时间 02 付款时间 03 发货时间 04 结算时间 05 转账时间 06 更新时间
    filterBeginDate: str  # 开始日期，格式：Y-m-d，双闭区间
    filterEndDate: str  # 结束日期，格式：Y-m-d，双闭区间
    countryCodes: Optional[list] = None  # 国家编码
    orderNumbers: Optional[list] = None  # 订单编号
    shipmentNumbers: Optional[list] = None  # 配送编号
    customNumbers: Optional[list] = None  # 自定义编号
    mskus: Optional[list] = None  # msku
    skus: Optional[list] = None  # sku
    productNames: Optional[list] = None  # 品名
    trackCodes: Optional[list] = None  # 物流追踪编码
    fulfillmentType: Optional[str] = None  # 配送方式【不传默认全部】：   01 FBA
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限1000


class FinanceSettlementExportUrlGetRequest(LingXingModel):
    """Request for 查询settlement下载URL.

    POST
    """

    seller_id: Optional[Any] = None  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    financial_event_group_id: Optional[Any] = None  # 结算汇总财务事件组ID【结算汇总->financialEventGroupId】


class FinanceCostStreamRequest(LingXingModel):
    """Request for 查询FBA成本计价流水.

    POST
    """

    wh_names: Optional[list] = None  # 仓库名
    shop_names: Optional[list] = None  # 店铺名
    skus: Optional[list] = None  # sku
    mskus: Optional[list] = None  # msku
    disposition_types: Optional[list] = None  # 库存属性： 1 可用在途 2 可用 3 次品
    business_types: List  # 出入库类型： 1 期初库存-FBA上月结存 10 调拨入库-FBA补货入库 11 调拨入库-FBA途损补回 12 调拨入库-FBA超签入库 13 调拨入库-FBA超签入库（close后） 14 调拨入
    query_type: str  # 日期查询类型： 01 库存动作日期【对应成本计价详情页面单据日期，即在FBA仓库内发生各项库存动作的日期】 02 结算日期【仅销售、退货场景会存在结算日期，其他库存动作结算日期为空】
    start_date: str  # 起始日期，Y-m-d，不允许跨月
    end_date: str  # 结束日期，Y-m-d，不允许跨月
    business_numbers: Optional[list] = None  # 业务编号
    origin_accounts: Optional[list] = None  # 源头单据号
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认200条


class FinanceInvoiceListRequest(LingXingModel):
    """Request for 查询广告发票列表.

    POST
    """

    offset: Optional[int] = None  # 分页偏移量，默认值0
    length: Optional[int] = None  # 分页大小，默认20
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    mids: Optional[list] = None  # 国家id
    ads_type: Optional[list] = (
        None  # 广告类型： SPONSORED PRODUCTS SPONSORED DISPLAY SPONSORED BRANDS SPONSORED BRANDS VIDEO
    )
    invoice_start_time: str  # 开始时间【发票开具时间】
    invoice_end_time: str  # 结束时间【发票开具时间】
    search_type: Optional[str] = (
        None  # 搜索类型： ads_campaign【对应页面广告活动】 invoice_id【对应发票编号】 msku asin
    )
    search_value: Optional[str] = None  # 搜索值


class FinanceInvoiceCampaignListRequest(LingXingModel):
    """Request for 查询广告发票活动列表.

    POST
    """

    offset: Optional[int] = None  # 分页偏移量，默认值0
    length: Optional[int] = None  # 分页大小，默认20
    invoice_id: str  # 广告发票编号
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    ads_type: Optional[list] = (
        None  # 广告类型： SPONSORED PRODUCTS SPONSORED DISPLAY SPONSORED BRANDS SPONSORED BRANDS VIDEO
    )
    search_type: Optional[str] = None  # 搜索类型： ads_campaign【对应页面广告活动】 item【对应页面承担商品】
    search_value: Optional[str] = None  # 搜索值


class FinanceInvoiceDetailRequest(LingXingModel):
    """Request for 查询广告发票基本信息.

    POST
    """

    invoice_id: str  # 广告发票编号
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】


class FinanceComputeManualRequest(LingXingModel):
    """Request for 立即重算-利润报表数据.

    POST /bd/profit/report/open/report/settle/compute/manual
    """

    date_month: str  # 重算月份，格式：yyyy-MM


class FinanceRequestFundsOrderListRequest(LingXingModel):
    """Request for 查询请款单列表.

    POST /basicOpen/finance/requestFunds/order/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    status: Optional[int] = None  # 状态： 1  待付款 2 已完成 3 已作废 121 待审批 122 已驳回 124 已作废
    search_field_time: Optional[str] = (
        None  # 搜索时间类型： apply_time 申请时间 real_pay_time 实际付款时间 prepay_time 预计付款时间
    )
    start_date: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索字段：purchase_order_sn 关联单据，order_sn  请款单号
    search_value: Optional[str] = None  # 搜索值


class FinanceQueryReceiptFundsListRequest(LingXingModel):
    """Request for 查询收款单列表.

    POST /basicOpen/finance/queryReceiptFundsList
    """

    endDate: Optional[str] = None  # 结束日期，必填，格式：yyyy-MM-dd
    length: Optional[int] = None  # 分页长度，默认20，最大200
    offset: Optional[int] = None  # 分页偏移量，默认0
    searchField: Optional[str] = (
        None  # 搜索字段，必填，枚举值：supplier_name-供应商, order_sn-收款单号, purchase_order_sn-采购单号, purchase_return_order_sn-退货单号,
    )
    searchFieldTime: Optional[str] = None  # 搜索时间字段，枚举值：create_time-申请时间, receipt_time-收款时间
    searchValue: Optional[str] = None  # 搜索值，搜索字段对应的值
    seniorSearchList: Optional[str] = None  # 高级筛选，JSON字符串格式
    startDate: Optional[str] = None  # 开始日期，必填，格式：yyyy-MM-dd
    status: Optional[list] = (
        None  # 状态筛选，String数组，枚举值：1-待收款, 2-已完成, 3-已作废, 121-待审批, 122-已驳回, 124-已作废
    )


class FinanceRequestfundspoolpurchaselistRequest(LingXingModel):
    """Request for 查询请款池 - 货款现结.

    POST /basicOpen/finance/requestFundsPool/purchase/list
    """

    pay_status: Optional[str] = None  # 支付状态【多个使用英文逗号分隔】： 0 未申请 1 已申请 2 部分付款 3 已付清
    time_field: Optional[str] = None  # 时间搜索类型： create_time 创建时间
    start_time: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_time: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索类型： sku SKU order_sn 采购单号
    search_value: Optional[str] = None  # 查询值
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class FinanceRequestfundspoolinboundlistRequest(LingXingModel):
    """Request for 查询请款池 - 货款月结.

    POST /basicOpen/finance/requestFundsPool/inbound/list
    """

    pay_status: Optional[str] = None  # 状态： 0 未申请 10 已申请 20 已付清
    time_field: Optional[str] = None  # 时间搜索类型： create_time 入库时间 prepay_time 应付款日
    start_time: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_time: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索类型： order_sn 入库单号 purchase_order_sn 采购单号 sku SKU
    search_value: Optional[str] = None  # 搜索值
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class FinanceRequestfundspoolprepaylistRequest(LingXingModel):
    """Request for 查询请款池 - 货款预付款.

    POST /basicOpen/finance/requestFundsPool/prepay/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    pay_status: Optional[str] = None  # 支付状态：  0  未申请 1  已申请 2  部分付款 3  已付清
    start_time: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_time: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    time_field: Optional[str] = None  # 时间搜索类型： create_time  创建时间
    search_field: Optional[str] = None  # 搜索类型： purchase_order_sn  采购单号 order_sn  预付款单号
    search_value: Optional[str] = None  # 搜索值


class FinanceRequestfundspoollogisticslistRequest(LingXingModel):
    """Request for 查询请款池-物流请款.

    POST /basicOpen/finance/requestFundsPool/logistics/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    search_field_time: Optional[str] = (
        None  # 时间搜索类型： create_time  费用录入时间   delivery_create_time  发货单创建时间  shipment_time  发货时间  close_time  付清时间
    )
    start_time: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_time: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索类型： order_sn  发货单号  logistics_center_code  物流中心编码
    search_value: Optional[str] = None  # 搜索值


class FinanceRequestfundspoolcustomfeelistRequest(LingXingModel):
    """Request for 查询请款池-其他应付款.

    POST /basicOpen/finance/requestFundsPool/customFee/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    pay_status: Optional[str] = None  # 支付状态【多个状态用英文逗号分隔】： 0 未申请 1 已申请 2 部分付款 3 已付清
    search_field_time: Optional[str] = None  # 时间搜索类型： create_time   创建时间   close_time     付清时间
    start_time: Optional[str] = None  # 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_time: Optional[str] = None  # 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索类型： business_sn   费用单号 custom_fee_sn   其他应付单号
    search_value: Optional[str] = None  # 搜索值


class FinanceRequestfundspoolotherfeelistRequest(LingXingModel):
    """Request for 查询请款池-其他费用.

    POST /basicOpen/finance/requestFundsPool/otherFee/list
    """

    endTime: Optional[str] = None  # 结束时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度
    startTime: Optional[str] = None  # 开始时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度
    length: Optional[int] = None  # 分页长度
    offset: Optional[int] = None  # 分页偏移量
    purchaserIds: Optional[list] = None  # 采购方ID列表，筛选指定采购方的其他费用
    searchField: Optional[str] = (
        None  # 搜索字段，枚举值：order_sn-采购单号, create_username-采购员，配合searchValue使用
    )
    searchFieldTime: Optional[str] = (
        None  # 时间维度，枚举值：create_time-创建时间, close_time-付清时间，默认create_time
    )
    searchValue: Optional[str] = None  # 搜索值，根据searchField字段进行搜索，支持模糊查询
    status: Optional[int] = None  # 付款状态，枚举值：0-查询未付清, 1-查询已付清，不传默认查询全部
    supplierIds: Optional[list] = None  # 应付对象ID列表，筛选指定供应商的其他费用


class FinanceReceivablereportlistRequest(LingXingModel):
    """Request for 应收报告-列表查询.

    POST /bd/sp/api/open/monthly/receivable/report/list
    """

    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    mids: Optional[list] = None  # 国家id
    currencyCode: Optional[str] = None  # 币种code
    archiveStatus: Optional[int] = None  # 对账状态 ： 1   已对账， 0   未对账
    settleMonth: str  # 结算月,格式：Y-m
    sortField: Optional[str] = (
        None  # 排序字段： beginningBalanceCurrencyAmount 期初余额 incomeAmount 收入 refundAmount 退款 spendAmount 支出 other 其他
    )
    sortType: Optional[str] = None  # 排序规则： asc  升序 desc  降序
    receivedState: Optional[int] = None  # 转账/到账金额:  0  不相符 1  相符
    offset: Optional[int] = None  # 分页偏移量， 默认0
    length: Optional[int] = None  # 分页长度，默认20


class FinanceReportlistdetailRequest(LingXingModel):
    """Request for 应收报告-详情-列表.

    POST /bd/sp/api/open/monthly/receivable/report/list/detail
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    currencyCode: str  # 币种code
    settleMonth: str  # 结算月
    searchField: Optional[str] = (
        None  # 搜索值类型： fid 结算编号  settlementId settlementId  sellerSku Msku  localSku sku localName 品名  abstractName
    )
    searchValue: Optional[str] = None  # 搜索值
    offset: Optional[int] = None  # 偏移量
    length: Optional[int] = None  # 分页长度，默认20


class FinanceReportlistdetailinfoRequest(LingXingModel):
    """Request for 应收报告-详情-基础信息.

    POST /bd/sp/api/open/monthly/receivable/report/list/detail/info
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    currencyCode: str  # 币种code
    settleMonth: str  # 结算月


class FinanceOrderProfitListMSKURequest(LingXingModel):
    """Request for 查询订单利润-MSKU.

    POST /basicOpen/finance/mreport/OrderProfit
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限5000
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s
    endDate: str  # 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s
    searchField: Optional[str] = None  # 搜索值类型, 可选值:seller_sku,asin,local_name, local_sku
    searchValue: Optional[list] = None  # 搜索的值
    currencyCode: Optional[str] = (
        None  # 币种code【默认原币种】, 可选值：原币种,CNY,USD,EUR,JPY,AUD,CAD,MXN,GBP,INR,AED,SGD,SAR,BRL,SEK,PLN,TRY,HKD
    )


class FinanceLazadasettlementlistRequest(LingXingModel):
    """Request for 账单明细-LazadaSettlement.

    POST /basicOpen/finance/lazada/settlement/list
    """

    compareLogic: Optional[str] = None  # 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`
    currencyCode: Optional[str] = None  # 目标货币代码（为空则使用原币种）
    endDate: Optional[str] = (
        None  # 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59`
    )
    envKey: Optional[str] = None  # 环境标识
    exportFields: Optional[list] = None  # 导出字段值
    feeNames: Optional[list] = None  # 费用名称数组
    fieldCompares: Optional[list] = None  # 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）
    isInSettlement: Optional[float] = None  # 是否计入结算： `0` 否 `1` 是 `null` 全部
    length: float  # 分页大小，默认 `20`，最大不超过 `200`
    offset: float  # 分页偏移，默认 `0`
    paidStatuses: Optional[list] = None  # 回款状态数组
    platformCode: Optional[str] = None  # 平台码
    searchExactly: Optional[bool] = None  # 是否精确匹配
    searchExactly1: Optional[bool] = None  # 商品搜索是否精确匹配
    searchMultiValue: Optional[list] = None  # 多个搜索值（精确匹配）
    searchMultiValue1: Optional[list] = None  # 商品搜索值（多个，精确匹配）
    searchSingleValue: Optional[str] = None  # 单个搜索值（支持模糊匹配，多个值用逗号分隔）
    searchSingleValue1: Optional[str] = None  # 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔）
    searchType: Optional[float] = (
        None  # 搜索类型： `1` 平台单号 `2` 平台子单号 `3` 交易编号 `4` 支付参考编号 `5` 参考单号
    )
    searchType1: Optional[float] = None  # 商品搜索类型： `11` MSKU ID `12` MSKU `13` 商品名称
    sids: Optional[list] = None  # 店铺 ID 数组
    sites: Optional[list] = None  # 站点数组
    sortField: Optional[str] = None  # 排序字段
    sortType: Optional[str] = None  # 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`
    startDate: Optional[str] = (
        None  # 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00`
    )
    storeTypes: Optional[list] = None  # 店铺类型数组： `1` 跨境店 `2` 本土店
    timeType: Optional[float] = None  # 时间类型： `1` 结算日期 `2` 结算周期 默认 `1`
    transactionTypes: Optional[list] = None  # 交易类型数组


class FinanceLazadapayoutlistRequest(LingXingModel):
    """Request for 回款明细-LazadaPayout.

    POST /basicOpen/finance/lazada/payout/list
    """

    compareLogic: Optional[str] = None  # 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`
    currencyCode: Optional[str] = None  # 目标货币代码（为空则使用原币种）
    endDate: Optional[str] = (
        None  # 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59`
    )
    envKey: Optional[str] = None  # 环境标识
    exportFields: Optional[list] = None  # 导出字段值
    fieldCompares: Optional[list] = None  # 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）
    hasDifference: Optional[bool] = None  # 是否有差额：`true`=有差额，`false`=无差额，`null`=全部
    length: float  # 分页大小，默认 `20`，最大不超过 `200`
    offset: float  # 分页偏移，默认 `0`
    paid: Optional[float] = None  # 支付标志： `0` 未支付 `1` 已支付
    platformCode: Optional[str] = None  # 平台码
    searchExactly: Optional[bool] = None  # 是否精确匹配
    searchMultiValue: Optional[list] = None  # 多个搜索值（精确匹配）
    searchSingleValue: Optional[str] = None  # 单个搜索值（支持模糊匹配，多个值用逗号分隔）
    searchType: Optional[float] = None  # 搜索类型： `1` 回款编号
    sids: Optional[list] = None  # 店铺 ID 数组（全部店铺/指定店铺）
    sites: Optional[list] = None  # 站点数组
    sortField: Optional[str] = None  # 排序字段
    sortType: Optional[str] = None  # 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`
    startDate: Optional[str] = (
        None  # 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00`
    )
    storeTypes: Optional[list] = None  # 店铺类型数组： `1` 跨境店 `2` 本土店
    timeType: Optional[float] = None  # 时间类型： `1` 回款时间 `2` 结算周期 默认 `1`


class FinanceShopeeadjustmentlistRequest(LingXingModel):
    """Request for 账单明细-ShopeeAdjustment.

    POST /basicOpen/finance/shopee/adjustment/list
    """

    adjDimensions: Optional[list] = None  # 调整维度数组（下拉多选）： `Order` `Shop` `other` 其他维度
    adjTypes: Optional[list] = (
        None  # 调整类型数组（下拉多选）： `Refund Amount` `Marketing Fee` `Warehouse Fee` `Other` 其他类型
    )
    compareLogic: Optional[str] = None  # 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`
    currencyCode: Optional[str] = None  # 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）
    endDate: Optional[str] = None  # 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期
    envKey: Optional[str] = None  # 环境标识
    exportFields: Optional[list] = None  # 导出字段值
    fieldCompares: Optional[list] = None  # 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）
    length: float  # 分页大小，默认 `20`，最大不超过 `200`
    offset: float  # 分页偏移，默认 `0`
    platformCode: Optional[str] = None  # 平台码
    searchExactly: Optional[bool] = None  # 是否精确匹配
    searchMultiValue: Optional[list] = None  # 多个搜索值（精确匹配）
    searchSingleValue: Optional[str] = None  # 单个搜索值（支持模糊匹配，多个值用逗号分隔）
    searchType: Optional[float] = None  # 搜索类型： `1` 平台单号
    sids: Optional[list] = None  # 店铺 ID 数组
    sites: Optional[list] = None  # 站点数组
    sortField: Optional[str] = None  # 排序字段
    sortType: Optional[str] = None  # 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`
    startDate: Optional[str] = None  # 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天
    storeTypes: Optional[list] = None  # 店铺类型数组： `1` 跨境店(CB) `2` 本土店(Local)


class FinanceShopeeincomelistRequest(LingXingModel):
    """Request for 账单明细-ShopeeIncome.

    POST /basicOpen/finance/shopee/income/list
    """

    compareLogic: Optional[str] = None  # 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`
    currencyCode: Optional[str] = None  # 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）
    endDate: Optional[str] = None  # 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期
    envKey: Optional[str] = None  # 环境标识
    expandChildren: Optional[bool] = None  # 是否展开子项（商品明细），默认 `true` 展开树形结构
    exportFields: Optional[list] = None  # 导出字段值
    fieldCompares: Optional[list] = None  # 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）
    length: float  # 分页大小，默认 `20`，最大不超过 `200`
    offset: float  # 分页偏移，默认 `0`
    platformCode: Optional[str] = None  # 平台码
    searchExactly: Optional[bool] = None  # 是否精确匹配
    searchExactly1: Optional[bool] = None  # 商品搜索是否精确匹配
    searchMultiValue: Optional[list] = None  # 多个搜索值（精确匹配）
    searchMultiValue1: Optional[list] = None  # 商品搜索值（多个，精确匹配）
    searchSingleValue: Optional[str] = None  # 单个搜索值（支持模糊匹配，多个值用逗号分隔）
    searchSingleValue1: Optional[str] = None  # 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔）
    searchType: Optional[float] = None  # 搜索类型： `1` 平台单号
    searchType1: Optional[float] = (
        None  # 商品搜索类型： `11` MSKU ID `12` MSKU `13` MSKU 名称 `14` 商品ID `15` 全球商品货号 `16` 商品名称
    )
    sids: Optional[list] = None  # 店铺 ID 数组
    sites: Optional[list] = None  # 站点数组
    sortField: Optional[str] = None  # 排序字段
    sortType: Optional[str] = None  # 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`
    startDate: Optional[str] = None  # 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天
    storeTypes: Optional[list] = None  # 店铺类型数组： `1` 跨境店(CB) `2` 本土店(Local)


class FinanceShopeepayoutlistRequest(LingXingModel):
    """Request for 回款明细-ShopeePayout.

    POST /basicOpen/finance/shopee/payout/list
    """

    compareLogic: Optional[str] = None  # 字段比较条件逻辑关系： `AND` 所有条件都满足 `OR` 满足任一条件 默认 `AND`
    currencyCode: Optional[str] = None  # 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算）
    endDate: Optional[str] = None  # 结束时间（拨款时间），格式 `yyyy-MM-dd`，默认当前日期
    envKey: Optional[str] = None  # 环境标识
    exportFields: Optional[list] = None  # 导出字段值
    fieldCompares: Optional[list] = None  # 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定）
    length: float  # 分页大小，默认 `20`，最大不超过 `200`
    offset: float  # 分页偏移，默认 `0`
    platformCode: Optional[str] = None  # 平台码
    searchExactly: Optional[bool] = None  # 是否精确匹配
    searchMultiValue: Optional[list] = None  # 多个搜索值（精确匹配）
    searchSingleValue: Optional[str] = None  # 单个搜索值（支持模糊匹配，多个值用逗号分隔）
    searchType: Optional[str] = None  # 搜索类型： `1` 付款ID
    sids: Optional[list] = None  # 店铺 ID 数组
    sites: Optional[list] = None  # 站点数组
    sortField: Optional[str] = None  # 排序字段
    sortType: Optional[str] = None  # 排序方向： `1` 升序/ASC `0` 降序/DESC 默认 `0`
    startDate: Optional[str] = None  # 开始时间（拨款时间），格式 `yyyy-MM-dd`，默认当前月份第一天
    storeType: Optional[float] = None  # 店铺类型： `1` 跨境店(CB)

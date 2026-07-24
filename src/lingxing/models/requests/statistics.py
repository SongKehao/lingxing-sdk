"""Request models for Statistics APIs (auto-generated from API docs)."""

from typing import List, Optional

from ..common import LingXingModel


class StatisticsAsinDailyListsRequest(LingXingModel):
    """Request for 查询亚马逊销量统计.

    POST /erp/sc/data/sales_report/asinDailyLists
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    event_date: str  # 报表时间【站点时间】，格式：Y-m-d
    asin_type: Optional[int] = None  # 查询维度：【默认1】 1 asin 2 msku
    type: Optional[int] = None  # 类型：【默认1】 1 销售额 2 销量 3 订单量
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class StatisticsAsinListRequest(LingXingModel):
    """Request for 查询产品表现（旧）.

    POST /erp/sc/data/sales_report/asinList
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    asin_type: Optional[int] = None  # 产品表现维度：【默认0】 0 asin 1 父asin
    start_date: str  # 报表时间，格式：Y-m-d，闭区间
    end_date: str  # 报表时间，格式：Y-m-d，开区间
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class StatisticsAsinListNewRequestExtendSearchItem(LingXingModel):
    field: Optional[str] = (
        None  # 筛选字段，对应返回字段的字段名，含义参考返回字段，只支持以下字段： volume order_items amount volume_chain_ratio order_chain_ratio amo
    )
    from_value: Optional[int] = (
        None  # 数值： 1、当exp为gt、lt、ge、le、eq 时，比较值填充至此字段； 2、当exp为range时，左区间值填充至此字段；
    )
    to_value: Optional[int] = None  # 数值，仅当exp为range时，填充右区间值
    exp: Optional[str] = None  # 可取值：range、gt、lt、ge、le、eq，其中range是闭区间


class StatisticsAsinListNewRequest(LingXingModel):
    """Request for 查询产品表现.

    POST /bd/productPerformance/openApi/asinList
    """

    offset: int  # 分页偏移量
    length: int  # 分页长度，最大10000
    sort_field: str  # 排序字段，默认按volume排序，含义参考返回字段，只支持以下字段： volume order_items amount volume_chain_ratio order_chain_ratio am
    sort_type: str  # 排序方式：desc【降序】、asc【升序】，默认desc
    search_field: Optional[str] = (
        None  # 搜索字段，目前支持字段如下： asin parent_asin msku local_sku【sku】 item_name【标题】
    )
    search_value: Optional[list] = None  # 搜索值，最多批量搜索50个
    mid: Optional[int] = None  # 站点id
    sid: dict  # 店铺id，上限200 ，对应查询亚马逊店铺列表接口对应字段【sid】 当单店铺查询时，传入字符串，示例："sid":"5608"; 当多店铺查询时，传入数组，示例："sid":[5609,5608]
    start_date: str  # 开始日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD
    end_date: str  # 结束日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD
    summary_field: str  # 汇总行维度，可取值为： asin parent_asin msku sku
    currency_code: Optional[str] = None  # 货币类型，不传代表原币种，转换仅支持USD、CNY
    is_recently_enum: Optional[bool] = None  # 是否仅查询活跃商品： true 仅活跃【默认值】 false 全部商品
    purchase_status: Optional[int] = (
        None  # 退货退款统计方式： 0 默认值，表示按退货退款的发生时间统计退货退款数据 1 表示按下单时间统计退货退款数据
    )
    extend_search: Optional[List[StatisticsAsinListNewRequestExtendSearchItem]] = None


class StatisticsPerformancetrendbyhourRequest(LingXingModel):
    """Request for 查询asin360小时数据.

    POST /basicOpen/salesAnalysis/productPerformance/performanceTrendByHour
    """

    sids: str  # 店铺id，多个值使用英文逗号隔开，最大上限为200
    date_start: str  # 开始时间，闭区间，格式：Y-m-d
    date_end: str  # 结束时间，闭区间，格式：Y-m-d
    summary_field: str  # 查询维度： parent_asin asin msku sku spu
    summary_field_value: str  # 查询维度值


class StatisticsMonthRefundRequest(LingXingModel):
    """Request for 查询退款量（旧）.

    POST /erp/sc/routing/finance/Refund/profitMonthRefund
    """

    asin_type: str  # 1 asin  2 父asin
    offset: int  # 分页偏移量
    length: int  # 分页条数，上限200
    start_date: str  # 起始日期
    end_date: str  # 结束日期
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    sort_field: Optional[str] = None  # 排序字段：asin
    sort_type: Optional[str] = None  # desc 倒序 asc 顺序


class StatisticsProfitMskuRequest(LingXingModel):
    """Request for 查询利润统计（旧）-MSKU.

    POST /erp/sc/routing/finance/ProfitStatis/profitMsku
    """

    start_date: str  # 起始日期
    end_date: str  # 起始日期
    offset: int  # 分页偏移量
    length: int  # 分页长度，上限200
    sids: Optional[str] = None  # 店铺id，通过逗号分隔可以多选，默认返回全部 ，对应查询亚马逊店铺列表接口对应字段【sid】
    currency_type: Optional[str] = (
        None  # 币种，默认原币种 1 人民币-CNY 2 美元-USD 3 欧元-EUR 4 日元-JPY 5 澳元-AUD 6 加拿大元-CAD 7 墨西哥比索-MXN 8 英镑-GBP 9 印度卢比-INR 10
    )
    sort_field: Optional[str] = None  # 排序字段：asin
    sort_type: Optional[str] = None  # desc:倒序   asc:顺序


class StatisticsStatisticsopenmskuRequest(LingXingModel):
    """Request for 查询利润统计-MSKU.

    POST /bd/profit/statistics/open/msku/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    endDate: str  # 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    searchField: Optional[str] = None  # 搜索值类型：msku
    searchValue: Optional[list] = None  # 搜索值
    currencyCode: Optional[str] = None  # 币种code


class StatisticsStatisticsopenasinRequest(LingXingModel):
    """Request for 查询利润统计-ASIN.

    POST /bd/profit/statistics/open/asin/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    endDate: str  # 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    searchField: Optional[str] = None  # 搜索值类型：asin
    searchValue: Optional[list] = None  # 搜索值
    currencyCode: Optional[str] = None  # 币种code


class StatisticsStatisticsopenparentRequest(LingXingModel):
    """Request for .

    POST /bd/profit/statistics/open/parent/asin/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    endDate: str  # 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    searchField: Optional[str] = None  # 搜索值类型：parent_asin
    searchValue: Optional[list] = None  # 搜索值
    currencyCode: Optional[str] = None  # 币种code


class StatisticsStatisticsopensellerRequest(LingXingModel):
    """Request for 查询利润统计-店铺.

    POST /bd/profit/statistics/open/seller/list
    """

    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，上限10000
    mids: Optional[list] = None  # 站点id
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    startDate: str  # 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    endDate: str  # 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】
    currencyCode: Optional[str] = None  # 币种code


class StatisticsFBAStorageFeeLongTermRequest(LingXingModel):
    """Request for 查询FBA长期仓储费.

    POST /erp/sc/data/fba_report/storageFeeLongTerm
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 收费日期，左闭区间
    end_date: str  # 收费日期，右开区间
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class StatisticsFBAStorageFeeMonthRequest(LingXingModel):
    """Request for 查询FBA月仓储费.

    POST /erp/sc/data/fba_report/storageFeeMonth
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    month: str  # 收费月份，格式：Y-m
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class StatisticsStoreSalesRequest(LingXingModel):
    """Request for 查询店铺汇总销量.

    POST /erp/sc/data/sales_report/sales
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 报表时间，格式：Y-m-d，闭区间
    end_date: str  # 报表时间，格式：Y-m-d，闭区间
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000


class StatisticsLocalAggregateListNewRequest(LingXingModel):
    """Request for 库存报表-本地仓-新报表-汇总.

    POST /inventory/center/openapi/storageReport/local/aggregate/list
    """

    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    sys_wid: Optional[int] = None  # 系统仓库id，多个用英文逗号分隔


class StatisticsLocalDetailListNewRequest(LingXingModel):
    """Request for 库存报表-本地仓-新报表-明细.

    POST /inventory/center/openapi/storageReport/local/detail/page
    """

    offset: int  # 分页页码，默认1
    length: int  # 分页长度，默认15，不超过100
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    sys_wid: Optional[str] = None  # 系统仓库id，多个用英文逗号分隔


class StatisticsLocalAggregateListRequest(LingXingModel):
    """Request for 库存报表-本地仓-历史报表-汇总.

    POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList
    """

    sys_wid: Optional[int] = None  # 领星系统仓库id，多个用英文逗号分隔
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d


class StatisticsLocalDetailListRequest(LingXingModel):
    """Request for 库存报表-本地仓-历史报表-明细.

    POST /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList
    """

    sys_wid: Optional[int] = None  # 系统仓库id，多个用英文逗号分隔
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认15


class StatisticsOverseasAggregateListNewRequest(LingXingModel):
    """Request for 库存报表-海外仓-新报表-汇总.

    POST /inventory/center/openapi/storageReport/overseas/aggregate/list
    """

    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    sys_wid: Optional[str] = None  # 系统仓库id，多个用英文逗号分隔


class StatisticsOverseasDetailListNewRequest(LingXingModel):
    """Request for 库存报表-海外仓-新报表-明细.

    POST /inventory/center/openapi/storageReport/overseas/detail/page
    """

    offset: int  # 页码，默认1
    length: int  # 分页长度，默认15
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    sys_wid: Optional[str] = None  # 系统仓库id，多个以英文逗号分隔


class StatisticsOverseasAggregateListRequest(LingXingModel):
    """Request for 库存报表-海外仓-历史报表-汇总.

    POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList
    """

    sys_wid: Optional[int] = None  # 领星仓库id，多个用英文逗号分隔
    start_date: str  # 开始时间
    end_date: str  # 结束时间


class StatisticsOverseasDetailListRequest(LingXingModel):
    """Request for 库存报表-海外仓-历史报表-明细.

    POST /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList
    """

    sys_wid: Optional[int] = None  # 系统仓库id，多个用英文逗号分隔
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 每页条数，默认15


class StatisticsFbaStockAggregateListNewRequest(LingXingModel):
    """Request for 库存报表-FBA-新版-汇总.

    POST /cost/center/openApi/fba/gather/query
    """

    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认为15
    seller_id: List  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    start_date: str  # 统计起始月份，格式：Y-m
    end_date: str  # 统计结束月份，格式：Y-m


class StatisticsFbaStockDetailListNewRequest(LingXingModel):
    """Request for 库存报表-FBA-新版-明细.

    POST /cost/center/openApi/fba/detail/query
    """

    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认15，最大2100
    start_date: str  # 开始日期，格式：Y-m
    end_date: str  # 结束日期，格式：Y-m
    seller_id: List  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】


class StatisticsFbaStockReportListRequest(LingXingModel):
    """Request for 库存报表-FBA-历史报表-汇总-明细.

    POST /erp/sc/routing/fba/fbaStockReport/getList
    """

    start_month: Optional[str] = None  # 开始月份，默认当前月份
    end_month: Optional[str] = None  # 截至月份，默认当前月份
    seller_id: Optional[str] = None  # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    dimention: Optional[int] = None  # 数据维度： 1 汇总 2 明细【默认值】
    offset: Optional[int] = None  # 分页偏移量【dimention=2 明细维度生效】，默认0
    length: Optional[int] = None  # 分页长度【dimention=2 明细维度生效】，默认20，上限5000
    attribute: Optional[int] = None  # 可售状态：【dimention=2 明细维度生效】 0 不可售 1 可售 2 全部【默认值】


class StatisticsCreateRemovalOrderRequestListsItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    order_type: int  # 移除类型：2 Return，3 Disposal
    country_code: str  # 国家code，查询亚马逊市场列表接口对应【code】字段
    state_or_region: str  # 省州code，查询亚马逊国家下地区列表接口对应【code】字段
    sys_wid: Optional[int] = None  # 系统仓库id，查询仓库列表接口对应【wid】字段
    removal_no: Optional[str] = None  # 移除订单号，最长10位，为空则自动创建订单号
    city: str  # 城市
    address_line1: str  # 地址1
    address_line2: Optional[str] = None  # 地址2
    address_line3: Optional[str] = None  # 地址3
    postal_code: str  # 邮编
    phone: str  # 联系电话
    name: str  # 地址名称
    remark: Optional[str] = None  # 备注
    items: List  # items列表
    items__msku: str  # msku
    items__sellable_quantity: int  # 移除可售数量
    items__unsellable_quantity: int  # 移除不可售数量


class StatisticsCreateRemovalOrderRequest(LingXingModel):
    """Request for 创建移除订单.

    POST /erp/sc/statistic/removalOrder/createAndCommit
    """

    lists: List[StatisticsCreateRemovalOrderRequestListsItem]


class StatisticsReimbursementListRequest(LingXingModel):
    """Request for 查询亚马逊赔偿报告列表.

    POST /basicOpen/openapi/mwsReport/reimbursementList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    search_field: Optional[str] = (
        None  # 搜索字段： reimbursement_id 赔偿编号 amazon_order_id 订单号 asin ASIN msku MSKU fnsku FNSKU item_name 标题
    )
    search_value: Optional[str] = None  # 搜索值
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分割 ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: Optional[str] = None  # 批准日期开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 批准日期结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d


class StatisticsPurchaseReportProductListRequest(LingXingModel):
    """Request for 查询采购报表列表 - 产品.

    POST /basicOpen/report/purchase/product/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    start_date: Optional[str] = None  # 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    time_type: Optional[int] = None  # 时间类型：1 下单时间，2 到货时间
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = (
        None  # 搜索字段名： product_name 品名 sku SKU msku MSKU fnsku FNSKU spu_name 款名 spu SPU
    )
    search_value: Optional[str] = None  # 搜索值


class StatisticsPurchaseReportSupplierListRequest(LingXingModel):
    """Request for 查询采购报表列表 - 供应商.

    POST /basicOpen/report/purchase/supplier/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    start_date: Optional[str] = None  # 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    time_type: Optional[int] = None  # 时间类型： 1 下单时间 2 到货时间
    search_field: Optional[str] = None  # 搜索字段名： order_no 单据号
    search_value: Optional[str] = None  # 搜索值
    product_type: Optional[list] = None  # 产品类型： 1 普通产品 2 组合产品 3 辅料


class StatisticsPurchaseReportBuyerListRequest(LingXingModel):
    """Request for 查询采购报表列表 - 采购员.

    POST /basicOpen/report/purchase/buyer/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    start_date: Optional[str] = None  # 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d
    time_type: Optional[int] = None  # 时间类型：1 下单时间，2 到货时间
    product_type: Optional[list] = None  # 产品类型： 1 普通产品 2 组合产品 3 辅料


class StatisticsOperateloglistRequest(LingXingModel):
    """Request for 查询运营日志.

    POST /basicOpen/operateManage/operateLog/list
    """

    sids: List  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: str  # 搜索类型： asin  ASIN parent_asin  父ASIN msku  MSKU
    search_value: str  # 搜索值
    date_type: str  # 时间类型： 1  日 2  周 3  月
    start_date: str  # 开始时间，闭区间，格式：Y-m-d
    end_date: str  # 结束时间，闭区间，格式：Y-m-d


class StatisticsOperatelogv2listRequest(LingXingModel):
    """Request for 查询运营日志(新).

    POST /basicOpen/operateManage/operateLog/list/v2
    """

    offset: Optional[float] = None  # 分页偏移量，默认为20
    length: Optional[float] = None  # 分页长度，默认为200
    sids: Optional[list] = None  # 店铺列表
    mids: Optional[list] = None  # 国家列表
    start_date: str  # 开始时间，格式：yyyy-mm-dd
    end_date: str  # 结束时间，格式：yyyy-mm-dd
    search_field: Optional[str] = None  # 搜索条件： asin ASIN parent_asin 父ASIN msku MSKU【默认】
    search_value: Optional[list] = None  # 搜索值
    summary_type: str  # 日志维度： asin ASIN parent_asin 父ASIN msku MSKU


class StatisticsReturnOrderAnalysisListsRequest(LingXingModel):
    """Request for 统计-查询退货分析.

    POST /basicOpen/salesAnalysis/returnOrder/analysisLists
    """

    endDate: Optional[str] = None  # 结束日期，格式：yyyy-MM-dd，与startDate配合使用，最多支持366天范围
    length: Optional[int] = None  # 分页长度，每页数据条数
    offset: Optional[int] = None  # 分页偏移量，当前页码
    startDate: Optional[str] = None  # 开始日期，格式：yyyy-MM-dd，与endDate配合使用，最多支持366天范围
    asinType: Optional[str] = (
        None  # 维度类型，枚举值：msku, asin, parentAsin, sku, spu（注意：不支持sid、country、category、band）
    )
    dateType: Optional[int] = None  # 时间类型，枚举值：0-退货时间, 1-下单时间
    mids: Optional[list] = None  # 国家ID列表（mid）
    principalUid: Optional[list] = None  # 负责人ID列表
    searchField: Optional[str] = (
        None  # 搜索字段类型，枚举值：msku-MSKU, asin-ASIN, parentAsin-父ASIN, localSku-SKU, localName-品名, spu-SPU, spuName-款名
    )
    searchValue: Optional[list] = None  # 搜索值列表，与searchField配合使用
    sortField: Optional[str] = (
        None  # 排序字段，枚举值：curReturnGoodsCount-退货量, returnGoodsCountRatio-退货量环比, curVolume-销量, curReturnGoodsVolumeRat
    )
    sortType: Optional[str] = None  # 排序类型，枚举值：ASC-升序, DESC-降序
    storeId: Optional[list] = None  # 店铺ID列表


class StatisticsPlatformStatisticsSaleStatPageListV2Request(LingXingModel):
    """Request for 查询销量统计列表v2.

    POST /basicOpen/platformStatisticsV2/saleStat/pageList
    """

    start_date: str  # 开始日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天
    end_date: str  # 结束日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天
    result_type: str  # 汇总类型：  1 销量  2 订单量  3 销售额
    date_unit: str  # 统计时间指标： 1 年  2 月  3 周  4 日
    page: Optional[int] = None  # 分页页码，默认1
    length: Optional[int] = None  # 分页大小，默认20
    data_type: str  # 统计数据维度：  1 ASIN  2 父体  3 MSKU  4 SKU  5 SPU  6 店铺
    sids: Optional[list] = (
        None  # 店铺id，多个使用英文逗号分隔。 如果id属于亚马逊店铺id，则对应查询亚马逊店铺列表接口对应字段【sid】  如果id属于多平台店铺id，则对应查询多平台店铺信息接口对应字段【store_id】
    )


class StatisticsVctrafficlistRequest(LingXingModel):
    """Request for VC报表-流量报表.

    POST /basicOpen/vc/report/traffic/list
    """

    sid: int  # 店铺id
    startDate: Optional[str] = None  # 开始日期，yyyy-MM-dd
    endDate: Optional[str] = None  # 结束日期，yyyy-MM-dd
    offset: int  # 偏移量，默认0
    length: int  # 长度，最大200
    asinList: Optional[list] = None  # 指定asin列表


class StatisticsVcsaleslistRequest(LingXingModel):
    """Request for VC报表-销量报表.

    POST /basicOpen/vc/report/sales/list
    """

    sid: int  # 店铺id
    view: str  # 视图： sourcing manufacturing
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20，最大200
    startDate: Optional[str] = None  # 开始时间，yyyy-MM-dd
    endDate: Optional[str] = None  # 结束时间，yyyy-MM-dd
    asinList: Optional[list] = None  # 指定asin列表


class StatisticsVcrealtimesaleslistRequest(LingXingModel):
    """Request for VC报表-实时销量报表.

    POST /basicOpen/vc/report/realtimeSales/list
    """

    sid: int  # 店铺id
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20，最大200
    startDate: Optional[str] = None  # 开始时间，yyyy-MM-dd
    endDate: Optional[str] = None  # 结束时间，yyyy-MM-dd
    dateType: Optional[int] = None  # 日期类型： 1=站点时间 2=UTC时间 默认1
    asinList: Optional[list] = None  # 指定asin列表


class StatisticsVcnppmlistRequest(LingXingModel):
    """Request for VC报表-产品利润率报表.

    POST /basicOpen/vc/report/nppm/list
    """

    sid: int  # 店铺id
    startDate: Optional[str] = None  # 开始日期，yyyy-MM-dd
    endDate: Optional[str] = None  # 结束日期，yyyy-MM-dd
    offset: int  # 偏移量，默认0
    length: int  # 长度，最大200
    asinList: Optional[list] = None  # 指定asin列表


class StatisticsVcinventorylistRequest(LingXingModel):
    """Request for VC报表-库存报表.

    POST /basicOpen/vc/report/inventory/list
    """

    sid: float  # 店铺id
    startDate: Optional[str] = None  # 开始时间，格式：`yyyy-MM-dd`
    endDate: Optional[str] = None  # 结束时间，格式：`yyyy-MM-dd`
    offset: float  # 偏移量
    length: float  # 长度，最大 `200`
    view: str  # 视图： `sourcing` 货源视图 `manufacturing` 生产视图
    asinList: Optional[list] = None  # 指定asin列表


class StatisticsReportcreatereportexporttaskRequest(LingXingModel):
    """Request for 报告导出 - 创建导出任务.

    POST /basicOpen/report/create/reportExportTask
    """

    seller_id: str  # 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】
    report_type: str  # 亚马逊报表类型【具体类型参看下方附加说明】
    data_start_time: Optional[str] = None  # 亚马逊报表请求开始时间，时间格式：YYYY-MM-DDTHH:MM:SSZ
    data_end_time: Optional[str] = None  # 亚马逊报表请求结束时间，时间格式：YYYY-MM-DDTHH:MM:SSZ
    marketplace_ids: List  # 亚马逊市场id
    region: str  # 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东


class StatisticsReportqueryreportexporttaskRequest(LingXingModel):
    """Request for 报告导出-查询导出任务结果.

    POST /basicOpen/report/query/reportExportTask
    """

    seller_id: str  # 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】
    task_id: str  # 任务id
    region: str  # 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东


class StatisticsAmazonReportExportTaskRequest(LingXingModel):
    """Request for 报告导出 - 报告下载链接续期.

    POST /basicOpen/report/amazonReportExportTask
    """

    region: str  # 店铺所在的地区【对应区域值支持国家见附加说明】： na 北美 eu 欧洲 fe 远东
    seller_id: str  # 亚马逊店铺id，查询亚马逊店铺列表接口对应字段【seller_id】
    report_document_id: str  # 报告文档Id,报告导出-查询导出任务结果接口对应字段【data>>report_document_id】

"""Request models for Service APIs (auto-generated from API docs)."""

from typing import List, Optional

from ..common import LingXingModel


class ServiceListsRequest(LingXingModel):
    """Request for 查询邮件列表.

    POST /erp/sc/data/mail/lists
    """

    flag: str  # 类型： sent 发件 receive 收件
    email: str  # 店铺绑定邮箱
    start_date: str  # 开始日期，格式：yyyy-mm-dd
    end_date: str  # 开始日期，格式：yyyy-mm-dd
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class ServiceDetailRequest(LingXingModel):
    """Request for 查询邮件详情.

    POST /erp/sc/data/mail/detail
    """

    webmail_uuid: str  # 邮件唯一标识


class ServiceReviewRequest(LingXingModel):
    """Request for 查询评价管理-Review.

    POST /erp/sc/v2/data/mws/reviews
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 开始评论时间，闭区间，格式：Y-m-d
    end_date: str  # 结束评论时间，闭区间，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度
    date_field: Optional[str] = None  # 时间类型: review_date 评价时间【默认值】 create_time 创建时间


class ServiceReviewv2Request(LingXingModel):
    """Request for 查询评论管理 - Review(新).

    POST /basicOpen/openapi/service/v3/data/mws/reviews
    """

    sort_field: Optional[str] = None  # 排序类型
    sort_type: Optional[str] = None  # 排序
    sids: Optional[str] = None  # 店铺id，多个用逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    mids: Optional[str] = None  # 站点id，多个用逗号分隔
    principal_uids: Optional[str] = None  # lisitng负责人，多个用逗号分隔
    search_field: Optional[str] = (
        None  # 搜索字段: asin ASIN parent_asin 父ASIN remark 备注 amazon_order_id 订单号 author 买家信息 review_id  Review ID buy
    )
    search_value: Optional[str] = None  # 搜索值
    date_field: str  # 时间搜索类型: review_time 评价时间 create_time 创建时间 last_update_time 更新时间
    start_date: str  # 开始时间，格式：Y-m-d
    end_date: str  # 结束时间，格式：Y-m-d
    status: Optional[str] = None  # 状态，多个用逗号分隔: 0 待处理 1 处理中 2 已完成
    star: Optional[str] = None  # 星级，多个用逗号分隔
    review_modified_status: Optional[str] = None  # 内容，多个用逗号分隔: -1 已删除 0 未标识 1 已变更
    mark: Optional[str] = None  # 标识，多个用逗号分隔: is_vp is_er is_topc is_topr is_vine
    cs_principal_uids: Optional[str] = None  # 处理人，多个用逗号分隔
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    cids: Optional[str] = None  # 分类id，多个用逗号分隔
    global_tag_ids: Optional[str] = None  # 标签id，多个用逗号分隔
    match_types: Optional[str] = None  # 匹配类型，多个用逗号分隔，默认传空字符串


class ServiceFeedbackListMwsRequest(LingXingModel):
    """Request for 查询评价管理 1-3星Feedback列表.

    POST /erp/sc/cs/feedback/listMws
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 评论开始日期，格式：Y-m-d
    end_date: str  # 评论结束日期，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20


class ServiceFeedbackListRequest(LingXingModel):
    """Request for 查询评价管理 4-5星Feedback列表.

    POST /erp/sc/cs/feedback/list
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 评论开始日期，格式：Y-m-d
    end_date: str  # 评论结束日期，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20


class ServiceReviewlistsRequest(LingXingModel):
    """Request for 查询评价统计-Review列表.

    GET /erp/sc/v2/cs/reviewReport/lists
    """

    start_date: str  # 开始时间【时间间隔不超过1年】，格式：Y-m-d
    end_date: str  # 结束时间【时间间隔不超过1年】，格式：Y-m-d
    sid: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class ServiceReviewdetailRequest(LingXingModel):
    """Request for 查询评价统计-Review每日新增数.

    POST /erp/sc/cs/reviewReport/detail
    """

    mid: int  # 国家id
    asin: str  # asin
    start_date: str  # 开始时间【时间间隔不超过1年】
    end_date: str  # 结束时间【时间间隔不超过1年】


class ServiceFeedbacklistsRequest(LingXingModel):
    """Request for 查询评价统计-Feedback列表.

    POST /erp/sc/cs/feedbackReport/lists
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20
    start_date: str  # 开始时间【时间间隔不超过1年】，格式：Y-m-d
    end_date: str  # 结束时间【时间间隔不超过1年】，格式：Y-m-d


class ServiceFeedbackdetailRequest(LingXingModel):
    """Request for 查询评价统计-Feedback每日新增数.

    POST /erp/sc/cs/feedbackReport/detail
    """

    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 开始时间【时间间隔不超过1年】
    end_date: str  # 结束时间【时间间隔不超过1年】


class ServiceCustomerListRequest(LingXingModel):
    """Request for 查询客户列表（旧）.

    POST /bd/crm/open/api/customer/list
    """

    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    time_search_type: int  # 时间筛选查询类型： 1 首次购买时间 2 最近购买时间
    start_date: str  # 开始时间
    end_date: str  # 结束时间
    offset: Optional[int] = None  # 页码，默认1
    length: Optional[int] = None  # 每页条数，默认100


class ServiceAfterSalesWorkOrderListRequest(LingXingModel):
    """Request for 查询售后工单列表.

    POST /pb/mp/returns/workOrder/list
    """

    date_type: str  # 时间类型： create_time 创建时间 complete_time 完成时间
    start_time: str  # 开始时间，闭区间，格式：Y-m-d H:i:s
    end_time: str  # 结束时间，闭区间，格式：Y-m-d H:i:s
    offset: int  # 分页偏移量
    length: int  # 分页长度，上限500


class ServiceStoreperformancelistRequest(LingXingModel):
    """Request for 查询店铺绩效列表.

    POST /basicOpen/customerService/storeTarget/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    search_field_time: Optional[str] = None  # 搜索时间类型： pull_date 报表获取时间  update_date 更新时间
    search_time: Optional[str] = None  # 搜索时间，格式：Y-m-d
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    anomaly_indicator: Optional[list] = (
        None  # 异常指标： commodity_policy_compliance 商品政策合规性 on_time_delivery 准时交货率 valid_tracking 有效追踪率 pre_fulfillmen
    )


class ServicePerformanceNoticeDetailRequest(LingXingModel):
    """Request for 查询店铺绩效详情.

    POST /basicOpen/customerService/storeTarget/detail
    """

    pullDate: Optional[str] = None  # 报表更新日期，必填，日期格式：yyyy-MM-dd
    sid: Optional[int] = None  # 店铺ID，必填


class ServiceVoiceofbuyerlistRequest(LingXingModel):
    """Request for 查询买家之声列表.

    POST /basicOpen/customerService/voiceOfBuyer/list
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    fulfillment_channel: Optional[str] = None  # 配送方式： FBA  FBA MFN  FBM
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    pxc_health: Optional[list] = None  # 满意度状况： -1  反馈不足 0  极差 1  不合格 2  一般 3  良好 4  极好
    search_field: Optional[str] = None  # 搜索类型： asin  ASIN msku   MSKU sku   SKU
    search_value: Optional[list] = None  # 搜索值
    return_badge: Optional[list] = None  # 退货标记， Yes No At_Risk


class ServiceCustomerservicermamanagelistRequest(LingXingModel):
    """Request for 查询RMA管理.

    POST /basicOpen/customerService/rmaManage/list
    """

    sid: List  # 店铺id，支持多选，数组
    searchTimeFiled: str  # 搜索时间类型：1创建时间 2.操作时间   createTime operationTime
    startTime: str  # 创建或完成时间（开始），精确到年月日，无默认
    endTime: str  # 创建或完成时间（开始），精确到年月日，无默认
    searchValue: List  # 搜索值，msku和asin支持多个搜索，数组
    searchField: str  # 搜索字段：msku，asin，sku
    sortColumn: str  # 排序字段
    sortType: str  # 排序方式
    pageNum: float  # 页码
    pageSize: float  # 每页数量


class ServiceCustomerservicecrmcustomerindexRequest(LingXingModel):
    """Request for 查询客户列表（新）.

    POST /basicOpen/customerService/crm/customer/index
    """

    sort_field: Optional[str] = None  # 结果按字段排序
    sort_type: Optional[str] = None  # desc=倒序，asc=升序
    date_field: Optional[str] = None  # 时间筛选查询类型，1：首次购买时间 ，2：最近购买时间
    start_date: Optional[str] = None  # 筛选开始时间
    end_date: Optional[str] = None  # 筛选结束时间
    currency_type: Optional[float] = None  # 币种，0=原币种，1=CNY，2=USD
    search_field: Optional[str] = None  # 支持搜索的字段 buyer_email、buyer_name
    offset: Optional[float] = None  # 偏移量
    length: Optional[float] = None  # 分页长度 ，默认20 ，上限200
    search_value: Optional[str] = None  # 搜索值
    sids: Optional[str] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】


class ServicePerformanceNoticeListRequest(LingXingModel):
    """Request for 查询业绩通知列表.

    POST /basicOpen/customerService/performanceNotice/list
    """

    sid: float  # 店铺id
    status: Optional[list] = None  # 处理状态：0（无），1（待处理），2（已处理），3（无需处理）
    startDate: Optional[str] = None  # 开始时间 YYYY-MM-DD
    endDate: Optional[str] = None  # 结束时间 YYYY-MM-DD
    searchField: Optional[str] = None  # 搜索字段,subject 邮件主题,content 邮件内容
    searchValue: Optional[str] = None  # 搜索值
    mailTagIds: Optional[list] = None  # 邮件标签 id
    isRead: Optional[float] = None  # 是否已读，-1 全部，0 未读，1 已读
    offset: Optional[float] = None  # 偏移量
    length: Optional[float] = None  # 分页长度

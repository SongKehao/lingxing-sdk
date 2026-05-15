"""客服 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class CustomerServiceEndpoints(BaseEndpoint):
    """领星客服 API (16个接口)."""

    async def feedback_list(self, **kwargs) -> list | dict:
        """查询评价管理 4-5星Feedback列表.

POST /erp/sc/cs/feedback/list

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    start_date: 评论开始日期，格式：Y-m-d (required), string.
    end_date: 评论结束日期，格式：Y-m-d (required), string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/cs/feedback/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_list_mws(self, **kwargs) -> list | dict:
        """查询评价管理 1-3星Feedback列表.

POST /erp/sc/cs/feedback/listMws

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    start_date: 评论开始日期，格式：Y-m-d (required), string.
    end_date: 评论结束日期，格式：Y-m-d (required), string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/cs/feedback/listMws", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def performance_notice_detail(self, **kwargs) -> list | dict:
        """查询店铺绩效详情.

POST /basicOpen/customerService/storeTarget/detail

Args:
    pullDate: 报表更新日期，必填，日期格式：yyyy-MM-dd, string.
    sid: 店铺ID，必填, long."""
        resp = await self._post("/basicOpen/customerService/storeTarget/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def performance_notice_list(self, **kwargs) -> list | dict:
        """查询业绩通知列表.

POST /basicOpen/customerService/performanceNotice/list

Args:
    sid: 店铺id (required), number.
    status: 处理状态：0（无），1（待处理），2（已处理），3（无需处理）, array.
    startDate: 开始时间 YYYY-MM-DD, string.
    endDate: 结束时间 YYYY-MM-DD, string.
    searchField: 搜索字段,subject 邮件主题,content 邮件内容, string.
    searchValue: 搜索值, string.
    mailTagIds: 邮件标签 id, array.
    isRead: 是否已读，-1 全部，0 未读，1 已读, number.
    offset: 偏移量, number.
    length: 分页长度, number."""
        resp = await self._post("/basicOpen/customerService/performanceNotice/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def customer_service_crmcustomer_index(self, **kwargs) -> list | dict:
        """查询客户列表（新）.

POST /basicOpen/customerService/crm/customer/index

Args:
    sort_field: 结果按字段排序, string.
    sort_type: desc=倒序，asc=升序, string.
    date_field: 时间筛选查询类型，1：首次购买时间 ，2：最近购买时间, string.
    start_date: 筛选开始时间, string.
    end_date: 筛选结束时间, string.
    currency_type: 币种，0=原币种，1=CNY，2=USD, number.
    search_field: 支持搜索的字段 buyer_email、buyer_name, string.
    offset: 偏移量, number.
    length: 分页长度 ，默认20 ，上限200, number.
    search_value: 搜索值, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, string."""
        resp = await self._post("/basicOpen/customerService/crm/customer/index", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def customer_service_rma_manage_list(self, **kwargs) -> list | dict:
        """查询RMA管理.

POST /basicOpen/customerService/rmaManage/list

Args:
    sid: 店铺id，支持多选，数组 (required), array.
    searchTimeFiled: 搜索时间类型：1创建时间 2.操作时间   createTime operationTime (required), string.
    startTime: 创建或完成时间（开始），精确到年月日，无默认 (required), string.
    endTime: 创建或完成时间（开始），精确到年月日，无默认 (required), string.
    searchValue: 搜索值，msku和asin支持多个搜索，数组 (required), array.
    searchField: 搜索字段：msku，asin，sku (required), string.
    sortColumn: 排序字段 (required), string.
    sortType: 排序方式 (required), string.
    pageNum: 页码 (required), number.
    pageSize: 每页数量 (required), number."""
        resp = await self._post("/basicOpen/customerService/rmaManage/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def detail(self, **kwargs) -> list | dict:
        """查询邮件详情.

POST /erp/sc/data/mail/detail

Args:
    webmail_uuid: 邮件唯一标识 (required), string."""
        resp = await self._post("/erp/sc/data/mail/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_detail(self, **kwargs) -> list | dict:
        """查询评价统计-Feedback每日新增数.

POST /erp/sc/cs/feedbackReport/detail

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    start_date: 开始时间【时间间隔不超过1年】 (required), string.
    end_date: 结束时间【时间间隔不超过1年】 (required), string."""
        resp = await self._post("/erp/sc/cs/feedbackReport/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def feedback_lists(self, **kwargs) -> list | dict:
        """查询评价统计-Feedback列表.

POST /erp/sc/cs/feedbackReport/lists

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    start_date: 开始时间【时间间隔不超过1年】，格式：Y-m-d (required), string.
    end_date: 结束时间【时间间隔不超过1年】，格式：Y-m-d (required), string."""
        resp = await self._post("/erp/sc/cs/feedbackReport/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def lists(self, **kwargs) -> list | dict:
        """查询邮件列表.

POST /erp/sc/data/mail/lists

Args:
    flag: 类型： sent 发件 receive 收件 (required), string.
    email: 店铺绑定邮箱 (required), string.
    start_date: 开始日期，格式：yyyy-mm-dd (required), string.
    end_date: 开始日期，格式：yyyy-mm-dd (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/data/mail/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review(self, **kwargs) -> list | dict:
        """查询评价管理-Review.

POST /erp/sc/v2/data/mws/reviews

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    start_date: 开始评论时间，闭区间，格式：Y-m-d (required), string.
    end_date: 结束评论时间，闭区间，格式：Y-m-d (required), string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度 (required), int.
    date_field: 时间类型: review_date 评价时间【默认值】 create_time 创建时间, string."""
        resp = await self._post("/erp/sc/v2/data/mws/reviews", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_detail(self, **kwargs) -> list | dict:
        """查询评价统计-Review每日新增数.

POST /erp/sc/cs/reviewReport/detail

Args:
    mid: 国家id (required), int.
    asin: asin (required), string.
    start_date: 开始时间【时间间隔不超过1年】 (required), string.
    end_date: 结束时间【时间间隔不超过1年】 (required), string."""
        resp = await self._post("/erp/sc/cs/reviewReport/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_lists(self, **kwargs) -> list | dict:
        """查询评价统计-Review列表.

POST /erp/sc/v2/cs/reviewReport/lists

Args:
    start_date: 开始时间【时间间隔不超过1年】，格式：Y-m-d (required), string.
    end_date: 结束时间【时间间隔不超过1年】，格式：Y-m-d (required), string.
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/v2/cs/reviewReport/lists", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def review_v2(self, **kwargs) -> list | dict:
        """查询评论管理 - Review(新).

POST /basicOpen/openapi/service/v3/data/mws/reviews

Args:
    sort_field: 排序类型, string.
    sort_type: 排序, string.
    sids: 店铺id，多个用逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    mids: 站点id，多个用逗号分隔, string.
    principal_uids: lisitng负责人，多个用逗号分隔, string.
    search_field: 搜索字段: asin ASIN parent_asin 父ASIN remark 备注 amazon_order_id 订单号 author 买家信息 review_id  Review ID buyer_email 买家 last_title 评价标题, string.
    search_value: 搜索值, string.
    date_field: 时间搜索类型: review_time 评价时间 create_time 创建时间 last_update_time 更新时间 (required), string.
    start_date: 开始时间，格式：Y-m-d (required), string.
    end_date: 结束时间，格式：Y-m-d (required), string.
    status: 状态，多个用逗号分隔: 0 待处理 1 处理中 2 已完成, string.
    star: 星级，多个用逗号分隔, string.
    review_modified_status: 内容，多个用逗号分隔: -1 已删除 0 未标识 1 已变更, string.
    mark: 标识，多个用逗号分隔: is_vp is_er is_topc is_topr is_vine, string.
    cs_principal_uids: 处理人，多个用逗号分隔, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    cids: 分类id，多个用逗号分隔, string.
    global_tag_ids: 标签id，多个用逗号分隔, string.
    match_types: 匹配类型，多个用逗号分隔，默认传空字符串, string."""
        resp = await self._post("/basicOpen/openapi/service/v3/data/mws/reviews", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def store_performance_list(self, **kwargs) -> list | dict:
        """查询店铺绩效列表.

POST /basicOpen/customerService/storeTarget/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    search_field_time: 搜索时间类型： pull_date 报表获取时间  update_date 更新时间, string.
    search_time: 搜索时间，格式：Y-m-d, string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    anomaly_indicator: 异常指标： commodity_policy_compliance 商品政策合规性 on_time_delivery 准时交货率 valid_tracking 有效追踪率 pre_fulfillment_cancellation 预配送取消率 late_shipment 迟发率  invoice_defect 发票缺陷率 fba_order_with_defect FBA订单缺陷率 order_with_defect FBM订单缺陷率, array."""
        resp = await self._post("/basicOpen/customerService/storeTarget/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def voice_of_buyer_list(self, **kwargs) -> list | dict:
        """查询买家之声列表.

POST /basicOpen/customerService/voiceOfBuyer/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    fulfillment_channel: 配送方式： FBA  FBA MFN  FBM, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    pxc_health: 满意度状况： -1  反馈不足 0  极差 1  不合格 2  一般 3  良好 4  极好, array.
    search_field: 搜索类型： asin  ASIN msku   MSKU sku   SKU, string.
    search_value: 搜索值, array.
    return_badge: 退货标记， Yes No At_Risk, array."""
        resp = await self._post("/basicOpen/customerService/voiceOfBuyer/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

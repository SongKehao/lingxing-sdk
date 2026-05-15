"""Customer service API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class CustomerServiceEndpoints:
    """Customer service API endpoints."""

    def __init__(self, openapi: OpenApiBase):
        """
        初始化客服端点

        Args:
            openapi: OpenAPI基础客户端实例
        """
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== 客户管理 ====================

    async def get_customer_list_new(
        self,
        access_token: str,
        sids: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        date_field: str | None = None,
        sort_field: str | None = None,
        sort_type: str | None = None,
        currency_type: int | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询客户列表（新）

        API: POST /basicOpen/customerService/crm/customer/index

        Args:
            access_token: 访问令牌
            sids: 店铺ID，逗号分隔
            start_date: 筛选开始时间，格式 YYYY-MM-DD
            end_date: 筛选结束时间，格式 YYYY-MM-DD
            date_field: 时间筛选查询类型，1=首次购买时间，2=最近购买时间
            sort_field: 结果按字段排序（如 order_items）
            sort_type: 排序方式，desc=倒序，asc=升序
            currency_type: 币种，0=原币种，1=CNY，2=USD
            search_field: 搜索字段，支持 buyer_email、buyer_name
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含客户列表数据

        Example:
            >>> result = await cs.get_customer_list_new(
            ...     access_token="xxx",
            ...     sids="17",
            ...     start_date="2021-01-31",
            ...     end_date="2021-03-02",
            ...     search_field="buyer_email",
            ...     search_value="test@marketplace.amazon.com"
            ... )
        """
        logger.debug("Fetching customer list (new): sids=%s", sids)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if start_date:
            req_body["start_date"] = start_date
        if end_date:
            req_body["end_date"] = end_date
        if date_field:
            req_body["date_field"] = date_field
        if sort_field:
            req_body["sort_field"] = sort_field
        if sort_type:
            req_body["sort_type"] = sort_type
        if currency_type is not None:
            req_body["currency_type"] = currency_type
        if search_field:
            req_body["search_field"] = search_field
        if search_value:
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/crm/customer/index",
            req_body=req_body
        )

    # ==================== 评价管理 - Feedback ====================

    async def get_feedback_list_low_star(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询1-3星Feedback列表

        API: POST /erp/sc/cs/feedback/list

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 评论开始日期，格式 YYYY-MM-DD
            end_date: 评论结束日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含1-3星Feedback列表

        Example:
            >>> result = await cs.get_feedback_list_low_star(
            ...     access_token="xxx",
            ...     sid=1,
            ...     start_date="2024-01-01",
            ...     end_date="2024-08-05"
            ... )
        """
        logger.debug("Fetching 1-3 star feedback list: sid=%s", sid)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/cs/feedback/list",
            req_body=req_body
        )

    async def get_feedback_list_high_star(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询4-5星Feedback列表

        API: POST /erp/sc/cs/feedback/listMws

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 评论开始日期，格式 YYYY-MM-DD
            end_date: 评论结束日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含4-5星Feedback列表

        Example:
            >>> result = await cs.get_feedback_list_high_star(
            ...     access_token="xxx",
            ...     sid=1,
            ...     start_date="2024-01-01",
            ...     end_date="2024-08-05"
            ... )
        """
        logger.debug("Fetching 4-5 star feedback list: sid=%s", sid)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/cs/feedback/listMws",
            req_body=req_body
        )

    # ==================== 评价管理 - Review ====================

    async def get_review_list_new(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sids: str | None = None,
        mids: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        date_field: str = "review_time",
        sort_field: str | None = None,
        sort_type: str | None = None,
        status: str | None = None,
        star: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询评论管理 - Review(新)

        API: POST /basicOpen/openapi/service/v3/data/mws/reviews

        Args:
            access_token: 访问令牌
            start_date: 开始时间，格式 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD
            sids: 店铺ID，多个用逗号分隔
            mids: 站点ID，多个用逗号分隔
            search_field: 搜索字段（asin/parent_asin/remark/amazon_order_id/author/review_id/buyer_email/last_title）
            search_value: 搜索值
            date_field: 时间搜索类型（review_time/create_time/last_update_time）
            sort_field: 排序类型（如 review_date）
            sort_type: 排序方式（desc/asc）
            status: 状态，多个用逗号分隔（0=待处理,1=处理中,2=已完成）
            star: 星级，多个用逗号分隔（1,2,3,4,5）
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数（principal_uids, review_modified_status, mark, cs_principal_uids, cids, global_tag_ids, match_types）

        Returns:
            ResponseResult: 包含Review列表

        Example:
            >>> result = await cs.get_review_list_new(
            ...     access_token="xxx",
            ...     start_date="2024-06-06",
            ...     end_date="2024-09-04",
            ...     search_field="review_id",
            ...     search_value="R1KKLEHWNZWH05"
            ... )
        """
        logger.debug("Fetching review list (new): start=%s, end=%s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "date_field": date_field,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if mids:
            req_body["mids"] = mids
        if search_field:
            req_body["search_field"] = search_field
        if search_value:
            req_body["search_value"] = search_value
        if sort_field:
            req_body["sort_field"] = sort_field
        if sort_type:
            req_body["sort_type"] = sort_type
        if status:
            req_body["status"] = status
        if star:
            req_body["star"] = star

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/service/v3/data/mws/reviews",
            req_body=req_body
        )

    # ==================== 评价统计 - Feedback ====================

    async def get_feedback_stats_list(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sid: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询评价统计-Feedback列表

        API: POST /erp/sc/cs/feedbackReport/lists

        Args:
            access_token: 访问令牌
            start_date: 开始时间，格式 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD
            sid: 店铺ID列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含Feedback统计列表

        Example:
            >>> result = await cs.get_feedback_stats_list(
            ...     access_token="xxx",
            ...     start_date="2024-01-01",
            ...     end_date="2024-08-05",
            ...     sid=[1, 2]
            ... )
        """
        logger.debug("Fetching feedback stats list: start=%s, end=%s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sid:
            req_body["sid"] = sid

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/cs/feedbackReport/lists",
            req_body=req_body
        )

    async def get_feedback_daily_stats(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询评价统计-Feedback每日新增数

        API: POST /erp/sc/cs/feedbackReport/detail

        注意: 时间间隔不超过1年

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 开始时间，格式 YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含每日Feedback新增数据

        Example:
            >>> result = await cs.get_feedback_daily_stats(
            ...     access_token="xxx",
            ...     sid=1,
            ...     start_date="2024-01-01 00:00:00",
            ...     end_date="2024-08-05 00:00:00"
            ... )
        """
        logger.debug("Fetching feedback daily stats: sid=%s", sid)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/cs/feedbackReport/detail",
            req_body=req_body
        )

    # ==================== 评价统计 - Review ====================

    async def get_review_stats_list(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sid: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询评价统计-Review列表

        API: GET /erp/sc/v2/cs/reviewReport/lists
        注意: 此接口为GET请求，参数作为query参数拼接在url上

        Args:
            access_token: 访问令牌
            start_date: 开始时间，格式 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD
            sid: 店铺ID列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含Review统计列表

        Example:
            >>> result = await cs.get_review_stats_list(
            ...     access_token="xxx",
            ...     start_date="2024-09-01",
            ...     end_date="2025-05-01",
            ...     sid=[1, 136, 139]
            ... )
        """
        logger.debug("Fetching review stats list: start=%s, end=%s", start_date, end_date)

        # GET请求参数构建
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sid:
            params["sid"] = sid

        return await self.openapi.request(
            access_token=access_token,
            route_name="/erp/sc/v2/cs/reviewReport/lists",
            method="GET",
            req_body=params
        )

    async def get_review_daily_stats(
        self,
        access_token: str,
        mid: int,
        asin: str,
        start_date: str,
        end_date: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询评价统计-Review每日新增数

        API: POST /erp/sc/cs/reviewReport/detail

        注意: 时间间隔不超过1年

        Args:
            access_token: 访问令牌
            mid: 站点ID（国家ID）
            asin: ASIN
            start_date: 开始时间，格式 YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD HH:mm:ss 或 YYYY-MM-DD
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含每日Review新增数据

        Example:
            >>> result = await cs.get_review_daily_stats(
            ...     access_token="xxx",
            ...     mid=1,
            ...     asin="B085NQDDXS",
            ...     start_date="2024-01-01 00:00:00",
            ...     end_date="2024-08-05 00:00:00"
            ... )
        """
        logger.debug("Fetching review daily stats: mid=%s, asin=%s", mid, asin)

        req_body = {
            "mid": mid,
            "asin": asin,
            "start_date": start_date,
            "end_date": end_date,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/cs/reviewReport/detail",
            req_body=req_body
        )

    # ==================== 店铺绩效 ====================

    async def get_performance_list(
        self,
        access_token: str,
        sid: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询店铺绩效列表

        API: POST /basicOpen/customerService/performance/list

        Args:
            access_token: 访问令牌
            sid: 店铺ID列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含店铺绩效列表

        Example:
            >>> result = await cs.get_performance_list(
            ...     access_token="xxx",
            ...     sid=[1, 2]
            ... )
        """
        logger.debug("Fetching performance list: sid=%s", sid)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sid:
            req_body["sid"] = sid

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/performance/list",
            req_body=req_body
        )

    async def get_performance_detail(
        self,
        access_token: str,
        sid: int,
        **kwargs
    ) -> ResponseResult:
        """
        查询店铺绩效详情

        API: POST /basicOpen/customerService/performance/detail

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含店铺绩效详情

        Example:
            >>> result = await cs.get_performance_detail(
            ...     access_token="xxx",
            ...     sid=1
            ... )
        """
        logger.debug("Fetching performance detail: sid=%s", sid)

        req_body = {
            "sid": sid,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/performance/detail",
            req_body=req_body
        )

    # ==================== 业绩通知 ====================

    async def get_performance_notice_list(
        self,
        access_token: str,
        sid: int,
        status: list[int] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        mail_tag_ids: list[str] | None = None,
        is_read: int = -1,
        offset: int = 0,
        length: int = 50,
        **kwargs
    ) -> ResponseResult:
        """
        查询业绩通知列表

        API: POST /basicOpen/customerService/performanceNotice/list

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            status: 处理状态列表（0=无, 1=待处理, 2=已处理, 3=无需处理）
            start_date: 开始时间，格式 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD
            search_field: 搜索字段（subject=邮件主题, content=邮件内容）
            search_value: 搜索值
            mail_tag_ids: 邮件标签ID列表
            is_read: 是否已读（-1=全部, 0=未读, 1=已读）
            offset: 偏移量，默认0
            length: 分页长度，默认50
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含业绩通知列表

        Example:
            >>> result = await cs.get_performance_notice_list(
            ...     access_token="xxx",
            ...     sid=121,
            ...     status=[0, 1],
            ...     start_date="2025-09-11",
            ...     end_date="2025-09-10",
            ...     search_field="subject",
            ...     search_value="123"
            ... )
        """
        logger.debug("Fetching performance notice list: sid=%s", sid)

        req_body = {
            "sid": sid,
            "isRead": is_read,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if status:
            req_body["status"] = status
        if start_date:
            req_body["startDate"] = start_date
        if end_date:
            req_body["endDate"] = end_date
        if search_field:
            req_body["searchField"] = search_field
        if search_value:
            req_body["searchValue"] = search_value
        if mail_tag_ids:
            req_body["mailTagIds"] = mail_tag_ids

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/performanceNotice/list",
            req_body=req_body
        )

    # ==================== 买家之声 ====================

    async def get_voice_of_customer_list(
        self,
        access_token: str,
        sid: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询买家之声列表

        API: POST /basicOpen/customerService/voiceOfCustomer/list

        Args:
            access_token: 访问令牌
            sid: 店铺ID列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含买家之声列表

        Example:
            >>> result = await cs.get_voice_of_customer_list(
            ...     access_token="xxx",
            ...     sid=[1, 2]
            ... )
        """
        logger.debug("Fetching voice of customer list: sid=%s", sid)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sid:
            req_body["sid"] = sid

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/voiceOfCustomer/list",
            req_body=req_body
        )

    # ==================== 邮件管理 ====================

    async def get_mail_list(
        self,
        access_token: str,
        flag: str,
        email: str,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询邮件列表

        API: POST /erp/sc/data/mail/lists

        Args:
            access_token: 访问令牌
            flag: 类型（sent=发件, receive=收件）
            email: 店铺绑定邮箱
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含邮件列表

        Example:
            >>> result = await cs.get_mail_list(
            ...     access_token="xxx",
            ...     flag="sent",
            ...     email="xxx@qq.com",
            ...     start_date="2024-10-30",
            ...     end_date="2024-10-30"
            ... )
        """
        logger.debug("Fetching mail list: flag=%s, email=%s", flag, email)

        req_body = {
            "flag": flag,
            "email": email,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mail/lists",
            req_body=req_body
        )

    async def get_mail_detail(
        self,
        access_token: str,
        webmail_uuid: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询邮件详情

        API: POST /erp/sc/data/mail/detail

        Args:
            access_token: 访问令牌
            webmail_uuid: 邮件唯一标识
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含邮件详情

        Example:
            >>> result = await cs.get_mail_detail(
            ...     access_token="xxx",
            ...     webmail_uuid="1615637469510164901"
            ... )
        """
        logger.debug("Fetching mail detail: uuid=%s", webmail_uuid)

        req_body = {
            "webmail_uuid": webmail_uuid,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mail/detail",
            req_body=req_body
        )

    # ==================== 售后管理 ====================

    async def get_after_sale_work_order_list(
        self,
        access_token: str,
        date_type: str,
        start_time: str,
        end_time: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询售后工单列表

        API: POST /pb/mp/returns/workOrder/list

        Args:
            access_token: 访问令牌
            date_type: 时间类型（create_time=创建时间, complete_time=完成时间）
            start_time: 开始时间，格式 YYYY-MM-DD HH:mm:ss
            end_time: 结束时间，格式 YYYY-MM-DD HH:mm:ss
            offset: 分页偏移量，默认0
            length: 分页长度，上限500
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含售后工单列表

        Example:
            >>> result = await cs.get_after_sale_work_order_list(
            ...     access_token="xxx",
            ...     date_type="create_time",
            ...     start_time="2023-06-15 00:00:00",
            ...     end_time="2023-06-16 23:59:59"
            ... )
        """
        logger.debug("Fetching after sale work order list: date_type=%s", date_type)

        req_body = {
            "date_type": date_type,
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "length": min(length, 500),  # 上限500
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/pb/mp/returns/workOrder/list",
            req_body=req_body
        )

    async def get_rma_list(
        self,
        access_token: str,
        sid: list[int],
        search_time_field: str,
        start_time: str,
        end_time: str,
        search_value: list[str] | None = None,
        search_field: str | None = None,
        sort_column: str | None = None,
        sort_type: str | None = None,
        page_num: int = 1,
        page_size: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询RMA管理列表

        API: POST /basicOpen/customerService/rmaManage/list

        Args:
            access_token: 访问令牌
            sid: 店铺ID列表
            search_time_field: 搜索时间类型（createTime=创建时间, operationTime=操作时间）
            start_time: 开始时间，格式 YYYY-MM-DD
            end_time: 结束时间，格式 YYYY-MM-DD
            search_value: 搜索值列表（msku和asin支持多个搜索）
            search_field: 搜索字段（msku, asin, sku）
            sort_column: 排序字段
            sort_type: 排序方式（desc/asc）
            page_num: 页码，默认1
            page_size: 每页数量，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含RMA管理列表

        Example:
            >>> result = await cs.get_rma_list(
            ...     access_token="xxx",
            ...     sid=[114, 115],
            ...     search_time_field="operationTime",
            ...     start_time="2024-04-10",
            ...     end_time="2024-04-10",
            ...     search_field="msku",
            ...     search_value=["PEE-618"]
            ... )
        """
        logger.debug("Fetching RMA list: sid=%s", sid)

        req_body = {
            "sid": sid,
            "searchTimeFiled": search_time_field,
            "startTime": start_time,
            "endTime": end_time,
            "pageNum": page_num,
            "pageSize": page_size,
            **kwargs
        }

        if search_value:
            req_body["searchValue"] = search_value
        if search_field:
            req_body["searchField"] = search_field
        if sort_column:
            req_body["sortColumn"] = sort_column
        if sort_type:
            req_body["sortType"] = sort_type

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/customerService/rmaManage/list",
            req_body=req_body
        )


__all__ = [
    'CustomerServiceEndpoints',
]

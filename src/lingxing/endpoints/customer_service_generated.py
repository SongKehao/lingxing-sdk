"""CustomerService API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class CustomerServiceEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_rma(
        self,
        access_token: str,
        sid: list[Any],
        searchTimeFiled: str,
        startTime: str,
        endTime: str,
        searchValue: list[Any],
        searchField: str,
        sortColumn: str,
        sortType: str,
        pageNum: Any,
        pageSize: Any
    ) -> dict[str, Any]:
        """
        查询RMA管理

        API: /basicOpen/customerService/rmaManage/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，支持多选，数组 (Required)
            searchTimeFiled: 搜索时间类型：1创建时间 2.操作时间 createTime operationTime (Required)
            startTime: 创建或完成时间（开始），精确到年月日，无默认 (Required)
            endTime: 创建或完成时间（开始），精确到年月日，无默认 (Required)
            searchValue: 搜索值，msku和asin支持多个搜索，数组 (Required)
            searchField: 搜索字段：msku，asin，sku (Required)
            sortColumn: 排序字段 (Required)
            sortType: 排序方式 (Required)
            pageNum: 页码 (Required)
            pageSize: 每页数量 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_rma(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "searchTimeFiled": searchTimeFiled,
            "startTime": startTime,
            "endTime": endTime,
            "searchValue": searchValue,
            "searchField": searchField,
            "sortColumn": sortColumn,
            "sortType": sortType,
            "pageNum": pageNum,
            "pageSize": pageSize
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/rmaManage/list",
            method="POST",
            req_body=params
        )



    async def get_statistics_reviewlist(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sid: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询评价统计-Review列表

        API: /erp/sc/v2/cs/reviewReport/lists
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始时间【时间间隔不超过1年】，格式：Y-m-d (Required)
            end_date: 结束时间【时间间隔不超过1年】，格式：Y-m-d (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statistics_reviewlist(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sid": sid,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/v2/cs/reviewReport/lists",
            method="GET",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        sid: Any,
        status: list[Any] | None = None,
        startDate: str | None = None,
        endDate: str | None = None,
        searchField: str | None = None,
        searchValue: str | None = None,
        mailTagIds: list[Any] | None = None,
        isRead: Any | None = None,
        offset: Any | None = None,
        length: Any | None = None
    ) -> dict[str, Any]:
        """
        查询业绩通知列表

        API: /basicOpen/customerService/performanceNotice/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id (Required)
            status: 处理状态：0（无），1（待处理），2（已处理），3（无需处理） (Optional)
            startDate: 开始时间 YYYY-MM-DD (Optional)
            endDate: 结束时间 YYYY-MM-DD (Optional)
            searchField: 搜索字段,subject 邮件主题,content 邮件内容 (Optional)
            searchValue: 搜索值 (Optional)
            mailTagIds: 邮件标签 id (Optional)
            isRead: 是否已读，-1 全部，0 未读，1 已读 (Optional)
            offset: 偏移量 (Optional)
            length: 分页长度 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "status": status,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue,
            "mailTagIds": mailTagIds,
            "isRead": isRead,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/performanceNotice/list",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        webmail_uuid: str
    ) -> dict[str, Any]:
        """
        查询邮件详情

        API: /erp/sc/data/mail/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            webmail_uuid: 邮件唯一标识 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "webmail_uuid": webmail_uuid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mail/detail",
            method="POST",
            req_body=params
        )



    async def get_review(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询评价管理-Review

        API: /erp/sc/v2/data/mws/reviews
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始评论时间，闭区间，格式：Y-m-d (Required)
            end_date: 结束评论时间，闭区间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_review(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/v2/data/mws/reviews",
            method="POST",
            req_body=params
        )



    async def get_statistics_feedbacklist(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询评价统计-Feedback列表

        API: /erp/sc/cs/feedbackReport/lists
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)
            start_date: 开始时间【时间间隔不超过1年】，格式：Y-m-d (Required)
            end_date: 结束时间【时间间隔不超过1年】，格式：Y-m-d (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statistics_feedbacklist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/cs/feedbackReport/lists",
            method="POST",
            req_body=params
        )



    async def get_review(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sort_field: str | None = None,
        sort_type: str | None = None,
        sids: str | None = None,
        mids: str | None = None,
        principal_uids: str | None = None,
        search_value: str | None = None,
        star: str | None = None,
        cs_principal_uids: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        cids: str | None = None,
        global_tag_ids: str | None = None,
        match_types: str | None = None
    ) -> dict[str, Any]:
        """
        查询评论管理 - Review(新)

        API: /basicOpen/openapi/service/v3/data/mws/reviews
        Method: POST

        Args:
            access_token: Access token for authentication
            sort_field: 排序类型 (Optional)
            sort_type: 排序 (Optional)
            sids: 店铺id，多个用逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            mids: 站点id，多个用逗号分隔 (Optional)
            principal_uids: lisitng负责人，多个用逗号分隔 (Optional)
            search_value: 搜索值 (Optional)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            star: 星级，多个用逗号分隔 (Optional)
            cs_principal_uids: 处理人，多个用逗号分隔 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            cids: 分类id，多个用逗号分隔 (Optional)
            global_tag_ids: 标签id，多个用逗号分隔 (Optional)
            match_types: 匹配类型，多个用逗号分隔，默认传空字符串 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_review(token, ...)
            >>> print(result)
        """
        params = {
            "sort_field": sort_field,
            "sort_type": sort_type,
            "sids": sids,
            "mids": mids,
            "principal_uids": principal_uids,
            "search_value": search_value,
            "start_date": start_date,
            "end_date": end_date,
            "star": star,
            "cs_principal_uids": cs_principal_uids,
            "offset": offset,
            "length": length,
            "cids": cids,
            "global_tag_ids": global_tag_ids,
            "match_types": match_types
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/service/v3/data/mws/reviews",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        email: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询邮件列表

        API: /erp/sc/data/mail/lists
        Method: POST

        Args:
            access_token: Access token for authentication
            email: 店铺绑定邮箱 (Required)
            start_date: 开始日期，格式：yyyy-mm-dd (Required)
            end_date: 开始日期，格式：yyyy-mm-dd (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "email": email,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mail/lists",
            method="POST",
            req_body=params
        )



    async def get_1_3feedbacklist(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询评价管理 1-3星Feedback列表

        API: /erp/sc/cs/feedback/listMws
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 评论开始日期，格式：Y-m-d (Required)
            end_date: 评论结束日期，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_1_3feedbacklist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/cs/feedback/listMws",
            method="POST",
            req_body=params
        )



    async def get_statistics_review(
        self,
        access_token: str,
        mid: int,
        asin: str,
        start_date: str,
        end_date: str
    ) -> dict[str, Any]:
        """
        查询评价统计-Review每日新增数

        API: /erp/sc/cs/reviewReport/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            mid: 国家id (Required)
            asin: asin (Required)
            start_date: 开始时间【时间间隔不超过1年】 (Required)
            end_date: 结束时间【时间间隔不超过1年】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statistics_review(token, ...)
            >>> print(result)
        """
        params = {
            "mid": mid,
            "asin": asin,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/cs/reviewReport/detail",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None,
        search_value: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询买家之声列表

        API: /basicOpen/customerService/voiceOfBuyer/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/voiceOfBuyer/list",
            method="POST",
            req_body=params
        )



    async def get_store(
        self,
        access_token: str,
        pullDate: str,
        sid: Any
    ) -> dict[str, Any]:
        """
        查询店铺绩效详情

        API: /basicOpen/customerService/storeTarget/detail
        Method: GET

        Args:
            access_token: Access token for authentication
            pullDate: 报表更新日期，必填，日期格式：yyyy-MM-dd (Required)
            sid: 店铺ID，必填 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_store(token, ...)
            >>> print(result)
        """
        params = {
            "pullDate": pullDate,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/storeTarget/detail",
            method="GET",
            req_body=params
        )



    async def get_4_5feedbacklist(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询评价管理 4-5星Feedback列表

        API: /erp/sc/cs/feedback/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 评论开始日期，格式：Y-m-d (Required)
            end_date: 评论结束日期，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_4_5feedbacklist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/cs/feedback/list",
            method="POST",
            req_body=params
        )



    async def get_storelist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        search_time: str | None = None,
        sids: str | None = None,
        order_with_defect_FBM订单缺陷率: Any | None = None
    ) -> dict[str, Any]:
        """
        查询店铺绩效列表

        API: /basicOpen/customerService/storeTarget/list
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            search_time: 搜索时间，格式：Y-m-d (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            order_with_defect_FBM订单缺陷率: 否 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_storelist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "search_time": search_time,
            "sids": sids,
            "order_with_defect_FBM订单缺陷率": order_with_defect_FBM订单缺陷率
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/storeTarget/list",
            method="GET",
            req_body=params
        )



    async def get_statistics_feedback(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str
    ) -> dict[str, Any]:
        """
        查询评价统计-Feedback每日新增数

        API: /erp/sc/cs/feedbackReport/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始时间【时间间隔不超过1年】 (Required)
            end_date: 结束时间【时间间隔不超过1年】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statistics_feedback(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/cs/feedbackReport/detail",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sort_field: str | None = None,
        sort_type: str | None = None,
        date_field: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        currency_type: Any | None = None,
        search_field: str | None = None,
        offset: Any | None = None,
        length: Any | None = None,
        search_value: str | None = None,
        sids: str | None = None
    ) -> dict[str, Any]:
        """
        查询客户列表（新）

        API: /basicOpen/customerService/crm/customer/index
        Method: POST

        Args:
            access_token: Access token for authentication
            sort_field: 结果按字段排序 (Optional)
            sort_type: desc=倒序，asc=升序 (Optional)
            date_field: 时间筛选查询类型，1：首次购买时间 ，2：最近购买时间 (Optional)
            start_date: 筛选开始时间 (Optional)
            end_date: 筛选结束时间 (Optional)
            currency_type: 币种，0=原币种，1=CNY，2=USD (Optional)
            search_field: 支持搜索的字段 buyer_email、buyer_name (Optional)
            offset: 偏移量 (Optional)
            length: 分页长度 ，默认20 ，上限200 (Optional)
            search_value: 搜索值 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sort_field": sort_field,
            "sort_type": sort_type,
            "date_field": date_field,
            "start_date": start_date,
            "end_date": end_date,
            "currency_type": currency_type,
            "search_field": search_field,
            "offset": offset,
            "length": length,
            "search_value": search_value,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/customerService/crm/customer/index",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_time: str,
        end_time: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询售后工单列表

        API: /pb/mp/returns/workOrder/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_time: 开始时间，闭区间，格式：Y-m-d H:i:s (Required)
            end_time: 结束时间，闭区间，格式：Y-m-d H:i:s (Required)
            offset: 分页偏移量 (Required)
            length: 分页长度，上限500 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/returns/workOrder/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询客户列表（旧）

        API: /bd/crm/open/api/customer/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            start_date: 开始时间 (Required)
            end_date: 结束时间 (Required)
            offset: 页码，默认1 (Optional)
            length: 每页条数，默认100 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/crm/open/api/customer/list",
            method="POST",
            req_body=params
        )


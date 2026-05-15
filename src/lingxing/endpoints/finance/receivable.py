#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""应收账款API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class ReceivableEndpoint(BaseEndpoint):
    """应收账款API"""
    async def get_other_fee_request_pool(
        self,
        access_token: str,
        start_time: str,
        end_time: str,
        search_field_time: str = "create_time",
        status: int | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        purchaser_ids: list[int] | None = None,
        supplier_ids: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-其他费用

        API: POST /basicOpen/finance/requestFundsPool/otherFee/list

        Args:
            access_token: 访问令牌
            start_time: 开始时间，格式 YYYY-MM-DD（必填）
            end_time: 结束时间，格式 YYYY-MM-DD（必填）
            search_field_time: 时间维度（create_time=创建时间，close_time=付清时间）
            status: 付款状态（0=查询未付清，1=查询已付清，不传默认查询全部）
            search_field: 搜索字段（order_sn=采购单号，create_username=采购员）
            search_value: 搜索值（支持模糊查询）
            purchaser_ids: 采购方ID列表
            supplier_ids: 应付对象ID列表
            offset: 偏移量，默认0
            length: 返回条数，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: {list: [...], total: int}}

        Example:
            >>> result = await finance.get_other_fee_request_pool(
            ...     access_token="xxx",
            ...     start_time="2024-01-01",
            ...     end_time="2024-12-31",
            ...     status=0
            ... )
        """
        logger.debug("Fetching other fee request pool: start=%s, end=%s", start_time, end_time)

        req_body = {
            "startTime": start_time,
            "endTime": end_time,
            "searchFieldTime": search_field_time,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if status is not None:
            req_body["status"] = status
        if search_field and search_value:
            req_body["searchField"] = search_field
            req_body["searchValue"] = search_value
        if purchaser_ids:
            req_body["purchaserIds"] = purchaser_ids
        if supplier_ids:
            req_body["supplierIds"] = supplier_ids

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/otherFee/list",
            req_body=req_body
        )

    # ==================== 应收报告 ====================

    async def get_receivable_report_list(
        self,
        access_token: str,
        settle_month: str,
        sids: list[int] | None = None,
        mids: list[int] | None = None,
        currency_code: str | None = None,
        archive_status: int | None = None,
        sort_field: str | None = None,
        sort_type: str | None = None,
        received_state: int | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        应收报告列表查询

        API: POST /bd/sp/api/open/monthly/receivable/report/list

        Args:
            access_token: 访问令牌
            settle_month: 结算月，格式 YYYY-MM
            sids: 店铺ID列表（可选）
            mids: 国家ID列表（可选）
            currency_code: 币种代码（可选）
            archive_status: 对账状态（1=已对账，0=未对账）
            sort_field: 排序字段（beginningBalanceCurrencyAmount/incomeAmount/refundAmount/
                        spendAmount/other/endingBalance）
            sort_type: 排序规则（asc=升序，desc=降序）
            received_state: 转账/到账金额（0=不相符，1=相符）
            offset: 偏移量，默认0
            length: 返回条数，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_receivable_report_list(
            ...     access_token="xxx",
            ...     settle_month="2023-01",
            ...     sids=[109, 123]
            ... )
        """
        logger.debug("Fetching receivable report list: settle_month=%s", settle_month)

        req_body = {
            "settleMonth": settle_month,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if mids:
            req_body["mids"] = mids
        if currency_code:
            req_body["currencyCode"] = currency_code
        if archive_status is not None:
            req_body["archiveStatus"] = archive_status
        if sort_field:
            req_body["sortField"] = sort_field
        if sort_type:
            req_body["sortType"] = sort_type
        if received_state is not None:
            req_body["receivedState"] = received_state

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/sp/api/open/monthly/receivable/report/list",
            req_body=req_body
        )

    async def get_receivable_report_basic_info(
        self,
        access_token: str,
        sid: int,
        settle_month: str,
        currency_code: str = "CNY",
        **kwargs
    ) -> ResponseResult:
        """
        应收报告详情-基础信息

        API: POST /bd/sp/api/open/monthly/receivable/report/list/detail/info

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            settle_month: 结算月，格式 YYYY-MM
            currency_code: 币种代码，默认 CNY
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含店铺应收报告基础信息

        Example:
            >>> result = await finance.get_receivable_report_basic_info(
            ...     access_token="xxx",
            ...     sid=1,
            ...     settle_month="2023-01",
            ...     currency_code="CNY"
            ... )
        """
        logger.debug("Fetching receivable report basic info: sid=%s, month=%s", sid, settle_month)

        req_body = {
            "sid": sid,
            "settleMonth": settle_month,
            "currencyCode": currency_code,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/sp/api/open/monthly/receivable/report/list/detail/info",
            req_body=req_body
        )

    async def get_receivable_report_detail_list(
        self,
        access_token: str,
        sid: int,
        settle_month: str,
        currency_code: str = "CNY",
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 200,
        **kwargs
    ) -> ResponseResult:
        """
        应收报告详情-列表

        API: POST /bd/sp/api/open/monthly/receivable/report/list/detail

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            settle_month: 结算月，格式 YYYY-MM
            currency_code: 币种代码，默认 CNY
            search_field: 搜索值类型（fid/settlementId/sellerSku/localSku/localName/abstractName）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_receivable_report_detail_list(
            ...     access_token="xxx",
            ...     sid=1,
            ...     settle_month="2023-01",
            ...     currency_code="CNY"
            ... )
        """
        logger.debug("Fetching receivable report detail list: sid=%s, month=%s", sid, settle_month)

        req_body = {
            "sid": sid,
            "settleMonth": settle_month,
            "currencyCode": currency_code,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if search_field and search_value:
            req_body["searchField"] = search_field
            req_body["searchValue"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/sp/api/open/monthly/receivable/report/list/detail",
            req_body=req_body
        )

    # ==================== 利润重算 ====================

    async def recompute_profit_report(
        self,
        access_token: str,
        date_month: str,
    ) -> ResponseResult:
        """
        立即重算利润报表数据

        API: POST /bd/profit/report/open/report/settle/compute/manual

        用于触发指定月份的利润数据重新计算。
        注意：此操作会重新计算整月的利润数据，可能需要一定时间。

        Args:
            access_token: 访问令牌
            date_month: 重算月份，格式 yyyy-MM（如 2023-01）

        Returns:
            ResponseResult: 包含 {code, message, data: []}

        Example:
            >>> result = await finance.recompute_profit_report(
            ...     access_token="xxx",
            ...     date_month="2024-01"
            ... )
            >>> if result.code == 0:
            ...     print("利润重算任务已触发")
        """
        logger.debug("Triggering profit report recomputation: month=%s", date_month)

        req_body = {
            "date_month": date_month,
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/settle/compute/manual",
            req_body=req_body
        )


__all__ = [
    'ReceivableEndpoint',
]

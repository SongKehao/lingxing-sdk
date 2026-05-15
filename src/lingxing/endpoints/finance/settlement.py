#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""结算报表API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class SettlementEndpoint(BaseEndpoint):
    """结算报表API"""
    async def get_settlement_summary(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        date_type: int = 1,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        结算汇总列表

        API: POST /bd/sp/api/open/settlement/summary/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            date_type: 日期类型，1=结算结束时间（默认）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_settlement_summary(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24",
            ...     date_type=1
            ... )
        """
        logger.debug("Fetching settlement summary: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "dateType": date_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request(
            access_token=access_token,
            route_name="/bd/sp/api/open/settlement/summary/list",
            req_body=req_body
        )

    async def get_settlement_transactions(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        date_type: int = 1,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        结算交易明细列表

        API: POST /bd/sp/api/open/settlement/transaction/detail/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            date_type: 日期类型，1=结算结束时间（默认）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_settlement_transactions(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24",
            ...     date_type=1
            ... )
        """
        logger.debug("Fetching settlement transactions: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "dateType": date_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request(
            access_token=access_token,
            route_name="/bd/sp/api/open/settlement/transaction/detail/list",
            req_body=req_body
        )

    # ==================== 费用相关API ====================

    async def get_fba_long_term_storage_fee(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        FBA长期仓储费查询

        API: POST /erp/sc/data/fba_report/storageFeeLongTerm
        验证状态: ✅ 已验证 (2026-02-24)

        注意: 此API使用单个sid而非sids数组，且使用snake_case日期参数

        Args:
            access_token: 访问令牌
            sid: 店铺ID（单个）
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            offset: 偏移量，默认0
            length: 返回条数，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
        """
        logger.debug("Fetching FBA long-term storage fee: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "start_date": start_date,  # snake_case
            "end_date": end_date,      # snake_case
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/storageFeeLongTerm",
            req_body=req_body
        )

    async def get_reimbursement_report(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        search_field: str | None = None,
        search_value: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        亚马逊赔偿报告查询

        API: POST /basicOpen/openapi/mwsReport/reimbursementList
        验证状态: ✅ 已验证 (2026-02-24)

        注意: 此API使用逗号分隔的sids字符串，且使用snake_case日期参数

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD（最长90天范围）
            end_date: 结束日期，格式 YYYY-MM-DD
            offset: 偏移量，默认0
            length: 返回条数，默认100（最大200）
            search_field: 搜索字段（reimbursement_id/amazon_order_id/asin/msku/fnsku/item_name）
            search_value: 搜索值
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_reimbursement_report(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching reimbursement report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": ",".join(str(s) for s in sids),  # 逗号分隔的字符串
            "start_date": start_date,  # snake_case
            "end_date": end_date,      # snake_case
            "offset": offset,
            "length": min(length, 200),  # 最大200
            **kwargs
        }

        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request(
            access_token=access_token,
            route_name="/basicOpen/openapi/mwsReport/reimbursementList",
            req_body=req_body
        )

    # ==================== 父ASIN利润报表 ====================


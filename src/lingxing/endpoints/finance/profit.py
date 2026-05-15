#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""利润报表API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class ProfitEndpoint(BaseEndpoint):
    """利润报表API"""
    async def get_profit_report_msku(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        MSKU利润报表

        API: POST /bd/profit/report/open/report/msku/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_msku(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
            >>> data = result.data  # {"total": 100, "records": [...]}
        """
        logger.debug("Fetching MSKU profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        # 构建请求体 - 注意使用数组格式的sids
        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/msku/list",
            req_body=req_body
        )

    async def get_profit_report_asin(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        ASIN利润报表

        API: POST /bd/profit/report/open/report/asin/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_asin(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching ASIN profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/asin/list",
            req_body=req_body
        )

    async def get_profit_report_sku(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        SKU利润报表

        API: POST /bd/profit/report/open/report/sku/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_sku(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching SKU profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/sku/list",
            req_body=req_body
        )

    async def get_profit_report_seller(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        店铺利润报表

        API: POST /bd/profit/report/open/report/seller/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_seller(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching seller profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/seller/list",
            req_body=req_body
        )

    async def get_profit_seller_monthly(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        currency_code: str = "CNY",
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        店铺月度汇总

        API: POST /bd/profit/report/open/report/seller/summary/list

        注意: currencyCode 是必填参数

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            currency_code: 币种代码，默认 CNY
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_seller_monthly(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-01-01",
            ...     end_date="2026-01-31",
            ...     currency_code="CNY"
            ... )
        """
        logger.debug("Fetching seller monthly summary: sids=%s, start=%s, end=%s, currency=%s", sids, start_date, end_date, currency_code)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "currencyCode": currency_code,  # 必填参数
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/seller/summary/list",
            req_body=req_body
        )

    async def get_order_transactions(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        订单交易明细

        API: POST /basicOpen/finance/profitReport/order/transcation/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_order_transactions(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching order transactions: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/profitReport/order/transcation/list",
            req_body=req_body
        )

    async def get_profit_stats_msku(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        MSKU利润统计

        API: POST /bd/profit/statistics/open/msku/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_stats_msku(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching MSKU profit statistics: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/statistics/open/msku/list",
            req_body=req_body
        )

    async def get_profit_stats_asin(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        ASIN利润统计

        API: POST /bd/profit/statistics/open/asin/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD（不能超过31天范围）
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_stats_asin(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching ASIN profit statistics: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/statistics/open/asin/list",
            req_body=req_body
        )

    # ==================== 结算相关API ====================


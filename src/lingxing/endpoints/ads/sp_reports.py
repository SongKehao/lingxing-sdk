#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""SP广告报表API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class SPReportsEndpoint(BaseEndpoint):
    """SP广告报表API"""
    async def get_sp_campaign_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告活动报表

        API: POST /pb/openapi/newad/spCampaignReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告活动报表列表

        Example:
            reports = await ads.get_sp_campaign_reports(
                access_token="xxx",
                sid=4661,
                report_date="2026-02-22"
            )
        """
        logger.debug("Fetching SP campaign reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spCampaignReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_adgroup_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告组报表

        API: POST /pb/openapi/newad/spAdGroupReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告组报表列表
        """
        logger.debug("Fetching SP ad group reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdGroupReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_product_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告商品报表

        API: POST /pb/openapi/newad/spProductAdReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告商品报表列表
        """
        logger.debug("Fetching SP product reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spProductAdReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_keyword_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP关键词报表

        API: POST /pb/openapi/newad/spKeywordReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 关键词报表列表
        """
        logger.debug("Fetching SP keyword reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spKeywordReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_search_term_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        target_type: str = "keyword",
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP搜索词报表（买家搜索词报告）

        API: POST /pb/openapi/newad/queryWordReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            target_type: 投放类型：keyword（关键词）、target（商品投放），默认keyword
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 搜索词报表列表
        """
        logger.debug("Fetching SP search term reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "target_type": target_type,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/queryWordReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_target_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP商品定位报表

        API: POST /pb/openapi/newad/spTargetReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 商品定位报表列表
        """
        logger.debug("Fetching SP target reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spTargetReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_asin_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        show_detail: int = 0,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP已购买商品报表（Other Asin Report）

        API: POST /pb/openapi/newad/asinReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 已购买商品报表列表
        """
        logger.debug("Fetching SP ASIN reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "show_detail": show_detail,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/asinReports",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== SB广告基础数据 ====================


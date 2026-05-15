#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""SB广告API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class SBAdsEndpoint(BaseEndpoint):
    """SB广告API"""
    async def get_sb_campaigns(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告活动列表

        API: POST /pb/openapi/newad/hsaCampaigns

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告活动列表
        """
        logger.debug("Fetching SB campaigns: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaCampaigns",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_adgroups(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告组列表

        API: POST /pb/openapi/newad/hsaAdGroups

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告组列表
        """
        logger.debug("Fetching SB ad groups: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaAdGroups",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_creatives(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告创意列表

        API: POST /pb/openapi/newad/hsaProductAds

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告创意列表
        """
        logger.debug("Fetching SB creatives: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaProductAds",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_targeting(
        self,
        access_token: str,
        sid: int,
        ads_type: str = "ALL",
        targeting_type: str = "ALL",
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告投放列表（关键词/商品定位）

        API: POST /pb/openapi/newad/sbTargeting

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            ads_type: 广告类型：SB、SBV、ALL（同时返回SB和SBV）
            targeting_type: 投放类型：keyword（关键词）、producttarget（商品定位）、ALL
            offset: 偏移量，默认0
            length: 返回数量，默认1000
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告投放列表
        """
        logger.debug("Fetching SB targeting: sid=%s, ads_type=%s, targeting_type=%s", sid, ads_type, targeting_type)

        req_body = {
            "sid": sid,
            "ads_type": ads_type,
            "targeting_type": targeting_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbTargeting",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_negative_keywords(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告否定关键词列表

        API: POST /pb/openapi/newad/hsaNegativeKeywords

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB否定关键词列表
        """
        logger.debug("Fetching SB negative keywords: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaNegativeKeywords",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_negative_targets(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告否定商品投放列表

        API: POST /pb/openapi/newad/hsaNegativeTargets

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB否定商品投放列表
        """
        logger.debug("Fetching SB negative targets: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaNegativeTargets",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== SB广告报表 ====================

    async def get_sb_campaign_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告活动报表

        API: POST /pb/openapi/newad/hsaCampaignReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告活动报表列表
        """
        logger.debug("Fetching SB campaign reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaCampaignReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_adgroup_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告组报表

        API: POST /pb/openapi/newad/hsaAdGroupReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告组报表列表
        """
        logger.debug("Fetching SB ad group reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaAdGroupReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_creative_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告创意报表

        API: POST /pb/openapi/newad/listHsaProductAdReport

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB广告创意报表列表
        """
        logger.debug("Fetching SB creative reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/listHsaProductAdReport",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_search_term_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        target_type: str = "keyword",
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告用户搜索词报表

        API: POST /pb/openapi/newad/hsaQueryWordReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            target_type: 投放类型：keyword（关键词）、target（商品投放），默认keyword
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB用户搜索词报表列表
        """
        logger.debug("Fetching SB search term reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "target_type": target_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaQueryWordReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sb_targeting_reports(
        self,
        access_token: str,
        sid: int,
        report_date: str,
        sponsored_type: str = "ALL",
        target_type: str = "keyword",
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SB品牌广告投放报表

        API: POST /pb/openapi/newad/listHsaTargetingReport

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            sponsored_type: 广告类型：ALL、SB、SBV
            target_type: 投放类型：keyword（关键词）、producttarget（商品投放）、ALL
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SB投放报表列表
        """
        logger.debug("Fetching SB targeting reports: sid=%s, report_date=%s", sid, report_date)

        req_body = {
            "sid": sid,
            "report_date": report_date,
            "sponsored_type": sponsored_type,
            "target_type": target_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/listHsaTargetingReport",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== SD广告基础数据 ====================


#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""SD广告API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class SDAdsEndpoint(BaseEndpoint):
    """SD广告API"""
    async def get_sd_campaigns(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SD展示广告活动列表

        API: POST /pb/openapi/newad/sdCampaigns

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告活动列表
        """
        logger.debug("Fetching SD campaigns: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdCampaigns",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_adgroups(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SD展示广告组列表

        API: POST /pb/openapi/newad/sdAdGroups

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告组列表
        """
        logger.debug("Fetching SD ad groups: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAdGroups",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_product_ads(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SD展示广告商品列表

        API: POST /pb/openapi/newad/sdProductAds

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告商品列表
        """
        logger.debug("Fetching SD product ads: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdProductAds",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_targets(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SD展示广告商品定位列表

        API: POST /pb/openapi/newad/sdTargets

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD商品定位列表
        """
        logger.debug("Fetching SD targets: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdTargets",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_negative_targets(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SD展示广告否定商品定位列表

        API: POST /pb/openapi/newad/sdNegativeTargets

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD否定商品定位列表
        """
        logger.debug("Fetching SD negative targets: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdNegativeTargets",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== SD广告报表 ====================

    async def get_sd_campaign_reports(
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
        SD展示广告活动报表

        API: POST /pb/openapi/newad/sdCampaignReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告活动报表列表
        """
        logger.debug("Fetching SD campaign reports: sid=%s, report_date=%s", sid, report_date)

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
            route_name="/pb/openapi/newad/sdCampaignReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_adgroup_reports(
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
        SD展示广告组报表

        API: POST /pb/openapi/newad/sdAdGroupReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告组报表列表
        """
        logger.debug("Fetching SD ad group reports: sid=%s, report_date=%s", sid, report_date)

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
            route_name="/pb/openapi/newad/sdAdGroupReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_product_reports(
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
        SD展示广告商品报表

        API: POST /pb/openapi/newad/sdProductAdReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD广告商品报表列表
        """
        logger.debug("Fetching SD product reports: sid=%s, report_date=%s", sid, report_date)

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
            route_name="/pb/openapi/newad/sdProductAdReports",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sd_target_reports(
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
        SD展示广告投放报表

        API: POST /pb/openapi/newad/sdTargetReports

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            report_date: 报表日期，格式: "2026-02-22"（单日期，非日期范围）
            show_detail: 是否展示完整归因期信息，默认0（否），1（是）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: SD投放报表列表
        """
        logger.debug("Fetching SD target reports: sid=%s, report_date=%s", sid, report_date)

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
            route_name="/pb/openapi/newad/sdTargetReports",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== 广告组合 ====================


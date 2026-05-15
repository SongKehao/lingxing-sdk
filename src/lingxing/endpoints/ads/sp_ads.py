#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""SP广告基础数据API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class SPAdsEndpoint(BaseEndpoint):
    """SP广告基础数据API"""
    async def get_sp_campaigns(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告活动列表

        API: POST /pb/openapi/newad/spCampaigns

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告活动列表

        Example:
            campaigns = await ads.get_sp_campaigns(
                access_token="xxx",
                sid=4661,
                offset=0,
                length=100
            )
        """
        logger.debug("Fetching SP campaigns: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spCampaigns",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_adgroups(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告组列表

        API: POST /pb/openapi/newad/spAdGroups

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告组列表
        """
        logger.debug("Fetching SP ad groups: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdGroups",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_product_ads(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP广告商品列表

        API: POST /pb/openapi/newad/spProductAds

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 广告商品列表
        """
        logger.debug("Fetching SP product ads: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spProductAds",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_keywords(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP关键词列表

        API: POST /pb/openapi/newad/spKeywords

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 关键词列表
        """
        logger.debug("Fetching SP keywords: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spKeywords",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_targets(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP投放列表（商品投放/品类投放）

        API: POST /pb/openapi/newad/spTargets

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数

        Returns:
            List[Dict]: 投放列表
        """
        logger.debug("Fetching SP targets: sid=%s, offset=%s, length=%s", sid, offset, length)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spTargets",
            req_body=req_body
        )

        return self._parse_response(response)

    async def get_sp_negative_targets(
        self,
        access_token: str,
        sid: int,
        target_type: str = "target",
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        SP否定投放列表（否定关键词/否定商品/否定品牌）

        API: POST /pb/openapi/newad/spNegativeTargetsOrKeywords

        Args:
            access_token: 访问令牌
            sid: 店铺ID，如 4661
            target_type: 投放类型：keyword（否定关键词）、target（否定商品/品牌）
            offset: 偏移量，默认0
            length: 返回数量，默认100
            **kwargs: 其他查询参数（如 campaign_id）

        Returns:
            List[Dict]: 否定投放列表
        """
        logger.debug("Fetching SP negative targets: sid=%s, target_type=%s", sid, target_type)

        req_body = {
            "sid": sid,
            "target_type": target_type,
            "offset": offset,
            "length": length,
            **kwargs
        }

        response = await self._request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spNegativeTargetsOrKeywords",
            req_body=req_body
        )

        return self._parse_response(response)

    # ==================== SP广告报表 (使用 report_date) ====================


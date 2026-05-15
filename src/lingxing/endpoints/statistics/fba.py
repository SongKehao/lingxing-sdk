#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""FBA统计API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class FBAEndpoint(BaseEndpoint):
    """FBA统计API"""
    async def get_operate_log(
        self,
        access_token: str,
        sids: list[str],
        search_field: str,
        search_value: str,
        date_type: str,
        start_date: str,
        end_date: str,
    ) -> dict[str, Any]:
        """
        查询运营日志

        API: POST /basicOpen/operateManage/operateLog/list
        对应系统：【统计】>【运营日志】

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表 (格式: ["109,136"])
            search_field: 搜索类型 (asin/parent_asin/msku)
            search_value: 搜索值
            date_type: 时间类型 (1=日, 2=周, 3=月)
            start_date: 开始日期 (Y-m-d)
            end_date: 结束日期 (Y-m-d)

        Returns:
            Dict包含:
            - records: 运营日志数据列表
            - total: 总数
        """
        logger.debug("Fetching operate log: %s ~ %s", start_date, end_date)

        req_body = {
            "sids": sids,
            "search_field": search_field,
            "search_value": search_value,
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
        }

        response = await self._request(
            access_token=access_token,
            route_name="/basicOpen/operateManage/operateLog/list",
            req_body=req_body,
        )

        return self._parse_response(response)

    # ==================== 库存报表 ====================

    async def get_fba_stock_report(
        self,
        access_token: str,
        start_month: str,
        end_month: str,
        seller_id: str | None = None,
        dimension: int = 1,
        attribute: int = 2,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询FBA库存报表（新版-汇总/明细）

        API: POST /erp/sc/routing/fba/fbaStockReport/getList
        对应系统：【统计】>【库存报表】>【FBA】>【新版】

        Args:
            access_token: 访问令牌
            start_month: 开始月份 (Y-m)
            end_month: 截至月份 (Y-m)
            seller_id: 亚马逊店铺ID (seller_id)
            dimension: 数据维度 (1=汇总, 2=明细)
            attribute: 可售状态 (0=不可售, 1=可售, 2=全部)，仅明细维度生效
            offset: 分页偏移量，仅明细维度生效
            length: 分页长度，仅明细维度生效，上限5000

        Returns:
            Dict包含:
            - records: FBA库存报表数据列表
            - total: 总数
        """
        logger.debug("Fetching FBA stock report: %s ~ %s", start_month, end_month)

        req_body = {
            "start_month": start_month,
            "end_month": end_month,
            "dimention": dimension,  # 注意：API参数名是 dimention（拼写错误）
            "offset": offset,
            "length": length,
            "attribute": attribute,
        }

        if seller_id:
            req_body["seller_id"] = seller_id

        response = await self._request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/fbaStockReport/getList",
            req_body=req_body,
        )

        return self._parse_response(response)

    async def get_fba_cost_center_gather(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        seller_id: list[str],
        offset: int = 0,
        length: int = 15,
    ) -> dict[str, Any]:
        """
        查询FBA库存报表-成本中心汇总

        API: POST /cost/center/openApi/fba/gather/query
        对应系统：【统计】>【库存报表】>【FBA】>【历史报表】>【汇总】

        Args:
            access_token: 访问令牌
            start_date: 统计起始月份 (Y-m)
            end_date: 统计结束月份 (Y-m)
            seller_id: 亚马逊店铺ID列表 (seller_id)
            offset: 分页偏移量
            length: 分页长度，默认15

        Returns:
            Dict包含:
            - records: FBA成本中心汇总数据列表
            - total: 总数
        """
        logger.debug("Fetching FBA cost center gather: %s ~ %s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "seller_id": seller_id,
            "offset": offset,
            "length": length,
        }

        response = await self._request(
            access_token=access_token,
            route_name="/cost/center/openApi/fba/gather/query",
            req_body=req_body,
        )

        return self._parse_response(response)

    async def get_fba_cost_center_detail(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        seller_id: list[str],
        offset: int = 0,
        length: int = 15,
    ) -> dict[str, Any]:
        """
        查询FBA库存报表-成本中心明细

        API: POST /cost/center/openApi/fba/detail/query
        对应系统：【统计】>【库存报表】>【FBA】>【历史报表】>【明细】

        Args:
            access_token: 访问令牌
            start_date: 统计起始月份 (Y-m)
            end_date: 统计结束月份 (Y-m)
            seller_id: 亚马逊店铺ID列表 (seller_id)
            offset: 分页偏移量
            length: 分页长度，默认15，最大2100

        Returns:
            Dict包含:
            - records: FBA成本中心明细数据列表
            - total: 总数
        """
        logger.debug("Fetching FBA cost center detail: %s ~ %s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "seller_id": seller_id,
            "offset": offset,
            "length": length,
        }

        response = await self._request(
            access_token=access_token,
            route_name="/cost/center/openApi/fba/detail/query",
            req_body=req_body,
        )

        return self._parse_response(response)


__all__ = ['FBAEndpoint']

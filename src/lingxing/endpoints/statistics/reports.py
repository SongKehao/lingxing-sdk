#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""报表统计API"""

import logging  # noqa: E402
from typing import Any  # noqa: E402

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class ReportsEndpoint(BaseEndpoint):
    """报表统计API"""
    async def get_order_profit(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sids: list[int] | None = None,
        search_field: str | None = None,
        search_value: list[str] | None = None,
        currency_code: str | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询订单利润-MSKU维度

        API: POST /basicOpen/finance/mreport/OrderProfit
        对应系统：【财务】>【订单利润】
        唯一键: sid + msku

        Args:
            access_token: 访问令牌
            start_date: 开始日期 (Y-m-d 或 Y-m-d H:i:s)
            end_date: 结束日期 (Y-m-d 或 Y-m-d H:i:s)
            sids: 店铺ID列表
            search_field: 搜索字段类型 (seller_sku/asin/local_name/local_sku)
            search_value: 搜索值列表
            currency_code: 币种代码 (原币种/CNY/USD/EUR/JPY等)
            offset: 分页偏移量
            length: 分页长度，默认20，上限5000

        Returns:
            Dict包含:
            - records: 订单利润数据列表
            - total: 总数
        """
        logger.debug("Fetching order profit: %s ~ %s", start_date, end_date)

        req_body = {
            "startDate": start_date,
            "endDate": end_date,
            "offset": offset,
            "length": length,
        }

        if sids:
            req_body["sids"] = sids
        if search_field:
            req_body["searchField"] = search_field
        if search_value:
            req_body["searchValue"] = search_value
        if currency_code:
            req_body["currencyCode"] = currency_code

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.ORDER_PROFIT,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch order profit: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("data", data.get("records", [])),
                "total": data.get("total", 0),
            }
        return {"records": [], "total": 0}

    # ==================== FBA仓储费 ====================

    async def get_fba_storage_fee_month(
        self,
        access_token: str,
        sid: int,
        month: str,
        offset: int = 0,
        length: int = 1000,
    ) -> dict[str, Any]:
        """
        查询FBA月仓储费

        API: POST /erp/sc/data/fba_report/storageFeeMonth
        对应系统：【统计】>【FBA月仓储费】

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            month: 收费月份 (Y-m)
            offset: 分页偏移量
            length: 分页长度，默认1000

        Returns:
            Dict包含:
            - records: 月仓储费数据列表
            - total: 总数
        """
        logger.debug("Fetching FBA storage fee month: sid=%s, month=%s", sid, month)

        req_body = {
            "sid": sid,
            "month": month,
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.FBA_STORAGE_FEE_MONTH,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch FBA storage fee month: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("data", []),
                "total": data.get("total", 0),
            }
        return {"records": [], "total": 0}

    async def get_fba_storage_fee_long_term(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 1000,
    ) -> dict[str, Any]:
        """
        查询FBA长期仓储费

        API: POST /erp/sc/data/fba_report/storageFeeLongTerm
        对应系统：【统计】>【FBA长期仓储费】

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 收费日期开始 (Y-m-d)
            end_date: 收费日期结束 (Y-m-d)
            offset: 分页偏移量
            length: 分页长度，默认1000

        Returns:
            Dict包含:
            - records: 长期仓储费数据列表
            - total: 总数
        """
        logger.debug("Fetching FBA storage fee long term: sid=%s", sid)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.FBA_STORAGE_FEE_LONG_TERM,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch FBA storage fee long term: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        if isinstance(data, dict):
            return {
                "records": data.get("data", []),
                "total": data.get("total", 0),
            }
        return {"records": [], "total": 0}

    # ==================== 采购报表 ====================

    async def get_purchase_report_buyer(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        time_type: int = 1,
        product_type: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询采购报表-采购员维度

        API: POST /basicOpen/report/purchase/buyer/list
        对应系统：【采购】>【采购报表】>【采购员】

        Args:
            access_token: 访问令牌
            start_date: 开始日期 (Y-m-d)，时间间隔最长90天
            end_date: 结束日期 (Y-m-d)
            time_type: 时间类型 (1=下单时间, 2=到货时间)
            product_type: 产品类型列表 (1=普通产品, 2=组合产品, 3=辅料)
            offset: 分页偏移量
            length: 分页长度，默认20，上限200

        Returns:
            Dict包含:
            - records: 采购员报表数据列表
            - total: 总数
        """
        logger.debug("Fetching purchase report buyer: %s ~ %s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "time_type": time_type,
            "offset": offset,
            "length": length,
        }

        if product_type:
            req_body["product_type"] = product_type

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_REPORT_BUYER,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase report buyer: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        return {"records": [], "total": 0}

    async def get_purchase_report_product(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        time_type: int = 1,
        sids: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询采购报表-产品维度

        API: POST /basicOpen/report/purchase/product/list
        对应系统：【采购】>【采购报表】>【产品】

        Args:
            access_token: 访问令牌
            start_date: 开始日期 (Y-m-d)，时间间隔最长90天
            end_date: 结束日期 (Y-m-d)
            time_type: 时间类型 (1=下单时间, 2=到货时间)
            sids: 店铺ID，多个使用英文逗号分隔
            search_field: 搜索字段 (product_name/sku/msku/fnsku/spu_name/spu)
            search_value: 搜索值
            offset: 分页偏移量
            length: 分页长度，默认20，上限200

        Returns:
            Dict包含:
            - records: 产品报表数据列表
            - total: 总数
        """
        logger.debug("Fetching purchase report product: %s ~ %s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "time_type": time_type,
            "offset": offset,
            "length": length,
        }

        if sids:
            req_body["sids"] = sids
        if search_field:
            req_body["search_field"] = search_field
        if search_value:
            req_body["search_value"] = search_value

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_REPORT_PRODUCT,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase report product: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        return {"records": [], "total": 0}

    async def get_purchase_report_supplier(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        time_type: int = 1,
        search_field: str | None = None,
        search_value: str | None = None,
        product_type: list[int] | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """
        查询采购报表-供应商维度

        API: POST /basicOpen/report/purchase/supplier/list
        对应系统：【采购】>【采购报表】>【供应商】

        Args:
            access_token: 访问令牌
            start_date: 开始日期 (Y-m-d)，时间间隔最长90天
            end_date: 结束日期 (Y-m-d)
            time_type: 时间类型 (1=下单时间, 2=到货时间)
            search_field: 搜索字段 (order_no)
            search_value: 搜索值
            product_type: 产品类型列表 (1=普通产品, 2=组合产品, 3=辅料)
            offset: 分页偏移量
            length: 分页长度，默认20，上限200

        Returns:
            Dict包含:
            - records: 供应商报表数据列表
            - total: 总数
        """
        logger.debug("Fetching purchase report supplier: %s ~ %s", start_date, end_date)

        req_body = {
            "start_date": start_date,
            "end_date": end_date,
            "time_type": time_type,
            "offset": offset,
            "length": length,
        }

        if search_field:
            req_body["search_field"] = search_field
        if search_value:
            req_body["search_value"] = search_value
        if product_type:
            req_body["product_type"] = product_type

        resp_result = await self._client.request(
            access_token=access_token,
            route_name=self.PURCHASE_REPORT_SUPPLIER,
            method="POST",
            req_body=req_body,
        )

        if resp_result.code != 0:
            logger.error("Failed to fetch purchase report supplier: %s", resp_result.message)
            return {"records": [], "total": 0}

        data = resp_result.data
        if isinstance(data, list):
            return {"records": data, "total": resp_result.total or len(data)}
        return {"records": [], "total": 0}

    # ==================== 销售统计 ====================


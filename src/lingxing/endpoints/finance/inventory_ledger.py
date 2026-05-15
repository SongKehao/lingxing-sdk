#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""库存账本API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class InventoryLedgerEndpoint(BaseEndpoint):
    """库存账本API"""
    async def get_profit_report_parent_asin(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        currency_code: str = "CNY",
        monthly_query: bool = False,
        summary_enabled: bool = False,
        order_status: str = "Disbursed",
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        父ASIN利润报表

        API: POST /bd/profit/report/open/report/parent/asin/list
        验证状态: ✅ 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD（按天）或 YYYY-MM（按月）
            end_date: 结束日期，格式 YYYY-MM-DD（按天）或 YYYY-MM（按月）
            currency_code: 币种代码，默认 CNY
            monthly_query: 是否按月查询，默认 False（按天）
            summary_enabled: 是否按父ASIN汇总，默认 False
            order_status: 交易状态（Deferred/Disbursed/DisbursedAndPreSettled/All），默认 Disbursed
            offset: 偏移量，默认0
            length: 返回条数，默认1000（最大10000）
            **kwargs: 其他查询参数（如 mids, searchField, searchValue）

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_parent_asin(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching parent ASIN profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "startDate": start_date,
            "endDate": end_date,
            "currencyCode": currency_code,
            "monthlyQuery": monthly_query,
            "summaryEnabled": summary_enabled,
            "orderStatus": order_status,
            "offset": offset,
            "length": min(length, 10000),
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/parent/asin/list",
            req_body=req_body
        )

    # ==================== 订单利润报表 ====================

    async def get_profit_report_order(
        self,
        access_token: str,
        sids: list[int],
        start_date: str,
        end_date: str,
        search_date_field: str = "posted_date_locale",
        offset: int = 0,
        length: int = 100,
        **kwargs
    ) -> ResponseResult:
        """
        订单利润报表

        API: POST /bd/profit/report/open/report/order/list

        Args:
            access_token: 访问令牌
            sids: 店铺ID列表，如 [4661]
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            search_date_field: 时间类型 (posted_date_locale|fund_transfer_datetime_locale|shipment_datetime_locale)
            offset: 偏移量，默认0
            length: 返回条数，默认100
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_profit_report_order(
            ...     access_token="xxx",
            ...     sids=[4661],
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching order profit report: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date,
            "search_date_field": search_date_field,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/profit/report/open/report/order/list",
            req_body=req_body
        )

    # ==================== 库存分类账 ====================

    async def get_inventory_ledger_detail(
        self,
        access_token: str,
        seller_ids: list[str],
        start_date: str,
        end_date: str,
        fnskus: list[str] | None = None,
        asins: list[str] | None = None,
        mskus: list[str] | None = None,
        event_types: list[str] | None = None,
        disposition: str = "01",
        locations: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        库存分类账明细数据

        API: POST /cost/center/ods/detail/query

        注意: 由于亚马逊库存分类账生成数据后5天内会发生变更，
              接口获取的5天内数据是有可能发生变更的

        Args:
            access_token: 访问令牌
            seller_ids: 亚马逊店铺ID列表，如 ["AN05PRUL7R796"]
            start_date: 统计起始日期，格式 YYYY-MM-DD
            end_date: 统计结束日期，格式 YYYY-MM-DD
            fnskus: FNSKU列表（可选）
            asins: ASIN列表（可选）
            mskus: MSKU列表（可选）
            event_types: 事件类型列表（01-06），如 ["01", "02"]
                - 01: Shipments
                - 02: CustomerReturns
                - 03: WhseTransfers
                - 04: Receipts
                - 05: VendorReturns
                - 06: Adjustments
            disposition: 库存类型（01=SELLABLE, 02=UNSELLABLE, 03=ALL），默认 01
            locations: 国家编码列表（可选）
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大1000）
            **kwargs: 其他查询参数（如 referenceId）

        Returns:
            ResponseResult: 包含 {total, size, current, records: [...]}

        Example:
            >>> result = await finance.get_inventory_ledger_detail(
            ...     access_token="xxx",
            ...     seller_ids=["AN05PRUL7R796"],
            ...     start_date="2024-03-02",
            ...     end_date="2024-06-01"
            ... )
        """
        logger.debug("Fetching inventory ledger detail: seller_ids=%s, start=%s, end=%s", seller_ids, start_date, end_date)

        req_body = {
            "sellerIds": seller_ids,
            "startDate": start_date,
            "endDate": end_date,
            "disposition": disposition,
            "offset": offset,
            "length": min(length, 1000),
            **kwargs
        }

        if fnskus:
            req_body["fnskus"] = fnskus
        if asins:
            req_body["asins"] = asins
        if mskus:
            req_body["mskus"] = mskus
        if event_types:
            req_body["eventTypes"] = event_types
        if locations:
            req_body["locations"] = locations

        return await self._request_with_token(
            access_token=access_token,
            route="/cost/center/ods/detail/query",
            req_body=req_body
        )

    async def get_inventory_ledger_summary(
        self,
        access_token: str,
        seller_ids: list[str],
        query_type: int,
        start_date: str,
        end_date: str,
        fnskus: list[str] | None = None,
        asins: list[str] | None = None,
        mskus: list[str] | None = None,
        disposition: str = "01",
        locations: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        库存分类账汇总数据

        API: POST /cost/center/ods/summary/query

        Args:
            access_token: 访问令牌
            seller_ids: 亚马逊店铺ID列表，如 ["AN05PRUL7R796"]
            query_type: 查询维度（1=按月，2=按天）
            start_date: 统计起始日期（月维度：YYYY-MM，天维度：YYYY-MM-DD）
            end_date: 统计结束日期（月维度：YYYY-MM，天维度：YYYY-MM-DD）
            fnskus: FNSKU列表（可选）
            asins: ASIN列表（可选）
            mskus: MSKU列表（可选）
            disposition: 库存属性（01=SELLABLE, 02=UNSELLABLE, 03=ALL），默认 01
            locations: 国家编码列表（可选）
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大1000）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, size, current, records: [...]}

        Example:
            >>> result = await finance.get_inventory_ledger_summary(
            ...     access_token="xxx",
            ...     seller_ids=["AN05PRUL7R796"],
            ...     query_type=1,
            ...     start_date="2024-04",
            ...     end_date="2024-06"
            ... )
        """
        logger.debug("Fetching inventory ledger summary: seller_ids=%s, query_type=%s", seller_ids, query_type)

        req_body = {
            "sellerIds": seller_ids,
            "queryType": query_type,
            "startDate": start_date,
            "endDate": end_date,
            "disposition": disposition,
            "offset": offset,
            "length": min(length, 1000),
            **kwargs
        }

        if fnskus:
            req_body["fnskus"] = fnskus
        if asins:
            req_body["asins"] = asins
        if mskus:
            req_body["mskus"] = mskus
        if locations:
            req_body["locations"] = locations

        return await self._request_with_token(
            access_token=access_token,
            route="/cost/center/ods/summary/query",
            req_body=req_body
        )

    # ==================== FBA成本计价流水 ====================

    async def get_fba_cost_stream(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        query_type: str = "01",
        wh_names: list[str] | None = None,
        shop_names: list[str] | None = None,
        skus: list[str] | None = None,
        mskus: list[str] | None = None,
        disposition_types: list[int] | None = None,
        business_types: list[int] | None = None,
        business_numbers: list[str] | None = None,
        origin_accounts: list[str] | None = None,
        offset: int = 0,
        length: int = 200,
        **kwargs
    ) -> ResponseResult:
        """
        FBA成本计价流水查询

        API: POST /cost/center/api/cost/stream

        注意:
        1. 由于亚马逊库存分类账生成数据后5天内会发生变更，
           接口获取的5天内数据是有可能发生变更的
        2. 日期范围不允许跨月
        3. business_types传参为1（期初库存-FBA上月结存）时，
           change_other_amount、change_logistics_amount、change_purchase_amount、
           change_quantity字段不返回

        Args:
            access_token: 访问令牌
            start_date: 起始日期，格式 YYYY-MM-DD（不允许跨月）
            end_date: 结束日期，格式 YYYY-MM-DD（不允许跨月）
            query_type: 日期查询类型（01=库存动作日期，02=结算日期），默认 01
            wh_names: 仓库名列表（可选）
            shop_names: 店铺名列表（可选）
            skus: SKU列表（可选）
            mskus: MSKU列表（可选）
            disposition_types: 库存属性列表（1=可用在途，2=可用，3=次品）
            business_types: 出入库类型列表（如 [1, 10, 11, ...]）
            business_numbers: 业务编号列表（可选）
            origin_accounts: 源头单据号列表（可选）
            offset: 偏移量，默认0
            length: 返回条数，默认200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, size, current, records: [...]}

        Example:
            >>> result = await finance.get_fba_cost_stream(
            ...     access_token="xxx",
            ...     start_date="2023-06-01",
            ...     end_date="2023-06-30",
            ...     business_types=[1]
            ... )
        """
        logger.debug("Fetching FBA cost stream: start=%s, end=%s", start_date, end_date)

        req_body = {
            "query_type": query_type,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if wh_names:
            req_body["wh_names"] = wh_names
        if shop_names:
            req_body["shop_names"] = shop_names
        if skus:
            req_body["skus"] = skus
        if mskus:
            req_body["mskus"] = mskus
        if disposition_types:
            req_body["disposition_types"] = disposition_types
        if business_types:
            req_body["business_types"] = business_types
        if business_numbers:
            req_body["business_numbers"] = business_numbers
        if origin_accounts:
            req_body["origin_accounts"] = origin_accounts

        return await self._request_with_token(
            access_token=access_token,
            route="/cost/center/api/cost/stream",
            req_body=req_body
        )

    # ==================== 费用管理 ====================


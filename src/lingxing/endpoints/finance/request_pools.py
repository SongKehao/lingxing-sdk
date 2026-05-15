#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""请求池API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class RequestPoolsEndpoint(BaseEndpoint):
    """请求池API"""
    async def get_prepay_request_pool(
        self,
        access_token: str,
        pay_status: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        time_field: str = "create_time",
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-货款预付款

        API: POST /basicOpen/finance/requestFundsPool/prepay/list

        Args:
            access_token: 访问令牌
            pay_status: 支付状态（0=未申请，1=已申请，2=部分付款，3=已付清）
            start_time: 开始时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            end_time: 结束时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            time_field: 时间搜索类型（create_time=创建时间）
            search_field: 搜索类型（purchase_order_sn=采购单号，order_sn=预付款单号）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大200）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_prepay_request_pool(
            ...     access_token="xxx",
            ...     pay_status="3",
            ...     start_time="2024-07-23",
            ...     end_time="2024-07-25"
            ... )
        """
        logger.debug("Fetching prepay request pool: pay_status=%s", pay_status)

        req_body = {
            "time_field": time_field,
            "offset": offset,
            "length": min(length, 200),
            **kwargs
        }

        if pay_status is not None:
            req_body["pay_status"] = pay_status
        if start_time:
            req_body["start_time"] = start_time
        if end_time:
            req_body["end_time"] = end_time
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/prepay/list",
            req_body=req_body
        )

    async def get_logistics_request_pool(
        self,
        access_token: str,
        search_field_time: str = "create_time",
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-物流请款

        API: POST /basicOpen/finance/requestFundsPool/logistics/list

        Args:
            access_token: 访问令牌
            search_field_time: 时间搜索类型（create_time=费用录入时间，
                               delivery_create_time=发货单创建时间，
                               shipment_time=发货时间，close_time=付清时间）
            start_time: 开始时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            end_time: 结束时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            search_field: 搜索类型（order_sn=发货单号，logistics_center_code=物流中心编码）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大200）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_logistics_request_pool(
            ...     access_token="xxx",
            ...     search_field_time="create_time",
            ...     start_time="2024-07-23",
            ...     end_time="2024-07-25"
            ... )
        """
        logger.debug("Fetching logistics request pool: time=%s", search_field_time)

        req_body = {
            "search_field_time": search_field_time,
            "offset": offset,
            "length": min(length, 200),
            **kwargs
        }

        if start_time:
            req_body["start_time"] = start_time
        if end_time:
            req_body["end_time"] = end_time
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/logistics/list",
            req_body=req_body
        )

    async def get_monthly_settlement_request_pool(
        self,
        access_token: str,
        pay_status: str | None = None,
        time_field: str = "create_time",
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-货款月结

        API: POST /basicOpen/finance/requestFundsPool/inbound/list

        Args:
            access_token: 访问令牌
            pay_status: 状态（0=未申请，10=已申请，20=已付清）
            time_field: 时间搜索类型（create_time=入库时间，prepay_time=应付款日）
            start_time: 开始时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            end_time: 结束时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            search_field: 搜索类型（order_sn=入库单号，purchase_order_sn=采购单号，sku=SKU）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大200）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_monthly_settlement_request_pool(
            ...     access_token="xxx",
            ...     pay_status="0",
            ...     time_field="create_time",
            ...     start_time="2024-07-25",
            ...     end_time="2024-07-25"
            ... )
        """
        logger.debug("Fetching monthly settlement request pool: pay_status=%s", pay_status)

        req_body = {
            "time_field": time_field,
            "offset": offset,
            "length": min(length, 200),
            **kwargs
        }

        if pay_status is not None:
            req_body["pay_status"] = pay_status
        if start_time:
            req_body["start_time"] = start_time
        if end_time:
            req_body["end_time"] = end_time
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/inbound/list",
            req_body=req_body
        )

    async def get_spot_settlement_request_pool(
        self,
        access_token: str,
        pay_status: str | None = None,
        time_field: str = "create_time",
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-货款现结

        API: POST /basicOpen/finance/requestFundsPool/purchase/list

        Args:
            access_token: 访问令牌
            pay_status: 支付状态（多个使用英文逗号分隔：0=未申请，1=已申请，2=部分付款，3=已付清）
            time_field: 时间搜索类型（create_time=创建时间）
            start_time: 开始时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            end_time: 结束时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            search_field: 搜索类型（sku=SKU，order_sn=采购单号）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大200）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_spot_settlement_request_pool(
            ...     access_token="xxx",
            ...     pay_status="0,1",
            ...     time_field="create_time",
            ...     start_time="2024-07-25",
            ...     end_time="2024-07-25"
            ... )
        """
        logger.debug("Fetching spot settlement request pool: pay_status=%s", pay_status)

        req_body = {
            "time_field": time_field,
            "offset": offset,
            "length": min(length, 200),
            **kwargs
        }

        if pay_status is not None:
            req_body["pay_status"] = pay_status
        if start_time:
            req_body["start_time"] = start_time
        if end_time:
            req_body["end_time"] = end_time
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/purchase/list",
            req_body=req_body
        )

    async def get_other_payable_request_pool(
        self,
        access_token: str,
        pay_status: str | None = None,
        search_field_time: str = "create_time",
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询请款池-其他应付款

        API: POST /basicOpen/finance/requestFundsPool/customFee/list

        Args:
            access_token: 访问令牌
            pay_status: 支付状态（多个状态用英文逗号分隔：0=未申请，1=已申请，2=部分付款，3=已付清）
            search_field_time: 时间搜索类型（create_time=创建时间，close_time=付清时间）
            start_time: 开始时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            end_time: 结束时间，格式 YYYY-MM-DD（时间间隔最长不得超过90天）
            search_field: 搜索类型（business_sn=费用单号，custom_fee_sn=其他应付单号）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20（最大200）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}

        Example:
            >>> result = await finance.get_other_payable_request_pool(
            ...     access_token="xxx",
            ...     pay_status="3",
            ...     search_field_time="create_time",
            ...     start_time="2024-07-23",
            ...     end_time="2024-07-25"
            ... )
        """
        logger.debug("Fetching other payable request pool: pay_status=%s", pay_status)

        req_body = {
            "search_field_time": search_field_time,
            "offset": offset,
            "length": min(length, 200),
            **kwargs
        }

        if pay_status is not None:
            req_body["pay_status"] = pay_status
        if start_time:
            req_body["start_time"] = start_time
        if end_time:
            req_body["end_time"] = end_time
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/finance/requestFundsPool/customFee/list",
            req_body=req_body
        )


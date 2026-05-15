#!/usr/bin/env python3
from __future__ import annotations

# -*- coding: utf-8 -*-
"""费用管理API"""

import logging  # noqa: E402
from typing import TYPE_CHECKING, Any  # noqa: E402

if TYPE_CHECKING:
    from ...core.resp_schema import ResponseResult

from ..base import BaseEndpoint  # noqa: E402

logger = logging.getLogger(__name__)


class FeeManagementEndpoint(BaseEndpoint):
    """费用管理API"""
    async def get_fee_detail_list(
        self,
        access_token: str,
        date_type: str,
        start_date: str,
        end_date: str,
        sids: list[int] | None = None,
        other_fee_type_ids: list[int] | None = None,
        status_order: int | None = None,
        dimensions: list[int] | None = None,
        apportion_status: list[int] | None = None,
        status_merge: int | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        费用明细列表查询

        API: POST /bd/fee/management/open/feeManagement/otherFee/list

        Args:
            access_token: 访问令牌
            date_type: 时间类型（gmt_create=创建日期，date=分摊日期）
            start_date: 开始时间，格式 YYYY-MM-DD
            end_date: 结束时间，格式 YYYY-MM-DD
            sids: 店铺ID列表（可选）
            other_fee_type_ids: 费用类型ID列表（可选）
            status_order: 单据状态（1=待提交，2=待审批，3=已处理，4=已驳回，5=已作废）
            dimensions: 分摊维度ID列表（1=msku，2=asin，3=店铺，4=父asin，5=sku，6=企业）
            apportion_status: 分摊状态（1=未分摊，2=已分摊-新，3=已分摊-旧，4=已分摊）
            status_merge: 分摊状态（1=未分摊，2=已分摊）
            search_field: 搜索类型（number/msku/asin/create_name/remark_order/remark_item）
            search_value: 搜索值
            offset: 偏移量，默认0
            length: 返回条数，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, records: [...]}

        Example:
            >>> result = await finance.get_fee_detail_list(
            ...     access_token="xxx",
            ...     date_type="gmt_create",
            ...     start_date="2022-12-01",
            ...     end_date="2023-12-01"
            ... )
        """
        logger.debug("Fetching fee detail list: date_type=%s, start=%s, end=%s", date_type, start_date, end_date)

        req_body = {
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if other_fee_type_ids:
            req_body["other_fee_type_ids"] = other_fee_type_ids
        if status_order is not None:
            req_body["status_order"] = status_order
        if dimensions:
            req_body["dimensions"] = dimensions
        if apportion_status:
            req_body["apportion_status"] = apportion_status
        if status_merge is not None:
            req_body["status_merge"] = status_merge
        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/fee/management/open/feeManagement/otherFee/list",
            req_body=req_body
        )

    async def create_fee_order(
        self,
        access_token: str,
        submit_type: int,
        dimension: int,
        apportion_rule: int,
        is_request_pool: int,
        remark: str,
        fee_items: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        创建费用单

        API: POST /bd/fee/management/open/feeManagement/otherFee/create

        Args:
            access_token: 访问令牌
            submit_type: 提交类型（1=暂存，2=提交）
            dimension: 分摊维度（1=msku，2=asin，3=店铺，4=父asin，5=sku，6=企业）
            apportion_rule: 分摊规则（0=无，1=按销售额，2=按销量，
                            3=店铺均摊后按销售额占比分摊，4=店铺均摊后按销量占比分摊）
            is_request_pool: 是否请款（0=否，1=是）
            remark: 费用单备注
            fee_items: 费用明细项列表，每项包含:
                - sids: 店铺ID列表（单选店铺传[id]，全部店铺传[99999999]，企业费用传[88888888]）
                - dimension_value: 维度值（如 ASIN 值）
                - date: 分摊日期，格式 YYYY-MM-DD 或 YYYY-MM
                - other_fee_type_id: 费用类型 ID
                - fee: 金额（注意正负数）
                - currency_code: 币种代码
                - remark: 费用子项备注
            **kwargs: 其他参数

        Returns:
            ResponseResult: 包含操作结果

        Example:
            >>> result = await finance.create_fee_order(
            ...     access_token="xxx",
            ...     submit_type=2,
            ...     dimension=1,
            ...     apportion_rule=1,
            ...     is_request_pool=0,
            ...     remark="备注",
            ...     fee_items=[{
            ...         "sids": [106],
            ...         "dimension_value": "FO-F20Y-K0KC",
            ...         "date": "2023-02",
            ...         "other_fee_type_id": 1167,
            ...         "fee": -100,
            ...         "currency_code": "CNY",
            ...         "remark": "费用子项备注"
            ...     }]
            ... )
        """
        logger.debug("Creating fee order: dimension=%s, submit_type=%s", dimension, submit_type)

        req_body = {
            "submit_type": submit_type,
            "dimension": dimension,
            "apportion_rule": apportion_rule,
            "is_request_pool": is_request_pool,
            "remark": remark,
            "fee_items": fee_items,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/fee/management/open/feeManagement/otherFee/create",
            req_body=req_body
        )

    async def edit_fee_order(
        self,
        access_token: str,
        fee_order_id: str,
        submit_type: int,
        dimension: int,
        apportion_rule: int,
        date: str,
        currency_code: str,
        other_fee_type_id: int,
        is_request_pool: int,
        fee_items: list[dict[str, Any]],
        remark: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        编辑费用单

        API: POST /bd/fee/management/open/feeManagement/otherFee/edit

        Args:
            access_token: 访问令牌
            fee_order_id: 费用单ID
            submit_type: 提交类型（1=暂存，2=提交）
            dimension: 分摊维度（1=msku，2=asin，3=店铺，4=父asin，5=sku，6=企业）
            apportion_rule: 分摊规则（0=无，1=按销售额，2=按销量，
                            3=店铺均摊后按销售额占比分摊，4=店铺均摊后按销量占比分摊）
            date: 分摊日期，格式 YYYY-MM-DD 或 YYYY-MM
            currency_code: 币种代码
            other_fee_type_id: 费用类型ID
            is_request_pool: 是否请款（0=否，1=是）
            fee_items: 费用明细项列表，每项包含:
                - fof_id: 费用单子项ID
                - sids: 店铺ID列表
                - dimension_value: 维度值
                - fee: 金额
                - remark: 备注
            remark: 单据备注（可选）
            **kwargs: 其他参数

        Returns:
            ResponseResult: 包含操作结果

        Example:
            >>> result = await finance.edit_fee_order(
            ...     access_token="xxx",
            ...     fee_order_id="304363977645646336",
            ...     submit_type=2,
            ...     dimension=1,
            ...     apportion_rule=1,
            ...     date="2023-09",
            ...     currency_code="CNY",
            ...     other_fee_type_id=1167,
            ...     is_request_pool=0,
            ...     fee_items=[{
            ...         "fof_id": "304363977645675520",
            ...         "sids": [106],
            ...         "dimension_value": "FO-F20Y-K0KC",
            ...         "fee": -100,
            ...         "remark": ""
            ...     }]
            ... )
        """
        logger.debug("Editing fee order: id=%s", fee_order_id)

        req_body = {
            "id": fee_order_id,
            "submit_type": submit_type,
            "dimension": dimension,
            "apportion_rule": apportion_rule,
            "date": date,
            "currency_code": currency_code,
            "other_fee_type_id": other_fee_type_id,
            "is_request_pool": is_request_pool,
            "fee_items": fee_items,
            **kwargs
        }

        if remark:
            req_body["remark"] = remark

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/fee/management/open/feeManagement/otherFee/edit",
            req_body=req_body
        )

    async def delete_fee_order(
        self,
        access_token: str,
        numbers: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        删除费用单

        API: POST /bd/fee/management/open/feeManagement/otherFee/delete

        注意: 只能删除"待提交"状态的费用单

        Args:
            access_token: 访问令牌
            numbers: 费用单号列表，上限200
            **kwargs: 其他参数

        Returns:
            ResponseResult: 包含操作结果

        Example:
            >>> result = await finance.delete_fee_order(
            ...     access_token="xxx",
            ...     numbers=["FY231009000001"]
            ... )
        """
        logger.debug("Deleting fee orders: numbers=%s", numbers)

        req_body = {
            "numbers": numbers[:200],  # 上限200
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/fee/management/open/feeManagement/otherFee/delete",
            req_body=req_body
        )

    async def discard_fee_order(
        self,
        access_token: str,
        numbers: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        作废费用单

        API: POST /bd/fee/management/open/feeManagement/otherFee/discard

        Args:
            access_token: 访问令牌
            numbers: 费用单号列表，上限200
            **kwargs: 其他参数

        Returns:
            ResponseResult: 包含操作结果

        Example:
            >>> result = await finance.discard_fee_order(
            ...     access_token="xxx",
            ...     numbers=["FY231009000001"]
            ... )
        """
        logger.debug("Discarding fee orders: numbers=%s", numbers)

        req_body = {
            "numbers": numbers[:200],  # 上限200
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/fee/management/open/feeManagement/otherFee/discard",
            req_body=req_body
        )

    # ==================== 请款池查询 ====================


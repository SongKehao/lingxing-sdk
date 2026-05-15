"""领星ERP工具类API端点封装"""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class ToolsEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    async def get_inventory_warning_messages(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        show_status: int = 1,
        model_id_list: list[int] | None = None,
        product_type_list: list[int] | None = None,
        offset: int = 0,
        length: int = 50,
        **kwargs
    ) -> ResponseResult:
        """
        库存预警消息列表

        API: POST /basicOpen/settings/warningMessage/inventoryList

        Args:
            access_token: 访问令牌
            start_date: 开始日期【提醒时间】，闭区间，格式 Y-m-d（最长不超过90天）
            end_date: 结束日期【提醒时间】，闭区间，格式 Y-m-d（最长不超过90天）
            show_status: 处理状态，0=待处理，1=全部（默认）
            model_id_list: 预警模型列表，默认查询全部
                - 4: 本地库存预警
                - 5: 亚马逊库存预警
                - 22: 本地库龄预警
                - 23: 亚马逊库龄预警
                示例: [5, 22]
            product_type_list: 产品类型列表，默认查询全部
                - 2: MSKU
                - 3: SKU+仓库+店铺+FNSKU
                示例: [2, 3]
            offset: 分页偏移量，默认0
            length: 分页长度，默认50，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [{message_id, model_id, model_name, ...}]}

        Example:
            >>> result = await tools.get_inventory_warning_messages(
            ...     access_token="xxx",
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24",
            ...     model_id_list=[5, 22],
            ...     product_type_list=[2, 3]
            ... )
            >>> data = result.data  # {"total": 10, "data": [...]}
        """
        logger.debug("Fetching inventory warning messages: start=%s, end=%s, models=%s, product_types=%s", start_date, end_date, model_id_list, product_type_list)

        req_body = {
            "offset": offset,
            "length": min(length, 200),  # 最大200
            "start_date": start_date,
            "end_date": end_date,
            "show_status": show_status,
            **kwargs
        }

        if model_id_list:
            req_body["mode_id_list"] = model_id_list  # 注意: API参数名是 mode_id_list

        if product_type_list:
            req_body["product_type_list"] = product_type_list

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/settings/warningMessage/inventoryList",
            req_body=req_body
        )

    async def get_goods_warning_messages(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        show_status: int = 1,
        model_id_list: list[int] | None = None,
        sids: list[int] | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 50,
        **kwargs
    ) -> ResponseResult:
        """
        商品预警消息列表

        API: POST /basicOpen/settings/warningMessage/goodsList

        Args:
            access_token: 访问令牌
            start_date: 开始日期【提醒时间】，闭区间，格式 Y-m-d（最长不超过90天）
            end_date: 结束日期【提醒时间】，闭区间，格式 Y-m-d（最长不超过90天）
            show_status: 处理状态，0=待处理，1=全部（默认）
            model_id_list: 预警模型列表，默认查询全部
                - 1: Listing调价预警
                - 2: FBA费变更预警
                - 3: Listing下架预警
                - 6: FBA费异常预警
                - 7: 折扣异常预警
                - 18: 业务指标预警
                - 20: 折扣叠加预警
                - 21: buybox丢失预警
                - 26: 父ASIN变更预警
                示例: [1, 2]
            sids: 店铺ID列表，如 [1, 136]
            search_field: 搜索字段，可选值: rule_name（规则名称）, asin, msku
            search_value: 搜索值，多个使用英文逗号分隔
            offset: 分页偏移量，默认0
            length: 分页长度，默认50，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [{message_id, asin, title, model_name, ...}]}

        Example:
            >>> result = await tools.get_goods_warning_messages(
            ...     access_token="xxx",
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24",
            ...     model_id_list=[1, 2],
            ...     sids=[4661],
            ...     search_field="asin",
            ...     search_value="B0CWS8MNW1"
            ... )
            >>> data = result.data  # {"total": 5, "data": [...]}
        """
        logger.debug("Fetching goods warning messages: start=%s, end=%s, models=%s, sids=%s, search=%s=%s", start_date, end_date, model_id_list, sids, search_field, search_value)

        req_body = {
            "offset": offset,
            "length": min(length, 200),  # 最大200
            "start_date": start_date,
            "end_date": end_date,
            "show_status": show_status,
            **kwargs
        }

        if model_id_list:
            req_body["model_id_list"] = model_id_list

        if sids:
            req_body["sids"] = sids

        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/settings/warningMessage/goodsList",
            req_body=req_body
        )

    # ==================== 监控工具相关API ====================

    async def get_competitive_monitor_list(
        self,
        access_token: str,
        levels: list[int] | None = None,
        update_time_start: str | None = None,
        update_time_end: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        竞品监控列表

        API: POST /basicOpen/tool/competitiveMonitor/list

        Args:
            access_token: 访问令牌
            levels: 竞品等级列表，默认查询全部
                - 1: A级
                - 2: B级
                - 3: C级
                - 4: D级
                示例: [1, 2, 3, 4]
            update_time_start: 开始时间【更新时间】，闭区间，格式 Y-m-d
            update_time_end: 结束时间【更新时间】，闭区间，格式 Y-m-d
            search_field: 搜索字段，可选值: asin
            search_value: 搜索值，多个使用英文逗号分隔，上限200
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [{mid, asin, title, level_name, ...}]}

        Example:
            >>> result = await tools.get_competitive_monitor_list(
            ...     access_token="xxx",
            ...     levels=[1, 2, 3, 4],
            ...     update_time_start="2026-02-01",
            ...     update_time_end="2026-02-24",
            ...     search_field="asin",
            ...     search_value="B0CWS8MNW1"
            ... )
            >>> data = result.data  # {"total": 10, "data": [...]}
        """
        logger.debug("Fetching competitive monitor list: levels=%s, update_time=%s~%s, search=%s=%s", levels, update_time_start, update_time_end, search_field, search_value)

        req_body = {
            "offset": offset,
            "length": min(length, 200),  # 最大200
            **kwargs
        }

        if levels:
            req_body["levels"] = levels

        if update_time_start:
            req_body["update_time_start"] = update_time_start

        if update_time_end:
            req_body["update_time_end"] = update_time_end

        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/tool/competitiveMonitor/list",
            req_body=req_body
        )

    async def get_keyword_rank_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
        mid: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        关键词排名列表

        API: POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，最大值2000
            mid: 国家ID，如 1=美国
            start_date: 开始日期，格式 Y-m-d
            end_date: 结束日期，格式 Y-m-d
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [{id, key_word, rank, page, asin, ...}]}

        Example:
            >>> result = await tools.get_keyword_rank_list(
            ...     access_token="xxx",
            ...     mid=1,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
            >>> data = result.data  # {"total": 100, "data": [...]}
        """
        logger.debug("Fetching keyword rank list: mid=%s, start_date=%s, end_date=%s", mid, start_date, end_date)

        req_body = {
            "offset": offset,
            "length": min(length, 2000),  # 最大2000
            **kwargs
        }

        if mid is not None:
            req_body["mid"] = mid

        if start_date:
            req_body["start_date"] = start_date

        if end_date:
            req_body["end_date"] = end_date

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/tool/toolKeywordRank/getKeywordList",
            req_body=req_body
        )


__all__ = [
    'ToolsEndpoints',
]

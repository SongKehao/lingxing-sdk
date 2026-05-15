"""Restocking limit API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class RestockingLimitEndpoints:
    """Restocking limit API endpoints."""

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

    async def get_ipi_info(
        self,
        access_token: str,
        sids: str | None = None,
        seller_ids: str | None = None,
        mids: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询IPI信息

        API: POST /erp/sc/routing/fbaLimit/restock/getIpiInfo

        获取亚马逊店铺的IPI（库存绩效指标）信息，包括冗余库存率、售出率、
        无在售信息的库存率、有存货库存率等关键指标。

        Args:
            access_token: 访问令牌
            sids: 店铺ID，多个用英文逗号分隔（对应查询亚马逊店铺列表接口的sid字段）
            seller_ids: 亚马逊店铺ID，多个用英文逗号分隔（对应查询亚马逊店铺列表接口的seller_id字段）
            mids: 站点ID，多个用英文逗号分隔
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含IPI信息列表
                - seller_id: 亚马逊店铺ID
                - seller_account_name: 店铺账户名称
                - seller_name: 店铺名称
                - marketplace: 国家
                - update_date: 更新时间
                - vol_unit_text: 体积单位
                - ipi: IPI分数
                - excess_inventory_rate: 冗余库存率
                - sell_through_rate: 售出率
                - stranded_inventory_rate: 无在售信息的库存率
                - in_stock_rate: 有存货库存率
                - sub_items: 各仓储类型的详细信息

        Example:
            >>> result = await restocking_limit.get_ipi_info(
            ...     access_token="xxx",
            ...     sids="4661,4662"
            ... )
            >>> data = result.data  # [{"seller_id": "...", "ipi": 528, ...}]
        """
        logger.debug(
            "Fetching IPI info: sids=%s, seller_ids=%s, mids=%s", sids, seller_ids, mids
        )

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        # 添加可选参数
        if sids:
            req_body["sids"] = sids
        if seller_ids:
            req_body["seller_ids"] = seller_ids
        if mids:
            req_body["mids"] = mids

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaLimit/restock/getIpiInfo",
            req_body=req_body
        )

    async def get_restocking_limit_list(
        self,
        access_token: str,
        storage_type: str,
        sids: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询补货限制列表

        API: POST /basicOpen/openapi/replenishmentRestriction/page/list

        获取亚马逊FBA补货限制的详细信息，包括各仓储类型的容量限制、
        使用量、剩余量等数据，支持按仓储类型筛选。

        Args:
            access_token: 访问令牌
            storage_type: 仓储类型，可选值：
                - "Standard": 标准尺寸
                - "Oversize": 大件
                - "Apparel": 服装
                - "Footwear": 鞋靴
                - "ExtraLarge": 超大
            sids: 店铺ID，多个用英文逗号分隔（对应查询亚马逊店铺列表接口的sid字段）
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含补货限制列表
                - data.month: 近4个月份列表
                - list: 店铺补货限制详情列表
                    - sid: 店铺ID
                    - vol_unit_type: 体积单位类型（1=立方米，2=立方英尺）
                    - ipi: IPI分数
                    - update_type: 更新类型（1=插件，2=手动，3=导入）
                    - excess_inventory_rate: 冗余库存率
                    - sell_through_rate: 售出率
                    - stranded_inventory_rate: 无在售信息的库存率
                    - in_stock_rate: 有存货库存率
                    - items: 近4个月的体积和数量限制详情
                    - overview: 当月数据概览
                    - sub_items: 各月份详细数据

        Example:
            >>> result = await restocking_limit.get_restocking_limit_list(
            ...     access_token="xxx",
            ...     storage_type="Standard",
            ...     sids="4661"
            ... )
            >>> data = result.data  # {"data": {"month": [...]}, "list": [...]}
        """
        logger.debug(
            "Fetching restocking limit list: storage_type=%s, sids=%s", storage_type, sids
        )

        req_body = {
            "storage_type": storage_type,
            "offset": offset,
            "length": min(length, 200),  # 上限200
            **kwargs
        }

        # 添加可选参数
        if sids:
            req_body["sids"] = sids

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/replenishmentRestriction/page/list",
            req_body=req_body
        )


__all__ = [
    'RestockingLimitEndpoints',
]

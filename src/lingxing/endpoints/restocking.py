"""Restocking suggestion API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class RestockingEndpoints:
    """Restocking suggestion API endpoints."""

    def __init__(self, openapi: OpenApiBase):
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== 补货列表查询 ====================

    async def get_restocking_list(
        self,
        access_token: str,
        data_type: int,
        sid_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        msku_list: list[str] | None = None,
        mode: int | None = None,
        listing_date_range: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询补货列表

        API: POST /erp/sc/routing/restocking/analysis/getSummaryList

        Args:
            access_token: 访问令牌
            data_type: 查询维度，1=ASIN, 2=MSKU
            sid_list: 店铺ID列表，如 ["136", "139"]
            asin_list: 按ASIN列表筛选数据
            msku_list: 按MSKU列表筛选数据
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式
            listing_date_range: Listing创建时间范围，如 ["2023-06-06", "2024-07-13"]
            offset: 分页偏移量，默认0
            length: 分页条数，默认20，上限50
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [{basic_info, amazon_quantity_info, scm_quantity_info, sales_info, suggest_info, ext_info, item_list}]}

        Example:
            >>> result = await restocking.get_restocking_list(
            ...     access_token="xxx",
            ...     data_type=1,
            ...     sid_list=["136", "139"],
            ...     offset=0,
            ...     length=20
            ... )
        """
        logger.debug("Fetching restocking list: data_type=%s, offset=%s, length=%s", data_type, offset, length)

        req_body = {
            "data_type": data_type,
            "offset": offset,
            "length": min(length, 50),  # 最大50
            **kwargs
        }

        if sid_list:
            req_body["sid_list"] = sid_list
        if asin_list:
            req_body["asin_list"] = asin_list
        if msku_list:
            req_body["msku_list"] = msku_list
        if mode is not None:
            req_body["mode"] = mode
        if listing_date_range:
            req_body["listing_date_range"] = listing_date_range

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/restocking/analysis/getSummaryList",
            req_body=req_body
        )

    # ==================== MSKU维度API ====================

    async def get_msku_restocking_info(
        self,
        access_token: str,
        sid: int,
        msku: str,
        mode: int | None = None
    ) -> ResponseResult:
        """
        查询MSKU维度补货建议信息

        API: POST /erp/sc/routing/fbaSug/msku/getInfo

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            msku: MSKU编码
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式（不传默认取ERP当前设置模式）

        Returns:
            ResponseResult: 包含MSKU补货建议详情

        Example:
            >>> result = await restocking.get_msku_restocking_info(
            ...     access_token="xxx",
            ...     sid=136,
            ...     msku="CNxxxx",
            ...     mode=0
            ... )
        """
        logger.debug("Fetching MSKU restocking info: sid=%s, msku=%s, mode=%s", sid, msku, mode)

        req_body = {
            "sid": sid,
            "msku": msku
        }

        if mode is not None:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/getInfo",
            req_body=req_body
        )

    async def get_msku_restocking_config(
        self,
        access_token: str,
        sid: int,
        msku: str
    ) -> ResponseResult:
        """
        查询MSKU补货规则配置

        API: POST /erp/sc/routing/fbaSug/msku/getConfig

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            msku: MSKU编码

        Returns:
            ResponseResult: 包含 {info: {days_total, days_plan, ...}, list: [...], denoise: [...]}

        Example:
            >>> result = await restocking.get_msku_restocking_config(
            ...     access_token="xxx",
            ...     sid=136,
            ...     msku="CNxxxx"
            ... )
        """
        logger.debug("Fetching MSKU restocking config: sid=%s, msku=%s", sid, msku)

        req_body = {
            "sid": sid,
            "msku": msku
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/getConfig",
            req_body=req_body
        )

    async def get_msku_source_list(
        self,
        access_token: str,
        sid: int,
        msku: str,
        source_type: str | None = None,
        mode: str | None = None
    ) -> ResponseResult:
        """
        查询MSKU报表型数据明细（库存来源明细）

        API: POST /erp/sc/routing/fbaSug/msku/getSourceList

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            msku: MSKU编码
            source_type: 数据类型，1=FBA可售，2=FBA在途，3=本地可用，4=待检量，5=待交付，6=采购计划，8=海外仓可用，9=海外仓在途
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式

        Returns:
            ResponseResult: 包含 {mode, source_list: [{quantity, type, amazon_sale_date, remark, expect_arrive_time}]}

        Example:
            >>> result = await restocking.get_msku_source_list(
            ...     access_token="xxx",
            ...     sid=136,
            ...     msku="CNxxxx",
            ...     source_type="3"
            ... )
        """
        logger.debug("Fetching MSKU source list: sid=%s, msku=%s, type=%s", sid, msku, source_type)

        req_body = {
            "sid": sid,
            "msku": msku
        }

        if source_type:
            req_body["type"] = source_type
        if mode:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/getSourceList",
            req_body=req_body
        )

    async def get_msku_daily_sales_forecast(
        self,
        access_token: str,
        sid: int,
        msku: str,
        sug_type: int,
        mode: int | None = None
    ) -> ResponseResult:
        """
        按MSKU查询FBA补货建议图表（未来销量预测和库存预测）

        API: POST /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            msku: MSKU编码
            sug_type: 建议类型，1=建议采购量，2=建议本地仓发货量，3=建议海外仓发货量
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式

        Returns:
            ResponseResult: 包含 {list: {日期: [到货量, 当日销量, 实时库存]}, sug_date_line: [...]}

        Example:
            >>> result = await restocking.get_msku_daily_sales_forecast(
            ...     access_token="xxx",
            ...     sid=136,
            ...     msku="CNxxxx",
            ...     sug_type=1,
            ...     mode=1
            ... )
        """
        logger.debug("Fetching MSKU daily sales forecast: sid=%s, msku=%s, sug_type=%s", sid, msku, sug_type)

        req_body = {
            "sid": sid,
            "msku": msku,
            "sug_type": sug_type
        }

        if mode is not None:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature",
            req_body=req_body
        )

    async def set_msku_restocking_config(
        self,
        access_token: str,
        sid: int,
        msku: str,
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[dict[str, str]],
        sm_oversea_list: list[dict[str, str]],
        days_oversea_to_fba: int,
        days_frequency_purchase: int,
        days_frequency_local_send: int,
        days_frequency_oversea_send: int,
        safe_day: int,
        is_ignore_certainly_short: int,
        is_ignore_history_out_stock: int,
        config_list: list[dict[str, Any]],
        denoise_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        设置单个MSKU的FBA补货建议规则

        API: POST /erp/sc/routing/fbaSug/msku/setConfig

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            msku: MSKU编码
            days_plan: 采购计划时长
            days_qc: 质检时长
            sm_fba_list: 本地仓至FBA时效列表，如 [{"sm_id": "xxx", "days": "25"}]
            sm_oversea_list: 本地仓至海外仓时效列表
            days_oversea_to_fba: 海外仓至FBA天数
            days_frequency_purchase: 采购频率
            days_frequency_local_send: 本地仓发货频率
            days_frequency_oversea_send: 海外仓发货频率
            safe_day: 安全天数
            is_ignore_certainly_short: 建议量扣除必断货量，0=否，1=是
            is_ignore_history_out_stock: 历史销量排除断货数据，0=否，1=是
            config_list: 日销量设置列表
            denoise_list: 日销量去噪设置列表
            **kwargs: 其他参数（如已弃用字段）

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await restocking.set_msku_restocking_config(
            ...     access_token="xxx",
            ...     sid=3,
            ...     msku="xxxxx",
            ...     days_plan="2",
            ...     days_qc="3",
            ...     sm_fba_list=[{"sm_id": "241250000631390721", "days": "25"}],
            ...     sm_oversea_list=[{"sm_id": "241250000631390721", "days": "20"}],
            ...     days_oversea_to_fba=0,
            ...     days_frequency_purchase=0,
            ...     days_frequency_local_send=0,
            ...     days_frequency_oversea_send=0,
            ...     safe_day=14,
            ...     is_ignore_certainly_short=0,
            ...     is_ignore_history_out_stock=0,
            ...     config_list=[{...}],
            ...     denoise_list=[{...}]
            ... )
        """
        logger.debug("Setting MSKU restocking config: sid=%s, msku=%s", sid, msku)

        req_body = {
            "sid": sid,
            "msku": msku,
            "days_plan": days_plan,
            "days_qc": days_qc,
            "sm_fba_list": sm_fba_list,
            "sm_oversea_list": sm_oversea_list,
            "days_oversea_to_fba": days_oversea_to_fba,
            "days_frequency_purchase": days_frequency_purchase,
            "days_frequency_local_send": days_frequency_local_send,
            "days_frequency_oversea_send": days_frequency_oversea_send,
            "safe_day": safe_day,
            "is_ignore_certainly_short": is_ignore_certainly_short,
            "is_ignore_history_out_stock": is_ignore_history_out_stock,
            "config_list": config_list,
            "denoise_list": denoise_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/setConfig",
            req_body=req_body
        )

    async def set_msku_restocking_configs(
        self,
        access_token: str,
        msku_list: list[dict[str, Any]],
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[dict[str, str]],
        sm_oversea_list: list[dict[str, str]],
        days_oversea_to_fba: int,
        days_frequency_purchase: int,
        days_frequency_local_send: int,
        days_frequency_oversea_send: int,
        safe_day: int,
        is_ignore_certainly_short: int,
        is_ignore_history_out_stock: int,
        config_list: list[dict[str, Any]],
        denoise_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        批量设置MSKU的补货建议规则

        API: POST /erp/sc/routing/fbaSug/msku/setConfigs

        Args:
            access_token: 访问令牌
            msku_list: MSKU信息列表，如 [{"sid": 3, "msku": "XXXXX"}]
            days_plan: 采购计划时长
            days_qc: 质检时长
            sm_fba_list: 本地仓至FBA时效列表
            sm_oversea_list: 本地仓至海外仓时效列表
            days_oversea_to_fba: 海外仓至FBA天数
            days_frequency_purchase: 采购频率
            days_frequency_local_send: 本地仓发货频率
            days_frequency_oversea_send: 海外仓发货频率
            safe_day: 安全天数
            is_ignore_certainly_short: 建议量扣除必断货量，0=否，1=是
            is_ignore_history_out_stock: 历史销量排除断货数据，0=否，1=是
            config_list: 日销量设置列表
            denoise_list: 日销量去噪设置列表
            **kwargs: 其他参数

        Returns:
            ResponseResult: 操作结果，error_details包含失败的记录

        Example:
            >>> result = await restocking.set_msku_restocking_configs(
            ...     access_token="xxx",
            ...     msku_list=[{"sid": 3, "msku": "XXXXX"}],
            ...     days_plan="2",
            ...     days_qc="3",
            ...     sm_fba_list=[{"sm_id": "241250000631390721", "days": "25"}],
            ...     sm_oversea_list=[{"sm_id": "241250000631390721", "days": "20"}],
            ...     days_oversea_to_fba=0,
            ...     days_frequency_purchase=0,
            ...     days_frequency_local_send=0,
            ...     days_frequency_oversea_send=0,
            ...     safe_day=14,
            ...     is_ignore_certainly_short=0,
            ...     is_ignore_history_out_stock=0,
            ...     config_list=[{...}],
            ...     denoise_list=[{...}]
            ... )
        """
        logger.debug("Batch setting MSKU restocking configs: count=%s", len(msku_list))

        req_body = {
            "msku_list": msku_list,
            "days_plan": days_plan,
            "days_qc": days_qc,
            "sm_fba_list": sm_fba_list,
            "sm_oversea_list": sm_oversea_list,
            "days_oversea_to_fba": days_oversea_to_fba,
            "days_frequency_purchase": days_frequency_purchase,
            "days_frequency_local_send": days_frequency_local_send,
            "days_frequency_oversea_send": days_frequency_oversea_send,
            "safe_day": safe_day,
            "is_ignore_certainly_short": is_ignore_certainly_short,
            "is_ignore_history_out_stock": is_ignore_history_out_stock,
            "config_list": config_list,
            "denoise_list": denoise_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/msku/setConfigs",
            req_body=req_body
        )

    # ==================== ASIN维度API ====================

    async def get_asin_restocking_info(
        self,
        access_token: str,
        sid: int,
        asin: str,
        mode: int | None = None
    ) -> ResponseResult:
        """
        查询ASIN维度补货建议信息

        API: POST /erp/sc/routing/fbaSug/asin/getInfo

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            asin: ASIN编码
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式（不传默认取ERP当前设置模式）

        Returns:
            ResponseResult: 包含ASIN补货建议详情

        Example:
            >>> result = await restocking.get_asin_restocking_info(
            ...     access_token="xxx",
            ...     sid=136,
            ...     asin="B0xxxxxxxx",
            ...     mode=0
            ... )
        """
        logger.debug("Fetching ASIN restocking info: sid=%s, asin=%s, mode=%s", sid, asin, mode)

        req_body = {
            "sid": sid,
            "asin": asin
        }

        if mode is not None:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/getInfo",
            req_body=req_body
        )

    async def get_asin_restocking_config(
        self,
        access_token: str,
        sid: int,
        asin: str
    ) -> ResponseResult:
        """
        查询ASIN补货规则配置

        API: POST /erp/sc/routing/fbaSug/asin/getConfig

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            asin: ASIN编码

        Returns:
            ResponseResult: 包含 {info: {days_total, days_plan, ...}, list: [...], denoise: [...]}

        Example:
            >>> result = await restocking.get_asin_restocking_config(
            ...     access_token="xxx",
            ...     sid=136,
            ...     asin="B0xxxxxxxx"
            ... )
        """
        logger.debug("Fetching ASIN restocking config: sid=%s, asin=%s", sid, asin)

        req_body = {
            "sid": sid,
            "asin": asin
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/getConfig",
            req_body=req_body
        )

    async def get_asin_source_list(
        self,
        access_token: str,
        sid: int,
        asin: str,
        source_type: str | None = None,
        mode: str | None = None
    ) -> ResponseResult:
        """
        查询ASIN报表型数据明细（库存来源明细）

        API: POST /erp/sc/routing/fbaSug/asin/getSourceList

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            asin: ASIN编码
            source_type: 数据类型，1=FBA可售，2=FBA在途，3=本地可用，4=待检量，5=待交付，6=采购计划，8=海外仓可用，9=海外仓在途
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式

        Returns:
            ResponseResult: 包含 {mode, source_list: [{quantity, type, amazon_sale_date, remark, expect_arrive_time}]}

        Example:
            >>> result = await restocking.get_asin_source_list(
            ...     access_token="xxx",
            ...     sid=136,
            ...     asin="B0xxxxxxxx",
            ...     source_type="3"
            ... )
        """
        logger.debug("Fetching ASIN source list: sid=%s, asin=%s, type=%s", sid, asin, source_type)

        req_body = {
            "sid": sid,
            "asin": asin
        }

        if source_type:
            req_body["type"] = source_type
        if mode:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/getSourceList",
            req_body=req_body
        )

    async def get_asin_daily_sales_forecast(
        self,
        access_token: str,
        sid: int,
        asin: str,
        sug_type: int,
        mode: int | None = None
    ) -> ResponseResult:
        """
        按ASIN查询FBA补货建议图表（未来销量预测和库存预测）

        API: POST /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            asin: ASIN编码
            sug_type: 建议类型，1=建议采购量，2=建议本地仓发货量，3=建议海外仓发货量
            mode: 补货建议模式，0=普通模式，1=海外仓中转模式

        Returns:
            ResponseResult: 包含 {list: {日期: [到货量, 当日销量, 实时库存]}, sug_date_line: [...]}

        Example:
            >>> result = await restocking.get_asin_daily_sales_forecast(
            ...     access_token="xxx",
            ...     sid=136,
            ...     asin="B0xxxxxxxx",
            ...     sug_type=3,
            ...     mode=1
            ... )
        """
        logger.debug("Fetching ASIN daily sales forecast: sid=%s, asin=%s, sug_type=%s", sid, asin, sug_type)

        req_body = {
            "sid": sid,
            "asin": asin,
            "sug_type": sug_type
        }

        if mode is not None:
            req_body["mode"] = mode

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature",
            req_body=req_body
        )

    async def set_asin_restocking_config(
        self,
        access_token: str,
        sid: int,
        asin: str,
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[dict[str, str]],
        sm_oversea_list: list[dict[str, str]],
        days_oversea_to_fba: int,
        days_frequency_purchase: int,
        days_frequency_local_send: int,
        days_frequency_oversea_send: int,
        safe_day: int,
        is_ignore_certainly_short: int,
        is_ignore_history_out_stock: int,
        config_list: list[dict[str, Any]],
        denoise_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        设置单个ASIN的FBA补货建议规则

        API: POST /erp/sc/routing/fbaSug/asin/setConfig

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            asin: ASIN编码
            days_plan: 采购计划时长
            days_qc: 质检时长
            sm_fba_list: 本地仓至FBA时效列表，如 [{"sm_id": "xxx", "days": "25"}]
            sm_oversea_list: 本地仓至海外仓时效列表
            days_oversea_to_fba: 海外仓至FBA天数
            days_frequency_purchase: 采购频率
            days_frequency_local_send: 本地仓发货频率
            days_frequency_oversea_send: 海外仓发货频率
            safe_day: 安全天数
            is_ignore_certainly_short: 建议量扣除必断货量，0=否，1=是
            is_ignore_history_out_stock: 历史销量排除断货数据，0=否，1=是
            config_list: 日销量设置列表
            denoise_list: 日销量去噪设置列表
            **kwargs: 其他参数（如已弃用字段）

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await restocking.set_asin_restocking_config(
            ...     access_token="xxx",
            ...     sid=3,
            ...     asin="xxxxx",
            ...     days_plan="2",
            ...     days_qc="3",
            ...     sm_fba_list=[{"sm_id": "241250000631390721", "days": "25"}],
            ...     sm_oversea_list=[{"sm_id": "241250000631390721", "days": "20"}],
            ...     days_oversea_to_fba=0,
            ...     days_frequency_purchase=0,
            ...     days_frequency_local_send=0,
            ...     days_frequency_oversea_send=0,
            ...     safe_day=14,
            ...     is_ignore_certainly_short=0,
            ...     is_ignore_history_out_stock=0,
            ...     config_list=[{...}],
            ...     denoise_list=[{...}]
            ... )
        """
        logger.debug("Setting ASIN restocking config: sid=%s, asin=%s", sid, asin)

        req_body = {
            "sid": sid,
            "asin": asin,
            "days_plan": days_plan,
            "days_qc": days_qc,
            "sm_fba_list": sm_fba_list,
            "sm_oversea_list": sm_oversea_list,
            "days_oversea_to_fba": days_oversea_to_fba,
            "days_frequency_purchase": days_frequency_purchase,
            "days_frequency_local_send": days_frequency_local_send,
            "days_frequency_oversea_send": days_frequency_oversea_send,
            "safe_day": safe_day,
            "is_ignore_certainly_short": is_ignore_certainly_short,
            "is_ignore_history_out_stock": is_ignore_history_out_stock,
            "config_list": config_list,
            "denoise_list": denoise_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/setConfig",
            req_body=req_body
        )

    async def set_asin_restocking_configs(
        self,
        access_token: str,
        asin_list: list[dict[str, Any]],
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[dict[str, str]],
        sm_oversea_list: list[dict[str, str]],
        days_oversea_to_fba: int,
        days_frequency_purchase: int,
        days_frequency_local_send: int,
        days_frequency_oversea_send: int,
        safe_day: int,
        is_ignore_certainly_short: int,
        is_ignore_history_out_stock: int,
        config_list: list[dict[str, Any]],
        denoise_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        批量设置ASIN的补货建议规则

        API: POST /erp/sc/routing/fbaSug/asin/setConfigs

        Args:
            access_token: 访问令牌
            asin_list: ASIN信息列表，如 [{"sid": 3, "asin": "XXXXX"}]
            days_plan: 采购计划时长
            days_qc: 质检时长
            sm_fba_list: 本地仓至FBA时效列表
            sm_oversea_list: 本地仓至海外仓时效列表
            days_oversea_to_fba: 海外仓至FBA天数
            days_frequency_purchase: 采购频率
            days_frequency_local_send: 本地仓发货频率
            days_frequency_oversea_send: 海外仓发货频率
            safe_day: 安全天数
            is_ignore_certainly_short: 建议量扣除必断货量，0=否，1=是
            is_ignore_history_out_stock: 历史销量排除断货数据，0=否，1=是
            config_list: 日销量设置列表
            denoise_list: 日销量去噪设置列表
            **kwargs: 其他参数

        Returns:
            ResponseResult: 操作结果，error_details包含失败的记录

        Example:
            >>> result = await restocking.set_asin_restocking_configs(
            ...     access_token="xxx",
            ...     asin_list=[{"sid": 3, "asin": "XXXXX"}],
            ...     days_plan="2",
            ...     days_qc="3",
            ...     sm_fba_list=[{"sm_id": "241250000631390721", "days": "25"}],
            ...     sm_oversea_list=[{"sm_id": "241250000631390721", "days": "20"}],
            ...     days_oversea_to_fba=0,
            ...     days_frequency_purchase=0,
            ...     days_frequency_local_send=0,
            ...     days_frequency_oversea_send=0,
            ...     safe_day=14,
            ...     is_ignore_certainly_short=0,
            ...     is_ignore_history_out_stock=0,
            ...     config_list=[{...}],
            ...     denoise_list=[{...}]
            ... )
        """
        logger.debug("Batch setting ASIN restocking configs: count=%s", len(asin_list))

        req_body = {
            "asin_list": asin_list,
            "days_plan": days_plan,
            "days_qc": days_qc,
            "sm_fba_list": sm_fba_list,
            "sm_oversea_list": sm_oversea_list,
            "days_oversea_to_fba": days_oversea_to_fba,
            "days_frequency_purchase": days_frequency_purchase,
            "days_frequency_local_send": days_frequency_local_send,
            "days_frequency_oversea_send": days_frequency_oversea_send,
            "safe_day": safe_day,
            "is_ignore_certainly_short": is_ignore_certainly_short,
            "is_ignore_history_out_stock": is_ignore_history_out_stock,
            "config_list": config_list,
            "denoise_list": denoise_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fbaSug/asin/setConfigs",
            req_body=req_body
        )


__all__ = [
    'RestockingEndpoints',
]

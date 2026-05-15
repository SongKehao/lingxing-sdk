"""Restocking API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class RestockingEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def asin(
        self,
        access_token: str,
        sid: int,
        asin: str,
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[Any],
        sm_oversea_list: list[Any],
        days_oversea_to_fba: Any,
        days_frequency_purchase: Any,
        days_frequency_local_send: Any,
        days_frequency_oversea_send: Any,
        safe_day: Any,
        is_ignore_certainly_short: Any,
        is_ignore_history_out_stock: Any,
        config_list: list[Any],
        denoise_list: list[Any],
        days_toucheng: Any | None = None,
        days_oversea: Any | None = None,
        days_toucheng_air: Any | None = None,
        days_oversea_air: Any | None = None,
        default_type_toucheng: Any | None = None,
        default_type_oversea: Any | None = None,
        days_frequency: Any | None = None
    ) -> dict[str, Any]:
        """
        单个设置规则-ASIN

        API: /erp/sc/routing/fbaSug/asin/setConfig
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            asin: ASIN (Required)
            days_plan: 采购计划时长 (Required)
            days_qc: 质检时长 (Required)
            sm_fba_list: 本地仓至FBA时效 (Required)
            sm_oversea_list: 本地仓至海外仓时效 (Required)
            days_oversea_to_fba: 海外仓至FBA天数 (Required)
            days_frequency_purchase: 采购频率 (Required)
            days_frequency_local_send: 本地仓发货频率 (Required)
            days_frequency_oversea_send: 海外仓发货频率 (Required)
            safe_day: 安全天数 (Required)
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (Required)
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (Required)
            days_toucheng: 已弃用（原本地至FBA天数-海运） (Optional)
            days_oversea: 已弃用（原本地至海外仓天数-海运） (Optional)
            days_toucheng_air: 已弃用（原本地至FBA时效-空运） (Optional)
            days_oversea_air: 已弃用（原本地至海外仓时效-空运） (Optional)
            default_type_toucheng: 已弃用（原默认头程物流类型） (Optional)
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型） (Optional)
            days_frequency: 已弃用（原补货频率） (Optional)
            config_list: 日销量设置 (Required)
            denoise_list: 日销量去噪设置 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.asin(token, ...)
            >>> print(result)
        """
        params = {
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
            "days_toucheng": days_toucheng,
            "days_oversea": days_oversea,
            "days_toucheng_air": days_toucheng_air,
            "days_oversea_air": days_oversea_air,
            "default_type_toucheng": default_type_toucheng,
            "default_type_oversea": default_type_oversea,
            "days_frequency": days_frequency,
            "config_list": config_list,
            "denoise_list": denoise_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/setConfig",
            method="POST",
            req_body=params
        )



    async def msku(
        self,
        access_token: str,
        sid: int,
        msku: str,
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[Any],
        sm_oversea_list: list[Any],
        days_oversea_to_fba: Any,
        days_frequency_purchase: Any,
        days_frequency_local_send: Any,
        days_frequency_oversea_send: Any,
        safe_day: Any,
        is_ignore_certainly_short: Any,
        is_ignore_history_out_stock: Any,
        config_list: list[Any],
        denoise_list: list[Any],
        days_toucheng: Any | None = None,
        days_oversea: Any | None = None,
        days_toucheng_air: Any | None = None,
        days_oversea_air: Any | None = None,
        default_type_toucheng: Any | None = None,
        default_type_oversea: Any | None = None,
        days_frequency: Any | None = None
    ) -> dict[str, Any]:
        """
        单个设置规则-MSKU

        API: /erp/sc/routing/fbaSug/msku/setConfig
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)
            days_plan: 采购计划时长 (Required)
            days_qc: 质检时长 (Required)
            sm_fba_list: 本地仓至FBA时效 (Required)
            sm_oversea_list: 本地仓至海外仓时效 (Required)
            days_oversea_to_fba: 海外仓至FBA天数 (Required)
            days_frequency_purchase: 采购频率 (Required)
            days_frequency_local_send: 本地仓发货频率 (Required)
            days_frequency_oversea_send: 海外仓发货频率 (Required)
            safe_day: 安全天数 (Required)
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (Required)
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (Required)
            days_toucheng: 已弃用（原本地至FBA天数-海运） (Optional)
            days_oversea: 已弃用（原本地至海外仓天数-海运） (Optional)
            days_toucheng_air: 已弃用（原本地至FBA时效-空运） (Optional)
            days_oversea_air: 已弃用（原本地至海外仓时效-空运） (Optional)
            default_type_toucheng: 已弃用（原默认头程物流类型） (Optional)
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型） (Optional)
            days_frequency: 已弃用（原补货频率） (Optional)
            config_list: 日销量设置 (Required)
            denoise_list: 日销量去噪设置 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.msku(token, ...)
            >>> print(result)
        """
        params = {
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
            "days_toucheng": days_toucheng,
            "days_oversea": days_oversea,
            "days_toucheng_air": days_toucheng_air,
            "days_oversea_air": days_oversea_air,
            "default_type_toucheng": default_type_toucheng,
            "default_type_oversea": default_type_oversea,
            "days_frequency": days_frequency,
            "config_list": config_list,
            "denoise_list": denoise_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/setConfig",
            method="POST",
            req_body=params
        )



    async def get_asinfbarestockingsuggestion(
        self,
        access_token: str,
        sid: int,
        asin: str
    ) -> dict[str, Any]:
        """
        按ASIN查询FBA补货建议图表

        API: /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            asin: ASIN (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_asinfbarestockingsuggestion(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "asin": asin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature",
            method="GET",
            req_body=params
        )



    async def get_suggestioninfo_asin(
        self,
        access_token: str,
        sid: int,
        asin: str
    ) -> dict[str, Any]:
        """
        查询建议信息-ASIN

        API: /erp/sc/routing/fbaSug/asin/getInfo
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            asin: ASIN (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_suggestioninfo_asin(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "asin": asin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/getInfo",
            method="GET",
            req_body=params
        )



    async def get_msku(
        self,
        access_token: str,
        sid: str,
        msku: str
    ) -> dict[str, Any]:
        """
        查询规则 - MSKU

        API: /erp/sc/routing/fbaSug/msku/getConfig
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_msku(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/getConfig",
            method="GET",
            req_body=params
        )



    async def get_suggestioninfo_msku(
        self,
        access_token: str,
        sid: int,
        msku: str
    ) -> dict[str, Any]:
        """
        查询建议信息-MSKU

        API: /erp/sc/routing/fbaSug/msku/getInfo
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_suggestioninfo_msku(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/getInfo",
            method="GET",
            req_body=params
        )



    async def get_asin(
        self,
        access_token: str,
        sid: int,
        asin: str
    ) -> dict[str, Any]:
        """
        查询规则 - ASIN

        API: /erp/sc/routing/fbaSug/asin/getConfig
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            asin: ASIN (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_asin(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "asin": asin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/getConfig",
            method="GET",
            req_body=params
        )



    async def msku(  # noqa: F811
        self,
        access_token: str,
        msku_list: list[Any],
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[Any],
        sm_oversea_list: list[Any],
        days_oversea_to_fba: Any,
        days_frequency_purchase: Any,
        days_frequency_local_send: Any,
        days_frequency_oversea_send: Any,
        safe_day: Any,
        is_ignore_certainly_short: Any,
        is_ignore_history_out_stock: Any,
        config_list: list[Any],
        denoise_list: list[Any],
        days_toucheng: Any | None = None,
        days_oversea: Any | None = None,
        days_toucheng_air: Any | None = None,
        days_oversea_air: Any | None = None,
        default_type_toucheng: Any | None = None,
        default_type_oversea: Any | None = None,
        days_frequency: Any | None = None
    ) -> dict[str, Any]:
        """
        批量设置规则 - MSKU

        API: /erp/sc/routing/fbaSug/msku/setConfigs
        Method: POST

        Args:
            access_token: Access token for authentication
            msku_list: msku信息 (Required)
            days_plan: 采购计划时长 (Required)
            days_qc: 质检时长 (Required)
            sm_fba_list: 本地仓至FBA时效 (Required)
            sm_oversea_list: 本地仓至海外仓时效 (Required)
            days_oversea_to_fba: 海外仓至FBA天数 (Required)
            days_frequency_purchase: 采购频率 (Required)
            days_frequency_local_send: 本地仓发货频率 (Required)
            days_frequency_oversea_send: 海外仓发货频率 (Required)
            safe_day: 安全天数 (Required)
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (Required)
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (Required)
            days_toucheng: 已弃用（原本地至FBA天数-海运） (Optional)
            days_oversea: 已弃用（原本地至海外仓天数-海运） (Optional)
            days_toucheng_air: 已弃用（原本地至FBA时效-空运） (Optional)
            days_oversea_air: 已弃用（原本地至海外仓时效-空运） (Optional)
            default_type_toucheng: 已弃用（原默认头程物流类型） (Optional)
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型 ） (Optional)
            days_frequency: 已弃用（原补货频率） (Optional)
            config_list: 日销量设置 (Required)
            denoise_list: 日销量去噪设置 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.msku(token, ...)
            >>> print(result)
        """
        params = {
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
            "days_toucheng": days_toucheng,
            "days_oversea": days_oversea,
            "days_toucheng_air": days_toucheng_air,
            "days_oversea_air": days_oversea_air,
            "default_type_toucheng": default_type_toucheng,
            "default_type_oversea": default_type_oversea,
            "days_frequency": days_frequency,
            "config_list": config_list,
            "denoise_list": denoise_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/setConfigs",
            method="POST",
            req_body=params
        )



    async def get_restockinglist(
        self,
        access_token: str,
        data_type: int,
        sid_list: list[Any] | None = None,
        asin_list: list[Any] | None = None,
        msku_list: list[Any] | None = None,
        listing_date_range: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询补货列表

        API: /erp/sc/routing/restocking/analysis/getSummaryList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid_list: 店铺id (Optional)
            data_type: 查询维度：1 asin，2 msku (Required)
            asin_list: 按传入的asin列表筛选数据 (Optional)
            msku_list: 按传入的msku列表筛选数据 (Optional)
            listing_date_range: listing创建时间范围筛选：[开始日期，结束日期]，必须同时包含两个日期才生效 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页条数，默认20，上限50 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_restockinglist(token, ...)
            >>> print(result)
        """
        params = {
            "sid_list": sid_list,
            "data_type": data_type,
            "asin_list": asin_list,
            "msku_list": msku_list,
            "listing_date_range": listing_date_range,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/restocking/analysis/getSummaryList",
            method="GET",
            req_body=params
        )



    async def asin(  # noqa: F811
        self,
        access_token: str,
        asin_list: list[Any],
        days_plan: str,
        days_qc: str,
        sm_fba_list: list[Any],
        sm_oversea_list: list[Any],
        days_oversea_to_fba: Any,
        days_frequency_purchase: Any,
        days_frequency_local_send: Any,
        days_frequency_oversea_send: Any,
        safe_day: Any,
        is_ignore_certainly_short: Any,
        is_ignore_history_out_stock: Any,
        config_list: list[Any],
        days_toucheng: Any | None = None,
        days_oversea: Any | None = None,
        days_toucheng_air: Any | None = None,
        days_oversea_air: Any | None = None,
        default_type_toucheng: Any | None = None,
        default_type_oversea: Any | None = None,
        days_frequency: Any | None = None,
        denoise_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        批量设置规则 - ASIN

        API: /erp/sc/routing/fbaSug/asin/setConfigs
        Method: POST

        Args:
            access_token: Access token for authentication
            asin_list: asin信息 (Required)
            days_plan: 采购计划时长 (Required)
            days_qc: 质检时长 (Required)
            sm_fba_list: 本地仓至FBA时效 (Required)
            sm_oversea_list: 本地仓至海外仓时效 (Required)
            days_oversea_to_fba: 海外仓至FBA天数 (Required)
            days_frequency_purchase: 采购频率 (Required)
            days_frequency_local_send: 本地仓发货频率 (Required)
            days_frequency_oversea_send: 海外仓发货频率 (Required)
            safe_day: 安全天数 (Required)
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (Required)
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (Required)
            days_toucheng: 已弃用（原本地至FBA天数-海运） (Optional)
            days_oversea: 已弃用（原本地至海外仓天数-海运） (Optional)
            days_toucheng_air: 已弃用（原本地至FBA时效-空运） (Optional)
            days_oversea_air: 已弃用（原本地至海外仓时效-空运） (Optional)
            default_type_toucheng: 已弃用（原默认头程物流类型） (Optional)
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型 ） (Optional)
            days_frequency: 已弃用（原补货频率） (Optional)
            config_list: 日销量设置 (Required)
            denoise_list: 日销量去噪设置 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.asin(token, ...)
            >>> print(result)
        """
        params = {
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
            "days_toucheng": days_toucheng,
            "days_oversea": days_oversea,
            "days_toucheng_air": days_toucheng_air,
            "days_oversea_air": days_oversea_air,
            "default_type_toucheng": default_type_toucheng,
            "default_type_oversea": default_type_oversea,
            "days_frequency": days_frequency,
            "config_list": config_list,
            "denoise_list": denoise_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/setConfigs",
            method="POST",
            req_body=params
        )



    async def get_mskufbarestockingsuggestion(
        self,
        access_token: str,
        sid: int,
        msku: str
    ) -> dict[str, Any]:
        """
        按MSKU查询FBA补货建议图表

        API: /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_mskufbarestockingsuggestion(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature",
            method="GET",
            req_body=params
        )



    async def get_reportdatadetail_msku(
        self,
        access_token: str,
        sid: int,
        msku: str
    ) -> dict[str, Any]:
        """
        查询报表型数据明细-MSKU

        API: /erp/sc/routing/fbaSug/msku/getSourceList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportdatadetail_msku(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/msku/getSourceList",
            method="GET",
            req_body=params
        )



    async def get_reportdatadetail_asin(
        self,
        access_token: str,
        sid: int,
        asin: str
    ) -> dict[str, Any]:
        """
        查询报表型数据明细-ASIN

        API: /erp/sc/routing/fbaSug/asin/getSourceList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            asin: ASIN (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportdatadetail_asin(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "asin": asin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fbaSug/asin/getSourceList",
            method="GET",
            req_body=params
        )


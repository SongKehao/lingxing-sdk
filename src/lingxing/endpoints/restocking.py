"""FBA补货建议 API endpoints."""

from __future__ import annotations

from ..models.responses.fba_sug import (
    FbasugAsinGetconfigResponse,
    FbasugAsinGetdailysalesinfofeatureResponse,
    FbasugAsinGetinfoResponse,
    FbasugAsinGetsourcelistResponse,
    FbasugAsinSetconfigsResponse,
    FbasugMskuGetconfigResponse,
    FbasugMskuGetdailysalesinfofeatureResponse,
    FbasugMskuGetinfoResponse,
    FbasugMskuGetsourcelistResponse,
    FbasugMskuSetconfigsResponse,
    RestockingAnalysisGetsummarylistResponse,
)
from ._base import BaseEndpoint


class RestockingEndpoints(BaseEndpoint):
    """领星FBA补货建议 API (13个接口)."""

    async def config_asin(self, sid: int = None, asin: str = None) -> FbasugAsinGetconfigResponse | None:
        """查询规则 - ASIN.

        POST /erp/sc/routing/fbaSug/asin/getConfig

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin: ASIN (required), string."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/getConfig",
            {k: v for k, v in {"sid": sid, "asin": asin}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugAsinGetconfigResponse)

    async def config_msku(self, sid: str = None, msku: str = None) -> FbasugMskuGetconfigResponse | None:
        """查询规则 - MSKU.

        POST /erp/sc/routing/fbaSug/msku/getConfig

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
            msku: MSKU (required), string."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/getConfig",
            {k: v for k, v in {"sid": sid, "msku": msku}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugMskuGetconfigResponse)

    async def daily_sales_info_feature_asin(
        self, sid: int = None, asin: str = None, sug_type: int = None, mode: int = None
    ) -> FbasugAsinGetdailysalesinfofeatureResponse | None:
        """按ASIN查询FBA补货建议图表.

        POST /erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin: ASIN (required), string.
            sug_type: 建议类型： 1 建议采购量 2 建议本地仓发货量 3 建议海外仓发货量 (required), int.
            mode: 补货建议模式： 0=普通模式 1=海外仓中转模式 不传默认取系统当前设置模式, int."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature",
            {k: v for k, v in {"sid": sid, "asin": asin, "sug_type": sug_type, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugAsinGetdailysalesinfofeatureResponse)

    async def daily_sales_info_feature_msku(
        self, sid: int = None, msku: str = None, sug_type: int = None, mode: int = None
    ) -> FbasugMskuGetdailysalesinfofeatureResponse | None:
        """按MSKU查询FBA补货建议图表.

        POST /erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            msku: MSKU (required), string.
            sug_type: 建议类型： 1 建议采购量 2 建议本地仓发货量 3 建议海外仓发货量 (required), int.
            mode: 补货建议模式： 0=普通模式 1=海外仓中转模式 不传默认取系统当前设置模式, int."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature",
            {k: v for k, v in {"sid": sid, "msku": msku, "sug_type": sug_type, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugMskuGetdailysalesinfofeatureResponse)

    async def get_summary_list(
        self,
        sid_list: list = None,
        data_type: int = None,
        asin_list: list = None,
        msku_list: list = None,
        mode: int = None,
        listing_date_range: list = None,
        offset: int = None,
        length: int = None,
    ) -> list[RestockingAnalysisGetsummarylistResponse]:
        """查询补货列表.

        POST /erp/sc/routing/restocking/analysis/getSummaryList

        Args:
            sid_list: 店铺id, array.
            data_type: 查询维度：1 asin，2 msku (required), int.
            asin_list: 按传入的asin列表筛选数据, array.
            msku_list: 按传入的msku列表筛选数据, array.
            mode: 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式（在补货建议列表可切换）】, int.
            listing_date_range: listing创建时间范围筛选：[开始日期，结束日期]，必须同时包含两个日期才生效, array.
            offset: 分页偏移量，默认0, int.
            length: 分页条数，默认20，上限50, int."""
        resp = await self._post(
            "/erp/sc/routing/restocking/analysis/getSummaryList",
            {
                k: v
                for k, v in {
                    "sid_list": sid_list,
                    "data_type": data_type,
                    "asin_list": asin_list,
                    "msku_list": msku_list,
                    "mode": mode,
                    "listing_date_range": listing_date_range,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, RestockingAnalysisGetsummarylistResponse)

    async def info_asin(self, sid: int = None, asin: str = None, mode: int = None) -> FbasugAsinGetinfoResponse | None:
        """查询建议信息-ASIN.

        POST /erp/sc/routing/fbaSug/asin/getInfo

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin: ASIN (required), string.
            mode: 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式】, int."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/getInfo",
            {k: v for k, v in {"sid": sid, "asin": asin, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugAsinGetinfoResponse)

    async def info_msku(self, sid: int = None, msku: str = None, mode: int = None) -> FbasugMskuGetinfoResponse | None:
        """查询建议信息-MSKU.

        POST /erp/sc/routing/fbaSug/msku/getInfo

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            msku: MSKU (required), string.
            mode: 补货建议模式： 0 普通模式 1 海外仓中转模式 【不传默认取erp当前设置模式】, int."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/getInfo",
            {k: v for k, v in {"sid": sid, "msku": msku, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugMskuGetinfoResponse)

    async def set_config_asin(
        self,
        sid: int = None,
        asin: str = None,
        days_plan: str = None,
        days_qc: str = None,
        days_oversea_to_fba: float = None,
        days_frequency_purchase: float = None,
        days_frequency_local_send: float = None,
        days_frequency_oversea_send: float = None,
        safe_day: float = None,
        is_ignore_certainly_short: float = None,
        is_ignore_history_out_stock: float = None,
        days_toucheng: float = None,
        days_oversea: float = None,
        days_toucheng_air: float = None,
        days_oversea_air: float = None,
        default_type_toucheng: float = None,
        default_type_oversea: float = None,
        days_frequency: float = None,
        sm_fba_list: list = None,
        sm_oversea_list: list = None,
        config_list: list = None,
        denoise_list: list = None,
    ) -> FbasugAsinGetconfigResponse | None:
        """单个设置规则-ASIN.

        POST /erp/sc/routing/fbaSug/asin/setConfig

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin: ASIN (required), string.
            days_plan: 采购计划时长 (required), string.
            days_qc: 质检时长 (required), string.
            sm_fba_list: 本地仓至FBA时效 (required), array.
            sm_oversea_list: 本地仓至海外仓时效 (required), array.
            days_oversea_to_fba: 海外仓至FBA天数 (required), number.
            days_frequency_purchase: 采购频率 (required), number.
            days_frequency_local_send: 本地仓发货频率 (required), number.
            days_frequency_oversea_send: 海外仓发货频率 (required), number.
            safe_day: 安全天数 (required), number.
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (required), number.
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (required), number.
            days_toucheng: 已弃用（原本地至FBA天数-海运）, number.
            days_oversea: 已弃用（原本地至海外仓天数-海运）, number.
            days_toucheng_air: 已弃用（原本地至FBA时效-空运）, number.
            days_oversea_air: 已弃用（原本地至海外仓时效-空运）, number.
            default_type_toucheng: 已弃用（原默认头程物流类型）, number.
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型）, number.
            days_frequency: 已弃用（原补货频率）, number.
            config_list: 日销量设置 (required), array.
            denoise_list: 日销量去噪设置 (required), array."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/setConfig",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "asin": asin,
                    "days_plan": days_plan,
                    "days_qc": days_qc,
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
                    "sm_fba_list": sm_fba_list,
                    "sm_oversea_list": sm_oversea_list,
                    "config_list": config_list,
                    "denoise_list": denoise_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, FbasugAsinGetconfigResponse)

    async def set_config_msku(
        self,
        sid: int = None,
        msku: str = None,
        days_plan: str = None,
        days_qc: str = None,
        days_oversea_to_fba: float = None,
        days_frequency_purchase: float = None,
        days_frequency_local_send: float = None,
        days_frequency_oversea_send: float = None,
        safe_day: float = None,
        is_ignore_certainly_short: float = None,
        is_ignore_history_out_stock: float = None,
        days_toucheng: float = None,
        days_oversea: float = None,
        days_toucheng_air: float = None,
        days_oversea_air: float = None,
        default_type_toucheng: float = None,
        default_type_oversea: float = None,
        days_frequency: float = None,
        sm_fba_list: list = None,
        sm_oversea_list: list = None,
        config_list: list = None,
        denoise_list: list = None,
    ) -> FbasugMskuGetconfigResponse | None:
        """单个设置规则-MSKU.

        POST /erp/sc/routing/fbaSug/msku/setConfig

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            msku: MSKU (required), string.
            days_plan: 采购计划时长 (required), string.
            days_qc: 质检时长 (required), string.
            sm_fba_list: 本地仓至FBA时效 (required), array.
            sm_oversea_list: 本地仓至海外仓时效 (required), array.
            days_oversea_to_fba: 海外仓至FBA天数 (required), number.
            days_frequency_purchase: 采购频率 (required), number.
            days_frequency_local_send: 本地仓发货频率 (required), number.
            days_frequency_oversea_send: 海外仓发货频率 (required), number.
            safe_day: 安全天数 (required), number.
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (required), number.
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (required), number.
            days_toucheng: 已弃用（原本地至FBA天数-海运）, number.
            days_oversea: 已弃用（原本地至海外仓天数-海运）, number.
            days_toucheng_air: 已弃用（原本地至FBA时效-空运）, number.
            days_oversea_air: 已弃用（原本地至海外仓时效-空运）, number.
            default_type_toucheng: 已弃用（原默认头程物流类型）, number.
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型）, number.
            days_frequency: 已弃用（原补货频率）, number.
            config_list: 日销量设置 (required), array.
            denoise_list: 日销量去噪设置 (required), array."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/setConfig",
            {
                k: v
                for k, v in {
                    "sid": sid,
                    "msku": msku,
                    "days_plan": days_plan,
                    "days_qc": days_qc,
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
                    "sm_fba_list": sm_fba_list,
                    "sm_oversea_list": sm_oversea_list,
                    "config_list": config_list,
                    "denoise_list": denoise_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, FbasugMskuGetconfigResponse)

    async def set_configs_asin(
        self,
        days_plan: str = None,
        days_qc: str = None,
        days_oversea_to_fba: float = None,
        days_frequency_purchase: float = None,
        days_frequency_local_send: float = None,
        days_frequency_oversea_send: float = None,
        safe_day: float = None,
        is_ignore_certainly_short: float = None,
        is_ignore_history_out_stock: float = None,
        days_toucheng: float = None,
        days_oversea: float = None,
        days_toucheng_air: float = None,
        days_oversea_air: float = None,
        default_type_toucheng: float = None,
        default_type_oversea: float = None,
        days_frequency: float = None,
        asin_list: list = None,
        sm_fba_list: list = None,
        sm_oversea_list: list = None,
        config_list: list = None,
        denoise_list: list = None,
    ) -> FbasugAsinSetconfigsResponse | None:
        """批量设置规则 - ASIN.

        POST /erp/sc/routing/fbaSug/asin/setConfigs

        Args:
            asin_list: asin信息 (required), array.
            days_plan: 采购计划时长 (required), string.
            days_qc: 质检时长 (required), string.
            sm_fba_list: 本地仓至FBA时效 (required), array.
            sm_oversea_list: 本地仓至海外仓时效 (required), array.
            days_oversea_to_fba: 海外仓至FBA天数 (required), number.
            days_frequency_purchase: 采购频率 (required), number.
            days_frequency_local_send: 本地仓发货频率 (required), number.
            days_frequency_oversea_send: 海外仓发货频率 (required), number.
            safe_day: 安全天数 (required), number.
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (required), number.
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (required), number.
            days_toucheng: 已弃用（原本地至FBA天数-海运）, number.
            days_oversea: 已弃用（原本地至海外仓天数-海运）, number.
            days_toucheng_air: 已弃用（原本地至FBA时效-空运）, number.
            days_oversea_air: 已弃用（原本地至海外仓时效-空运）, number.
            default_type_toucheng: 已弃用（原默认头程物流类型）, number.
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型 ）, number.
            days_frequency: 已弃用（原补货频率）, number.
            config_list: 日销量设置 (required), array.
            denoise_list: 日销量去噪设置, array."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/setConfigs",
            {
                k: v
                for k, v in {
                    "days_plan": days_plan,
                    "days_qc": days_qc,
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
                    "asin_list": asin_list,
                    "sm_fba_list": sm_fba_list,
                    "sm_oversea_list": sm_oversea_list,
                    "config_list": config_list,
                    "denoise_list": denoise_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, FbasugAsinSetconfigsResponse)

    async def set_configs_msku(
        self,
        days_plan: str = None,
        days_qc: str = None,
        days_oversea_to_fba: float = None,
        days_frequency_purchase: float = None,
        days_frequency_local_send: float = None,
        days_frequency_oversea_send: float = None,
        safe_day: float = None,
        is_ignore_certainly_short: float = None,
        is_ignore_history_out_stock: float = None,
        days_toucheng: float = None,
        days_oversea: float = None,
        days_toucheng_air: float = None,
        days_oversea_air: float = None,
        default_type_toucheng: float = None,
        default_type_oversea: float = None,
        days_frequency: float = None,
        msku_list: list = None,
        sm_fba_list: list = None,
        sm_oversea_list: list = None,
        config_list: list = None,
        denoise_list: list = None,
    ) -> FbasugMskuSetconfigsResponse | None:
        """批量设置规则 - MSKU.

        POST /erp/sc/routing/fbaSug/msku/setConfigs

        Args:
            msku_list: msku信息 (required), array.
            days_plan: 采购计划时长 (required), string.
            days_qc: 质检时长 (required), string.
            sm_fba_list: 本地仓至FBA时效 (required), array.
            sm_oversea_list: 本地仓至海外仓时效 (required), array.
            days_oversea_to_fba: 海外仓至FBA天数 (required), number.
            days_frequency_purchase: 采购频率 (required), number.
            days_frequency_local_send: 本地仓发货频率 (required), number.
            days_frequency_oversea_send: 海外仓发货频率 (required), number.
            safe_day: 安全天数 (required), number.
            is_ignore_certainly_short: 建议量扣除必断货量：0 否，1 是 (required), number.
            is_ignore_history_out_stock: 历史销量排除断货数据：0 否，1 是 (required), number.
            days_toucheng: 已弃用（原本地至FBA天数-海运）, number.
            days_oversea: 已弃用（原本地至海外仓天数-海运）, number.
            days_toucheng_air: 已弃用（原本地至FBA时效-空运）, number.
            days_oversea_air: 已弃用（原本地至海外仓时效-空运）, number.
            default_type_toucheng: 已弃用（原默认头程物流类型）, number.
            default_type_oversea: 已弃用（原默认本地发海外仓物流类型 ）, number.
            days_frequency: 已弃用（原补货频率）, number.
            config_list: 日销量设置 (required), array.
            denoise_list: 日销量去噪设置 (required), array."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/setConfigs",
            {
                k: v
                for k, v in {
                    "days_plan": days_plan,
                    "days_qc": days_qc,
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
                    "msku_list": msku_list,
                    "sm_fba_list": sm_fba_list,
                    "sm_oversea_list": sm_oversea_list,
                    "config_list": config_list,
                    "denoise_list": denoise_list,
                }.items()
                if v is not None
            },
        )
        return self._parse_one(resp.data, FbasugMskuSetconfigsResponse)

    async def source_list_asin(
        self, sid: int = None, asin: str = None, type: str = None, mode: str = None
    ) -> FbasugAsinGetsourcelistResponse | None:
        """查询报表型数据明细-ASIN.

        POST /erp/sc/routing/fbaSug/asin/getSourceList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            asin: ASIN (required), string.
            type: 数据类型：【默认1】 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途, string.
            mode: 补货建议模式： 0 普通模式 1 海外仓中转模式 不传默认取erp当前设置模式（在补货建议列表可切换）, string."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/asin/getSourceList",
            {k: v for k, v in {"sid": sid, "asin": asin, "type": type, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugAsinGetsourcelistResponse)

    async def source_list_msku(
        self, sid: int = None, msku: str = None, type: str = None, mode: str = None
    ) -> FbasugMskuGetsourcelistResponse | None:
        """查询报表型数据明细-MSKU.

        POST /erp/sc/routing/fbaSug/msku/getSourceList

        Args:
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
            msku: MSKU (required), string.
            type: 数据类型：【默认1】 1 FBA可售 2 FBA在途 3 本地可用 4 待检量 5 待交付 6 采购计划 8 海外仓可用 9 海外仓在途, string.
            mode: 补货建议模式： 0 普通模式 1 海外仓中转模式 不传默认取erp当前设置模式（在补货建议列表可切换）, string."""
        resp = await self._post(
            "/erp/sc/routing/fbaSug/msku/getSourceList",
            {k: v for k, v in {"sid": sid, "msku": msku, "type": type, "mode": mode}.items() if v is not None},
        )
        return self._parse_one(resp.data, FbasugMskuGetsourcelistResponse)

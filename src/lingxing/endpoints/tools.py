"""工具 API endpoints."""

from __future__ import annotations

from ..models.responses.tools import (
    SettingsWarningmessageGoodslistResponse,
    SettingsWarningmessageInventorylistResponse,
    ToolCompetitivemonitorListResponse,
    ToolToolkeywordrankGetkeywordlistResponse,
)
from ._base import BaseEndpoint


class ToolsEndpoints(BaseEndpoint):
    """领星工具 API (5个接口)."""

    async def competitive_monitor_list(
        self,
        levels: list = None,
        update_time_start: str = None,
        update_time_end: str = None,
        search_field: str = None,
        search_value: str = None,
        offset: int = None,
        length: int = None,
    ) -> list[ToolCompetitivemonitorListResponse]:
        """查询竞品监控列表.

        POST /basicOpen/tool/competitiveMonitor/list

        Args:
            levels: 竞品等级： 1 A 2 B 3 C 4 D, array.
            update_time_start: 开始时间【更新时间】，闭区间，格式：Y-m-d, string.
            update_time_end: 结束时间【更新时间】，闭区间，格式：Y-m-d, string.
            search_field: 搜索字段：asin ASIN, string.
            search_value: 搜索值：多个使用英文逗号分隔，上限200, string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int."""
        resp = await self._post(
            "/basicOpen/tool/competitiveMonitor/list",
            {
                k: v
                for k, v in {
                    "levels": levels,
                    "update_time_start": update_time_start,
                    "update_time_end": update_time_end,
                    "search_field": search_field,
                    "search_value": search_value,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ToolCompetitivemonitorListResponse)

    async def get_keyword_list(
        self, mid: int = None, start_date: str = None, end_date: str = None, offset: int = None, length: int = None
    ) -> list[ToolToolkeywordrankGetkeywordlistResponse]:
        """关键词列表.

        POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList

        Args:
            mid: 国家id, int.
            start_date: 开始日期，格式：Y-m-d, string.
            end_date: 结束日期，格式：Y-m-d, string.
            offset: 分页偏移量，默认0 (required), int.
            length: 分页长度，默认20，最大值为2000 (required), int."""
        resp = await self._post(
            "/erp/sc/routing/tool/toolKeywordRank/getKeywordList",
            {
                k: v
                for k, v in {
                    "mid": mid,
                    "start_date": start_date,
                    "end_date": end_date,
                    "offset": offset,
                    "length": length,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ToolToolkeywordrankGetkeywordlistResponse)

    async def query_erp_keyword_ranking_asin(
        self, asin: str, mid: int = None, start_date: str = None, end_date: str = None, length: int = 2000
    ) -> list[ToolToolkeywordrankGetkeywordlistResponse]:
        """查询指定 ASIN 的关键词排名.

        领星关键词排名接口（/erp/sc/routing/tool/toolKeywordRank/getKeywordList）返回全量监控数据，
        本方法在其基础上按 asin 过滤，返回该 ASIN 的关键词排名（关键词/排名/页码/PC或移动/广告或自然）。

        Args:
            asin: 要查询的 ASIN (required), string.
            mid: 国家id, int.
            start_date: 开始日期 Y-m-d, string.
            end_date: 结束日期 Y-m-d, string.
            length: 拉取条数，默认2000（越大覆盖越全，最大2000）, int."""
        rows = await self.get_keyword_list(mid=mid, start_date=start_date, end_date=end_date, offset=0, length=length)
        return [
            r
            for r in rows
            if (r.asin if hasattr(r, "asin") else (r.get("asin") if isinstance(r, dict) else None)) == asin
        ]

    async def warning_message_goods_list(
        self,
        offset: int = None,
        length: int = None,
        model_id_list: list = None,
        sids: list = None,
        start_date: str = None,
        end_date: str = None,
        search_field: str = None,
        search_value: str = None,
        show_status: int = None,
    ) -> list[SettingsWarningmessageGoodslistResponse]:
        """查询预警消息列表-商品.

        POST /basicOpen/settings/warningMessage/goodsList

        Args:
            offset: 分页偏移量, int.
            length: 分页长度，默认50，上限200, int.
            model_id_list: 预警模型： 1  Listing调价预警 2  FBA费变更预警 3  Listing下架预警 6  FBA费异常预警 7  折扣异常预警 18  业务指标预警 20  折扣叠加预警 21  buybox丢失预警 26  父ASIN变更预警, array.
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
            start_date: 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            end_date: 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            search_field: 搜索类型： rule_name   规则名称 asin  ASIN msku  MSKU, string.
            search_value: 搜索值, string.
            show_status: 处理状态： 0  待处理 1  全部 (required), int."""
        resp = await self._post(
            "/basicOpen/settings/warningMessage/goodsList",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "model_id_list": model_id_list,
                    "sids": sids,
                    "start_date": start_date,
                    "end_date": end_date,
                    "search_field": search_field,
                    "search_value": search_value,
                    "show_status": show_status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SettingsWarningmessageGoodslistResponse)

    async def warning_message_inventory_list(
        self,
        offset: int = None,
        length: int = None,
        model_id_list: list = None,
        product_type_list: list = None,
        start_date: str = None,
        end_date: str = None,
        show_status: int = None,
    ) -> list[SettingsWarningmessageInventorylistResponse]:
        """查询预警消息列表-库存.

        POST /basicOpen/settings/warningMessage/inventoryList

        Args:
            offset: 分页偏移量, int.
            length: 分页长度，默认50，上限200, int.
            model_id_list: 预警模型：  4  本地库存预警 5  亚马逊库存预警 22  本地库龄预警 23  亚马逊库龄预警, array.
            product_type_list: 产品类型： 2  MSKU 3   SKU+仓库+店铺+FNSKU, array.
            start_date: 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            end_date: 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
            show_status: 处理状态： 0   待处理  1    全部 (required), int."""
        resp = await self._post(
            "/basicOpen/settings/warningMessage/inventoryList",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "model_id_list": model_id_list,
                    "product_type_list": product_type_list,
                    "start_date": start_date,
                    "end_date": end_date,
                    "show_status": show_status,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, SettingsWarningmessageInventorylistResponse)

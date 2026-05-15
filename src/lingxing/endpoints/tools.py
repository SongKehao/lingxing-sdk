"""工具 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint


class ToolsEndpoints(BaseEndpoint):
    """领星工具 API (4个接口)."""

    async def competitive_monitor_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/tool/competitiveMonitor/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_keyword_list(self, **kwargs) -> list | dict:
        """关键词列表.

POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList

Args:
    mid: 国家id, int.
    start_date: 开始日期，格式：Y-m-d, string.
    end_date: 结束日期，格式：Y-m-d, string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20，最大值为2000 (required), int."""
        resp = await self._post("/erp/sc/routing/tool/toolKeywordRank/getKeywordList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warning_message_goods_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/settings/warningMessage/goodsList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def warning_message_inventory_list(self, **kwargs) -> list | dict:
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
        resp = await self._post("/basicOpen/settings/warningMessage/inventoryList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

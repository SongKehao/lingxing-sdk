"""新版广告 API endpoints."""
from __future__ import annotations

from typing import Any

from ._base import BaseEndpoint


class NewAdEndpoints(BaseEndpoint):
    """领星新版广告 API (4个接口)."""

    async def dsp_account_list(self, offset: int = None, length: int = None, type: str = None) -> list | dict:
        """查询广告账号列表.

POST /basicOpen/baseData/account/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    type: 类型：  dsp   seller   vendor (required), string."""
        resp = await self._post("/basicOpen/baseData/account/list", {k: v for k, v in {"offset": offset, "length": length, "type": type}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_analysis_list(self, sid: str = None, profile_id: int = None, sku: Any = None, start_date: str = None, end_date: str = None, group_type: str = None, sponsored_type: list = None) -> list | dict:
        """出单时段分析（产品）.

POST /basicOpen/adReport/productOrderAnalysis/list

Args:
    sid: sid (required), string.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (required), int.
    sku: msku最多10个 (required), array.
    start_date: 开始日期，格式：Y-m-d (required), string.
    end_date: 结束日期，格式：Y-m-d (required), string.
    group_type: 时间维度 hourly 按小时 weekly 按周 (required), string.
    sponsored_type: 广告类型  sp   sd, array."""
        resp = await self._post("/basicOpen/adReport/productOrderAnalysis/list", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "sku": sku, "start_date": start_date, "end_date": end_date, "group_type": group_type, "sponsored_type": sponsored_type}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_query_advertiser_list(self, searchText: str = None, paging: str = None, limit: int = None, page: int = None) -> list | dict:
        """查询沃尔玛广告主列表.

POST /basicOpen/adReport/advertiser/list

Args:
    searchText: 广告主名称模糊搜索, string.
    paging: 不分页传false  分页传true (required), string.
    limit: 分页条数, int.
    page: 页码, int."""
        resp = await self._post("/basicOpen/adReport/advertiser/list", {k: v for k, v in {"searchText": searchText, "paging": paging, "limit": limit, "page": page}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def dsp_report_order_list(self, offset: int = None, length: int = None, profile_id: str = None, start_date: str = None, end_date: str = None) -> list | dict:
        """查询DSP报告列表-订单.

POST /basicOpen/dspReport/order/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    profile_id: 亚马逊店铺数字id，查询广告账号列表接口对应字段【profile_id】 (required), string.
    start_date: 报告开始日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
    end_date: 报告结束日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string."""
        resp = await self._post("/basicOpen/dspReport/order/list", {k: v for k, v in {"offset": offset, "length": length, "profile_id": profile_id, "start_date": start_date, "end_date": end_date}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

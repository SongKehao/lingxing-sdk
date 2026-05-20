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


    async def spcampaignreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP广告活动报表.

POST /pb/openapi/newad/spCampaignReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spCampaignReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def campaignplacementreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP广告位报告.

POST /pb/openapi/newad/spCampaignPlacementReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spCampaignPlacementReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spadgroupreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP广告组报表.

POST /pb/openapi/newad/spAdGroupReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spAdGroupReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spproductadreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP广告商品报表.

POST /pb/openapi/newad/spProductAdReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spProductAdReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spkeywordreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP关键词报表.

POST /pb/openapi/newad/spKeywordReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spKeywordReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sptargetreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP商品定位报表.

POST /pb/openapi/newad/spTargetReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spTargetReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def asinreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP已购买商品报表.

POST /pb/openapi/newad/spAsinReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】，sid跟profile_id其中一个必填, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spAsinReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def querywordreports(self, sid: int, profile_id: int, report_date: str, target_type: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SP用户搜索词报表.

POST /pb/openapi/newad/spQueryWordReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期, str.
    target_type: 投放类型【默认 keyword】： keyword 关键词 target 商品投放, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页条数，默认15, int."""
        resp = await self._post("/pb/openapi/newad/spQueryWordReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "target_type": target_type, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsacampaignreports(self, sid: int, profile_id: int, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB广告活动报表.

POST /pb/openapi/newad/hsaCampaignReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaCampaignReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsacampaignplacementreports(self, sid: int, profile_id: int, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB广告活动-广告位报告.

POST /pb/openapi/newad/hsaCampaignPlacementReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaCampaignPlacementReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsaadgroupreports(self, sid: int, profile_id: int, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB广告组报表.

POST /pb/openapi/newad/hsaAdGroupReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaAdGroupReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def listhsatargetingreport(self, sid: int, profile_id: int, sponsored_type: str, target_type: str, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB广告的投放报告.

POST /pb/openapi/newad/listHsaTargetingReport

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    sponsored_type: 广告类型： ALL, str.
    target_type: 投放类型： keyword producttarget ALL, str.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认10, int."""
        resp = await self._post("/pb/openapi/newad/listHsaTargetingReport", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "sponsored_type": sponsored_type, "target_type": target_type, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsaquerywordreports(self, sid: int, profile_id: int, report_date: str, target_type: str, offset: int = None, length: int = None) -> list | dict:
        """SB用户搜索词报表.

POST /pb/openapi/newad/hsaQueryWordReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期, str.
    target_type: 投放类型【默认 keyword】：keyword 关键词, str.
    offset: 分页偏移量，默认0, int.
    length: 分页条数，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaQueryWordReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "target_type": target_type, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsapurchasedasinreports(self, sid: int, profile_id: int, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB广告归因于广告的购买报告.

POST /pb/openapi/newad/hsaPurchasedAsinReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaPurchasedAsinReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def listhsakeywordplacementreport(self, sid: int, profile_id: int, sponsored_type: str, target_type: str, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SB关键词-广告位报告.

POST /pb/openapi/newad/listHsaKeywordPlacementReport

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    sponsored_type: 广告类型： ALL, str.
    target_type: 投放类型： keyword, str.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/listHsaKeywordPlacementReport", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "sponsored_type": sponsored_type, "target_type": target_type, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdcampaignreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SD广告活动报表.

POST /pb/openapi/newad/sdCampaignReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdCampaignReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdadgroupreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SD广告组报表.

POST /pb/openapi/newad/sdAdGroupReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdAdGroupReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdproductadreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SD广告商品报表.

POST /pb/openapi/newad/sdProductAdReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdProductAdReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdtargetreports(self, sid: int, profile_id: int, report_date: str, offset: int = None, length: int = None) -> list | dict:
        """SD商品定位报表.

POST /pb/openapi/newad/sdTargetReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdTargetReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdasinreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SD已购买商品报表.

POST /pb/openapi/newad/sdAsinReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdAsinReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdmatchtargetreports(self, sid: int, profile_id: int, report_date: str, show_detail: int = None, offset: int = None, length: int = None) -> list | dict:
        """SD匹配的目标报表.

POST /pb/openapi/newad/sdMatchTargetReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页条数，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdMatchTargetReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spcampaignhourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SP广告活动小时数据.

POST /pb/openapi/newad/spCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/spCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spadgrouphourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SP广告组小时数据.

POST /pb/openapi/newad/spAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/spAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spadvertisehourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list | dict:
        """SP广告小时数据.

POST /pb/openapi/newad/spAdvertiseHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度:  ad  广告维度  both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/spAdvertiseHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sptargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list | dict:
        """SP投放小时数据.

POST /pb/openapi/newad/spTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: target  投放维度 both_ad_target  广告+投放维度   both_target_placement 投放+广告位placement维度, str."""
        resp = await self._post("/pb/openapi/newad/spTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbcampaignhourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SB广告活动小时数据.

POST /pb/openapi/newad/sbCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbadgrouphourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SB广告组小时数据.

POST /pb/openapi/newad/sbAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbtargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list | dict:
        """SB投放小时数据.

POST /pb/openapi/newad/sbTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度： target  投放, str."""
        resp = await self._post("/pb/openapi/newad/sbTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbadplacementhourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SB广告位小时数据.

POST /pb/openapi/newad/sbAdPlacementHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbAdPlacementHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdcampaignhourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SD广告活动小时数据.

POST /pb/openapi/newad/sdCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sdCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdadgrouphourdata(self, report_date: str, campaign_id: float) -> list | dict:
        """SD广告组小时数据.

POST /pb/openapi/newad/sdAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sdAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdadvertisehourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list | dict:
        """SD广告小时数据.

POST /pb/openapi/newad/sdAdvertiseHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: ad  广告维度 both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/sdAdvertiseHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdtargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list | dict:
        """SD投放小时数据.

POST /pb/openapi/newad/sdTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: target  投放维度 both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/sdTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbdivideasinreports(self, profile_id: int, report_date: str, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB分摊.

POST /pb/openapi/newad/sbDivideAsinReports

Args:
    profile_id: 店铺profile_id, int.
    report_date: 报告日期, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token和offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sbDivideAsinReports", {k: v for k, v in {"profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def portfolios(self, sid: int, profile_id: int, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """广告组合.

POST /pb/openapi/newad/portfolios

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/portfolios", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spcampaigns(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP广告活动.

POST /pb/openapi/newad/spCampaigns

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spCampaigns", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spadgroups(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP广告组.

POST /pb/openapi/newad/spAdGroups

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spAdGroups", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spproductads(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP广告商品.

POST /pb/openapi/newad/spProductAds

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spProductAds", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spkeywords(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP关键词.

POST /pb/openapi/newad/spKeywords

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spKeywords", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sptargets(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP商品定位.

POST /pb/openapi/newad/spTargets

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spTargets", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def spnegativetargetsorkeywords(self, sid: int, profile_id: int, target_type: str, campaign_id: float = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SP否定投放.

POST /pb/openapi/newad/spNegativeTargetsOrKeywords

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    target_type: 投放类型：keyword target, str.
    campaign_id: 广告活动id, float.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/spNegativeTargetsOrKeywords", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "target_type": target_type, "campaign_id": campaign_id, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsacampaigns(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB广告活动.

POST /pb/openapi/newad/hsaCampaigns

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/hsaCampaigns", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsaadgroups(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB广告组.

POST /pb/openapi/newad/hsaAdGroups

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态:状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/hsaAdGroups", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sbtargeting(self, sid: int, profile_id: int, ads_type: str, targeting_type: str, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB广告的投放.

POST /pb/openapi/newad/sbTargeting

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    ads_type: 广告类型： SB 返回SB广告数据 SBV 返回SBV广告数据 ALL 同时返回SB和SBV广告数据, str.
    targeting_type: 投放类型： keyword 返回关键词数据 producttarget 返回商品定位数据 ALL：同时返回关键词和商品定位数据, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sbTargeting", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "ads_type": ads_type, "targeting_type": targeting_type, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsanegativekeywords(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB否定关键词.

POST /pb/openapi/newad/hsaNegativeKeywords

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/hsaNegativeKeywords", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def hsanegativetargets(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SB否定商品投放.

POST /pb/openapi/newad/hsaNegativeTargets

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/hsaNegativeTargets", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdcampaigns(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SD广告活动.

POST /pb/openapi/newad/sdCampaigns

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sdCampaigns", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdadgroups(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SD广告组.

POST /pb/openapi/newad/sdAdGroups

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sdAdGroups", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdproductads(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SD广告商品.

POST /pb/openapi/newad/sdProductAds

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sdProductAds", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdtargets(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SD商品定位.

POST /pb/openapi/newad/sdTargets

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sdTargets", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def sdnegativetargets(self, sid: int, profile_id: int, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list | dict:
        """SD否定商品定位.

POST /pb/openapi/newad/sdNegativeTargets

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    state: 状态：【不传默认为所有】 enabled paused archived, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sdNegativeTargets", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "state": state, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def download_abareport(self, country: str, data_start_time: str) -> list | dict:
        """ABA搜索词报告-按周维度.

POST /pb/openapi/newad/abaReport

Args:
    country: 国家代码：如US, str.
    data_start_time: 报表开始日期：每周周日的日期，仅支持最近45天, str."""
        resp = await self._post("/pb/openapi/newad/abaReport", {k: v for k, v in {"country": country, "data_start_time": data_start_time}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

    async def apilogstandard(self, sid: int, log_source: str, sponsored_type: str, operate_type: str, start_date: str, end_date: str, offset: int = None, length: int = None) -> list | dict:
        """操作日志（新）.

POST /pb/openapi/newad/apiLogStandard

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    log_source: 日志来源： all 包括ERP和亚马逊后台的操作 erp 仅ERP中调整广告的日志 amazon 亚马逊后台的日志, str.
    sponsored_type: 广告类型： sp 返回sp操作日志 sb 返回sb操作日志 sd 返回sd操作日志, str.
    operate_type: 对象类型: campaigns 广告活动 adGroups 广告组 productAds 广告 keywords 关键词 negativeKeywords 否定关键词 targets 商品投放 neg, str.
    start_date: 起始时间，格式：Y-m-d【日期间隔不能超过一个月】, str.
    end_date: 结束时间，格式：Y-m-d【日期间隔不能超过一个月】, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/apiLogStandard", {k: v for k, v in {"sid": sid, "log_source": log_source, "sponsored_type": sponsored_type, "operate_type": operate_type, "start_date": start_date, "end_date": end_date, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

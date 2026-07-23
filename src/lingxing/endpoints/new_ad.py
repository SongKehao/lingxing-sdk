"""新版广告 API endpoints."""
from __future__ import annotations

from ..models.responses.new_ad import (
    AdReportAdvertiserListResponse,
    AdreportAdvertiserListResponse,
    AdreportProductorderanalysisListResponse,
    BasedataAccountListResponse,
    DspreportOrderListResponse,
    OpenapiNewadAbareportResponse,
    OpenapiNewadApilogstandardResponse,
    OpenapiNewadHsaadgroupreportsResponse,
    OpenapiNewadHsaadgroupsResponse,
    OpenapiNewadHsacampaignplacementreportsResponse,
    OpenapiNewadHsacampaignreportsResponse,
    OpenapiNewadHsacampaignsResponse,
    OpenapiNewadHsanegativekeywordsResponse,
    OpenapiNewadHsanegativetargetsResponse,
    OpenapiNewadHsapurchasedasinreportsResponse,
    OpenapiNewadHsaquerywordreportsResponse,
    OpenapiNewadListhsakeywordplacementreportResponse,
    OpenapiNewadListhsatargetingreportResponse,
    OpenapiNewadPortfoliosResponse,
    OpenapiNewadQuerywordreportsResponse,
    OpenapiNewadSbadgrouphourdataResponse,
    OpenapiNewadSbadplacementhourdataResponse,
    OpenapiNewadSbcampaignhourdataResponse,
    OpenapiNewadSbdivideasinreportsResponse,
    OpenapiNewadSbtargethourdataResponse,
    OpenapiNewadSbtargetingResponse,
    OpenapiNewadSdasinreportsResponse,
    OpenapiNewadSdadgrouphourdataResponse,
    OpenapiNewadSdadgroupreportsResponse,
    OpenapiNewadSdadgroupsResponse,
    OpenapiNewadSdadvertisehourdataResponse,
    OpenapiNewadSdcampaignhourdataResponse,
    OpenapiNewadSdcampaignreportsResponse,
    OpenapiNewadSdcampaignsResponse,
    OpenapiNewadSdmatchtargetreportsResponse,
    OpenapiNewadSdnegativetargetsResponse,
    OpenapiNewadSdproductadreportsResponse,
    OpenapiNewadSdproductadsResponse,
    OpenapiNewadSdtargethourdataResponse,
    OpenapiNewadSdtargetreportsResponse,
    OpenapiNewadSdtargetsResponse,
    OpenapiNewadSpadgrouphourdataResponse,
    OpenapiNewadSpadgroupreportsResponse,
    OpenapiNewadSpadgroupsResponse,
    OpenapiNewadSpadvertisehourdataResponse,
    OpenapiNewadSpcampaignhourdataResponse,
    OpenapiNewadSpcampaignplacementreportsResponse,
    OpenapiNewadSpcampaignreportsResponse,
    OpenapiNewadSpcampaignsResponse,
    OpenapiNewadSpasinreportsResponse,
    OpenapiNewadSpkeywordreportsResponse,
    OpenapiNewadSpkeywordsResponse,
    OpenapiNewadSpnegativetargetsorkeywordsResponse,
    OpenapiNewadSpproductadreportsResponse,
    OpenapiNewadSpproductadsResponse,
    OpenapiNewadSptargethourdataResponse,
    OpenapiNewadSptargetreportsResponse,
    OpenapiNewadSptargetsResponse,
)

from typing import Any

from ._base import BaseEndpoint


class NewAdEndpoints(BaseEndpoint):
    """领星新版广告 API (4个接口)."""

    async def walmart_advertiser_list(self, search_text: str = None, page: int = None, limit: int = None) -> list[AdReportAdvertiserListResponse]:
        """查询沃尔玛-广告-广告主列表.

POST /basicOpen/adReport/advertiser/list

Args:
    search_text: see API doc.
    page: see API doc.
    limit: see API doc."""
        resp = await self._post("/basicOpen/adReport/advertiser/list", {k: v for k, v in {"searchText": search_text, "page": page, "limit": limit}.items() if v is not None})
        return self._parse_list(resp.data, AdReportAdvertiserListResponse)

    async def dsp_account_list(self, offset: int = None, length: int = None, type: str = None) -> list[BasedataAccountListResponse]:
        """查询广告账号列表.

POST /basicOpen/baseData/account/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    type: 类型：  dsp   seller   vendor (required), string."""
        resp = await self._post("/basicOpen/baseData/account/list", {k: v for k, v in {"offset": offset, "length": length, "type": type}.items() if v is not None})
        return self._parse_list(resp.data, BasedataAccountListResponse)
    async def product_analysis_list(self, profile_id: int = None, sid: str = None, sku: Any = None, start_date: str = None, end_date: str = None, group_type: str = None, sponsored_type: list = None) -> list[AdreportProductorderanalysisListResponse]:
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
        return self._parse_list(resp.data, AdreportProductorderanalysisListResponse)
    async def walmart_query_advertiser_list(self, searchText: str = None, paging: str = None, limit: int = None, page: int = None) -> list[AdreportAdvertiserListResponse]:
        """查询沃尔玛广告主列表.

POST /basicOpen/adReport/advertiser/list

Args:
    searchText: 广告主名称模糊搜索, string.
    paging: 不分页传false  分页传true (required), string.
    limit: 分页条数, int.
    page: 页码, int."""
        resp = await self._post("/basicOpen/adReport/advertiser/list", {k: v for k, v in {"searchText": searchText, "paging": paging, "limit": limit, "page": page}.items() if v is not None})
        return self._parse_list(resp.data, AdreportAdvertiserListResponse)
    async def dsp_report_order_list(self, offset: int = None, length: int = None, profile_id: str = None, start_date: str = None, end_date: str = None) -> list[DspreportOrderListResponse]:
        """查询DSP报告列表-订单.

POST /basicOpen/dspReport/order/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    profile_id: 亚马逊店铺数字id，查询广告账号列表接口对应字段【profile_id】 (required), string.
    start_date: 报告开始日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string.
    end_date: 报告结束日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (required), string."""
        resp = await self._post("/basicOpen/dspReport/order/list", {k: v for k, v in {"offset": offset, "length": length, "profile_id": profile_id, "start_date": start_date, "end_date": end_date}.items() if v is not None})
        return self._parse_list(resp.data, DspreportOrderListResponse)


    async def spcampaignreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpcampaignreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpcampaignreportsResponse)

    async def campaignplacementreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpcampaignplacementreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpcampaignplacementreportsResponse)

    async def spadgroupreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpadgroupreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpadgroupreportsResponse)

    async def spproductadreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpproductadreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpproductadreportsResponse)

    async def spkeywordreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpkeywordreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpkeywordreportsResponse)

    async def sptargetreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSptargetreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSptargetreportsResponse)

    async def asinreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSpasinreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpasinreportsResponse)

    async def querywordreports(self, sid: int, report_date: str, target_type: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadQuerywordreportsResponse]:
        """SP用户搜索词报表.

POST /pb/openapi/newad/queryWordReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期, str.
    target_type: 投放类型【默认 keyword】： keyword 关键词 target 商品投放, str.
    show_detail: 是否展示完整归因期信息【默认0】：0 否，1 是, int.
    offset: 分页偏移量，默认0, int.
    length: 分页条数，默认15, int."""
        resp = await self._post("/pb/openapi/newad/queryWordReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "target_type": target_type, "show_detail": show_detail, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadQuerywordreportsResponse)

    async def hsacampaignreports(self, sid: int, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadHsacampaignreportsResponse]:
        """SB广告活动报表.

POST /pb/openapi/newad/hsaCampaignReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaCampaignReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadHsacampaignreportsResponse)

    async def hsacampaignplacementreports(self, sid: int, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadHsacampaignplacementreportsResponse]:
        """SB广告活动-广告位报告.

POST /pb/openapi/newad/hsaCampaignPlacementReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaCampaignPlacementReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadHsacampaignplacementreportsResponse)

    async def hsaadgroupreports(self, sid: int, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadHsaadgroupreportsResponse]:
        """SB广告组报表.

POST /pb/openapi/newad/hsaAdGroupReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报表日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaAdGroupReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadHsaadgroupreportsResponse)

    async def listhsatargetingreport(self, sid: int, sponsored_type: str, target_type: str, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadListhsatargetingreportResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadListhsatargetingreportResponse)

    async def hsaquerywordreports(self, sid: int, report_date: str, target_type: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadHsaquerywordreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadHsaquerywordreportsResponse)

    async def hsapurchasedasinreports(self, sid: int, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadHsapurchasedasinreportsResponse]:
        """SB广告归因于广告的购买报告.

POST /pb/openapi/newad/hsaPurchasedAsinReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/hsaPurchasedAsinReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadHsapurchasedasinreportsResponse)

    async def listhsakeywordplacementreport(self, sid: int, sponsored_type: str, target_type: str, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadListhsakeywordplacementreportResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadListhsakeywordplacementreportResponse)

    async def sdcampaignreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdcampaignreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdcampaignreportsResponse)

    async def sdadgroupreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdadgroupreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdadgroupreportsResponse)

    async def sdproductadreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdproductadreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdproductadreportsResponse)

    async def sdtargetreports(self, sid: int, report_date: str, profile_id: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdtargetreportsResponse]:
        """SD商品定位报表.

POST /pb/openapi/newad/sdTargetReports

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    report_date: 报告日期，格式：Y-m-d, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/pb/openapi/newad/sdTargetReports", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSdtargetreportsResponse)

    async def sdasinreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdasinreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdasinreportsResponse)

    async def sdmatchtargetreports(self, sid: int, report_date: str, profile_id: int = None, show_detail: int = None, offset: int = None, length: int = None) -> list[OpenapiNewadSdmatchtargetreportsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdmatchtargetreportsResponse)

    async def spcampaignhourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSpcampaignhourdataResponse]:
        """SP广告活动小时数据.

POST /pb/openapi/newad/spCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/spCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSpcampaignhourdataResponse)

    async def spadgrouphourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSpadgrouphourdataResponse]:
        """SP广告组小时数据.

POST /pb/openapi/newad/spAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/spAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSpadgrouphourdataResponse)

    async def spadvertisehourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list[OpenapiNewadSpadvertisehourdataResponse]:
        """SP广告小时数据.

POST /pb/openapi/newad/spAdvertiseHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度:  ad  广告维度  both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/spAdvertiseHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSpadvertisehourdataResponse)

    async def sptargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list[OpenapiNewadSptargethourdataResponse]:
        """SP投放小时数据.

POST /pb/openapi/newad/spTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: target  投放维度 both_ad_target  广告+投放维度   both_target_placement 投放+广告位placement维度, str."""
        resp = await self._post("/pb/openapi/newad/spTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSptargethourdataResponse)

    async def sbcampaignhourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSbcampaignhourdataResponse]:
        """SB广告活动小时数据.

POST /pb/openapi/newad/sbCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSbcampaignhourdataResponse)

    async def sbadgrouphourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSbadgrouphourdataResponse]:
        """SB广告组小时数据.

POST /pb/openapi/newad/sbAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSbadgrouphourdataResponse)

    async def sbtargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list[OpenapiNewadSbtargethourdataResponse]:
        """SB投放小时数据.

POST /pb/openapi/newad/sbTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度： target  投放, str."""
        resp = await self._post("/pb/openapi/newad/sbTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSbtargethourdataResponse)

    async def sbadplacementhourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSbadplacementhourdataResponse]:
        """SB广告位小时数据.

POST /pb/openapi/newad/sbAdPlacementHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sbAdPlacementHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSbadplacementhourdataResponse)

    async def sdcampaignhourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSdcampaignhourdataResponse]:
        """SD广告活动小时数据.

POST /pb/openapi/newad/sdCampaignHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sdCampaignHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSdcampaignhourdataResponse)

    async def sdadgrouphourdata(self, report_date: str, campaign_id: float) -> list[OpenapiNewadSdadgrouphourdataResponse]:
        """SD广告组小时数据.

POST /pb/openapi/newad/sdAdGroupHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float."""
        resp = await self._post("/pb/openapi/newad/sdAdGroupHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSdadgrouphourdataResponse)

    async def sdadvertisehourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list[OpenapiNewadSdadvertisehourdataResponse]:
        """SD广告小时数据.

POST /pb/openapi/newad/sdAdvertiseHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: ad  广告维度 both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/sdAdvertiseHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSdadvertisehourdataResponse)

    async def sdtargethourdata(self, report_date: str, campaign_id: float, agg_dimension: str) -> list[OpenapiNewadSdtargethourdataResponse]:
        """SD投放小时数据.

POST /pb/openapi/newad/sdTargetHourData

Args:
    report_date: 报告日期，格式：Y-m-d 只能查询最近60天, str.
    campaign_id: 广告活动id, float.
    agg_dimension: 聚合维度: target  投放维度 both_ad_target  广告+投放维度, str."""
        resp = await self._post("/pb/openapi/newad/sdTargetHourData", {k: v for k, v in {"report_date": report_date, "campaign_id": campaign_id, "agg_dimension": agg_dimension}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSdtargethourdataResponse)

    async def sbdivideasinreports(self, report_date: str, profile_id: int = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSbdivideasinreportsResponse]:
        """SB分摊.

POST /pb/openapi/newad/sbDivideAsinReports

Args:
    profile_id: 店铺profile_id, int.
    report_date: 报告日期, str.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token和offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/sbDivideAsinReports", {k: v for k, v in {"profile_id": profile_id, "report_date": report_date, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadSbdivideasinreportsResponse)

    async def portfolios(self, sid: int, profile_id: int = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadPortfoliosResponse]:
        """广告组合.

POST /pb/openapi/newad/portfolios

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int.
    next_token: 分页游标，上次分页结果中的next_token (第一次分页无需填写，当next_token 和 offset同时存在时以next_token为主, str."""
        resp = await self._post("/pb/openapi/newad/portfolios", {k: v for k, v in {"sid": sid, "profile_id": profile_id, "offset": offset, "length": length, "next_token": next_token}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadPortfoliosResponse)

    async def spcampaigns(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSpcampaignsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpcampaignsResponse)

    async def spadgroups(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSpadgroupsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpadgroupsResponse)

    async def spproductads(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSpproductadsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpproductadsResponse)

    async def spkeywords(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSpkeywordsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpkeywordsResponse)

    async def sptargets(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSptargetsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSptargetsResponse)

    async def spnegativetargetsorkeywords(self, sid: int, target_type: str, profile_id: int = None, campaign_id: float = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSpnegativetargetsorkeywordsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSpnegativetargetsorkeywordsResponse)

    async def hsacampaigns(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadHsacampaignsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadHsacampaignsResponse)

    async def hsaadgroups(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadHsaadgroupsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadHsaadgroupsResponse)

    async def sbtargeting(self, sid: int, ads_type: str, targeting_type: str, profile_id: int = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSbtargetingResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSbtargetingResponse)

    async def hsanegativekeywords(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadHsanegativekeywordsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadHsanegativekeywordsResponse)

    async def hsanegativetargets(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadHsanegativetargetsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadHsanegativetargetsResponse)

    async def sdcampaigns(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSdcampaignsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdcampaignsResponse)

    async def sdadgroups(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSdadgroupsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdadgroupsResponse)

    async def sdproductads(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSdproductadsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdproductadsResponse)

    async def sdtargets(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSdtargetsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdtargetsResponse)

    async def sdnegativetargets(self, sid: int, profile_id: int = None, state: str = None, offset: int = None, length: int = None, next_token: str = None) -> list[OpenapiNewadSdnegativetargetsResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadSdnegativetargetsResponse)

    async def download_abareport(self, country: str, data_start_time: str) -> list[OpenapiNewadAbareportResponse]:
        """ABA搜索词报告-按周维度.

POST /pb/openapi/newad/abaReport

Args:
    country: 国家代码：如US, str.
    data_start_time: 报表开始日期：每周周日的日期，仅支持最近45天, str."""
        resp = await self._post("/pb/openapi/newad/abaReport", {k: v for k, v in {"country": country, "data_start_time": data_start_time}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiNewadAbareportResponse)

    async def apilogstandard(self, sid: int, log_source: str, sponsored_type: str, operate_type: str, start_date: str, end_date: str, offset: int = None, length: int = None) -> list[OpenapiNewadApilogstandardResponse]:
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
        return self._parse_list(resp.data, OpenapiNewadApilogstandardResponse)

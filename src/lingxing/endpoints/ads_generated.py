"""Ads API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class AdsEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def newad_apiLogStandard(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        操作日志（新）

        API: /pb/openapi/newad/apiLogStandard
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 起始时间，格式：Y-m-d【日期间隔不能超过一个月】 (Required)
            end_date: 结束时间，格式：Y-m-d【日期间隔不能超过一个月】 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_apiLogStandard(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/apiLogStandard",
            method="GET",
            req_body=params
        )



    async def sddata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SD广告组小时数据

        API: /pb/openapi/newad/sdAdGroupHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sddata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAdGroupHourData",
            method="POST",
            req_body=params
        )



    async def get_sb(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB关键词-广告位报告

        API: /pb/openapi/newad/listHsaKeywordPlacementReport
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/listHsaKeywordPlacementReport",
            method="GET",
            req_body=params
        )



    async def sbreport(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB广告活动报表

        API: /pb/openapi/newad/hsaCampaignReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaCampaignReports",
            method="POST",
            req_body=params
        )



    async def get_dsplist_order(
        self,
        access_token: str,
        profile_id: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询DSP报告列表-订单

        API: /basicOpen/dspReport/order/list
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)
            profile_id: 亚马逊店铺数字id，查询广告账号列表接口对应字段【profile_id】 (Required)
            start_date: 报告开始日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            end_date: 报告结束日期，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_dsplist_order(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "profile_id": profile_id,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/dspReport/order/list",
            method="GET",
            req_body=params
        )



    async def sbdata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SB广告组小时数据

        API: /pb/openapi/newad/sbAdGroupHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbAdGroupHourData",
            method="POST",
            req_body=params
        )



    async def spdata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SP广告活动小时数据

        API: /pb/openapi/newad/spCampaignHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spCampaignHourData",
            method="POST",
            req_body=params
        )



    async def sbdata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SB广告位小时数据

        API: /pb/openapi/newad/sbAdPlacementHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbAdPlacementHourData",
            method="POST",
            req_body=params
        )



    async def newad_hsaCampaignPlacementReports(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB广告活动-广告位报告

        API: /pb/openapi/newad/hsaCampaignPlacementReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaCampaignPlacementReports(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaCampaignPlacementReports",
            method="POST",
            req_body=params
        )



    async def spdata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SP广告组小时数据

        API: /pb/openapi/newad/spAdGroupHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdGroupHourData",
            method="POST",
            req_body=params
        )



    async def sdreport(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD广告活动报表

        API: /pb/openapi/newad/sdCampaignReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdCampaignReports",
            method="POST",
            req_body=params
        )



    async def sddata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SD广告活动小时数据

        API: /pb/openapi/newad/sdCampaignHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sddata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdCampaignHourData",
            method="POST",
            req_body=params
        )



    async def spdata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SP广告位小时数据

        API: /pb/openapi/newad/spAdPlacementHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdPlacementHourData",
            method="POST",
            req_body=params
        )



    async def spreport(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP广告组报表

        API: /pb/openapi/newad/spAdGroupReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdGroupReports",
            method="POST",
            req_body=params
        )



    async def newad_campaignPlacementReports(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP广告位报告

        API: /pb/openapi/newad/campaignPlacementReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_campaignPlacementReports(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/campaignPlacementReports",
            method="POST",
            req_body=params
        )



    async def sdreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD广告组报表

        API: /pb/openapi/newad/sdAdGroupReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAdGroupReports",
            method="POST",
            req_body=params
        )



    async def spreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP广告活动报表

        API: /pb/openapi/newad/spCampaignReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spCampaignReports",
            method="GET",
            req_body=params
        )



    async def newad_sbDivideAsinReports(
        self,
        access_token: str,
        profile_id: int,
        report_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB分摊

        API: /pb/openapi/newad/sbDivideAsinReports
        Method: POST

        Args:
            access_token: Access token for authentication
            profile_id: 店铺profile_id (Required)
            report_date: 报告日期 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_sbDivideAsinReports(token, ...)
            >>> print(result)
        """
        params = {
            "profile_id": profile_id,
            "report_date": report_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbDivideAsinReports",
            method="POST",
            req_body=params
        )



    async def get_sddata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SD投放小时数据

        API: /pb/openapi/newad/sdTargetHourData
        Method: GET

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sddata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdTargetHourData",
            method="GET",
            req_body=params
        )



    async def spreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP广告商品报表

        API: /pb/openapi/newad/spProductAdReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spProductAdReports",
            method="POST",
            req_body=params
        )



    async def get_spreport(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP商品定位报表

        API: /pb/openapi/newad/spTargetReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spTargetReports",
            method="GET",
            req_body=params
        )



    async def spreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP关键词报表

        API: /pb/openapi/newad/spKeywordReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spKeywordReports",
            method="POST",
            req_body=params
        )



    async def sbdata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SB广告活动小时数据

        API: /pb/openapi/newad/sbCampaignHourData
        Method: POST

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbCampaignHourData",
            method="POST",
            req_body=params
        )



    async def sddata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SD广告小时数据

        API: /pb/openapi/newad/sdAdvertiseHourData
        Method: GET

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sddata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAdvertiseHourData",
            method="GET",
            req_body=params
        )



    async def get_sdreport(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD匹配的目标报表

        API: /pb/openapi/newad/sdMatchTargetReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdMatchTargetReports",
            method="GET",
            req_body=params
        )



    async def get_sbdata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SB投放小时数据

        API: /pb/openapi/newad/sbTargetHourData
        Method: GET

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sbdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbTargetHourData",
            method="GET",
            req_body=params
        )



    async def get_sdreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD商品定位报表

        API: /pb/openapi/newad/sdTargetReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdTargetReports",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB广告的投放报告

        API: /pb/openapi/newad/listHsaTargetingReport
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/listHsaTargetingReport",
            method="GET",
            req_body=params
        )



    async def sdreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD广告商品报表

        API: /pb/openapi/newad/sdProductAdReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdProductAdReports",
            method="POST",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        report_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB广告创意报告

        API: /pb/openapi/newad/listHsaProductAdReport
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            report_date: 报告日期，时间格式：yyyy-MM-dd (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "report_date": report_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/listHsaProductAdReport",
            method="POST",
            req_body=params
        )



    async def get_spdata(
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SP投放小时数据

        API: /pb/openapi/newad/spTargetHourData
        Method: GET

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_spdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spTargetHourData",
            method="GET",
            req_body=params
        )



    async def newad_hsaPurchasedAsinReports(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB广告归因于广告的购买报告

        API: /pb/openapi/newad/hsaPurchasedAsinReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaPurchasedAsinReports(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaPurchasedAsinReports",
            method="POST",
            req_body=params
        )



    async def spdata(  # noqa: F811
        self,
        access_token: str,
        report_date: str,
        campaign_id: Any
    ) -> dict[str, Any]:
        """
        SP广告小时数据

        API: /pb/openapi/newad/spAdvertiseHourData
        Method: GET

        Args:
            access_token: Access token for authentication
            report_date: 报告日期，格式：Y-m-d 只能查询最近60天 (Required)
            campaign_id: 广告活动id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spdata(token, ...)
            >>> print(result)
        """
        params = {
            "report_date": report_date,
            "campaign_id": campaign_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdvertiseHourData",
            method="GET",
            req_body=params
        )



    async def sdreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SD已购买商品报表

        API: /pb/openapi/newad/sdAsinReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sdreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAsinReports",
            method="POST",
            req_body=params
        )



    async def sbreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB用户搜索词报表

        API: /pb/openapi/newad/hsaQueryWordReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaQueryWordReports",
            method="GET",
            req_body=params
        )



    async def sbreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SB广告组报表

        API: /pb/openapi/newad/hsaAdGroupReports
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.sbreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaAdGroupReports",
            method="POST",
            req_body=params
        )



    async def spreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP用户搜索词报表

        API: /pb/openapi/newad/queryWordReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/queryWordReports",
            method="GET",
            req_body=params
        )



    async def get_analysisproduct(
        self,
        access_token: str,
        sid: str,
        profile_id: int,
        sku: list[Any],
        start_date: str,
        end_date: str,
        sd: Any | None = None
    ) -> dict[str, Any]:
        """
        出单时段分析（产品）

        API: /basicOpen/adReport/productOrderAnalysis/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: sid (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            sku: msku最多10个 (Required)
            start_date: 开始日期，格式：Y-m-d (Required)
            end_date: 结束日期，格式：Y-m-d (Required)
            sd: 否 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_analysisproduct(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "sku": sku,
            "start_date": start_date,
            "end_date": end_date,
            "sd": sd
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/adReport/productOrderAnalysis/list",
            method="POST",
            req_body=params
        )



    async def spreport(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        SP已购买商品报表

        API: /pb/openapi/newad/asinReports
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.spreport(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/asinReports",
            method="GET",
            req_body=params
        )



    async def newad_sdCampaigns(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SD广告活动

        API: /pb/openapi/newad/sdCampaigns
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_sdCampaigns(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdCampaigns",
            method="GET",
            req_body=params
        )



    async def newad_spCampaigns(
        self,
        access_token: str,
        code: int,
        message: str,
        error_details: list[Any],
        request_id: str,
        response_time: str,
        total: int,
        next_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        SP广告活动

        API: /pb/openapi/newad/spCampaigns
        Method: GET

        Args:
            access_token: Access token for authentication
            code: 状态码，0 成功 (Required)
            message: 提示消息 (Required)
            error_details: 错误信息 (Required)
            request_id: 请求链路id (Required)
            response_time: 响应时间 (Required)
            total: 总数 (Required)
            next_token: 分页游标，填入下次请求中的next_token (Required)
            data: 响应数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_spCampaigns(token, ...)
            >>> print(result)
        """
        params = {
            "code": code,
            "message": message,
            "error_details": error_details,
            "request_id": request_id,
            "response_time": response_time,
            "total": total,
            "next_token": next_token,
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spCampaigns",
            method="GET",
            req_body=params
        )



    async def newad_hsaProductAds(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB广告创意

        API: /pb/openapi/newad/hsaProductAds
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaProductAds(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaProductAds",
            method="GET",
            req_body=params
        )



    async def newad_sdProductAds(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SD广告商品

        API: /pb/openapi/newad/sdProductAds
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_sdProductAds(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdProductAds",
            method="POST",
            req_body=params
        )



    async def newad_spProductAds(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SP广告商品

        API: /pb/openapi/newad/spProductAds
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_spProductAds(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spProductAds",
            method="POST",
            req_body=params
        )



    async def newad_hsaAdGroups(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB广告组

        API: /pb/openapi/newad/hsaAdGroups
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaAdGroups(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaAdGroups",
            method="POST",
            req_body=params
        )



    async def newad_hsaNegativeKeywords(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB否定关键词

        API: /pb/openapi/newad/hsaNegativeKeywords
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaNegativeKeywords(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaNegativeKeywords",
            method="POST",
            req_body=params
        )



    async def newad_sdAdGroups(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SD广告组

        API: /pb/openapi/newad/sdAdGroups
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_sdAdGroups(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdAdGroups",
            method="POST",
            req_body=params
        )



    async def newad_hsaCampaigns(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB广告活动

        API: /pb/openapi/newad/hsaCampaigns
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_hsaCampaigns(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaCampaigns",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB广告的投放

        API: /pb/openapi/newad/sbTargeting
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sbTargeting",
            method="GET",
            req_body=params
        )



    async def newad_portfolios(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        广告组合

        API: /pb/openapi/newad/portfolios
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_portfolios(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/portfolios",
            method="GET",
            req_body=params
        )



    async def get_sd(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SD否定商品定位

        API: /pb/openapi/newad/sdNegativeTargets
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sd(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdNegativeTargets",
            method="GET",
            req_body=params
        )



    async def get_sp(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        target_type: str,
        campaign_id: Any | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SP否定投放

        API: /pb/openapi/newad/spNegativeTargetsOrKeywords
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            campaign_id: 广告活动id (Optional)
            target_type: 投放类型：keyword target (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "campaign_id": campaign_id,
            "target_type": target_type,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spNegativeTargetsOrKeywords",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SB否定商品投放

        API: /pb/openapi/newad/hsaNegativeTargets
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/hsaNegativeTargets",
            method="GET",
            req_body=params
        )



    async def newad_spKeywords(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SP关键词

        API: /pb/openapi/newad/spKeywords
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_spKeywords(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spKeywords",
            method="POST",
            req_body=params
        )



    async def newad_spAdGroups(
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SP广告组

        API: /pb/openapi/newad/spAdGroups
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.newad_spAdGroups(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spAdGroups",
            method="POST",
            req_body=params
        )



    async def get_sd(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SD商品定位

        API: /pb/openapi/newad/sdTargets
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sd(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/sdTargets",
            method="GET",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询广告账号列表

        API: /basicOpen/baseData/account/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/baseData/account/list",
            method="POST",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        profile_id: int,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        SP商品定位

        API: /pb/openapi/newad/spTargets
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            profile_id: VC广告店铺profile_id，对应查询广告账号列表接口对应字段【profile_id】，sid跟profile_id其中一个必填 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "profile_id": profile_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/spTargets",
            method="GET",
            req_body=params
        )



    async def aba(
        self,
        access_token: str,
        country: str,
        data_start_time: str
    ) -> dict[str, Any]:
        """
        ABA搜索词报告-按周维度

        API: /pb/openapi/newad/abaReport
        Method: POST

        Args:
            access_token: Access token for authentication
            country: 国家代码：如US (Required)
            data_start_time: 报表开始日期：每周周日的日期，仅支持最近45天 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.aba(token, ...)
            >>> print(result)
        """
        params = {
            "country": country,
            "data_start_time": data_start_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/openapi/newad/abaReport",
            method="POST",
            req_body=params
        )


"""Statistics API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class StatisticsEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_inventoryreport_report(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sys_wid: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-本地仓-历史报表-汇总

        API: /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList
        Method: GET

        Args:
            access_token: Access token for authentication
            sys_wid: 领星系统仓库id，多个用英文逗号分隔 (Optional)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList",
            method="GET",
            req_body=params
        )



    async def get_asin360data(
        self,
        access_token: str,
        sids: str,
        date_start: str,
        date_end: str,
        summary_field_value: str
    ) -> dict[str, Any]:
        """
        查询asin360小时数据

        API: /basicOpen/salesAnalysis/productPerformance/performanceTrendByHour
        Method: POST

        Args:
            access_token: Access token for authentication
            sids: 店铺id，多个值使用英文逗号隔开，最大上限为200 (Required)
            date_start: 开始时间，闭区间，格式：Y-m-d (Required)
            date_end: 结束时间，闭区间，格式：Y-m-d (Required)
            summary_field_value: 查询维度值 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_asin360data(token, ...)
            >>> print(result)
        """
        params = {
            "sids": sids,
            "date_start": date_start,
            "date_end": date_end,
            "summary_field_value": summary_field_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/salesAnalysis/productPerformance/performanceTrendByHour",
            method="POST",
            req_body=params
        )



    async def get_order(
        self,
        access_token: str,
        sid: int,
        event_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询销量、订单量、销售额

        API: /erp/sc/data/sales_report/asinDailyLists
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            event_date: 报表时间【站点时间】，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "event_date": event_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/sales_report/asinDailyLists",
            method="POST",
            req_body=params
        )



    async def get_reportlist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询采购报表列表 - 供应商

        API: /basicOpen/report/purchase/supplier/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/report/purchase/supplier/list",
            method="POST",
            req_body=params
        )



    async def get_orderprofit_msku(
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询订单利润-MSKU

        API: /basicOpen/finance/mreport/OrderProfit
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限5000 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s (Required)
            endDate: 查询时间，双闭区间，格式：Y-m-d 或 Y-m-d H:i:s (Required)
            searchField: 搜索值类型, 可选值:seller_sku,asin,local_name, local_sku (Optional)
            searchValue: 搜索的值 (Optional)
            currencyCode: 币种code【默认原币种】, 可选值：原币种,CNY,USD,EUR,JPY,AUD,CAD,MXN,GBP,INR,AED,SGD,SAR,BRL,SEK,PLN,TRY,HKD (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderprofit_msku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/mreport/OrderProfit",
            method="POST",
            req_body=params
        )



    async def get_fba(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA长期仓储费

        API: /erp/sc/data/fba_report/storageFeeLongTerm
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 收费日期，左闭区间 (Required)
            end_date: 收费日期，右开区间 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba(token, ...)
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
            route_name="/erp/sc/data/fba_report/storageFeeLongTerm",
            method="POST",
            req_body=params
        )



    async def get_inventoryreport_report_detail(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int,
        length: int,
        sys_wid: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-本地仓-历史报表-明细

        API: /erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            sys_wid: 系统仓库id，多个用英文逗号分隔 (Optional)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认15 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList",
            method="GET",
            req_body=params
        )



    async def get_profitstatistics_asin(
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润统计-父ASIN

        API: /bd/profit/statistics/open/parent/asin/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            endDate: 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            searchField: 搜索值类型：parent_asin (Optional)
            searchValue: 搜索值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitstatistics_asin(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/statistics/open/parent/asin/list",
            method="POST",
            req_body=params
        )



    async def inventoryreport_fba(
        self,
        access_token: str,
        offset: int,
        length: int,
        seller_id: list[Any],
        start_date: str,
        end_date: str
    ) -> dict[str, Any]:
        """
        库存报表-FBA-新版-汇总

        API: /cost/center/openApi/fba/gather/query
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认为15 (Required)
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Required)
            start_date: 统计起始月份，格式：Y-m (Required)
            end_date: 统计结束月份，格式：Y-m (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventoryreport_fba(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "seller_id": seller_id,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/openApi/fba/gather/query",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        search_value: str | None = None,
        sids: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊赔偿报告列表

        API: /basicOpen/openapi/mwsReport/reimbursementList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            search_value: 搜索值 (Optional)
            sids: 店铺id，多个使用英文逗号分割 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            start_date: 批准日期开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_date: 批准日期结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "search_value": search_value,
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/mwsReport/reimbursementList",
            method="POST",
            req_body=params
        )



    async def get_inventoryreport_fba_report_detail(
        self,
        access_token: str,
        start_month: str | None = None,
        end_month: str | None = None,
        seller_id: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-FBA-历史报表-汇总-明细

        API: /erp/sc/routing/fba/fbaStockReport/getList
        Method: GET

        Args:
            access_token: Access token for authentication
            start_month: 开始月份，默认当前月份 (Optional)
            end_month: 截至月份，默认当前月份 (Optional)
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Optional)
            offset: 分页偏移量【dimention=2 明细维度生效】，默认0 (Optional)
            length: 分页长度【dimention=2 明细维度生效】，默认20，上限5000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_fba_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "start_month": start_month,
            "end_month": end_month,
            "seller_id": seller_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/fba/fbaStockReport/getList",
            method="GET",
            req_body=params
        )



    async def get_inventoryreport_report(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sys_wid: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-海外仓-历史报表-汇总

        API: /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList
        Method: GET

        Args:
            access_token: Access token for authentication
            sys_wid: 领星仓库id，多个用英文逗号分隔 (Optional)
            start_date: 开始时间 (Required)
            end_date: 结束时间 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList",
            method="GET",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        sids: list[Any],
        search_value: str,
        start_date: str,
        end_date: str
    ) -> dict[str, Any]:
        """
        查询运营日志

        API: /basicOpen/operateManage/operateLog/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            search_value: 搜索值 (Required)
            start_date: 开始时间，闭区间，格式：Y-m-d (Required)
            end_date: 结束时间，闭区间，格式：Y-m-d (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "sids": sids,
            "search_value": search_value,
            "start_date": start_date,
            "end_date": end_date
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/operateManage/operateLog/list",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: Any | None = None,
        length: Any | None = None,
        sids: list[Any] | None = None,
        mids: list[Any] | None = None,
        search_value: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询运营日志(新)

        API: /basicOpen/operateManage/operateLog/list/v2
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认为20 (Optional)
            length: 分页长度，默认为200 (Optional)
            sids: 店铺列表 (Optional)
            mids: 国家列表 (Optional)
            start_date: 开始时间，格式：yyyy-mm-dd (Required)
            end_date: 结束时间，格式：yyyy-mm-dd (Required)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "mids": mids,
            "start_date": start_date,
            "end_date": end_date,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/operateManage/operateLog/list/v2",
            method="POST",
            req_body=params
        )



    async def get_statistics_analysis(
        self,
        access_token: str,
        endDate: str,
        length: int,
        offset: int,
        startDate: str,
        asinType: str | None = None,
        dateType: int | None = None,
        mids: list[Any] | None = None,
        principalUid: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        storeId: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        统计-查询退货分析

        API: /basicOpen/salesAnalysis/returnOrder/analysisLists
        Method: POST

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，格式：yyyy-MM-dd，与startDate配合使用，最多支持366天范围 (Required)
            length: 分页长度，每页数据条数 (Required)
            offset: 分页偏移量，当前页码 (Required)
            startDate: 开始日期，格式：yyyy-MM-dd，与endDate配合使用，最多支持366天范围 (Required)
            asinType: 维度类型，枚举值：msku, asin, parentAsin, sku, spu（注意：不支持sid、country、category、band） (Optional)
            dateType: 时间类型，枚举值：0-退货时间, 1-下单时间 (Optional)
            mids: 国家ID列表（mid） (Optional)
            principalUid: 负责人ID列表 (Optional)
            searchField: 搜索字段类型，枚举值：msku-MSKU, asin-ASIN, parentAsin-父ASIN, localSku-SKU, localName-品名, spu-SPU, spuName-款名 (Optional)
            searchValue: 搜索值列表，与searchField配合使用 (Optional)
            sortField: 排序字段，枚举值：curReturnGoodsCount-退货量, returnGoodsCountRatio-退货量环比, curVolume-销量, curReturnGoodsVolumeRatio-退货率, returnGoodsVolumeRatioDiff-退货率环比差异 (Optional)
            sortType: 排序类型，枚举值：ASC-升序, DESC-降序 (Optional)
            storeId: 店铺ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statistics_analysis(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "offset": offset,
            "startDate": startDate,
            "asinType": asinType,
            "dateType": dateType,
            "mids": mids,
            "principalUid": principalUid,
            "searchField": searchField,
            "searchValue": searchValue,
            "sortField": sortField,
            "sortType": sortType,
            "storeId": storeId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/salesAnalysis/returnOrder/analysisLists",
            method="POST",
            req_body=params
        )



    async def inventoryreport_report_detail(
        self,
        access_token: str,
        offset: int,
        length: int,
        start_date: str,
        end_date: str,
        sys_wid: str | None = None
    ) -> dict[str, Any]:
        """
        库存报表-本地仓-新报表-明细

        API: /inventory/center/openapi/storageReport/local/detail/page
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页页码，默认1 (Required)
            length: 分页长度，默认15 (Required)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            sys_wid: 系统仓库id，多个用英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventoryreport_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "sys_wid": sys_wid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/inventory/center/openapi/storageReport/local/detail/page",
            method="POST",
            req_body=params
        )



    async def get_report_fbaorder(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBA退货订单

        API: /erp/sc/data/mws_report/refundOrders
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始时间，左闭右开，格式：Y-m-d (Required)
            end_date: 结束时间，左闭右开，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbaorder(token, ...)
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
            route_name="/erp/sc/data/mws_report/refundOrders",
            method="POST",
            req_body=params
        )



    async def get_report_fbmorder(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊源报表-FBM退货订单

        API: /erp/sc/routing/data/order/fbmReturnOrderList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 开始时间，左闭区间，格式：Y-m-d (Required)
            end_date: 结束时间，右开区间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_report_fbmorder(token, ...)
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
            route_name="/erp/sc/routing/data/order/fbmReturnOrderList",
            method="POST",
            req_body=params
        )



    async def create_order(
        self,
        access_token: str,
        lists: list[Any]
    ) -> dict[str, Any]:
        """
        创建移除订单

        API: /erp/sc/statistic/removalOrder/createAndCommit
        Method: POST

        Args:
            access_token: Access token for authentication
            lists: 提交数据，支持批量，上限100个 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_order(token, ...)
            >>> print(result)
        """
        params = {
            "lists": lists
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/statistic/removalOrder/createAndCommit",
            method="POST",
            req_body=params
        )



    async def get_product(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询产品表现（旧）

        API: /erp/sc/data/sales_report/asinList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 报表时间，格式：Y-m-d，闭区间 (Required)
            end_date: 报表时间，格式：Y-m-d，开区间 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
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
            route_name="/erp/sc/data/sales_report/asinList",
            method="POST",
            req_body=params
        )



    async def get_inventoryreport_report_detail(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int,
        length: int,
        sys_wid: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-海外仓-历史报表-明细

        API: /erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList
        Method: GET

        Args:
            access_token: Access token for authentication
            sys_wid: 系统仓库id，多个用英文逗号分隔 (Optional)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Required)
            length: 每页条数，默认15 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "sys_wid": sys_wid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList",
            method="GET",
            req_body=params
        )



    async def inventoryreport_fba_detail(
        self,
        access_token: str,
        offset: int,
        length: int,
        start_date: str,
        end_date: str,
        seller_id: list[Any]
    ) -> dict[str, Any]:
        """
        库存报表-FBA-新版-明细

        API: /cost/center/openApi/fba/detail/query
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认15，最大2100 (Required)
            start_date: 开始日期，格式：Y-m (Required)
            end_date: 结束日期，格式：Y-m (Required)
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventoryreport_fba_detail(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "seller_id": seller_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/openApi/fba/detail/query",
            method="POST",
            req_body=params
        )



    async def inventoryreport_report_detail(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int,
        start_date: str,
        end_date: str,
        sys_wid: str | None = None
    ) -> dict[str, Any]:
        """
        库存报表-海外仓-新报表-明细

        API: /inventory/center/openapi/storageReport/overseas/detail/page
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 页码，默认1 (Required)
            length: 分页长度，默认15 (Required)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            sys_wid: 系统仓库id，多个以英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventoryreport_report_detail(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "sys_wid": sys_wid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/inventory/center/openapi/storageReport/overseas/detail/page",
            method="POST",
            req_body=params
        )



    async def get_profitstatistics_store(
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润统计-店铺

        API: /bd/profit/statistics/open/seller/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            endDate: 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitstatistics_store(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/statistics/open/seller/list",
            method="POST",
            req_body=params
        )



    async def get_inventoryreport_report(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sys_wid: int | None = None
    ) -> dict[str, Any]:
        """
        库存报表-本地仓-新报表-汇总

        API: /inventory/center/openapi/storageReport/local/aggregate/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            sys_wid: 系统仓库id，多个用英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sys_wid": sys_wid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/inventory/center/openapi/storageReport/local/aggregate/list",
            method="POST",
            req_body=params
        )



    async def get_profitstatistics_asin(  # noqa: F811
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润统计-ASIN

        API: /bd/profit/statistics/open/asin/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            endDate: 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            searchField: 搜索值类型：asin (Optional)
            searchValue: 搜索值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitstatistics_asin(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/statistics/open/asin/list",
            method="POST",
            req_body=params
        )



    async def get_profitstatistics_msku(
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润统计-MSKU

        API: /bd/profit/statistics/open/msku/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            endDate: 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】 (Required)
            searchField: 搜索值类型：msku (Optional)
            searchValue: 搜索值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitstatistics_msku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/statistics/open/msku/list",
            method="POST",
            req_body=params
        )



    async def get_reportlist(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        time_type: int | None = None
    ) -> dict[str, Any]:
        """
        查询采购报表列表 - 采购员

        API: /basicOpen/report/purchase/buyer/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_date: 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            time_type: 时间类型：1 下单时间，2 到货时间 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "time_type": time_type
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/report/purchase/buyer/list",
            method="POST",
            req_body=params
        )



    async def get_inventoryreport_report(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sys_wid: str | None = None
    ) -> dict[str, Any]:
        """
        库存报表-海外仓-新报表-汇总

        API: /inventory/center/openapi/storageReport/overseas/aggregate/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            sys_wid: 系统仓库id，多个用英文逗号分隔 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventoryreport_report(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sys_wid": sys_wid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/inventory/center/openapi/storageReport/overseas/aggregate/list",
            method="POST",
            req_body=params
        )



    async def get_store(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询店铺汇总销量

        API: /erp/sc/data/sales_report/sales
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            start_date: 报表时间，格式：Y-m-d，闭区间 (Required)
            end_date: 报表时间，格式：Y-m-d，闭区间 (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_store(token, ...)
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
            route_name="/erp/sc/data/sales_report/sales",
            method="POST",
            req_body=params
        )



    async def get_reportlist_product(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        time_type: int | None = None,
        sids: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询采购报表列表 - 产品

        API: /basicOpen/report/purchase/product/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_date: 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            time_type: 时间类型：1 下单时间，2 到货时间 (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_reportlist_product(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "time_type": time_type,
            "sids": sids,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/report/purchase/product/list",
            method="POST",
            req_body=params
        )



    async def get_fba(  # noqa: F811
        self,
        access_token: str,
        sid: int,
        month: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA月仓储费

        API: /erp/sc/data/fba_report/storageFeeMonth
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            month: 收费月份，格式：Y-m (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "month": month,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/fba_report/storageFeeMonth",
            method="POST",
            req_body=params
        )



    async def get_product(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int,
        sort_type: str,
        start_date: str,
        end_date: str,
        search_value: list[Any] | None = None,
        mid: int | None = None,
        extend_search: list[Any] | None = None,
        currency_code: str | None = None
    ) -> dict[str, Any]:
        """
        查询产品表现

        API: /bd/productPerformance/openApi/asinList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度，最大10000 (Required)
            sort_type: 排序方式：desc【降序】、asc【升序】，默认desc (Required)
            search_value: 搜索值，最多批量搜索50个 (Optional)
            mid: 站点id (Optional)
            start_date: 开始日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD (Required)
            end_date: 结束日期，筛选开始结束时间范围不能超过92天，双闭区间，格式：YYYY-MM-DD (Required)
            extend_search: 表头筛选 (Optional)
            currency_code: 货币类型，不传代表原币种，转换仅支持USD、CNY (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sort_type": sort_type,
            "search_value": search_value,
            "mid": mid,
            "start_date": start_date,
            "end_date": end_date,
            "extend_search": extend_search,
            "currency_code": currency_code
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/productPerformance/openApi/asinList",
            method="POST",
            req_body=params
        )


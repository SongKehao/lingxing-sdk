"""Finance API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class FinanceEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def otherFee_discard(
        self,
        access_token: str,
        numbers: list[Any]
    ) -> dict[str, Any]:
        """
        作废费用单

        API: /bd/fee/management/open/feeManagement/otherFee/discard
        Method: POST

        Args:
            access_token: Access token for authentication
            numbers: 费用单号，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.otherFee_discard(token, ...)
            >>> print(result)
        """
        params = {
            "numbers": numbers
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/discard",
            method="POST",
            req_body=params
        )



    async def delete(
        self,
        access_token: str,
        numbers: list[Any]
    ) -> dict[str, Any]:
        """
        删除费用单

        API: /bd/fee/management/open/feeManagement/otherFee/delete
        Method: POST

        Args:
            access_token: Access token for authentication
            numbers: 费用单号，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "numbers": numbers
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/delete",
            method="POST",
            req_body=params
        )



    async def get_settlement_settlement(
        self,
        access_token: str,
        店铺id: Any | None = None
    ) -> dict[str, Any]:
        """
        查询结算中心 - 结算汇总

        API: /bd/sp/api/open/settlement/summary/list
        Method: POST

        Args:
            access_token: Access token for authentication
            店铺id: [array] (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlement_settlement(token, ...)
            >>> print(result)
        """
        params = {
            "店铺id": 店铺id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/settlement/summary/list",
            method="POST",
            req_body=params
        )



    async def get_inventorydetaildata(
        self,
        access_token: str,
        sellerIds: list[Any],
        startDate: str,
        endDate: str,
        fnskus: list[Any] | None = None,
        asins: list[Any] | None = None,
        mskus: list[Any] | None = None,
        referenceId: str | None = None,
        locations: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询库存分类账detail数据

        API: /cost/center/ods/detail/query
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerIds: 亚马逊店铺id (Required)
            startDate: 统计起始日期 Y-m-d 闭区间 (Required)
            endDate: 统计结束日期 Y-m-d 闭区间 (Required)
            fnskus: fnsku列表 (Optional)
            asins: asin列表 (Optional)
            mskus: msku列表 (Optional)
            referenceId: 引用id，支持模糊搜索 (Optional)
            locations: 国家编码列表 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventorydetaildata(token, ...)
            >>> print(result)
        """
        params = {
            "sellerIds": sellerIds,
            "startDate": startDate,
            "endDate": endDate,
            "fnskus": fnskus,
            "asins": asins,
            "mskus": mskus,
            "referenceId": referenceId,
            "locations": locations,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/ods/detail/query",
            method="GET",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询请款池 - 货款预付款

        API: /basicOpen/finance/requestFundsPool/prepay/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
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
            "start_time": start_time,
            "end_time": end_time,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/prepay/list",
            method="POST",
            req_body=params
        )



    async def otherFee_edit(
        self,
        access_token: str,
        id: str,
        submit_type: int,
        date: str,
        currency_code: str,
        other_fee_type_id: int,
        is_request_pool: int,
        fee_items: list[Any],
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        编辑费用单

        API: /bd/fee/management/open/feeManagement/otherFee/edit
        Method: POST

        Args:
            access_token: Access token for authentication
            id: 费用单id，查询费用明细列表 接口对应字段【records>>id】 (Required)
            submit_type: 提交类型：1 暂存，2 提交 (Required)
            date: 分摊日期，格式：Y-m-d 或 Y-m (Required)
            currency_code: 币种代码 (Required)
            other_fee_type_id: 费用类型id，查询费用类型列表 接口对应字段【id】 (Required)
            is_request_pool: 是否请款：0 否，1 是 (Required)
            remark: 单据备注 (Optional)
            fee_items: 费用明细项 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.otherFee_edit(token, ...)
            >>> print(result)
        """
        params = {
            "id": id,
            "submit_type": submit_type,
            "date": date,
            "currency_code": currency_code,
            "other_fee_type_id": other_fee_type_id,
            "is_request_pool": is_request_pool,
            "remark": remark,
            "fee_items": fee_items
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/edit",
            method="POST",
            req_body=params
        )



    async def get_fba(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        wh_names: list[Any] | None = None,
        shop_names: list[Any] | None = None,
        skus: list[Any] | None = None,
        mskus: list[Any] | None = None,
        business_numbers: list[Any] | None = None,
        origin_accounts: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询FBA成本计价流水

        API: /cost/center/api/cost/stream
        Method: POST

        Args:
            access_token: Access token for authentication
            wh_names: 仓库名 (Optional)
            shop_names: 店铺名 (Optional)
            skus: sku (Optional)
            mskus: msku (Optional)
            start_date: 起始日期，Y-m-d，不允许跨月 (Required)
            end_date: 结束日期，Y-m-d，不允许跨月 (Required)
            business_numbers: 业务编号 (Optional)
            origin_accounts: 源头单据号 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认200条 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba(token, ...)
            >>> print(result)
        """
        params = {
            "wh_names": wh_names,
            "shop_names": shop_names,
            "skus": skus,
            "mskus": mskus,
            "start_date": start_date,
            "end_date": end_date,
            "business_numbers": business_numbers,
            "origin_accounts": origin_accounts,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/api/cost/stream",
            method="POST",
            req_body=params
        )



    async def get_info(
        self,
        access_token: str,
        sid: Any,
        currencyCode: str,
        settleMonth: str
    ) -> dict[str, Any]:
        """
        应收报告-详情-基础信息

        API: /bd/sp/api/open/monthly/receivable/report/list/detail/info
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            currencyCode: 币种code (Required)
            settleMonth: 结算月 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "currencyCode": currencyCode,
            "settleMonth": settleMonth
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/monthly/receivable/report/list/detail/info",
            method="POST",
            req_body=params
        )



    async def get_profitreport_asin(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-父ASIN

        API: /bd/profit/report/open/report/parent/asin/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            searchField: 搜索值类型，parent_asin (Optional)
            searchValue: 搜索的值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_asin(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/parent/asin/list",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        sid: int,
        currencyCode: str,
        settleMonth: str,
        searchValue: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        应收报告-详情-列表

        API: /bd/sp/api/open/monthly/receivable/report/list/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            currencyCode: 币种code (Required)
            settleMonth: 结算月 (Required)
            searchValue: 搜索值 (Optional)
            offset: 偏移量 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "currencyCode": currencyCode,
            "settleMonth": settleMonth,
            "searchValue": searchValue,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/monthly/receivable/report/list/detail",
            method="POST",
            req_body=params
        )



    async def get_profitreport_store(
        self,
        access_token: str,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-店铺月度汇总

        API: /bd/profit/report/open/report/seller/summary/list
        Method: POST

        Args:
            access_token: Access token for authentication
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_store(token, ...)
            >>> print(result)
        """
        params = {
            "mids": mids,
            "sids": sids,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/seller/summary/list",
            method="POST",
            req_body=params
        )



    async def get_profitreport_store(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-店铺

        API: /bd/profit/report/open/report/seller/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            currencyCode: 币种code【默认原币种】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_store(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/seller/list",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询请款池-物流请款

        API: /basicOpen/finance/requestFundsPool/logistics/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
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
            "start_time": start_time,
            "end_time": end_time,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/logistics/list",
            method="POST",
            req_body=params
        )



    async def get_profitreport_ordertransaction(
        self,
        access_token: str,
        startDate: str,
        endDate: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        gmtModifiedStartDate: str | None = None,
        gmtModifiedEndDate: str | None = None,
        searchValue: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        FBM_FBM: Any | None = None,
        principalUids: list[Any] | None = None,
        productDeveloperUids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表 - 订单维度transaction视图

        API: /basicOpen/finance/profitReport/order/transcation/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限1000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            startDate: 开始时间 (Required)
            endDate: 结束时间 (Required)
            gmtModifiedStartDate: 修改开始时间，格式：yyyy-MM-dd HH:mm:ss (Optional)
            gmtModifiedEndDate: 修改结束时间，格式：yyyy-MM-dd HH:mm:ss (Optional)
            searchValue: 查询索引字段值 (Optional)
            sortField: 参与排序字段 (Optional)
            sortType: 排序方式 (Optional)
            FBM_FBM: 否 (Optional)
            principalUids: listing负责人 (Optional)
            productDeveloperUids: 开发负责人 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_ordertransaction(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "gmtModifiedStartDate": gmtModifiedStartDate,
            "gmtModifiedEndDate": gmtModifiedEndDate,
            "searchValue": searchValue,
            "sortField": sortField,
            "sortType": sortType,
            "FBM_FBM": FBM_FBM,
            "principalUids": principalUids,
            "productDeveloperUids": productDeveloperUids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/profitReport/order/transcation/list",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        start_time: str | None = None,
        end_time: str | None = None,
        search_value: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询请款池 - 货款现结

        API: /basicOpen/finance/requestFundsPool/purchase/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            search_value: 查询值 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "search_value": search_value,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/purchase/list",
            method="POST",
            req_body=params
        )



    async def get_settlement(
        self,
        access_token: str,
        amazonSellerIds: list[Any],
        sids: list[Any],
        filterBeginDate: str,
        filterEndDate: str,
        countryCodes: list[Any] | None = None,
        orderNumbers: list[Any] | None = None,
        shipmentNumbers: list[Any] | None = None,
        customNumbers: list[Any] | None = None,
        mskus: list[Any] | None = None,
        skus: list[Any] | None = None,
        productNames: list[Any] | None = None,
        trackCodes: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询发货结算报告

        API: /cost/center/api/settlement/report
        Method: POST

        Args:
            access_token: Access token for authentication
            amazonSellerIds: 亚马逊店铺id (Required)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            filterBeginDate: 开始日期，格式：Y-m-d，双闭区间 (Required)
            filterEndDate: 结束日期，格式：Y-m-d，双闭区间 (Required)
            countryCodes: 国家编码 (Optional)
            orderNumbers: 订单编号 (Optional)
            shipmentNumbers: 配送编号 (Optional)
            customNumbers: 自定义编号 (Optional)
            mskus: msku (Optional)
            skus: sku (Optional)
            productNames: 品名 (Optional)
            trackCodes: 物流追踪编码 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlement(token, ...)
            >>> print(result)
        """
        params = {
            "amazonSellerIds": amazonSellerIds,
            "sids": sids,
            "filterBeginDate": filterBeginDate,
            "filterEndDate": filterEndDate,
            "countryCodes": countryCodes,
            "orderNumbers": orderNumbers,
            "shipmentNumbers": shipmentNumbers,
            "customNumbers": customNumbers,
            "mskus": mskus,
            "skus": skus,
            "productNames": productNames,
            "trackCodes": trackCodes,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/api/settlement/report",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        start_time: str | None = None,
        end_time: str | None = None,
        search_value: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询请款池 - 货款月结

        API: /basicOpen/finance/requestFundsPool/inbound/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            search_value: 搜索值 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "start_time": start_time,
            "end_time": end_time,
            "search_value": search_value,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/inbound/list",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询请款池-其他应付款

        API: /basicOpen/finance/requestFundsPool/customFee/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_time: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_time: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
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
            "start_time": start_time,
            "end_time": end_time,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/customFee/list",
            method="POST",
            req_body=params
        )



    async def get_detaillist(
        self,
        access_token: str,
        offset: int,
        length: int,
        date_type: str,
        start_date: str,
        end_date: str,
        sids: list[Any] | None = None,
        other_fee_type_ids: list[Any] | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询费用明细列表

        API: /bd/fee/management/open/feeManagement/otherFee/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认20 (Required)
            date_type: 时间类型：gmt_create 创建日期，date 分摊日期 (Required)
            start_date: 开始时间，格式：Y-m-d (Required)
            end_date: 结束时间，格式：Y-m-d (Required)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            other_fee_type_ids: 费用类型id (Optional)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_detaillist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "other_fee_type_ids": other_fee_type_ids,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/list",
            method="POST",
            req_body=params
        )



    async def create(
        self,
        access_token: str,
        submit_type: int,
        is_request_pool: int,
        remark: str,
        fee_items: list[Any]
    ) -> dict[str, Any]:
        """
        创建费用单

        API: /bd/fee/management/open/feeManagement/otherFee/create
        Method: POST

        Args:
            access_token: Access token for authentication
            submit_type: 提交类型：1 暂存，2 提交 (Required)
            is_request_pool: 是否请款：0 否，1 是 (Required)
            remark: 费用单备注 (Required)
            fee_items: 费用明细项 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "submit_type": submit_type,
            "is_request_pool": is_request_pool,
            "remark": remark,
            "fee_items": fee_items
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/create",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        invoice_id: str,
        sid: int,
        offset: int | None = None,
        length: int | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询广告发票活动列表

        API: /bd/profit/report/open/report/ads/invoice/campaign/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认值0 (Optional)
            length: 分页大小，默认20 (Optional)
            invoice_id: 广告发票编号 (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "invoice_id": invoice_id,
            "sid": sid,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/ads/invoice/campaign/list",
            method="POST",
            req_body=params
        )



    async def get_settlementurl(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询settlement下载URL

        API: /bd/sp/api/open/settlement/export/url/get
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlementurl(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/settlement/export/url/get",
            method="GET",
            req_body=params
        )



    async def get_settlement_detail(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        countryCodes: list[Any] | None = None,
        sids: list[Any] | None = None,
        eventType: str | None = None,
        type: str | None = None,
        searchValue: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询结算中心 - 交易明细

        API: /bd/sp/api/open/settlement/transaction/detail/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            countryCodes: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            eventType: 来源，多个英文用逗号隔开 (Optional)
            type: 交易类型 (Optional)
            searchValue: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlement_detail(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "countryCodes": countryCodes,
            "sids": sids,
            "eventType": eventType,
            "type": type,
            "searchValue": searchValue
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/settlement/transaction/detail/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        invoice_start_time: str,
        invoice_end_time: str,
        offset: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None,
        mids: list[Any] | None = None,
        SPONSORED_BRANDS_VIDEO: Any | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询广告发票列表

        API: /bd/profit/report/open/report/ads/invoice/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认值0 (Optional)
            length: 分页大小，默认20 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            mids: 国家id (Optional)
            SPONSORED_BRANDS_VIDEO: 否 (Optional)
            invoice_start_time: 开始时间【发票开具时间】 (Required)
            invoice_end_time: 结束时间【发票开具时间】 (Required)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sids": sids,
            "mids": mids,
            "SPONSORED_BRANDS_VIDEO": SPONSORED_BRANDS_VIDEO,
            "invoice_start_time": invoice_start_time,
            "invoice_end_time": invoice_end_time,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/ads/invoice/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        settleMonth: str,
        sids: list[Any] | None = None,
        mids: list[Any] | None = None,
        currencyCode: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        应收报告-列表查询

        API: /bd/sp/api/open/monthly/receivable/report/list
        Method: POST

        Args:
            access_token: Access token for authentication
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            mids: 国家id (Optional)
            currencyCode: 币种code (Optional)
            settleMonth: 结算月,格式：Y-m (Required)
            offset: 分页偏移量， 默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sids": sids,
            "mids": mids,
            "currencyCode": currencyCode,
            "settleMonth": settleMonth,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/sp/api/open/monthly/receivable/report/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询请款单列表

        API: /basicOpen/finance/requestFunds/order/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            end_date: 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d (Optional)
            search_field: 搜索字段：purchase_order_sn 关联单据，order_sn 请款单号 (Optional)
            search_value: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "search_field": search_field,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFunds/order/list",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        endTime: str,
        startTime: str,
        length: int | None = None,
        offset: int | None = None,
        purchaserIds: list[Any] | None = None,
        searchField: str | None = None,
        searchFieldTime: str | None = None,
        searchValue: str | None = None,
        status: int | None = None,
        supplierIds: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询请款池-其他费用

        API: /basicOpen/finance/requestFundsPool/otherFee/list
        Method: POST

        Args:
            access_token: Access token for authentication
            endTime: 结束时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度 (Required)
            startTime: 开始时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度 (Required)
            length: 分页长度 (Optional)
            offset: 分页偏移量 (Optional)
            purchaserIds: 采购方ID列表，筛选指定采购方的其他费用 (Optional)
            searchField: 搜索字段，枚举值：order_sn-采购单号, create_username-采购员，配合searchValue使用 (Optional)
            searchFieldTime: 时间维度，枚举值：create_time-创建时间, close_time-付清时间，默认create_time (Optional)
            searchValue: 搜索值，根据searchField字段进行搜索，支持模糊查询 (Optional)
            status: 付款状态，枚举值：0-查询未付清, 1-查询已付清，不传默认查询全部 (Optional)
            supplierIds: 应付对象ID列表，筛选指定供应商的其他费用 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "endTime": endTime,
            "startTime": startTime,
            "length": length,
            "offset": offset,
            "purchaserIds": purchaserIds,
            "searchField": searchField,
            "searchFieldTime": searchFieldTime,
            "searchValue": searchValue,
            "status": status,
            "supplierIds": supplierIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/finance/requestFundsPool/otherFee/list",
            method="POST",
            req_body=params
        )



    async def get_profitreport_order(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        search_value: list[Any] | None = None,
        currency_code: str | None = None,
        RemovalShipment: Any | None = None,
        description: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-订单

        API: /bd/profit/report/open/report/order/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            start_date: 开始时间 (Required)
            end_date: 结束时间 (Required)
            search_value: 搜索的值 (Optional)
            currency_code: 币种code (Optional)
            RemovalShipment: 否 (Optional)
            description: 描述 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_order(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date,
            "search_value": search_value,
            "currency_code": currency_code,
            "RemovalShipment": RemovalShipment,
            "description": description
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/order/list",
            method="POST",
            req_body=params
        )



    async def get_info(  # noqa: F811
        self,
        access_token: str,
        invoice_id: str,
        sid: int
    ) -> dict[str, Any]:
        """
        查询广告发票基本信息

        API: /bd/profit/report/open/report/ads/invoice/detail
        Method: POST

        Args:
            access_token: Access token for authentication
            invoice_id: 广告发票编号 (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_info(token, ...)
            >>> print(result)
        """
        params = {
            "invoice_id": invoice_id,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/ads/invoice/detail",
            method="POST",
            req_body=params
        )



    async def get_profitreport_msku(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-MSKU

        API: /bd/profit/report/open/report/msku/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            searchField: 搜索值类型，seller_sku (Optional)
            searchValue: 搜索的值 (Optional)
            currencyCode: 币种code【默认原币种】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_msku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/msku/list",
            method="POST",
            req_body=params
        )



    async def get_profitreport_asin(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-ASIN

        API: /bd/profit/report/open/report/asin/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            searchField: 搜索值类型，ASIN (Optional)
            searchValue: 搜索的值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_asin(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/asin/list",
            method="POST",
            req_body=params
        )



    async def get_profitreport_sku(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        mids: list[Any] | None = None,
        sids: list[Any] | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        currencyCode: str | None = None
    ) -> dict[str, Any]:
        """
        查询利润报表-SKU

        API: /bd/profit/report/open/report/sku/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限10000 (Optional)
            mids: 站点id (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            searchField: 搜索值类型，local_sku (Optional)
            searchValue: 搜索的值 (Optional)
            currencyCode: 币种code (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_profitreport_sku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "searchField": searchField,
            "searchValue": searchValue,
            "currencyCode": currencyCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/sku/list",
            method="POST",
            req_body=params
        )



    async def get_inventorysummarydata(
        self,
        access_token: str,
        sellerIds: list[Any],
        queryType: int,
        startDate: str,
        endDate: str,
        fnskus: list[Any] | None = None,
        asins: list[Any] | None = None,
        mskus: list[Any] | None = None,
        disposition: str | None = None,
        locations: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询库存分类账summary数据

        API: /cost/center/ods/summary/query
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerIds: 亚马逊店铺id (Required)
            queryType: 查询维度：1 按月，2 按天 (Required)
            startDate: 统计起始日期：月维度：Y-m ，天维度：Y-m-d，闭区间 (Required)
            endDate: 统计结束日期：月维度：Y-m ，天维度：Y-m-d，闭区间 (Required)
            fnskus: fnsku列表 (Optional)
            asins: asin列表 (Optional)
            mskus: msku列表 (Optional)
            disposition: 库存属性：01 SELLABLE，02 UNSELLABLE，03 ALL (Optional)
            locations: 国家编码列表 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_inventorysummarydata(token, ...)
            >>> print(result)
        """
        params = {
            "sellerIds": sellerIds,
            "queryType": queryType,
            "startDate": startDate,
            "endDate": endDate,
            "fnskus": fnskus,
            "asins": asins,
            "mskus": mskus,
            "disposition": disposition,
            "locations": locations,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cost/center/ods/summary/query",
            method="GET",
            req_body=params
        )



    async def profitreportdata(
        self,
        access_token: str,
        date_month: str
    ) -> dict[str, Any]:
        """
        立即重算-利润报表数据

        API: /bd/profit/report/open/report/settle/compute/manual
        Method: POST

        Args:
            access_token: Access token for authentication
            date_month: 重算月份，格式：yyyy-MM (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.profitreportdata(token, ...)
            >>> print(result)
        """
        params = {
            "date_month": date_month
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/profit/report/open/report/settle/compute/manual",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询费用类型列表

        API: /bd/fee/management/open/feeManagement/otherFee/type
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/bd/fee/management/open/feeManagement/otherFee/type",
            method="POST",
            req_body=params
        )


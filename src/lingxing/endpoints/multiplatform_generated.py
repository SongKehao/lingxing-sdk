"""MultiPlatform API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class MultiPlatformEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def update_walmartinventory(
        self,
        access_token: str,
        queue_type: Any | None = None,
        data: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        Walmart修改库存

        API: /basicOpen/multiplatform/walmart/publishQueue
        Method: POST

        Args:
            access_token: Access token for authentication
            queue_type: 调整类型,可用值:1 (Optional)
            data: 响应数据 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_walmartinventory(token, ...)
            >>> print(result)
        """
        params = {
            "queue_type": queue_type,
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/walmart/publishQueue",
            method="POST",
            req_body=params
        )



    async def get_line(
        self,
        access_token: str,
        isParent: int,
        availableNumber: str | None = None,
        availableNumberCondition: int | None = None,
        brandIds: list[Any] | None = None,
        categoryIds: list[Any] | None = None,
        length: int | None = None,
        offset: int | None = None,
        pairingStatus: int | None = None,
        parentUniqueIds: list[Any] | None = None,
        price: str | None = None,
        priceCondition: int | None = None,
        principalUids: list[Any] | None = None,
        productUniqueId: Any | None = None,
        searchField: str | None = None,
        searchSingleValue: str | None = None,
        searchValues: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        statusList: list[Any] | None = None,
        storeIds: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        多平台-查询Line在线商品

        API: /basicOpen/multiplatform/line/list
        Method: POST

        Args:
            access_token: Access token for authentication
            isParent: 是否父体，枚举值：1-父体, 0-子体 (Required)
            availableNumber: 可用库存数，用于库存筛选 (Optional)
            availableNumberCondition: 库存筛选条件，枚举值：1-大于, 2-小于 (Optional)
            brandIds: 品牌ID列表 (Optional)
            categoryIds: 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来 (Optional)
            length: 分页长度，每页条数，最大200 (Optional)
            offset: 分页偏移量，从0开始 (Optional)
            pairingStatus: 配对状态，枚举值：0-未配对, 1-配对, null-全部 (Optional)
            parentUniqueIds: 父体全局唯一ID列表 (Optional)
            price: 金额，用于价格筛选 (Optional)
            priceCondition: 金额筛选条件，枚举值：1-大于, 2-小于 (Optional)
            principalUids: 商品负责人UID列表 (Optional)
            productUniqueId: 商品全局唯一ID (Optional)
            searchField: 搜索类型，枚举值：1-msku, 2-msku ID, 3-SKU, 4-品名 (Optional)
            searchSingleValue: 搜索值，单个模糊搜索，字符串类型 (Optional)
            searchValues: 搜索值，数组类型，多个精确搜索 (Optional)
            sortField: 排序字段，直接传返参的字段名 (Optional)
            sortType: 排序类型，枚举值：asc-升序, desc-降序 (Optional)
            statusList: 状态列表，枚举值：0-正常, 1-已删除 (Optional)
            storeIds: 店铺ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_line(token, ...)
            >>> print(result)
        """
        params = {
            "isParent": isParent,
            "availableNumber": availableNumber,
            "availableNumberCondition": availableNumberCondition,
            "brandIds": brandIds,
            "categoryIds": categoryIds,
            "length": length,
            "offset": offset,
            "pairingStatus": pairingStatus,
            "parentUniqueIds": parentUniqueIds,
            "price": price,
            "priceCondition": priceCondition,
            "principalUids": principalUids,
            "productUniqueId": productUniqueId,
            "searchField": searchField,
            "searchSingleValue": searchSingleValue,
            "searchValues": searchValues,
            "sortField": sortField,
            "sortType": sortType,
            "statusList": statusList,
            "storeIds": storeIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/line/list",
            method="POST",
            req_body=params
        )



    async def get_list_walmart_payment(
        self,
        access_token: str,
        new_report: int,
        store_id: list[Any]
    ) -> dict[str, Any]:
        """
        查询可用报告列表 - Walmart Payment

        API: /cepf/fms/openapi/walmartPayment/queryReport
        Method: POST

        Args:
            access_token: Access token for authentication
            new_report: 是否查询最新的报告：1 是，2 否 (Required)
            store_id: 店铺id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list_walmart_payment(token, ...)
            >>> print(result)
        """
        params = {
            "new_report": new_report,
            "store_id": store_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/fms/openapi/walmartPayment/queryReport",
            method="POST",
            req_body=params
        )



    async def get_ebaylist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        store_ids: list[Any] | None = None,
        site_code: list[Any] | None = None,
        listing_status: list[Any] | None = None,
        auto_restocks: list[Any] | None = None,
        listing_type: list[Any] | None = None,
        search_field: int | None = None,
        search_single_value: str | None = None,
        listing_time_field: int | None = None,
        listing_start_time: str | None = None,
        listing_end_time: str | None = None
    ) -> dict[str, Any]:
        """
        查询eBay在线商品列表

        API: /basicOpen/multiplatform/ebay/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，默认20，最大上限200 (Optional)
            store_ids: 店铺id (Optional)
            site_code: 站点code (Optional)
            listing_status: 销售状态 (Optional)
            auto_restocks: 是否自动补货：0:无补货规则，1:启用，2:停用 (Optional)
            listing_type: 销售类型：1:拍卖，2:固价，3:多属性 (Optional)
            search_field: 查询字段类型：1:msku，2:商品ID，3:sku，4:标题，5:品名，6:walmart gtin码 (Optional)
            search_single_value: 搜索值(字符串,单个模糊搜索) (Optional)
            listing_time_field: 查询时间类型：1:创建时间，2:结束时间 (Optional)
            listing_start_time: 开始时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】 (Optional)
            listing_end_time: 结束时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_ebaylist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "store_ids": store_ids,
            "site_code": site_code,
            "listing_status": listing_status,
            "auto_restocks": auto_restocks,
            "listing_type": listing_type,
            "search_field": search_field,
            "search_single_value": search_single_value,
            "listing_time_field": listing_time_field,
            "listing_start_time": listing_start_time,
            "listing_end_time": listing_end_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ebay/list",
            method="POST",
            req_body=params
        )



    async def order(
        self,
        access_token: str,
        platform_code: str,
        order_list: list[Any]
    ) -> dict[str, Any]:
        """
        合并订单

        API: /pb/mp/order/v2/mergeOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            platform_code: 平台code【不支持10007 Lazada、10011 TikTok、10012 MERCADO】 (Required)
            order_list: 系统单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "platform_code": platform_code,
            "order_list": order_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/mergeOrder",
            method="POST",
            req_body=params
        )



    async def create(
        self,
        access_token: str,
        pair_multi_platform_list: list[Any]
    ) -> dict[str, Any]:
        """
        批量添加、编辑多平台配对关系

        API: /pb/mp/listing/v2/pairMultiPlatform
        Method: POST

        Args:
            access_token: Access token for authentication
            pair_multi_platform_list: 配对数据，上限为5000条 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "pair_multi_platform_list": pair_multi_platform_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/listing/v2/pairMultiPlatform",
            method="POST",
            req_body=params
        )



    async def update_order(
        self,
        access_token: str,
        order_list: list[Any]
    ) -> dict[str, Any]:
        """
        编辑更新自发货订单

        API: /pb/mp/order/v2/updateOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_list: 订单列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_order(token, ...)
            >>> print(result)
        """
        params = {
            "order_list": order_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/updateOrder",
            method="POST",
            req_body=params
        )



    async def get_settlementprofitprofitreport_msku(
        self,
        access_token: str,
        offset: Any,
        length: Any,
        startDate: str,
        endDate: str,
        mids: str | None = None,
        sids: str | None = None,
        searchValue: str | None = None,
        developers: list[Any] | None = None,
        cids: list[Any] | None = None,
        bids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询结算利润（利润报表）-msku

        API: /basicOpen/multiplatform/profit/report/msku
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认1000 (Required)
            mids: 国家id，多个使用英文逗号分隔 (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】 (Optional)
            startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (Required)
            endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (Required)
            searchValue: 搜索值 (Optional)
            developers: 开发人 (Optional)
            cids: 分类 (Optional)
            bids: 品牌 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlementprofitprofitreport_msku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchValue": searchValue,
            "developers": developers,
            "cids": cids,
            "bids": bids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/profit/report/msku",
            method="POST",
            req_body=params
        )



    async def get_wayfairinventory(
        self,
        access_token: str,
        length: int,
        offset: int,
        storeIds: list[Any],
        warehouseIds: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        多平台-查询wayfair库存

        API: /basicOpen/multiplatform/wayfair/stockSearch
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数，必填，最大200 (Required)
            offset: 偏移量，必填，表示从第几条开始，最小为0 (Required)
            storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】 (Required)
            warehouseIds: 仓库ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_wayfairinventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "storeIds": storeIds,
            "warehouseIds": warehouseIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/wayfair/stockSearch",
            method="POST",
            req_body=params
        )



    async def create_temuinventory(
        self,
        access_token: str,
        platformCode: str,
        storeId: str,
        productUniqueId: str,
        quantity: str,
        warehouseId: str,
        warehouseName: str | None = None
    ) -> dict[str, Any]:
        """
        Temu修改库存

        API: /basicOpen/multiplatform/temu/createPublishQueue
        Method: POST

        Args:
            access_token: Access token for authentication
            platformCode: 平台代码 (Required)
            storeId: 店铺id (Required)
            productUniqueId: 商品uid (Required)
            quantity: 数量 (Required)
            warehouseId: 仓库ID (Required)
            warehouseName: 仓库名称 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_temuinventory(token, ...)
            >>> print(result)
        """
        params = {
            "platformCode": platformCode,
            "storeId": storeId,
            "productUniqueId": productUniqueId,
            "quantity": quantity,
            "warehouseId": warehouseId,
            "warehouseName": warehouseName
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/temu/createPublishQueue",
            method="POST",
            req_body=params
        )



    async def create_sheininventory(
        self,
        access_token: str,
        platformCode: str | None = None,
        storeId: str | None = None,
        productUniqueId: str | None = None,
        quantity: str | None = None,
        warehouseId: str | None = None,
        warehouseName: str | None = None
    ) -> dict[str, Any]:
        """
        Shein修改库存

        API: /basicOpen/multiplatform/shein/createPublishQueue
        Method: POST

        Args:
            access_token: Access token for authentication
            platformCode: 平台代码 (Optional)
            storeId: 店铺id (Optional)
            productUniqueId: 商品uid (Optional)
            quantity: 数量 (Optional)
            warehouseId: 仓库ID (Optional)
            warehouseName: 仓库名称 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_sheininventory(token, ...)
            >>> print(result)
        """
        params = {
            "platformCode": platformCode,
            "storeId": storeId,
            "productUniqueId": productUniqueId,
            "quantity": quantity,
            "warehouseId": warehouseId,
            "warehouseName": warehouseName
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/shein/createPublishQueue",
            method="POST",
            req_body=params
        )



    async def get_storeinfo(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        platform_code: list[Any] | None = None,
        is_sync: int | None = None,
        status: int | None = None
    ) -> dict[str, Any]:
        """
        查询多平台店铺信息

        API: /pb/mp/shop/v2/getSellerList
        Method: GET

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限200 (Optional)
            platform_code: 平台code：10001:AMAZON，10002:Shopify，10003:eBay，10004:Wish，10005:AliExpress，10006:Shopee，10007:Lazada，10008:Walmart，10009:自定义平台，10010:Wayfair，10011:TikTok，10012:MERCADO，10013:CDISCOUNT，10014:NEWEGG，10015:RAKUTEN，10016:SHOPLINE，10017:TEAPPLIX，10018:SHOPLAZZA，10019:UEESHOP，10020:COUPANG，10021:SHEIN，10022:Temu全托管，10024:Temu半托管，10025:OTTO，10026:OZON，10027:SHEIN全托管，10028:SHEIN半托管，10029:AliExpress半托管，10030:AliExpress全托管，10033:Qoo10，10034:Mirakl，10038:line shopping (Optional)
            is_sync: 店铺同步状态：1:启用，0:停用 (Optional)
            status: 店铺授权状态：1:正常授权，0:授权失败 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_storeinfo(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "platform_code": platform_code,
            "is_sync": is_sync,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/shop/v2/getSellerList",
            method="GET",
            req_body=params
        )



    async def get_walmart(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        store_ids: list[Any] | None = None,
        status: list[Any] | None = None,
        fulfillment_types: list[Any] | None = None,
        listing_time_field: int | None = None,
        listing_start_time: str | None = None,
        listing_end_time: str | None = None,
        search_field: int | None = None,
        search_single_value: str | None = None
    ) -> dict[str, Any]:
        """
        查询Walmart在线商品

        API: /basicOpen/multiplatform/walmart/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            store_ids: 店铺id (Optional)
            status: 状态：0:PUBLISHED，1:READY TO PUBLISH，2:IN PROGRESS，3:UNPUBLISHED，4:STAGE，5:SYSTEM PROBLEM (Optional)
            fulfillment_types: 发货方式：0:WFS Eligible，1:Walmart Fulfilled，2:Seller Fulfilled (Optional)
            listing_time_field: 搜索时间类型：1:创建时间，2:更新时间 (Optional)
            listing_start_time: 开始日期，Y-m-d，闭区间【开始结束时间不超过31天】 (Optional)
            listing_end_time: 结束日期，Y-m-d，闭区间【开始结束时间不超过31天】 (Optional)
            search_field: 搜索字段类型：1:MSKU，2:商品ID，3:SKU，4:标题 (Optional)
            search_single_value: 搜索值(字符串,单个模糊搜索) (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_walmart(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "store_ids": store_ids,
            "status": status,
            "fulfillment_types": fulfillment_types,
            "listing_time_field": listing_time_field,
            "listing_start_time": listing_start_time,
            "listing_end_time": listing_end_time,
            "search_field": search_field,
            "search_single_value": search_single_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/walmart/list",
            method="POST",
            req_body=params
        )



    async def get_tiktok(
        self,
        access_token: str,
        brandIds: list[Any] | None = None,
        categoryIds: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None,
        pairingStatus: int | None = None,
        searchField: str | None = None,
        platformStatus: list[Any] | None = None,
        storeIds: list[Any] | None = None,
        searchSingleValue: str | None = None,
        searchValues: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok在线商品

        API: /basicOpen/multiplatform/tiktok/list
        Method: POST

        Args:
            access_token: Access token for authentication
            brandIds: 品牌id列表 (Optional)
            categoryIds: 分类id列表 (Optional)
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限1000 (Optional)
            pairingStatus: 配对状态 (Optional)
            searchField: 搜索维度：1:标题，2:品名，5:平台SPU，7:MSKU ID，8:SKU，9:MSKU，10:SPU货号 (Optional)
            platformStatus: 状态：DRAFT，PENDING，FAILED，ACTIVATE，SELLER_DEACTIVATED，PLATFORM_DEACTIVATED，FREEZE，DELETED (Optional)
            storeIds: 店铺id列表 (Optional)
            searchSingleValue: 搜索值 (Optional)
            searchValues: 搜索值列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok(token, ...)
            >>> print(result)
        """
        params = {
            "brandIds": brandIds,
            "categoryIds": categoryIds,
            "offset": offset,
            "length": length,
            "pairingStatus": pairingStatus,
            "searchField": searchField,
            "platformStatus": platformStatus,
            "storeIds": storeIds,
            "searchSingleValue": searchSingleValue,
            "searchValues": searchValues
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/tiktok/list",
            method="POST",
            req_body=params
        )



    async def get_settlementprofitprofitreport_sku(
        self,
        access_token: str,
        offset: Any,
        length: Any,
        mids: str,
        startDate: str,
        endDate: str,
        sids: str | None = None,
        searchValue: str | None = None,
        developers: list[Any] | None = None,
        cids: list[Any] | None = None,
        bids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询结算利润（利润报表）-sku

        API: /basicOpen/multiplatform/profit/report/sku
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认1000 (Required)
            mids: 国家id，多个使用英文逗号分隔 (Required)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】 (Optional)
            startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (Required)
            endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (Required)
            searchValue: 搜索值 (Optional)
            developers: 开发人 (Optional)
            cids: 分类 (Optional)
            bids: 品牌 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlementprofitprofitreport_sku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate,
            "searchValue": searchValue,
            "developers": developers,
            "cids": cids,
            "bids": bids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/profit/report/sku",
            method="POST",
            req_body=params
        )



    async def get_walmart_reviewlist(
        self,
        access_token: str,
        endDate: str,
        startDate: str,
        pageNum: int | None = None,
        pageSize: int | None = None,
        ratings: list[Any] | None = None,
        searchDateField: str | None = None,
        searchField: str | None = None,
        searchValue: list[Any] | None = None,
        storeIds: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询Walmart Review列表

        API: /basicOpen/multiplatform/walmart/queryCommentList
        Method: POST

        Args:
            access_token: Access token for authentication
            endDate: 结束日期 (Required)
            pageNum: 页码 (Optional)
            pageSize: 每页大小 (Optional)
            ratings: 评分列表 (Optional)
            searchDateField: 搜索日期字段 (Optional)
            searchField: 搜索字段 (Optional)
            searchValue: 搜索值列表 (Optional)
            startDate: 开始日期 (Required)
            storeIds: 店铺ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_walmart_reviewlist(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "ratings": ratings,
            "searchDateField": searchDateField,
            "searchField": searchField,
            "searchValue": searchValue,
            "startDate": startDate,
            "storeIds": storeIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/walmart/queryCommentList",
            method="POST",
            req_body=params
        )



    async def get_listv2(
        self,
        access_token: str,
        platformCodes: list[Any],
        offset: int | None = None,
        length: int | None = None,
        timeField: int | None = None,
        startTime: str | None = None,
        endTime: str | None = None,
        pickingStatus: str | None = None,
        shippingListStatus: int | None = None,
        searchField: int | None = None,
        searchSingleValue: str | None = None,
        storeIds: list[Any] | None = None,
        updateStartTime: str | None = None,
        updateEndTime: str | None = None,
        isDelete: int | None = None
    ) -> dict[str, Any]:
        """
        查询平台仓发货单列表v2

        API: /basicOpen/multiplatform/query/shippingList
        Method: POST

        Args:
            access_token: Access token for authentication
            platformCodes: 平台代码：Walmart:10008，TikTok:10011，Temu:10022，Shein:10027 (Required)
            offset: 分页偏移量 (Optional)
            length: 分页长度 (Optional)
            timeField: 时间维度：1:创建时间，2:发货时间，3:开船时间，4:预计到港时间，5:实际妥投时间，6:实际发货时间 (Optional)
            startTime: 开始时间 (Optional)
            endTime: 结束时间 (Optional)
            pickingStatus: 拣货状态：1:已拣货，0:待拣货 (Optional)
            shippingListStatus: 发货单状态：0:待配货，1:待发货，2:已发货，3:已作废 (Optional)
            searchField: 搜索维度：1:MSKU，2:发货单号，7:货件单号，8:商品条码 (Optional)
            searchSingleValue: 模糊搜索值 (Optional)
            storeIds: 店铺id列表，对应查询多平台店铺信息接口对应字段【store_id】 (Optional)
            updateStartTime: 修改开始时间 (Optional)
            updateEndTime: 修改结束时间 (Optional)
            isDelete: 是否删除 0 未删除（默认） 1 已删除 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listv2(token, ...)
            >>> print(result)
        """
        params = {
            "platformCodes": platformCodes,
            "offset": offset,
            "length": length,
            "timeField": timeField,
            "startTime": startTime,
            "endTime": endTime,
            "pickingStatus": pickingStatus,
            "shippingListStatus": shippingListStatus,
            "searchField": searchField,
            "searchSingleValue": searchSingleValue,
            "storeIds": storeIds,
            "updateStartTime": updateStartTime,
            "updateEndTime": updateEndTime,
            "isDelete": isDelete
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/query/shippingList",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        global_order_no: list[Any]
    ) -> dict[str, Any]:
        """
        获取快速出库结果

        API: /pb/mp/order/v2/getFastOutboundResult
        Method: GET

        Args:
            access_token: Access token for authentication
            global_order_no: 系统单号数组，最大1000单 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "global_order_no": global_order_no
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/getFastOutboundResult",
            method="GET",
            req_body=params
        )



    async def delete(
        self,
        access_token: str,
        id: str
    ) -> dict[str, Any]:
        """
        删除暂存货件

        API: /basicOpen/multiplatform/deleteCargoStorage
        Method: POST

        Args:
            access_token: Access token for authentication
            id: WFS货件id，查询WFS货件列表 接口对应字段【id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete(token, ...)
            >>> print(result)
        """
        params = {
            "id": id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/deleteCargoStorage",
            method="POST",
            req_body=params
        )



    async def get_fullinventory(
        self,
        access_token: str,
        length: int,
        offset: int,
        selectTypeEnum: str,
        custom: dict[str, Any] | None = None,
        hideZeroStorage: int | None = None,
        storeIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询FULL库存

        API: /basicOpen/multiplatform/full/stockSearch
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数，必填，最大200条 (Required)
            offset: 分页偏移量，必填，从0开始 (Required)
            selectTypeEnum: 数据维度，COUNT_TYPE-数量 PRICE_TYPE-成本（必填） (Required)
            custom: 自定义搜索参数 (Optional)
            hideZeroStorage: 是否隐藏0库存，0不隐藏，1隐藏 (Optional)
            storeIdList: 店铺ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fullinventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "selectTypeEnum": selectTypeEnum,
            "custom": custom,
            "hideZeroStorage": hideZeroStorage,
            "storeIdList": storeIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/full/stockSearch",
            method="POST",
            req_body=params
        )



    async def get_settlementprofitprofitreport_order(
        self,
        access_token: str,
        offset: Any,
        length: Any,
        startDate: str,
        endDate: str,
        mids: str | None = None,
        sids: str | None = None,
        transactionTypeS: list[Any] | None = None,
        currencyCode: str | None = None,
        searchDateType: str | None = None,
        searchField: str | None = None,
        searchValue: str | None = None
    ) -> dict[str, Any]:
        """
        查询结算利润（利润报表）-订单

        API: /basicOpen/multiplatform/profit/report/order
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认200 (Required)
            mids: 国家id，多个使用英文逗号分隔 (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】 (Optional)
            transactionTypeS: 交易类型：0 销售，2 退货，4 退款，5 补发，6 调整，7 其他 (Optional)
            currencyCode: 币种code：原币种，USD，EUR，GBP，CNY (Optional)
            searchDateType: 时间筛选方式：1 下单时间，2 结算日期【默认】，3 发货日期 (Optional)
            startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (Required)
            endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (Required)
            searchField: 搜索值类型：msku MSKU，local_sku SKU，product_name，品名，platform_order_no 平台单号 (Optional)
            searchValue: 搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlementprofitprofitreport_order(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "transactionTypeS": transactionTypeS,
            "currencyCode": currencyCode,
            "searchDateType": searchDateType,
            "startDate": startDate,
            "endDate": endDate,
            "searchField": searchField,
            "searchValue": searchValue
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/profit/report/order",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        split_mod: int,
        global_order_no: str,
        order_item: list[Any]
    ) -> dict[str, Any]:
        """
        拆分订单

        API: /pb/mp/order/v2/splitOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            split_mod: 拆分模式：1 按商品拆分，2 按捆绑商品拆分 (Required)
            global_order_no: 系统单号 (Required)
            order_item: 订单数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "split_mod": split_mod,
            "global_order_no": global_order_no,
            "order_item": order_item
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/splitOrder",
            method="POST",
            req_body=params
        )



    async def get_wfsinventorylist(
        self,
        access_token: str,
        store_id: list[Any],
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询WFS库存列表

        API: /cepf/warehouse/api/openApi/queryWFSInventionPage
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_wfsinventorylist(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/warehouse/api/openApi/queryWFSInventionPage",
            method="POST",
            req_body=params
        )



    async def get_walmart_payment(
        self,
        access_token: str,
        store_id: list[Any],
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询报告详情 - Walmart Payment

        API: /cepf/fms/openapi/walmartPayment/queryPage
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15，上限200 (Optional)
            store_id: 店铺id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_walmart_payment(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "store_id": store_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/fms/openapi/walmartPayment/queryPage",
            method="POST",
            req_body=params
        )



    async def order_review(
        self,
        access_token: str,
        global_order_no: list[Any]
    ) -> dict[str, Any]:
        """
        审核发货

        API: /basicOpen/openapi/multiplatform/order/review
        Method: POST

        Args:
            access_token: Access token for authentication
            global_order_no: 系统单号列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order_review(token, ...)
            >>> print(result)
        """
        params = {
            "global_order_no": global_order_no
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/multiplatform/order/review",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        shippingIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        平台仓发货单拣货

        API: /basicOpen/multiplatform/shippingList/picking
        Method: POST

        Args:
            access_token: Access token for authentication
            shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "shippingIdList": shippingIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/shippingList/picking",
            method="POST",
            req_body=params
        )



    async def create_wfslist(
        self,
        access_token: str,
        store_id: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询WFS货件可添加商品列表

        API: /basicOpen/multiplatform/cargo/addCargoGoods/list
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_wfslist(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/cargo/addCargoGoods/list",
            method="POST",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        store_id: list[Any] | None = None,
        cargo_code: str | None = None,
        shipping_list_codes: list[Any] | None = None,
        shipping_list_status: int | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询平台仓发货单列表

        API: /cepf/warehouse/api/openApi/queryShippingListPage
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Optional)
            cargo_code: 货件单号 (Optional)
            shipping_list_codes: 发货单编号，上限100 (Optional)
            shipping_list_status: 发货单状态：0:待配货，1:待发货，2:已发货，3:已作废 (Optional)
            start_time: 开始时间【创建时间】，格式：Y-m-d，双闭区间 (Optional)
            end_time: 结束时间【创建时间】，格式：Y-m-d，双闭区间 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "cargo_code": cargo_code,
            "shipping_list_codes": shipping_list_codes,
            "shipping_list_status": shipping_list_status,
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/warehouse/api/openApi/queryShippingListPage",
            method="POST",
            req_body=params
        )



    async def get_shopify(
        self,
        access_token: str,
        store_ids: list[Any] | None = None,
        status: list[Any] | None = None,
        inventory_policy: list[Any] | None = None,
        type_id: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None,
        search_field: int | None = None,
        search_single_value: str | None = None,
        search_values: list[Any] | None = None,
        quantity: str | None = None,
        quantity_condition: int | None = None,
        price: Any | None = None,
        price_condition: int | None = None,
        listing_time_field: int | None = None,
        listing_start_time: str | None = None,
        listing_end_time: str | None = None
    ) -> dict[str, Any]:
        """
        查询Shopify在线商品

        API: /basicOpen/multiplatform/shopify/variantList
        Method: POST

        Args:
            access_token: Access token for authentication
            store_ids: 店铺Id (Optional)
            status: 状态：1:Active，2:Draft，3:Archived，4:Deleted (Optional)
            inventory_policy: 库存策略：1:不跟踪库存，2:缺货停止销售，3:缺货继续销售 (Optional)
            type_id: 分类Id (Optional)
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限1000 (Optional)
            search_field: 搜索维度 (Optional)
            search_single_value: 模糊搜索值 (Optional)
            search_values: 精确搜索列表，上限200个 (Optional)
            quantity: 库存数量 (Optional)
            quantity_condition: 库存数量大于或小于：1:大于，2:小于 (Optional)
            price: 售价 (Optional)
            price_condition: 售价大于或小于：1:大于，2:小于 (Optional)
            listing_time_field: 时间维度 (Optional)
            listing_start_time: 开始时间 (Optional)
            listing_end_time: 结束时间 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_shopify(token, ...)
            >>> print(result)
        """
        params = {
            "store_ids": store_ids,
            "status": status,
            "inventory_policy": inventory_policy,
            "type_id": type_id,
            "offset": offset,
            "length": length,
            "search_field": search_field,
            "search_single_value": search_single_value,
            "search_values": search_values,
            "quantity": quantity,
            "quantity_condition": quantity_condition,
            "price": price,
            "price_condition": price_condition,
            "listing_time_field": listing_time_field,
            "listing_start_time": listing_start_time,
            "listing_end_time": listing_end_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/shopify/variantList",
            method="POST",
            req_body=params
        )



    async def get_orderorderlist(
        self,
        access_token: str,
        offset: int,
        length: int,
        date_type: str | None = None,
        start_time: int | None = None,
        end_time: int | None = None
    ) -> dict[str, Any]:
        """
        查询订单管理订单列表

        API: /pb/mp/order/v2/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度，上限500 (Required)
            date_type: 时间类型：update_time:更新时间，global_purchase_time:订购时间，global_delivery_time:发货时间，global_payment_time:付款时间，delivery_time:平台发货时间（当且仅当传入平台单号或平台单名称查询时可不必传） (Optional)
            start_time: 开始时间，时间戳格式【单位：秒】，双开区间，当且仅当传入平台单号或平台单名称查询时可不必传，查询时间跨度不能超过31天 (Optional)
            end_time: 结束时间，时间戳格式【单位：秒】，双开区间，当且仅当传入平台单号或平台单名称查询时可不必传，查询时间跨度不能超过31天 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderorderlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "date_type": date_type,
            "start_time": start_time,
            "end_time": end_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/list",
            method="POST",
            req_body=params
        )



    async def update_order(  # noqa: F811
        self,
        access_token: str,
        orders: list[Any]
    ) -> dict[str, Any]:
        """
        更新订单客服备注

        API: /pb/mp/order/setRemark
        Method: POST

        Args:
            access_token: Access token for authentication
            orders: 系统订单列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_order(token, ...)
            >>> print(result)
        """
        params = {
            "orders": orders
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/setRemark",
            method="POST",
            req_body=params
        )



    async def get_temu(
        self,
        access_token: str,
        endTime: Any,
        startTime: Any,
        statusList: list[Any],
        storeIdList: list[Any],
        timeType: int,
        length: Any | None = None,
        offset: Any | None = None
    ) -> dict[str, Any]:
        """
        查询Temu货件

        API: /basicOpen/multiplatform/temu/cargo
        Method: POST

        Args:
            access_token: Access token for authentication
            endTime: yyyy-MM-dd (Required)
            length: 每页条数 (Optional)
            offset: 偏移量 (Optional)
            startTime: yyyy-MM-dd (Required)
            statusList: 待发货：0 ；待收货：1 ；已收货：2 ；已入库：3 ；已退货：4 ；已取消：5 ；部分收货：6 ;待申报（本地状态）7 (Required)
            storeIdList:  (Required)
            timeType: 1:创建时间 2：发货时间 3：收货时间 4：入库时间 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_temu(token, ...)
            >>> print(result)
        """
        params = {
            "endTime": endTime,
            "length": length,
            "offset": offset,
            "startTime": startTime,
            "statusList": statusList,
            "storeIdList": storeIdList,
            "timeType": timeType
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/temu/cargo",
            method="POST",
            req_body=params
        )



    async def order_preShipment(
        self,
        access_token: str,
        global_order_no: list[Any]
    ) -> dict[str, Any]:
        """
        预发货

        API: /basicOpen/openapi/multiplatform/order/preShipment
        Method: POST

        Args:
            access_token: Access token for authentication
            global_order_no: 系统单号列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order_preShipment(token, ...)
            >>> print(result)
        """
        params = {
            "global_order_no": global_order_no
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/multiplatform/order/preShipment",
            method="POST",
            req_body=params
        )



    async def get_fbtinventory(
        self,
        access_token: str,
        length: int,
        offset: int,
        storeIds: list[Any]
    ) -> dict[str, Any]:
        """
        多平台-查询FBT库存

        API: /basicOpen/multiplatform/fbt/stockSearch/v2
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数，必填，最大200 (Required)
            offset: 偏移量，必填，最小0 (Required)
            storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbtinventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "storeIds": storeIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/fbt/stockSearch/v2",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        order_number_list: str
    ) -> dict[str, Any]:
        """
        订单发货

        API: /basicOpen/selfShipmentOrder/deliveryGoods
        Method: POST

        Args:
            access_token: Access token for authentication
            order_number_list: 系统单号列表，多个使用英文逗号分隔，上限100 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "order_number_list": order_number_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/selfShipmentOrder/deliveryGoods",
            method="POST",
            req_body=params
        )



    async def get_settlementprofitprofitreport_store(
        self,
        access_token: str,
        offset: Any,
        length: Any,
        startDate: str,
        endDate: str,
        mids: str | None = None,
        sids: str | None = None
    ) -> dict[str, Any]:
        """
        查询结算利润（利润报表）-店铺

        API: /basicOpen/multiplatform/profit/report/seller
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Required)
            length: 分页长度，默认1000 (Required)
            mids: 国家id，多个使用英文逗号分隔 (Optional)
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】 (Optional)
            startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (Required)
            endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_settlementprofitprofitreport_store(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "mids": mids,
            "sids": sids,
            "startDate": startDate,
            "endDate": endDate
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/profit/report/seller",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        order_list: list[Any]
    ) -> dict[str, Any]:
        """
        编辑订单

        API: /pb/mp/order/editOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_list: 订单列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "order_list": order_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/editOrder",
            method="POST",
            req_body=params
        )



    async def wfs(
        self,
        access_token: str,
        store_id: str,
        cargo_goods_list: list[Any],
        return_address: dict[str, Any],
        cargo_remark: str | None = None,
        inbound_order_id: str | None = None
    ) -> dict[str, Any]:
        """
        WFS货件暂存

        API: /basicOpen/multiplatform/cargo/storage
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Required)
            cargo_goods_list: 货件包含的商品 (Required)
            cargo_remark: 货件备注 (Optional)
            inbound_order_id: 入库订单id (Optional)
            return_address: 退件地址，查询退件地址列表 接口获取 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.wfs(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "cargo_goods_list": cargo_goods_list,
            "cargo_remark": cargo_remark,
            "inbound_order_id": inbound_order_id,
            "return_address": return_address
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/cargo/storage",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        pkg_real_weight: str,
        pkg_real_weight_unit: str,
        order_number: str | None = None,
        wo_number: str | None = None,
        sync_product_gross_weight: str | None = None
    ) -> dict[str, Any]:
        """
        订单称重

        API: /erp/sc/routing/wms/order/setOrderWeighed
        Method: POST

        Args:
            access_token: Access token for authentication
            order_number: 系统单号 与销售出库单二选一 (Optional)
            wo_number: 销售出库单 与系统单号二选一 (Optional)
            pkg_real_weight: 重量 (Required)
            pkg_real_weight_unit: 单位 支持 g,kg,oz,lb (Required)
            sync_product_gross_weight: 一单一件同步重量到产品模块 0:否,1:是 默认否 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "order_number": order_number,
            "wo_number": wo_number,
            "pkg_real_weight": pkg_real_weight,
            "pkg_real_weight_unit": pkg_real_weight_unit,
            "sync_product_gross_weight": sync_product_gross_weight
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/wms/order/setOrderWeighed",
            method="POST",
            req_body=params
        )



    async def create_order(
        self,
        access_token: str,
        platform_code: int,
        store_id: str,
        orders: list[Any]
    ) -> dict[str, Any]:
        """
        创建订单

        API: /pb/mp/order/v2/create
        Method: POST

        Args:
            access_token: Access token for authentication
            platform_code: 平台code (Required)
            store_id: 店铺id (Required)
            orders: 订单列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_order(token, ...)
            >>> print(result)
        """
        params = {
            "platform_code": platform_code,
            "store_id": store_id,
            "orders": orders
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/create",
            method="POST",
            req_body=params
        )



    async def get_wfslist(
        self,
        access_token: str,
        store_id: list[Any] | None = None,
        cargo_status_list: list[Any] | None = None,
        inbound_order_id: str | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        update_time_ge: str | None = None,
        update_time_le: str | None = None,
        cargo_update_time_ge: str | None = None,
        cargo_update_time_le: str | None = None
    ) -> dict[str, Any]:
        """
        查询WFS货件列表

        API: /cepf/warehouse/api/openApi/queryWFSCargoPage
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Optional)
            cargo_status_list: 货件平台状态：0:PENDING_SHIPMENT_DETAILS，1:AWAITING_DELIVERY，2:RECEIVING_IN_PROGRESS，3:CLOSED，4:CANCELLED (Optional)
            inbound_order_id: 入库订单编号 (Optional)
            start_time: 开始时间【创建时间】，格式：Y-m-d，双闭区间 (Optional)
            end_time: 结束时间【创建时间】，格式：Y-m-d，双闭区间 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认15，上限200 (Optional)
            update_time_ge: 货件更新开始时间，格式：yyyy-MM-dd HH:mm:SS (Optional)
            update_time_le: 货件更新结束时间，格式：yyyy-MM-dd HH:mm:SS (Optional)
            cargo_update_time_ge: 货件平台更新时间开始 格式:yyyy-MM-dd HH:mm:ss (Optional)
            cargo_update_time_le: 货件平台更新时间结束 格式:yyyy-MM-dd HH:mm:ss (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_wfslist(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "cargo_status_list": cargo_status_list,
            "inbound_order_id": inbound_order_id,
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "length": length,
            "update_time_ge": update_time_ge,
            "update_time_le": update_time_le,
            "cargo_update_time_ge": cargo_update_time_ge,
            "cargo_update_time_le": cargo_update_time_le
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/warehouse/api/openApi/queryWFSCargoPage",
            method="POST",
            req_body=params
        )



    async def update(
        self,
        access_token: str,
        remarkContent: str,
        shippingListCode: str
    ) -> dict[str, Any]:
        """
        修改平台仓发货单备注

        API: /cepf/warehouse/api/openApi/editPlatfromShippingRemark
        Method: POST

        Args:
            access_token: Access token for authentication
            remarkContent: 备注内容 (Required)
            shippingListCode: 平台单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update(token, ...)
            >>> print(result)
        """
        params = {
            "remarkContent": remarkContent,
            "shippingListCode": shippingListCode
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepf/warehouse/api/openApi/editPlatfromShippingRemark",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        order_list: list[Any]
    ) -> dict[str, Any]:
        """
        标记订单不发货

        API: /pb/mp/order/v2/cancelOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            order_list: 系统单号列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "order_list": order_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/cancelOrder",
            method="POST",
            req_body=params
        )



    async def get_temu(  # noqa: F811
        self,
        access_token: str,
        searchField: str,
        brandIds: list[Any] | None = None,
        categoryIds: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None,
        pairingStatus: int | None = None,
        status: int | None = None,
        storeIds: list[Any] | None = None,
        searchValues: list[Any] | None = None,
        searchSingleValue: str | None = None
    ) -> dict[str, Any]:
        """
        查询Temu在线商品

        API: /basicOpen/multiplatform/temu/list
        Method: POST

        Args:
            access_token: Access token for authentication
            brandIds: 品牌id列表 (Optional)
            categoryIds: 分类id列表 (Optional)
            offset: 分页偏移量 (Optional)
            length: 分页长度，上限1000 (Optional)
            pairingStatus: 配对状态：0:未配对，1:已配对 (Optional)
            searchField: 搜索维度：1:标题，2:品名，4:SKC货号，5:平台SPU，6:平台SKC，7:MSKU ID，8:SKU，9:MSKU (Required)
            status: 状态：0:删除，2:正常 (Optional)
            storeIds: 店铺id列表 (Optional)
            searchValues: 精确搜索值列表 (Optional)
            searchSingleValue: 模糊搜索值 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_temu(token, ...)
            >>> print(result)
        """
        params = {
            "brandIds": brandIds,
            "categoryIds": categoryIds,
            "offset": offset,
            "length": length,
            "pairingStatus": pairingStatus,
            "searchField": searchField,
            "status": status,
            "storeIds": storeIds,
            "searchValues": searchValues,
            "searchSingleValue": searchSingleValue
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/temu/list",
            method="POST",
            req_body=params
        )



    async def get_orderlist(
        self,
        access_token: str,
        dateType: int,
        startDate: str,
        endDate: str,
        deliveryTypeList: list[Any] | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        platformCodeList: list[Any] | None = None,
        searchMultiValue: list[Any] | None = None,
        searchSingleValue: str | None = None,
        searchType: int | None = None,
        siteCodeList: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        statusList: list[Any] | None = None,
        storeIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询平台订单列表

        API: /cepfPlatformOrder/open-api/newPlatformOrder/list
        Method: POST

        Args:
            access_token: Access token for authentication
            dateType: 时间类型 0.平台数据变动时间 1.订购时间 2.订购时间-北京 3.支付时间 4.支付时间-北京 5.发货时间 6.发货时间-北京 (Required)
            deliveryTypeList: 发货类型: 0-自发货 1-平台发货 2-部分自发货 (Optional)
            pageNum: 查询起始位置 (Optional)
            pageSize: 分页大小 (Optional)
            platformCodeList: 平台CODE，目前仅支持 TikTok、TEMU 半托管、Line Shopping、Lazada、Shopee、Shopify、Walmart、Wayfair 平台 (Optional)
            searchMultiValue: 多个精确搜索查询值 (Optional)
            searchSingleValue: 单个模糊搜索查询值 (Optional)
            searchType: 搜索查询类型：1：sku，2：品名，3：msku 4.商品id 5.平台单号 6.参考号 7.商品标题 (Optional)
            siteCodeList: 站点列表 (Optional)
            sortField: 排序字段列表字段支持：purchaseTime，paymentTime，platformOrderModifiedTime,deliveryTime (Optional)
            sortType: 升降序 asc desc (Optional)
            startDate: 开始时间，闭区间 格式：2025-10-22 00:00:01 (Required)
            endDate: 结束时间，闭区间 格式：2025-10-22 20:00:01 (Required)
            statusList: 平台单状态的编码 平台订单状态枚举 (Optional)
            storeIdList: 店铺唯一标识 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderlist(token, ...)
            >>> print(result)
        """
        params = {
            "dateType": dateType,
            "deliveryTypeList": deliveryTypeList,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "platformCodeList": platformCodeList,
            "searchMultiValue": searchMultiValue,
            "searchSingleValue": searchSingleValue,
            "searchType": searchType,
            "siteCodeList": siteCodeList,
            "sortField": sortField,
            "sortType": sortType,
            "startDate": startDate,
            "endDate": endDate,
            "statusList": statusList,
            "storeIdList": storeIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/cepfPlatformOrder/open-api/newPlatformOrder/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        length: int | None = None,
        offset: int | None = None,
        msku: list[Any] | None = None,
        sku: list[Any] | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        platform_codes: list[Any] | None = None,
        store_ids: list[Any] | None = None,
        use_cursor: bool | None = None,
        cursor_id: bool | None = None
    ) -> dict[str, Any]:
        """
        查询多平台配对列表

        API: /pb/mp/listing/v2/getPairList
        Method: GET

        Args:
            access_token: Access token for authentication
            length: 分页条数 (Optional)
            offset: 分页偏移量 (Optional)
            msku: MSKU (Optional)
            sku: 本地SKU (Optional)
            start_time: 操作开始时间，闭区间 (Optional)
            end_time: 操作结束时间，开区间 (Optional)
            platform_codes: 平台码 (Optional)
            store_ids: 店铺id (Optional)
            use_cursor: 分页游标，默认为fasle，如配对数据多时，强烈建议您使用分页游标的方式分页，可加快接口响应速度 (Optional)
            cursor_id: 游标id, 当分页游标为true时，该字段必填 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "msku": msku,
            "sku": sku,
            "start_time": start_time,
            "end_time": end_time,
            "platform_codes": platform_codes,
            "store_ids": store_ids,
            "use_cursor": use_cursor,
            "cursor_id": cursor_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/listing/v2/getPairList",
            method="GET",
            req_body=params
        )



    async def get_aliexpress(
        self,
        access_token: str,
        isParent: int,
        length: int,
        brandIds: list[Any] | None = None,
        categoryIds: list[Any] | None = None,
        end: str | None = None,
        offset: int | None = None,
        pairingStatus: int | None = None,
        platformCodeList: list[Any] | None = None,
        price: int | None = None,
        priceCondition: int | None = None,
        principalUids: list[Any] | None = None,
        productTypeList: list[Any] | None = None,
        productUniqueId: Any | None = None,
        productUniqueIdList: list[Any] | None = None,
        quantity: int | None = None,
        quantityCondition: int | None = None,
        searchField: int | None = None,
        searchSingleValue: str | None = None,
        searchValues: list[Any] | None = None,
        sortField: str | None = None,
        sortType: str | None = None,
        start: str | None = None,
        statusList: list[Any] | None = None,
        storeIds: list[Any] | None = None,
        storeType: int | None = None
    ) -> dict[str, Any]:
        """
        查询AliExpress在线商品 - 托管模式

        API: /basicOpen/multiplatform/aliexpress/list/v2
        Method: POST

        Args:
            access_token: Access token for authentication
            isParent: 是否父体，必填，枚举值：1-父体, 0-子体 (Required)
            length: 分页长度，必填，每页条数 (Required)
            brandIds: 品牌ID列表 (Optional)
            categoryIds: 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来 (Optional)
            end: 结束时间，格式：yyyy-MM-dd (Optional)
            offset: 分页偏移量，必填，从0开始 (Optional)
            pairingStatus: 配对状态，枚举值：0-未配对, 1-配对, null-全部 (Optional)
            platformCodeList: 平台编码列表 (Optional)
            price: 供货价金额 (Optional)
            priceCondition: 供货价金额筛选条件，枚举值：1-大于, 2-小于 (Optional)
            principalUids: 商品负责人UID列表 (Optional)
            productTypeList: 发货模式列表，枚举值：0-仓发, 1-JIT, 2-海外备仓 (Optional)
            productUniqueId: 商品全局唯一ID (Optional)
            productUniqueIdList: 父体唯一ID列表 (Optional)
            quantity: 库存数 (Optional)
            quantityCondition: 库存筛选条件，枚举值：1-大于, 2-小于 (Optional)
            searchField: 搜索类型，枚举值：1-msku, 2-商品ID, 3-SKU, 4-品名, 5-SKU, 6-品名, 7-标题 (Optional)
            searchSingleValue: 搜索值，单个模糊搜索 (Optional)
            searchValues: 搜索值，数组，多个精确搜索 (Optional)
            sortField: 排序字段，直接传返参的字段名 (Optional)
            sortType: 排序类型，枚举值：asc-升序, desc-降序 (Optional)
            start: 开始时间，格式：yyyy-MM-dd (Optional)
            statusList: 状态列表，枚举值：S1-待售, S2-可售 (Optional)
            storeIds: 店铺ID列表 (Optional)
            storeType: 店铺类型，枚举值：半托管, 全托管, 海外托管 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_aliexpress(token, ...)
            >>> print(result)
        """
        params = {
            "isParent": isParent,
            "length": length,
            "brandIds": brandIds,
            "categoryIds": categoryIds,
            "end": end,
            "offset": offset,
            "pairingStatus": pairingStatus,
            "platformCodeList": platformCodeList,
            "price": price,
            "priceCondition": priceCondition,
            "principalUids": principalUids,
            "productTypeList": productTypeList,
            "productUniqueId": productUniqueId,
            "productUniqueIdList": productUniqueIdList,
            "quantity": quantity,
            "quantityCondition": quantityCondition,
            "searchField": searchField,
            "searchSingleValue": searchSingleValue,
            "searchValues": searchValues,
            "sortField": sortField,
            "sortType": sortType,
            "start": start,
            "statusList": statusList,
            "storeIds": storeIds,
            "storeType": storeType
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/aliexpress/list/v2",
            method="POST",
            req_body=params
        )



    async def get_coupanginventory(
        self,
        access_token: str,
        length: int,
        offset: int,
        storeIds: list[Any]
    ) -> dict[str, Any]:
        """
        多平台-查询Coupang库存

        API: /basicOpen/multiplatform/coupang/stockSearch
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数，必填 (Required)
            offset: 偏移量，必填 (Required)
            storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_coupanginventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "storeIds": storeIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/coupang/stockSearch",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        shippingIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        平台仓发货单发货

        API: /basicOpen/multiplatform/shippingList/delivery
        Method: POST

        Args:
            access_token: Access token for authentication
            shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "shippingIdList": shippingIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/shippingList/delivery",
            method="POST",
            req_body=params
        )



    async def get_statisticslistv2(
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        result_type: str,
        date_unit: str,
        data_type: str,
        page: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询销量统计列表v2

        API: /basicOpen/platformStatisticsV2/saleStat/pageList
        Method: POST

        Args:
            access_token: Access token for authentication
            start_date: 开始日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            end_date: 结束日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天 (Required)
            result_type: 汇总类型：1:销量，2:订单量，3:销售额 (Required)
            date_unit: 统计时间指标：1:年，2:月，3:周，4:日 (Required)
            page: 分页页码，默认1 (Optional)
            length: 分页大小，默认20 (Optional)
            data_type: 统计数据维度：1:ASIN，2:父体，3:MSKU，4:SKU，5:SPU，6:店铺 (Required)
            sids: 店铺id，多个使用英文逗号分隔。如果id属于亚马逊店铺id，则对应查询亚马逊店铺列表接口对应字段【sid】；如果id属于多平台店铺id，则对应查询多平台店铺信息接口对应字段【store_id】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_statisticslistv2(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "result_type": result_type,
            "date_unit": date_unit,
            "page": page,
            "length": length,
            "data_type": data_type,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/platformStatisticsV2/saleStat/pageList",
            method="POST",
            req_body=params
        )



    async def get_shein(
        self,
        access_token: str,
        brandIds: list[Any] | None = None,
        categoryIds: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None,
        pairingStatus: int | None = None,
        searchField: str | None = None,
        status: int | None = None,
        storeIds: list[Any] | None = None,
        searchSingleValue: str | None = None,
        searchValues: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询Shein在线商品

        API: /basicOpen/multiplatform/shein/list
        Method: POST

        Args:
            access_token: Access token for authentication
            brandIds: 品牌ID列表 (Optional)
            categoryIds: 分类ID列表 (Optional)
            offset: 偏移量 (Optional)
            length: 分页长度，上限1000 (Optional)
            pairingStatus: 配对状态：0:未配对，1:已配对 (Optional)
            searchField: 搜索字段：1:标题，2:品名，3:SPU货号，4:SKC货号，5:平台SPU，6:平台SKC，7:MSKU ID，8:SKU，9:MSKU (Optional)
            status: 状态：0:删除，1:在售，2:停售 (Optional)
            storeIds: 店铺ID列表 (Optional)
            searchSingleValue: 单一值搜索 (Optional)
            searchValues: 精确搜索值列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_shein(token, ...)
            >>> print(result)
        """
        params = {
            "brandIds": brandIds,
            "categoryIds": categoryIds,
            "offset": offset,
            "length": length,
            "pairingStatus": pairingStatus,
            "searchField": searchField,
            "status": status,
            "storeIds": storeIds,
            "searchSingleValue": searchSingleValue,
            "searchValues": searchValues
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/shein/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        store_id: str
    ) -> dict[str, Any]:
        """
        查询退件地址列表

        API: /basicOpen/multiplatform/address/returnAddressList
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: 店铺id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/address/returnAddressList",
            method="POST",
            req_body=params
        )



    async def v2_fastOutbound(
        self,
        access_token: str,
        package: list[Any]
    ) -> dict[str, Any]:
        """
        快速出库

        API: /pb/mp/order/v2/fastOutbound
        Method: POST

        Args:
            access_token: Access token for authentication
            package: 出库包裹信息，最多1000个订单 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.v2_fastOutbound(token, ...)
            >>> print(result)
        """
        params = {
            "package": package
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/v2/fastOutbound",
            method="POST",
            req_body=params
        )



    async def get_fbsinventory(
        self,
        access_token: str,
        length: int,
        offset: int,
        storeIds: list[Any],
        hideZeroStorage: Any | None = None,
        whsIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        多平台-查询FBS库存

        API: /basicOpen/multiplatform/fbs/stockSearch
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数，必填，最大200 (Required)
            offset: 偏移量，必填 (Required)
            storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】 (Required)
            hideZeroStorage: 是否隐藏0库存，默认0，枚举值：0-不隐藏，1-隐藏 (Optional)
            whsIdList: 仓库ID列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fbsinventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "storeIds": storeIds,
            "hideZeroStorage": hideZeroStorage,
            "whsIdList": whsIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/fbs/stockSearch",
            method="POST",
            req_body=params
        )



    async def get_temuinventory(
        self,
        access_token: str,
        storeIdList: list[Any],
        length: Any | None = None,
        offset: Any | None = None
    ) -> dict[str, Any]:
        """
        查询Temu库存

        API: /basicOpen/multiplatform/fbt/stockSearch
        Method: POST

        Args:
            access_token: Access token for authentication
            length: 每页条数 (Optional)
            offset: 偏移量 (Optional)
            storeIdList: 店铺Id集合 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_temuinventory(token, ...)
            >>> print(result)
        """
        params = {
            "length": length,
            "offset": offset,
            "storeIdList": storeIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/fbt/stockSearch",
            method="POST",
            req_body=params
        )



    async def inventory(
        self,
        access_token: str,
        shippingIdList: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        平台仓发货单分配库存

        API: /basicOpen/multiplatform/allocate/stock
        Method: POST

        Args:
            access_token: Access token for authentication
            shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.inventory(token, ...)
            >>> print(result)
        """
        params = {
            "shippingIdList": shippingIdList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/allocate/stock",
            method="POST",
            req_body=params
        )



    async def temu(
        self,
        access_token: str,
        decryptSnList: list[Any]
    ) -> dict[str, Any]:
        """
        批量TEMU地址解密

        API: /basicOpen/temu/temuAddressDecrypt
        Method: POST

        Args:
            access_token: Access token for authentication
            decryptSnList: 系统单号数组 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.temu(token, ...)
            >>> print(result)
        """
        params = {
            "decryptSnList": decryptSnList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/temu/temuAddressDecrypt",
            method="POST",
            req_body=params
        )



    async def get_sp(
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 平台

        API: /basicOpen/multiplatform/ads/reportPlatformSpList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportPlatformSpList",
            method="GET",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        orderType: str | None = None,
        adDatePicker: list[Any] | None = None,
        advertiserIds: list[Any] | None = None,
        campaignType: list[Any] | None = None,
        endDate: str | None = None,
        pageSize: int | None = None,
        campaignIds: list[Any] | None = None,
        orderField: str | None = None,
        day: int | None = None,
        pageNum: int | None = None,
        startDate: str | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 页面类型

        API: /basicOpen/multiplatform/ads/queryPageTypeSPList
        Method: GET

        Args:
            access_token: Access token for authentication
            orderType: orderType (Optional)
            adDatePicker: adDatePicker（日期格式：yyyy-MM-dd） (Optional)
            advertiserIds: advertiserIds列表 (Optional)
            campaignType: campaignType列表 (Optional)
            endDate: 结束日期 (Optional)
            pageSize: 每页大小 (Optional)
            campaignIds: campaignIds列表 (Optional)
            orderField: orderField (Optional)
            day: day (Optional)
            pageNum: 页码 (Optional)
            startDate: 开始日期 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "orderType": orderType,
            "adDatePicker": adDatePicker,
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "pageSize": pageSize,
            "campaignIds": campaignIds,
            "orderField": orderField,
            "day": day,
            "pageNum": pageNum,
            "startDate": startDate
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryPageTypeSPList",
            method="GET",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        day: int,
        endDate: str,
        operationSourceType: str,
        pageNum: int,
        pageSize: int,
        paging: bool,
        startDate: str,
        campaignIds: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 广告活动

        API: /basicOpen/multiplatform/ads/queryCampaignSpList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：1.查询sp广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto；2.查询sb广告报告必须且只能携带sba；3.查询sv广告报告必须且只能携带video (Required)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30 (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            operationSourceType: 操作来源，openapi调用必传gateway，前端传web (Required)
            pageNum: 页码，分页时的页码，从1开始 (Required)
            pageSize: 每页大小，分页时每页显示的记录数，openapi必传且小于2000 (Required)
            paging: 是否分页，openapi必填true (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "day": day,
            "endDate": endDate,
            "operationSourceType": operationSourceType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "orderField": orderField,
            "orderType": orderType,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryCampaignSpList",
            method="GET",
            req_body=params
        )



    async def get_tiktok_gmv_max_storelist(
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询TikTok-GMV MAX-店铺列表

        API: /basicOpen/multiplatform/ads/queryGmvStoreList
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok_gmv_max_storelist(token, ...)
            >>> print(result)
        """
        params = {

        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryGmvStoreList",
            method="POST",
            req_body=params
        )



    async def get_sv(
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 平台

        API: /basicOpen/multiplatform/ads/reportPlatformSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportPlatformSvList",
            method="GET",
            req_body=params
        )



    async def get_tiktok_gmv_max(
        self,
        access_token: str,
        endDate: str,
        length: int,
        page: int,
        startDate: str,
        advertiserIds: list[Any] | None = None,
        gmvMaxPromotionTypeCodes: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        ownerBcIds: list[Any] | None = None,
        status: list[Any] | None = None,
        storeIds: list[Any] | None = None,
        summaryCurrency: str | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-GMV MAX-广告帐号

        API: /basicOpen/multiplatform/ads/queryGmvAdvertiserReportList
        Method: POST

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            length: 每页条数，必填，小于2000 (Required)
            page: 页码，必填，从1开始 (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            advertiserIds: 广告账号ID列表，Long数组，用于筛选特定广告账号 (Optional)
            gmvMaxPromotionTypeCodes: GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV (Optional)
            orderField: 排序字段名称，如：cost, orders, roi (Optional)
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序 (Optional)
            ownerBcIds: 广告主账号ID列表，Long数组，业务负责人的BC ID列表 (Optional)
            status: 广告账号状态编码列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户 (Optional)
            storeIds: 店铺ID列表，Long数组，用于筛选特定店铺的数据 (Optional)
            summaryCurrency: 汇总币种编码，默认USD，用于统一汇总不同币种的数据 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok_gmv_max(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "page": page,
            "startDate": startDate,
            "advertiserIds": advertiserIds,
            "gmvMaxPromotionTypeCodes": gmvMaxPromotionTypeCodes,
            "orderField": orderField,
            "orderType": orderType,
            "ownerBcIds": ownerBcIds,
            "status": status,
            "storeIds": storeIds,
            "summaryCurrency": summaryCurrency
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryGmvAdvertiserReportList",
            method="POST",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        day: int,
        endDate: str,
        operationSourceType: str,
        pageNum: int,
        pageSize: int,
        paging: bool,
        startDate: str,
        campaignIds: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 广告组

        API: /basicOpen/multiplatform/ads/queryGroupSpList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，必填，BigInteger数组，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，必填，String数组，枚举值：sponsoredProducts-manual-SP手动, sponsoredProducts-auto-SP自动, sba-SB品牌广告, video-SV视频广告。注意：1.查询sp广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto；2.查询sb广告报告必须且只能携带sba；3.查询sv广告报告必须且只能携带video (Required)
            day: 归因天数，必填，数据归因天数，枚举值：3, 14, 30 (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            operationSourceType: 操作来源，必填，openapi调用必传gateway，前端传web (Required)
            pageNum: 页码，必填，分页时的页码，从1开始 (Required)
            pageSize: 每页大小，必填，分页时每页显示的记录数，openapi必传且小于2000 (Required)
            paging: 是否分页，必填，openapi必填true (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC (Optional)
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name） (Optional)
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "day": day,
            "endDate": endDate,
            "operationSourceType": operationSourceType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "orderField": orderField,
            "orderType": orderType,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryGroupSpList",
            method="GET",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 关键词

        API: /basicOpen/multiplatform/ads/reportKeywordSpList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text） (Optional)
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportKeywordSpList",
            method="GET",
            req_body=params
        )



    async def get_sv(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        companyId: int | None = None,
        day: int | None = None,
        operationSourceType: str | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        pageType: list[Any] | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 页面类型

        API: /basicOpen/multiplatform/ads/queryReportPageTypeSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            companyId: 公司ID (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            operationSourceType: 操作来源，默认网页操作 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            pageType: 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "companyId": companyId,
            "day": day,
            "operationSourceType": operationSourceType,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "pageType": pageType,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryReportPageTypeSvList",
            method="GET",
            req_body=params
        )



    async def get_tiktok_report(
        self,
        access_token: str,
        endDate: str,
        length: int,
        page: int,
        startDate: str,
        advertiserIds: list[Any] | None = None,
        advertiserType: list[Any] | None = None,
        bidStrategies: list[Any] | None = None,
        budgetTypes: list[Any] | None = None,
        currencies: list[Any] | None = None,
        displayTimezones: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        ownerBcIds: list[Any] | None = None,
        searchType: str | None = None,
        searchValue: list[Any] | None = None,
        serviceStatus: list[Any] | None = None,
        status: list[Any] | None = None,
        summaryCurrency: str | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-推广广告-广告帐号报表

        API: /basicOpen/multiplatform/ads/queryAdvertiserList
        Method: GET

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            length: 每页条数，必填，小于2000 (Required)
            page: 页码，必填 (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            advertiserIds: 广告账号Id列表，Long数组 (Optional)
            advertiserType: 广告主类型列表，String数组 (Optional)
            bidStrategies: 出价策略列表，String数组 (Optional)
            budgetTypes: 预算类型列表，String数组 (Optional)
            currencies: 币种列表，String数组 (Optional)
            displayTimezones: 地区时区列表，String数组 (Optional)
            orderField: 排序字段（驼峰格式） (Optional)
            orderType: 排序方式 (Optional)
            ownerBcIds: 广告主BusinessId列表，Long数组 (Optional)
            searchType: 搜索字段，当字段searchValue有值时该字段也必须有值，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告 (Optional)
            searchValue: 搜索值列表 (Optional)
            serviceStatus: 服务状态列表，String数组 (Optional)
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户 (Optional)
            summaryCurrency: 汇总币种 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok_report(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "page": page,
            "startDate": startDate,
            "advertiserIds": advertiserIds,
            "advertiserType": advertiserType,
            "bidStrategies": bidStrategies,
            "budgetTypes": budgetTypes,
            "currencies": currencies,
            "displayTimezones": displayTimezones,
            "orderField": orderField,
            "orderType": orderType,
            "ownerBcIds": ownerBcIds,
            "searchType": searchType,
            "searchValue": searchValue,
            "serviceStatus": serviceStatus,
            "status": status,
            "summaryCurrency": summaryCurrency
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryAdvertiserList",
            method="GET",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        reportDate: str,
        pageSize: int,
        pageNum: int,
        orderType: str | None = None,
        itemBrand: dict[str, Any] | None = None,
        itemQueryType: int | None = None,
        itemQueryField: int | None = None,
        searchKeywordType: int | None = None,
        orderField: str | None = None,
        searchKeyword: dict[str, Any] | None = None,
        itemQueryValue: dict[str, Any] | None = None,
        itemBrandType: int | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-词 - 沃尔玛热门搜索词

        API: /basicOpen/multiplatform/ads/reportSearchTrendsList
        Method: POST

        Args:
            access_token: Access token for authentication
            reportDate: 报告日期，必填，格式：yyyy-MM-dd (Required)
            pageSize: 每页大小，必填，不能大于100 (Required)
            pageNum: 页码，必填 (Required)
            orderType: 排序方向，枚举值：ASC-升序, DESC-降序 (Optional)
            itemBrand: 商品品牌(在item_brand_1/2/3中搜索)，模糊搜索请使用String类型，精确搜索请使用数组类型 (Optional)
            itemQueryType: 字段类型，枚举值：0-模糊搜索, 1-精确搜索 (Optional)
            itemQueryField: 查询字段，枚举值：0-itemId, 1-itemName (Optional)
            searchKeywordType: 搜索关键词类型，枚举值：0-模糊搜索, 1-精确搜索 (Optional)
            orderField: 排序字段(驼峰格式)，枚举值：searchKeyword-搜索关键词, keywordRank-关键词排名, totalPctClickShare-前3商品点击占比总和, totalPctConvShare-前3商品转化占比总和 (Optional)
            searchKeyword: 搜索关键词，模糊搜索请使用String类型，精确搜索请使用数组类型 (Optional)
            itemQueryValue: 文本框中的值，模糊搜索请使用String类型，精确搜索请使用数组类型 (Optional)
            itemBrandType: 商品品牌类型，枚举值：0-模糊搜索, 1-精确搜索 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "reportDate": reportDate,
            "pageSize": pageSize,
            "pageNum": pageNum,
            "orderType": orderType,
            "itemBrand": itemBrand,
            "itemQueryType": itemQueryType,
            "itemQueryField": itemQueryField,
            "searchKeywordType": searchKeywordType,
            "orderField": orderField,
            "searchKeyword": searchKeyword,
            "itemQueryValue": itemQueryValue,
            "itemBrandType": itemBrandType
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportSearchTrendsList",
            method="POST",
            req_body=params
        )



    async def get_sv(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        day: int,
        endDate: str,
        operationSourceType: str,
        pageNum: int,
        pageSize: int,
        paging: bool,
        startDate: str,
        campaignIds: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 广告活动

        API: /basicOpen/multiplatform/ads/reportCampaignSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video (Required)
            day: 归因天数，必填，数据归因天数，枚举值：3, 14, 30 (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            operationSourceType: 操作来源，必填，openapi调用必传gateway，前端传web (Required)
            pageNum: 页码，必填，分页时的页码，从1开始 (Required)
            pageSize: 每页大小，必填，openapi必传且小于2000 (Required)
            paging: 是否分页，必填，openapi必填true (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，指定查询的广告活动ID，支持批量查询 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "day": day,
            "endDate": endDate,
            "operationSourceType": operationSourceType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "orderField": orderField,
            "orderType": orderType,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportCampaignSvList",
            method="GET",
            req_body=params
        )



    async def get_sb(
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 平台

        API: /basicOpen/multiplatform/ads/reportPlatformSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportPlatformSbList",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        pageType: list[Any] | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 页面类型

        API: /basicOpen/multiplatform/ads/reportPageTypeSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            pageType: 页面类型列表，String数组，枚举值：browse-浏览, item-商品, search-搜索, topic-主题, category-分类, homepage-首页, other-其他 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "pageType": pageType,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportPageTypeSbList",
            method="GET",
            req_body=params
        )



    async def get_sv(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 关键词

        API: /basicOpen/multiplatform/ads/reportKeywordSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text） (Optional)
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportKeywordSvList",
            method="GET",
            req_body=params
        )



    async def get_sv(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        dateKey: str,
        endDate: str,
        startDate: str,
        campaignIds: list[Any] | None = None,
        companyId: int | None = None,
        day: int | None = None,
        operationSourceType: str | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 广告组

        API: /basicOpen/multiplatform/ads/queryAdGroupSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。不传时默认查询所有类型 (Required)
            dateKey: 天数据聚合维度，枚举值：day-按天, week-按周, month-按月。【仅天维度接口使用】 (Required)
            endDate: 结束日期，格式: yyyy-MM-dd (Required)
            startDate: 开始日期，格式: yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组 (Optional)
            companyId: 公司ID (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30。默认14天 (Optional)
            operationSourceType: 操作来源，默认网页操作 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括但不限于: 基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序。不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用, delete-归档 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "dateKey": dateKey,
            "endDate": endDate,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "companyId": companyId,
            "day": day,
            "operationSourceType": operationSourceType,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryAdGroupSvList",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 广告

        API: /basicOpen/multiplatform/ads/reportAdItemSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告名称（ad_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportAdItemSbList",
            method="GET",
            req_body=params
        )



    async def get_tiktok(  # noqa: F811
        self,
        access_token: str,
        endDate: str,
        length: int,
        page: int,
        startDate: str,
        advertiserIds: list[Any] | None = None,
        bidStrategies: list[Any] | None = None,
        budgetTypes: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        currencies: list[Any] | None = None,
        objectiveType: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        ownerBcIds: list[Any] | None = None,
        searchType: str | None = None,
        searchValue: list[Any] | None = None,
        serviceStatus: list[Any] | None = None,
        status: list[Any] | None = None,
        summaryCurrency: str | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-推广广告-广告系列

        API: /basicOpen/multiplatform/ads/queryTiktokCampaignList
        Method: GET

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            length: 每页条数，必填，小于2000 (Required)
            page: 页码，必填 (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            advertiserIds: 广告账号Id列表，Long数组 (Optional)
            bidStrategies: 出价策略列表，String数组 (Optional)
            budgetTypes: 预算类型列表，String数组 (Optional)
            campaignIds: 广告活动id列表，Long数组 (Optional)
            currencies: 币种列表，String数组 (Optional)
            objectiveType: 推广目标列表，String数组，枚举值：REACH-覆盖人数, TRAFFIC-访问量, VIDEO_VIEWS-视频播放量, LEAD_GENERATION-线索收集, ENGAGEMENT-社区互动, APP_PROMOTION-应用推广, WEB_CONVERSIONS-网站转化量, PRODUCT_SALES-商品销量 (Optional)
            orderField: 排序字段（驼峰格式） (Optional)
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序 (Optional)
            ownerBcIds: 广告主BusinessId列表，Long数组 (Optional)
            searchType: 搜索字段，枚举值：advertiser_name-广告账号, ad_group_name-广告组, campaign_name-推广系列, ad_name-广告。当字段searchValue有值时，该字段也必须有值 (Optional)
            searchValue: 搜索值，String数组 (Optional)
            serviceStatus: 服务状态列表，String数组 (Optional)
            status: 状态列表，String数组，枚举值：STATUS_ENABLE-已启用, SYSTEM_STATUS_IN_REVIEW-审核中, SYSTEM_STATUS_NOT_PASS-未通过, STATUS_LIMIT-惩罚中, STATUS_DISABLE-已关户 (Optional)
            summaryCurrency: 汇总币种 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "page": page,
            "startDate": startDate,
            "advertiserIds": advertiserIds,
            "bidStrategies": bidStrategies,
            "budgetTypes": budgetTypes,
            "campaignIds": campaignIds,
            "currencies": currencies,
            "objectiveType": objectiveType,
            "orderField": orderField,
            "orderType": orderType,
            "ownerBcIds": ownerBcIds,
            "searchType": searchType,
            "searchValue": searchValue,
            "serviceStatus": serviceStatus,
            "status": status,
            "summaryCurrency": summaryCurrency
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryTiktokCampaignList",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        realtime: int | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 广告活动

        API: /basicOpen/multiplatform/ads/reportCampaignSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            realtime: 实时数据标识，0-非实时, 1-实时数据 (Optional)
            searchText: 搜索文本，模糊搜索广告活动名称（campaign_name） (Optional)
            status: 广告活动状态列表，String数组，枚举值：enabled-启用, paused-暂停, scheduled-已安排, rescheduled-重新安排, live-运行中, proposal-提议, completed-已完成 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "realtime": realtime,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportCampaignSbList",
            method="GET",
            req_body=params
        )



    async def get_tiktok_gmv_max(  # noqa: F811
        self,
        access_token: str,
        endDate: str,
        length: int,
        page: int,
        startDate: str,
        advertiserIds: list[Any] | None = None,
        bidTypeCodes: list[Any] | None = None,
        campaignId: Any | None = None,
        campaignIds: list[Any] | None = None,
        gmvMaxPromotionTypeCodes: list[Any] | None = None,
        itemGroupIds: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        ownerBcIds: list[Any] | None = None,
        scheduleEndDate: str | None = None,
        scheduleStartDate: str | None = None,
        status: list[Any] | None = None,
        storeIds: list[Any] | None = None,
        summaryCurrency: str | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-GMV MAX-推广系列

        API: /basicOpen/multiplatform/ads/queryGmvCampaignReportList
        Method: GET

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            length: 每页条数，必填，小于2000 (Required)
            page: 页码，必填，从1开始 (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            advertiserIds: 广告账号ID列表，Long数组，用于筛选特定广告账号 (Optional)
            bidTypeCodes: 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量 (Optional)
            campaignId: 推广系列ID，用于筛选单个推广系列 (Optional)
            campaignIds: 推广系列ID列表，Long数组，用于查询多个推广系列 (Optional)
            gmvMaxPromotionTypeCodes: GMV Max类型编码列表，String数组，枚举值：PRODUCT-商品GMV, LIVE-直播GMV (Optional)
            itemGroupIds: 广告商品ID列表，Long数组，用于筛选特定商品 (Optional)
            orderField: 排序字段名称，如：cost, orders, roi (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序 (Optional)
            ownerBcIds: 广告主账号ID列表，Long数组，业务负责人的BC ID列表 (Optional)
            scheduleEndDate: 排期结束日期，格式：yyyy-MM-dd (Optional)
            scheduleStartDate: 排期开始日期，格式：yyyy-MM-dd (Optional)
            status: 推广系列操作状态编码列表，String数组，枚举值：ENABLE-已开启, DISABLE-已暂停, DELETE-已删除 (Optional)
            storeIds: 店铺ID列表，Long数组，用于筛选特定店铺的数据 (Optional)
            summaryCurrency: 汇总币种编码，用于统一汇总不同币种的数据 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok_gmv_max(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "page": page,
            "startDate": startDate,
            "advertiserIds": advertiserIds,
            "bidTypeCodes": bidTypeCodes,
            "campaignId": campaignId,
            "campaignIds": campaignIds,
            "gmvMaxPromotionTypeCodes": gmvMaxPromotionTypeCodes,
            "itemGroupIds": itemGroupIds,
            "orderField": orderField,
            "orderType": orderType,
            "ownerBcIds": ownerBcIds,
            "scheduleEndDate": scheduleEndDate,
            "scheduleStartDate": scheduleStartDate,
            "status": status,
            "storeIds": storeIds,
            "summaryCurrency": summaryCurrency
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryGmvCampaignReportList",
            method="GET",
            req_body=params
        )



    async def get_sp(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SP广告 - 广告

        API: /basicOpen/multiplatform/ads/reportAdItemSpList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SP广告报告必须且只能携带sponsoredProducts-manual和sponsoredProducts-auto (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告名称（ad_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sp(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportAdItemSpList",
            method="GET",
            req_body=params
        )



    async def get_tiktok_gmv_max(  # noqa: F811
        self,
        access_token: str,
        endDate: str,
        length: int,
        page: int,
        startDate: str,
        advertiserIds: list[Any] | None = None,
        bidTypeCodes: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        itemGroupIds: list[Any] | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        ownerBcIds: list[Any] | None = None,
        status: list[Any] | None = None,
        storeIds: list[Any] | None = None,
        summaryCurrency: str | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-GMV MAX-广告商品

        API: /basicOpen/multiplatform/ads/queryGmvItemGroupReportList
        Method: POST

        Args:
            access_token: Access token for authentication
            endDate: 结束日期，必填，格式：yyyy-MM-dd，与开始日期间隔不超过31天 (Required)
            length: 每页条数，必填，小于2000 (Required)
            page: 页码，必填 (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            advertiserIds: 广告账号ID列表，Long数组 (Optional)
            bidTypeCodes: 优化模式编码列表，String数组，枚举值：CUSTOM-目标ROI, NO_BID-最大投放量 (Optional)
            campaignIds: 推广系列ID列表，Long数组 (Optional)
            itemGroupIds: 广告商品ID列表，Long数组 (Optional)
            orderField: 排序字段 (Optional)
            orderType: 排序方式，枚举值：ASC-升序, DESC-降序 (Optional)
            ownerBcIds: 广告主账号ID列表，Long数组 (Optional)
            status: 商品状态编码列表，String数组，枚举值：available-可用, unavailable-不可用 (Optional)
            storeIds: 店铺ID列表，Long数组 (Optional)
            summaryCurrency: 汇总币种编码 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok_gmv_max(token, ...)
            >>> print(result)
        """
        params = {
            "endDate": endDate,
            "length": length,
            "page": page,
            "startDate": startDate,
            "advertiserIds": advertiserIds,
            "bidTypeCodes": bidTypeCodes,
            "campaignIds": campaignIds,
            "itemGroupIds": itemGroupIds,
            "orderField": orderField,
            "orderType": orderType,
            "ownerBcIds": ownerBcIds,
            "status": status,
            "storeIds": storeIds,
            "summaryCurrency": summaryCurrency
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryGmvItemGroupReportList",
            method="POST",
            req_body=params
        )



    async def get_sv(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SV广告 - 广告

        API: /basicOpen/multiplatform/ads/reportAdItemSvList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SV广告报告必须且只能携带video (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Long数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告名称（ad_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告状态列表，String数组，枚举值：enabled-启用, disabled-禁用 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sv(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportAdItemSvList",
            method="GET",
            req_body=params
        )



    async def get_tiktok(  # noqa: F811
        self,
        access_token: str,
        internalStatus: str | None = None,
        hasGmvStore: int | None = None
    ) -> dict[str, Any]:
        """
        查询TikTok-推广广告-广告帐号

        API: /basicOpen/multiplatform/ads/queryCommonAdvertiserList
        Method: POST

        Args:
            access_token: Access token for authentication
            internalStatus: 内部状态，枚举值：ENABLE-启用, DISABLE-禁用, DELETE-删除。用于过滤授权信息表中的状态，不传则返回所有状态的广告账号 (Optional)
            hasGmvStore: 是否有GMV店铺，枚举值：1-只返回有GMV店铺的广告账号，不传或传其他值则不过滤 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_tiktok(token, ...)
            >>> print(result)
        """
        params = {
            "internalStatus": internalStatus,
            "hasGmvStore": hasGmvStore
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/queryCommonAdvertiserList",
            method="POST",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        adGroupIds: list[Any] | None = None,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 关键词

        API: /basicOpen/multiplatform/ads/reportKeywordSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            adGroupIds: 广告组ID列表，Integer数组，按广告组ID筛选 (Optional)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索关键词文本（keyword_text） (Optional)
            status: 关键词状态列表，String数组，枚举值：enabled-启用, paused-暂停 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "adGroupIds": adGroupIds,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportKeywordSbList",
            method="GET",
            req_body=params
        )



    async def get_sb(  # noqa: F811
        self,
        access_token: str,
        advertiserIds: list[Any],
        campaignType: list[Any],
        endDate: str,
        startDate: str,
        campaignIds: list[Any] | None = None,
        day: int | None = None,
        orderField: str | None = None,
        orderType: str | None = None,
        pageNum: int | None = None,
        pageSize: int | None = None,
        paging: bool | None = None,
        searchText: str | None = None,
        searchType: str | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询沃尔玛-广告 - SB广告 - 广告组

        API: /basicOpen/multiplatform/ads/reportAdGroupSbList
        Method: GET

        Args:
            access_token: Access token for authentication
            advertiserIds: 广告账号ID列表，BigInteger数组，必填，必须至少选择一个店铺 (Required)
            campaignType: 广告活动类型列表，String数组，必填，枚举值：sponsoredProducts-manual(SP手动), sponsoredProducts-auto(SP自动), sba(SB品牌广告), video(SV视频广告)。注意：查询SB广告报告必须且只能携带sba (Required)
            endDate: 结束日期，必填，格式：yyyy-MM-dd (Required)
            startDate: 开始日期，必填，格式：yyyy-MM-dd (Required)
            campaignIds: 广告活动ID列表，Long数组，按广告活动ID筛选广告组 (Optional)
            day: 归因天数，数据归因天数，枚举值：3, 14, 30，默认14天 (Optional)
            orderField: 排序字段，支持对查询结果中的任意字段进行排序（驼峰命名）。包括：基础指标(numAdsShown/numAdsClicks/adSpend)、销售指标(attributedSales/attributedOrders/attributedUnits/advertisedSkuSales/advertisedSkuUnits)、关联指标(otherSkuSales/otherSkuUnits)、品牌新买家指标(ntbOrders/ntbRevenue/ntbUnits)、计算指标(cpc/ctr/cvr/acos/roas/aov/cpa)、时间字段(startDate/endDate/entityCreateAt)等所有返回的报表字段。不传时默认按广告花费倒序 (Optional)
            orderType: 排序类型，枚举值：ASC-升序, DESC-降序，不传时默认ASC (Optional)
            pageNum: 页码，分页时的页码，从1开始 (Optional)
            pageSize: 每页大小，分页时每页显示的记录数，最大200 (Optional)
            paging: 是否分页，默认为true (Optional)
            searchText: 搜索文本，模糊搜索广告组名称（ad_group_name） (Optional)
            searchType: 搜索类型，目前不用传 (Optional)
            status: 广告组状态列表，String数组，枚举值：enabled-启用, disabled-禁用，delete-归档 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_sb(token, ...)
            >>> print(result)
        """
        params = {
            "advertiserIds": advertiserIds,
            "campaignType": campaignType,
            "endDate": endDate,
            "startDate": startDate,
            "campaignIds": campaignIds,
            "day": day,
            "orderField": orderField,
            "orderType": orderType,
            "pageNum": pageNum,
            "pageSize": pageSize,
            "paging": paging,
            "searchText": searchText,
            "searchType": searchType,
            "status": status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/multiplatform/ads/reportAdGroupSbList",
            method="GET",
            req_body=params
        )


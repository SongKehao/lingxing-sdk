"""Order API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class OrderEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def order(
        self,
        access_token: str,
        sid: int,
        seller_fulfillment_order_id: str
    ) -> dict[str, Any]:
        """
        取消多渠道订单

        API: /order/amzod/api/cancelOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            seller_fulfillment_order_id: 卖家订单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "seller_fulfillment_order_id": seller_fulfillment_order_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/order/amzod/api/cancelOrder",
            method="POST",
            req_body=params
        )



    async def create_order(
        self,
        access_token: str,
        store_name: str,
        country: str,
        order_id: str,
        receiver: str,
        country_code: str,
        region: str,
        address1: str,
        postcode: str,
        buyers_mailbox: str,
        order_id_for_packing: str,
        date_for_packing: str,
        item_list: list[Any],
        is_blank_box: str | None = None,
        is_block_amzl: str | None = None,
        city: str | None = None,
        address2: str | None = None,
        phone_number: str | None = None,
        remark_for_packing: str | None = None,
        delivery_operation: str | None = None,
        delivery_service: str | None = None,
        remark: str | None = None
    ) -> dict[str, Any]:
        """
        创建亚马逊多渠道订单

        API: /order/amzod/api/createOrder
        Method: POST

        Args:
            access_token: Access token for authentication
            store_name: 店铺名 (Required)
            country: 店铺国家 (Required)
            order_id: 订单号 (Required)
            is_blank_box: 是否使用无品牌包装箱（“是”/“否”，默认为“否”） (Optional)
            is_block_amzl: 是否阻止亚马逊物流（“是”/“否”，默认为“否”） (Optional)
            receiver: 收件人 (Required)
            country_code: 收货地址国家/地区（输入国家/地区简码） (Required)
            region: 地区 (Required)
            city: 城市（日本市场非必填，其他市场必填） (Optional)
            address1: 地址1 (Required)
            address2: 地址2 (Optional)
            postcode: 邮编 (Required)
            phone_number: 电话号码 (Optional)
            buyers_mailbox: 买家邮箱 (Required)
            order_id_for_packing: 装箱单-订单号 (Required)
            date_for_packing: 装箱单-订单日期 (Required)
            remark_for_packing: 装箱单-装箱单备注 (Optional)
            delivery_operation: 配送操作（“立即配送”/“保留订单”） (Optional)
            delivery_service: 配送服务（“标准配送”/“加急配送”/“优先配送”） (Optional)
            remark: 订单备注 (Optional)
            item_list: 商品列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_order(token, ...)
            >>> print(result)
        """
        params = {
            "store_name": store_name,
            "country": country,
            "order_id": order_id,
            "is_blank_box": is_blank_box,
            "is_block_amzl": is_block_amzl,
            "receiver": receiver,
            "country_code": country_code,
            "region": region,
            "city": city,
            "address1": address1,
            "address2": address2,
            "postcode": postcode,
            "phone_number": phone_number,
            "buyers_mailbox": buyers_mailbox,
            "order_id_for_packing": order_id_for_packing,
            "date_for_packing": date_for_packing,
            "remark_for_packing": remark_for_packing,
            "delivery_operation": delivery_operation,
            "delivery_service": delivery_service,
            "remark": remark,
            "item_list": item_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/order/amzod/api/createOrder",
            method="POST",
            req_body=params
        )



    async def get_order(
        self,
        access_token: str,
        order_id: str
    ) -> dict[str, Any]:
        """
        查询亚马逊订单详情

        API: /erp/sc/data/mws/orderDetail
        Method: POST

        Args:
            access_token: Access token for authentication
            order_id: 亚马逊订单号，多个使用英文逗号分隔，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order(token, ...)
            >>> print(result)
        """
        params = {
            "order_id": order_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws/orderDetail",
            method="POST",
            req_body=params
        )



    async def get_order_info(
        self,
        access_token: str,
        order_info: list[Any]
    ) -> dict[str, Any]:
        """
        查询亚马逊多渠道订单详情-物流信息

        API: /order/amzod/api/orderDetails/logisticsInformation
        Method: POST

        Args:
            access_token: Access token for authentication
            order_info: 订单信息，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order_info(token, ...)
            >>> print(result)
        """
        params = {
            "order_info": order_info
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/order/amzod/api/orderDetails/logisticsInformation",
            method="POST",
            req_body=params
        )



    async def get_orderlist(
        self,
        access_token: str,
        sid: int | None = None,
        sid_list: list[Any] | None = None,
        Canceled_取消: Any | None = None,
        sort_desc_by_date_type: int | None = None,
        fulfillment_channel: int | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊订单列表

        API: /erp/sc/data/mws/orders
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            sid_list: 店铺id列表，最大长度20 (Optional)
            Canceled_取消: 否 (Optional)
            sort_desc_by_date_type: 是否按查询日期类型排序：0 否，1 降序，2 升序【默认0】 (Optional)
            fulfillment_channel: 配送方式：1 亚马逊订单-AFN，2 自发货-MFN (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限5000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderlist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "sid_list": sid_list,
            "Canceled_取消": Canceled_取消,
            "sort_desc_by_date_type": sort_desc_by_date_type,
            "fulfillment_channel": fulfillment_channel,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws/orders",
            method="GET",
            req_body=params
        )



    async def get_order_info(  # noqa: F811
        self,
        access_token: str,
        order_info: list[Any]
    ) -> dict[str, Any]:
        """
        查询亚马逊多渠道订单详情-退货换货信息

        API: /order/amzod/api/orderDetails/returnInformation
        Method: POST

        Args:
            access_token: Access token for authentication
            order_info: 订单信息，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order_info(token, ...)
            >>> print(result)
        """
        params = {
            "order_info": order_info
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/order/amzod/api/orderDetails/returnInformation",
            method="POST",
            req_body=params
        )



    async def get_order_detail(
        self,
        access_token: str,
        amazonOrderId: str,
        sid: int
    ) -> dict[str, Any]:
        """
        多渠道订单-交易明细

        API: /basicOpen/openapi/salesOrder/multi-channel/list/transaction
        Method: POST

        Args:
            access_token: Access token for authentication
            amazonOrderId: 亚马逊订单ID (Required)
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order_detail(token, ...)
            >>> print(result)
        """
        params = {
            "amazonOrderId": amazonOrderId,
            "sid": sid
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/salesOrder/multi-channel/list/transaction",
            method="POST",
            req_body=params
        )



    async def scorder_order(
        self,
        access_token: str,
        sid: int,
        amazonOrderId: str,
        remark: str
    ) -> dict[str, Any]:
        """
        SC订单-设置订单备注

        API: /basicOpen/platformOrder/scOrder/setRemark
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            amazonOrderId: 订单id (Required)
            remark: 备注 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.scorder_order(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "amazonOrderId": amazonOrderId,
            "remark": remark
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/platformOrder/scOrder/setRemark",
            method="POST",
            req_body=params
        )



    async def get_orderlist(  # noqa: F811
        self,
        access_token: str,
        start_date: str,
        end_date: str,
        sid: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        amazon_order_id_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询售后订单列表

        API: /erp/sc/routing/amzod/order/afterSaleList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            start_date: 查询时间，左闭右开，格式：Y-m-d (Required)
            end_date: 查询时间，左闭右开，格式：Y-m-d (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000 (Optional)
            amazon_order_id_list: 亚马逊订单id列表，上限50 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderlist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            "amazon_order_id_list": amazon_order_id_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/amzod/order/afterSaleList",
            method="POST",
            req_body=params
        )



    async def get_order_info(  # noqa: F811
        self,
        access_token: str,
        order_info: list[Any]
    ) -> dict[str, Any]:
        """
        查询亚马逊多渠道订单详情-商品信息

        API: /order/amzod/api/orderDetails/productInformation
        Method: POST

        Args:
            access_token: Access token for authentication
            order_info: 订单信息，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order_info(token, ...)
            >>> print(result)
        """
        params = {
            "order_info": order_info
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/order/amzod/api/orderDetails/productInformation",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        record_unique_id: int | None = None,
        sku: str | None = None,
        store_id: int | None = None,
        operate_time: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        刊登管理-查询刊登结果

        API: /listing/publish/openapi/amazon/product/list
        Method: POST

        Args:
            access_token: Access token for authentication
            record_unique_id: 批次唯一ID (Optional)
            sku: sku (Optional)
            store_id: store_id (Optional)
            operate_time: 操作时间 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "record_unique_id": record_unique_id,
            "sku": sku,
            "store_id": store_id,
            "operate_time": operate_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/publish/openapi/amazon/product/list",
            method="POST",
            req_body=params
        )



    async def get_amazon(
        self,
        access_token: str,
        storeId: Any,
        categoryUniqueId: Any
    ) -> dict[str, Any]:
        """
        刊登管理-查询 Amazon 子分类

        API: /basicOpen/openapi/publish/manage/categoryChildren
        Method: POST

        Args:
            access_token: Access token for authentication
            storeId: 店铺id (Required)
            categoryUniqueId: 类目唯一ID (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_amazon(token, ...)
            >>> print(result)
        """
        params = {
            "storeId": storeId,
            "categoryUniqueId": categoryUniqueId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/publish/manage/categoryChildren",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        store_id: Any,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        刊登管理-提交商品资料

        API: /listing/publish/openapi/amazon/product/publish
        Method: POST

        Args:
            access_token: Access token for authentication
            store_id: store_id (Required)
            data:  (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "store_id": store_id,
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/publish/openapi/amazon/product/publish",
            method="POST",
            req_body=params
        )



    async def get_producttype_json_schema(
        self,
        access_token: str,
        marketplaceId: str,
        productTypeOrigin: str
    ) -> dict[str, Any]:
        """
        刊登管理-获取指定 productType 的 JSON Schema

        API: /basicOpen/openapi/publish/manage/getProductType
        Method: GET

        Args:
            access_token: Access token for authentication
            marketplaceId: 市场ID (Required)
            productTypeOrigin: 商品原始类型 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_producttype_json_schema(token, ...)
            >>> print(result)
        """
        params = {
            "marketplaceId": marketplaceId,
            "productTypeOrigin": productTypeOrigin
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/publish/manage/getProductType",
            method="GET",
            req_body=params
        )



    async def get_amazon(  # noqa: F811
        self,
        access_token: str,
        storeId: Any
    ) -> dict[str, Any]:
        """
        刊登管理-查询 Amazon 根分类

        API: /basicOpen/openapi/publish/manage/categoryRoot
        Method: POST

        Args:
            access_token: Access token for authentication
            storeId: 店铺id (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_amazon(token, ...)
            >>> print(result)
        """
        params = {
            "storeId": storeId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/publish/manage/categoryRoot",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        sellerId: str,
        marketplaceId: str,
        productType: str,
        flag: Any | None = None
    ) -> dict[str, Any]:
        """
        刊登管理-获取运费模板

        API: /basicOpen/openapi/publish/manage/getMerchantShippingGroup
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerId: 店铺id (Required)
            marketplaceId: 市场id (Required)
            productType: 商品原始类目 (Required)
            flag: 默认传0，返回为空则传1，实时请求亚马逊获取后台最新数据 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "sellerId": sellerId,
            "marketplaceId": marketplaceId,
            "productType": productType,
            "flag": flag
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/publish/manage/getMerchantShippingGroup",
            method="GET",
            req_body=params
        )



    async def get_listing(
        self,
        access_token: str,
        list: list[Any]
    ) -> dict[str, Any]:
        """
        解除Listing配对

        API: /basicOpen/listingManage/unLinkListingPairs
        Method: POST

        Args:
            access_token: Access token for authentication
            list: 解除配对列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listing(token, ...)
            >>> print(result)
        """
        params = {
            "list": list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/listingManage/unLinkListingPairs",
            method="POST",
            req_body=params
        )



    async def get_listing(  # noqa: F811
        self,
        access_token: str,
        sid: str,
        is_pair: int | None = None,
        is_delete: int | None = None,
        pair_update_start_time: str | None = None,
        pair_update_end_time: str | None = None,
        listing_update_start_time: str | None = None,
        listing_update_end_time: str | None = None,
        search_field: str | None = None,
        search_value: list[Any] | None = None,
        exact_search: int | None = None,
        store_type: int | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊Listing

        API: /erp/sc/data/mws/listing
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            is_pair: 是否配对：1 已配对，2 未配对 (Optional)
            is_delete: 是否删除：0 未删除，1 已删除 (Optional)
            pair_update_start_time: 【配对更新时间】的开始时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1 (Optional)
            pair_update_end_time: 【配对更新时间】的结束时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1 (Optional)
            listing_update_start_time: 【All Listing报表更新时间】的开始时间（此为零时区时间，格式Y-m-d H:i:s） (Optional)
            listing_update_end_time: 【All Listing报表更新时间】的结束时间（此为零时区时间，格式Y-m-d H:i:s） (Optional)
            search_field: 搜索支持字段：seller_sku、asin、sku (Optional)
            search_value: 搜索值，上限10个 (Optional)
            exact_search: 搜索模式：0 模糊搜索，1 精确搜索【默认值】 (Optional)
            store_type: 商品类型，1-非低价商店 ，2-低价商店商品 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listing(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "is_pair": is_pair,
            "is_delete": is_delete,
            "pair_update_start_time": pair_update_start_time,
            "pair_update_end_time": pair_update_end_time,
            "listing_update_start_time": listing_update_start_time,
            "listing_update_end_time": listing_update_end_time,
            "search_field": search_field,
            "search_value": search_value,
            "exact_search": exact_search,
            "store_type": store_type,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/mws/listing",
            method="POST",
            req_body=params
        )



    async def get_listing(  # noqa: F811
        self,
        access_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        批量获取Listing费用

        API: /listing/listing/open/api/listing/getPrices
        Method: GET

        Args:
            access_token: Access token for authentication
            data: 请求数据，上限500 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listing(token, ...)
            >>> print(result)
        """
        params = {
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/listing/open/api/listing/getPrices",
            method="GET",
            req_body=params
        )



    async def update_b2b(
        self,
        access_token: str,
        content: list[Any]
    ) -> dict[str, Any]:
        """
        修改B2B价格

        API: /basicOpen/b2bPrice/modifyPrice
        Method: POST

        Args:
            access_token: Access token for authentication
            content: B2B售价 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_b2b(token, ...)
            >>> print(result)
        """
        params = {
            "content": content
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/b2bPrice/modifyPrice",
            method="POST",
            req_body=params
        )



    async def get_listinglist(
        self,
        access_token: str,
        bind_detail: list[Any]
    ) -> dict[str, Any]:
        """
        查询Listing标记标签列表

        API: /basicOpen/listingManage/queryListingRelationTagList
        Method: POST

        Args:
            access_token: Access token for authentication
            bind_detail: listing数据，上限100 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listinglist(token, ...)
            >>> print(result)
        """
        params = {
            "bind_detail": bind_detail
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/listingManage/queryListingRelationTagList",
            method="POST",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        offset: Any,
        length: Any,
        sid: list[Any] | None = None,
        processing_status: list[Any] | None = None,
        time_type: Any | None = None,
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: list[Any] | None = None,
        tab_status: Any | None = None
    ) -> dict[str, Any]:
        """
        查询调价队列

        API: /basicOpen/module/adjustPrice/AdjustPriceManual
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 偏移量 (Required)
            length: 页长度，上限500 (Required)
            sid: 搜索店铺id (Optional)
            processing_status: 调价状态，支持多选，数组 1待调价 2调价中 3调价成功 4调价失败 5审批中 6已驳回 7已作废 (Optional)
            time_type: 搜索时间类型：1创建时间 2完成时间 (Optional)
            start_time: 开始时间 (Optional)
            end_time: 结束时间 (Optional)
            search_field: 搜索字段：msku，asin (Optional)
            search_value: 搜索值，msku和asin支持多个搜索，数组 (Optional)
            tab_status: tab状态栏 0全部 1待审批 2调价中 3成功 4失败 5已作废 默认0 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "sid": sid,
            "processing_status": processing_status,
            "time_type": time_type,
            "start_time": start_time,
            "end_time": end_time,
            "search_field": search_field,
            "search_value": search_value,
            "tab_status": tab_status
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/module/adjustPrice/AdjustPriceManual",
            method="POST",
            req_body=params
        )



    async def get_fba_order_order(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        search_field: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        FBA费差异-异常订单-订单

        API: /basicOpen/openapi/sale/fbaFeeDifference/order/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始时间【结算时间】，闭区间，格式：Y-m-d (Optional)
            end_date: 结束时间【结算时间】，闭区间，格式：Y-m-d (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_field: 搜索字段：order_id 订单号，msku MSKU (Optional)
            search_value: 搜索值：多个使用英文逗号分隔，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba_order_order(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "search_field": search_field,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/sale/fbaFeeDifference/order/list",
            method="POST",
            req_body=params
        )



    async def get_fba_order_msku(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        search_field: str | None = None,
        search_value: str | None = None
    ) -> dict[str, Any]:
        """
        FBA费差异-异常订单-MSKU

        API: /basicOpen/openapi/sale/fbaFeeDifference/msku/list
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            start_date: 开始时间【结算时间】，闭区间，格式：Y-m-d (Optional)
            end_date: 结束时间【结算时间】，闭区间，格式：Y-m-d (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            search_field: 搜索字段：msku MSKU (Optional)
            search_value: 搜索值：多个使用英文逗号分隔，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_fba_order_msku(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "search_field": search_field,
            "search_value": search_value
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/openapi/sale/fbaFeeDifference/msku/list",
            method="POST",
            req_body=params
        )



    async def get_listing(  # noqa: F811
        self,
        access_token: str,
        bindDetail: list[Any],
        tagIds: list[Any]
    ) -> dict[str, Any]:
        """
        Listing新增商品标签

        API: /basicOpen/listingManage/bindListingAndTag
        Method: POST

        Args:
            access_token: Access token for authentication
            bindDetail: 配对信息 (Required)
            tagIds: 标签id数组 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listing(token, ...)
            >>> print(result)
        """
        params = {
            "bindDetail": bindDetail,
            "tagIds": tagIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/listingManage/bindListingAndTag",
            method="POST",
            req_body=params
        )



    async def delete_listing(
        self,
        access_token: str,
        bindDetail: list[Any],
        glabalTagIds: list[Any]
    ) -> dict[str, Any]:
        """
        Listing删除商品标签

        API: /basicOpen/listingManage/removeListingAndTag
        Method: POST

        Args:
            access_token: Access token for authentication
            bindDetail: 配对信息 (Required)
            glabalTagIds: 标签id数组 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete_listing(token, ...)
            >>> print(result)
        """
        params = {
            "bindDetail": bindDetail,
            "glabalTagIds": glabalTagIds
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/listingManage/removeListingAndTag",
            method="POST",
            req_body=params
        )



    async def create_listing(
        self,
        access_token: str,
        tag_name: str
    ) -> dict[str, Any]:
        """
        添加Listing标签

        API: /basicOpen/globalTag/listing/addTag
        Method: POST

        Args:
            access_token: Access token for authentication
            tag_name: 标签名称 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_listing(token, ...)
            >>> print(result)
        """
        params = {
            "tag_name": tag_name
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/globalTag/listing/addTag",
            method="POST",
            req_body=params
        )



    async def delete_listing(  # noqa: F811
        self,
        access_token: str,
        tag_ids: list[Any]
    ) -> dict[str, Any]:
        """
        删除Listing标签

        API: /basicOpen/globalTag/listing/removeTag
        Method: POST

        Args:
            access_token: Access token for authentication
            tag_ids: 标签id，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete_listing(token, ...)
            >>> print(result)
        """
        params = {
            "tag_ids": tag_ids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/globalTag/listing/removeTag",
            method="POST",
            req_body=params
        )



    async def update_listing(
        self,
        access_token: str,
        sid_asin_list: list[Any]
    ) -> dict[str, Any]:
        """
        批量分配Listing负责人

        API: /listing/listing/open/api/asin/updatePrincipal
        Method: POST

        Args:
            access_token: Access token for authentication
            sid_asin_list: asin负责人分配信息，最多支持200个 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_listing(token, ...)
            >>> print(result)
        """
        params = {
            "sid_asin_list": sid_asin_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/listing/open/api/asin/updatePrincipal",
            method="POST",
            req_body=params
        )



    async def get_listinglist(  # noqa: F811
        self,
        access_token: str,
        sid: str,
        msku: str,
        offset: int | None = None,
        length: int | None = None,
        operate_uid: list[Any] | None = None,
        operate_time_start: str | None = None,
        operate_time_end: str | None = None
    ) -> dict[str, Any]:
        """
        查询Listing操作日志列表

        API: /basicOpen/listingManage/listingOperateLog/pageList
        Method: POST

        Args:
            access_token: Access token for authentication
            sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            msku: MSKU (Required)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)
            operate_uid: 操作人id (Optional)
            operate_time_start: 开始时间【操作时间】，格式：Y-m-d H:i:s (Optional)
            operate_time_end: 结束时间【操作时间】，格式：Y-m-d H:i:s (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listinglist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "msku": msku,
            "offset": offset,
            "length": length,
            "operate_uid": operate_uid,
            "operate_time_start": operate_time_start,
            "operate_time_end": operate_time_end
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/listingManage/listingOperateLog/pageList",
            method="POST",
            req_body=params
        )



    async def create_listing(  # noqa: F811
        self,
        access_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        批量添加编辑Listing配对

        API: /erp/sc/storage/product/link
        Method: POST

        Args:
            access_token: Access token for authentication
            data:  (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_listing(token, ...)
            >>> print(result)
        """
        params = {
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/product/link",
            method="POST",
            req_body=params
        )



    async def update_fbminventory(
        self,
        access_token: str,
        fbmInventoryList: list[Any]
    ) -> dict[str, Any]:
        """
        修改 FBM库存&处理时间

        API: /basicOpen/FbmManagement/modifyFbmInventory
        Method: POST

        Args:
            access_token: Access token for authentication
            fbmInventoryList: 修改库存列表（支持批量修改，单次最多传200个元素） (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_fbminventory(token, ...)
            >>> print(result)
        """
        params = {
            "fbmInventoryList": fbmInventoryList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/FbmManagement/modifyFbmInventory",
            method="POST",
            req_body=params
        )



    async def update_listing(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        批量修改Listing价格

        API: /erp/sc/listing/ProductPricing/pricingSubmit
        Method: POST

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.update_listing(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/listing/ProductPricing/pricingSubmit",
            method="POST",
            req_body=params
        )



    async def order(  # noqa: F811
        self,
        access_token: str,
        seller_id: str,
        marketplace_id: str,
        order_list: list[Any]
    ) -> dict[str, Any]:
        """
        亚马逊订单提交标发

        API: /pb/mp/order/submitFulfillment
        Method: GET

        Args:
            access_token: Access token for authentication
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Required)
            marketplace_id: 市场id (Required)
            order_list: 提交标发数据列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.order(token, ...)
            >>> print(result)
        """
        params = {
            "seller_id": seller_id,
            "marketplace_id": marketplace_id,
            "order_list": order_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/submitFulfillment",
            method="GET",
            req_body=params
        )



    async def get(  # noqa: F811
        self,
        access_token: str,
        seller_id: str,
        task_id: list[Any]
    ) -> dict[str, Any]:
        """
        查询亚马逊标发结果

        API: /pb/mp/order/getFulfillmentResult
        Method: GET

        Args:
            access_token: Access token for authentication
            seller_id: 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】 (Required)
            task_id: 任务id【提交标发接口返回】，单次请求最多支持查询10个任务ID。 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "seller_id": seller_id,
            "task_id": task_id
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/pb/mp/order/getFulfillmentResult",
            method="GET",
            req_body=params
        )



    async def selfShipmentOrder_importLabel(
        self,
        access_token: str,
        fileName: str,
        base64File: str,
        trackingNo: str,
        waybillNo: str,
        woId: int
    ) -> dict[str, Any]:
        """
        导入面单

        API: /basicOpen/selfShipmentOrder/importLabel
        Method: POST

        Args:
            access_token: Access token for authentication
            fileName: 面单文件名 (Required)
            base64File: PDF/PNG/JPG/JPEG格式文件 Base64编码 (Required)
            trackingNo: 运单号 (Required)
            waybillNo: 跟踪号 (Required)
            woId: 出库单id，对应查询销售出库单列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.selfShipmentOrder_importLabel(token, ...)
            >>> print(result)
        """
        params = {
            "fileName": fileName,
            "base64File": base64File,
            "trackingNo": trackingNo,
            "waybillNo": waybillNo,
            "woId": woId
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/selfShipmentOrder/importLabel",
            method="POST",
            req_body=params
        )



    async def get_orderlist(  # noqa: F811
        self,
        access_token: str,
        sid: str,
        page: int | None = None,
        length: int | None = None,
        start_time: str | None = None,
        end_time: str | None = None
    ) -> dict[str, Any]:
        """
        查询亚马逊自发货订单列表

        API: /erp/sc/routing/order/Order/getOrderList
        Method: GET

        Args:
            access_token: Access token for authentication
            sid: 店铺sid，用英文逗号分隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】 (Required)
            page: 页码数，默认1 (Optional)
            length: 分页长度，默认100 (Optional)
            start_time: 订购时间开始 (Optional)
            end_time: 订购时间结束 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orderlist(token, ...)
            >>> print(result)
        """
        params = {
            "sid": sid,
            "page": page,
            "length": length,
            "start_time": start_time,
            "end_time": end_time
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/order/Order/getOrderList",
            method="GET",
            req_body=params
        )



    async def get_order(  # noqa: F811
        self,
        access_token: str,
        order_number: str
    ) -> dict[str, Any]:
        """
        查询亚马逊自发货订单详情

        API: /erp/sc/routing/order/Order/getOrderDetail
        Method: GET

        Args:
            access_token: Access token for authentication
            order_number: 系统单号 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_order(token, ...)
            >>> print(result)
        """
        params = {
            "order_number": order_number
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/order/Order/getOrderDetail",
            method="GET",
            req_body=params
        )



    async def get_list(
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询促销活动列表-优惠券

        API: /basicOpen/promotionalActivities/coupon/list
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            sids: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotionalActivities/coupon/list",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sellerSku: str,
        storeId: str,
        startTime: str,
        endTime: str,
        sortField: str,
        sortType: str,
        pageNum: Any,
        pageSize: Any,
        promotionType: list[Any] | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询商品折扣详情-列表-会员折扣

        API: /basicOpen/promotion/listingDetailPrimeDiscount
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerSku: seller_sku(msku) (Required)
            promotionType: 促销类型 (Optional)
            status: 促销状态 (Optional)
            storeId: 店铺id (Required)
            startTime: 活动开始时间 (Required)
            endTime: 活动结束时间 (Required)
            sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (Required)
            sortType: 排序类型 asc desc (Required)
            pageNum: 分页页码 (Required)
            pageSize: 分页大小 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sellerSku": sellerSku,
            "promotionType": promotionType,
            "status": status,
            "storeId": storeId,
            "startTime": startTime,
            "endTime": endTime,
            "sortField": sortField,
            "sortType": sortType,
            "pageNum": pageNum,
            "pageSize": pageSize
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotion/listingDetailPrimeDiscount",
            method="GET",
            req_body=params
        )



    async def get_orlistingorder(
        self,
        access_token: str,
        itemList: list[Any]
    ) -> dict[str, Any]:
        """
        查询会员折扣or价格折扣详情+listing+订单(批量)

        API: /promotionApi/open/promotion/primeDiscountAllDetailBatch
        Method: GET

        Args:
            access_token: Access token for authentication
            itemList: 批量请求详情itemList个数最小为1最大为20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_orlistingorder(token, ...)
            >>> print(result)
        """
        params = {
            "itemList": itemList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/promotionApi/open/promotion/primeDiscountAllDetailBatch",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询促销活动列表-会员折扣价格折扣

        API: /basicOpen/promotionalActivities/vipDiscount/list
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotionalActivities/vipDiscount/list",
            method="GET",
            req_body=params
        )



    async def get_listingorder(
        self,
        access_token: str,
        itemList: list[Any]
    ) -> dict[str, Any]:
        """
        查询秒杀详情+listing+订单(批量)

        API: /promotionApi/open/promotion/secKillAllDetailBatch
        Method: POST

        Args:
            access_token: Access token for authentication
            itemList: 批量请求详情itemList个数最小为1最大为20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listingorder(token, ...)
            >>> print(result)
        """
        params = {
            "itemList": itemList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/promotionApi/open/promotion/secKillAllDetailBatch",
            method="POST",
            req_body=params
        )



    async def get_listingorder(  # noqa: F811
        self,
        access_token: str,
        itemList: list[Any]
    ) -> dict[str, Any]:
        """
        查询管理促销详情+listing+订单(批量)

        API: /promotionApi/open/promotion/managementAllDetailBatch
        Method: GET

        Args:
            access_token: Access token for authentication
            itemList: 批量请求详情itemList个数最小为1最大为20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listingorder(token, ...)
            >>> print(result)
        """
        params = {
            "itemList": itemList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/promotionApi/open/promotion/managementAllDetailBatch",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sellerSku: str,
        storeId: str,
        startTime: str,
        endTime: str,
        sortField: str,
        sortType: str,
        pageNum: Any,
        pageSize: Any,
        promotionType: list[Any] | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询商品折扣详情-列表-管理促销

        API: /basicOpen/promotion/listingDetailManage
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerSku: seller_sku(msku) (Required)
            promotionType: 促销类型 (Optional)
            status: 促销状态 (Optional)
            storeId: 店铺id (Required)
            startTime: 活动开始时间 (Required)
            endTime: 活动结束时间 (Required)
            sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (Required)
            sortType: 排序类型 asc desc (Required)
            pageNum: 分页页码 (Required)
            pageSize: 分页大小 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sellerSku": sellerSku,
            "promotionType": promotionType,
            "status": status,
            "storeId": storeId,
            "startTime": startTime,
            "endTime": endTime,
            "sortField": sortField,
            "sortType": sortType,
            "pageNum": pageNum,
            "pageSize": pageSize
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotion/listingDetailManage",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询促销活动列表-秒杀

        API: /basicOpen/promotionalActivities/secKill/list
        Method: POST

        Args:
            access_token: Access token for authentication
            start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotionalActivities/secKill/list",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sellerSku: str,
        storeId: str,
        startTime: str,
        endTime: str,
        sortField: str,
        sortType: str,
        pageNum: Any,
        pageSize: Any,
        promotionType: list[Any] | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询商品折扣详情-列表-秒杀

        API: /basicOpen/promotion/listingDetailSecKill
        Method: POST

        Args:
            access_token: Access token for authentication
            sellerSku: sellerSku (Required)
            promotionType: 促销类型 (Optional)
            status: 促销状态 (Optional)
            storeId: 店铺id (Required)
            startTime: 活动开始时间 (Required)
            endTime: 活动结束时间 (Required)
            sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (Required)
            sortType: 排序类型 asc desc (Required)
            pageNum: 分页页码 (Required)
            pageSize: 分页大小 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sellerSku": sellerSku,
            "promotionType": promotionType,
            "status": status,
            "storeId": storeId,
            "startTime": startTime,
            "endTime": endTime,
            "sortField": sortField,
            "sortType": sortType,
            "pageNum": pageNum,
            "pageSize": pageSize
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotion/listingDetailSecKill",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        sellerSku: str,
        storeId: str,
        startTime: str,
        endTime: str,
        sortField: str,
        sortType: str,
        pageNum: Any,
        pageSize: Any,
        promotionType: list[Any] | None = None,
        status: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询商品折扣详情-列表-优惠卷

        API: /basicOpen/promotion/listingDetailCoupon
        Method: GET

        Args:
            access_token: Access token for authentication
            sellerSku: seller_sku(msku) (Required)
            promotionType: 促销类型 (Optional)
            status: 促销状态： 0 其他 1 进行中 2 已过期 3 未开始 (Optional)
            storeId: 店铺id (Required)
            startTime: 活动开始时间 (Required)
            endTime: 活动结束时间 (Required)
            sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (Required)
            sortType: 排序类型 asc desc (Required)
            pageNum: 分页页码 (Required)
            pageSize: 分页大小 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "sellerSku": sellerSku,
            "promotionType": promotionType,
            "status": status,
            "storeId": storeId,
            "startTime": startTime,
            "endTime": endTime,
            "sortField": sortField,
            "sortType": sortType,
            "pageNum": pageNum,
            "pageSize": pageSize
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotion/listingDetailCoupon",
            method="GET",
            req_body=params
        )



    async def get_listingorder(  # noqa: F811
        self,
        access_token: str,
        itemList: list[Any]
    ) -> dict[str, Any]:
        """
        查询优惠券详情+listing+订单(批量)

        API: /promotionApi/open/promotion/couponAllDetailBatch
        Method: GET

        Args:
            access_token: Access token for authentication
            itemList: 批量请求详情itemList个数最小为1最大为20 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_listingorder(token, ...)
            >>> print(result)
        """
        params = {
            "itemList": itemList
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/promotionApi/open/promotion/couponAllDetailBatch",
            method="GET",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        site_date: str,
        start_time: str | None = None,
        end_time: str | None = None,
        offset: int | None = None,
        length: int | None = None,
        sids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询商品折扣列表

        API: /basicOpen/promotion/listingList
        Method: POST

        Args:
            access_token: Access token for authentication
            site_date: 站点时间，格式：Y-m-d (Required)
            start_time: 开始时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            end_time: 结束时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "site_date": site_date,
            "start_time": start_time,
            "end_time": end_time,
            "offset": offset,
            "length": length,
            "sids": sids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotion/listingList",
            method="POST",
            req_body=params
        )



    async def get_list(  # noqa: F811
        self,
        access_token: str,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[Any] | None = None,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询促销活动列表-管理促销

        API: /basicOpen/promotionalActivities/manage/list
        Method: GET

        Args:
            access_token: Access token for authentication
            start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 (Optional)
            sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20，上限200 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_list(token, ...)
            >>> print(result)
        """
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "sids": sids,
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/promotionalActivities/manage/list",
            method="GET",
            req_body=params
        )


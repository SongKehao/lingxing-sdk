"""订单管理API端点"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase


class OrderEndpoints:

    def __init__(self, client: 'OpenApiBase'):
        self.client = client

    async def get_orders(
        self,
        sid: int | None = None,
        sid_list: list[int] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        offset: int = 0,
        length: int = 1000,
        order_status: list[str] | None = None,
        fulfillment_channel: int | None = None,
        date_type: int = 1,
        **filters
    ) -> dict[str, Any]:
        """查询订单列表

        POST /erp/sc/data/mws/orders

        Args:
            sid: 店铺ID（可选，不传则查询所有店铺）
            sid_list: 店铺ID列表，最大长度20（可选，与sid二选一）
            start_date: 开始日期，格式：YYYY-MM-DD（必填）
            end_date: 结束日期，格式：YYYY-MM-DD（必填）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000，上限5000
            order_status: 订单状态列表，如["Shipped", "Unshipped", "Pending"]
            fulfillment_channel: 配送方式：1 亚马逊订单-AFN，2 自发货-MFN
            date_type: 查询日期类型：1 订购时间【默认】，2 订单修改时间，3 平台更新时间，10 发货时间
            **filters: 其他筛选条件

        Returns:
            包含订单列表和分页信息的字典:
            {
                "code": 0,
                "message": "success",
                "data": [
                    {
                        "sid": "4661",
                        "seller_name": "店铺名",
                        "amazon_order_id": "111-2222222-3333333",
                        "order_status": "Shipped",
                        "order_total_amount": "29.99",
                        "fulfillment_channel": "AFN",
                        ...
                    }
                ],
                "total": 1000
            }
        """
        data = {
            "offset": offset,
            "length": length,
            "date_type": date_type,
        }

        # 添加店铺参数（sid或sid_list）
        if sid_list:
            data["sid_list"] = sid_list
        elif sid:
            data["sid"] = sid

        # 添加日期参数（必填）
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date

        if order_status:
            data["order_status"] = order_status
        if fulfillment_channel:
            data["fulfillment_channel"] = fulfillment_channel

        # 添加其他筛选条件
        data.update(filters)

        return await self.client.post(
            "/erp/sc/data/mws/orders",
            req_body=data
        )

    async def get_order_items(self, amazon_order_id: str) -> list[dict[str, Any]]:
        """查询订单商品

        POST /erp/sc/data/mws/orderItems

        Args:
            amazon_order_id: 亚马逊订单ID

        Returns:
            订单商品列表:
            [
                {
                    "order_item_id": "12345678901234",
                    "asin": "B00XXXXXXXX",
                    "seller_sku": "SKU001",
                    "title": "商品标题",
                    "quantity_ordered": 1,
                    "quantity_shipped": 1,
                    "item_price": {
                        "currency_code": "USD",
                        "amount": "25.99"
                    },
                    "shipping_price": {
                        "currency_code": "USD",
                        "amount": "4.99"
                    },
                    "gift_wrap_price": {...},
                    "item_tax": {...},
                    "shipping_tax": {...},
                    "promotion_discount": {...},
                    "condition_note": "New",
                    ...
                }
            ]
        """
        data = {
            "amazon_order_id": amazon_order_id
        }

        result = await self.client.post(
            "/erp/sc/data/mws/orderItems",
            req_body=data
        )

        # 返回订单商品列表（result是ResponseResult，使用.data访问）
        data = result.data if hasattr(result, 'data') else (result.get("data", []) if isinstance(result, dict) else [])
        return data if isinstance(data, list) else (data.get("list", data.get("data", [])) if isinstance(data, dict) else [])

    async def get_listings(
        self,
        sid: int,
        offset: int = 0,
        length: int = 1000,
        sku_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        status: str | None = None,
        **filters
    ) -> dict[str, Any]:
        """查询Listing

        POST /erp/sc/data/mws/listing

        Args:
            sid: 店铺ID (Seller ID)
            offset: 偏移量，用于分页，默认0
            length: 返回数量，默认1000
            sku_list: SKU列表，用于批量查询特定SKU
            asin_list: ASIN列表，用于批量查询特定ASIN
            status: Listing状态，如"Active"、"Inactive"
            **filters: 其他筛选条件

        Returns:
            包含Listing列表和分页信息的字典:
            {
                "data": [
                    {
                        "sku": "SKU001",
                        "asin": "B00XXXXXXXX",
                        "title": "Listing标题",
                        "status": "Active",
                        "price": {
                            "currency_code": "USD",
                            "amount": "29.99"
                        },
                        "quantity": 100,
                        "fulfillment_channel": "AFN",
                        "product_id_type": "ASIN",
                        "item_condition": "New",
                        "main_image": "https://...",
                        "created_at": "2024-01-01 00:00:00",
                        "updated_at": "2024-01-01 00:00:00",
                        ...
                    }
                ],
                "total": 5000,
                "offset": 0,
                "length": 1000
            }
        """
        data = {
            "sid": sid,
            "offset": offset,
            "length": length,
        }

        if sku_list:
            data["sku_list"] = sku_list
        if asin_list:
            data["asin_list"] = asin_list
        if status:
            data["status"] = status

        # 添加其他筛选条件
        data.update(filters)

        return await self.client.post(
            "/erp/sc/data/mws/listing",
            req_body=data
        )

    async def get_order_by_id(self, amazon_order_id: str, sid: int) -> dict[str, Any] | None:
        """根据订单ID获取订单详情

        便捷方法，通过亚马逊订单ID查询单个订单。

        Args:
            amazon_order_id: 亚马逊订单ID
            sid: 店铺ID

        Returns:
            订单信息字典，如果不存在返回None
        """
        # 从订单ID中提取日期范围（假设查询最近30天）
        # 注意：这是简化实现，实际可能需要调整日期范围
        from datetime import datetime, timedelta  # noqa: PLC0415

        end_date = datetime.now().strftime("%Y-%m-%d")
        start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

        result = await self.get_orders(
            sid=sid,
            start_date=start_date,
            end_date=end_date,
            page=1,
            page_size=100
        )

        # Handle ResponseResult Pydantic model - use .data attribute
        orders = result.data if hasattr(result, 'data') else (result.get("data", []) if isinstance(result, dict) else [])
        for order in orders:
            if order.get("amazon_order_id") == amazon_order_id:
                return order

        return None

    async def get_orders_by_date_range(
        self,
        sid: int | None = None,
        sid_list: list[int] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        length: int = 1000
    ) -> list[dict[str, Any]]:
        """获取指定日期范围内的所有订单

        便捷方法，自动处理分页，返回所有订单。

        Args:
            sid: 店铺ID（可选，不传则查询所有店铺）
            sid_list: 店铺ID列表（可选，与sid二选一）
            start_date: 开始日期，格式：YYYY-MM-DD（必填）
            end_date: 结束日期，格式：YYYY-MM-DD（必填）
            length: 每页数量，默认1000

        Returns:
            所有订单列表
        """
        all_orders = []
        offset = 0
        total = None

        while True:
            result = await self.get_orders(
                sid=sid,
                sid_list=sid_list,
                start_date=start_date,
                end_date=end_date,
                offset=offset,
                length=length
            )

            # Handle ResponseResult Pydantic model - use .data attribute
            orders = result.data if hasattr(result, 'data') else (result.get("data", []) if isinstance(result, dict) else [])
            if not orders:
                break

            all_orders.extend(orders)

            if total is None:
                total = result.total if hasattr(result, 'total') else (result.get("total", 0) if isinstance(result, dict) else 0)

            if len(all_orders) >= total:
                break

            offset += length

        return all_orders

    async def get_order_details(self, amazon_order_id: str, sid: int) -> dict[str, Any]:
        """获取订单完整详情（包含商品信息）

        便捷方法，返回订单信息和商品信息的组合。

        Args:
            amazon_order_id: 亚马逊订单ID
            sid: 店铺ID

        Returns:
            完整订单详情:
            {
                "order": {...},
                "items": [...]
            }
        """
        order = await self.get_order_by_id(amazon_order_id, sid)
        items = await self.get_order_items(amazon_order_id)

        return {
            "order": order,
            "items": items
        }

    async def get_active_listings(self, sid: int, limit: int = 1000) -> list[dict[str, Any]]:
        """获取活跃的Listing列表

        便捷方法，只返回状态为Active的Listing。

        Args:
            sid: 店铺ID
            limit: 最大返回数量，默认1000

        Returns:
            活跃的Listing列表
        """
        result = await self.get_listings(
            sid=sid,
            offset=0,
            length=limit,
            status="Active"
        )

        # Handle ResponseResult Pydantic model - use .data attribute
        return result.data if hasattr(result, 'data') else (result.get("data", []) if isinstance(result, dict) else [])

    async def get_listing_by_sku(self, sid: int, sku: str) -> dict[str, Any] | None:
        """根据SKU获取Listing信息

        便捷方法，通过SKU查询单个Listing。

        Args:
            sid: 店铺ID
            sku: 产品SKU

        Returns:
            Listing信息字典，如果不存在返回None
        """
        result = await self.get_listings(
            sid=sid,
            sku_list=[sku],
            length=1
        )

        # Handle ResponseResult Pydantic model - use .data attribute
        listings = result.data if hasattr(result, 'data') else (result.get("data", []) if isinstance(result, dict) else [])
        return listings[0] if listings else None

    # ==================== 订单详情 API ====================

    async def get_order_details_batch(
        self,
        order_ids: list[str],
    ) -> dict[str, Any]:
        """批量查询订单详情

        POST /erp/sc/data/mws/orderDetail

        Args:
            order_ids: 亚马逊订单号列表，多个使用英文逗号分隔，上限200

        Returns:
            包含订单详情的字典:
            {
                "data": [
                    {
                        "amazon_order_id": "209-3501178-3501387",
                        "fulfillment_channel": "AFN",
                        "order_status": "Shipped",
                        "order_total_amount": 5.49,
                        "currency": "GBP",
                        "purchase_date_local": "2021-01-01 00:08:26",
                        "item_list": [...]
                    }
                ]
            }
        """
        data = {
            "order_id": ",".join(order_ids) if isinstance(order_ids, list) else order_ids
        }

        return await self.client.post(
            "/erp/sc/data/mws/orderDetail",
            req_body=data
        )

    # ==================== 多渠道订单 API ====================

    async def get_mcf_orders(
        self,
        sids: list[int] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        date_type: int = 1,
        order_status: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """查询亚马逊多渠道订单列表 (v2)

        POST /order/amzod/api/orderList

        Args:
            sids: 店铺ID列表
            start_date: 订购时间-开始，格式：Y-m-d，不传默认最近6个月
            end_date: 订购时间-结束，格式：Y-m-d，不传默认最近6个月
            date_type: 查询日期类型：1 订购时间【默认】，2 订单修改时间
            order_status: 订单状态列表，枚举值：NEW, RECEIVED, PLANNING, PROCESSING,
                         CANCELLED, COMPLETE, COMPLETE_PARTIALLED, UNFULFILLABLE, INVALID
            offset: 分页偏移量，默认0
            length: 分页长度，默认10，上限1000

        Returns:
            多渠道订单列表
        """
        data = {
            "offset": offset,
            "length": length,
            "date_type": date_type,
        }

        if sids:
            data["sids"] = sids
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        if order_status:
            data["order_status"] = order_status

        return await self.client.post(
            "/order/amzod/api/orderList",
            req_body=data
        )

    async def get_mcf_order_product_info(
        self,
        order_info: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """查询亚马逊多渠道订单详情-商品信息

        POST /order/amzod/api/orderDetails/productInformation

        Args:
            order_info: 订单信息列表，上限200
                [{"sid": 17, "seller_fulfillment_order_id": "quan332122-R"}]

        Returns:
            多渠道订单商品信息
        """
        return await self.client.post(
            "/order/amzod/api/orderDetails/productInformation",
            data={"order_info": order_info}
        )

    async def get_mcf_order_logistics_info(
        self,
        order_info: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """查询亚马逊多渠道订单详情-物流信息

        POST /order/amzod/api/orderDetails/logisticsInformation

        Args:
            order_info: 订单信息列表，上限200
                [{"sid": 17, "seller_fulfillment_order_id": "quan332122-R"}]

        Returns:
            多渠道订单物流信息，包含追踪号、承运商等
        """
        return await self.client.post(
            "/order/amzod/api/orderDetails/logisticsInformation",
            data={"order_info": order_info}
        )

    async def get_mcf_order_return_info(
        self,
        order_info: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """查询亚马逊多渠道订单详情-退货换货信息

        POST /order/amzod/api/orderDetails/returnInformation

        Args:
            order_info: 订单信息列表，上限200
                [{"sid": 17, "seller_fulfillment_order_id": "quan332122-R"}]

        Returns:
            多渠道订单退货换货信息
        """
        return await self.client.post(
            "/order/amzod/api/orderDetails/returnInformation",
            data={"order_info": order_info}
        )

    async def get_mcf_order_transactions(
        self,
        sid: int,
        amazon_order_id: str,
    ) -> dict[str, Any]:
        """查询多渠道订单交易明细

        POST /basicOpen/openapi/salesOrder/multi-channel/list/transaction

        Args:
            sid: 店铺ID
            amazon_order_id: 亚马逊订单ID

        Returns:
            多渠道订单交易明细，包含费用详情
        """
        return await self.client.post(
            "/basicOpen/openapi/salesOrder/multi-channel/list/transaction",
            data={
                "sid": sid,
                "amazonOrderId": amazon_order_id
            }
        )

    async def create_mcf_order(
        self,
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
        item_list: list[dict[str, Any]],
        city: str | None = None,
        address2: str | None = None,
        phone_number: str | None = None,
        is_blank_box: str = "否",
        is_block_amzl: str = "否",
        remark_for_packing: str | None = None,
        delivery_operation: str | None = None,
        delivery_service: str | None = None,
        remark: str | None = None,
    ) -> dict[str, Any]:
        """创建亚马逊多渠道订单

        POST /order/amzod/api/createOrder

        Args:
            store_name: 店铺名
            country: 店铺国家
            order_id: 订单号
            receiver: 收件人
            country_code: 收货地址国家/地区（简码）
            region: 地区
            address1: 地址1
            postcode: 邮编
            buyers_mailbox: 买家邮箱
            order_id_for_packing: 装箱单-订单号
            date_for_packing: 装箱单-订单日期
            item_list: 商品列表，包含 msku, quantity_shipped, declared_value 等
            city: 城市（日本市场非必填）
            address2: 地址2
            phone_number: 电话号码
            is_blank_box: 是否使用无品牌包装箱
            is_block_amzl: 是否阻止亚马逊物流
            remark_for_packing: 装箱单备注
            delivery_operation: 配送操作（"立即配送"/"保留订单"）
            delivery_service: 配送服务（"标准配送"/"加急配送"/"优先配送"）
            remark: 订单备注

        Returns:
            创建结果
        """
        data = {
            "store_name": store_name,
            "country": country,
            "order_id": order_id,
            "is_blank_box": is_blank_box,
            "is_block_amzl": is_block_amzl,
            "receiver": receiver,
            "country_code": country_code,
            "region": region,
            "address1": address1,
            "postcode": postcode,
            "buyers_mailbox": buyers_mailbox,
            "order_id_for_packing": order_id_for_packing,
            "date_for_packing": date_for_packing,
            "item_list": item_list,
        }

        if city:
            data["city"] = city
        if address2:
            data["address2"] = address2
        if phone_number:
            data["phone_number"] = phone_number
        if remark_for_packing:
            data["remark_for_packing"] = remark_for_packing
        if delivery_operation:
            data["delivery_operation"] = delivery_operation
        if delivery_service:
            data["delivery_service"] = delivery_service
        if remark:
            data["remark"] = remark

        return await self.client.post(
            "/order/amzod/api/createOrder",
            req_body=data
        )

    async def cancel_mcf_order(
        self,
        sid: int,
        seller_fulfillment_order_id: str,
    ) -> dict[str, Any]:
        """取消多渠道订单

        POST /order/amzod/api/cancelOrder

        Args:
            sid: 店铺ID
            seller_fulfillment_order_id: 卖家订单号

        Returns:
            取消结果
        """
        return await self.client.post(
            "/order/amzod/api/cancelOrder",
            data={
                "sid": sid,
                "seller_fulfillment_order_id": seller_fulfillment_order_id
            }
        )

    async def set_order_remark(
        self,
        sid: int,
        amazon_order_id: str,
        remark: str,
    ) -> dict[str, Any]:
        """设置SC订单备注

        POST /basicOpen/platformOrder/scOrder/setRemark

        Args:
            sid: 店铺ID
            amazon_order_id: 订单ID
            remark: 备注

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/platformOrder/scOrder/setRemark",
            data={
                "sid": sid,
                "amazonOrderId": amazon_order_id,
                "remark": remark
            }
        )

    # ==================== 售后订单 API ====================

    async def get_after_sale_orders(
        self,
        start_date: str,
        end_date: str,
        sid: str | None = None,
        date_type: int = 1,
        after_type: str | None = None,
        offset: int = 0,
        length: int = 1000,
        amazon_order_id_list: list[str] | None = None,
    ) -> dict[str, Any]:
        """查询售后订单列表

        POST /erp/sc/routing/amzod/order/afterSaleList

        Args:
            start_date: 查询时间-开始，格式：Y-m-d
            end_date: 查询时间-结束，格式：Y-m-d
            sid: 店铺ID，多个使用英文逗号分隔
            date_type: 查询时间类型：1 售后时间【默认】，2 订购时间，3 更新时间
            after_type: 售后类型，多个使用英文逗号分隔：1 退款，2 退货，3 换货
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            amazon_order_id_list: 亚马逊订单ID列表，上限50

        Returns:
            售后订单列表，包含退款、退货、换货信息
        """
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "date_type": date_type,
            "offset": offset,
            "length": length,
        }

        if sid:
            data["sid"] = sid
        if after_type:
            data["after_type"] = after_type
        if amazon_order_id_list:
            data["amazon_order_id_list"] = amazon_order_id_list

        return await self.client.post(
            "/erp/sc/routing/amzod/order/afterSaleList",
            req_body=data
        )

    # ==================== Listing 管理 API ====================

    async def update_listing_price(
        self,
        pricing_params: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """批量修改Listing价格

        POST /erp/sc/listing/ProductPricing/pricingSubmit

        价格幅度不超50%

        Args:
            pricing_params: 调价参数列表
                [{
                    "sid": 1,
                    "msku": "MSKU679E6BF",
                    "standard_price": 16.99,
                    "sale_price": 11.99,
                    "start_date": "2023-02-10",
                    "end_date": "2023-02-11"
                }]

        Returns:
            调价结果，包含成功数和失败详情
        """
        return await self.client.post(
            "/erp/sc/listing/ProductPricing/pricingSubmit",
            data={"pricing_params": pricing_params}
        )

    async def get_listing_prices(
        self,
        data: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """批量获取Listing费用（FBA预估费）

        POST /listing/listing/open/api/listing/getPrices

        Args:
            data: 请求数据列表，上限500
                [{"sid": 46545, "msku": "ABC-MSKU"}]

        Returns:
            Listing费用信息，包含FBA预估费
        """
        return await self.client.post(
            "/listing/listing/open/api/listing/getPrices",
            data={"data": data}
        )

    async def update_fbm_inventory(
        self,
        fbm_inventory_list: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """修改FBM库存和处理时间

        POST /basicOpen/FbmManagement/modifyFbmInventory

        Args:
            fbm_inventory_list: 修改库存列表，单次最多200个元素
                [{
                    "storeId": 6,
                    "msku": "EXAMPLE-MSKU-123",
                    "fbmInventory": 4213,
                    "shipDays": "1"
                }]

        Returns:
            修改结果，包含成功数和失败详情
        """
        return await self.client.post(
            "/basicOpen/FbmManagement/modifyFbmInventory",
            data={"fbmInventoryList": fbm_inventory_list}
        )

    async def update_b2b_price(
        self,
        content: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """修改B2B价格

        POST /basicOpen/b2bPrice/modifyPrice

        Args:
            content: B2B售价列表
                [{
                    "sid": 31,
                    "msku": "7K-YYWO-O4GB",
                    "asin": "B09S9XCP1T",
                    "b2b_price": "1.00"
                }]

        Returns:
            修改结果
        """
        return await self.client.post(
            "/basicOpen/b2bPrice/modifyPrice",
            data={"content": content}
        )

    async def link_listing_pairs(
        self,
        data: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """批量添加编辑Listing配对

        POST /erp/sc/storage/product/link

        推送Listing与本地仓库SKU的配对关系

        Args:
            data: 配对数据列表
                [{
                    "seller_id": "A4373BD6018725",
                    "marketplace_id": "xxxxxxxxxxxxxxxx",
                    "msku": "xxxx",
                    "sku": "xxx",
                    "is_sync_pic": 0
                }]

        Returns:
            配对结果，包含成功数和失败数
        """
        return await self.client.post(
            "/erp/sc/storage/product/link",
            data={"data": data}
        )

    async def unlink_listing_pairs(
        self,
        list_data: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """解除Listing配对

        POST /basicOpen/listingManage/unLinkListingPairs

        Args:
            list_data: 解除配对列表
                [{"storeId": 31, "msku": "09-CJWX-DFQH"}]

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/listingManage/unLinkListingPairs",
            data={"list": list_data}
        )

    async def update_listing_principal(
        self,
        sid_asin_list: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """批量分配Listing负责人

        POST /listing/listing/open/api/asin/updatePrincipal

        Args:
            sid_asin_list: ASIN负责人分配信息，最多支持200个
                [{
                    "sid": 16,
                    "asin": "B09JK94H12",
                    "principal_name": ["小明"]
                }]

        Returns:
            分配结果
        """
        return await self.client.post(
            "/listing/listing/open/api/asin/updatePrincipal",
            data={"sid_asin_list": sid_asin_list}
        )

    async def add_listing_tag(
        self,
        tag_name: str,
    ) -> dict[str, Any]:
        """添加Listing标签

        POST /basicOpen/globalTag/listing/addTag

        Args:
            tag_name: 标签名称

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/globalTag/listing/addTag",
            data={"tag_name": tag_name}
        )

    async def remove_listing_tag(
        self,
        tag_ids: list[str],
    ) -> dict[str, Any]:
        """删除Listing标签

        POST /basicOpen/globalTag/listing/removeTag

        Args:
            tag_ids: 标签ID列表，上限200

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/globalTag/listing/removeTag",
            data={"tag_ids": tag_ids}
        )

    async def get_listing_operation_logs(
        self,
        sid: int,
        msku: str,
        offset: int = 0,
        length: int = 20,
        operate_uid: list[int] | None = None,
        operate_type: list[int] | None = None,
        operate_time_start: str | None = None,
        operate_time_end: str | None = None,
    ) -> dict[str, Any]:
        """查询Listing操作日志列表

        POST /basicOpen/listingManage/listingOperateLog/pageList

        Args:
            sid: 店铺ID
            msku: MSKU
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            operate_uid: 操作人ID列表
            operate_type: 操作类型列表：1 调价，2 调库存，3 修改标题，4 编辑商品，5 B2B调价
            operate_time_start: 开始时间，格式：Y-m-d H:i:s
            operate_time_end: 结束时间，格式：Y-m-d H:i:s

        Returns:
            操作日志列表
        """
        data = {
            "sid": sid,
            "msku": msku,
            "offset": offset,
            "length": length,
        }

        if operate_uid:
            data["operate_uid"] = operate_uid
        if operate_type:
            data["operate_type"] = operate_type
        if operate_time_start:
            data["operate_time_start"] = operate_time_start
        if operate_time_end:
            data["operate_time_end"] = operate_time_end

        return await self.client.post(
            "/basicOpen/listingManage/listingOperateLog/pageList",
            req_body=data
        )

    async def get_price_adjustment_queue(
        self,
        offset: int = 0,
        length: int = 20,
        sid: list[int] | None = None,
        processing_status: list[int] | None = None,
        time_type: int = 1,
        start_time: str | None = None,
        end_time: str | None = None,
        search_field: str | None = None,
        search_value: list[str] | None = None,
        tab_status: int = 0,
    ) -> dict[str, Any]:
        """查询调价队列

        POST /basicOpen/module/adjustPrice/AdjustPriceManual

        Args:
            offset: 偏移量
            length: 页长度，上限500
            sid: 搜索店铺ID列表
            processing_status: 调价状态列表：1 待调价，2 调价中，3 调价成功，
                              4 调价失败，5 审批中，6 已驳回，7 已作废
            time_type: 搜索时间类型：1 创建时间，2 完成时间
            start_time: 开始时间
            end_time: 结束时间
            search_field: 搜索字段：msku, asin
            search_value: 搜索值
            tab_status: tab状态栏：0 全部，1 待审批，2 调价中，3 成功，4 失败，5 已作废

        Returns:
            调价队列列表
        """
        data = {
            "offset": offset,
            "length": length,
            "time_type": time_type,
            "tab_status": tab_status,
        }

        if sid:
            data["sid"] = sid
        if processing_status:
            data["processing_status"] = processing_status
        if start_time:
            data["start_time"] = start_time
        if end_time:
            data["end_time"] = end_time
        if search_field:
            data["search_field"] = search_field
        if search_value:
            data["search_value"] = search_value

        return await self.client.post(
            "/basicOpen/module/adjustPrice/AdjustPriceManual",
            req_body=data
        )

    # ==================== 刊登管理 API ====================

    async def get_amazon_root_categories(
        self,
        store_id: int,
    ) -> dict[str, Any]:
        """查询Amazon根分类

        POST /basicOpen/openapi/publish/manage/categoryRoot

        Args:
            store_id: 店铺ID

        Returns:
            根分类列表
        """
        return await self.client.post(
            "/basicOpen/openapi/publish/manage/categoryRoot",
            data={"storeId": store_id}
        )

    async def get_amazon_child_categories(
        self,
        store_id: int,
        category_unique_id: int,
    ) -> dict[str, Any]:
        """查询Amazon子分类

        POST /basicOpen/openapi/publish/manage/categoryChildren

        Args:
            store_id: 店铺ID
            category_unique_id: 类目唯一ID

        Returns:
            子分类列表
        """
        return await self.client.post(
            "/basicOpen/openapi/publish/manage/categoryChildren",
            data={
                "storeId": store_id,
                "categoryUniqueId": category_unique_id
            }
        )

    async def get_publish_results(
        self,
        record_unique_id: int | None = None,
        sku: str | None = None,
        store_id: int | None = None,
        operate_time: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """查询刊登结果

        POST /listing/publish/openapi/amazon/product/list

        Args:
            record_unique_id: 批次唯一ID
            sku: SKU
            store_id: 店铺ID
            operate_time: 操作时间范围 {"start": "", "end": ""}

        Returns:
            刊登结果列表
        """
        data = {}

        if record_unique_id:
            data["record_unique_id"] = record_unique_id
        if sku:
            data["sku"] = sku
        if store_id:
            data["store_id"] = store_id
        if operate_time:
            data["operate_time"] = operate_time

        return await self.client.post(
            "/listing/publish/openapi/amazon/product/list",
            req_body=data
        )

    async def get_product_type_schema(
        self,
        marketplace_id: str,
        product_type_origin: str,
    ) -> dict[str, Any]:
        """获取指定productType的JSON Schema

        POST /basicOpen/openapi/publish/manage/getProductType

        Args:
            marketplace_id: 市场ID
            product_type_origin: 商品原始类型

        Returns:
            商品类型的JSON Schema
        """
        return await self.client.post(
            "/basicOpen/openapi/publish/manage/getProductType",
            data={
                "marketplaceId": marketplace_id,
                "productTypeOrigin": product_type_origin
            }
        )

    async def get_shipping_template(
        self,
        seller_id: str,
        marketplace_id: str,
        product_type: str,
        flag: int = 0,
    ) -> dict[str, Any]:
        """获取运费模板

        POST /basicOpen/openapi/publish/manage/getMerchantShippingGroup

        Args:
            seller_id: 店铺ID
            marketplace_id: 市场ID
            product_type: 商品原始类目
            flag: 默认传0，返回为空则传1实时请求亚马逊获取最新数据

        Returns:
            运费模板列表
        """
        return await self.client.post(
            "/basicOpen/openapi/publish/manage/getMerchantShippingGroup",
            data={
                "sellerId": seller_id,
                "marketplaceId": marketplace_id,
                "productType": product_type,
                "flag": flag
            }
        )

    # ==================== Listing 标签管理 API ====================

    async def bind_listing_tag(
        self,
        bind_detail: list[dict[str, Any]],
        tag_ids: list[str],
    ) -> dict[str, Any]:
        """Listing新增商品标签

        POST /basicOpen/listingManage/bindListingAndTag

        Args:
            bind_detail: 配对信息列表
                [{"sid": 17, "relationId": "HOLDER001"}]
            tag_ids: 标签ID数组

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/listingManage/bindListingAndTag",
            data={
                "bindDetail": bind_detail,
                "tagIds": tag_ids
            }
        )

    async def remove_listing_and_tag(
        self,
        bind_detail: list[dict[str, Any]],
        global_tag_ids: list[str],
    ) -> dict[str, Any]:
        """Listing删除商品标签

        POST /basicOpen/listingManage/removeListingAndTag

        Args:
            bind_detail: 配对信息列表
                [{"sid": 17, "relationId": "HOLDER001"}]
            global_tag_ids: 标签ID数组

        Returns:
            操作结果
        """
        return await self.client.post(
            "/basicOpen/listingManage/removeListingAndTag",
            data={
                "bindDetail": bind_detail,
                "glabalTagIds": global_tag_ids  # 注意：API文档中的拼写是glabalTagIds
            }
        )

    async def get_listing_tag_list(
        self,
        bind_detail: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """查询Listing标记标签列表

        POST /basicOpen/listingManage/queryListingRelationTagList

        Args:
            bind_detail: listing数据，上限100
                [{"sid": 17, "relation_id": "HOLDER001"}]

        Returns:
            Listing标签列表
        """
        return await self.client.post(
            "/basicOpen/listingManage/queryListingRelationTagList",
            data={"bind_detail": bind_detail}
        )

    # ==================== FBA费差异异常订单 API ====================

    async def get_fba_fee_difference_by_msku(
        self,
        offset: int = 0,
        length: int = 20,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[int] | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
    ) -> dict[str, Any]:
        """FBA费差异-异常订单-MSKU维度

        POST /basicOpen/openapi/sale/fbaFeeDifference/msku/list

        Args:
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            start_date: 开始时间（结算时间），格式：Y-m-d
            end_date: 结束时间（结算时间），格式：Y-m-d
            sids: 店铺ID列表
            search_field: 搜索字段：msku
            search_value: 搜索值，多个使用英文逗号分隔，上限200

        Returns:
            MSKU维度的FBA费差异异常订单
        """
        data = {
            "offset": offset,
            "length": length,
        }

        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        if sids:
            data["sids"] = sids
        if search_field:
            data["search_field"] = search_field
        if search_value:
            data["search_value"] = search_value

        return await self.client.post(
            "/basicOpen/openapi/sale/fbaFeeDifference/msku/list",
            req_body=data
        )

    async def get_fba_fee_difference_by_order(
        self,
        offset: int = 0,
        length: int = 20,
        start_date: str | None = None,
        end_date: str | None = None,
        sids: list[int] | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
    ) -> dict[str, Any]:
        """FBA费差异-异常订单-订单维度

        POST /basicOpen/openapi/sale/fbaFeeDifference/order/list

        Args:
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            start_date: 开始时间（结算时间），格式：Y-m-d
            end_date: 结束时间（结算时间），格式：Y-m-d
            sids: 店铺ID列表
            search_field: 搜索字段：order_id 订单号，msku MSKU
            search_value: 搜索值，多个使用英文逗号分隔，上限200

        Returns:
            订单维度的FBA费差异异常订单
        """
        data = {
            "offset": offset,
            "length": length,
        }

        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        if sids:
            data["sids"] = sids
        if search_field:
            data["search_field"] = search_field
        if search_value:
            data["search_value"] = search_value

        return await self.client.post(
            "/basicOpen/openapi/sale/fbaFeeDifference/order/list",
            req_body=data
        )

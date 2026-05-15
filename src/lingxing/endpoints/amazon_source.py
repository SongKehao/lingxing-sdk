"""Amazon source data API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class AmazonSourceEndpoints:
    """Amazon source data API endpoints."""

    def __init__(self, openapi: OpenApiBase):
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== 库存报表API ====================

    async def get_daily_inventory(
        self,
        access_token: str,
        sid: int,
        event_date: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询每日库存报表

        API: POST /erp/sc/data/mws_report/dailyInventory

        注意: 由于亚马逊对应报表下线，2023年12月1日后不再更新此接口数据，
              获取数据请使用查询库存分类账summary数据

        Args:
            access_token: 访问令牌
            sid: 店铺ID（欧洲传UK下的店铺，美国传US下的店铺）
            event_date: 报表日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - snapshot_date: 快照时间
                - fnsku: FNSKU
                - sku: SKU
                - product_name: 品名
                - quantity: 数量
                - fulfillment_center_id: 存储库存的运营中心
                - detailed_disposition: 商品状态
                - country: 库存存放地所在的国家/地区代码

        Example:
            >>> result = await amazon_source.get_daily_inventory(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     event_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching daily inventory: sid=%s, event_date=%s", sid, event_date)

        req_body = {
            "sid": sid,
            "event_date": event_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/dailyInventory",
            req_body=req_body
        )

    async def get_fba_inventory(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA库存报表 (FBA Manage Inventory)

        API: POST /erp/sc/data/mws_report/manageInventory
        验证状态: 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sku: MSKU
                - fnsku: FNSKU
                - asin: ASIN
                - product_name: 品名
                - condition: 商品的状况
                - mfn_listing_exists: 商品是否由卖家自行配送
                - mfn_fulfillable_quantity: 卖家配送可取件数量
                - afn_listing_exists: 商品是否由亚马逊物流配送
                - afn_warehouse_quantity: 亚马逊运营中心已处理商品数量
                - afn_fulfillable_quantity: 亚马逊运营中心可取件数量
                - afn_unsellable_quantity: 不可售商品数量
                - afn_reserved_quantity: 预留商品数量
                - afn_total_quantity: 总数量
                - your_price: 当前销售价格
                - gmt_modified: 更新时间

        Example:
            >>> result = await amazon_source.get_fba_inventory(
            ...     access_token="xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching FBA inventory: sid=%s", sid)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/manageInventory",
            req_body=req_body
        )

    async def get_fba_fulfillable_quantity(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA可售库存报表 (FBA Multi-Country Inventory Report)

        API: POST /erp/sc/data/mws_report/getAfnFulfillableQuantity
        验证状态: 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - seller_sku: 销售SKU
                - fnsku: FNSKU
                - asin: ASIN
                - condition_type: 商品成色
                - country: 国家二字码
                - afn_fulfillable_quantity: FBA可售数量
                - gmt_modified: 更新时间

        Example:
            >>> result = await amazon_source.get_fba_fulfillable_quantity(
            ...     access_token="xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching FBA fulfillable quantity: sid=%s", sid)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/getAfnFulfillableQuantity",
            req_body=req_body
        )

    async def get_reserved_inventory(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询预留库存报表 (FBA Reserved Inventory Report)

        API: POST /erp/sc/data/mws_report/reservedInventory

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sku: SKU
                - fnsku: FNSKU
                - asin: ASIN
                - product_name: 品名
                - reserved_qty: 预留数量
                - reserved_customerorders: 为买家订单预留的商品数量
                - reserved_fc_transfers: 预留运营中心转运数量
                - reserved_fc_processing: 预留运营中心处理中数量
                - gmt_modified: 更新时间

        Example:
            >>> result = await amazon_source.get_reserved_inventory(
            ...     access_token="xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching reserved inventory: sid=%s", sid)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/reservedInventory",
            req_body=req_body
        )

    async def get_fba_age_list(
        self,
        access_token: str,
        sid: int,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询库龄表 (Manage Inventory Health Report)

        API: POST /erp/sc/routing/fba/fbaStock/getFbaAgeList

        注意: 此API使用sid作为字符串参数，支持多个店铺逗号分隔

        Args:
            access_token: 访问令牌
            sid: 店铺ID（支持多个店铺逗号分隔）
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: {list: [...], total: int}}
                - sid: 店铺ID
                - snapshot_date: 生成报告的日期
                - sku: SKU
                - fnsku: FNSKU
                - asin: ASIN
                - product_name: 商品名称
                - condition: 商品的状况
                - available: 可售数量
                - inv_age_0_to_90_days: 0-90天库龄数量
                - inv_age_91_to_180_days: 91-180天库龄数量
                - inv_age_181_to_270_days: 181-270天库龄数量
                - inv_age_271_to_365_days: 271-365天库龄数量
                - inv_age_365_plus_days: 超过365天库龄数量
                - currency: 货币
                - qty_to_be_charged_ltsf_6_mo: 180天长期仓储费商品数量
                - qty_to_be_charged_ltsf_12_mo: 超过365天商品数量
                - 等更多字段...

        Example:
            >>> result = await amazon_source.get_fba_age_list(
            ...     access_token="xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching FBA age list: sid=%s", sid)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fba/fbaStock/getFbaAgeList",
            req_body=req_body
        )

    # ==================== 订单报表API ====================

    async def get_all_orders(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        date_type: int = 1,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询所有订单报表 (All Orders Report By last update)

        API: POST /erp/sc/data/mws_report/allOrders
        验证状态: 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            date_type: 时间查询类型，1=下单日期（默认），2=亚马逊订单更新时间
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - amazon_order_id: 亚马逊订单号
                - merchant_order_id: 卖家为订单提供的唯一编号
                - last_updated_time: 订单最近更新时间
                - purchase_date: 下单日期
                - shipment_date: 发货时间
                - order_status: 订单的当前状态
                - fulfillment_channel: 订单的配送方式 (Amazon/Merchant)
                - sales_channel: 下单渠道
                - ship_service_level: 配送服务类型
                - sku: MSKU
                - asin: ASIN
                - product_name: 品名
                - item_status: 该商品在订单内的当前状态
                - quantity: 此商品的购买数量
                - currency: 币种
                - item_price: 买家为商品支付的金额
                - shipping_price: 买家支付的运费金额
                - 等更多字段...

        Example:
            >>> result = await amazon_source.get_all_orders(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching all orders: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/allOrders",
            req_body=req_body
        )

    async def get_fba_orders(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        date_type: int = 1,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA订单报表 (Amazon-Fulfilled Shipments Report)

        API: POST /erp/sc/data/mws_report/fbaOrders
        验证状态: 已验证 (2026-02-24)

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            date_type: 日期搜索维度，1=下单日期（默认），2=配送日期
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - amazon_order_id: 订单号
                - shipment_id: 配送ID
                - shipment_item_id: 配送子ID
                - amazon_order_item_id: 订单子项ID
                - purchase_date: 下单日期
                - payments_date: 支付日期
                - shipment_date: 配送日期
                - reporting_date: 报表日期
                - estimated_arrival_date: 预计送达日期
                - sku: SKU
                - product_name: 品名
                - quantity_shipped: 数量
                - currency: 币种
                - item_price: 商品金额
                - shipping_price: 运费金额
                - carrier: 运输方
                - tracking_number: 快递号
                - fulfillment_channel: 配送方式 (AFN/MFN)
                - 等更多字段...

        Example:
            >>> result = await amazon_source.get_fba_orders(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching FBA orders: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "date_type": date_type,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/fbaOrders",
            req_body=req_body
        )

    async def get_fba_exchange_orders(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA换货订单报表 (Replacements Report)

        API: POST /erp/sc/routing/data/order/fbaExchangeOrderList

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 开始日期，格式 YYYY-MM-DD
            end_date: 结束日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - order_hash: 订单唯一hash
                - sid: 店铺ID
                - replacement_amazon_order_id: 换货订单号
                - shipment_date: 换货时间
                - asin: ASIN
                - seller_sku: MSKU
                - original_amazon_order_id: 原始订单号
                - fulfillment_center_id: 换货仓库
                - original_fulfillment_center_id: 原始仓库
                - quantity: 换货数量
                - replacement_reason_code: 换货原因
                - sync_time: 数据同步时间戳

        Example:
            >>> result = await amazon_source.get_fba_exchange_orders(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching FBA exchange orders: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/data/order/fbaExchangeOrderList",
            req_body=req_body
        )

    async def get_removal_orders(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        search_field_time: str = "last_updated_date",
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询移除订单报表 (Reports-Fulfillment-Removal Order Detail)

        API: POST /erp/sc/routing/data/order/removalOrderListNew

        注意: 报表为seller_id维度，按sid请求会返回对应seller_id下所有移除订单数据

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            start_date: 查询时间（更新时间），格式 YYYY-MM-DD
            end_date: 查询时间（更新时间），格式 YYYY-MM-DD
            search_field_time: 搜索时间类型，last_updated_date（默认）或 request_date
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - seller_id: 亚马逊店铺ID
                - sid: 店铺ID（为0代表未确定订单店铺）
                - region: 地区
                - request_date: 订单日期
                - order_id: 订单号
                - order_type: 订单类型
                - order_status: 订单状态
                - last_updated_date: 更新时间
                - sku: MSKU
                - fnsku: FNSKU
                - disposition: 库存属性
                - requested_quantity: 请求数量
                - cancelled_quantity: 取消数量
                - disposed_quantity: 已处置数量
                - shipped_quantity: 已发货数量
                - in_process_quantity: 处置中数量
                - removal_fee: 移除费用
                - currency: 币种
                - address_detail: 配送地址
                - local_sku: 本地SKU
                - local_name: 品名

        Example:
            >>> result = await amazon_source.get_removal_orders(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching removal orders: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "search_field_time": search_field_time,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/data/order/removalOrderListNew",
            req_body=req_body
        )

    async def get_removal_shipments(
        self,
        access_token: str,
        sid: int,
        start_date: str,
        end_date: str,
        seller_id: str | None = None,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询移除货件报表 (Reports-Fulfillment-Removal Shipment Detail)

        API: POST /erp/sc/statistic/removalShipment/list

        注意: 报表为seller_id维度，按sid请求会返回对应seller_id下所有移除订单数据，
              同一个seller_id授权的店铺任取一个sid请求报表数据即可

        Args:
            access_token: 访问令牌
            sid: 店铺ID（seller_id同时传值时，以sid为准）
            start_date: 开始日期（发货日期），格式 YYYY-MM-DD
            end_date: 结束日期（发货日期），格式 YYYY-MM-DD
            seller_id: 亚马逊店铺ID（可选）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - mid: 站点ID
                - seller_id: 亚马逊店铺ID
                - seller_account_name: 店铺账号名称
                - marketplace: 市场
                - uuid_new: 业务标识
                - uuid_num_new: 业务标识-序号
                - order_id: 移除订单号
                - sku: MSKU
                - fnsku: FNSKU
                - disposition: 库存属性
                - shipped_quantity: 发货数量
                - carrier: 承运商
                - tracking_number: 运单号
                - removal_order_type: 移除货件类型
                - overseas_removal_order_no: 移除入库单号
                - shipment_date: 发货日期
                - request_date: 创建时间
                - local_info: 本地产品信息
                - delivery_info: 配送信息

        Example:
            >>> result = await amazon_source.get_removal_shipments(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching removal shipments: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if seller_id:
            req_body["seller_id"] = seller_id

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/statistic/removalShipment/list",
            req_body=req_body
        )

    # ==================== 库存事件API ====================

    async def get_fba_inventory_event_detail(
        self,
        access_token: str,
        sid: int,
        snapshot_date_after: str,
        snapshot_date_before: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA库存事件明细报表 (FBA Inventory Event Detail)

        API: POST /erp/sc/data/mws_report/getFbaInventoryEventDetailList

        注意: 2023年3月后不再更新此接口数据（亚马逊对应报表下线），
              获取之后的数据请使用查询亚马逊库存分类账detail数据

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            snapshot_date_after: 快照开始时间，格式 YYYY-MM-DD（开始结束时间区间支持7天）
            snapshot_date_before: 快照结束时间，格式 YYYY-MM-DD（开始结束时间区间支持7天）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - snapshot_date: 快照时间
                - snapshot_date_locale: 快照时间（本地）
                - snapshot_date_timestamp: 快照时间对应时间戳
                - snapshot_date_report: 快照日期
                - transaction_type: 交易类型
                - fnsku: FNSKU
                - sku: SKU
                - product_name: 商品名称
                - fulfillment_center_id: 运营中心
                - quantity: 数量
                - disposition: 状况

        Example:
            >>> result = await amazon_source.get_fba_inventory_event_detail(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     snapshot_date_after="2026-02-01",
            ...     snapshot_date_before="2026-02-07"
            ... )
        """
        logger.debug("Fetching FBA inventory event detail: sid=%s, after=%s, before=%s", sid, snapshot_date_after, snapshot_date_before)

        req_body = {
            "sid": sid,
            "snapshot_date_after": snapshot_date_after,
            "snapshot_date_before": snapshot_date_before,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/getFbaInventoryEventDetailList",
            req_body=req_body
        )

    async def get_fba_inventory_event_detail_v1(
        self,
        access_token: str,
        sid: int,
        snapshot_date_after: str,
        snapshot_date_before: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA库存事件明细报表V1 (FBA Inventory Event Detail v1)

        API: POST /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList

        注意: 2023年3月后不再更新此接口数据（亚马逊对应报表下线），
              获取之后的数据请使用查询亚马逊库存分类账detail数据

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            snapshot_date_after: 快照开始时间，格式 YYYY-MM-DD（开始结束时间区间支持7天）
            snapshot_date_before: 快照结束时间，格式 YYYY-MM-DD（开始结束时间区间支持7天）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000，上限10000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - snapshot_date: 快照时间
                - snapshot_date_locale: 快照时间（本地）
                - snapshot_date_timestamp: 快照时间对应时间戳
                - snapshot_date_report: 快照日期
                - transaction_type: 交易类型
                - fnsku: FNSKU
                - msku: 亚马逊SKU
                - product_name: 商品名称
                - fulfillment_center_id: 运营中心
                - quantity: 数量
                - disposition: 状况
                - local_name: 品名
                - local_sku: 本地SKU

        Example:
            >>> result = await amazon_source.get_fba_inventory_event_detail_v1(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     snapshot_date_after="2026-02-01",
            ...     snapshot_date_before="2026-02-07"
            ... )
        """
        logger.debug("Fetching FBA inventory event detail v1: sid=%s, after=%s, before=%s", sid, snapshot_date_after, snapshot_date_before)

        req_body = {
            "sid": sid,
            "snapshot_date_after": snapshot_date_after,
            "snapshot_date_before": snapshot_date_before,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList",
            req_body=req_body
        )

    async def get_amazon_fulfilled_shipments_v1(
        self,
        access_token: str,
        sid: int,
        shipment_date_after: str,
        shipment_date_before: str,
        amazon_order_id: list[str] | None = None,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询Amazon Fulfilled Shipments报表V1

        API: POST /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            shipment_date_after: 快照开始时间，格式 YYYY-MM-DD HH:MM:SS（开始结束时间区间支持7天）
            shipment_date_before: 快照结束时间，格式 YYYY-MM-DD HH:MM:SS（开始结束时间区间支持7天）
            amazon_order_id: 亚马逊订单号列表（可选）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - amazon_order_id: 亚马逊订单号
                - merchant_order_id: 卖家订单标识
                - shipment_id: 亚马逊货件编号
                - shipment_item_id: 亚马逊货件商品编号
                - amazon_order_item_id: 亚马逊订单商品编号
                - merchant_order_item_id: 订单商品唯一标识
                - purchase_date: 订单下单日期
                - payments_date: 买家付款处理日期
                - shipment_date: 亚马逊完成货件日期
                - reporting_date: 提供报告数据的日期
                - msku: 亚马逊SKU
                - product_name: 商品名称
                - quantity_shipped: 已配送数量
                - currency: 购物使用的货币
                - item_price: 买家为商品支付的金额
                - shipping_price: 买家支付的运费
                - carrier: 配送包裹的承运人
                - tracking_number: 包裹的追踪编码
                - fulfillment_center_id: 配送订单的运营中心
                - fulfillment_channel: 配送方式 (AFN/MFN)
                - sales_channel: 订单来源
                - local_name: 品名
                - local_sku: 本地SKU

        Example:
            >>> result = await amazon_source.get_amazon_fulfilled_shipments_v1(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     shipment_date_after="2026-02-01 00:00:00",
            ...     shipment_date_before="2026-02-07 00:00:00"
            ... )
        """
        logger.debug("Fetching Amazon fulfilled shipments v1: sid=%s, after=%s, before=%s", sid, shipment_date_after, shipment_date_before)

        req_body = {
            "sid": sid,
            "shipment_date_after": shipment_date_after,
            "shipment_date_before": shipment_date_before,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if amazon_order_id:
            req_body["amazon_order_id"] = amazon_order_id

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList",
            req_body=req_body
        )

    async def get_adjustment_list(
        self,
        access_token: str,
        sids: str,
        start_date: str,
        end_date: str,
        search_field: str | None = None,
        search_value: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询盘存记录报表

        API: POST /basicOpen/openapi/mwsReport/adjustmentList

        Args:
            access_token: 访问令牌
            sids: 店铺ID，多个店铺以英文逗号分隔
            start_date: 发货日期开始时间，格式 YYYY-MM-DD
            end_date: 发货日期结束时间，格式 YYYY-MM-DD
            search_field: 搜索的字段（asin/msku/fnsku/item_name/transaction_item_id）
            search_value: 搜索值
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限10000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - report_date: 发货日期
                - transaction_item_id: 交易编号
                - fnsku: FNSKU
                - msku: MSKU
                - item_name: 标题
                - fulfillment_center_id: 运营中心code
                - quantity: 数量
                - reason: 原因code
                - reason_text: 原因
                - disposition: 库存属性

        Example:
            >>> result = await amazon_source.get_adjustment_list(
            ...     access_token="xxx",
            ...     sids="4661,4662",
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching adjustment list: sids=%s, start=%s, end=%s", sids, start_date, end_date)

        req_body = {
            "sids": sids,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if search_field and search_value:
            req_body["search_field"] = search_field
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/mwsReport/adjustmentList",
            req_body=req_body
        )

    # ==================== 交易报表API ====================

    async def get_transaction_report(
        self,
        access_token: str,
        sid: int,
        event_date: str,
        offset: int = 0,
        length: int = 1000,
        **kwargs
    ) -> ResponseResult:
        """
        查询交易明细报表 (Transaction Report)

        API: POST /erp/sc/data/mws_report/transaction

        注意: 本接口即将下线，建议使用查询结算中心 - 交易明细

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            event_date: 报表日期，格式 YYYY-MM-DD（每月3日后支持查询上月数据）
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {total, data: [...]}
                - sid: 店铺ID
                - is_to_b: 是否为B2B订单（0否/1是）
                - report_date_month: client_task的月份
                - report_index: 报表行索引
                - date_str: 原本的日期字符串
                - date_locale: 当地日期
                - date_iso: ISO时间
                - settlement_id: 结算编号
                - type: 类型（1=ORDER, 2=REFUND, 3=ADJUSTMENT等）
                - type_str: 类型说明
                - order_id: 订单号
                - sku: SKU
                - description: 商品描述
                - quantity: 商品数量
                - marketplace: 销售市场
                - fulfillment: 发货方式
                - product_sales: 销售价格
                - currency: 币种
                - selling_fees: 平台费（佣金）
                - fba_fees: FBA发货费
                - total: 总计

        Example:
            >>> result = await amazon_source.get_transaction_report(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     event_date="2026-02-01"
            ... )
        """
        logger.debug("Fetching transaction report: sid=%s, event_date=%s", sid, event_date)

        req_body = {
            "sid": sid,
            "event_date": event_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/mws_report/transaction",
            req_body=req_body
        )

    # ==================== 报告导出API ====================

    async def create_report_export_task(
        self,
        access_token: str,
        seller_id: str,
        report_type: str,
        marketplace_ids: list[str],
        region: str,
        data_start_time: str | None = None,
        data_end_time: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        创建报告导出任务

        API: POST /basicOpen/report/create/reportExportTask

        Args:
            access_token: 访问令牌
            seller_id: 亚马逊店铺ID
            report_type: 亚马逊报表类型（参见附加说明）
            marketplace_ids: 亚马逊市场ID列表
            region: 店铺所在的地区（na=北美, eu=欧洲, fe=远东）
            data_start_time: 报表请求开始时间，格式 YYYY-MM-DDTHH:MM:SSZ
            data_end_time: 报表请求结束时间，格式 YYYY-MM-DDTHH:MM:SSZ
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {data: {task_id: "xxx"}}

        常用report_type:
            - GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL: 亚马逊配送货件
            - GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL: 所有订单
            - GET_VAT_TRANSACTION_DATA: VAT交易报告
            - GET_RESERVED_INVENTORY_DATA: 预留库存
            - GET_AFN_INVENTORY_DATA: 亚马逊库存
            - GET_FBA_STORAGE_FEE_CHARGES_DATA: 月度仓储费
            - GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA: 管理亚马逊物流库存报告
            - GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA: 亚马逊物流买家退货
            - GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA: 移除订单详情
            - GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA: 移除货件详情

        region说明:
            - na (北美): CA, US, MX, BR
            - eu (欧洲): ES, UK, FR, BE, NL, DE, IT, SE, ZA, PL, EG, TR, SA, AE, IN
            - fe (远东): SG, AU, JP

        Example:
            >>> result = await amazon_source.create_report_export_task(
            ...     access_token="xxx",
            ...     seller_id="A1MQMW3JWPNCBX",
            ...     report_type="GET_AFN_INVENTORY_DATA",
            ...     marketplace_ids=["ATVPDKIXK0"],
            ...     region="na"
            ... )
        """
        logger.debug("Creating report export task: seller_id=%s, report_type=%s, region=%s", seller_id, report_type, region)

        req_body = {
            "seller_id": seller_id,
            "report_type": report_type,
            "marketplace_ids": marketplace_ids,
            "region": region,
            **kwargs
        }

        if data_start_time:
            req_body["data_start_time"] = data_start_time
        if data_end_time:
            req_body["data_end_time"] = data_end_time

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/report/create/reportExportTask",
            req_body=req_body
        )

    async def query_report_export_task(
        self,
        access_token: str,
        seller_id: str,
        task_id: str,
        region: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询报告导出任务结果

        API: POST /basicOpen/report/query/reportExportTask

        Args:
            access_token: 访问令牌
            seller_id: 亚马逊店铺ID
            task_id: 任务ID（创建导出任务返回的task_id）
            region: 店铺所在的地区（na=北美, eu=欧洲, fe=远东）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {data: {...}}
                - report_document_id: 报告文件ID
                - progress_status: 报表生成状态
                    - IN_PROGRESS: 导出中
                    - CANCELLED: 已取消
                    - DONE: 已完成
                    - FATAL: 导出失败
                    - IN_QUEUE: 排队中
                    - UNKNOWN: 未知
                - compression_algorithm: 报表内容压缩方式
                - url: 报表下载地址（有效期5分钟）

        Example:
            >>> result = await amazon_source.query_report_export_task(
            ...     access_token="xxx",
            ...     seller_id="A1MQMW3JWPNCBX",
            ...     task_id="f5345297-07e2-4b08-becf-a4c29335246b",
            ...     region="na"
            ... )
            >>> if result.data.get("progress_status") == "DONE":
            ...     download_url = result.data.get("url")
        """
        logger.debug("Querying report export task: seller_id=%s, task_id=%s", seller_id, task_id)

        req_body = {
            "seller_id": seller_id,
            "task_id": task_id,
            "region": region,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/report/query/reportExportTask",
            req_body=req_body
        )

    async def renew_report_download_url(
        self,
        access_token: str,
        seller_id: str,
        report_document_id: str,
        region: str,
        **kwargs
    ) -> ResponseResult:
        """
        报告下载链接续期

        API: POST /basicOpen/report/amazonReportExportTask

        当报告下载链接过期时，可使用此接口续期获取新的下载链接

        Args:
            access_token: 访问令牌
            seller_id: 亚马逊店铺ID
            report_document_id: 报告文档ID（查询导出任务结果返回的report_document_id）
            region: 店铺所在的地区（na=北美, eu=欧洲, fe=远东）
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含 {data: {...}}
                - url: 亚马逊报告下载链接
                - report_document_id: 报告文档ID

        Example:
            >>> result = await amazon_source.renew_report_download_url(
            ...     access_token="xxx",
            ...     seller_id="A1MQMW3JWPNCBX",
            ...     report_document_id="amzn1.spdoc.1.4.eu.xxx",
            ...     region="na"
            ... )
            >>> download_url = result.data.get("url")
        """
        logger.debug("Renewing report download URL: seller_id=%s, report_document_id=%s", seller_id, report_document_id)

        req_body = {
            "region": region,
            "seller_id": seller_id,
            "report_document_id": report_document_id,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/report/amazonReportExportTask",
            req_body=req_body
        )


__all__ = [
    'AmazonSourceEndpoints',
]

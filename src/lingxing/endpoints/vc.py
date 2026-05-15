"""Amazon VC (Vendor Central) API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class VCEndpoints:
    """Amazon VC (Vendor Central) API endpoints."""

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

    # ==================== 店铺管理 ====================

    async def get_vc_stores(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC店铺列表

        API: POST /basicOpen/platformAuth/vcSeller/pageList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含店铺列表和总数
                - data: 店铺列表
                - total: 总数

        返回字段说明:
            - account_id: 账号ID
            - seller_id: SELLER_ID
            - account_name: 账号名称
            - region: 站点简称
            - region_name: 站点名称
            - vc_store_id: VC店铺ID
            - name: 店铺名称
            - status: 店铺授权服务状态 (-1删除, 0暂停同步, 1正常同步, 2授权异常)
            - mid: 站点ID

        Example:
            >>> result = await vc.get_vc_stores(access_token="xxx")
            >>> stores = result.data  # [{"vc_store_id": "xxx", "name": "VC01-美国", ...}]
        """
        logger.debug("Fetching VC stores: offset=%s, length=%s", offset, length)

        req_body = {
            "offset": offset,
            "length": min(length, 200),  # 上限200
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformAuth/vcSeller/pageList",
            req_body=req_body
        )

    # ==================== Listing管理 ====================

    async def get_vc_listings(
        self,
        access_token: str,
        vc_store_ids: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC Listing列表

        API: POST /basicOpen/listingManage/vcListing/pageList

        Args:
            access_token: 访问令牌
            vc_store_ids: VC店铺ID列表，如 ["134225003201380864"]
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含Listing列表和总数
                - data: Listing列表
                - total: 总数

        返回字段说明:
            - vc_store_id: VC店铺ID
            - asin: ASIN
            - msku: MSKU
            - upc: UPC
            - ean: EAN
            - item_name: 标题
            - parent_asin: 父ASIN
            - local_sku: 本地SKU
            - local_name: 品名
            - category_name: 本地产品分类名
            - product_id: 本地产品ID
            - reviews_num: 评论数
            - stars: 星级
            - status: 在线商品状态 (-1已删除, 0停售, 1在售)
            - price: 优惠金额

        Example:
            >>> result = await vc.get_vc_listings(
            ...     access_token="xxx",
            ...     vc_store_ids=["134225003201380864"]
            ... )
        """
        logger.debug("Fetching VC listings: vc_store_ids=%s, offset=%s, length=%s", vc_store_ids, offset, length)

        req_body = {
            "offset": offset,
            "length": min(length, 200),  # 上限200
            **kwargs
        }

        if vc_store_ids:
            req_body["vc_store_ids"] = vc_store_ids

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/listingManage/vcListing/pageList",
            req_body=req_body
        )

    # ==================== 订单管理 ====================

    async def get_vc_orders(
        self,
        access_token: str,
        purchase_order_type: list[str],
        vc_store_ids: list[str] | None = None,
        search_field_time: str | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        search_field: str | None = None,
        search_value: list[str] | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC订单列表

        API: POST /basicOpen/platformOrder/vcOrder/pageList

        Args:
            access_token: 访问令牌
            purchase_order_type: 订单类型列表，["0"]=DF订单，["1"]=PO订单
            vc_store_ids: VC店铺ID列表，如 ["134225003201380864"]
            search_field_time: 查询时间类型
                - 1: 订购时间
                - 2: 要求发货时间
                - 3: 订单更新时间
            start_date: 开始时间，格式 YYYY-MM-DD（最长不超过90天范围）
            end_date: 结束时间，格式 YYYY-MM-DD（最长不超过90天范围）
            search_field: 搜索类型
                - purchase_order_number: 订单号
                - asin: ASIN
                - local_name: 品名
                - customer_order_number: 客户订单号【DF类型订单】
                - vendor_product_id: 商品编码
            search_value: 搜索值列表
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，上限200
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含订单列表和总数
                - data: 订单列表
                - total: 总数

        返回字段说明:
            - id: 订单ID
            - purchase_order_number: 订单编号
            - customer_order_number: 客户订单号【DF类型订单】
            - vc_store_id: VC店铺ID
            - seller_name: 店铺名称
            - purchase_order_type: 订单类型 (0=DF, 1=PO)
            - purchase_order_state: 订单状态
            - purchase_order_process_state: 订单流转状态 (0待处理, 1待发货, 2已完成, 3已取消)
            - purchase_order_date: 订单下单时间
            - total_price: 订单总金额
            - currency_code: 币种
            - item_amount: 货物总数量
            - local_po_number: 本地PO号
            - purchase_order_sku_list: 订单商品明细数据

        Example:
            >>> result = await vc.get_vc_orders(
            ...     access_token="xxx",
            ...     purchase_order_type=["0"],  # DF订单
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug(
            "Fetching VC orders: purchase_order_type=%s, "
            "vc_store_ids=%s, start=%s, end=%s",
            purchase_order_type, vc_store_ids, start_date, end_date,
        )

        req_body = {
            "purchase_order_type": purchase_order_type,
            "offset": offset,
            "length": min(length, 200),  # 上限200
            **kwargs
        }

        if vc_store_ids:
            req_body["vc_store_ids"] = vc_store_ids
        if search_field_time:
            req_body["search_field_time"] = search_field_time
        if start_date:
            req_body["start_date"] = start_date
        if end_date:
            req_body["end_date"] = end_date
        if search_field:
            req_body["search_field"] = search_field
        if search_value:
            req_body["search_value"] = search_value

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrder/pageList",
            req_body=req_body
        )

    async def get_vc_order_detail_po(
        self,
        access_token: str,
        local_po_number: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC订单详情【PO类型】

        API: POST /basicOpen/platformOrder/vcOrderPo/detail

        Args:
            access_token: 访问令牌
            local_po_number: 本地PO号，查询VC订单列表接口字段【local_po_number】
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含订单详情

        返回字段说明:
            - vc_store_id: 店铺ID
            - seller_name: 店铺名称
            - purchase_order_number: 订单编号
            - local_po_number: 本地订单编号
            - purchase_order_date: 下单时间
            - purchase_order_state: 订单状态 (Acknowledged确认, Closed关闭)
            - purchase_order_process_state: 订单流转状态 (0待处理, 1确认中, 2确认成功, 3确认失败)
            - payment_method: 支付类型
            - purchase_order_type: 订单类型 (0=DF, 1=PO)
            - related_warehouse_id: 仓库ID
            - related_warehouse_name: 仓库名称
            - ship_to_party_id: 收件人
            - total_price: 订单总金额
            - currency_code: 币种
            - item_amount: 货物数量
            - ship_window_start: 发货窗口开始时间
            - ship_window_end: 发货窗口结束时间
            - items: 商品数据列表

        Example:
            >>> result = await vc.get_vc_order_detail_po(
            ...     access_token="xxx",
            ...     local_po_number="402242689523401371"
            ... )
        """
        logger.debug("Fetching VC PO order detail: local_po_number=%s", local_po_number)

        req_body = {
            "local_po_number": local_po_number,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrderPo/detail",
            req_body=req_body
        )

    async def get_vc_order_detail_df(
        self,
        access_token: str,
        vc_store_id: str,
        purchase_order_number: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC订单详情【DF类型】

        API: POST /basicOpen/platformOrder/vcOrderDf/detail

        Args:
            access_token: 访问令牌
            vc_store_id: VC店铺ID，查询VC店铺列表接口对应字段【vc_store_id】
            purchase_order_number: 订单编号
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含订单详情

        返回字段说明:
            - vc_store_id: VC店铺ID
            - seller_name: 店铺名称
            - local_po_number: 本地PO号
            - purchase_order_number: 订单编号
            - purchase_order_date: 下单时间
            - purchase_order_state: 订单状态 (New新的订单, SHIPPED已发货, ACCEPTED已确定, CANCELED已取消)
            - purchase_order_type: 订单类型 (0=DF, 1=PO)
            - bill_to_party_id: 结算方式
            - ship_from_party_id: 供货编码
            - related_warehouse_id: 仓库ID
            - related_warehouse_name: 仓库名称
            - ship_method: 运输方式
            - ship_window_time: 要求发货时间
            - promised_delivery_date: 承诺送达时间
            - ship_to_party_address: 收货方地址
            - total_price: 订单总金额
            - currency_code: 币种
            - item_amount: 货物数量
            - items: 商品列表
            - tracking_number_list: 箱号/跟踪号列表

        Example:
            >>> result = await vc.get_vc_order_detail_df(
            ...     access_token="xxx",
            ...     vc_store_id="134225003201380864",
            ...     purchase_order_number="XB95bX69r"
            ... )
        """
        logger.debug(
            "Fetching VC DF order detail: vc_store_id=%s, "
            "purchase_order_number=%s",
            vc_store_id, purchase_order_number,
        )

        req_body = {
            "vc_store_id": vc_store_id,
            "purchase_order_number": purchase_order_number,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrderDf/detail",
            req_body=req_body
        )

    # ==================== 发货单管理 ====================

    async def get_vc_invoices(
        self,
        access_token: str,
        shipment_type: str,
        sids: list[str] | None = None,
        wid: list[int] | None = None,
        status: int = 0,
        create_time_start: str | None = None,
        create_time_end: str | None = None,
        shipment_time_start: str | None = None,
        shipment_time_end: str | None = None,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC发货单列表

        API: POST /basicOpen/openapi/getInvoice/page/list

        Args:
            access_token: 访问令牌
            shipment_type: 出库类型 (1=DF, 2=PO, 3=DI)
            sids: 店铺ID列表，如 ["1", "2"]
            wid: 国家ID列表，如 [1, 2]
            status: 订单状态
                - 0: 全部（默认）
                - 5: 待配货
                - 10: 待出库
                - 15: 已完成
                - 100: 已作废
            create_time_start: 创建日期-开始，格式 YYYY-MM-DD
            create_time_end: 创建日期-结束，格式 YYYY-MM-DD
            shipment_time_start: 出库日期-开始，格式 YYYY-MM-DD
            shipment_time_end: 出库日期-结束，格式 YYYY-MM-DD
            offset: 偏移量，默认0
            length: 每页条数，默认20
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含发货单列表和总数
                - data: {"count": 总数, "list": [发货单列表]}

        返回字段说明:
            - id: 主键ID
            - orderNo: 发货单号
            - purchaseOrderNumber: 订单号/货件号
            - remark: 备注
            - shippingWid: 发货仓库ID
            - shippingWarehouseName: 发货仓库名称
            - shipmentTime: 发货时间
            - shipmentUser: 发货人
            - status: 发货状态
            - createUser: 创建人名称
            - createTime: 创建时间
            - shipmentType: 发货类型
            - statusName: 状态名称
            - totalNum: 总发货量
            - estimatedPickupTime: 预计到货时间
            - shipmentTypeName: 出库类型名称
            - sourceType: 来源类型 (0订单生成, 1货件生成)
            - invoiceModel: 下单模式 (0手工下单, 1系统下单)
            - outboundDate: 出库日期
            - items: 发货单明细列表

        Example:
            >>> result = await vc.get_vc_invoices(
            ...     access_token="xxx",
            ...     shipment_type="2",  # PO类型
            ...     status=5  # 待配货
            ... )
        """
        logger.debug(
            "Fetching VC invoices: shipment_type=%s, status=%s, "
            "offset=%s, length=%s",
            shipment_type, status, offset, length,
        )

        req_body = {
            "shipmentType": shipment_type,
            "status": status,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if wid:
            req_body["wid"] = wid
        if create_time_start:
            req_body["createTimeStartTime"] = create_time_start
        if create_time_end:
            req_body["createTimeEndTime"] = create_time_end
        if shipment_time_start:
            req_body["shipmentTimeStartTime"] = shipment_time_start
        if shipment_time_end:
            req_body["shipmentTimeEndTime"] = shipment_time_end

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/getInvoice/page/list",
            req_body=req_body
        )

    async def get_vc_invoice_detail(
        self,
        access_token: str,
        order_no: str,
        **kwargs
    ) -> ResponseResult:
        """
        查询VC发货单详情

        API: POST /basicOpen/openapi/getInvoice/detail

        Args:
            access_token: 访问令牌
            order_no: 订单号
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含发货单详情

        返回字段说明:
            - invoice: 发货单信息
                - orderNo: 发货单号
                - purchaseOrderNumber: 订单号/货件号
                - remark: 备注
                - shippingWid: 发货仓库ID
                - shippingWarehouseName: 发货仓库名称
                - shipmentTime: 发货时间
                - shipmentUser: 发货人
                - status: 发货状态
                - createUser: 创建人名称
                - createTime: 创建时间
                - shipmentType: 发货类型
                - statusName: 状态名称
                - totalNum: 总发货量
                - items: 发货单明细列表
                - invoiceTrackingList: 物流信息

        Example:
            >>> result = await vc.get_vc_invoice_detail(
            ...     access_token="xxx",
            ...     order_no="RO250101001"
            ... )
        """
        logger.debug("Fetching VC invoice detail: order_no=%s", order_no)

        req_body = {
            "orderNo": order_no,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/getInvoice/detail",
            req_body=req_body
        )

    async def confirm_vc_invoice_shipment(
        self,
        access_token: str,
        order_no_list: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        VC发货单确认发货

        API: POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods

        Args:
            access_token: 访问令牌
            order_no_list: 发货单号列表，如 ["RO260205007"]
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含操作结果
                - data: {"errorMsg": [...], "failedCount": 失败数, "successCount": 成功数}

        Example:
            >>> result = await vc.confirm_vc_invoice_shipment(
            ...     access_token="xxx",
            ...     order_no_list=["RO260205007"]
            ... )
        """
        logger.debug("Confirming VC invoice shipment: order_no_list=%s", order_no_list)

        req_body = {
            "orderNoList": order_no_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/openapi/getInvoice/invoice/batchSendGoods",
            req_body=req_body
        )

    # ==================== DF订单操作 ====================

    async def submit_shipping_label_df(
        self,
        access_token: str,
        ids: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        VC订单请求标签【DF类型】

        API: POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel

        Args:
            access_token: 访问令牌
            ids: 订单ID列表，查询VC订单列表接口对应字段【id】
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await vc.submit_shipping_label_df(
            ...     access_token="xxx",
            ...     ids=["107"]
            ... )
        """
        logger.debug("Submitting shipping label for DF orders: ids=%s", ids)

        req_body = {
            "ids": ids,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrderDf/submitShippingLabel",
            req_body=req_body
        )

    async def get_shipping_label_df(
        self,
        access_token: str,
        ids: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        VC订单打印标签【DF类型】

        API: POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel

        Args:
            access_token: 访问令牌
            ids: 订单ID列表，查询VC订单列表接口对应字段【id】
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含标签下载链接

        返回字段说明:
            - label_list: 标签数据列表
                - id: 订单ID
                - purchase_order_number: 订单编号
                - label_count: 标签数量
                - error_msg: 错误信息
            - pdf_url: PDF下载链接
            - download_url: 压缩包下载链接

        Example:
            >>> result = await vc.get_shipping_label_df(
            ...     access_token="xxx",
            ...     ids=["107"]
            ... )
            >>> data = result.data  # {"label_list": [...], "pdf_url": "xxx", "download_url": "xxx"}
        """
        logger.debug("Getting shipping label for DF orders: ids=%s", ids)

        req_body = {
            "ids": ids,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrderDf/getShippingLabel",
            req_body=req_body
        )

    async def confirm_shipment_df(
        self,
        access_token: str,
        ids: list[str],
        **kwargs
    ) -> ResponseResult:
        """
        VC订单确认发货【DF类型】

        API: POST /basicOpen/platformOrder/vcOrderDf/confirmShipment

        Args:
            access_token: 访问令牌
            ids: 订单ID列表，查询VC订单列表接口对应字段【id】
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await vc.confirm_shipment_df(
            ...     access_token="xxx",
            ...     ids=["107"]
            ... )
        """
        logger.debug("Confirming shipment for DF orders: ids=%s", ids)

        req_body = {
            "ids": ids,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/platformOrder/vcOrderDf/confirmShipment",
            req_body=req_body
        )

    # ==================== 产品配对 ====================

    async def batch_link_product(
        self,
        access_token: str,
        sid_asins: list[dict[str, str]],
        product_id: int,
        is_sync_pic: int = 0,
        **kwargs
    ) -> ResponseResult:
        """
        批量配对产品

        API: POST /basicOpen/vcservice/productRelation/batchLink

        Args:
            access_token: 访问令牌
            sid_asins: 配对的sid和asin对象数组
                [{"sid": "134228919447351298", "asin": "B09N15BYDM"}, ...]
            product_id: 本地商品表主键ID
            is_sync_pic: 是否同步图片到本地商品 (0=否, 1=是)
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 操作结果，data为true表示成功

        Example:
            >>> result = await vc.batch_link_product(
            ...     access_token="xxx",
            ...     sid_asins=[{"sid": "134228919447351298", "asin": "B09N15BYDM"}],
            ...     product_id=5913,
            ...     is_sync_pic=0
            ... )
        """
        logger.debug(
            "Batch linking product: product_id=%s, "
            "sid_asins count=%s, is_sync_pic=%s",
            product_id, len(sid_asins), is_sync_pic,
        )

        req_body = {
            "sidAsins": sid_asins,
            "productId": product_id,
            "isSyncPic": is_sync_pic,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/basicOpen/vcservice/productRelation/batchLink",
            req_body=req_body
        )


__all__ = [
    'VCEndpoints',
]

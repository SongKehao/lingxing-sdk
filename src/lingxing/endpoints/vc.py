"""VC卖家 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class VCEndpoints(BaseEndpoint):
    """领星VC卖家 API (10个接口)."""

    async def listing_manage_vc_listing_page_list(self, **kwargs) -> list | dict:
        """查询Listing列表.

POST /basicOpen/listingManage/vcListing/pageList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    vc_store_ids: vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】, array."""
        resp = await self._post("/basicOpen/listingManage/vcListing/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def platform_auth_vc_seller_page_list(self, **kwargs) -> list | dict:
        """查询VC店铺列表.

POST /basicOpen/platformAuth/vcSeller/pageList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/platformAuth/vcSeller/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_deliver_detail(self, **kwargs) -> list | dict:
        """查询VC发货单详情.

POST /basicOpen/openapi/getInvoice/detail

Args:
    orderNo: 订单号 (required), string."""
        resp = await self._post("/basicOpen/openapi/getInvoice/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_deliver_page_list(self, **kwargs) -> list | dict:
        """查询VC发货单列表.

POST /basicOpen/openapi/getInvoice/page/list

Args:
    offset: 偏移量(默认0), number.
    length: 每页条数(默认20）, number.
    sids: 店铺id, array.
    wid: 国家id, array.
    shipmentType: 出库类型 1:DF 2:PO 3:DI (required), string.
    status: 订单状态 0: 全部 5:待配货 10:待出库 15:已完成 100:已作废 (默认0）, number.
    createTimeStartTime: 创建日期-开始, string.
    createTimeEndTime: 创建日期-结束, string.
    shipmentTimeStartTime: 出库日期-开始, string.
    shipmentTimeEndTime: 出库日期-结束, string."""
        resp = await self._post("/basicOpen/openapi/getInvoice/page/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_confirm_shipment(self, **kwargs) -> dict:
        """VC订单-确认发货【DF】.

POST /basicOpen/platformOrder/vcOrderDf/confirmShipment

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/confirmShipment", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_order_df_detail(self, **kwargs) -> list | dict:
        """查询VC订单详情【DF】.

POST /basicOpen/platformOrder/vcOrderDf/detail

Args:
    vc_store_id: vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】 (required), string.
    purchase_order_number: 订单编号 (required), string."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_get_shipping_label(self, **kwargs) -> list | dict:
        """VC订单-打印标签【DF】.

POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/getShippingLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_df_submit_shipping_label(self, **kwargs) -> dict:
        """VC订单-请求标签【DF】.

POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/submitShippingLabel", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_order_page_list(self, **kwargs) -> list | dict:
        """查询VC订单列表.

POST /basicOpen/platformOrder/vcOrder/pageList

Args:
    purchase_order_type: 订单类型： 0  DF 1  PO  2  DI (required), array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    vc_store_ids: vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】, array.
    search_field_time: 查询时间类型： 1  订购时间 2  要求发货时间 3  订单更新时间, string.
    start_date: 开始时间，开区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_date: 结束时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    search_field: 搜索类型： purchase_order_number 订单号 asin ASIN local_name 品名  customer_order_number 客户订单号【DF类型订单】 vendor_product_id 商品编码, string.
    search_value: 搜索值, array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrder/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def vc_order_po_detail(self, **kwargs) -> list | dict:
        """查询VC订单详情【PO】.

POST /basicOpen/platformOrder/vcOrderPo/detail

Args:
    local_po_number: 本地po号，查询VC订单列表 接口字段【local_po_number】 (required), string."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderPo/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

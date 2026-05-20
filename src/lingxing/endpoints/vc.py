"""VC卖家 API endpoints."""
from __future__ import annotations

from ..models.responses.vc import (
    GetinvoicePageListResponse,
    ListingmanageVclistingPagelistResponse,
    OpenapiGetinvoiceDetailResponse,
    PlatformauthVcsellerPagelistResponse,
    PlatformorderVcorderdfConfirmshipmentResponse,
    PlatformorderVcorderdfSubmitsshippinglabelResponse,
    PlatformorderVcorderPagelistResponse,
    PlatformorderVcorderdfDetailResponse,
    PlatformorderVcorderdfGetshippinglabelResponse,
    PlatformorderVcorderpoDetailResponse,
)

from typing import Any

from ._base import BaseEndpoint


class VCEndpoints(BaseEndpoint):
    """领星VC卖家 API (10个接口)."""

    async def listing_manage_vc_listing_page_list(self, offset: int = None, length: int = None, vc_store_ids: list = None) -> list[ListingmanageVclistingPagelistResponse]:
        """查询Listing列表.

POST /basicOpen/listingManage/vcListing/pageList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    vc_store_ids: vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】, array."""
        resp = await self._post("/basicOpen/listingManage/vcListing/pageList", {k: v for k, v in {"offset": offset, "length": length, "vc_store_ids": vc_store_ids}.items() if v is not None})
        return self._parse_list(resp.data, ListingmanageVclistingPagelistResponse)
    async def platform_auth_vc_seller_page_list(self, offset: int = None, length: int = None) -> list[PlatformauthVcsellerPagelistResponse]:
        """查询VC店铺列表.

POST /basicOpen/platformAuth/vcSeller/pageList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/platformAuth/vcSeller/pageList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, PlatformauthVcsellerPagelistResponse)
    async def vc_deliver_detail(self, orderNo: str = None) -> list[OpenapiGetinvoiceDetailResponse]:
        """查询VC发货单详情.

POST /basicOpen/openapi/getInvoice/detail

Args:
    orderNo: 订单号 (required), string."""
        resp = await self._post("/basicOpen/openapi/getInvoice/detail", {k: v for k, v in {"orderNo": orderNo}.items() if v is not None})
        return self._parse_list(resp.data, OpenapiGetinvoiceDetailResponse)
    async def vc_deliver_page_list(self, offset: float = None, length: float = None, sids: list = None, wid: list = None, shipmentType: str = None, status: float = None, createTimeStartTime: str = None, createTimeEndTime: str = None, shipmentTimeStartTime: str = None, shipmentTimeEndTime: str = None) -> list[GetinvoicePageListResponse]:
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
        resp = await self._post("/basicOpen/openapi/getInvoice/page/list", {k: v for k, v in {"offset": offset, "length": length, "sids": sids, "wid": wid, "shipmentType": shipmentType, "status": status, "createTimeStartTime": createTimeStartTime, "createTimeEndTime": createTimeEndTime, "shipmentTimeStartTime": shipmentTimeStartTime, "shipmentTimeEndTime": shipmentTimeEndTime}.items() if v is not None})
        return self._parse_list(resp.data, GetinvoicePageListResponse)
    async def vc_order_df_confirm_shipment(self, ids: Any = None) -> PlatformorderVcorderdfConfirmshipmentResponse | None:
        """VC订单-确认发货【DF】.

POST /basicOpen/platformOrder/vcOrderDf/confirmShipment

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/confirmShipment", {k: v for k, v in {"ids": ids}.items() if v is not None})
        return self._parse_one(resp.data, PlatformorderVcorderdfConfirmshipmentResponse)
    async def vc_order_df_detail(self, vc_store_id: str = None, purchase_order_number: str = None) -> list[PlatformorderVcorderdfDetailResponse]:
        """查询VC订单详情【DF】.

POST /basicOpen/platformOrder/vcOrderDf/detail

Args:
    vc_store_id: vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】 (required), string.
    purchase_order_number: 订单编号 (required), string."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/detail", {k: v for k, v in {"vc_store_id": vc_store_id, "purchase_order_number": purchase_order_number}.items() if v is not None})
        return self._parse_list(resp.data, PlatformorderVcorderdfDetailResponse)
    async def vc_order_df_get_shipping_label(self, ids: Any = None) -> list[PlatformorderVcorderdfGetshippinglabelResponse]:
        """VC订单-打印标签【DF】.

POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/getShippingLabel", {k: v for k, v in {"ids": ids}.items() if v is not None})
        return self._parse_list(resp.data, PlatformorderVcorderdfGetshippinglabelResponse)
    async def vc_order_df_submit_shipping_label(self, ids: Any = None) -> PlatformorderVcorderdfSubmitsshippinglabelResponse | None:
        """VC订单-请求标签【DF】.

POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel

Args:
    ids: 订单ID，查询VC订单列表接口对应字段【id】 (required), array."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderDf/submitShippingLabel", {k: v for k, v in {"ids": ids}.items() if v is not None})
        return self._parse_one(resp.data, PlatformorderVcorderdfSubmitsshippinglabelResponse)
    async def vc_order_page_list(self, purchase_order_type: Any = None, offset: int = None, length: int = None, vc_store_ids: list = None, search_field_time: str = None, start_date: str = None, end_date: str = None, search_field: str = None, search_value: list = None) -> list[PlatformorderVcorderPagelistResponse]:
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
        resp = await self._post("/basicOpen/platformOrder/vcOrder/pageList", {k: v for k, v in {"purchase_order_type": purchase_order_type, "offset": offset, "length": length, "vc_store_ids": vc_store_ids, "search_field_time": search_field_time, "start_date": start_date, "end_date": end_date, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        return self._parse_list(resp.data, PlatformorderVcorderPagelistResponse)
    async def vc_order_po_detail(self, local_po_number: str = None) -> list[PlatformorderVcorderpoDetailResponse]:
        """查询VC订单详情【PO】.

POST /basicOpen/platformOrder/vcOrderPo/detail

Args:
    local_po_number: 本地po号，查询VC订单列表 接口字段【local_po_number】 (required), string."""
        resp = await self._post("/basicOpen/platformOrder/vcOrderPo/detail", {k: v for k, v in {"local_po_number": local_po_number}.items() if v is not None})
        return self._parse_list(resp.data, PlatformorderVcorderpoDetailResponse)

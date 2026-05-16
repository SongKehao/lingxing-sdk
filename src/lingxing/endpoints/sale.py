"""销售/订单/Listing API endpoints."""
from __future__ import annotations

from typing import Any

from ._base import BaseEndpoint


class SaleEndpoints(BaseEndpoint):
    """领星销售/订单/Listing API (44个接口)."""

    async def add_goods_tag(self, tagIds: Any = None, bindDetail: list = None) -> dict:
        """Listing新增商品标签.

POST /basicOpen/listingManage/bindListingAndTag

Args:
    bindDetail: 配对信息 (required), array.
    tagIds: 标签id数组 (required), array."""
        resp = await self._post("/basicOpen/listingManage/bindListingAndTag", {k: v for k, v in {"tagIds": tagIds, "bindDetail": bindDetail}.items() if v is not None})
        return resp.data or {}
    async def delete_goods_tag(self, globalTagIds: Any = None, bindDetail: list = None) -> dict:
        """Listing删除商品标签.

POST /basicOpen/listingManage/removeListingAndTag

Args:
    bindDetail: 配对信息 (required), array.
    globalTagIds: 标签id数组 (required), array."""
        resp = await self._post("/basicOpen/listingManage/removeListingAndTag", {k: v for k, v in {"globalTagIds": globalTagIds, "bindDetail": bindDetail}.items() if v is not None})
        return resp.data or {}
    async def fbm_order_detail(self, order_number: str = None) -> list | dict:
        """查询亚马逊自发货订单详情.

POST /erp/sc/routing/order/Order/getOrderDetail

Args:
    order_number: 系统单号 (required), string."""
        resp = await self._post("/erp/sc/routing/order/Order/getOrderDetail", {k: v for k, v in {"order_number": order_number}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbm_order_list(self, sid: str = None, order_status: str = None, page: int = None, length: int = None, start_time: str = None, end_time: str = None) -> list | dict:
        """查询亚马逊自发货订单列表.

POST /erp/sc/routing/order/Order/getOrderList

Args:
    sid: 店铺sid，用英文逗号分隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    order_status: 订单状态，多个用英文逗号分隔： 2 已发货 3 未付款 4 待审核 5 待发货 6 已取消, string.
    page: 页码数，默认1, int.
    length: 分页长度，默认100, int.
    start_time: 订购时间开始, string.
    end_time: 订购时间结束, string."""
        resp = await self._post("/erp/sc/routing/order/Order/getOrderList", {k: v for k, v in {"sid": sid, "order_status": order_status, "page": page, "length": length, "start_time": start_time, "end_time": end_time}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_merchant_shipping_group(self, sellerId: str = None, marketplaceId: str = None, productType: str = None, flag: float = None) -> list | dict:
        """刊登管理-获取运费模板.

POST /basicOpen/openapi/publish/manage/getMerchantShippingGroup

Args:
    sellerId: 店铺id (required), string.
    marketplaceId: 市场id (required), string.
    productType: 商品原始类目 (required), string.
    flag: 默认传0，返回为空则传1，实时请求亚马逊获取后台最新数据, number."""
        resp = await self._post("/basicOpen/openapi/publish/manage/getMerchantShippingGroup", {k: v for k, v in {"sellerId": sellerId, "marketplaceId": marketplaceId, "productType": productType, "flag": flag}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_prices(self, data: list = None) -> list | dict:
        """批量获取Listing费用.

POST /listing/listing/open/api/listing/getPrices

Args:
    data: 请求数据，上限500 (required), array."""
        resp = await self._post("/listing/listing/open/api/listing/getPrices", {k: v for k, v in {"data": data}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def listing(self, sid: str = None, is_pair: int = None, is_delete: int = None, pair_update_start_time: str = None, pair_update_end_time: str = None, listing_update_start_time: str = None, listing_update_end_time: str = None, search_field: str = None, search_value: list = None, exact_search: int = None, store_type: int = None, offset: int = None, length: int = None) -> list | dict:
        """查询亚马逊Listing.

POST /erp/sc/data/mws/listing

Args:
    sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    is_pair: 是否配对：1 已配对，2 未配对, int.
    is_delete: 是否删除：0 未删除，1 已删除, int.
    pair_update_start_time: 【配对更新时间】的开始时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1, string.
    pair_update_end_time: 【配对更新时间】的结束时间（此为北京时间，格式：Y-m-d H:i:s），用此时间查询要求 is_pair=1, string.
    listing_update_start_time: 【All Listing报表更新时间】的开始时间（此为零时区时间，格式Y-m-d H:i:s）, string.
    listing_update_end_time: 【All Listing报表更新时间】的结束时间（此为零时区时间，格式Y-m-d H:i:s）, string.
    search_field: 搜索支持字段：seller_sku、asin、sku, string.
    search_value: 搜索值，上限10个, array.
    exact_search: 搜索模式：0 模糊搜索，1 精确搜索【默认值】, int.
    store_type: 商品类型，1-非低价商店 ，2-低价商店商品, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int."""
        resp = await self._post("/erp/sc/data/mws/listing", {k: v for k, v in {"sid": sid, "is_pair": is_pair, "is_delete": is_delete, "pair_update_start_time": pair_update_start_time, "pair_update_end_time": pair_update_end_time, "listing_update_start_time": listing_update_start_time, "listing_update_end_time": listing_update_end_time, "search_field": search_field, "search_value": search_value, "exact_search": exact_search, "store_type": store_type, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_detail(self, order_id: str = None) -> list | dict:
        """查询亚马逊订单详情.

POST /erp/sc/data/mws/orderDetail

Args:
    order_id: 亚马逊订单号，多个使用英文逗号分隔，上限200 (required), string."""
        resp = await self._post("/erp/sc/data/mws/orderDetail", {k: v for k, v in {"order_id": order_id}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def orderlists(self, sid: int = None, sid_list: list = None, start_date: str = None, end_date: str = None, date_type: int = None, order_status: list = None, sort_desc_by_date_type: int = None, fulfillment_channel: int = None, offset: int = None, length: int = None) -> list | dict:
        """查询亚马逊订单列表.

POST /erp/sc/data/mws/orders

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, int.
    sid_list: 店铺id列表，最大长度20, array.
    start_date: 查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s 当date_type=3时，需要传入时间格式为：Y-m-d H:i:s (required), string.
    end_date: 查询时间，左闭右开，格式：Y-m-d 或 Y-m-d H:i:s 当date_type=3时，需要传入时间格式为：Y-m-d H:i:s (required), string.
    date_type: 查询日期类型：【默认1】 1 订购时间【站点时间】 2 订单修改时间【北京时间】 3 平台更新时间【UTC时间】 10 发货时间【站点时间】 查询时间范围不超过一年, int.
    order_status: Pending 待处理 Unshipped 未发货 PartiallyShipped 部分发货 Shipped 已发货 Canceled 取消, array.
    sort_desc_by_date_type: 是否按查询日期类型排序：0 否，1 降序，2 升序【默认0】, int.
    fulfillment_channel: 配送方式：1 亚马逊订单-AFN，2 自发货-MFN, int.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限5000, int."""
        resp = await self._post("/erp/sc/data/mws/orders", {k: v for k, v in {"sid": sid, "sid_list": sid_list, "start_date": start_date, "end_date": end_date, "date_type": date_type, "order_status": order_status, "sort_desc_by_date_type": sort_desc_by_date_type, "fulfillment_channel": fulfillment_channel, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_list(self, record_unique_id: int = None, sku: str = None, store_id: int = None, operate_time: dict = None, operate_time_: Any = None) -> list | dict:
        """刊登管理-查询刊登结果.

POST /listing/publish/openapi/amazon/product/list

Args:
    record_unique_id: 批次唯一ID, int.
    sku: sku, string.
    store_id: store_id, int.
    operate_time: 操作时间, object."""
        resp = await self._post("/listing/publish/openapi/amazon/product/list", {k: v for k, v in {"record_unique_id": record_unique_id, "sku": sku, "store_id": store_id, "operate_time": operate_time, "operate_time_": operate_time_}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_publish(self, store_id: float = None, data: Any = None) -> list | dict:
        """刊登管理-提交商品资料.

POST /listing/publish/openapi/amazon/product/publish

Args:
    store_id: store_id (required), number."""
        resp = await self._post("/listing/publish/openapi/amazon/product/publish", {k: v for k, v in {"store_id": store_id, "data": data}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def productlink(self, data: Any = None) -> list | dict:
        """批量添加/编辑Listing配对.

POST /erp/sc/storage/product/link"""
        resp = await self._post("/erp/sc/storage/product/link", {k: v for k, v in {"data": data}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_helper_v2(self, storeId: float = None) -> list | dict:
        """刊登管理-查询 Amazon 根分类.

POST /basicOpen/openapi/publish/manage/categoryRoot

Args:
    storeId: 店铺id (required), number."""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryRoot", {k: v for k, v in {"storeId": storeId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_category_children(self, storeId: float = None, categoryUniqueId: float = None) -> list | dict:
        """刊登管理-查询 Amazon 子分类.

POST /basicOpen/openapi/publish/manage/categoryChildren

Args:
    storeId: 店铺id (required), number.
    categoryUniqueId: 类目唯一ID (required), number."""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryChildren", {k: v for k, v in {"storeId": storeId, "categoryUniqueId": categoryUniqueId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_category_root(self, storeId: float = None) -> list | dict:
        """刊登管理-查询 Amazon 根分类.

POST /basicOpen/openapi/publish/manage/categoryRoot

Args:
    storeId: 店铺id (required), number."""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryRoot", {k: v for k, v in {"storeId": storeId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_get_product_type(self, marketplaceId: str = None, productTypeOrigin: str = None) -> list | dict:
        """刊登管理-获取指定 productType 的 JSON Schema.

POST /basicOpen/openapi/publish/manage/getProductType

Args:
    marketplaceId: 市场ID (required), string.
    productTypeOrigin: 商品原始类型 (required), string."""
        resp = await self._post("/basicOpen/openapi/publish/manage/getProductType", {k: v for k, v in {"marketplaceId": marketplaceId, "productTypeOrigin": productTypeOrigin}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_product_list(self, store_id: int = None, skus: Any = None) -> list | dict:
        """查询已有商品信息.

POST /listing/publish/openapi/amazon/product/search

Args:
    store_id: store_id (required), int.
    skus: sku列表，最多20个 (required), array."""
        resp = await self._post("/listing/publish/openapi/amazon/product/search", {k: v for k, v in {"store_id": store_id, "skus": skus}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def refund_order(self, sid: float = None, amazonOrderId: str = None, purchaseDateLocal: str = None, data: Any = None) -> list | dict:
        """订单退款.

POST /basicOpen/openapi/salesOrder/refundOrder

Args:
    sid: 店铺id (required), number.
    amazonOrderId: 亚马逊订单ID (required), string.
    purchaseDateLocal: 订购时间 (required), string."""
        resp = await self._post("/basicOpen/openapi/salesOrder/refundOrder", {k: v for k, v in {"sid": sid, "amazonOrderId": amazonOrderId, "purchaseDateLocal": purchaseDateLocal, "data": data}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def sc_order_set_remark(self, sid: int = None, amazonOrderId: str = None, remark: str = None) -> list | dict:
        """SC订单-设置订单备注.

POST /basicOpen/platformOrder/scOrder/setRemark

Args:
    sid: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    amazonOrderId: 订单id (required), string.
    remark: 备注 (required), string."""
        resp = await self._post("/basicOpen/platformOrder/scOrder/setRemark", {k: v for k, v in {"sid": sid, "amazonOrderId": amazonOrderId, "remark": remark}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def unlink_listing(self, list_field: list = None) -> list | dict:
        """解除Listing配对.

POST /basicOpen/listingManage/unLinkListingPairs

Args:
    list: 解除配对列表 (required), array."""
        resp = await self._post("/basicOpen/listingManage/unLinkListingPairs", {k: v for k, v in {"list_field": list_field}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_fbm_inventory(self, fbmInventoryList: list = None) -> dict:
        """修改 FBM库存&处理时间.

POST /basicOpen/FbmManagement/modifyFbmInventory

Args:
    fbmInventoryList: 修改库存列表（支持批量修改，单次最多传200个元素） (required), array."""
        resp = await self._post("/basicOpen/FbmManagement/modifyFbmInventory", {k: v for k, v in {"fbmInventoryList": fbmInventoryList}.items() if v is not None})
        return resp.data or {}
    async def update_principal(self, sid_asin_list: list = None) -> dict:
        """批量分配Listing负责人.

POST /listing/listing/open/api/asin/updatePrincipal

Args:
    sid_asin_list: asin负责人分配信息，最多支持200个 (required), array."""
        resp = await self._post("/listing/listing/open/api/asin/updatePrincipal", {k: v for k, v in {"sid_asin_list": sid_asin_list}.items() if v is not None})
        return resp.data or {}
    async def upload_tracking(self, fileName: str = None, base64File: str = None, trackingNo: str = None, waybillNo: str = None, woId: int = None) -> list | dict:
        """导入面单.

POST /basicOpen/selfShipmentOrder/importLabel

Args:
    fileName: 面单文件名 (required), string.
    base64File: PDF/PNG/JPG/JPEG格式文件 Base64编码 (required), string.
    trackingNo: 运单号 (required), string.
    waybillNo: 跟踪号 (required), string.
    woId: 出库单id，对应查询销售出库单列表 (required), int."""
        resp = await self._post("/basicOpen/selfShipmentOrder/importLabel", {k: v for k, v in {"fileName": fileName, "base64File": base64File, "trackingNo": trackingNo, "waybillNo": waybillNo, "woId": woId}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def adjust_price_adjust_price_manual(self, offset: float = None, length: float = None, sid: list = None, processing_status: list = None, time_type: float = None, start_time: str = None, end_time: str = None, search_field: str = None, search_value: list = None, tab_status: float = None) -> list | dict:
        """查询调价队列.

POST /basicOpen/module/adjustPrice/AdjustPriceManual

Args:
    offset: 偏移量 (required), number.
    length: 页长度，上限500 (required), number.
    sid: 搜索店铺id, array.
    processing_status: 调价状态，支持多选，数组 1待调价 2调价中 3调价成功 4调价失败 5审批中 6已驳回 7已作废, array.
    time_type: 搜索时间类型：1创建时间 2完成时间, number.
    start_time: 开始时间, string.
    end_time: 结束时间, string.
    search_field: 搜索字段：msku，asin, string.
    search_value: 搜索值，msku和asin支持多个搜索，数组, array.
    tab_status: tab状态栏  0全部 1待审批 2调价中 3成功 4失败 5已作废 默认0, number."""
        resp = await self._post("/basicOpen/module/adjustPrice/AdjustPriceManual", {k: v for k, v in {"offset": offset, "length": length, "sid": sid, "processing_status": processing_status, "time_type": time_type, "start_time": start_time, "end_time": end_time, "search_field": search_field, "search_value": search_value, "tab_status": tab_status}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def after_sale_list(self, **kwargs) -> list | dict:
        """afterSaleList. POST /erp/sc/routing/amzod/order/afterSaleList"""
        resp = await self._post("/erp/sc/routing/amzod/order/afterSaleList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def b2b_price_modify_price(self, content: list = None) -> list | dict:
        """修改B2B价格.

POST /basicOpen/b2bPrice/modifyPrice

Args:
    content: B2B售价 (required), array."""
        resp = await self._post("/basicOpen/b2bPrice/modifyPrice", {k: v for k, v in {"content": content}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_fee_difference_list(self, offset: int = None, length: int = None, start_date: str = None, end_date: str = None, sids: list = None, search_field: str = None, search_value: str = None) -> list | dict:
        """FBA费差异-异常订单-订单.

POST /basicOpen/openapi/sale/fbaFeeDifference/order/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    start_date: 开始时间【结算时间】，闭区间，格式：Y-m-d, string.
    end_date: 结束时间【结算时间】，闭区间，格式：Y-m-d, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 搜索字段：order_id 订单号，msku MSKU, string.
    search_value: 搜索值：多个使用英文逗号分隔，上限200, string."""
        resp = await self._post("/basicOpen/openapi/sale/fbaFeeDifference/order/list", {k: v for k, v in {"offset": offset, "length": length, "start_date": start_date, "end_date": end_date, "sids": sids, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_fee_difference_msku_list(self, offset: int = None, length: int = None, start_date: str = None, end_date: str = None, sids: list = None, search_field: str = None, search_value: str = None) -> list | dict:
        """FBA费差异-异常订单-MSKU.

POST /basicOpen/openapi/sale/fbaFeeDifference/msku/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    start_date: 开始时间【结算时间】，闭区间，格式：Y-m-d, string.
    end_date: 结束时间【结算时间】，闭区间，格式：Y-m-d, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 搜索字段：msku MSKU, string.
    search_value: 搜索值：多个使用英文逗号分隔，上限200, string."""
        resp = await self._post("/basicOpen/openapi/sale/fbaFeeDifference/msku/list", {k: v for k, v in {"offset": offset, "length": length, "start_date": start_date, "end_date": end_date, "sids": sids, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def global_tag_add_tag(self, tag_name: str = None) -> dict:
        """添加Listing标签.

POST /basicOpen/globalTag/listing/addTag

Args:
    tag_name: 标签名称 (required), string."""
        resp = await self._post("/basicOpen/globalTag/listing/addTag", {k: v for k, v in {"tag_name": tag_name}.items() if v is not None})
        return resp.data or {}
    async def global_tag_page_list(self, offset: int = None, length: int = None, search_field: str = None, search_value: str = None) -> list | dict:
        """查询Listing标签列表.

POST /basicOpen/globalTag/listing/page/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    search_field: 搜索类型：tag_name 标签名称, string.
    search_value: 搜索值, string."""
        resp = await self._post("/basicOpen/globalTag/listing/page/list", {k: v for k, v in {"offset": offset, "length": length, "search_field": search_field, "search_value": search_value}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def global_tag_remove_tag(self, tag_ids: Any = None) -> dict:
        """删除Listing标签.

POST /basicOpen/globalTag/listing/removeTag

Args:
    tag_ids: 标签id，上限200 (required), array."""
        resp = await self._post("/basicOpen/globalTag/listing/removeTag", {k: v for k, v in {"tag_ids": tag_ids}.items() if v is not None})
        return resp.data or {}
    async def listing_operate_log_page_list(self, sid: str = None, msku: str = None, offset: int = None, length: int = None, operate_uid: list = None, operate_type: list = None, operate_time_start: str = None, operate_time_end: str = None) -> list | dict:
        """查询Listing操作日志列表.

POST /basicOpen/listingManage/listingOperateLog/pageList

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    msku: MSKU (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    operate_uid: 操作人id, array.
    operate_type: 操作类型：  1  调价   2  调库存   3  修改标题   4  编辑商品   5  B2B调价, array.
    operate_time_start: 开始时间【操作时间】，格式：Y-m-d H:i:s, string.
    operate_time_end: 结束时间【操作时间】，格式：Y-m-d H:i:s, string."""
        resp = await self._post("/basicOpen/listingManage/listingOperateLog/pageList", {k: v for k, v in {"sid": sid, "msku": msku, "offset": offset, "length": length, "operate_uid": operate_uid, "operate_type": operate_type, "operate_time_start": operate_time_start, "operate_time_end": operate_time_end}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def pricing_submit(self, pricing_params: list = None) -> dict:
        """批量修改Listing价格.

POST /erp/sc/listing/ProductPricing/pricingSubmit

Args:
    pricing_params: [array] (required), 参数数组，支持多个listing批量调价."""
        resp = await self._post("/erp/sc/listing/ProductPricing/pricingSubmit", {k: v for k, v in {"pricing_params": pricing_params}.items() if v is not None})
        return resp.data or {}
    async def product_relationbatch_link(self, productId: float = None, isSyncPic: float = None, sidAsins: list = None) -> dict:
        """配对/批量配对.

POST /basicOpen/vcservice/productRelation/batchLink

Args:
    sidAsins: 配对的sid和asin对象数组 (required), array.
    productId: 本地商品表主键ID (required), number.
    isSyncPic: 是否同步图片到本地商品 (required), number."""
        resp = await self._post("/basicOpen/vcservice/productRelation/batchLink", {k: v for k, v in {"productId": productId, "isSyncPic": isSyncPic, "sidAsins": sidAsins}.items() if v is not None})
        return resp.data or {}
    async def promotion_listing_detail_coupon(self, sellerSku: str = None, promotionType: list = None, status: list = None, storeId: str = None, startTime: str = None, endTime: str = None, sortField: str = None, sortType: str = None, pageNum: float = None, pageSize: float = None) -> list | dict:
        """查询商品折扣详情-列表-优惠卷.

POST /basicOpen/promotion/listingDetailCoupon

Args:
    sellerSku: seller_sku(msku) (required), string.
    promotionType: 促销类型, array.
    status: 促销状态： 0 其他 1 进行中 2 已过期 3 未开始, array.
    storeId: 店铺id (required), string.
    startTime: 活动开始时间 (required), string.
    endTime: 活动结束时间 (required), string.
    sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (required), string.
    sortType: 排序类型 asc desc (required), string.
    pageNum: 分页页码 (required), number.
    pageSize: 分页大小 (required), number."""
        resp = await self._post("/basicOpen/promotion/listingDetailCoupon", {k: v for k, v in {"sellerSku": sellerSku, "promotionType": promotionType, "status": status, "storeId": storeId, "startTime": startTime, "endTime": endTime, "sortField": sortField, "sortType": sortType, "pageNum": pageNum, "pageSize": pageSize}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_manage(self, sellerSku: str = None, promotionType: list = None, status: list = None, storeId: str = None, startTime: str = None, endTime: str = None, sortField: str = None, sortType: str = None, pageNum: float = None, pageSize: float = None) -> list | dict:
        """查询商品折扣详情-列表-管理促销.

POST /basicOpen/promotion/listingDetailManage

Args:
    sellerSku: seller_sku(msku) (required), string.
    promotionType: 促销类型, array.
    status: 促销状态, array.
    storeId: 店铺id (required), string.
    startTime: 活动开始时间 (required), string.
    endTime: 活动结束时间 (required), string.
    sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (required), string.
    sortType: 排序类型 asc desc (required), string.
    pageNum: 分页页码 (required), number.
    pageSize: 分页大小 (required), number."""
        resp = await self._post("/basicOpen/promotion/listingDetailManage", {k: v for k, v in {"sellerSku": sellerSku, "promotionType": promotionType, "status": status, "storeId": storeId, "startTime": startTime, "endTime": endTime, "sortField": sortField, "sortType": sortType, "pageNum": pageNum, "pageSize": pageSize}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_prime_discount(self, sellerSku: str = None, promotionType: list = None, status: list = None, storeId: str = None, startTime: str = None, endTime: str = None, sortField: str = None, sortType: str = None, pageNum: float = None, pageSize: float = None) -> list | dict:
        """查询商品折扣详情-列表-会员折扣.

POST /basicOpen/promotion/listingDetailPrimeDiscount

Args:
    sellerSku: seller_sku(msku) (required), string.
    promotionType: 促销类型, array.
    status: 促销状态, array.
    storeId: 店铺id (required), string.
    startTime: 活动开始时间 (required), string.
    endTime: 活动结束时间 (required), string.
    sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (required), string.
    sortType: 排序类型 asc desc (required), string.
    pageNum: 分页页码 (required), number.
    pageSize: 分页大小 (required), number."""
        resp = await self._post("/basicOpen/promotion/listingDetailPrimeDiscount", {k: v for k, v in {"sellerSku": sellerSku, "promotionType": promotionType, "status": status, "storeId": storeId, "startTime": startTime, "endTime": endTime, "sortField": sortField, "sortType": sortType, "pageNum": pageNum, "pageSize": pageSize}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_sec_kill(self, sellerSku: str = None, promotionType: list = None, status: list = None, storeId: str = None, startTime: str = None, endTime: str = None, sortField: str = None, sortType: str = None, pageNum: float = None, pageSize: float = None) -> list | dict:
        """查询商品折扣详情-列表-秒杀.

POST /basicOpen/promotion/listingDetailSecKill

Args:
    sellerSku: sellerSku (required), string.
    promotionType: 促销类型, array.
    status: 促销状态, array.
    storeId: 店铺id (required), string.
    startTime: 活动开始时间 (required), string.
    endTime: 活动结束时间 (required), string.
    sortField: 排序项（"cost", "drawQuantity", "exchangeQuantity", "exchangeRate","startTime","salesVolume","salesAmount","startTime"） (required), string.
    sortType: 排序类型 asc desc (required), string.
    pageNum: 分页页码 (required), number.
    pageSize: 分页大小 (required), number."""
        resp = await self._post("/basicOpen/promotion/listingDetailSecKill", {k: v for k, v in {"sellerSku": sellerSku, "promotionType": promotionType, "status": status, "storeId": storeId, "startTime": startTime, "endTime": endTime, "sortField": sortField, "sortType": sortType, "pageNum": pageNum, "pageSize": pageSize}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_list(self, site_date: str = None, start_time: str = None, end_time: str = None, offset: int = None, length: int = None, is_overlay: int = None, sids: list = None, status: list = None, product_status: list = None, promotion_category: list = None) -> list | dict:
        """查询商品折扣列表.

POST /basicOpen/promotion/listingList

Args:
    site_date: 站点时间，格式：Y-m-d (required), string.
    start_time: 开始时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_time: 结束时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    is_overlay: 是否优惠叠加： 0  否 1  是, int.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    status: 促销状态： 0  其他 1  进行中 2  已过期 3  未开始, array.
    product_status: 商品状态： -1  已删除 0  停售 1  在售, array.
    promotion_category: 促销类型： 1  优惠券 2  秒杀 3  管理促销 4   会员折扣, array."""
        resp = await self._post("/basicOpen/promotion/listingList", {k: v for k, v in {"site_date": site_date, "start_time": start_time, "end_time": end_time, "offset": offset, "length": length, "is_overlay": is_overlay, "sids": sids, "status": status, "product_status": product_status, "promotion_category": promotion_category}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_coupon_list(self, start_date: str = None, end_date: str = None, sids: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询促销活动列表-优惠券.

POST /basicOpen/promotionalActivities/coupon/list

Args:
    start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    sids: 店铺id，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/promotionalActivities/coupon/list", {k: v for k, v in {"start_date": start_date, "end_date": end_date, "sids": sids, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_manage_list(self, start_date: str = None, end_date: str = None, sids: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询促销活动列表-管理促销.

POST /basicOpen/promotionalActivities/manage/list

Args:
    start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/promotionalActivities/manage/list", {k: v for k, v in {"start_date": start_date, "end_date": end_date, "sids": sids, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_sec_kill_list(self, start_date: str = None, end_date: str = None, sids: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询促销活动列表-秒杀.

POST /basicOpen/promotionalActivities/secKill/list

Args:
    start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/promotionalActivities/secKill/list", {k: v for k, v in {"start_date": start_date, "end_date": end_date, "sids": sids, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_vip_discount_list(self, start_date: str = None, end_date: str = None, sids: list = None, offset: int = None, length: int = None) -> list | dict:
        """查询促销活动列表-会员折扣/价格折扣.

POST /basicOpen/promotionalActivities/vipDiscount/list

Args:
    start_date: 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    end_date: 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天, string.
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/promotionalActivities/vipDiscount/list", {k: v for k, v in {"start_date": start_date, "end_date": end_date, "sids": sids, "offset": offset, "length": length}.items() if v is not None})
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_listing_relation_tag_list(self, **kwargs) -> list | dict:
        """queryListingRelationTagList. POST /basicOpen/listingManage/queryListingRelationTagList"""
        resp = await self._post("/basicOpen/listingManage/queryListingRelationTagList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

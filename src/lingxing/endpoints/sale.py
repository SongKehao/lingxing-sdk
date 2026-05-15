"""销售/订单/Listing API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint

class SaleEndpoints(BaseEndpoint):
    """领星销售/订单/Listing API (44个接口)."""

    async def add_goods_tag(self, **kwargs) -> list | dict:
        """AddGoodsTag. POST /basicOpen/listingManage/bindListingAndTag"""
        resp = await self._post("/basicOpen/listingManage/bindListingAndTag", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def delete_goods_tag(self, **kwargs) -> dict:
        """DeleteGoodsTag. POST /basicOpen/listingManage/removeListingAndTag"""
        resp = await self._post("/basicOpen/listingManage/removeListingAndTag", kwargs if kwargs else None)
        return resp.data or {}
    async def fbm_order_detail(self, **kwargs) -> list | dict:
        """FBMOrderDetail. POST /erp/sc/routing/order/Order/getOrderDetail"""
        resp = await self._post("/erp/sc/routing/order/Order/getOrderDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbm_order_list(self, **kwargs) -> list | dict:
        """FBMOrderList. POST /erp/sc/routing/order/Order/getOrderList"""
        resp = await self._post("/erp/sc/routing/order/Order/getOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_merchant_shipping_group(self, **kwargs) -> list | dict:
        """GetMerchantShippingGroup. POST /basicOpen/openapi/publish/manage/getMerchantShippingGroup"""
        resp = await self._post("/basicOpen/openapi/publish/manage/getMerchantShippingGroup", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_prices(self, **kwargs) -> list | dict:
        """GetPrices. POST /listing/listing/open/api/listing/getPrices"""
        resp = await self._post("/listing/listing/open/api/listing/getPrices", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def listing(self, **kwargs) -> list | dict:
        """Listing. POST /erp/sc/data/mws/listing"""
        resp = await self._post("/erp/sc/data/mws/listing", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def order_detail(self, **kwargs) -> list | dict:
        """OrderDetail. POST /erp/sc/data/mws/orderDetail"""
        resp = await self._post("/erp/sc/data/mws/orderDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def orderlists(self, **kwargs) -> list | dict:
        """Orderlists. POST /erp/sc/data/mws/orders"""
        resp = await self._post("/erp/sc/data/mws/orders", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_list(self, **kwargs) -> list | dict:
        """ProductList. POST /listing/publish/openapi/amazon/product/list"""
        resp = await self._post("/listing/publish/openapi/amazon/product/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def product_publish(self, **kwargs) -> list | dict:
        """ProductPublish. POST /listing/publish/openapi/amazon/product/publish"""
        resp = await self._post("/listing/publish/openapi/amazon/product/publish", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def productlink(self, **kwargs) -> list | dict:
        """Productlink. POST /erp/sc/storage/product/link"""
        resp = await self._post("/erp/sc/storage/product/link", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_helper_v2(self, **kwargs) -> list | dict:
        """PublishHelperV2. POST /basicOpen/openapi/publish/manage/categoryRoot"""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryRoot", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_category_children(self, **kwargs) -> list | dict:
        """PublishManageCategoryChildren. POST /basicOpen/openapi/publish/manage/categoryChildren"""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryChildren", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_category_root(self, **kwargs) -> list | dict:
        """PublishManageCategoryRoot. POST /basicOpen/openapi/publish/manage/categoryRoot"""
        resp = await self._post("/basicOpen/openapi/publish/manage/categoryRoot", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def publish_manage_get_product_type(self, **kwargs) -> list | dict:
        """PublishManageGetProductType. POST /basicOpen/openapi/publish/manage/getProductType"""
        resp = await self._post("/basicOpen/openapi/publish/manage/getProductType", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_product_list(self, **kwargs) -> list | dict:
        """QueryProductList. POST /listing/publish/openapi/amazon/product/search"""
        resp = await self._post("/listing/publish/openapi/amazon/product/search", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def refund_order(self, **kwargs) -> list | dict:
        """RefundOrder. POST /basicOpen/openapi/salesOrder/refundOrder"""
        resp = await self._post("/basicOpen/openapi/salesOrder/refundOrder", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def sc_order_set_remark(self, **kwargs) -> list | dict:
        """ScOrderSetRemark. POST /basicOpen/platformOrder/scOrder/setRemark"""
        resp = await self._post("/basicOpen/platformOrder/scOrder/setRemark", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def unlink_listing(self, **kwargs) -> list | dict:
        """UnlinkListing. POST /basicOpen/listingManage/unLinkListingPairs"""
        resp = await self._post("/basicOpen/listingManage/unLinkListingPairs", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_fbm_inventory(self, **kwargs) -> dict:
        """UpdateFbmInventory. POST /basicOpen/FbmManagement/modifyFbmInventory"""
        resp = await self._post("/basicOpen/FbmManagement/modifyFbmInventory", kwargs if kwargs else None)
        return resp.data or {}
    async def update_principal(self, **kwargs) -> dict:
        """UpdatePrincipal. POST /listing/listing/open/api/asin/updatePrincipal"""
        resp = await self._post("/listing/listing/open/api/asin/updatePrincipal", kwargs if kwargs else None)
        return resp.data or {}
    async def upload_tracking(self, **kwargs) -> list | dict:
        """UploadTracking. POST /basicOpen/selfShipmentOrder/importLabel"""
        resp = await self._post("/basicOpen/selfShipmentOrder/importLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def adjust_price_adjust_price_manual(self, **kwargs) -> list | dict:
        """adjustPriceAdjustPriceManual. POST /basicOpen/module/adjustPrice/AdjustPriceManual"""
        resp = await self._post("/basicOpen/module/adjustPrice/AdjustPriceManual", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def after_sale_list(self, **kwargs) -> list | dict:
        """afterSaleList. POST /erp/sc/routing/amzod/order/afterSaleList"""
        resp = await self._post("/erp/sc/routing/amzod/order/afterSaleList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def b2b_price_modify_price(self, **kwargs) -> list | dict:
        """b2bPriceModifyPrice. POST /basicOpen/b2bPrice/modifyPrice"""
        resp = await self._post("/basicOpen/b2bPrice/modifyPrice", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_fee_difference_list(self, **kwargs) -> list | dict:
        """fbaFeeDifferenceList. POST /basicOpen/openapi/sale/fbaFeeDifference/order/list"""
        resp = await self._post("/basicOpen/openapi/sale/fbaFeeDifference/order/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_fee_difference_msku_list(self, **kwargs) -> list | dict:
        """fbaFeeDifferenceMskuList. POST /basicOpen/openapi/sale/fbaFeeDifference/msku/list"""
        resp = await self._post("/basicOpen/openapi/sale/fbaFeeDifference/msku/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def global_tag_add_tag(self, **kwargs) -> list | dict:
        """globalTagAddTag. POST /basicOpen/globalTag/listing/addTag"""
        resp = await self._post("/basicOpen/globalTag/listing/addTag", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def global_tag_page_list(self, **kwargs) -> list | dict:
        """globalTagPageList. POST /basicOpen/globalTag/listing/page/list"""
        resp = await self._post("/basicOpen/globalTag/listing/page/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def global_tag_remove_tag(self, **kwargs) -> list | dict:
        """globalTagRemoveTag. POST /basicOpen/globalTag/listing/removeTag"""
        resp = await self._post("/basicOpen/globalTag/listing/removeTag", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def listing_operate_log_page_list(self, **kwargs) -> list | dict:
        """listingOperateLogPageList. POST /basicOpen/listingManage/listingOperateLog/pageList"""
        resp = await self._post("/basicOpen/listingManage/listingOperateLog/pageList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def pricing_submit(self, **kwargs) -> dict:
        """pricingSubmit. POST /erp/sc/listing/ProductPricing/pricingSubmit"""
        resp = await self._post("/erp/sc/listing/ProductPricing/pricingSubmit", kwargs if kwargs else None)
        return resp.data or {}
    async def product_relationbatch_link(self, **kwargs) -> list | dict:
        """productRelationbatchLink. POST /basicOpen/vcservice/productRelation/batchLink"""
        resp = await self._post("/basicOpen/vcservice/productRelation/batchLink", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_coupon(self, **kwargs) -> list | dict:
        """promotionListingDetailCoupon. POST /basicOpen/promotion/listingDetailCoupon"""
        resp = await self._post("/basicOpen/promotion/listingDetailCoupon", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_manage(self, **kwargs) -> list | dict:
        """promotionListingDetailManage. POST /basicOpen/promotion/listingDetailManage"""
        resp = await self._post("/basicOpen/promotion/listingDetailManage", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_prime_discount(self, **kwargs) -> list | dict:
        """promotionListingDetailPrimeDiscount. POST /basicOpen/promotion/listingDetailPrimeDiscount"""
        resp = await self._post("/basicOpen/promotion/listingDetailPrimeDiscount", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_detail_sec_kill(self, **kwargs) -> list | dict:
        """promotionListingDetailSecKill. POST /basicOpen/promotion/listingDetailSecKill"""
        resp = await self._post("/basicOpen/promotion/listingDetailSecKill", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotion_listing_list(self, **kwargs) -> list | dict:
        """promotionListingList. POST /basicOpen/promotion/listingList"""
        resp = await self._post("/basicOpen/promotion/listingList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_coupon_list(self, **kwargs) -> list | dict:
        """promotionalActivitiesCouponList. POST /basicOpen/promotionalActivities/coupon/list"""
        resp = await self._post("/basicOpen/promotionalActivities/coupon/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_manage_list(self, **kwargs) -> list | dict:
        """promotionalActivitiesManageList. POST /basicOpen/promotionalActivities/manage/list"""
        resp = await self._post("/basicOpen/promotionalActivities/manage/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_sec_kill_list(self, **kwargs) -> list | dict:
        """promotionalActivitiesSecKillList. POST /basicOpen/promotionalActivities/secKill/list"""
        resp = await self._post("/basicOpen/promotionalActivities/secKill/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def promotional_activities_vip_discount_list(self, **kwargs) -> list | dict:
        """promotionalActivitiesVipDiscountList. POST /basicOpen/promotionalActivities/vipDiscount/list"""
        resp = await self._post("/basicOpen/promotionalActivities/vipDiscount/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_listing_relation_tag_list(self, **kwargs) -> list | dict:
        """queryListingRelationTagList. POST /basicOpen/listingManage/queryListingRelationTagList"""
        resp = await self._post("/basicOpen/listingManage/queryListingRelationTagList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

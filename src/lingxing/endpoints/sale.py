"""Auto-generated SaleEndpoints endpoints from official lingxing docs."""
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...core.openapi import OpenApiBase


class SaleEndpoints:
    """领星API - SaleEndpoints (44个接口)."""

    def __init__(self, openapi: "OpenApiBase"):
        self._request_with_token = openapi.request_with_auto_token

    async def add_goods_tag(self, **kwargs) -> dict:
        """AddGoodsTag.
        
        POST /basicOpen/listingManage/bindListingAndTag
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/bindListingAndTag",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def delete_goods_tag(self, **kwargs) -> dict:
        """DeleteGoodsTag.
        
        POST /basicOpen/listingManage/removeListingAndTag
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/removeListingAndTag",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbmorder_detail(self, **kwargs) -> dict:
        """FBMOrderDetail.
        
        POST /erp/sc/routing/order/Order/getOrderDetail
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/order/Order/getOrderDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fbmorder_list(self, **kwargs) -> dict:
        """FBMOrderList.
        
        POST /erp/sc/routing/order/Order/getOrderList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/order/Order/getOrderList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_merchant_shipping_group(self, **kwargs) -> dict:
        """GetMerchantShippingGroup.
        
        POST /basicOpen/openapi/publish/manage/getMerchantShippingGroup
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/publish/manage/getMerchantShippingGroup",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def get_prices(self, **kwargs) -> dict:
        """GetPrices.
        
        POST /listing/listing/open/api/listing/getPrices
        """
        return await self._request_with_token(
            route_name="/listing/listing/open/api/listing/getPrices",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def listing(self, **kwargs) -> dict:
        """Listing.
        
        POST /erp/sc/data/mws/listing
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws/listing",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def order_detail(self, **kwargs) -> dict:
        """OrderDetail.
        
        POST /erp/sc/data/mws/orderDetail
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws/orderDetail",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def orderlists(self, **kwargs) -> dict:
        """Orderlists.
        
        POST /erp/sc/data/mws/orders
        """
        return await self._request_with_token(
            route_name="/erp/sc/data/mws/orders",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_list(self, **kwargs) -> dict:
        """ProductList.
        
        POST /listing/publish/openapi/amazon/product/list
        """
        return await self._request_with_token(
            route_name="/listing/publish/openapi/amazon/product/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_publish(self, **kwargs) -> dict:
        """ProductPublish.
        
        POST /listing/publish/openapi/amazon/product/publish
        """
        return await self._request_with_token(
            route_name="/listing/publish/openapi/amazon/product/publish",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def productlink(self, **kwargs) -> dict:
        """Productlink.
        
        POST /erp/sc/storage/product/link
        """
        return await self._request_with_token(
            route_name="/erp/sc/storage/product/link",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def publish_helper_v2(self, **kwargs) -> dict:
        """PublishHelperV2.
        
        POST /basicOpen/openapi/publish/manage/categoryRoot
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/publish/manage/categoryRoot",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def publish_manage_category_children(self, **kwargs) -> dict:
        """PublishManageCategoryChildren.
        
        POST /basicOpen/openapi/publish/manage/categoryChildren
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/publish/manage/categoryChildren",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def publish_manage_category_root(self, **kwargs) -> dict:
        """PublishManageCategoryRoot.
        
        POST /basicOpen/openapi/publish/manage/categoryRoot
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/publish/manage/categoryRoot",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def publish_manage_get_product_type(self, **kwargs) -> dict:
        """PublishManageGetProductType.
        
        POST /basicOpen/openapi/publish/manage/getProductType
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/publish/manage/getProductType",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def query_product_list(self, **kwargs) -> dict:
        """QueryProductList.
        
        POST /listing/publish/openapi/amazon/product/search
        """
        return await self._request_with_token(
            route_name="/listing/publish/openapi/amazon/product/search",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def refund_order(self, **kwargs) -> dict:
        """RefundOrder.
        
        POST /basicOpen/openapi/salesOrder/refundOrder
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/salesOrder/refundOrder",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def sc_order_set_remark(self, **kwargs) -> dict:
        """ScOrderSetRemark.
        
        POST /basicOpen/platformOrder/scOrder/setRemark
        """
        return await self._request_with_token(
            route_name="/basicOpen/platformOrder/scOrder/setRemark",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def unlink_listing(self, **kwargs) -> dict:
        """UnlinkListing.
        
        POST /basicOpen/listingManage/unLinkListingPairs
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/unLinkListingPairs",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_fbm_inventory(self, **kwargs) -> dict:
        """UpdateFbmInventory.
        
        POST /basicOpen/FbmManagement/modifyFbmInventory
        """
        return await self._request_with_token(
            route_name="/basicOpen/FbmManagement/modifyFbmInventory",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def update_principal(self, **kwargs) -> dict:
        """UpdatePrincipal.
        
        POST /listing/listing/open/api/asin/updatePrincipal
        """
        return await self._request_with_token(
            route_name="/listing/listing/open/api/asin/updatePrincipal",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def upload_tracking(self, **kwargs) -> dict:
        """UploadTracking.
        
        POST /basicOpen/selfShipmentOrder/importLabel
        """
        return await self._request_with_token(
            route_name="/basicOpen/selfShipmentOrder/importLabel",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def adjust_price_adjust_price_manual(self, **kwargs) -> dict:
        """adjustPriceAdjustPriceManual.
        
        POST /basicOpen/module/adjustPrice/AdjustPriceManual
        """
        return await self._request_with_token(
            route_name="/basicOpen/module/adjustPrice/AdjustPriceManual",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def after_sale_list(self, **kwargs) -> dict:
        """afterSaleList.
        
        POST /erp/sc/routing/amzod/order/afterSaleList
        """
        return await self._request_with_token(
            route_name="/erp/sc/routing/amzod/order/afterSaleList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def b2b_price_modify_price(self, **kwargs) -> dict:
        """b2bPriceModifyPrice.
        
        POST /basicOpen/b2bPrice/modifyPrice
        """
        return await self._request_with_token(
            route_name="/basicOpen/b2bPrice/modifyPrice",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fba_fee_difference_list(self, **kwargs) -> dict:
        """fbaFeeDifferenceList.
        
        POST /basicOpen/openapi/sale/fbaFeeDifference/order/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/sale/fbaFeeDifference/order/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def fba_fee_difference_msku_list(self, **kwargs) -> dict:
        """fbaFeeDifferenceMskuList.
        
        POST /basicOpen/openapi/sale/fbaFeeDifference/msku/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/openapi/sale/fbaFeeDifference/msku/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def global_tag_add_tag(self, **kwargs) -> dict:
        """globalTagAddTag.
        
        POST /basicOpen/globalTag/listing/addTag
        """
        return await self._request_with_token(
            route_name="/basicOpen/globalTag/listing/addTag",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def global_tag_page_list(self, **kwargs) -> dict:
        """globalTagPageList.
        
        POST /basicOpen/globalTag/listing/page/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/globalTag/listing/page/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def global_tag_remove_tag(self, **kwargs) -> dict:
        """globalTagRemoveTag.
        
        POST /basicOpen/globalTag/listing/removeTag
        """
        return await self._request_with_token(
            route_name="/basicOpen/globalTag/listing/removeTag",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def listing_operate_log_page_list(self, **kwargs) -> dict:
        """listingOperateLogPageList.
        
        POST /basicOpen/listingManage/listingOperateLog/pageList
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/listingOperateLog/pageList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def pricing_submit(self, **kwargs) -> dict:
        """pricingSubmit.
        
        POST /erp/sc/listing/ProductPricing/pricingSubmit
        """
        return await self._request_with_token(
            route_name="/erp/sc/listing/ProductPricing/pricingSubmit",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def product_relationbatch_link(self, **kwargs) -> dict:
        """productRelationbatchLink.
        
        POST /basicOpen/vcservice/productRelation/batchLink
        """
        return await self._request_with_token(
            route_name="/basicOpen/vcservice/productRelation/batchLink",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotion_listing_detail_coupon(self, **kwargs) -> dict:
        """promotionListingDetailCoupon.
        
        POST /basicOpen/promotion/listingDetailCoupon
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotion/listingDetailCoupon",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotion_listing_detail_manage(self, **kwargs) -> dict:
        """promotionListingDetailManage.
        
        POST /basicOpen/promotion/listingDetailManage
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotion/listingDetailManage",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotion_listing_detail_prime_discount(self, **kwargs) -> dict:
        """promotionListingDetailPrimeDiscount.
        
        POST /basicOpen/promotion/listingDetailPrimeDiscount
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotion/listingDetailPrimeDiscount",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotion_listing_detail_sec_kill(self, **kwargs) -> dict:
        """promotionListingDetailSecKill.
        
        POST /basicOpen/promotion/listingDetailSecKill
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotion/listingDetailSecKill",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotion_listing_list(self, **kwargs) -> dict:
        """promotionListingList.
        
        POST /basicOpen/promotion/listingList
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotion/listingList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotional_activities_coupon_list(self, **kwargs) -> dict:
        """promotionalActivitiesCouponList.
        
        POST /basicOpen/promotionalActivities/coupon/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotionalActivities/coupon/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotional_activities_manage_list(self, **kwargs) -> dict:
        """promotionalActivitiesManageList.
        
        POST /basicOpen/promotionalActivities/manage/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotionalActivities/manage/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotional_activities_sec_kill_list(self, **kwargs) -> dict:
        """promotionalActivitiesSecKillList.
        
        POST /basicOpen/promotionalActivities/secKill/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotionalActivities/secKill/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def promotional_activities_vip_discount_list(self, **kwargs) -> dict:
        """promotionalActivitiesVipDiscountList.
        
        POST /basicOpen/promotionalActivities/vipDiscount/list
        """
        return await self._request_with_token(
            route_name="/basicOpen/promotionalActivities/vipDiscount/list",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )
    async def query_listing_relation_tag_list(self, **kwargs) -> dict:
        """queryListingRelationTagList.
        
        POST /basicOpen/listingManage/queryListingRelationTagList
        """
        return await self._request_with_token(
            route_name="/basicOpen/listingManage/queryListingRelationTagList",
            method="POST",
            req_body={k: v for k, v in kwargs.items() if v is not None}
        )

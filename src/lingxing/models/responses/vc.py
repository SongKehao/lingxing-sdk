"""Auto-generated response models for VC."""

from typing import List, Optional

from pydantic import Field

from ..common import LingXingModel


class ListingmanageVclistingPagelistClassificationRank(LingXingModel):
    """classification_rank sub-structure."""

    classification_id: Optional[str] = Field(None, description="分类ID")
    title: Optional[str] = Field(None, description="分类名")
    link: Optional[str] = Field(None, description="分类链接")
    rank: Optional[str] = Field(None, description="排名")


class ListingmanageVclistingPagelistDisplayGroupRank(LingXingModel):
    """display_group_rank sub-structure."""

    website_display_group: Optional[str] = Field(None, description="分类组名")
    title: Optional[str] = Field(None, description="分类名")
    link: Optional[str] = Field(None, description="分类链接")
    rank: Optional[str] = Field(None, description="排名")


class ListingmanageVclistingPagelistPrincipalList(LingXingModel):
    """principal_list sub-structure."""

    uid: Optional[str] = Field(None, description="负责人uid")
    real_name: Optional[str] = Field(None, description="负责人姓名")


class ListingmanageVclistingPagelistResponse(LingXingModel):
    """查询Listing列表."""

    total: Optional[int] = Field(None, description="总数")
    vc_store_id: Optional[str] = Field(None, description="VC店铺id")
    small_min_image_url: Optional[str] = Field(None, description="在线商品略缩图地址")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    msku: Optional[str] = Field(None, description="MSKU")
    upc: Optional[str] = Field(None, description="UPC")
    ean: Optional[str] = Field(None, description="EAN")
    item_name: Optional[str] = Field(None, description="标题")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    local_sku: Optional[str] = Field(None, description="SKU")
    local_name: Optional[str] = Field(None, description="品名")
    category_name: Optional[str] = Field(None, description="本地产品分类名")
    brand_id: Optional[str] = Field(None, description="本地产品品牌ID")
    product_id: Optional[str] = Field(None, description="本地产品ID")
    classification_rank: Optional[List[ListingmanageVclistingPagelistClassificationRank]] = Field(
        None, description="小类排名"
    )
    display_group_rank: Optional[List[ListingmanageVclistingPagelistDisplayGroupRank]] = Field(
        None, description="大类排名"
    )
    reviews_num: Optional[str] = Field(None, description="评论数")
    stars: Optional[str] = Field(None, description="星级")
    principal_list: Optional[List[ListingmanageVclistingPagelistPrincipalList]] = Field(None, description="负责人列表")
    remark: Optional[str] = Field(None, description="备注")
    on_sale_time: Optional[str] = Field(None, description="开售时间")
    status: Optional[int] = Field(None, description="在线商品状态： -1已删除 0 停售 1 在售")
    price: Optional[str] = Field(None, description="优惠金额")
    price_currency_icon: Optional[str] = Field(None, description="优惠金额货币符号")


class GetinvoiceDetailInvoice(LingXingModel):
    """invoice sub-structure."""

    order_no: Optional[str] = Field(None, description="发货单号")
    purchase_order_number: Optional[str] = Field(None, description="订单号")
    remark: Optional[str] = Field(None, description="备注")
    shipping_wid: Optional[str] = Field(None, description="发货仓库id")
    shipping_warehouse_name: Optional[str] = Field(None, description="发货仓库名称")
    shipment_time: Optional[str] = Field(None, description="发货时间")
    shipment_user: Optional[str] = Field(None, description="发货人")
    status: Optional[float] = Field(None, description="发货状态")
    create_user: Optional[str] = Field(None, description="创建人名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    shipment_type: Optional[str] = Field(None, description="发货类型")
    status_name: Optional[str] = Field(None, description="状态名称")
    total_num: Optional[float] = Field(None, description="总发货量")
    estimated_pickup_time: Optional[str] = Field(None, description="预计取货时间")
    shipment_type_name: Optional[str] = Field(None, description="出库类型")
    source_type: Optional[float] = Field(None, description="来源类型（0：订单生成，1：货件生成）")
    invoice_model: Optional[float] = Field(None, description="下单模式（0：手工下单 1：系统下单）")
    outbound_date: Optional[str] = Field(None, description="出库日期")
    items: Optional[list] = Field(None, description="发货单明细列表")
    invoice_tracking_list: Optional[list] = Field(None, description="物流信息")


class GetinvoiceDetailResponse(LingXingModel):
    """查询VC发货单详情."""

    invoice: Optional[List[GetinvoiceDetailInvoice]] = Field(None, description="发货单信息")


class GetinvoicePageListList(LingXingModel):
    """list sub-structure."""

    gmt_create: Optional[str] = Field(None, description="创建时间")
    gmt_modified: Optional[str] = Field(None, description="修改时间")
    id: Optional[str] = Field(None, description="主键id")
    order_no: Optional[str] = Field(None, description="发货单号")
    purchase_order_number: Optional[str] = Field(None, description="订单号")
    remark: Optional[str] = Field(None, description="备注")
    shipping_wid: Optional[str] = Field(None, description="发货仓库ID")
    shipping_warehouse_name: Optional[str] = Field(None, description="发货仓库名称")
    shipment_time: Optional[str] = Field(None, description="发货时间")
    shipment_user: Optional[str] = Field(None, description="发货人")
    status: Optional[float] = Field(None, description="发货状态")
    create_user: Optional[str] = Field(None, description="创建人名称")
    create_time: Optional[str] = Field(None, description="创建时间")
    shipment_type: Optional[str] = Field(None, description="发货类型")
    status_name: Optional[str] = Field(None, description="状态名称")
    total_num: Optional[float] = Field(None, description="总发货量")
    estimated_pickup_time: Optional[str] = Field(None, description="预计到货时间")
    shipment_type_name: Optional[str] = Field(None, description="出库类型名称")
    source_type: Optional[float] = Field(None, description="来源类型（0：订单生成，1：货件生成）")
    invoice_model: Optional[float] = Field(None, description="下单模式（0：手工下单 1：系统下单）")
    outbound_date: Optional[str] = Field(None, description="出库日期")
    items: Optional[list] = Field(None, description="发货单明细列表")


class GetinvoicePageListResponse(LingXingModel):
    """查询VC发货单列表."""

    count: Optional[float] = Field(None, description="总记录数")
    list: Optional[List[GetinvoicePageListList]] = Field(None, description="发货单列表")


class PlatformauthVcsellerPagelistResponse(LingXingModel):
    """查询VC店铺列表."""

    total: Optional[int] = Field(None, description="总数")
    account_id: Optional[int] = Field(None, description="账号ID")
    seller_id: Optional[str] = Field(None, description="SELLER_ID")
    account_name: Optional[str] = Field(None, description="账号名称")
    region: Optional[str] = Field(None, description="站点简称")
    region_name: Optional[str] = Field(None, description="站点名称")
    vc_store_id: Optional[str] = Field(None, description="VC店铺id")
    name: Optional[str] = Field(None, description="店铺名称")
    status: Optional[int] = Field(None, description="店铺授权服务状态： -1 删除 0 暂停同步 1 正常同步 2 授权异常")
    mid: Optional[int] = Field(None, description="站点id")


class PlatformorderVcorderPagelistPurchaseOrderSkuList(LingXingModel):
    """purchase_order_sku_list sub-structure."""

    id: Optional[str] = Field(None, description="ID")
    vc_store_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    asin: Optional[str] = Field(None, description="ASIN")
    upc: Optional[str] = Field(None, description="UPC")
    ean: Optional[str] = Field(None, description="EAN")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    item_name: Optional[str] = Field(None, description="标题")
    large_main_image_url: Optional[str] = Field(None, description="在线商品主图大图")
    medium_main_image_url: Optional[str] = Field(None, description="在线商品主图中尺寸")
    small_main_image_url: Optional[str] = Field(None, description="在线商品主图略缩图")
    has_principal: Optional[int] = Field(None, description="是否分配负责人： 0 否 1 是")
    purchase_amount: Optional[int] = Field(None, description="采购量")
    sequence_number: Optional[str] = Field(None, description="序列号")
    vendor_product_id: Optional[str] = Field(None, description="商品编码")
    local_po_number: Optional[str] = Field(None, description="本地po编号")
    purchase_order_number: Optional[str] = Field(None, description="订单号")
    unit_price: Optional[str] = Field(None, description="单价")
    net_price: Optional[str] = Field(None, description="成本价")
    net_price_currency_code: Optional[str] = Field(None, description="成本价货币类型")
    net_price_currency_icon: Optional[str] = Field(None, description="成本价货币符号")
    tax_amount: Optional[str] = Field(None, description="税额")
    tax_amount_currency_code: Optional[str] = Field(None, description="税额货币类型")
    tax_amount_currency_icon: Optional[str] = Field(None, description="税额货币符号")
    tax_rate: Optional[str] = Field(None, description="税率")
    tax_rate_percent: Optional[str] = Field(None, description="税率百分比")
    deal_total_price: Optional[str] = Field(None, description="成交总价")
    deal_unit_price: Optional[str] = Field(None, description="成交单价")
    is_back_order_allowed: Optional[str] = Field(None, description="是否可以延期发货： 0 否 1 是")
    shipped_amount: Optional[int] = Field(None, description="已发货数量")
    to_ship_amount: Optional[int] = Field(None, description="待发货数量")
    local_name: Optional[str] = Field(None, description="品名")
    local_sku: Optional[str] = Field(None, description="SKU")
    product_id: Optional[str] = Field(None, description="本地产品id")
    available_amount: Optional[int] = Field(None, description="库存可用量")
    asin_url: Optional[str] = Field(None, description="ASIN跳转地址")
    pic_url: Optional[str] = Field(None, description="图片地址")
    accepted_quantity: Optional[int] = Field(None, description="接受量")
    rejected_quantity: Optional[int] = Field(None, description="拒绝量")
    received_quantity: Optional[int] = Field(None, description="签收量")


class PlatformorderVcorderPagelistResponse(LingXingModel):
    """查询VC订单列表."""

    total: Optional[int] = Field(None, description="总数")
    gmt_create: Optional[str] = Field(None, description="订单创建时间")
    gmt_modified: Optional[str] = Field(None, description="订单更新时间")
    id: Optional[str] = Field(None, description="订单ID")
    purchase_order_number: Optional[str] = Field(None, description="订单编号")
    customer_order_number: Optional[str] = Field(None, description="客户订单号【DF类型订单】")
    vc_store_id: Optional[str] = Field(None, description="vc店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    purchase_order_type: Optional[int] = Field(None, description="订单类型： 0 DF 1 PO")
    purchase_order_state: Optional[str] = Field(
        None,
        description="DF订单状态： New 新的订单 SHIPPED 已发货 ACCEPTED 已确定 CANCELLED 已取消 PO订单状态： Acknowledged 确认 Closed 关闭",
    )
    purchase_order_process_state: Optional[int] = Field(
        None, description="订单流转状态： 0 待处理 1 待发货 2 已完成 3 已取消"
    )
    purchase_order_date: Optional[str] = Field(None, description="订单下单时间")
    ack_status: Optional[int] = Field(
        None, description="ack状态：0：待确认 1：确认中 2：已确认 3：确认失败 4：平台已确认"
    )
    ack_status_desc: Optional[str] = Field(
        None, description="ack状态说明，0：待确认 1：确认中 2：已确认 3：确认失败 4：平台已确认"
    )
    ack_update_time: Optional[str] = Field(None, description="ack更新时间")
    focus_party_id: Optional[str] = Field(None, description="仓库id")
    erp_warehouse_name: Optional[str] = Field(None, description="配对后的本地仓名称")
    erp_warehouse_id: Optional[str] = Field(None, description="配对后的本地仓id")
    ship_window_time: Optional[str] = Field(None, description="DF要求发货时间")
    ship_window_start: Optional[str] = Field(None, description="PO要求起始发货时间")
    ship_windows_end: Optional[str] = Field(None, description="PO要求截止发货时间")
    total_price: Optional[str] = Field(None, description="订单总金额")
    currency_code: Optional[str] = Field(None, description="币种")
    currency_icon: Optional[str] = Field(None, description="币种符号")
    item_amount: Optional[int] = Field(None, description="货物总数量")
    local_po_number: Optional[str] = Field(None, description="本地po号")
    remark: Optional[str] = Field(None, description="订单备注")
    shipment_confirm_status: Optional[int] = Field(
        None, description="确认发货状态： 1 未确认 2 确认中 3 确认失败 4 确认成功 5 平台已确认"
    )
    shipment_label_status: Optional[int] = Field(None, description="标签状态： 1 未请求 2 请求中 3 请求失败 4 请求成功")
    print_num: Optional[int] = Field(None, description="标签打印次数")
    purchase_order_sku_list: Optional[List[PlatformorderVcorderPagelistPurchaseOrderSkuList]] = Field(
        None, description="订单商品明细数据"
    )


class PlatformorderVcorderdfDetailShipToPartyAddress(LingXingModel):
    """ship_to_party_address sub-structure."""

    name: Optional[str] = Field(None, description="收件人")
    address_line1: Optional[str] = Field(None, description="地址1")
    address_line2: Optional[str] = Field(None, description="地址2")
    address_line3: Optional[str] = Field(None, description="地址3")
    city: Optional[str] = Field(None, description="城市")
    county: Optional[str] = Field(None, description="国家")
    district: Optional[str] = Field(None, description="区域")
    state_or_region: Optional[str] = Field(None, description="州")
    postal_code: Optional[str] = Field(None, description="邮编")
    country_code: Optional[str] = Field(None, description="国家编码")
    phone: Optional[str] = Field(None, description="电话")


class PlatformorderVcorderdfDetailItems(LingXingModel):
    """items sub-structure."""

    asin: Optional[str] = Field(None, description="ASIN")
    msku: Optional[str] = Field(None, description="MSKU")
    parent_asin: Optional[str] = Field(None, description="父ASIN")
    item_name: Optional[str] = Field(None, description="标题")
    large_main_image_url: Optional[str] = Field(None, description="在线商品主图大图")
    medium_main_image_url: Optional[str] = Field(None, description="在线商品主图中尺寸")
    small_main_image_url: Optional[str] = Field(None, description="在线商品主图缩略图")
    pic_url: Optional[str] = Field(None, description="图片地址")
    local_sku: Optional[str] = Field(None, description="SKU")
    local_name: Optional[str] = Field(None, description="品名")
    purchase_amount: Optional[str] = Field(None, description="采购量")
    shipped_amount: Optional[str] = Field(None, description="已发货量")
    waiting_shipped_amount: Optional[str] = Field(None, description="待发货量")
    available_amount: Optional[str] = Field(None, description="可用量")
    sequence_number: Optional[str] = Field(None, description="序号")
    unit_price: Optional[str] = Field(None, description="单价")
    net_price: Optional[str] = Field(None, description="成本价")
    net_price_currency_code: Optional[str] = Field(None, description="币种")
    net_price_currency_icon: Optional[str] = Field(None, description="货币符号")
    tax_amount: Optional[str] = Field(None, description="税额")
    tax_amount_currency_code: Optional[str] = Field(None, description="币种")
    tax_amount_currency_icon: Optional[str] = Field(None, description="货币符号")
    tax_rate: Optional[str] = Field(None, description="税率")
    tax_rate_percent: Optional[str] = Field(None, description="税率的百分比")
    deal_total_price: Optional[str] = Field(None, description="成交总价")
    deal_unit_price: Optional[str] = Field(None, description="成交单价")


class PlatformorderVcorderdfDetailTrackingNumberList(LingXingModel):
    """tracking_number_List sub-structure."""

    box_no: Optional[str] = Field(None, description="箱号")
    tracking_number: Optional[str] = Field(None, description="跟踪号")


class PlatformorderVcorderdfDetailResponse(LingXingModel):
    """查询VC订单详情【DF】."""

    total: Optional[int] = Field(None, description="总数")
    vc_store_id: Optional[str] = Field(None, description="vc店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    local_po_number: Optional[str] = Field(None, description="本地po号")
    purchase_order_number: Optional[str] = Field(None, description="订单编号")
    purchase_order_date: Optional[str] = Field(None, description="下单时间")
    purchase_order_state: Optional[str] = Field(
        None, description="订单状态： New 新的订单 SHIPPED 已发货 ACCEPTED 已确定 CANCELED 已取消"
    )
    purchase_order_type: Optional[str] = Field(None, description="订单类型： 0 DF 1 PO")
    bill_to_party_id: Optional[str] = Field(None, description="结算方式")
    ship_from_party_id: Optional[str] = Field(None, description="供货编码")
    related_warehouse_id: Optional[str] = Field(None, description="仓库id")
    related_warehouse_name: Optional[str] = Field(None, description="仓库名称")
    ship_method: Optional[str] = Field(None, description="运输方式")
    ship_window_time: Optional[str] = Field(None, description="要求发货时间")
    promised_delivery_date: Optional[str] = Field(None, description="承诺送达时间")
    is_pslip_required: Optional[str] = Field(None, description="是否需要装箱清单： 0 否 1 是")
    is_gift: Optional[str] = Field(None, description="是否包含礼物： 0 否 1 是")
    is_scheduled_delivery_shipment: Optional[str] = Field(None, description="是否预定交付计划： 0 否 1 是")
    is_priority_shipment: Optional[str] = Field(None, description="是否优先发货： 0 否 1 是")
    ship_to_party_address: Optional[List[PlatformorderVcorderdfDetailShipToPartyAddress]] = Field(
        None, description="收货方地址"
    )
    message_to_customer: Optional[str] = Field(None, description="交易赠言")
    total_price: Optional[str] = Field(None, description="订单总金额")
    currency_code: Optional[str] = Field(None, description="币种")
    currency_icon: Optional[str] = Field(None, description="货币符号")
    item_amount: Optional[str] = Field(None, description="货物数量")
    remark: Optional[str] = Field(None, description="备注")
    items: Optional[List[PlatformorderVcorderdfDetailItems]] = Field(None, description="商品列表")
    tracking_number_list: Optional[List[PlatformorderVcorderdfDetailTrackingNumberList]] = Field(
        None, description="箱号/跟踪号列表"
    )


class PlatformorderVcorderdfGetshippinglabelLabelList(LingXingModel):
    """label_list sub-structure."""

    id: Optional[str] = Field(None, description="订单ID")
    purchase_order_number: Optional[str] = Field(None, description="订单编号")
    label_count: Optional[int] = Field(None, description="标签数量")
    error_msg: Optional[str] = Field(None, description="错误信息")


class PlatformorderVcorderdfGetshippinglabelResponse(LingXingModel):
    """VC订单-打印标签【DF】."""

    total: Optional[int] = Field(None, description="总数")
    label_list: Optional[List[PlatformorderVcorderdfGetshippinglabelLabelList]] = Field(None, description="标签数据")
    pdf_url: Optional[str] = Field(None, description="PDF下载链接")
    download_url: Optional[str] = Field(None, description="压缩包下载链接")


class PlatformorderVcorderpoDetailItems(LingXingModel):
    """items sub-structure."""

    sequence_number: Optional[str] = Field(None, description="序号")
    asin: Optional[str] = Field(None, description="ASIN")
    asin_url: Optional[str] = Field(None, description="ASIN地址")
    msku: Optional[str] = Field(None, description="MSKU")
    item_name: Optional[str] = Field(None, description="标题")
    large_main_image_url: Optional[str] = Field(None, description="在线商品主图大图")
    medium_main_image_url: Optional[str] = Field(None, description="在线商品主图中尺寸")
    small_main_image_url: Optional[str] = Field(None, description="在线商品主图缩略图")
    purchase_amount: Optional[str] = Field(None, description="数量")
    local_po_number: Optional[str] = Field(None, description="本地po号")
    unit_price: Optional[str] = Field(None, description="单价")
    net_price: Optional[str] = Field(None, description="成本价")
    net_price_currency_code: Optional[str] = Field(None, description="币种")
    net_price_currency_icon: Optional[str] = Field(None, description="货币符号")
    tax_amount: Optional[str] = Field(None, description="税额")
    tax_amount_currency_code: Optional[str] = Field(None, description="币种")
    tax_amount_currency_icon: Optional[str] = Field(None, description="货币符号")
    tax_rate: Optional[str] = Field(None, description="税率")
    tax_rate_percent: Optional[str] = Field(None, description="税率的百分比")
    deal_total_price: Optional[str] = Field(None, description="成交总价")
    deal_unit_price: Optional[str] = Field(None, description="成交单价")
    is_back_order_allowed: Optional[str] = Field(None, description="是否可以延期发货： 0 否 1 是")
    shipped_amount: Optional[str] = Field(None, description="已发货量")
    to_ship_amount: Optional[str] = Field(None, description="待发货量")
    local_name: Optional[str] = Field(None, description="品名")
    local_sku: Optional[str] = Field(None, description="SKU")


class PlatformorderVcorderpoDetailResponse(LingXingModel):
    """查询VC订单详情【PO】."""

    total: Optional[int] = Field(None, description="总数")
    vc_store_id: Optional[str] = Field(None, description="店铺id")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    purchase_order_number: Optional[str] = Field(None, description="订单编号")
    local_po_number: Optional[str] = Field(None, description="本地订单编号")
    purchase_order_date: Optional[str] = Field(None, description="下单时间")
    purchase_order_state: Optional[str] = Field(None, description="订单状态： Acknowledged 确认 Closed 关闭")
    purchase_order_process_state: Optional[int] = Field(
        None, description="订单流转状态： 0 待处理 1 确认中 2 确认成功 3 确认失败"
    )
    payment_method: Optional[str] = Field(None, description="支付类型")
    purchase_order_type: Optional[str] = Field(None, description="订单类型： 0 DF 1 PO")
    remark: Optional[str] = Field(None, description="备注")
    related_warehouse_id: Optional[str] = Field(None, description="仓库id")
    related_warehouse_name: Optional[str] = Field(None, description="仓库名称")
    ship_to_party_id: Optional[str] = Field(None, description="收件人")
    total_price: Optional[str] = Field(None, description="订单总金额")
    currency_code: Optional[str] = Field(None, description="币种")
    currency_icon: Optional[str] = Field(None, description="货币符号")
    item_amount: Optional[str] = Field(None, description="货物数量")
    ship_window_start: Optional[str] = Field(None, description="发货窗口开始时间")
    ship_window_end: Optional[str] = Field(None, description="发货窗口结束时间")
    delivery_window_start: Optional[str] = Field(None, description="交货窗口开始时间")
    delivery_window_end: Optional[str] = Field(None, description="交货窗口结束时间")
    items: Optional[List[PlatformorderVcorderpoDetailItems]] = Field(None, description="商品数据")


class PlatformorderVcorderdfConfirmshipmentResponse(LingXingModel):
    """VC订单-确认发货【DF】."""


class PlatformorderVcorderdfSubmitsshippinglabelResponse(LingXingModel):
    """VC订单-请求标签【DF】."""

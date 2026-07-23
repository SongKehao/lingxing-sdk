"""Auto-generated response models for Product."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


# ==================== 产品标签（US-003 补全）====================
class LabelProductListResponse(LingXingModel):
    """查询产品标签 (/label/operation/v1/label/product/list)."""
    label_id: Optional[str] = Field(None, description="标签id")
    label: Optional[str] = Field(None, description="标签名称")
    total: Optional[int] = None


class LabelProductCreateResponse(LingXingModel):
    """创建产品标签 (/label/operation/v1/label/product/create)."""
    label_id: Optional[str] = None
    msg: Optional[str] = None


class LabelProductMarkResponse(LingXingModel):
    """标记产品标签 (/label/operation/v1/label/product/mark)."""
    msg: Optional[str] = None


class LabelProductUnmarklabelResponse(LingXingModel):
    """删除产品标签 (/label/operation/v1/label/product/unmarkLabel)."""
    msg: Optional[str] = None


class ProductGetpagingloglistsResponse(LingXingModel):
    """查询操作日志."""
    action: Optional[str] = Field(None, description="操作类型")
    datetime: Optional[str] = Field(None, description="datetime（日期格式：yyyy-MM-dd hh:mm:ss）")
    detail: Optional[str] = Field(None, description="操作详情")
    user_id: Optional[int] = Field(None, description="操作人ID")
    user_name: Optional[str] = Field(None, description="操作人")
    total: Optional[int] = Field(None, description="总记录数")


class ProductGettransparencyproductlistPagelist(LingXingModel):
    """pageList sub-structure."""
    account_name: Optional[str] = Field(None, description="账号名称")
    asin: Optional[str] = Field(None, description="asin")
    brand_name: Optional[str] = Field(None, description="品牌名称")
    gtin: Optional[str] = Field(None, description="gtin")
    id: Optional[int] = Field(None, description="产品id")
    label_type: Optional[str] = Field(None, description="标签类型")
    pic_url: Optional[str] = Field(None, description="图片url")
    product_status: Optional[str] = Field(None, description="产品状态")
    seller_sku: Optional[str] = Field(None, description="卖家sku")
    ta_id: Optional[int] = Field(None, description="账号id")
    tcode_not_used_total: Optional[int] = Field(None, description="未使用tcode")
    tcode_total: Optional[int] = Field(None, description="合计tcode")
    title: Optional[str] = Field(None, description="标题")

class ProductGettransparencyproductlistResponse(LingXingModel):
    """产品管理-查询透明计划商品列表."""
    page_list: Optional[List[ProductGettransparencyproductlistPagelist]] = Field(None, description="分页列表")
    total: Optional[int] = Field(None, description="总记录数")


class LocalInventoryBrandResponse(LingXingModel):
    """查询产品品牌列表."""
    bid: Optional[int] = Field(None, description="品牌id")
    title: Optional[str] = Field(None, description="品牌名称")
    brand_code: Optional[str] = Field(None, description="品牌简码")


class LocalInventoryBatchgetproductinfoPictureList(LingXingModel):
    """picture_list sub-structure."""
    pic_url: Optional[str] = Field(None, description="图片链接")
    is_primary: Optional[int] = Field(None, description="是否产品主图：0 否，1 是")

class LocalInventoryBatchgetproductinfoPermissionUserInfo(LingXingModel):
    """permission_user_info sub-structure."""
    permission_uid: Optional[int] = Field(None, description="负责人id")
    permission_user_name: Optional[str] = Field(None, description="负责人名称")

class LocalInventoryBatchgetproductinfoGlobalTags(LingXingModel):
    """global_tags sub-structure."""
    global_tag_id: Optional[str] = Field(None, description="标签id")
    tag_name: Optional[str] = Field(None, description="标签名称")
    color: Optional[str] = Field(None, description="标签颜色")

class LocalInventoryBatchgetproductinfoCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class LocalInventoryBatchgetproductinfoQcStandard(LingXingModel):
    """qc_standard sub-structure."""
    custom_qc_template: Optional[dict] = Field(None, description="自定义质检标准")

class LocalInventoryBatchgetproductinfoSupplierQuote(LingXingModel):
    """supplier_quote sub-structure."""
    psq_id: Optional[str] = Field(None, description="供应商报价id")
    product_id: Optional[int] = Field(None, description="产品id")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    is_primary: Optional[int] = Field(None, description="是否为首选供应商：0否，1是")
    quote_remark: Optional[str] = Field(None, description="报价备注")
    supplier_product_url: Optional[list] = Field(None, description="采购链接")
    quotes: Optional[list] = Field(None, description="报价数据")

class LocalInventoryBatchgetproductinfoComboProductList(LingXingModel):
    """combo_product_list sub-structure."""
    product_id: Optional[int] = Field(None, description="本地产品id")
    quantity: Optional[int] = Field(None, description="数量")
    sku: Optional[str] = Field(None, description="SKU")

class LocalInventoryBatchgetproductinfoProductLogisticsRelation(LingXingModel):
    """product_logistics_relation sub-structure."""
    xx_cg_transport_costs: Optional[float] = Field(None, description="默认头程成本(含税)")
    xx_currency: Optional[str] = Field(None, description="官方汇率code")
    xx_clearance_price: Optional[float] = Field(None, description="清关价格")
    xx_clearance_price_currency: Optional[str] = Field(None, description="清关价格币种")
    xx_bg_import_hs_code: Optional[str] = Field(None, description="报关：HSCode（进口国）")
    xx_bg_tax_rate: Optional[float] = Field(None, description="报关：税率")

class LocalInventoryBatchgetproductinfoDeclaration(LingXingModel):
    """declaration sub-structure."""
    customs_declaration_unit: Optional[str] = Field(None, description="报关单位")
    customs_declaration_spec: Optional[str] = Field(None, description="规格型号")
    customs_declaration_origin_produce: Optional[str] = Field(None, description="报关：原厂国（地区）")
    customs_declaration_inlands_source: Optional[str] = Field(None, description="报关：境内货源地")
    other_declare_element: Optional[str] = Field(None, description="报关：其他申报要素")
    customs_declaration_exempt: Optional[str] = Field(None, description="报关：征免")

class LocalInventoryBatchgetproductinfoClearance(LingXingModel):
    """clearance sub-structure."""
    customs_clearance_material: Optional[str] = Field(None, description="清关：材质")
    customs_clearance_usage: Optional[str] = Field(None, description="清关：用途")
    customs_clearance_internal_code: Optional[str] = Field(None, description="清关：内部编码")
    customs_clearance_preferential: Optional[int] = Field(None, description="清关：出口享惠情况： 1 不享惠 2 享惠 3 不确定享惠情况")
    customs_clearance_brand_type: Optional[int] = Field(None, description="清关：品牌类型： 1 无品牌 2 境内自主品牌 3 境内收购品牌 4 境外品牌（贴牌生产） 5 境外品牌（其他）")
    customs_clearance_product_pattern: Optional[str] = Field(None, description="清关：产品型号")
    customs_clearance_pic_url: Optional[str] = Field(None, description="清关：清关图片")
    allocation_remark: Optional[str] = Field(None, description="清关：配货备注")
    weaving_mode: Optional[int] = Field(None, description="织造方式：1 针织，2 梭织")
    customs_clearance_price: Optional[float] = Field(None, description="默认清关单价")
    customs_clearance_price_currency: Optional[str] = Field(None, description="默认清关单价币种")
    customs_clearance_hs_code: Optional[str] = Field(None, description="默认清关HSCODE")
    customs_clearance_tax_rate: Optional[str] = Field(None, description="默认清关税率")
    customs_clearance_remark: Optional[str] = Field(None, description="默认清关备注")

class LocalInventoryBatchgetproductinfoResponse(LingXingModel):
    """批量查询本地产品详情."""
    id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="产品名称")
    sku: Optional[str] = Field(None, description="产品sku")
    pic_url: Optional[str] = Field(None, description="上传的图片地址")
    picture_list: Optional[List[LocalInventoryBatchgetproductinfoPictureList]] = Field(None, description="产品图片数组")
    model: Optional[str] = Field(None, description="产品型号")
    unit: Optional[str] = Field(None, description="商品单位：套、个、台")
    status: Optional[int] = Field(None, description="状态：0 停售，1 在售，2 开发中，3 清仓")
    cid: Optional[int] = Field(None, description="分类id")
    bid: Optional[int] = Field(None, description="品牌id")
    product_developer: Optional[str] = Field(None, description="开发者")
    product_developer_uid: Optional[int] = Field(None, description="开发人")
    permission_user_info: Optional[List[LocalInventoryBatchgetproductinfoPermissionUserInfo]] = Field(None, description="负责人信息")
    global_tags: Optional[List[LocalInventoryBatchgetproductinfoGlobalTags]] = Field(None, description="产品标签信息")
    description: Optional[str] = Field(None, description="产品描述")
    is_combo: Optional[int] = Field(None, description="是否组合产品：0否，1是")
    brand_name: Optional[str] = Field(None, description="品牌名称")
    category_name: Optional[str] = Field(None, description="分类名称")
    attachment_id: Optional[list] = Field(None, description="附件id")
    special_attr: Optional[list] = Field(None, description="产品特殊属性： 1 含电 2 纯电 3 液体 4 粉末 5 膏体 6 带磁")
    currency: Optional[str] = Field(None, description="中国官方汇率code")
    cg_opt_username: Optional[str] = Field(None, description="采购：采购员")
    cg_delivery: Optional[int] = Field(None, description="采购：交期")
    cg_price: Optional[float] = Field(None, description="采购：采购成本（人民币）")
    purchase_remark: Optional[str] = Field(None, description="采购备注")
    cg_product_material: Optional[str] = Field(None, description="采购：材质")
    cg_product_length: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_product_width: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_product_height: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_package_length: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_package_width: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_package_height: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_box_length: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_box_width: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_box_height: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_product_net_weight: Optional[float] = Field(None, description="采购：产品净重（G）")
    cg_product_gross_weight: Optional[float] = Field(None, description="采购：产品毛重（G）")
    cg_box_weight: Optional[float] = Field(None, description="采购：外箱实重（KG）")
    custom_fields: Optional[List[LocalInventoryBatchgetproductinfoCustomFields]] = Field(None, description="自定义字段")
    cg_box_pcs: Optional[int] = Field(None, description="采购：单箱数量（包装数量）")
    bg_customs_export_name: Optional[str] = Field(None, description="报关：申报品名（中文）【中文报关名】")
    bg_customs_import_name: Optional[str] = Field(None, description="报关：申报品名（英文）【英文报关名】")
    bg_customs_import_price: Optional[float] = Field(None, description="报关：申报金额（进口国）【申报单价】")
    bg_export_hs_code: Optional[str] = Field(None, description="报关：HSCode（出口国）【中国HSCode】")
    bg_import_hs_code: Optional[str] = Field(None, description="报关：HSCode（进口国）【美国HSCode】")
    bg_tax_rate: Optional[float] = Field(None, description="【已废弃字段】报关：税率【美国税率】")
    qc_standard: Optional[List[LocalInventoryBatchgetproductinfoQcStandard]] = Field(None, description="质检标准")
    supplier_quote: Optional[List[LocalInventoryBatchgetproductinfoSupplierQuote]] = Field(None, description="供应商报价数据")
    combo_product_list: Optional[List[LocalInventoryBatchgetproductinfoComboProductList]] = Field(None, description="组合商品列表")
    product_logistics_relation: Optional[List[LocalInventoryBatchgetproductinfoProductLogisticsRelation]] = Field(None, description="物料关联【XX为国家简码，比如美国 US】")
    declaration: Optional[List[LocalInventoryBatchgetproductinfoDeclaration]] = Field(None, description="报关数据")
    clearance: Optional[List[LocalInventoryBatchgetproductinfoClearance]] = Field(None, description="清关数据")


class LocalInventoryBundledproductlistBundledProducts(LingXingModel):
    """bundled_products sub-structure."""
    product_id: Optional[int] = Field(None, description="子产品ID")
    sku: Optional[str] = Field(None, description="子产品SKU")
    bundled_qty: Optional[int] = Field(None, description="捆绑数量")
    cost_ratio: Optional[int] = Field(None, description="费用比例")

class LocalInventoryBundledproductlistResponse(LingXingModel):
    """查询捆绑产品关系列表."""
    id: Optional[int] = Field(None, description="捆绑产品ID")
    sku: Optional[str] = Field(None, description="捆绑产品SKU")
    product_name: Optional[str] = Field(None, description="捆绑产品名")
    cg_price: Optional[float] = Field(None, description="捆绑产品采购成本")
    status_text: Optional[str] = Field(None, description="产品状态：停售、在售、开发中、清仓")
    bundled_products: Optional[List[LocalInventoryBundledproductlistBundledProducts]] = Field(None, description="捆绑产品关系")


class LocalInventoryCategoryResponse(LingXingModel):
    """查询产品分类列表."""
    cid: Optional[int] = Field(None, description="分类ID")
    parent_cid: Optional[int] = Field(None, description="父级分类ID")
    title: Optional[str] = Field(None, description="分类名称")
    category_code: Optional[str] = Field(None, description="分类简码")


class LocalInventoryProductauxlistPurchaseSupplierQuote(LingXingModel):
    """purchase_supplier_quote sub-structure."""
    product_id: Optional[int] = Field(None, description="产品ID")
    cg_price: Optional[float] = Field(None, description="采购：采购成本（人民币）")
    has_cg_permission: Optional[int] = Field(None, description="是否有采购成本权限：0-无，1-有")
    suppliers: Optional[Any] = Field(None, description="是")

class LocalInventoryProductauxlistAuxRelationProduct(LingXingModel):
    """aux_relation_product sub-structure."""
    pid: Optional[int] = Field(None, description="产品id")
    product_name: Optional[str] = Field(None, description="产品名称")
    sku: Optional[str] = Field(None, description="sku")
    quantity: Optional[int] = Field(None, description="关联辅料的数量")

class LocalInventoryProductauxlistResponse(LingXingModel):
    """查询产品辅料列表."""
    id: Optional[int] = Field(None, description="辅料id")
    sku: Optional[str] = Field(None, description="SKU")
    product_name: Optional[str] = Field(None, description="品名")
    cg_price: Optional[float] = Field(None, description="采购成本（人民币）")
    cg_product_length: Optional[float] = Field(None, description="单品规格长（CM）")
    cg_product_width: Optional[float] = Field(None, description="单品规格宽（CM）")
    cg_product_height: Optional[float] = Field(None, description="单品规格高（CM）")
    cg_product_net_weight: Optional[float] = Field(None, description="单品净重（G）")
    purchase_supplier_quote: Optional[List[LocalInventoryProductauxlistPurchaseSupplierQuote]] = Field(None, description="供应商报价信息")
    aux_relation_product: Optional[List[LocalInventoryProductauxlistAuxRelationProduct]] = Field(None, description="关联产品")


class LocalInventoryProductinfoPictureList(LingXingModel):
    """picture_list sub-structure."""
    pic_url: Optional[str] = Field(None, description="图片链接")
    is_primary: Optional[int] = Field(None, description="是否产品主图：0-否 1-是")

class LocalInventoryProductinfoPermissionUserInfo(LingXingModel):
    """permission_user_info sub-structure."""
    permission_uid: Optional[int] = Field(None, description="负责人id")
    permission_user_name: Optional[str] = Field(None, description="负责人名称")

class LocalInventoryProductinfoGlobalTags(LingXingModel):
    """global_tags sub-structure."""
    global_tag_id: Optional[str] = Field(None, description="标签id")
    tag_name: Optional[str] = Field(None, description="标签名称")
    color: Optional[str] = Field(None, description="标签颜色")

class LocalInventoryProductinfoCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class LocalInventoryProductinfoQcStandard(LingXingModel):
    """qc_standard sub-structure."""
    custom_qc_template: Optional[dict] = Field(None, description="自定义质检标准")

class LocalInventoryProductinfoSupplierQuote(LingXingModel):
    """supplier_quote sub-structure."""
    psq_id: Optional[str] = Field(None, description="供应商报价id")
    product_id: Optional[int] = Field(None, description="产品id")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    is_primary: Optional[int] = Field(None, description="是否为首选供应商：0 否，1 是")
    quote_remark: Optional[str] = Field(None, description="报价备注")
    supplier_product_url: Optional[list] = Field(None, description="采购链接")
    quote_cg_delivery: Optional[int] = Field(None, description="交期")
    quotes: Optional[list] = Field(None, description="报价数据")

class LocalInventoryProductinfoComboProductList(LingXingModel):
    """combo_product_list sub-structure."""
    product_id: Optional[int] = Field(None, description="本地产品id")
    quantity: Optional[int] = Field(None, description="数量")
    sku: Optional[str] = Field(None, description="SKU")

class LocalInventoryProductinfoProductLogisticsRelation(LingXingModel):
    """product_logistics_relation sub-structure."""
    xx_cg_transport_costs: Optional[float] = Field(None, description="默认头程成本(含税)")
    xx_currency: Optional[str] = Field(None, description="官方汇率code")
    xx_clearance_price: Optional[float] = Field(None, description="清关价格")
    xx_clearance_price_currency: Optional[str] = Field(None, description="清关价格币种")
    xx_bg_import_hs_code: Optional[str] = Field(None, description="报关：HSCode（进口国）")
    xx_bg_tax_rate: Optional[float] = Field(None, description="报关：税率")

class LocalInventoryProductinfoDeclaration(LingXingModel):
    """declaration sub-structure."""
    customs_declaration_unit: Optional[str] = Field(None, description="报关单位")
    customs_declaration_spec: Optional[str] = Field(None, description="规格型号")
    customs_declaration_origin_produce: Optional[str] = Field(None, description="报关：原厂国（地区）")
    customs_declaration_inlands_source: Optional[str] = Field(None, description="报关：境内货源地")
    other_declare_element: Optional[str] = Field(None, description="报关：其他申报要素")
    customs_declaration_exempt: Optional[str] = Field(None, description="报关：征免")
    customs_import_price: Optional[str] = Field(None, description="报关单价")
    customs_import_price_currency: Optional[str] = Field(None, description="报关单价单位")

class LocalInventoryProductinfoClearance(LingXingModel):
    """clearance sub-structure."""
    customs_clearance_material: Optional[str] = Field(None, description="清关：材质")
    customs_clearance_usage: Optional[str] = Field(None, description="清关：用途")
    customs_clearance_internal_code: Optional[str] = Field(None, description="清关：内部编码")
    customs_clearance_preferential: Optional[int] = Field(None, description="清关：出口享惠情况： 1 不享惠 2 享惠 3 不确定享惠情况")
    customs_clearance_brand_type: Optional[int] = Field(None, description="清关：品牌类型： 1 无品牌 2 境内自主品牌 3 境内收购品牌 4 境外品牌（贴牌生产） 5 境外品牌（其他）")
    customs_clearance_product_pattern: Optional[str] = Field(None, description="清关：产品型号")
    customs_clearance_pic_url: Optional[str] = Field(None, description="清关：清关图片")
    allocation_remark: Optional[str] = Field(None, description="清关：配货备注")
    weaving_mode: Optional[int] = Field(None, description="织造方式：1 针织，2 梭织")
    customs_clearance_price: Optional[str] = Field(None, description="默认清关单价")
    customs_clearance_price_currency: Optional[str] = Field(None, description="默认清关单价币种")
    customs_clearance_hs_code: Optional[str] = Field(None, description="默认清关HSCODE")
    customs_clearance_tax_rate: Optional[str] = Field(None, description="默认清关税率")
    customs_clearance_remark: Optional[str] = Field(None, description="默认清关备注")

class LocalInventoryProductinfoAuxRelationList(LingXingModel):
    """aux_relation_list sub-structure."""
    aux_sku: Optional[str] = Field(None, description="辅料sku")
    aux_name: Optional[str] = Field(None, description="辅料名称")
    sku_qty: Optional[str] = Field(None, description="辅料比例（主料）")
    aux_qty: Optional[str] = Field(None, description="辅料比例（辅料）")

class LocalInventoryProductinfoResponse(LingXingModel):
    """查询本地产品详情."""
    id: Optional[int] = Field(None, description="本地产品id")
    product_name: Optional[str] = Field(None, description="产品名称")
    sku: Optional[str] = Field(None, description="产品sku")
    sku_identifier: Optional[str] = Field(None, description="SKU识别码")
    pic_url: Optional[str] = Field(None, description="上传的图片地址")
    picture_list: Optional[List[LocalInventoryProductinfoPictureList]] = Field(None, description="产品图片数组")
    model: Optional[str] = Field(None, description="产品型号")
    unit: Optional[str] = Field(None, description="商品单位：套、个、台")
    status: Optional[int] = Field(None, description="状态：0 停售，1 在售，2 开发中，3 清仓")
    cid: Optional[int] = Field(None, description="分类id")
    bid: Optional[int] = Field(None, description="品牌id")
    product_developer: Optional[str] = Field(None, description="开发者")
    product_developer_uid: Optional[int] = Field(None, description="开发人")
    permission_user_info: Optional[List[LocalInventoryProductinfoPermissionUserInfo]] = Field(None, description="负责人数组")
    global_tags: Optional[List[LocalInventoryProductinfoGlobalTags]] = Field(None, description="产品标签信息")
    description: Optional[str] = Field(None, description="产品描述")
    is_combo: Optional[int] = Field(None, description="是否为组合产品：0 否，1 是")
    brand_name: Optional[str] = Field(None, description="品牌名称")
    category_name: Optional[str] = Field(None, description="分类名称")
    attachment_id: Optional[list] = Field(None, description="附件id")
    special_attr: Optional[list] = Field(None, description="产品特殊属性： 1 含电 2 纯电 3 液体 4 粉末 5 膏体 6 带磁")
    currency: Optional[str] = Field(None, description="中国官方汇率code")
    cg_opt_username: Optional[str] = Field(None, description="采购：采购员")
    cg_delivery: Optional[int] = Field(None, description="采购：交期")
    cg_price: Optional[float] = Field(None, description="采购：采购成本（人民币）")
    purchase_remark: Optional[str] = Field(None, description="采购备注")
    cg_product_material: Optional[str] = Field(None, description="采购：材质")
    cg_product_length: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_product_width: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_product_height: Optional[float] = Field(None, description="采购：产品规格（CM）")
    cg_package_length: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_package_width: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_package_height: Optional[float] = Field(None, description="采购：包装规格（CM）")
    cg_box_length: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_box_width: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_box_height: Optional[float] = Field(None, description="采购：外箱规格（CM）")
    cg_product_net_weight: Optional[float] = Field(None, description="采购：产品净重（G）")
    cg_product_gross_weight: Optional[float] = Field(None, description="采购：产品毛重（G）")
    cg_box_weight: Optional[float] = Field(None, description="采购：外箱实重（KG）")
    custom_fields: Optional[List[LocalInventoryProductinfoCustomFields]] = Field(None, description="自定义字段")
    cg_box_pcs: Optional[int] = Field(None, description="采购：单箱数量（包装数量）")
    bg_customs_export_name: Optional[str] = Field(None, description="报关：申报品名（中文）【中文报关名】")
    bg_customs_import_name: Optional[str] = Field(None, description="报关：申报品名（英文）【英文报关名】")
    bg_customs_import_price: Optional[float] = Field(None, description="报关：申报金额（进口国）【申报单价】")
    bg_export_hs_code: Optional[str] = Field(None, description="报关：HS Code（出口国）【中国HS Code】")
    bg_import_hs_code: Optional[str] = Field(None, description="报关：HS Code（进口国）【美国HS Code】")
    bg_tax_rate: Optional[float] = Field(None, description="【已废弃字段】报关：税率【美国税率】")
    qc_standard: Optional[List[LocalInventoryProductinfoQcStandard]] = Field(None, description="质检标准")
    supplier_quote: Optional[List[LocalInventoryProductinfoSupplierQuote]] = Field(None, description="供应商报价数据")
    combo_product_list: Optional[List[LocalInventoryProductinfoComboProductList]] = Field(None, description="组合产品列表")
    product_logistics_relation: Optional[List[LocalInventoryProductinfoProductLogisticsRelation]] = Field(None, description="物流关联【XX为国家简码，比如美国 US】")
    declaration: Optional[List[LocalInventoryProductinfoDeclaration]] = Field(None, description="报关数据")
    clearance: Optional[List[LocalInventoryProductinfoClearance]] = Field(None, description="清关数据")
    aux_relation_list: Optional[List[LocalInventoryProductinfoAuxRelationList]] = Field(None, description="辅料列表")
    category_full_name: Optional[str] = Field(None, description="完整分类层级名称")


class LocalInventoryProductlistGlobalTags(LingXingModel):
    """global_tags sub-structure."""
    global_tag_id: Optional[str] = Field(None, description="标签id")
    tag_name: Optional[str] = Field(None, description="标签名称")
    color: Optional[str] = Field(None, description="标签颜色")

class LocalInventoryProductlistSupplierQuote(LingXingModel):
    """supplier_quote sub-structure."""
    psq_id: Optional[str] = Field(None, description="供应商报价id")
    product_id: Optional[int] = Field(None, description="产品id")
    supplier_id: Optional[int] = Field(None, description="供应商id")
    is_primary: Optional[int] = Field(None, description="是否为首选供应商：0 否，1 是")
    supplier_product_url: Optional[list] = Field(None, description="采购链接")
    quote_remark: Optional[str] = Field(None, description="供应商报价备注")
    cg_price: Optional[str] = Field(None, description="采购成本")
    cg_currency_icon: Optional[str] = Field(None, description="采购成本币种符号")
    supplier_code: Optional[str] = Field(None, description="供应商代码")
    level_text: Optional[str] = Field(None, description="级别")
    employees_text: Optional[str] = Field(None, description="规模")
    remark: Optional[str] = Field(None, description="供应商备注")
    supplier_name: Optional[str] = Field(None, description="供应商名称")
    quotes: Optional[list] = Field(None, description="报价数据")

class LocalInventoryProductlistCustomFields(LingXingModel):
    """custom_fields sub-structure."""
    id: Optional[str] = Field(None, description="字段ID")
    name: Optional[str] = Field(None, description="字段名")
    val_text: Optional[str] = Field(None, description="字段值")

class LocalInventoryProductlistAttribute(LingXingModel):
    """attribute sub-structure."""
    attr_id: Optional[str] = Field(None, description="属性ID")
    attr_name: Optional[str] = Field(None, description="属性名称")
    attr_value: Optional[str] = Field(None, description="属性值")

class LocalInventoryProductlistResponse(LingXingModel):
    """查询本地产品列表."""
    total: Optional[int] = Field(None, description="总数")
    id: Optional[int] = Field(None, description="本地产品id")
    cid: Optional[int] = Field(None, description="类别id")
    category_name: Optional[str] = Field(None, description="类别")
    bid: Optional[int] = Field(None, description="品牌id")
    brand_name: Optional[str] = Field(None, description="品牌")
    sku: Optional[str] = Field(None, description="本地产品SKU")
    open_status: Optional[int] = Field(None, description="产品开启状态： 0-停用 ，1-启用")
    sku_identifier: Optional[str] = Field(None, description="SKU识别码")
    product_name: Optional[str] = Field(None, description="品名")
    pic_url: Optional[str] = Field(None, description="图片链接")
    ps_id: Optional[int] = Field(None, description="SPU唯一id")
    spu: Optional[str] = Field(None, description="SPU")
    cg_delivery: Optional[int] = Field(None, description="采购：交期")
    cg_transport_costs: Optional[float] = Field(None, description="采购：运输成本")
    purchase_remark: Optional[str] = Field(None, description="采购备注")
    cg_price: Optional[float] = Field(None, description="采购：采购成本（人民币）")

    status: Optional[int] = Field(None, description="状态：0 停售，1 在售，2 开发中，3 清仓")
    status_text: Optional[str] = Field(None, description="状态文本")
    is_combo: Optional[int] = Field(None, description="是否为组合产品：0 否，1 是")
    create_time: Optional[int] = Field(None, description="创建时间")
    update_time: Optional[int] = Field(None, description="更新时间")
    global_tags: Optional[List[LocalInventoryProductlistGlobalTags]] = Field(None, description="产品标签信息")
    product_developer_uid: Optional[str] = Field(None, description="开发人员id")
    product_developer: Optional[str] = Field(None, description="开发人员名称")
    cg_opt_uid: Optional[str] = Field(None, description="采购：采购员id")
    cg_opt_username: Optional[str] = Field(None, description="采购：采购员名称")
    supplier_quote: Optional[List[LocalInventoryProductlistSupplierQuote]] = Field(None, description="供应商报价信息")
    custom_fields: Optional[List[LocalInventoryProductlistCustomFields]] = Field(None, description="自定义字段")
    attribute: Optional[List[LocalInventoryProductlistAttribute]] = Field(None, description="产品属性")


class StorageAttributeAttributelistList(LingXingModel):
    """list sub-structure."""
    pa_id: Optional[int] = Field(None, description="属性id")
    attr_name: Optional[str] = Field(None, description="属性名称")
    create_time: Optional[str] = Field(None, description="属性创建时间")
    item_list: Optional[list] = Field(None, description="属性值列表")

class StorageAttributeAttributelistResponse(LingXingModel):
    """查询产品属性列表."""
    total: Optional[int] = Field(None, description="总数")
    list: Optional[List[StorageAttributeAttributelistList]] = Field(None, description="数据列表")


class StorageAttributeSetResponse(LingXingModel):
    """添加 / 编辑产品属性."""
    pa_id: Optional[int] = Field(None, description="属性名")
    pai_id: Optional[int] = Field(None, description="属性值")


class StorageCategorySetResponse(LingXingModel):
    """添加 / 编辑产品分类."""
    id: Optional[str] = Field(None, description="分类id")
    title: Optional[str] = Field(None, description="分类名称")


class StorageProductSetResponse(LingXingModel):
    """添加/编辑本地产品."""
    product_id: Optional[int] = Field(None, description="本地产品id")
    sku: Optional[str] = Field(None, description="本地产品sku")
    sku_identifier: Optional[str] = Field(None, description="SKU识别码")


class StorageProductSetauxResponse(LingXingModel):
    """添加 / 编辑辅料."""
    product_id: Optional[int] = Field(None, description="辅料产品id")


class StorageProductSetbundledResponse(LingXingModel):
    """添加 / 编辑捆绑产品."""
    product_id: Optional[int] = Field(None, description="本地产品id")


class StorageProductUploadpicturesPictureList(LingXingModel):
    """picture_list sub-structure."""
    pic_url: Optional[str] = Field(None, description="已上传到领星的图片链接")
    customer_url: Optional[str] = Field(None, description="客户提交的的图片链接")

class StorageProductUploadpicturesResponse(LingXingModel):
    """上传本地产品图片."""
    sku: Optional[str] = Field(None, description="本地产品SKU")
    picture_list: Optional[List[StorageProductUploadpicturesPictureList]] = Field(None, description="产品图片信息")


class StorageSpuInfoAttachmentfiles(LingXingModel):
    """attachmentFiles sub-structure."""
    file_id: Optional[str] = Field(None, description="附件id")
    file_name: Optional[str] = Field(None, description="附件名称")
    file_url: Optional[str] = Field(None, description="附件url")

class StorageSpuInfoPurchaseInfo(LingXingModel):
    """purchase_info sub-structure."""
    cg_uid: Optional[int] = Field(None, description="采购：采购员id")
    purchase_remark: Optional[str] = Field(None, description="采购：采购备注")
    cg_delivery: Optional[int] = Field(None, description="采购：采购交期（天）")
    cg_product_length: Optional[float] = Field(None, description="采购：单品规格-长（CM）")
    cg_product_width: Optional[float] = Field(None, description="采购：单品规格-宽（CM）")
    cg_product_height: Optional[float] = Field(None, description="采购：单品规格-高（CM）")
    cg_product_net_weight: Optional[float] = Field(None, description="采购：单品净重（g）")
    cg_product_gross_weight: Optional[float] = Field(None, description="采购：单品毛重（g）")
    cg_package_length: Optional[float] = Field(None, description="采购：包装规格-长（CM）")
    cg_package_width: Optional[float] = Field(None, description="采购：包装规格-宽（CM）")
    cg_package_height: Optional[float] = Field(None, description="采购：包装规格-高（CM）")
    cg_box_length: Optional[float] = Field(None, description="采购：外箱规格-长（CM）")
    cg_box_width: Optional[float] = Field(None, description="采购：外箱规格-宽（CM）")
    cg_box_height: Optional[float] = Field(None, description="采购：外箱规格-高（CM）")
    cg_product_box_weight: Optional[float] = Field(None, description="采购：单箱重量（KG）")
    cg_box_pcs: Optional[int] = Field(None, description="采购：单箱数量（包装数量）")
    cg_product_material: Optional[str] = Field(None, description="采购：产品材质")

class StorageSpuInfoAuxRelationList(LingXingModel):
    """aux_relation_list sub-structure."""
    aux_id: Optional[int] = Field(None, description="辅料id")
    aux_name: Optional[str] = Field(None, description="辅料品名")
    aux_sku: Optional[str] = Field(None, description="辅料SKU")
    cg_price: Optional[str] = Field(None, description="单位成本")
    quantity: Optional[int] = Field(None, description="数量")
    remark: Optional[str] = Field(None, description="备注")
    sku_qty: Optional[str] = Field(None, description="辅料比例（主料）")
    aux_qty: Optional[str] = Field(None, description="辅料比例（辅料）")

class StorageSpuInfoLogistics(LingXingModel):
    """logistics sub-structure."""
    declaration: Optional[dict] = Field(None, description="报关数据")
    clearance: Optional[dict] = Field(None, description="清关数据")
    base: Optional[dict] = Field(None, description="物流基础信息")
    fee: Optional[dict] = Field(None, description="头程费用，支持国家：US、CA、MX、JP、UK、DE、FR、ES、IT、NL、AU、SG、IN、AE、SA、BR、SE、PL、BE、TR、UA、HU、PK、LB、AT、CH、CZ、DK、IE、LU、NO、PT、SK、RU、KZ、BY、CL、KR")

class StorageSpuInfoSkuList(LingXingModel):
    """sku_list sub-structure."""
    sku: Optional[str] = Field(None, description="产品SKU")
    product_name: Optional[str] = Field(None, description="产品名称")
    attribute: Optional[list] = Field(None, description="属性列表")
    picture_list: Optional[list] = Field(None, description="产品图片链接")

class StorageSpuInfoAttributeSkcList(LingXingModel):
    """attribute_skc_list sub-structure."""
    pa_id: Optional[int] = Field(None, description="属性id")
    skc: Optional[str] = Field(None, description="skc编码（全局唯一）")
    can_edit: Optional[bool] = Field(None, description="是否允许编辑：true 允许编辑，false 不允许编辑")

class StorageSpuInfoResponse(LingXingModel):
    """查询多属性产品详情."""
    total: Optional[int] = Field(None, description="总数")
    ps_id: Optional[int] = Field(None, description="spu 唯一id")
    spu: Optional[str] = Field(None, description="SPU（添加时必填）")
    spu_name: Optional[str] = Field(None, description="款名（添加时必填）")
    model: Optional[str] = Field(None, description="型号")
    unit: Optional[str] = Field(None, description="单位")
    status: Optional[int] = Field(None, description="状态：0 停售，1 在售，2 开发中，3 清仓")
    cid: Optional[int] = Field(None, description="分类id")
    category_name: Optional[str] = Field(None, description="分类名")
    bid: Optional[int] = Field(None, description="品牌id")
    brand_name: Optional[str] = Field(None, description="品牌名")
    developer_uid: Optional[int] = Field(None, description="开发人id")
    product_duty_uids: Optional[list] = Field(None, description="产品负责人id")
    description: Optional[str] = Field(None, description="产品描述")
    attachment_files: Optional[List[StorageSpuInfoAttachmentfiles]] = Field(None, description="附件信息")
    purchase_info: Optional[List[StorageSpuInfoPurchaseInfo]] = Field(None, description="采购信息")
    aux_relation_list: Optional[List[StorageSpuInfoAuxRelationList]] = Field(None, description="关联辅料")
    logistics: Optional[List[StorageSpuInfoLogistics]] = Field(None, description="物流报关清关")
    sku_list: Optional[List[StorageSpuInfoSkuList]] = Field(None, description="产品列表")
    attribute_skc_list: Optional[List[StorageSpuInfoAttributeSkcList]] = Field(None, description="属性skc列表")


class StorageSpuSetSkuList(LingXingModel):
    """sku_list sub-structure."""
    product_id: Optional[int] = Field(None, description="本地产品id")
    sku: Optional[str] = Field(None, description="本地产品sku")

class StorageSpuSetResponse(LingXingModel):
    """添加/编辑多属性产品."""
    total: Optional[int] = Field(None, description="总数")
    ps_id: Optional[int] = Field(None, description="spu唯一id")
    sku_list: Optional[List[StorageSpuSetSkuList]] = Field(None, description="spu下对应的sku数据")


class StorageSpuSpulistResponse(LingXingModel):
    """查询多属性产品列表."""
    total: Optional[int] = Field(None, description="总数")
    ps_id: Optional[int] = Field(None, description="SPU 唯一id")
    spu: Optional[str] = Field(None, description="SPU")
    spu_name: Optional[str] = Field(None, description="款名")
    model: Optional[str] = Field(None, description="型号")
    cid: Optional[int] = Field(None, description="分类id")
    bid: Optional[int] = Field(None, description="品牌id")
    developer_uid: Optional[int] = Field(None, description="开发人id")
    cg_uid: Optional[int] = Field(None, description="采购员id")
    purchase_remark: Optional[str] = Field(None, description="采购备注")
    cg_price: Optional[str] = Field(None, description="采购成本")
    cg_delivery: Optional[int] = Field(None, description="交期")
    create_uid: Optional[str] = Field(None, description="创建人id")
    create_time: Optional[str] = Field(None, description="创建时间")
    status: Optional[int] = Field(None, description="状态： 0 停售， 1 在售， 2 开发中， 3 清仓")


class StorageBrandSetResponse(LingXingModel):
    """添加/编辑产品品牌."""
    id: Optional[str] = Field(None, description="品牌id")
    title: Optional[str] = Field(None, description="品牌名称")
    brand_code: Optional[str] = Field(None, description="品牌简码")


class LabelProductListList(LingXingModel):
    """list sub-structure."""
    label_id: Optional[str] = Field(None, description="标签id")
    label_name: Optional[str] = Field(None, description="标签名称")
    gmt_created: Optional[int] = Field(None, description="创建时间")

class PublishUpcUpclistList(LingXingModel):
    """list sub-structure."""
    id: Optional[int] = Field(None, description="记录唯一id")
    commodity_code: Optional[str] = Field(None, description="商品编码")
    code_type: Optional[str] = Field(None, description="商品编码类型")
    is_used: Optional[int] = Field(None, description="商品编码使用状态：0 否 ，1 是")
    created_user_id: Optional[int] = Field(None, description="创建人uid")
    use_user_id: Optional[int] = Field(None, description="使用人uid")
    use_time: Optional[str] = Field(None, description="商品编码被使用的时间")
    remark: Optional[str] = Field(None, description="备注")
    gmt_create: Optional[str] = Field(None, description="商品编码创建时间")
    is_used_desc: Optional[str] = Field(None, description="商品编码使用状态说明")

class PublishUpcUpclistResponse(LingXingModel):
    """获取UPC编码列表."""
    total: Optional[int] = Field(None, description="商品编码总数")
    list: Optional[List[PublishUpcUpclistList]] = Field(None, description="商品编码数据列表")


class PublishUpcAddcommoditycodeResponse(LingXingModel):
    """创建UPC编码."""


class ProductOperateBatchResponse(LingXingModel):
    """产品启用、禁用."""


# Migrated from old models/
class AttributeListItem(LingXingModel):
    """Response item for attributeList."""

    list: Optional[list] = None
    total: Optional[int] = None


class BrandItem(LingXingModel):
    """Response item for Brand."""

    bid: Optional[int] = None
    brand_code: Optional[str] = None
    title: Optional[str] = None


class CategoryItem(LingXingModel):
    """Response item for Category."""

    category_code: Optional[str] = None
    cid: Optional[int] = None
    parent_cid: Optional[int] = None
    title: Optional[str] = None


class ProductListsItem(LingXingModel):
    """Response item for ProductLists."""

    attribute: Optional[list] = None
    aux_relation_list: Optional[list] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    category_name: Optional[str] = None
    cg_delivery: Optional[int] = None
    cg_opt_uid: Optional[int] = None
    cg_opt_username: Optional[str] = None
    cg_price: Optional[float] = None
    cg_transport_costs: Optional[float] = None
    cid: Optional[int] = None
    create_time: Optional[int] = None
    custom_fields: Optional[list] = None
    global_tags: Optional[list] = None
    id: Optional[int] = None
    is_combo: Optional[int] = None
    open_status: Optional[int] = None
    pic_url: Optional[str] = None
    product_developer: Optional[str] = None
    product_developer_uid: Optional[int] = None
    product_name: Optional[str] = None
    ps_id: Optional[int] = None
    purchase_remark: Optional[str] = None
    sku: Optional[str] = None
    sku_identifier: Optional[str] = None
    spu: Optional[str] = None
    status: Optional[int] = None
    status_text: Optional[str] = None
    supplier_quote: Optional[list] = None
    update_time: Optional[int] = None


class UpcListItem(LingXingModel):
    """Response item for UpcList."""

    list: Optional[list] = None
    total: Optional[int] = None

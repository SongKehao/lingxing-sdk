"""Request models for Product APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class ProductAddCommodityCodeRequest(LingXingModel):
    """Request for 创建UPC编码.

    POST /listing/publish/api/upc/addCommodityCode
    """

    commodity_codes: List  # 编码-最多支持两百个
    code_type: str  # 编码类型：支持UPC、EAN、ISBN


class ProductUpcListRequest(LingXingModel):
    """Request for 获取UPC编码列表.

    POST /listing/publish/api/upc/upcList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20


class ProductProductListsRequest(LingXingModel):
    """Request for 查询本地产品列表.

    POST /erp/sc/routing/data/local_inventory/productList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000
    update_time_start: Optional[int] = None  # 更新时间-开始时间【时间戳，单位：秒，左闭右开】
    update_time_end: Optional[int] = None  # 更新时间-结束时间【时间戳，单位：秒，左闭右开】
    create_time_start: Optional[int] = None  # 创建时间-开始时间【时间戳，单位：秒，左闭右开】
    create_time_end: Optional[int] = None  # 创建时间-结束时间【时间戳，单位：秒，左闭右开】
    sku_list: Optional[list] = None  # 本地产品sku
    sku_identifier_list: Optional[list] = None  # sku识别码列表


class ProductProductDetailsRequest(LingXingModel):
    """Request for 查询本地产品详情.

    POST /erp/sc/routing/data/local_inventory/productInfo
    """

    id: Optional[int] = None  # 产品id【产品id、 产品SKU 、SKU识别码 三选一必填】
    sku: Optional[str] = None  # 产品SKU【产品id、 产品SKU 、SKU识别码 三选一必填】
    sku_identifier: Optional[str] = None  # SKU识别码【产品id、 产品SKU 、SKU识别码 三选一必填】


class ProductBatchgetproductinfoRequest(LingXingModel):
    """Request for 批量查询本地产品详情.

    POST /erp/sc/routing/data/local_inventory/batchGetProductInfo
    """

    productIds: Optional[list] = None  # 产品id，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】
    skus: Optional[list] = None  # 产品SKU，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】
    sku_identifiers: Optional[list] = None  # SKU识别码，上限100个上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】


class ProductProductoperatebatchRequest(LingXingModel):
    """Request for 产品启用、禁用.

    POST /basicOpen/product/productManager/product/operate/batch
    """

    product_ids: Optional[list] = None  # 产品id
    batch_status: str  # 状态: Enable 启用 Disable 禁用


class ProductSetProductRequestPictureListItem(LingXingModel):
    pic_url: Optional[str] = None  # 产品图片链接
    is_primary: Optional[int] = None  # 是否产品主图：0 否，1 是


class ProductSetProductRequestGroupListItem(LingXingModel):
    sku: Optional[str] = None  # 子商品
    quantity: Optional[int] = None  # 商品比例数


class ProductSetProductRequestQcStandardItem(LingXingModel):
    custom_qc_template: Optional[dict] = None  # 自定义质检标准
    custom_qc_template__qc_image: Optional[list] = None  # 质检图片【最多十张图】
    custom_qc_template__qc_image__file_id: Optional[str] = None  # 质检图片文件id
    custom_qc_template__qc_image__customer_url: Optional[str] = None  # 客户的质检图片URL


class ProductSetProductRequestProductLogisticsListItem(LingXingModel):
    US_cg_transport_costs: Optional[str] = None  # 默认头程费用（含税）
    US_currency: Optional[str] = None  # 默认头程费用币种
    US_clearance_price: Optional[str] = None  # 清关价格
    US_clearance_price_currency: Optional[str] = None  # 清关价格币种，默认CNY
    US_bg_import_hs_code: Optional[str] = None  # HS Code
    US_bg_tax_rate: Optional[str] = None  # 税率


class ProductSetProductRequestSupplierQuoteItem(LingXingModel):
    erp_supplier_id: int  # 领星ERP供应商id，查询本地产品详情接口对应字段【supplier_id】，与supplier_id必填其一
    supplier_id: Optional[int] = (
        None  # 客户系统供应商id，没有填这个值或者对应供应商不存在，则取erp_supplier_id，与erp_supplier_id必填其一
    )
    supplier_product_url: Optional[list] = None  # 采购链接，字符串数组，最多20个，没有则传空数组
    quote_remark: Optional[str] = None  # 报价备注
    quote_cg_delivery: Optional[int] = None  # 供应商交期
    is_primary: int  # 首选供应商：0 否，1 是
    quotes: List  # 报价信息，传供应商报价时必传
    quotes__currency: str  # 报价币种，目前只有CNY和USD
    quotes__is_tax: int  # 是否含税：0 否，1 是
    quotes__tax_rate: str  # 税率，为空则表示为0
    quotes__step_prices: List  # 阶梯价信息
    quotes__step_prices__moq: int  # 最小起订量，最小值为1
    quotes__step_prices__price_with_tax: str  # 含税单价，4位小数


class ProductSetProductRequestDeclarationItem(LingXingModel):
    customs_import_price: Optional[int] = None  # 报关：报关单价
    customs_import_price_currency: Optional[str] = None  # 报关：报关单价币种
    customs_export_name: Optional[str] = None  # 报关：中文报关名
    customs_import_name: Optional[str] = None  # 报关：英文报关名
    customs_declaration_unit: Optional[str] = None  # 报关：报关单位
    customs_declaration_spec: Optional[str] = None  # 报关：规格型号
    customs_declaration_origin_produce: Optional[str] = None  # 报关：原厂国（地区）
    customs_declaration_inlands_source: Optional[str] = None  # 报关：境内货源地
    customs_declaration_hs_code: Optional[str] = None  # 报关：报关HSCODE
    other_declare_element: Optional[str] = None  # 报关：其他申报要素
    customs_declaration_exempt: Optional[str] = None  # 报关：征免


class ProductSetProductRequestClearanceItem(LingXingModel):
    customs_clearance_material: Optional[str] = None  # 清关：中文材质
    customs_clearance_en_material: Optional[str] = None  # 清关：英文材质
    customs_clearance_usage: Optional[str] = None  # 清关：中文用途
    customs_clearance_en_usage: Optional[str] = None  # 清关：英文用途
    customs_clearance_internal_code: Optional[str] = None  # 清关：内部编码
    customs_clearance_preferential: Optional[int] = None  # 清关：出口享惠情况：1 不享惠，2 享惠，3 不确定享惠情况
    customs_clearance_brand_type: Optional[int] = (
        None  # 清关：品牌类型：1 无品牌，2 境内自主品牌，3 境内收购品牌，4 境外品牌（贴牌生产），5 境外品牌（其他）
    )
    customs_clearance_product_pattern: Optional[str] = None  # 清关：产品型号
    allocation_remark: Optional[str] = None  # 清关：配货备注
    weaving_mode: Optional[int] = None  # 织造方式：1 针织，2 梭织
    customs_clearance_pic_url: Optional[str] = None  # 清关：清关图片


class ProductSetProductRequestAuxRelationListItem(LingXingModel):
    aux_sku: str  # 辅料sku
    sku_qty: Optional[int] = None  # 辅料比例（主料）
    aux_qty: Optional[int] = None  # 辅料比例（辅料）


class ProductSetProductRequestSpecPackListItem(LingXingModel):
    spec_title: str  # 采购：更多箱规-箱规名称
    cg_box_pcs: Optional[int] = None  # 采购：更多箱规-单箱数量
    cg_box_length: Optional[str] = None  # 采购：更多箱规-外箱规格-长（CM）
    cg_box_width: Optional[str] = None  # 采购：更多箱规-外箱规格-宽（CM）
    cg_box_height: Optional[str] = None  # 采购：更多箱规-外箱规格-高（CM）
    cg_package_length: Optional[str] = None  # 采购：更多箱规-包装规格-长（CM）
    cg_package_width: Optional[str] = None  # 采购：更多箱规-包装规格-宽（CM）
    cg_package_height: Optional[str] = None  # 采购：更多箱规-包装规格-高（CM）
    cg_box_weight: Optional[str] = None  # 采购：更多箱规-单箱重量（KG）
    cg_product_gross_weight: Optional[str] = None  # 采购：更多箱规-单品毛重（G）


class ProductSetProductRequestCustomFieldsItem(LingXingModel):
    id: Optional[Any] = None  # [string]
    val: Any  # [string]
    character: Optional[Any] = None  # [string]


class ProductSetProductRequest(LingXingModel):
    """Request for 添加/编辑本地产品.

    POST /erp/sc/routing/storage/product/set
    """

    sku: str  # SKU
    product_name: str  # 品名【添加时必填】
    sku_identifier: Optional[str] = None  # SKU识别码
    unit_process_fee: Optional[int] = None  # 单位加工费
    unit: Optional[str] = None  # 单位（商品单位：套、个、台）
    category_id: Optional[int] = None  # 分类id，与分类同时存在时，优先取分类id
    category: Optional[str] = None  # 分类
    model: Optional[str] = None  # 型号
    brand_id: Optional[int] = None  # 品牌id，与品牌同时存在时，优先取品牌id
    brand: Optional[str] = None  # 品牌
    open_status: Optional[int] = None  # 开启状态：0 停用，1 启用
    status: Optional[int] = None  # 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓
    description: Optional[str] = None  # 商品描述
    cg_opt_uid: Optional[int] = None  # 采购：采购员id，与采购员名同时填写时，以采购员id为准
    cg_opt_username: Optional[str] = None  # 采购：采购员名
    product_developer_uid: Optional[int] = None  # 开发者id，与开发者名称同时填写时，以开发者id为准
    product_developer: Optional[str] = None  # 开发者名称
    product_creator_uid: Optional[int] = None  # 创建人id，默认API账号id
    product_duty_uids: Optional[list] = None  # 负责人id
    is_append_product_duty: Optional[int] = None  # 负责人是否追加创建人：0 否，1 是；默认1，只有编辑SKU时才生效
    purchase_remark: Optional[str] = None  # 采购备注
    cg_price: Optional[str] = None  # 采购：采购成本（RMB）
    is_related: Optional[int] = None  # 是否关联单品成本：0 否，1 是
    cg_delivery: Optional[int] = None  # 采购：采购交期
    cg_product_material: Optional[str] = None  # 采购：商品材质
    cg_product_length: Optional[str] = None  # 采购：单品规格-长（CM）
    cg_product_width: Optional[str] = None  # 采购：单品规格-宽（CM）
    cg_product_height: Optional[str] = None  # 采购：单品规格-高（CM）
    cg_product_net_weight: Optional[str] = None  # 采购：单品净重（G）
    cg_product_gross_weight: Optional[str] = None  # 采购：单品毛重（G）
    cg_package_length: Optional[str] = None  # 采购：包装规格-长（CM）
    cg_package_width: Optional[str] = None  # 采购：包装规格-宽（CM）
    cg_package_height: Optional[str] = None  # 采购：包装规格-高（CM）
    cg_box_length: Optional[str] = None  # 采购：外箱规格-长（CM）
    cg_box_width: Optional[str] = None  # 采购：外箱规格-宽（CM）
    cg_box_height: Optional[str] = None  # 采购：外箱规格-高（CM）
    cg_box_weight: Optional[str] = None  # 采购：单箱重量（KG）
    cg_box_pcs: Optional[int] = None  # 采购：单箱数量（包装数量）
    bg_customs_export_name: Optional[str] = None  # 报关：申报品名(中文)
    bg_export_hs_code: Optional[str] = None  # 报关：HS Code(中国)
    bg_customs_import_name: Optional[str] = None  # 报关：申报品名(英文)
    currency: Optional[str] = None  # 报关：申报金额的币种
    bg_customs_import_price: Optional[str] = None  # 报关：申报金额
    special_attr: Optional[list] = (
        None  # 产品特殊属性：1 含电，2 纯电，3 液体，4 粉末，5 膏体，6 带磁，7 纺织品，8普货（普货于其他选项互斥）
    )
    picture_list: Optional[List[ProductSetProductRequestPictureListItem]] = None
    group_list: Optional[List[ProductSetProductRequestGroupListItem]] = None
    qc_standard: Optional[ProductSetProductRequestQcStandardItem] = None
    product_logistics_list: Optional[ProductSetProductRequestProductLogisticsListItem] = None
    supplier_quote: Optional[List[ProductSetProductRequestSupplierQuoteItem]] = None
    declaration: Optional[ProductSetProductRequestDeclarationItem] = None
    clearance: Optional[ProductSetProductRequestClearanceItem] = None
    aux_relation_list: Optional[List[ProductSetProductRequestAuxRelationListItem]] = None
    spec_pack_list: Optional[List[ProductSetProductRequestSpecPackListItem]] = None
    custom_fields: Optional[ProductSetProductRequestCustomFieldsItem] = None


class ProductAttributelistRequest(LingXingModel):
    """Request for 查询产品属性列表.

    POST /erp/sc/routing/storage/attribute/attributeList
    """

    offset: int  # 分页偏移量
    length: int  # 分页长度，上限200


class ProductAttributesetRequestAttrValuesItem(LingXingModel):
    pai_id: Optional[int] = None  # 领星属性值id
    attr_value: str  # 属性值名称


class ProductAttributesetRequest(LingXingModel):
    """Request for 添加 / 编辑产品属性.

    POST /erp/sc/routing/storage/attribute/set
    """

    pa_id: Optional[int] = None  # 领星属性id
    attr_name: str  # 属性名
    attr_values: List[ProductAttributesetRequestAttrValuesItem]


class ProductSpulistRequest(LingXingModel):
    """Request for 查询多属性产品列表.

    POST /erp/sc/routing/storage/spu/spuList
    """

    offset: int  # 分页偏移量
    length: int  # 分页长度，上限200


class ProductSpuinfoRequest(LingXingModel):
    """Request for 查询多属性产品详情.

    POST /erp/sc/routing/storage/spu/info
    """

    ps_id: int  # SPU唯一id【ps_id 与 spu二选一必填
    spu: str  # SPU


class ProductSpusetRequestSkuListItem(LingXingModel):
    sku: str  # 本地产品SKU
    product_name: Optional[str] = None  # 产品名称【提交的sku不存在时为必填项】
    attribute: List  # 属性列表
    attribute__pa_id: int  # 属性id
    attribute__pai_id: int  # 属性值id
    picture_list: Optional[list] = None  # 产品图片信息
    picture_list__is_primary: int  # 是否产品主图:0否,1是


class ProductSpusetRequestSkuLisItem(LingXingModel):
    picture_list__pic_url: str  # 产品图片链接


class ProductSpusetRequestPurchaseInfoItem(LingXingModel):
    cg_uid: Optional[int] = None  # 采购：采购员id
    purchase_remark: Optional[str] = None  # 采购：采购备注
    cg_delivery: Optional[int] = None  # 采购：采购交期（天）
    cg_product_length: Optional[float] = None  # 采购：单品规格-长（CM）
    cg_product_width: Optional[float] = None  # 采购：单品规格-宽（CM）
    cg_product_height: Optional[float] = None  # 采购：单品规格-高（CM）
    cg_product_net_weight: Optional[float] = None  # 采购：单品净重（G）
    cg_product_gross_weight: Optional[float] = None  # 采购：单品毛重（G）
    cg_package_length: Optional[float] = None  # 采购：包装规格-长（CM）
    cg_package_width: Optional[float] = None  # 采购：包装规格-宽（CM）
    cg_package_height: Optional[float] = None  # 采购：包装规格-高（CM）
    cg_box_length: Optional[float] = None  # 采购：外箱规格-长（CM）
    cg_box_width: Optional[float] = None  # 采购：外箱规格-宽（CM）
    cg_box_height: Optional[float] = None  # 采购：外箱规格-高（CM）
    cg_box_weight: Optional[float] = None  # 采购：单箱重量（KG）
    cg_box_pcs: Optional[str] = None  # 采购：单箱数量（包装数量）
    cg_product_material: Optional[str] = None  # 采购：产品材质


class ProductSpusetRequestLogisticsItem(LingXingModel):
    declaration: Optional[dict] = None  # 报关数据
    declaration__customs_export_name: Optional[str] = None  # 报关：申报品名（中文）
    declaration__customs_import_name: Optional[str] = None  # 报关：申报品名（英文）
    declaration__customs_import_price_currency: Optional[str] = None  # 报关：申报单价的币种
    declaration__customs_import_price: Optional[float] = None  # 报关：申报单价
    declaration__customs_declaration_unit: Optional[str] = None  # 报关单位
    declaration__customs_declaration_spec: Optional[str] = None  # 规格型号
    declaration__customs_declaration_origin_produce: Optional[str] = None  # 报关：原厂国（地区）
    declaration__customs_declaration_inlands_source: Optional[str] = None  # 报关：境内货源地
    declaration__customs_declaration_exempt: Optional[str] = None  # 报关：征免
    clearance: Optional[dict] = None  # 清关数据
    clearance__customs_clearance_material: Optional[str] = None  # 清关：材质
    clearance__customs_clearance_usage: Optional[str] = None  # 清关：用途
    clearance__customs_clearance_internal_code: Optional[str] = None  # 清关：内部编码
    clearance__customs_clearance_preferential: Optional[str] = (
        None  # 清关：出口享惠情况： 1 不享惠 2 享惠 3 不确定享惠情况
    )
    clearance__customs_clearance_brand_type: Optional[str] = (
        None  # 清关：品牌类型： 1 无品牌 2 境内自主品牌 3 境内收购品牌 4 境外品牌（贴牌生产） 5 境外品牌（其他）
    )
    clearance__customs_clearance_product_pattern: Optional[str] = None  # 清关：产品型号
    clearance__allocation_remark: Optional[str] = None  # 清关：配货备注
    clearance__customs_clearance_pic_url: Optional[str] = None  # 清关：清关图片
    base: Optional[dict] = None  # 物流基础信息
    base__bg_export_hs_code: Optional[str] = None  # 报关：HS Code（中国）
    base__special_attr: Optional[list] = None  # 产品特殊属性：1 含电 2 纯电 3 液体 4 粉末 5 膏体 6 带磁
    fee: Optional[dict] = (
        None  # 头程费用，支持国家：US、CA、MX、JP、UK、DE、FR、ES、IT、NL、AU、SG、IN、AE、SA、BR、SE、PL、BE、TR、UA、HU、PK、LB、AT、CH、CZ、DK、IE、LU、
    )
    fee_______cg_transport_costs: Optional[float] = None  # 默认头程费用（含税）
    fee_______currency: Optional[str] = None  # 默认头程费用币种
    fee_______clearance_price: Optional[float] = None  # 清关价格
    fee_______clearance_price_currency: Optional[str] = None  # 清关价格币种
    fee_______bg_import_hs_code: Optional[str] = None  # HS Code
    fee_______bg_tax_rate: Optional[float] = None  # 税率


class ProductSpusetRequestAuxRelationListItem(LingXingModel):
    aux_sku: str  # 辅料sku
    sku_qty: str  # 辅料比例（主料）
    aux_qty: str  # 辅料比例（辅料）


class ProductSpusetRequestAttributeSkcListItem(LingXingModel):
    pa_id: int  # 属性id
    skc: str  # skc，新增时根据skc业务配置规则自动生成


class ProductSpusetRequest(LingXingModel):
    """Request for 添加/编辑多属性产品.

    POST /erp/sc/routing/storage/spu/set
    """

    spu: str  # SPU（添加时必填）
    spu_name: str  # 款名（添加时必填）
    model: Optional[str] = None  # 型号
    unit: Optional[str] = None  # 单位
    status: Optional[int] = None  # 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓
    cid: Optional[int] = None  # 分类id
    bid: Optional[int] = None  # 品牌id
    create_uid: Optional[int] = None  # 创建人id
    developer_uid: Optional[int] = None  # 开发人id
    product_duty_uids: Optional[list] = None  # 产品负责人id
    description: Optional[str] = None  # 产品描述
    use_spu_template: Optional[int] = None  # 是否应用SPU信息至新生成的SKU：0 否，1 是
    sku_list: List[ProductSpusetRequestSkuListItem]
    sku_lis: ProductSpusetRequestSkuLisItem
    purchase_info: Optional[ProductSpusetRequestPurchaseInfoItem] = None
    logistics: Optional[ProductSpusetRequestLogisticsItem] = None
    aux_relation_list: Optional[List[ProductSpusetRequestAuxRelationListItem]] = None
    attribute_skc_list: Optional[List[ProductSpusetRequestAttributeSkcListItem]] = None


class ProductBundledproductlistRequest(LingXingModel):
    """Request for 查询捆绑产品关系列表.

    POST /erp/sc/routing/data/local_inventory/bundledProductList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000


class ProductSetBundledRequestPictureListItem(LingXingModel):
    pic_url: Optional[str] = None  # 产品图片链接
    is_primary: Optional[int] = None  # 是否产品主图：0 否，1 是


class ProductSetBundledRequestGroupListItem(LingXingModel):
    sku: Optional[str] = None  # 子商品
    quantity: Optional[int] = None  # 商品比例数
    cost_ratio: Optional[int] = None  # 费用比例，默认为空，若填写则每项必填，且总和为1


class ProductSetBundledRequest(LingXingModel):
    """Request for 添加 / 编辑捆绑产品.

    POST /erp/sc/routing/storage/product/setBundled
    """

    sku: str  # SKU（添加时必填）
    product_name: str  # 品名（添加时必填）
    model: Optional[str] = None  # 型号
    unit: Optional[str] = None  # 单位（商品单位：套、个、台）
    status: Optional[int] = None  # 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓
    category_id: Optional[int] = None  # 分类id,与分类同时存在时，优先取分类id
    category: Optional[str] = None  # 分类
    brand_id: Optional[int] = None  # 品牌id，与品牌同时存在时，优先取品牌id
    brand: Optional[str] = None  # 品牌
    product_developer: Optional[str] = None  # 开发者名称
    product_developer_uid: Optional[int] = None  # 开发者id，与开发者名称同时填写时，以开发者id为准
    product_duty_uids: Optional[list] = None  # 负责人id
    is_append_product_duty: Optional[int] = None  # 负责人是否追加创建人：0 否，1 是；默认1，该字段只有编辑SKU时该才生效
    product_creator_uid: Optional[int] = None  # 创建人ERP id，默认 api 用户id
    description: Optional[str] = None  # 商品描述
    picture_list: Optional[List[ProductSetBundledRequestPictureListItem]] = None
    group_list: Optional[List[ProductSetBundledRequestGroupListItem]] = None


class ProductProductauxlistRequest(LingXingModel):
    """Request for 查询产品辅料列表.

    POST /erp/sc/routing/data/local_inventory/productAuxList
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000


class ProductSetauxRequestSupplierQuoteItem(LingXingModel):
    erp_supplier_id: Optional[int] = None  # 领星ERP供应商id
    supplier_id: Optional[int] = None  # 客户系统供应商id，没有填这个值或者对应供应商不存在，则取erp_supplier_id
    supplier_product_url: Optional[list] = None  # 采购链接，字符串数组，最多20个，没有则传空数组
    is_primary: Optional[int] = None  # 是否首选供应商：0-否，1:是
    quotes: Optional[list] = None  # 报价信息
    quotes__currency: Optional[str] = None  # 报价币种，目前只有CNY和USD
    quotes__is_tax: Optional[int] = None  # 是否含税：0-否，1-是
    quotes__tax_rate: Optional[int] = None  # 税率，为空则表示为0
    quotes__step_prices: Optional[list] = None  # 阶梯价信息
    quotes__step_prices__moq: Optional[int] = None  # 最小起订量，最小值为1
    quotes__step_prices__price_with_tax: Optional[float] = None  # 含税单价，4位小数


class ProductSetauxRequest(LingXingModel):
    """Request for 添加 / 编辑辅料.

    POST /erp/sc/routing/storage/product/setAux
    """

    sku: str  # SKU
    product_name: str  # 品名
    cg_price: Optional[float] = None  # 采购：采购成本（人民币）
    cg_product_length: Optional[float] = None  # 采购：单品规格-长（CM）
    cg_product_width: Optional[float] = None  # 采购：单品规格-宽（CM）
    cg_product_height: Optional[float] = None  # 采购：单品规格-高（CM）
    cg_product_net_weight: Optional[float] = None  # 采购：单品净重（G）
    remark: str  # 辅料描述
    supplier_quote: Optional[List[ProductSetauxRequestSupplierQuoteItem]] = None


class ProductBrandRequest(LingXingModel):
    """Request for 查询产品品牌列表.

    POST /erp/sc/data/local_inventory/brand
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000


class ProductSetBrandRequestDataItem(LingXingModel):
    id: Optional[int] = None  # 为空时表新增，不为空时表编辑，查询本地产品品牌列表对应bid字段
    title: str  # 品牌名称
    brand_code: Optional[str] = None  # 品牌简码


class ProductSetBrandRequest(LingXingModel):
    """Request for 添加/编辑产品品牌.

    POST /erp/sc/storage/brand/set
    """

    data: List[ProductSetBrandRequestDataItem]


class ProductCategoryRequestDataItem(LingXingModel):
    ids: Optional[list] = None  # 分类ID


class ProductCategoryRequest(LingXingModel):
    """Request for 查询产品分类列表.

    POST /erp/sc/routing/data/local_inventory/category
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认1000，上限1000
    data: Optional[ProductCategoryRequestDataItem] = None


class ProductSetCategoryRequestDataItem(LingXingModel):
    id: Optional[int] = None  # 为空时新增，不为空时编辑，查询本地产品分类列表对应cid字段
    parent_cid: Optional[int] = None  # 父级分类id
    title: str  # 分类名称
    category_code: str  # 分类简码


class ProductSetCategoryRequest(LingXingModel):
    """Request for 添加 / 编辑产品分类.

    POST /erp/sc/routing/storage/category/set
    """

    data: List[ProductSetCategoryRequestDataItem]


class ProductUploadPicturesRequestPictureListItem(LingXingModel):
    pic_url: str  # 产品图片链接
    is_primary: int  # 是否产品主图：0 否，1 是


class ProductUploadPicturesRequest(LingXingModel):
    """Request for 上传本地产品图片.

    POST /erp/sc/routing/storage/product/uploadPictures
    """

    sku: str  # 本地产品SKU
    picture_list: List[ProductUploadPicturesRequestPictureListItem]


class ProductCreateProductTagRequest(LingXingModel):
    """Request for 创建产品标签.

    POST /label/operation/v1/label/product/create
    """

    label: str  # 标签名称，最长15个字符，中间不能有空格


class ProductSetProductTagRequestDetailListItem(LingXingModel):
    sku: str  # 产品SKU
    label_list: List  # 标签名称，上限10


class ProductSetProductTagRequest(LingXingModel):
    """Request for 标记产品标签.

    POST /label/operation/v1/label/product/mark
    """

    type: int  # 操作类型：1 追加，2 覆盖
    detail_list: List[ProductSetProductTagRequestDetailListItem]


class ProductDelProductTagRequestDetailListItem(LingXingModel):
    sku: str  # 本地产品sku
    label_list: List  # 标签名称，上限10


class ProductDelProductTagRequest(LingXingModel):
    """Request for 删除产品标签.

    POST /label/operation/v1/label/product/unmarkLabel
    """

    type: int  # 操作类型： 1 删除SKU指定的标签 2 删除SKU全部的标签【此类型下对应sku的label_list为空数组即可】
    detail_list: List[ProductDelProductTagRequestDetailListItem]


class ProductGetPagingLogListsRequest(LingXingModel):
    """Request for 查询操作日志.

    POST /basicOpen/product/getPagingLogLists
    """

    businessId: Optional[int] = None  # businessId，对应查询本地产品列表data>>id字段
    endTime: Optional[str] = None  # 结束时间
    startTime: Optional[str] = None  # 开始时间
    page: Optional[int] = None  # 页码
    size: Optional[int] = None  # 每页大小


class ProductGettransparencyproductlistRequest(LingXingModel):
    """Request for 产品管理-查询透明计划商品列表.

    POST /basicOpen/product/getTransparencyProductList
    """

    isRelateMsku: Optional[int] = None  # 是否关联MSKU，枚举值：1-是, 2-否
    length: Optional[int] = None  # 分页长度，默认20，最大200
    offset: Optional[int] = None  # 分页偏移量，默认0
    productStatus: Optional[str] = (
        None  # 产品状态，枚举值：all-全部, Enrolled-已注册, In OPR-OPR中, Protected-受保护, NoStatus-无状态
    )
    searchField: Optional[str] = None  # 搜索字段，指定搜索的字段名
    searchValue: Optional[str] = None  # 搜索值，用于模糊搜索

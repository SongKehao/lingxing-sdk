"""产品 API endpoints."""
from __future__ import annotations

from ..models.responses.product import (
    LocalInventoryBatchgetproductinfoResponse,
    LocalInventoryBrandResponse,
    LocalInventoryBundledproductlistResponse,
    LocalInventoryCategoryResponse,
    LocalInventoryProductauxlistResponse,
    LocalInventoryProductinfoResponse,
    LocalInventoryProductlistResponse,
    ProductGetpagingloglistsResponse,
    ProductGettransparencyproductlistResponse,
    ProductOperateBatchResponse,
    PublishUpcAddcommoditycodeResponse,
    PublishUpcUpclistResponse,
    StorageAttributeAttributelistResponse,
    StorageAttributeSetResponse,
    StorageBrandSetResponse,
    StorageCategorySetResponse,
    StorageProductSetResponse,
    StorageProductSetauxResponse,
    StorageProductSetbundledResponse,
    StorageProductUploadpicturesResponse,
    StorageSpuInfoResponse,
    StorageSpuSetResponse,
    StorageSpuSpulistResponse,
)

from typing import Any

from ..models.responses.product import AttributeListItem, BrandItem, CategoryItem, ProductListsItem, UpcListItem
from ._base import BaseEndpoint


class ProductEndpoints(BaseEndpoint):
    """领星产品 API (23个接口)."""

    async def add_commodity_code(self, commodity_codes: Any = None, code_type: str = None) -> PublishUpcAddcommoditycodeResponse | None:
        """创建UPC编码.

POST /listing/publish/api/upc/addCommodityCode

Args:
    commodity_codes: 编码-最多支持两百个 (required), array.
    code_type: 编码类型：支持UPC、EAN、ISBN (required), string."""
        resp = await self._post("/listing/publish/api/upc/addCommodityCode", {k: v for k, v in {"commodity_codes": commodity_codes, "code_type": code_type}.items() if v is not None})
        return self._parse_one(resp.data, PublishUpcAddcommoditycodeResponse)
    async def brand(self, offset: int = None, length: int = None) -> list[LocalInventoryBrandResponse]:
        """查询产品品牌列表.

POST /erp/sc/data/local_inventory/brand

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int."""
        resp = await self._post("/erp/sc/data/local_inventory/brand", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, BrandItem)
    async def category(self, offset: int = None, length: int = None, data: Any = None) -> list[LocalInventoryCategoryResponse]:
        """查询产品分类列表.

POST /erp/sc/routing/data/local_inventory/category

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/category", {k: v for k, v in {"offset": offset, "length": length, "data": data}.items() if v is not None})
        return self._parse_list(resp.data, CategoryItem)
    async def get_paging_log_lists(self, businessId: int = None, endTime: str = None, startTime: str = None, page: int = None, size: int = None) -> list[ProductGetpagingloglistsResponse]:
        """查询操作日志.

POST /basicOpen/product/getPagingLogLists

Args:
    businessId: businessId，对应查询本地产品列表data>>id字段, long.
    endTime: 结束时间, string.
    startTime: 开始时间, string.
    page: 页码, int.
    size: 每页大小, int."""
        resp = await self._post("/basicOpen/product/getPagingLogLists", {k: v for k, v in {"businessId": businessId, "endTime": endTime, "startTime": startTime, "page": page, "size": size}.items() if v is not None})
        return self._parse_list(resp.data, ProductGetpagingloglistsResponse)
    async def product_details(self, id: int = None, sku: str = None, sku_identifier: str = None) -> list[LocalInventoryProductinfoResponse]:
        """查询本地产品详情.

POST /erp/sc/routing/data/local_inventory/productInfo

Args:
    id: 产品id【产品id、 产品SKU 、SKU识别码 三选一必填】, int.
    sku: 产品SKU【产品id、 产品SKU 、SKU识别码 三选一必填】, string.
    sku_identifier: SKU识别码【产品id、 产品SKU 、SKU识别码 三选一必填】, string."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productInfo", {k: v for k, v in {"id": id, "sku": sku, "sku_identifier": sku_identifier}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryProductinfoResponse)
    async def product_lists(self, offset: int = None, length: int = None, update_time_start: int = None, update_time_end: int = None, create_time_start: int = None, create_time_end: int = None, sku_list: list = None, sku_identifier_list: list = None) -> list[LocalInventoryProductlistResponse]:
        """查询本地产品列表.

POST /erp/sc/routing/data/local_inventory/productList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int.
    update_time_start: 更新时间-开始时间【时间戳，单位：秒，左闭右开】, int.
    update_time_end: 更新时间-结束时间【时间戳，单位：秒，左闭右开】, int.
    create_time_start: 创建时间-开始时间【时间戳，单位：秒，左闭右开】, int.
    create_time_end: 创建时间-结束时间【时间戳，单位：秒，左闭右开】, int.
    sku_list: 本地产品sku, array.
    sku_identifier_list: sku识别码列表, array."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productList", {k: v for k, v in {"offset": offset, "length": length, "update_time_start": update_time_start, "update_time_end": update_time_end, "create_time_start": create_time_start, "create_time_end": create_time_end, "sku_list": sku_list, "sku_identifier_list": sku_identifier_list}.items() if v is not None})
        return self._parse_list(resp.data, ProductListsItem)
    async def set_brand(self, data: list = None) -> list[StorageBrandSetResponse]:
        """添加/编辑产品品牌.

POST /erp/sc/storage/brand/set

Args:
    data: 请求数据 (required), array."""
        resp = await self._post("/erp/sc/storage/brand/set", {k: v for k, v in {"data": data}.items() if v is not None})
        return self._parse_list(resp.data, StorageBrandSetResponse)
    async def set_bundled(self, sku: str = None, product_name: str = None, model: str = None, unit: str = None, status: int = None, category_id: int = None, category: str = None, brand_id: int = None, brand: str = None, product_developer: str = None, product_developer_uid: int = None, product_duty_uids: list = None, is_append_product_duty: int = None, product_creator_uid: int = None, description: str = None, picture_list: list = None, group_list: list = None) -> list[StorageProductSetbundledResponse]:
        """添加 / 编辑捆绑产品.

POST /erp/sc/routing/storage/product/setBundled

Args:
    sku: SKU（添加时必填） (required), string.
    product_name: 品名（添加时必填） (required), string.
    picture_list: 产品图片信息, array.
    model: 型号, string.
    unit: 单位（商品单位：套、个、台）, string.
    status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓, int.
    category_id: 分类id,与分类同时存在时，优先取分类id, int.
    category: 分类, string.
    brand_id: 品牌id，与品牌同时存在时，优先取品牌id, int.
    brand: 品牌, string.
    product_developer: 开发者名称, string.
    product_developer_uid: 开发者id，与开发者名称同时填写时，以开发者id为准, int.
    product_duty_uids: 负责人id, array.
    is_append_product_duty: 负责人是否追加创建人：0 否，1 是；默认1，该字段只有编辑SKU时该才生效, int.
    product_creator_uid: 创建人ERP id，默认 api 用户id, int.
    description: 商品描述, string.
    group_list: 组合商品列表，捆绑产品子产品的总数量要大于1, array."""
        resp = await self._post("/erp/sc/routing/storage/product/setBundled", {k: v for k, v in {"sku": sku, "product_name": product_name, "model": model, "unit": unit, "status": status, "category_id": category_id, "category": category, "brand_id": brand_id, "brand": brand, "product_developer": product_developer, "product_developer_uid": product_developer_uid, "product_duty_uids": product_duty_uids, "is_append_product_duty": is_append_product_duty, "product_creator_uid": product_creator_uid, "description": description, "picture_list": picture_list, "group_list": group_list}.items() if v is not None})
        return self._parse_list(resp.data, StorageProductSetbundledResponse)
    async def set_category(self, data: list = None) -> list[StorageCategorySetResponse]:
        """添加 / 编辑产品分类.

POST /erp/sc/routing/storage/category/set

Args:
    data: 请求数据 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/category/set", {k: v for k, v in {"data": data}.items() if v is not None})
        return self._parse_list(resp.data, StorageCategorySetResponse)
    async def set_product(self, sku: str = None, product_name: str = None, sku_identifier: str = None, unit_process_fee: int = None, unit: str = None, category_id: int = None, category: str = None, model: str = None, brand_id: int = None, brand: str = None, open_status: int = None, status: int = None, description: str = None, cg_opt_uid: int = None, cg_opt_username: str = None, product_developer_uid: int = None, product_developer: str = None, product_creator_uid: int = None, product_duty_uids: list = None, is_append_product_duty: int = None, purchase_remark: str = None, cg_price: str = None, is_related: int = None, cg_delivery: int = None, cg_product_material: str = None, cg_product_length: str = None, cg_product_width: str = None, cg_product_height: str = None, cg_product_net_weight: str = None, cg_product_gross_weight: str = None, cg_package_length: str = None, cg_package_width: str = None, cg_package_height: str = None, cg_box_length: str = None, cg_box_width: str = None, cg_box_height: str = None, cg_box_weight: str = None, cg_box_pcs: int = None, bg_customs_export_name: str = None, bg_export_hs_code: str = None, bg_customs_import_name: str = None, currency: str = None, bg_customs_import_price: str = None, special_attr: list = None, picture_list: list = None, group_list: list = None, qc_standard: Any = None, product_logistics_list: Any = None, supplier_quote: list = None, declaration: Any = None, clearance: Any = None, aux_relation_list: list = None, spec_pack_list: list = None, custom_fields: Any = None) -> list[StorageProductSetResponse]:
        """添加/编辑本地产品.

POST /erp/sc/routing/storage/product/set

Args:
    sku: SKU (required), string.
    product_name: 品名【添加时必填】 (required), string.
    sku_identifier: SKU识别码, string.
    picture_list: 产品图片信息, array.
    unit_process_fee: 单位加工费, int.
    unit: 单位（商品单位：套、个、台）, string.
    category_id: 分类id，与分类同时存在时，优先取分类id, int.
    category: 分类, string.
    model: 型号, string.
    brand_id: 品牌id，与品牌同时存在时，优先取品牌id, int.
    brand: 品牌, string.
    open_status: 开启状态：0 停用，1 启用, int.
    status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓, int.
    description: 商品描述, string.
    group_list: 组合商品列表, array.
    cg_opt_uid: 采购：采购员id，与采购员名同时填写时，以采购员id为准, int.
    cg_opt_username: 采购：采购员名, string.
    product_developer_uid: 开发者id，与开发者名称同时填写时，以开发者id为准, int.
    product_developer: 开发者名称, string.
    product_creator_uid: 创建人id，默认API账号id, int.
    product_duty_uids: 负责人id, array.
    is_append_product_duty: 负责人是否追加创建人：0 否，1 是；默认1，只有编辑SKU时才生效, int.
    purchase_remark: 采购备注, string.
    cg_price: 采购：采购成本（RMB）, string.
    is_related: 是否关联单品成本：0 否，1 是, int.
    cg_delivery: 采购：采购交期, int.
    cg_product_material: 采购：商品材质, string.
    cg_product_length: 采购：单品规格-长（CM）, string.
    cg_product_width: 采购：单品规格-宽（CM）, string.
    cg_product_height: 采购：单品规格-高（CM）, string.
    cg_product_net_weight: 采购：单品净重（G）, string.
    cg_product_gross_weight: 采购：单品毛重（G）, string.
    cg_package_length: 采购：包装规格-长（CM）, string.
    cg_package_width: 采购：包装规格-宽（CM）, string.
    cg_package_height: 采购：包装规格-高（CM）, string.
    cg_box_length: 采购：外箱规格-长（CM）, string.
    cg_box_width: 采购：外箱规格-宽（CM）, string.
    cg_box_height: 采购：外箱规格-高（CM）, string.
    cg_box_weight: 采购：单箱重量（KG）, string.
    cg_box_pcs: 采购：单箱数量（包装数量）, int.
    bg_customs_export_name: 报关：申报品名(中文), string.
    bg_export_hs_code: 报关：HS Code(中国), string.
    bg_customs_import_name: 报关：申报品名(英文), string.
    currency: 报关：申报金额的币种, string.
    bg_customs_import_price: 报关：申报金额, string.
    qc_standard: 质检标准, object.
    product_logistics_list: 报关清关费用信息 支持国家：US、CA、MX、JP、UK、DE、FR、ES、IT、NL、AU、SG、IN、AE、SA、BR、SE、PL、BE、TR、UA、HU、PK、LB、AT、CH、CZ、DK、IE、LU、NO、PT、SK、RU、KZ、BY、CL、KR, object.
    supplier_quote: 供应商报价信息（该参数传空值则清空产品供应商报价）, array.
    special_attr: 产品特殊属性：1 含电，2 纯电，3 液体，4 粉末，5 膏体，6 带磁，7 纺织品，8普货（普货于其他选项互斥）, array.
    declaration: 报关数据, object.
    clearance: 清关数据, object.
    aux_relation_list: 辅料列表, array.
    spec_pack_list: 采购：更多箱规（非默认箱规）, array.
    custom_fields: [array], 自定义字段."""
        resp = await self._post("/erp/sc/routing/storage/product/set", {k: v for k, v in {"sku": sku, "product_name": product_name, "sku_identifier": sku_identifier, "unit_process_fee": unit_process_fee, "unit": unit, "category_id": category_id, "category": category, "model": model, "brand_id": brand_id, "brand": brand, "open_status": open_status, "status": status, "description": description, "cg_opt_uid": cg_opt_uid, "cg_opt_username": cg_opt_username, "product_developer_uid": product_developer_uid, "product_developer": product_developer, "product_creator_uid": product_creator_uid, "product_duty_uids": product_duty_uids, "is_append_product_duty": is_append_product_duty, "purchase_remark": purchase_remark, "cg_price": cg_price, "is_related": is_related, "cg_delivery": cg_delivery, "cg_product_material": cg_product_material, "cg_product_length": cg_product_length, "cg_product_width": cg_product_width, "cg_product_height": cg_product_height, "cg_product_net_weight": cg_product_net_weight, "cg_product_gross_weight": cg_product_gross_weight, "cg_package_length": cg_package_length, "cg_package_width": cg_package_width, "cg_package_height": cg_package_height, "cg_box_length": cg_box_length, "cg_box_width": cg_box_width, "cg_box_height": cg_box_height, "cg_box_weight": cg_box_weight, "cg_box_pcs": cg_box_pcs, "bg_customs_export_name": bg_customs_export_name, "bg_export_hs_code": bg_export_hs_code, "bg_customs_import_name": bg_customs_import_name, "currency": currency, "bg_customs_import_price": bg_customs_import_price, "special_attr": special_attr, "picture_list": picture_list, "group_list": group_list, "qc_standard": qc_standard, "product_logistics_list": product_logistics_list, "supplier_quote": supplier_quote, "declaration": declaration, "clearance": clearance, "aux_relation_list": aux_relation_list, "spec_pack_list": spec_pack_list, "custom_fields": custom_fields}.items() if v is not None})
        return self._parse_list(resp.data, StorageProductSetResponse)
    async def upc_list(self, offset: int = None, length: int = None) -> tuple[list[PublishUpcUpclistResponse], int]:
        """获取UPC编码列表.

POST /listing/publish/api/upc/upcList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/listing/publish/api/upc/upcList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_page(resp.data, UpcListItem)
    async def upload_pictures(self, sku: str = None, picture_list: list = None) -> list[StorageProductUploadpicturesResponse]:
        """上传本地产品图片.

POST /erp/sc/routing/storage/product/uploadPictures

Args:
    sku: 本地产品SKU (required), string.
    picture_list: 产品图片信息 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/product/uploadPictures", {k: v for k, v in {"sku": sku, "picture_list": picture_list}.items() if v is not None})
        return self._parse_list(resp.data, StorageProductUploadpicturesResponse)
    async def attribute_list(self, offset: int = None, length: int = None) -> tuple[list[StorageAttributeAttributelistResponse], int]:
        """查询产品属性列表.

POST /erp/sc/routing/storage/attribute/attributeList

Args:
    offset: 分页偏移量 (required), int.
    length: 分页长度，上限200 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/attribute/attributeList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_page(resp.data, AttributeListItem)
    async def attribute_set(self, pa_id: int = None, attr_name: str = None, attr_values: list = None) -> list[StorageAttributeSetResponse]:
        """添加 / 编辑产品属性.

POST /erp/sc/routing/storage/attribute/set

Args:
    pa_id: 领星属性id, int.
    attr_name: 属性名 (required), string.
    attr_values: 属性值数组 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/attribute/set", {k: v for k, v in {"pa_id": pa_id, "attr_name": attr_name, "attr_values": attr_values}.items() if v is not None})
        return self._parse_list(resp.data, StorageAttributeSetResponse)
    async def batch_get_product_info(self, productIds: list = None, skus: list = None, sku_identifiers: list = None) -> LocalInventoryBatchgetproductinfoResponse | None:
        """批量查询本地产品详情.

POST /erp/sc/routing/data/local_inventory/batchGetProductInfo

Args:
    productIds: 产品id，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】, array.
    skus: 产品SKU，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】, array.
    sku_identifiers: SKU识别码，上限100个上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】, array."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/batchGetProductInfo", {k: v for k, v in {"productIds": productIds, "skus": skus, "sku_identifiers": sku_identifiers}.items() if v is not None})
        return self._parse_one(resp.data, LocalInventoryBatchgetproductinfoResponse)
    async def bundled_product_list(self, offset: int = None, length: int = None) -> list[LocalInventoryBundledproductlistResponse]:
        """查询捆绑产品关系列表.

POST /erp/sc/routing/data/local_inventory/bundledProductList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/bundledProductList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryBundledproductlistResponse)
    async def get_transparency_product_list(self, isRelateMsku: int = None, length: int = None, offset: int = None, productStatus: str = None, searchField: str = None, searchValue: str = None) -> list[ProductGettransparencyproductlistResponse]:
        """产品管理-查询透明计划商品列表.

POST /basicOpen/product/getTransparencyProductList

Args:
    isRelateMsku: 是否关联MSKU，枚举值：1-是, 2-否, int.
    length: 分页长度，默认20，最大200, int.
    offset: 分页偏移量，默认0, int.
    productStatus: 产品状态，枚举值：all-全部, Enrolled-已注册, In OPR-OPR中, Protected-受保护, NoStatus-无状态, string.
    searchField: 搜索字段，指定搜索的字段名, string.
    searchValue: 搜索值，用于模糊搜索, string."""
        resp = await self._post("/basicOpen/product/getTransparencyProductList", {k: v for k, v in {"isRelateMsku": isRelateMsku, "length": length, "offset": offset, "productStatus": productStatus, "searchField": searchField, "searchValue": searchValue}.items() if v is not None})
        return self._parse_list(resp.data, ProductGettransparencyproductlistResponse)
    async def product_aux_list(self, offset: int = None, length: int = None) -> list[LocalInventoryProductauxlistResponse]:
        """查询产品辅料列表.

POST /erp/sc/routing/data/local_inventory/productAuxList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000，上限1000, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/productAuxList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, LocalInventoryProductauxlistResponse)
    async def product_operate_batch(self, product_ids: list = None, batch_status: str = None) -> ProductOperateBatchResponse | None:
        """产品启用、禁用.

POST /basicOpen/product/productManager/product/operate/batch

Args:
    product_ids: 产品id, array.
    batch_status: 状态: Enable 启用 Disable 禁用 (required), string."""
        resp = await self._post("/basicOpen/product/productManager/product/operate/batch", {k: v for k, v in {"product_ids": product_ids, "batch_status": batch_status}.items() if v is not None})
        return self._parse_one(resp.data, ProductOperateBatchResponse)
    async def set_aux(self, sku: str = None, product_name: str = None, cg_price: float = None, cg_product_length: float = None, cg_product_width: float = None, cg_product_height: float = None, cg_product_net_weight: float = None, remark: str = None, supplier_quote: list = None) -> list[StorageProductSetauxResponse]:
        """添加 / 编辑辅料.

POST /erp/sc/routing/storage/product/setAux

Args:
    sku: SKU (required), string.
    product_name: 品名 (required), string.
    cg_price: 采购：采购成本（人民币）, number.
    cg_product_length: 采购：单品规格-长（CM）, number.
    cg_product_width: 采购：单品规格-宽（CM）, number.
    cg_product_height: 采购：单品规格-高（CM）, number.
    cg_product_net_weight: 采购：单品净重（G）, number.
    supplier_quote: 供应商报价信息（不传该参数则清空产品供应商报价）, array.
    remark: 辅料描述 (required), string."""
        resp = await self._post("/erp/sc/routing/storage/product/setAux", {k: v for k, v in {"sku": sku, "product_name": product_name, "cg_price": cg_price, "cg_product_length": cg_product_length, "cg_product_width": cg_product_width, "cg_product_height": cg_product_height, "cg_product_net_weight": cg_product_net_weight, "remark": remark, "supplier_quote": supplier_quote}.items() if v is not None})
        return self._parse_list(resp.data, StorageProductSetauxResponse)
    async def spu_info(self, ps_id: int = None, spu: str = None) -> list[StorageSpuInfoResponse]:
        """查询多属性产品详情.

POST /erp/sc/routing/storage/spu/info

Args:
    ps_id: SPU唯一id【ps_id 与 spu二选一必填 (required), int.
    spu: SPU (required), string."""
        resp = await self._post("/erp/sc/routing/storage/spu/info", {k: v for k, v in {"ps_id": ps_id, "spu": spu}.items() if v is not None})
        return self._parse_list(resp.data, StorageSpuInfoResponse)
    async def spu_list(self, offset: int = None, length: int = None) -> list[StorageSpuSpulistResponse]:
        """查询多属性产品列表.

POST /erp/sc/routing/storage/spu/spuList

Args:
    offset: 分页偏移量 (required), int.
    length: 分页长度，上限200 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/spu/spuList", {k: v for k, v in {"offset": offset, "length": length}.items() if v is not None})
        return self._parse_list(resp.data, StorageSpuSpulistResponse)
    async def spu_set(self, spu: str = None, spu_name: str = None, model: str = None, unit: str = None, status: int = None, cid: int = None, bid: int = None, create_uid: int = None, developer_uid: int = None, product_duty_uids: list = None, description: str = None, use_spu_template: int = None, sku_list: list = None, sku_lis: Any = None, purchase_info: Any = None, logistics: Any = None, aux_relation_list: list = None, attribute_skc_list: list = None) -> list[StorageSpuSetResponse]:
        """添加/编辑多属性产品.

POST /erp/sc/routing/storage/spu/set

Args:
    spu: SPU（添加时必填） (required), string.
    spu_name: 款名（添加时必填） (required), string.
    model: 型号, string.
    unit: 单位, string.
    status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓, int.
    cid: 分类id, int.
    bid: 品牌id, int.
    create_uid: 创建人id, int.
    developer_uid: 开发人id, int.
    product_duty_uids: 产品负责人id, array.
    description: 产品描述, string.
    use_spu_template: 是否应用SPU信息至新生成的SKU：0 否，1 是, int.
    sku_list: 产品列表【提交的sku不存在时系统会自动创建】 (required), array.
    purchase_info: 采购相关信息, object.
    logistics: 物流报关相关信息, object.
    aux_relation_list: 辅料列表, array.
    attribute_skc_list: skc列表, array."""
        resp = await self._post("/erp/sc/routing/storage/spu/set", {k: v for k, v in {"spu": spu, "spu_name": spu_name, "model": model, "unit": unit, "status": status, "cid": cid, "bid": bid, "create_uid": create_uid, "developer_uid": developer_uid, "product_duty_uids": product_duty_uids, "description": description, "use_spu_template": use_spu_template, "sku_list": sku_list, "sku_lis": sku_lis, "purchase_info": purchase_info, "logistics": logistics, "aux_relation_list": aux_relation_list, "attribute_skc_list": attribute_skc_list}.items() if v is not None})
        return self._parse_list(resp.data, StorageSpuSetResponse)

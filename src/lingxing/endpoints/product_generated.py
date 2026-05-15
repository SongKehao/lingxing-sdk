"""Product API Endpoints

Auto-generated from API documentation.
DO NOT EDIT MANUALLY - regenerate using code_generator.py
"""

from typing import Any

from ..core.openapi import OpenApiBase


class ProductEndpoints:

    def __init__(self, openapi: OpenApiBase):
        self._openapi = openapi

    async def get_product(
        self,
        access_token: str,
        id: int | None = None,
        sku: str | None = None,
        sku_identifier: str | None = None
    ) -> dict[str, Any]:
        """
        查询本地产品详情

        API: /erp/sc/routing/data/local_inventory/productInfo
        Method: POST

        Args:
            access_token: Access token for authentication
            id: 产品id【产品id、 产品SKU 、SKU识别码 三选一必填】 (Optional)
            sku: 产品SKU【产品id、 产品SKU 、SKU识别码 三选一必填】 (Optional)
            sku_identifier: SKU识别码【产品id、 产品SKU 、SKU识别码 三选一必填】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
            >>> print(result)
        """
        params = {
            "id": id,
            "sku": sku,
            "sku_identifier": sku_identifier
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productInfo",
            method="POST",
            req_body=params
        )



    async def get_productlist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询产品辅料列表

        API: /erp/sc/routing/data/local_inventory/productAuxList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productAuxList",
            method="POST",
            req_body=params
        )



    async def get_product(  # noqa: F811
        self,
        access_token: str,
        ps_id: int,
        spu: str
    ) -> dict[str, Any]:
        """
        查询多属性产品详情

        API: /erp/sc/routing/storage/spu/info
        Method: POST

        Args:
            access_token: Access token for authentication
            ps_id: SPU唯一id【ps_id 与 spu二选一必填 (Required)
            spu: SPU (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
            >>> print(result)
        """
        params = {
            "ps_id": ps_id,
            "spu": spu
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/info",
            method="POST",
            req_body=params
        )



    async def get_upclist(
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        获取UPC编码列表

        API: /listing/publish/api/upc/upcList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认20 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_upclist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/publish/api/upc/upcList",
            method="POST",
            req_body=params
        )



    async def create_product(
        self,
        access_token: str,
        label: str
    ) -> dict[str, Any]:
        """
        创建产品标签

        API: /label/operation/v1/label/product/create
        Method: POST

        Args:
            access_token: Access token for authentication
            label: 标签名称，最长15个字符，中间不能有空格 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "label": label
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/create",
            method="POST",
            req_body=params
        )



    async def get_product(  # noqa: F811
        self,
        access_token: str
    ) -> dict[str, Any]:
        """
        查询产品标签

        API: /label/operation/v1/label/product/list
        Method: GET

        Args:
            access_token: Access token for authentication

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
            >>> print(result)
        """
        params = {}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/list",
            method="GET",
            req_body=params
        )



    async def delete_product(
        self,
        access_token: str,
        detail_list: list[Any]
    ) -> dict[str, Any]:
        """
        删除产品标签

        API: /label/operation/v1/label/product/unmarkLabel
        Method: POST

        Args:
            access_token: Access token for authentication
            detail_list: 标签信息，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.delete_product(token, ...)
            >>> print(result)
        """
        params = {
            "detail_list": detail_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/unmarkLabel",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        sku: str,
        product_name: str,
        picture_list: list[Any] | None = None,
        model: str | None = None,
        unit: str | None = None,
        status: int | None = None,
        category_id: int | None = None,
        category: str | None = None,
        brand_id: int | None = None,
        brand: str | None = None,
        product_developer: str | None = None,
        product_developer_uid: int | None = None,
        product_duty_uids: list[Any] | None = None,
        is_append_product_duty: int | None = None,
        product_creator_uid: int | None = None,
        description: str | None = None,
        group_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        添加编辑捆绑产品

        API: /erp/sc/routing/storage/product/setBundled
        Method: POST

        Args:
            access_token: Access token for authentication
            sku: SKU（添加时必填） (Required)
            product_name: 品名（添加时必填） (Required)
            picture_list: 产品图片信息 (Optional)
            model: 型号 (Optional)
            unit: 单位（商品单位：套、个、台） (Optional)
            status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓 (Optional)
            category_id: 分类id,与分类同时存在时，优先取分类id (Optional)
            category: 分类 (Optional)
            brand_id: 品牌id，与品牌同时存在时，优先取品牌id (Optional)
            brand: 品牌 (Optional)
            product_developer: 开发者名称 (Optional)
            product_developer_uid: 开发者id，与开发者名称同时填写时，以开发者id为准 (Optional)
            product_duty_uids: 负责人id (Optional)
            is_append_product_duty: 负责人是否追加创建人：0 否，1 是；默认1，该字段只有编辑SKU时该才生效 (Optional)
            product_creator_uid: 创建人ERP id，默认 api 用户id (Optional)
            description: 商品描述 (Optional)
            group_list: 组合商品列表，捆绑产品子产品的总数量要大于1 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "sku": sku,
            "product_name": product_name,
            "picture_list": picture_list,
            "model": model,
            "unit": unit,
            "status": status,
            "category_id": category_id,
            "category": category,
            "brand_id": brand_id,
            "brand": brand,
            "product_developer": product_developer,
            "product_developer_uid": product_developer_uid,
            "product_duty_uids": product_duty_uids,
            "is_append_product_duty": is_append_product_duty,
            "product_creator_uid": product_creator_uid,
            "description": description,
            "group_list": group_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/setBundled",
            method="POST",
            req_body=params
        )



    async def product(
        self,
        access_token: str,
        type: int,
        detail_list: list[Any]
    ) -> dict[str, Any]:
        """
        标记产品标签

        API: /label/operation/v1/label/product/mark
        Method: POST

        Args:
            access_token: Access token for authentication
            type: 操作类型：1 追加，2 覆盖 (Required)
            detail_list: 标签信息，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.product(token, ...)
            >>> print(result)
        """
        params = {
            "type": type,
            "detail_list": detail_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/mark",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None,
        update_time_start: int | None = None,
        update_time_end: int | None = None,
        create_time_start: int | None = None,
        create_time_end: int | None = None,
        sku_list: list[Any] | None = None,
        sku_identifier_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        查询本地产品列表

        API: /erp/sc/routing/data/local_inventory/productList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)
            update_time_start: 更新时间-开始时间【时间戳，单位：秒，左闭右开】 (Optional)
            update_time_end: 更新时间-结束时间【时间戳，单位：秒，左闭右开】 (Optional)
            create_time_start: 创建时间-开始时间【时间戳，单位：秒，左闭右开】 (Optional)
            create_time_end: 创建时间-结束时间【时间戳，单位：秒，左闭右开】 (Optional)
            sku_list: 本地产品sku (Optional)
            sku_identifier_list: sku识别码列表 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length,
            "update_time_start": update_time_start,
            "update_time_end": update_time_end,
            "create_time_start": create_time_start,
            "create_time_end": create_time_end,
            "sku_list": sku_list,
            "sku_identifier_list": sku_identifier_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productList",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询产品属性列表

        API: /erp/sc/routing/storage/attribute/attributeList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/attribute/attributeList",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int,
        length: int
    ) -> dict[str, Any]:
        """
        查询多属性产品列表

        API: /erp/sc/routing/storage/spu/spuList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量 (Required)
            length: 分页长度，上限200 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/spuList",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        sku: str,
        product_name: str,
        spec_pack_list: list[Any],
        sku_identifier: str | None = None,
        picture_list: list[Any] | None = None,
        unit: str | None = None,
        category_id: int | None = None,
        category: str | None = None,
        model: str | None = None,
        brand_id: int | None = None,
        brand: str | None = None,
        open_status: int | None = None,
        status: int | None = None,
        description: str | None = None,
        group_list: list[Any] | None = None,
        cg_opt_uid: int | None = None,
        cg_opt_username: str | None = None,
        product_developer_uid: int | None = None,
        product_developer: str | None = None,
        product_creator_uid: int | None = None,
        product_duty_uids: list[Any] | None = None,
        is_append_product_duty: int | None = None,
        purchase_remark: str | None = None,
        cg_price: str | None = None,
        is_related: int | None = None,
        cg_delivery: int | None = None,
        cg_product_material: str | None = None,
        cg_product_length: str | None = None,
        cg_product_width: str | None = None,
        cg_product_height: str | None = None,
        cg_product_net_weight: str | None = None,
        cg_product_gross_weight: str | None = None,
        cg_package_length: str | None = None,
        cg_package_width: str | None = None,
        cg_package_height: str | None = None,
        cg_box_length: str | None = None,
        cg_box_width: str | None = None,
        cg_box_height: str | None = None,
        cg_box_weight: str | None = None,
        cg_box_pcs: int | None = None,
        bg_customs_export_name: str | None = None,
        bg_export_hs_code: str | None = None,
        bg_customs_import_name: str | None = None,
        currency: str | None = None,
        bg_customs_import_price: str | None = None,
        qc_standard: dict[str, Any] | None = None,
        supplier_quote: list[Any] | None = None,
        special_attr: list[Any] | None = None,
        declaration: dict[str, Any] | None = None,
        clearance: dict[str, Any] | None = None,
        aux_relation_list: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        添加编辑本地产品

        API: /erp/sc/routing/storage/product/set
        Method: POST

        Args:
            access_token: Access token for authentication
            sku: SKU (Required)
            product_name: 品名【添加时必填】 (Required)
            sku_identifier: SKU识别码 (Optional)
            picture_list: 产品图片信息 (Optional)
            unit: 单位（商品单位：套、个、台） (Optional)
            category_id: 分类id，与分类同时存在时，优先取分类id (Optional)
            category: 分类 (Optional)
            model: 型号 (Optional)
            brand_id: 品牌id，与品牌同时存在时，优先取品牌id (Optional)
            brand: 品牌 (Optional)
            open_status: 开启状态：0 停用，1 启用 (Optional)
            status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓 (Optional)
            description: 商品描述 (Optional)
            group_list: 组合商品列表 (Optional)
            cg_opt_uid: 采购：采购员id，与采购员名同时填写时，以采购员id为准 (Optional)
            cg_opt_username: 采购：采购员名 (Optional)
            product_developer_uid: 开发者id，与开发者名称同时填写时，以开发者id为准 (Optional)
            product_developer: 开发者名称 (Optional)
            product_creator_uid: 创建人id，默认API账号id (Optional)
            product_duty_uids: 负责人id (Optional)
            is_append_product_duty: 负责人是否追加创建人：0 否，1 是；默认1，只有编辑SKU时才生效 (Optional)
            purchase_remark: 采购备注 (Optional)
            cg_price: 采购：采购成本（RMB） (Optional)
            is_related: 是否关联单品成本：0 否，1 是 (Optional)
            cg_delivery: 采购：采购交期 (Optional)
            cg_product_material: 采购：商品材质 (Optional)
            cg_product_length: 采购：单品规格-长（CM） (Optional)
            cg_product_width: 采购：单品规格-宽（CM） (Optional)
            cg_product_height: 采购：单品规格-高（CM） (Optional)
            cg_product_net_weight: 采购：单品净重（G） (Optional)
            cg_product_gross_weight: 采购：单品毛重（G） (Optional)
            cg_package_length: 采购：包装规格-长（CM） (Optional)
            cg_package_width: 采购：包装规格-宽（CM） (Optional)
            cg_package_height: 采购：包装规格-高（CM） (Optional)
            cg_box_length: 采购：外箱规格-长（CM） (Optional)
            cg_box_width: 采购：外箱规格-宽（CM） (Optional)
            cg_box_height: 采购：外箱规格-高（CM） (Optional)
            cg_box_weight: 采购：单箱重量（KG） (Optional)
            cg_box_pcs: 采购：单箱数量（包装数量） (Optional)
            bg_customs_export_name: 报关：申报品名(中文) (Optional)
            bg_export_hs_code: 报关：HS Code(中国) (Optional)
            bg_customs_import_name: 报关：申报品名(英文) (Optional)
            currency: 报关：申报金额的币种 (Optional)
            bg_customs_import_price: 报关：申报金额 (Optional)
            qc_standard: 质检标准 (Optional)
            supplier_quote: 供应商报价信息（该参数传空值则清空产品供应商报价） (Optional)
            special_attr: 产品特殊属性：1 含电，2 纯电，3 液体，4 粉末，5 膏体，6 带磁 (Optional)
            declaration: 报关数据 (Optional)
            clearance: 清关数据 (Optional)
            aux_relation_list: 辅料列表 (Optional)
            spec_pack_list: 采购：更多箱规（非默认箱规） (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "sku": sku,
            "product_name": product_name,
            "sku_identifier": sku_identifier,
            "picture_list": picture_list,
            "unit": unit,
            "category_id": category_id,
            "category": category,
            "model": model,
            "brand_id": brand_id,
            "brand": brand,
            "open_status": open_status,
            "status": status,
            "description": description,
            "group_list": group_list,
            "cg_opt_uid": cg_opt_uid,
            "cg_opt_username": cg_opt_username,
            "product_developer_uid": product_developer_uid,
            "product_developer": product_developer,
            "product_creator_uid": product_creator_uid,
            "product_duty_uids": product_duty_uids,
            "is_append_product_duty": is_append_product_duty,
            "purchase_remark": purchase_remark,
            "cg_price": cg_price,
            "is_related": is_related,
            "cg_delivery": cg_delivery,
            "cg_product_material": cg_product_material,
            "cg_product_length": cg_product_length,
            "cg_product_width": cg_product_width,
            "cg_product_height": cg_product_height,
            "cg_product_net_weight": cg_product_net_weight,
            "cg_product_gross_weight": cg_product_gross_weight,
            "cg_package_length": cg_package_length,
            "cg_package_width": cg_package_width,
            "cg_package_height": cg_package_height,
            "cg_box_length": cg_box_length,
            "cg_box_width": cg_box_width,
            "cg_box_height": cg_box_height,
            "cg_box_weight": cg_box_weight,
            "cg_box_pcs": cg_box_pcs,
            "bg_customs_export_name": bg_customs_export_name,
            "bg_export_hs_code": bg_export_hs_code,
            "bg_customs_import_name": bg_customs_import_name,
            "currency": currency,
            "bg_customs_import_price": bg_customs_import_price,
            "qc_standard": qc_standard,
            "supplier_quote": supplier_quote,
            "special_attr": special_attr,
            "declaration": declaration,
            "clearance": clearance,
            "aux_relation_list": aux_relation_list,
            "spec_pack_list": spec_pack_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/set",
            method="POST",
            req_body=params
        )



    async def create_upc(
        self,
        access_token: str,
        commodity_codes: list[Any],
        code_type: str
    ) -> dict[str, Any]:
        """
        创建UPC编码

        API: /listing/publish/api/upc/addCommodityCode
        Method: POST

        Args:
            access_token: Access token for authentication
            commodity_codes: 编码-最多支持两百个 (Required)
            code_type: 编码类型：支持UPC、EAN、ISBN (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_upc(token, ...)
            >>> print(result)
        """
        params = {
            "commodity_codes": commodity_codes,
            "code_type": code_type
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/listing/publish/api/upc/addCommodityCode",
            method="POST",
            req_body=params
        )



    async def get_product_list(
        self,
        access_token: str,
        isRelateMsku: int | None = None,
        length: int | None = None,
        offset: int | None = None,
        productStatus: str | None = None,
        searchField: str | None = None,
        searchValue: str | None = None
    ) -> dict[str, Any]:
        """
        产品管理-查询透明计划商品列表

        API: /basicOpen/product/getTransparencyProductList
        Method: GET

        Args:
            access_token: Access token for authentication
            isRelateMsku: 是否关联MSKU，枚举值：1-是, 2-否 (Optional)
            length: 分页长度，默认20，最大200 (Optional)
            offset: 分页偏移量，默认0 (Optional)
            productStatus: 产品状态，枚举值：all-全部, Enrolled-已注册, In OPR-OPR中, Protected-受保护, NoStatus-无状态 (Optional)
            searchField: 搜索字段，指定搜索的字段名 (Optional)
            searchValue: 搜索值，用于模糊搜索 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product_list(token, ...)
            >>> print(result)
        """
        params = {
            "isRelateMsku": isRelateMsku,
            "length": length,
            "offset": offset,
            "productStatus": productStatus,
            "searchField": searchField,
            "searchValue": searchValue
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/product/getTransparencyProductList",
            method="GET",
            req_body=params
        )



    async def create(
        self,
        access_token: str,
        sku: str,
        product_name: str,
        remark: str,
        cg_price: Any | None = None,
        cg_product_length: Any | None = None,
        cg_product_width: Any | None = None,
        cg_product_height: Any | None = None,
        cg_product_net_weight: Any | None = None,
        supplier_quote: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        添加编辑辅料

        API: /erp/sc/routing/storage/product/setAux
        Method: POST

        Args:
            access_token: Access token for authentication
            sku: SKU (Required)
            product_name: 品名 (Required)
            cg_price: 采购：采购成本（人民币） (Optional)
            cg_product_length: 采购：单品规格-长（CM） (Optional)
            cg_product_width: 采购：单品规格-宽（CM） (Optional)
            cg_product_height: 采购：单品规格-高（CM） (Optional)
            cg_product_net_weight: 采购：单品净重（G） (Optional)
            supplier_quote: 供应商报价信息（不传该参数则清空产品供应商报价） (Optional)
            remark: 辅料描述 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create(token, ...)
            >>> print(result)
        """
        params = {
            "sku": sku,
            "product_name": product_name,
            "cg_price": cg_price,
            "cg_product_length": cg_product_length,
            "cg_product_width": cg_product_width,
            "cg_product_height": cg_product_height,
            "cg_product_net_weight": cg_product_net_weight,
            "supplier_quote": supplier_quote,
            "remark": remark
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/setAux",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询捆绑产品关系列表

        API: /erp/sc/routing/data/local_inventory/bundledProductList
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/bundledProductList",
            method="POST",
            req_body=params
        )



    async def product(  # noqa: F811
        self,
        access_token: str,
        product_ids: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        产品启用、禁用

        API: /basicOpen/product/productManager/product/operate/batch
        Method: POST

        Args:
            access_token: Access token for authentication
            product_ids: 产品id (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.product(token, ...)
            >>> print(result)
        """
        params = {
            "product_ids": product_ids
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/product/productManager/product/operate/batch",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        添加编辑产品分类

        API: /erp/sc/routing/storage/category/set
        Method: POST

        Args:
            access_token: Access token for authentication
            data: 请求数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/category/set",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询产品品牌列表

        API: /erp/sc/data/local_inventory/brand
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/data/local_inventory/brand",
            method="POST",
            req_body=params
        )



    async def get_productlist(  # noqa: F811
        self,
        access_token: str,
        offset: int | None = None,
        length: int | None = None
    ) -> dict[str, Any]:
        """
        查询产品分类列表

        API: /erp/sc/routing/data/local_inventory/category
        Method: POST

        Args:
            access_token: Access token for authentication
            offset: 分页偏移量，默认0 (Optional)
            length: 分页长度，默认1000，上限1000 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_productlist(token, ...)
            >>> print(result)
        """
        params = {
            "offset": offset,
            "length": length
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/category",
            method="POST",
            req_body=params
        )



    async def get(
        self,
        access_token: str,
        businessId: Any,
        endTime: str,
        startTime: str,
        page: int | None = None,
        size: int | None = None
    ) -> dict[str, Any]:
        """
        查询操作日志

        API: /basicOpen/product/getPagingLogLists
        Method: GET

        Args:
            access_token: Access token for authentication
            businessId: businessId，对应查询本地产品列表data>>id字段 (Required)
            endTime: 结束时间 (Required)
            startTime: 开始时间 (Required)
            page: 页码 (Optional)
            size: 每页大小 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get(token, ...)
            >>> print(result)
        """
        params = {
            "businessId": businessId,
            "endTime": endTime,
            "startTime": startTime,
            "page": page,
            "size": size
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/basicOpen/product/getPagingLogLists",
            method="GET",
            req_body=params
        )



    async def product(  # noqa: F811
        self,
        access_token: str,
        sku: str,
        picture_list: list[Any]
    ) -> dict[str, Any]:
        """
        上传本地产品图片

        API: /erp/sc/routing/storage/product/uploadPictures
        Method: POST

        Args:
            access_token: Access token for authentication
            sku: 本地产品SKU (Required)
            picture_list: 产品图片信息 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.product(token, ...)
            >>> print(result)
        """
        params = {
            "sku": sku,
            "picture_list": picture_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/uploadPictures",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        spu: str,
        spu_name: str,
        sku_list: list[Any],
        aux_relation_list: list[Any],
        model: str | None = None,
        unit: str | None = None,
        status: int | None = None,
        cid: int | None = None,
        bid: int | None = None,
        create_uid: int | None = None,
        developer_uid: int | None = None,
        product_duty_uids: list[Any] | None = None,
        description: str | None = None,
        use_spu_template: int | None = None,
        purchase_info: dict[str, Any] | None = None,
        logistics: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """
        添加编辑多属性产品

        API: /erp/sc/routing/storage/spu/set
        Method: POST

        Args:
            access_token: Access token for authentication
            spu: SPU（添加时必填） (Required)
            spu_name: 款名（添加时必填） (Required)
            model: 型号 (Optional)
            unit: 单位 (Optional)
            status: 状态【默认1】：0 停售，1 在售，2 开发中，3 清仓 (Optional)
            cid: 分类id (Optional)
            bid: 品牌id (Optional)
            create_uid: 创建人id (Optional)
            developer_uid: 开发人id (Optional)
            product_duty_uids: 产品负责人id (Optional)
            description: 产品描述 (Optional)
            use_spu_template: 是否应用SPU信息至新生成的SKU：0 否，1 是 (Optional)
            sku_list: 产品列表【提交的sku不存在时系统会自动创建】 (Required)
            purchase_info: 采购相关信息 (Optional)
            logistics: 物流报关相关信息 (Optional)
            aux_relation_list: 辅料列表 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "spu": spu,
            "spu_name": spu_name,
            "model": model,
            "unit": unit,
            "status": status,
            "cid": cid,
            "bid": bid,
            "create_uid": create_uid,
            "developer_uid": developer_uid,
            "product_duty_uids": product_duty_uids,
            "description": description,
            "use_spu_template": use_spu_template,
            "sku_list": sku_list,
            "purchase_info": purchase_info,
            "logistics": logistics,
            "aux_relation_list": aux_relation_list
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/set",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        attr_name: str,
        attr_values: list[Any],
        pa_id: int | None = None
    ) -> dict[str, Any]:
        """
        添加编辑产品属性

        API: /erp/sc/routing/storage/attribute/set
        Method: POST

        Args:
            access_token: Access token for authentication
            pa_id: 领星属性id (Optional)
            attr_name: 属性名 (Required)
            attr_values: 属性值数组 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "pa_id": pa_id,
            "attr_name": attr_name,
            "attr_values": attr_values
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/attribute/set",
            method="POST",
            req_body=params
        )



    async def create_product(  # noqa: F811
        self,
        access_token: str,
        data: list[Any]
    ) -> dict[str, Any]:
        """
        添加编辑产品品牌

        API: /erp/sc/storage/brand/set
        Method: POST

        Args:
            access_token: Access token for authentication
            data: 请求数据 (Required)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.create_product(token, ...)
            >>> print(result)
        """
        params = {
            "data": data
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/storage/brand/set",
            method="POST",
            req_body=params
        )



    async def get_product(  # noqa: F811
        self,
        access_token: str,
        productIds: list[Any] | None = None,
        skus: list[Any] | None = None,
        sku_identifiers: list[Any] | None = None
    ) -> dict[str, Any]:
        """
        批量查询本地产品详情

        API: /erp/sc/routing/data/local_inventory/batchGetProductInfo
        Method: GET

        Args:
            access_token: Access token for authentication
            productIds: 产品id，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】 (Optional)
            skus: 产品SKU，上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】 (Optional)
            sku_identifiers: SKU识别码，上限100个上限100个【产品id 、 产品sku 、SKU识别码 三选一必填】 (Optional)

        Returns:
            Dict containing API response

        Example:
            >>> result = await client.get_product(token, ...)
            >>> print(result)
        """
        params = {
            "productIds": productIds,
            "skus": skus,
            "sku_identifiers": sku_identifiers
        }

        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}

        return await self._openapi.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/batchGetProductInfo",
            method="GET",
            req_body=params
        )


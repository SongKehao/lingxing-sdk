"""产品管理API端点"""
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase


class ProductEndpoints:

    def __init__(self, client: 'OpenApiBase'):
        self._client = client

    async def get_products(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 1000,
        update_time_start: int | None = None,
        update_time_end: int | None = None,
        create_time_start: int | None = None,
        create_time_end: int | None = None,
        sku_list: list[str] | None = None,
        sku_identifier_list: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """查询本地产品列表

        POST /erp/sc/routing/data/local_inventory/productList

        对应系统【产品】>【产品管理】数据

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000，上限1000
            update_time_start: 更新时间-开始时间（时间戳，单位：秒，左闭右开）
            update_time_end: 更新时间-结束时间（时间戳，单位：秒，左闭右开）
            create_time_start: 创建时间-开始时间（时间戳，单位：秒，左闭右开）
            create_time_end: 创建时间-结束时间（时间戳，单位：秒，左闭右开）
            sku_list: 本地产品SKU列表
            sku_identifier_list: SKU识别码列表

        Returns:
            产品列表:
            [
                {
                    "id": 17835,              # 本地产品id
                    "cid": 0,                 # 类别id
                    "category_name": "",      # 类别
                    "bid": 0,                 # 品牌id
                    "brand_name": "",         # 品牌
                    "sku": "SKU001",          # 本地产品SKU
                    "sku_identifier": "",     # SKU识别码
                    "product_name": "",       # 品名
                    "pic_url": "",            # 图片链接
                    "ps_id": 12,              # SPU唯一id
                    "spu": "spu-123",         # SPU
                    "cg_delivery": 555,       # 采购：交期
                    "cg_transport_costs": "0.00",  # 采购：运输成本
                    "purchase_remark": "",    # 采购备注
                    "cg_price": "10.0000",    # 采购成本（人民币）
                    "open_status": 1,         # 产品开启状态：0-停用，1-启用
                    "status": 1,              # 状态：0停售，1在售，2开发中，3清仓
                    "status_text": "在售",    # 状态文本
                    "is_combo": 0,            # 是否为组合产品：0否，1是
                    "create_time": 1675945140,  # 创建时间（秒）
                    "update_time": 1675945635,  # 更新时间（秒）
                    "global_tags": [],        # 产品标签信息
                    "product_developer_uid": 0,  # 开发人员id
                    "product_developer": "",     # 开发人员名称
                    "cg_opt_uid": 0,             # 采购员id
                    "cg_opt_username": "",       # 采购员名称
                    "supplier_quote": [],        # 供应商报价信息
                    "custom_fields": [],         # 自定义字段
                    "attribute": []              # 产品属性
                }
            ]
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        if update_time_start is not None:
            req_body["update_time_start"] = update_time_start
        if update_time_end is not None:
            req_body["update_time_end"] = update_time_end
        if create_time_start is not None:
            req_body["create_time_start"] = create_time_start
        if create_time_end is not None:
            req_body["create_time_end"] = create_time_end
        if sku_list:
            req_body["sku_list"] = sku_list
        if sku_identifier_list:
            req_body["sku_identifier_list"] = sku_identifier_list

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productList",
            method="POST",
            req_body=req_body
        )

        # 返回产品列表
        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_product_info(self, access_token: str, product_id: int) -> dict[str, Any]:
        """查询产品详情

        POST /erp/sc/routing/data/local_inventory/productInfo

        Args:
            access_token: 访问令牌
            product_id: 产品ID

        Returns:
            产品详细信息字典
        """
        req_body = {"id": product_id}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productInfo",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def get_categories(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 100,
        parent_id: int | None = None
    ) -> list[dict[str, Any]]:
        """查询产品分类

        POST /erp/sc/routing/data/local_inventory/category

        Args:
            access_token: 访问令牌
            page: 页码，默认1
            page_size: 每页数量，默认100
            parent_id: 父分类ID，用于获取子分类

        Returns:
            分类列表
        """
        req_body = {
            "page": page,
            "page_size": page_size,
        }

        if parent_id is not None:
            req_body["parent_id"] = parent_id

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/category",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_brands(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        keyword: str | None = None
    ) -> list[dict[str, Any]]:
        """查询产品品牌

        POST /erp/sc/data/local_inventory/brand

        Args:
            access_token: 访问令牌
            offset: 偏移量，用于分页，默认0
            length: 返回数量，默认100
            keyword: 关键词，用于搜索品牌名称

        Returns:
            品牌列表
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        if keyword:
            req_body["keyword"] = keyword

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/local_inventory/brand",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_attributes(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 100,
        category_id: int | None = None
    ) -> list[dict[str, Any]]:
        """查询产品属性

        POST /erp/sc/data/local_inventory/attribute

        Args:
            access_token: 访问令牌
            offset: 偏移量，用于分页，默认0
            length: 返回数量，默认100
            category_id: 分类ID，用于获取特定分类的属性

        Returns:
            属性列表
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        if category_id is not None:
            req_body["category_id"] = category_id

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/local_inventory/attribute",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_product_by_sku(self, access_token: str, sku: str) -> dict[str, Any] | None:
        """根据SKU获取产品信息

        便捷方法，通过SKU查询单个产品。

        Args:
            access_token: 访问令牌
            sku: 产品SKU

        Returns:
            产品信息字典，如果不存在返回None
        """
        products = await self.get_products(access_token=access_token, sku_list=[sku], length=1)
        return products[0] if products else None

    # ==================== 批量查询 ====================

    async def batch_get_product_info(
        self,
        access_token: str,
        product_ids: list[int] | None = None,
        skus: list[str] | None = None,
        sku_identifiers: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """批量查询本地产品详情

        POST /erp/sc/routing/data/local_inventory/batchGetProductInfo

        Args:
            access_token: 访问令牌
            product_ids: 产品ID列表，上限100个
            skus: 产品SKU列表，上限100个
            sku_identifiers: SKU识别码列表，上限100个

        Returns:
            产品详情列表
        """
        req_body = {}

        if product_ids:
            req_body["productIds"] = product_ids
        if skus:
            req_body["skus"] = skus
        if sku_identifiers:
            req_body["sku_identifiers"] = sku_identifiers

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/batchGetProductInfo",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    # ==================== 产品操作 ====================

    async def set_product(
        self,
        access_token: str,
        sku: str,
        product_name: str,
        **kwargs
    ) -> dict[str, Any]:
        """添加/编辑本地产品

        POST /erp/sc/routing/storage/product/set

        Args:
            access_token: 访问令牌
            sku: SKU
            product_name: 品名（添加时必填）
            **kwargs: 其他可选参数
                - sku_identifier: SKU识别码
                - picture_list: 产品图片信息
                - unit: 单位
                - category_id: 分类id
                - category: 分类
                - model: 型号
                - brand_id: 品牌id
                - brand: 品牌
                - open_status: 开启状态：0 停用，1 启用
                - status: 状态：0 停售，1 在售，2 开发中，3 清仓
                - description: 商品描述
                - group_list: 组合商品列表
                - cg_opt_uid: 采购员id
                - cg_opt_username: 采购员名
                - product_developer_uid: 开发者id
                - product_developer: 开发者名称
                - purchase_remark: 采购备注
                - cg_price: 采购成本（RMB）
                - cg_delivery: 采购交期
                - supplier_quote: 供应商报价信息
                - special_attr: 产品特殊属性
                - declaration: 报关数据
                - clearance: 清关数据
                - custom_fields: 自定义字段

        Returns:
            包含 product_id, sku, sku_identifier 的字典
        """
        req_body = {
            "sku": sku,
            "product_name": product_name,
        }
        req_body.update(kwargs)

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/set",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def batch_operate_product(
        self,
        access_token: str,
        product_ids: list[int],
        batch_status: str,
    ) -> dict[str, Any]:
        """产品启用/禁用

        POST /basicOpen/product/productManager/product/operate/batch

        Args:
            access_token: 访问令牌
            product_ids: 产品ID列表
            batch_status: 状态：Enable 启用，Disable 禁用

        Returns:
            响应数据
        """
        req_body = {
            "product_ids": product_ids,
            "batch_status": batch_status,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/basicOpen/product/productManager/product/operate/batch",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 多属性产品 ====================

    async def get_spu_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> list[dict[str, Any]]:
        """查询多属性产品列表

        POST /erp/sc/routing/storage/spu/spuList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，上限200

        Returns:
            多属性产品列表
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/spuList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_spu_info(
        self,
        access_token: str,
        ps_id: int | None = None,
        spu: str | None = None,
    ) -> dict[str, Any]:
        """查询多属性产品详情

        POST /erp/sc/routing/storage/spu/info

        Args:
            access_token: 访问令牌
            ps_id: SPU唯一id（ps_id 与 spu 二选一必填）
            spu: SPU

        Returns:
            多属性产品详情
        """
        req_body = {}
        if ps_id is not None:
            req_body["ps_id"] = ps_id
        if spu:
            req_body["spu"] = spu

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/info",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def set_spu(
        self,
        access_token: str,
        spu: str,
        spu_name: str,
        sku_list: list[dict[str, Any]],
        **kwargs
    ) -> dict[str, Any]:
        """添加/编辑多属性产品

        POST /erp/sc/routing/storage/spu/set

        Args:
            access_token: 访问令牌
            spu: SPU（添加时必填）
            spu_name: 款名（添加时必填）
            sku_list: 产品列表
                - sku: 本地产品SKU
                - product_name: 产品名称
                - attribute: 属性列表
                - picture_list: 产品图片信息
            **kwargs: 其他可选参数
                - model: 型号
                - unit: 单位
                - status: 状态
                - cid: 分类id
                - bid: 品牌id
                - developer_uid: 开发人id
                - purchase_info: 采购相关信息
                - logistics: 物流报关相关信息

        Returns:
            包含 ps_id 和 sku_list 的字典
        """
        req_body = {
            "spu": spu,
            "spu_name": spu_name,
            "sku_list": sku_list,
        }
        req_body.update(kwargs)

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/spu/set",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 产品标签 ====================

    async def get_product_tags(
        self,
        access_token: str,
    ) -> list[dict[str, Any]]:
        """查询产品标签

        GET /label/operation/v1/label/product/list

        Args:
            access_token: 访问令牌

        Returns:
            标签列表
        """
        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/list",
            method="GET",
            req_body={}
        )

        data = resp_result.data if isinstance(resp_result.data, dict) else {}
        return data.get("list", [])

    async def create_product_tag(
        self,
        access_token: str,
        label: str,
    ) -> dict[str, Any]:
        """创建产品标签

        POST /label/operation/v1/label/product/create

        Args:
            access_token: 访问令牌
            label: 标签名称，最长15个字符，中间不能有空格

        Returns:
            包含 label_name 和 label_id 的字典
        """
        req_body = {"label": label}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/create",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def mark_product_tags(
        self,
        access_token: str,
        detail_list: list[dict[str, Any]],
        mark_type: int = 1,
    ) -> dict[str, Any]:
        """标记产品标签

        POST /label/operation/v1/label/product/mark

        Args:
            access_token: 访问令牌
            detail_list: 标签信息，上限200
                - sku: 产品SKU
                - label_list: 标签名称列表，上限10
            mark_type: 操作类型：1 追加，2 覆盖

        Returns:
            响应数据
        """
        req_body = {
            "type": mark_type,
            "detail_list": detail_list,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/mark",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def unmark_product_tags(
        self,
        access_token: str,
        detail_list: list[dict[str, Any]],
        unmark_type: int = 1,
    ) -> dict[str, Any]:
        """删除产品标签

        POST /label/operation/v1/label/product/unmarkLabel

        Args:
            access_token: 访问令牌
            detail_list: 标签信息，上限200
                - sku: 本地产品sku
                - label_list: 标签名称列表
            unmark_type: 操作类型
                - 1: 删除SKU指定的标签
                - 2: 删除SKU全部的标签（label_list为空数组即可）

        Returns:
            响应数据
        """
        req_body = {
            "type": unmark_type,
            "detail_list": detail_list,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/label/operation/v1/label/product/unmarkLabel",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 分类/品牌/属性 ====================

    async def set_category(
        self,
        access_token: str,
        data: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """添加/编辑产品分类

        POST /erp/sc/routing/storage/category/set

        Args:
            access_token: 访问令牌
            data: 分类数据列表
                - id: 为空时新增，不为空时编辑
                - parent_cid: 父级分类id
                - title: 分类名称
                - category_code: 分类简码

        Returns:
            成功的数据列表
        """
        req_body = {"data": data}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/category/set",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def set_brand(
        self,
        access_token: str,
        data: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """添加/编辑产品品牌

        POST /erp/sc/storage/brand/set

        Args:
            access_token: 访问令牌
            data: 品牌数据列表
                - id: 为空时新增，不为空时编辑
                - title: 品牌名称
                - brand_code: 品牌简码

        Returns:
            成功的数据列表
        """
        req_body = {"data": data}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/storage/brand/set",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def get_attribute_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """查询产品属性列表

        POST /erp/sc/routing/storage/attribute/attributeList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，上限200

        Returns:
            包含 total 和 list 的字典
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/attribute/attributeList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def set_attribute(
        self,
        access_token: str,
        attr_name: str,
        attr_values: list[dict[str, Any]],
        pa_id: int | None = None,
    ) -> list[dict[str, Any]]:
        """添加/编辑产品属性

        POST /erp/sc/routing/storage/attribute/set

        注意：
        1. 属性数据为覆盖式操作
        2. 属性值有关联SPU时不允许编辑、删除
        3. 如需新增属性值，入参为已存在属性值 + 新增属性值

        Args:
            access_token: 访问令牌
            attr_name: 属性名
            attr_values: 属性值数组
                - pai_id: 领星属性值id
                - attr_value: 属性值名称
            pa_id: 领星属性id（不传视为新增属性）

        Returns:
            包含 pa_id 和 pai_id 的列表
        """
        req_body = {
            "attr_name": attr_name,
            "attr_values": attr_values,
        }
        if pa_id is not None:
            req_body["pa_id"] = pa_id

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/attribute/set",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    # ==================== 图片上传 ====================

    async def upload_product_pictures(
        self,
        access_token: str,
        sku: str,
        picture_list: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """上传本地产品图片

        POST /erp/sc/routing/storage/product/uploadPictures

        Args:
            access_token: 访问令牌
            sku: 本地产品SKU
            picture_list: 产品图片信息
                - pic_url: 产品图片链接
                - is_primary: 是否产品主图：0 否，1 是

        Returns:
            包含 sku 和 picture_list 的字典
        """
        req_body = {
            "sku": sku,
            "picture_list": picture_list,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/uploadPictures",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 操作日志 ====================

    async def get_operation_logs(
        self,
        access_token: str,
        business_id: int,
        start_time: str,
        end_time: str,
        page: int = 1,
        size: int = 20,
    ) -> list[dict[str, Any]]:
        """查询操作日志

        POST /basicOpen/product/getPagingLogLists

        Args:
            access_token: 访问令牌
            business_id: businessId，对应查询本地产品列表data>>id字段
            start_time: 开始时间
            end_time: 结束时间
            page: 页码，默认1
            size: 每页大小，默认20

        Returns:
            操作日志列表
        """
        req_body = {
            "businessId": business_id,
            "startTime": start_time,
            "endTime": end_time,
            "page": page,
            "size": size,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/basicOpen/product/getPagingLogLists",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    # ==================== 辅料管理 ====================

    async def get_aux_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> list[dict[str, Any]]:
        """查询产品辅料列表

        POST /erp/sc/routing/data/local_inventory/productAuxList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000，上限1000

        Returns:
            辅料列表
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/productAuxList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def set_aux(
        self,
        access_token: str,
        sku: str,
        product_name: str,
        remark: str = "",
        **kwargs
    ) -> dict[str, Any]:
        """添加/编辑辅料

        POST /erp/sc/routing/storage/product/setAux

        Args:
            access_token: 访问令牌
            sku: SKU
            product_name: 品名
            remark: 辅料描述
            **kwargs: 其他可选参数
                - cg_price: 采购成本（人民币）
                - cg_product_length: 单品规格-长（CM）
                - cg_product_width: 单品规格-宽（CM）
                - cg_product_height: 单品规格-高（CM）
                - cg_product_net_weight: 单品净重（G）
                - supplier_quote: 供应商报价信息

        Returns:
            包含 product_id 的字典
        """
        req_body = {
            "sku": sku,
            "product_name": product_name,
            "remark": remark,
        }
        req_body.update(kwargs)

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/setAux",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 捆绑产品 ====================

    async def get_bundled_product_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> list[dict[str, Any]]:
        """查询捆绑产品关系列表

        POST /erp/sc/routing/data/local_inventory/bundledProductList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000，上限1000

        Returns:
            捆绑产品列表
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/data/local_inventory/bundledProductList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else resp_result.data.get("data", [])

    async def set_bundled_product(
        self,
        access_token: str,
        sku: str,
        product_name: str,
        **kwargs
    ) -> dict[str, Any]:
        """添加/编辑捆绑产品

        POST /erp/sc/routing/storage/product/setBundled

        Args:
            access_token: 访问令牌
            sku: SKU（添加时必填）
            product_name: 品名（添加时必填）
            **kwargs: 其他可选参数
                - picture_list: 产品图片信息
                - model: 型号
                - unit: 单位
                - status: 状态
                - category_id: 分类id
                - category: 分类
                - brand_id: 品牌id
                - brand: 品牌
                - product_developer: 开发者名称
                - product_developer_uid: 开发者id
                - product_duty_uids: 负责人id列表
                - description: 商品描述
                - group_list: 组合商品列表（捆绑产品子产品的总数量要大于1）

        Returns:
            包含 product_id 的字典
        """
        req_body = {
            "sku": sku,
            "product_name": product_name,
        }
        req_body.update(kwargs)

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/routing/storage/product/setBundled",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== 透明计划 ====================

    async def get_transparency_product_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
        product_status: str | None = None,
        is_relate_msku: int | None = None,
        search_field: str | None = None,
        search_value: str | None = None,
    ) -> dict[str, Any]:
        """查询透明计划商品列表

        POST /basicOpen/product/getTransparencyProductList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20，最大200
            product_status: 产品状态，枚举值：all-全部, Enrolled-已注册, In OPR-OPR中, Protected-受保护, NoStatus-无状态
            is_relate_msku: 是否关联MSKU，枚举值：1-是, 2-否
            search_field: 搜索字段
            search_value: 搜索值

        Returns:
            包含 pageList 和 total 的字典
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        if product_status:
            req_body["productStatus"] = product_status
        if is_relate_msku is not None:
            req_body["isRelateMsku"] = is_relate_msku
        if search_field:
            req_body["searchField"] = search_field
        if search_value:
            req_body["searchValue"] = search_value

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/basicOpen/product/getTransparencyProductList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    # ==================== UPC编码 ====================

    async def get_upc_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> dict[str, Any]:
        """获取UPC编码列表

        POST /listing/publish/api/upc/upcList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20

        Returns:
            包含 total 和 list 的字典
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/listing/publish/api/upc/upcList",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, dict) else {}

    async def create_upc(
        self,
        access_token: str,
        commodity_codes: list[str],
        code_type: str,
    ) -> list[int]:
        """创建UPC编码

        POST /listing/publish/api/upc/addCommodityCode

        Args:
            access_token: 访问令牌
            commodity_codes: 编码列表，最多支持200个
            code_type: 编码类型：支持UPC、EAN、ISBN

        Returns:
            编码ID列表
        """
        req_body = {
            "commodity_codes": commodity_codes,
            "code_type": code_type,
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/listing/publish/api/upc/addCommodityCode",
            method="POST",
            req_body=req_body
        )

        return resp_result.data if isinstance(resp_result.data, list) else []


__all__ = ["ProductEndpoints"]

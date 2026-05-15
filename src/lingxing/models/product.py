"""Auto-generated Pydantic models from API fixtures."""

from typing import Optional
from pydantic import Field

from .common import LingXingModel


class BrandItem(LingXingModel):
    """Product/Brand 响应数据项."""

    bid: Optional[int] = None
    brand_code: Optional[str] = None
    title: Optional[str] = None

class CategoryItem(LingXingModel):
    """Product/Category 响应数据项."""

    category_code: Optional[str] = None
    cid: Optional[int] = None
    parent_cid: Optional[int] = None
    title: Optional[str] = None

class ProductListsItem(LingXingModel):
    """Product/ProductLists 响应数据项."""

    attribute: Optional[list] = None
    aux_relation_list: Optional[list] = None
    bid: Optional[int] = None
    brand_name: Optional[str] = None
    category_name: Optional[str] = None
    cg_delivery: Optional[int] = None
    cg_opt_uid: Optional[int] = None
    cg_opt_username: Optional[str] = None
    cg_price: Optional[str] = None
    cg_transport_costs: Optional[str] = None
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

class UpcListData(LingXingModel):
    """Product/UpcList 响应数据项."""

    list: Optional[list] = None
    total: Optional[int] = None

class AttributeListData(LingXingModel):
    """Product/attributeList 响应数据项."""

    list: Optional[list] = None
    total: Optional[int] = None

"""Pydantic models for Product APIs."""
from typing import Optional

from .common import LingXingModel


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

class AttributeListItem(LingXingModel):
    """Response item for attributeList."""

    list: Optional[list] = None
    total: Optional[int] = None

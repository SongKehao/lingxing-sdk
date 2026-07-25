"""Request models for FBALimit APIs (auto-generated from API docs)."""

from typing import Optional

from ..common import LingXingModel


class FBALimitGetIpiInfoRequest(LingXingModel):
    """Request for 查询IPI信息.

    POST /erp/sc/routing/fbaLimit/restock/getIpiInfo
    """

    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20
    seller_ids: Optional[str] = (
        None  # 亚马逊店铺id，多个使用英文逗号分隔 ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    )
    mids: Optional[str] = None  # 站点id，多个使用英文逗号分隔
    sids: Optional[str] = None  # 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】


class FBALimitReplenishmentrestrictionlistRequest(LingXingModel):
    """Request for 查询补货限制列表.

    POST /basicOpen/openapi/replenishmentRestriction/page/list
    """

    storage_type: str  # 仓储类型： Standard 标准 Oversize 大件 Apparel 服装 Footwear 鞋靴 ExtraLarge 超大
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    sids: Optional[str] = None  # 店铺id，多个用英文逗号隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】

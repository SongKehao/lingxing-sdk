"""FBA库存限制 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint


class RestockingLimitEndpoints(BaseEndpoint):
    """领星FBA库存限制 API (2个接口)."""

    async def get_ipi_info(self, **kwargs) -> list | dict:
        """查询IPI信息.

POST /erp/sc/routing/fbaLimit/restock/getIpiInfo

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int.
    seller_ids: 亚马逊店铺id，多个使用英文逗号分隔 ,对应查询亚马逊店铺列表接口对应字段【seller_id】, string.
    mids: 站点id，多个使用英文逗号分隔, string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string."""
        resp = await self._post("/erp/sc/routing/fbaLimit/restock/getIpiInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def replenishment_restriction_list(self, **kwargs) -> list | dict:
        """查询补货限制列表.

POST /basicOpen/openapi/replenishmentRestriction/page/list

Args:
    storage_type: 仓储类型： Standard 标准 Oversize 大件 Apparel 服装 Footwear 鞋靴 ExtraLarge 超大 (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    sids: 店铺id，多个用英文逗号隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】, string."""
        resp = await self._post("/basicOpen/openapi/replenishmentRestriction/page/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

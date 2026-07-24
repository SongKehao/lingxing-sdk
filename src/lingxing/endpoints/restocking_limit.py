"""FBA库存限制 API endpoints."""

from __future__ import annotations

from ..models.responses.fba_limit import (
    FbalimitRestockGetipiinfoResponse,
    ReplenishmentrestrictionPageListResponse,
)
from ._base import BaseEndpoint


class RestockingLimitEndpoints(BaseEndpoint):
    """领星FBA库存限制 API (2个接口)."""

    async def get_ipi_info(
        self, offset: int = None, length: int = None, seller_ids: str = None, mids: str = None, sids: str = None
    ) -> list[FbalimitRestockGetipiinfoResponse]:
        """查询IPI信息.

        POST /erp/sc/routing/fbaLimit/restock/getIpiInfo

        Args:
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20, int.
            seller_ids: 亚马逊店铺id，多个使用英文逗号分隔 ,对应查询亚马逊店铺列表接口对应字段【seller_id】, string.
            mids: 站点id，多个使用英文逗号分隔, string.
            sids: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】, string."""
        resp = await self._post(
            "/erp/sc/routing/fbaLimit/restock/getIpiInfo",
            {
                k: v
                for k, v in {
                    "offset": offset,
                    "length": length,
                    "seller_ids": seller_ids,
                    "mids": mids,
                    "sids": sids,
                }.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, FbalimitRestockGetipiinfoResponse)

    async def replenishment_restriction_list(
        self, storage_type: str = None, offset: int = None, length: int = None, sids: str = None
    ) -> list[ReplenishmentrestrictionPageListResponse]:
        """查询补货限制列表.

        POST /basicOpen/openapi/replenishmentRestriction/page/list

        Args:
            storage_type: 仓储类型： Standard 标准 Oversize 大件 Apparel 服装 Footwear 鞋靴 ExtraLarge 超大 (required), string.
            offset: 分页偏移量，默认0, int.
            length: 分页长度，默认20，上限200, int.
            sids: 店铺id，多个用英文逗号隔开 ，对应查询亚马逊店铺列表接口对应字段【sid】, string."""
        resp = await self._post(
            "/basicOpen/openapi/replenishmentRestriction/page/list",
            {
                k: v
                for k, v in {"storage_type": storage_type, "offset": offset, "length": length, "sids": sids}.items()
                if v is not None
            },
        )
        return self._parse_list(resp.data, ReplenishmentrestrictionPageListResponse)

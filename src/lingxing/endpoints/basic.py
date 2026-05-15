"""基础数据 API - 店铺、账户、市场、汇率等基础信息查询."""
from __future__ import annotations

from ._base import BaseEndpoint
from ..models.basic import (
    AccoutListsItem,
    AllMarketplaceItem,
    ConceptSellerListsItem,
    SellerListsItem,
)


class BasicEndpoints(BaseEndpoint):
    """领星基础数据 API (10个接口)."""

    # ── 只读接口 ──

    async def list_accounts(self) -> list[AccoutListsItem]:
        """获取ERP用户信息列表.

        POST /erp/sc/data/account/lists
        """
        resp = await self._post("/erp/sc/data/account/lists")
        return self._parse_list(resp.data, AccoutListsItem)

    async def list_sellers(self) -> list[SellerListsItem]:
        """获取店铺列表.

        POST /erp/sc/data/seller/lists
        返回所有关联店铺信息（含店铺ID、名称、市场等）.
        """
        resp = await self._post("/erp/sc/data/seller/lists")
        return self._parse_list(resp.data, SellerListsItem)

    async def list_concept_sellers(self) -> list[ConceptSellerListsItem]:
        """获取概念店铺列表.

        POST /erp/sc/data/seller/conceptLists
        """
        resp = await self._post("/erp/sc/data/seller/conceptLists")
        return self._parse_list(resp.data, ConceptSellerListsItem)

    async def list_marketplaces(self) -> list[AllMarketplaceItem]:
        """获取所有亚马逊市场列表.

        POST /erp/sc/data/seller/allMarketplace
        返回市场代码、国家、区域等信息.
        """
        resp = await self._post("/erp/sc/data/seller/allMarketplace")
        return self._parse_list(resp.data, AllMarketplaceItem)

    async def list_world_states(self, **kwargs) -> list:
        """获取国家地区列表.

        POST /erp/sc/data/worldState/lists

        Keyword Args:
            country_code: 国家代码（如 "CN", "US"）
        """
        resp = await self._post("/erp/sc/data/worldState/lists", kwargs)
        return self._parse_list(resp.data, dict)

    async def get_currency_rate(self, **kwargs) -> dict:
        """获取汇率信息.

        POST /erp/sc/routing/finance/currency/currencyMonth

        Keyword Args:
            month: 月份（如 "2026-05"）
        """
        resp = await self._post("/erp/sc/routing/finance/currency/currencyMonth", kwargs)
        return resp.data or {}

    async def get_profit_state_list(self, **kwargs) -> list:
        """获取利润报表状态列表.

        POST /basicOpen/multiplatform/profit/report/stateList
        """
        resp = await self._post("/basicOpen/multiplatform/profit/report/stateList", kwargs)
        return self._parse_list(resp.data, dict)

    # ── 写操作（慎用）──

    async def batch_rename_seller(self, sellers: list[dict]) -> dict:
        """批量修改店铺名称.

        POST /erp/sc/data/seller/batchEditSellerName

        Args:
            sellers: 店铺改名列表 [{"sid": 123, "name": "新名称"}, ...]
        """
        resp = await self._post("/erp/sc/data/seller/batchEditSellerName", {"sellers": sellers})
        return resp.data or {}

    async def update_exchange_rate(self, **kwargs) -> dict:
        """修改汇率.

        POST /basicOpen/settings/exchangeRate/update

        Keyword Args:
            currency: 货币代码
            rate: 汇率
            month: 月份
        """
        resp = await self._post("/basicOpen/settings/exchangeRate/update", kwargs)
        return resp.data or {}

    async def download_attachment(self, **kwargs) -> dict:
        """下载附件.

        POST /erp/sc/routing/common/file/download
        """
        resp = await self._post("/erp/sc/routing/common/file/download", kwargs)
        return resp.data or {}

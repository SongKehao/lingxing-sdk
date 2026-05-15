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
        """
        查询ERP用户信息列表.

        POST /erp/sc/data/account/lists
        """
        resp = await self._post("/erp/sc/data/account/lists")
        return self._parse_list(resp.data, AccoutListsItem)

    async def list_sellers(self) -> list[SellerListsItem]:
        """
        查询亚马逊店铺列表.

        POST /erp/sc/data/seller/lists
        """
        resp = await self._post("/erp/sc/data/seller/lists")
        return self._parse_list(resp.data, SellerListsItem)

    async def list_concept_sellers(self) -> list[ConceptSellerListsItem]:
        """
        查询亚马逊概念店铺列表.

        POST /erp/sc/data/seller/conceptLists
        """
        resp = await self._post("/erp/sc/data/seller/conceptLists")
        return self._parse_list(resp.data, ConceptSellerListsItem)

    async def list_marketplaces(self) -> list[AllMarketplaceItem]:
        """
        查询亚马逊市场列表.

        POST /erp/sc/data/seller/allMarketplace
        """
        resp = await self._post("/erp/sc/data/seller/allMarketplace")
        return self._parse_list(resp.data, AllMarketplaceItem)

    async def list_world_states(self, **kwargs) -> list:
        """
        查询亚马逊国家下地区列表.

        POST /erp/sc/data/worldState/lists

        Args:
            country_code: 国家code，查询亚马逊市场列表 接口对应字段【code】 (required), string.
        """
        resp = await self._post("/erp/sc/data/worldState/lists", kwargs)
        return self._parse_list(resp.data, dict)

    async def get_currency_rate(self, **kwargs) -> dict:
        """
        查询汇率.

        POST /erp/sc/routing/finance/currency/currencyMonth

        Args:
            date: 汇率月份 (required), string.
        """
        resp = await self._post("/erp/sc/routing/finance/currency/currencyMonth", kwargs)
        return resp.data or {}

    async def get_profit_state_list(self, **kwargs) -> list:
        """
        获取国家下的州、省编码.

        POST /basicOpen/multiplatform/profit/report/stateList

        Args:
            countryCode: 国家编码，二字码 (required), string.
        """
        resp = await self._post("/basicOpen/multiplatform/profit/report/stateList", kwargs)
        return self._parse_list(resp.data, dict)

    # ── 写操作（慎用）──

    async def batch_rename_seller(self, sellers: list[dict]) -> dict:
        """
        批量修改店铺名称.

        POST /erp/sc/data/seller/batchEditSellerName

        Args:
            sid_name_list: 批量修改店铺数组，最多可批量修改10个 (required), array.
        """
        resp = await self._post("/erp/sc/data/seller/batchEditSellerName", {"sellers": sellers})
        return resp.data or {}

    async def update_exchange_rate(self, **kwargs) -> dict:
        """
        修改我的汇率.

        POST /basicOpen/settings/exchangeRate/update

        Args:
            my_rate: 我的汇率【小数位数最多10位】，查询汇率列表 接口对应字段【my_rate】 (required), string.
            date: 汇率年月，查询汇率列表 接口对应字段【date】 (required), string.
            code: 币种，查询汇率列表 接口对应字段【code】 (required), string.
        """
        resp = await self._post("/basicOpen/settings/exchangeRate/update", kwargs)
        return resp.data or {}

    async def download_attachment(self, **kwargs) -> dict:
        """
        下载附件.

        POST /erp/sc/routing/common/file/download

        Args:
            file_id: 附件id【取对应功能接口返回结果中的附件id值】 (required), int.
        """
        resp = await self._post("/erp/sc/routing/common/file/download", kwargs)
        return resp.data or {}

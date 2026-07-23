"""基础数据 API - 店铺、账户、市场、汇率等基础信息查询."""
from __future__ import annotations


from ..models.responses.basic_data import (
    AccountListsResponse,
    CommonFileDownloadResponse,
    ConceptSellerListsResponse,
    FinanceCurrencyCurrencymonthResponse,
    ProfitReportStatelistResponse,
    SellerAllmarketplaceResponse,
    SellerBatcheditsellernameResponse,
    SellerListsResponse,
    SettingsExchangerateUpdateResponse,
    WorldstateListsResponse,
)
from ._base import BaseEndpoint


class BasicEndpoints(BaseEndpoint):
    """领星基础数据 API (10个接口)."""

    # ── 只读接口 ──

    async def list_accounts(self) -> list[AccountListsResponse]:
        """
        查询ERP用户信息列表.

        POST /erp/sc/data/account/lists
        """
        resp = await self._post("/erp/sc/data/account/lists")
        return self._parse_list(resp.data, AccountListsResponse)

    async def list_sellers(self) -> list[SellerListsResponse]:
        """
        查询亚马逊店铺列表.

        POST /erp/sc/data/seller/lists
        """
        resp = await self._post("/erp/sc/data/seller/lists")
        return self._parse_list(resp.data, SellerListsResponse)

    async def list_concept_sellers(self) -> list[ConceptSellerListsResponse]:
        """
        查询亚马逊概念店铺列表.

        POST /erp/sc/data/seller/conceptLists
        """
        resp = await self._post("/erp/sc/data/seller/conceptLists")
        return self._parse_list(resp.data, ConceptSellerListsResponse)

    async def list_marketplaces(self) -> list[SellerAllmarketplaceResponse]:
        """
        查询亚马逊市场列表.

        POST /erp/sc/data/seller/allMarketplace
        """
        resp = await self._post("/erp/sc/data/seller/allMarketplace")
        return self._parse_list(resp.data, SellerAllmarketplaceResponse)

    async def list_world_states(self, country_code: str = None) -> list[WorldstateListsResponse]:
        """
        查询亚马逊国家下地区列表.

        POST /erp/sc/data/worldState/lists

        Args:
            country_code: 国家code，查询亚马逊市场列表 接口对应字段【code】 (required), string.
        """
        resp = await self._post("/erp/sc/data/worldState/lists", {k: v for k, v in {"country_code": country_code}.items() if v is not None})
        return self._parse_list(resp.data, WorldstateListsResponse)

    async def get_currency_rate(self, date: str = None) -> list[FinanceCurrencyCurrencymonthResponse]:
        """
        查询汇率.

        POST /erp/sc/routing/finance/currency/currencyMonth

        Args:
            date: 汇率月份 (required), string.
        """
        resp = await self._post("/erp/sc/routing/finance/currency/currencyMonth", {k: v for k, v in {"date": date}.items() if v is not None})
        return self._parse_list(resp.data, FinanceCurrencyCurrencymonthResponse)

    async def get_profit_state_list(self, countryCode: str = None) -> ProfitReportStatelistResponse:
        """
        获取国家下的州、省编码.

        POST /basicOpen/multiplatform/profit/report/stateList

        Args:
            countryCode: 国家编码，二字码 (required), string.
        """
        resp = await self._post("/basicOpen/multiplatform/profit/report/stateList", {k: v for k, v in {"countryCode": countryCode}.items() if v is not None})
        return self._parse_one(resp.data, ProfitReportStatelistResponse)

    # ── 写操作（慎用）──

    async def batch_rename_seller(self, sellers: list[dict]) -> SellerBatcheditsellernameResponse:
        """
        批量修改店铺名称.

        POST /erp/sc/data/seller/batchEditSellerName

        Args:
            sellers: 批量修改店铺数组，最多可批量修改10个 (required), array.
        """
        resp = await self._post("/erp/sc/data/seller/batchEditSellerName", {"sellers": sellers})
        return self._parse_one(resp.data, SellerBatcheditsellernameResponse)

    async def update_exchange_rate(self, my_rate: str = None, date: str = None, code: str = None) -> SettingsExchangerateUpdateResponse | None:
        """
        修改我的汇率.

        POST /basicOpen/settings/exchangeRate/update

        Args:
            my_rate: 我的汇率【小数位数最多10位】 (required), string.
            date: 汇率年月 (required), string.
            code: 币种 (required), string.
        """
        resp = await self._post("/basicOpen/settings/exchangeRate/update", {k: v for k, v in {"my_rate": my_rate, "date": date, "code": code}.items() if v is not None})
        return self._parse_one(resp.data, SettingsExchangerateUpdateResponse)

    async def download_attachment(self, file_id: int = None) -> CommonFileDownloadResponse | None:
        """
        下载附件.

        POST /erp/sc/routing/common/file/download

        Args:
            file_id: 附件id【取对应功能接口返回结果中的附件id值】 (required), int.
        """
        resp = await self._post("/erp/sc/routing/common/file/download", {k: v for k, v in {"file_id": file_id}.items() if v is not None})
        return self._parse_one(resp.data, CommonFileDownloadResponse)

"""基础数据API端点封装"""

import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase

logger = logging.getLogger(__name__)


class BasicEndpoints:

    def __init__(self, client: 'OpenApiBase'):
        self._client = client

    async def get_sellers(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询店铺列表

        API: GET /erp/sc/data/seller/lists

        领星API文档说明：
        - 获取当前账号下绑定的所有店铺信息
        - 返回店铺ID、名称、站点、状态等信息
        - 用于后续API调用中的店铺参数

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认100，最大500）
            **kwargs: 其他查询参数
                - sid: 店铺ID（可选，筛选指定店铺）
                - status: 店铺状态（可选，1-正常 2-失效）

        Returns:
            List[Dict[str, Any]]: 店铺列表
                - sid: 店铺ID
                - name: 店铺名称
                - marketplace: 站点代码
                - marketplace_name: 站点名称
                - status: 状态（1-正常 2-失效）
                - currency: 币种
                - seller_id: 亚马逊卖家ID
                - country: 国家代码

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> sellers = await basic.get_sellers(token)
            >>> for seller in sellers:
            ...     print(f"店铺: {seller['name']} - {seller['marketplace_name']}")
        """
        logger.debug("Fetching sellers: page=%s, page_size=%s", page, page_size)

        req_params = {
            "page": page,
            "pageSize": page_size,
            **kwargs
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/lists",
            method="GET",
            req_params=req_params
        )

        if resp_result.code not in [0, 200, '0', '200']:
            logger.error("Failed to fetch sellers: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_concept_sellers(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询概念店铺列表

        API: GET /erp/sc/data/seller/concept_seller_lists

        领星API文档说明：
        - 获取概念店铺（虚拟店铺分组）
        - 用于按业务线、品牌等维度组织店铺
        - 返回概念店铺ID、名称、包含的店铺列表

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认100）
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: 概念店铺列表
                - id: 概念店铺ID
                - name: 概念店铺名称
                - seller_list: 包含的店铺列表
                - created_at: 创建时间
                - updated_at: 更新时间

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> concept_sellers = await basic.get_concept_sellers(token)
            >>> for cs in concept_sellers:
            ...     print(f"概念店铺: {cs['name']}, 包含{len(cs['seller_list'])}个店铺")
        """
        logger.debug("Fetching concept sellers: page=%s, page_size=%s", page, page_size)

        req_params = {
            "page": page,
            "pageSize": page_size,
            **kwargs
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/concept_seller_lists",
            method="GET",
            req_params=req_params
        )

        if resp_result.code not in [200, '200']:
            logger.error("Failed to fetch concept sellers: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_marketplaces(
        self,
        access_token: str,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询市场列表

        API: GET /erp/sc/data/seller/allMarketplace

        领星API文档说明：
        - 获取亚马逊所有支持的市场/站点信息
        - 返回市场代码、名称、币种、国家等信息
        - 用于理解站点代码对应的实际市场

        Args:
            access_token: 访问令牌
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: 市场列表
                - marketplace: 市场代码（如 "ATVPDKIKX0DER"）
                - marketplace_name: 市场名称（如 "Amazon.com"）
                - marketplace_id: 市场ID
                - country: 国家代码（如 "US"）
                - currency: 币种（如 "USD"）
                - domain: 域名（如 "amazon.com"）

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> marketplaces = await basic.get_marketplaces(token)
            >>> for mp in marketplaces:
            ...     print(f"市场: {mp['marketplace_name']} - {mp['country']}")
        """
        logger.debug("Fetching marketplaces")

        req_params = kwargs or {}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/allMarketplace",
            method="GET",
            req_params=req_params
        )

        if resp_result.code not in [200, '200']:
            logger.error("Failed to fetch marketplaces: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_currencies(
        self,
        access_token: str,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询汇率列表

        API: GET /erp/sc/data/seller/allCurrency

        领星API文档说明：
        - 获取系统支持的所有币种汇率信息
        - 返回币种代码、对人民币汇率、更新时间
        - 用于财务数据的币种转换

        Args:
            access_token: 访问令牌
            **kwargs: 其他查询参数

        Returns:
            List[Dict[str, Any]]: 汇率列表
                - currency: 币种代码（如 "USD", "EUR", "GBP"）
                - currency_name: 币种名称（如 "美元", "欧元"）
                - rate: 对人民币汇率
                - updated_at: 更新时间

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> currencies = await basic.get_currencies(token)
            >>> for curr in currencies:
            ...     print(f"币种: {curr['currency']} - 汇率: {curr['rate']}")
        """
        logger.debug("Fetching currencies")

        req_params = kwargs or {}

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/allCurrency",
            method="GET",
            req_params=req_params
        )

        if resp_result.code not in [200, '200']:
            logger.error("Failed to fetch currencies: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_accounts(
        self,
        access_token: str,
        page: int = 1,
        page_size: int = 100,
        **kwargs
    ) -> list[dict[str, Any]]:
        """
        查询用户列表

        API: GET /erp/sc/data/seller/account_lists

        领星API文档说明：
        - 获取当前账号下的所有用户信息
        - 返回用户ID、用户名、权限角色等信息
        - 用于用户管理和权限控制

        Args:
            access_token: 访问令牌
            page: 页码（默认1）
            page_size: 每页数量（默认100）
            **kwargs: 其他查询参数
                - role: 角色筛选（可选）
                - status: 状态筛选（可选）

        Returns:
            List[Dict[str, Any]]: 用户列表
                - uid: 用户ID
                - username: 用户名
                - email: 邮箱
                - role: 角色权限
                - status: 状态（1-正常 0-禁用）
                - created_at: 创建时间
                - last_login_at: 最后登录时间

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> accounts = await basic.get_accounts(token)
            >>> for acc in accounts:
            ...     print(f"用户: {acc['username']} - 角色: {acc['role']}")
        """
        logger.debug("Fetching accounts: page=%s, page_size=%s", page, page_size)

        req_params = {
            "page": page,
            "pageSize": page_size,
            **kwargs
        }

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/seller/account_lists",
            method="GET",
            req_params=req_params
        )

        if resp_result.code not in [200, '200']:
            logger.error("Failed to fetch accounts: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_erp_accounts(
        self,
        access_token: str,
    ) -> list[dict[str, Any]]:
        """
        查询 ERP 用户信息列表

        API: GET /erp/sc/data/account/lists

        领星API文档说明：
        - 查询企业开启的全部 ERP 账号数据
        - 一次性返回所有账号，无分页
        - 唯一键：uid

        Args:
            access_token: 访问令牌

        Returns:
            List[Dict[str, Any]]: ERP 用户列表
                - uid: 用户ID（唯一键）
                - realname: 真实姓名
                - username: 用户名
                - mobile: 手机号
                - email: 邮箱
                - login_num: 登录次数
                - last_login_time: 最近登录时间
                - last_login_ip: 最近登录IP
                - status: 状态（0禁用，1正常）
                - create_time: 创建时间
                - role: 角色（逗号分隔）
                - seller: 店铺权限（逗号分隔）
                - is_master: 是否主账号（0否，1是）

        Raises:
            Exception: API请求失败时抛出异常

        Example:
            >>> accounts = await basic.get_erp_accounts(token)
            >>> for acc in accounts:
            ...     print(f"用户: {acc['realname']} ({acc['username']})")
        """
        logger.debug("Fetching ERP accounts list")

        resp_result = await self._client.request(
            access_token=access_token,
            route_name="/erp/sc/data/account/lists",
            method="GET",
            req_params={}
        )

        if resp_result.code not in [0, '0', 200, '200']:
            logger.error("Failed to fetch ERP accounts: %s", resp_result.message)
            raise Exception(f"API error: {resp_result.message}")

        # 解析响应数据
        data = resp_result.data or {}
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        if isinstance(data, dict) and "list" in data:
            return data["list"]

        return []

    async def get_all_sellers(self, access_token: str) -> list[dict[str, Any]]:
        """
        获取所有店铺（自动分页）

        便捷方法，自动处理分页，获取所有店铺数据。

        Args:
            access_token: 访问令牌

        Returns:
            List[Dict[str, Any]]: 所有店铺列表

        Example:
            >>> all_sellers = await basic.get_all_sellers(token)
            >>> print(f"总共{len(all_sellers)}个店铺")
        """
        all_sellers = []
        page = 1
        page_size = 500  # 使用最大页面大小

        while True:
            sellers = await self.get_sellers(
                access_token=access_token,
                page=page,
                page_size=page_size
            )

            if not sellers:
                break

            all_sellers.extend(sellers)

            # 如果返回数量小于页面大小，说明已经到最后了
            if len(sellers) < page_size:
                break

            page += 1

        logger.info("Fetched %s sellers in total", len(all_sellers))
        return all_sellers


__all__ = ['BasicEndpoints']

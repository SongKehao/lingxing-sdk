"""物流管理API端点封装"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from lingxing.core.openapi import OpenApiBase

from lingxing.core.resp_schema import ResponseResult


class LogisticsEndpoints:
    """
    物流管理API端点封装

    封装领星ERP物流相关的所有API接口

    使用示例:
        >>> from lingxing.openapi import OpenApiBase
        >>> from lingxing.endpoints.logistics import LogisticsEndpoints
        >>>
        >>> openapi = OpenApiBase(host, app_id, app_secret)
        >>> token = await openapi.generate_access_token()
        >>> logistics = LogisticsEndpoints(openapi)
        >>> channels = await logistics.get_logistics_channels(token.access_token)
    """

    # API路径
    HEAD_CHANNEL_LIST = "/erp/sc/data/local_inventory/channelList"
    HEAD_PROVIDER_LIST = "/basicOpen/logistics/headLogisticsProvider/query/list"
    USED_LOGISTICS_TYPE = "/erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType"
    TRANSPORT_METHOD_LIST = "/basicOpen/businessConfig/transportMethod/list"
    ADD_CHANNELS = "/erp/sc/routing/tms/FirstVessel/addChannels"
    ADD_PROVIDERS = "/erp/sc/routing/tms/FirstVessel/addProviders"

    def __init__(self, openapi: 'OpenApiBase'):
        """
        初始化物流端点

        Args:
            openapi: OpenAPI基础客户端实例
        """
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== 头程物流渠道 ====================

    async def get_logistics_channels(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
    ) -> ResponseResult:
        """
        查询头程物流渠道列表

        对应系统: 【物流】>【头程物流】>【物流渠道】

        API: POST /erp/sc/data/local_inventory/channelList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20

        Returns:
            ResponseResult: 包含物流渠道列表

        返回字段:
            - id: 物流渠道id（对应ERP页面"物流方案代码"）
            - channel_name: 物流渠道名称
            - method_id: 运输方式id
            - method_name: 运输方式名称
            - billing_type: 计费类型（0=计费重，1=体积）
            - volume_calc_param: 材积计算参数
            - zip_code: 邮编
            - valid_period: 时效天数
            - remark: 备注
            - enabled: 状态（0=停用，1=启用）
            - provider: 物流商信息
            - freight: 运费规则

        Example:
            >>> result = await logistics.get_logistics_channels(
            ...     access_token="xxx",
            ...     offset=0,
            ...     length=20
            ... )
        """
        req_body = {
            "offset": offset,
            "length": length,
        }

        return await self._request_with_token(
            access_token=access_token,
            route=self.HEAD_CHANNEL_LIST,
            req_body=req_body
        )

    async def get_all_logistics_channels(
        self,
        access_token: str,
        page_size: int = 100,
    ) -> list[dict[str, Any]]:
        """
        获取所有头程物流渠道（自动分页）

        Args:
            access_token: 访问令牌
            page_size: 每页数量

        Returns:
            所有物流渠道列表
        """
        all_channels = []
        offset = 0

        while True:
            result = await self.get_logistics_channels(
                access_token=access_token,
                offset=offset,
                length=page_size,
            )

            if result.code != 0:
                break

            data = result.data
            if isinstance(data, list):
                channels = data
            elif isinstance(data, dict):
                channels = data.get('data', [])
            else:
                break

            if not channels:
                break

            all_channels.extend(channels)

            if len(channels) < page_size:
                break

            offset += page_size

        return all_channels

    # ==================== 头程物流商 ====================

    async def get_head_logistics_providers(
        self,
        access_token: str,
        page: int = 1,
        length: int = 20,
        enabled: int | None = 1,
        is_auth: int | None = 1,
        pay_method: int | None = 1,
        search_field: str | None = None,
        search_value: str | None = None,
    ) -> ResponseResult:
        """
        查询头程物流商列表

        对应系统: 【物流】>【头程物流】>【物流商】
        默认返回已启用现结API对接的物流商

        API: POST /basicOpen/logistics/headLogisticsProvider/query/list

        Args:
            access_token: 访问令牌
            page: 页码，从1开始
            length: 分页长度
            enabled: 启用状态（0=禁用，1=启用），默认启用
            is_auth: 是否API对接（0=否，1=是），默认是
            pay_method: 结算方式（1=现结，2=月结），默认现结
            search_field: 搜索字段（code=代码，name=物流商）
            search_value: 搜索值

        Returns:
            ResponseResult: 包含物流商列表

        返回字段:
            - providerId: 物流商id
            - name: 物流商名称
            - code: 物流商代码
            - enabled: 是否启用（0=禁用，1=启用）
            - logisticsType: 类型（0=API物流，1=自定义物流，2=海外仓物流，3=头程物流，4=平台物流）
            - isAuth: 是否API对接
            - payMethod: 结算方式
            - status: 授权状态（0=未授权，1=已授权）

        Example:
            >>> result = await logistics.get_head_logistics_providers(
            ...     access_token="xxx",
            ...     page=1,
            ...     length=20
            ... )
        """
        search = {
            "page": page,
            "length": length,
        }

        if enabled is not None:
            search["enabled"] = enabled
        if is_auth is not None:
            search["isAuth"] = is_auth
        if pay_method is not None:
            search["payMethod"] = pay_method
        if search_field:
            search["searchField"] = search_field
        if search_value:
            search["searchValue"] = search_value

        req_body = {"search": search}

        return await self._request_with_token(
            access_token=access_token,
            route=self.HEAD_PROVIDER_LIST,
            req_body=req_body
        )

    async def get_all_head_logistics_providers(
        self,
        access_token: str,
        enabled: int | None = 1,
        is_auth: int | None = 1,
    ) -> list[dict[str, Any]]:
        """
        获取所有头程物流商（自动分页）

        Args:
            access_token: 访问令牌
            enabled: 启用状态
            is_auth: 是否API对接

        Returns:
            所有物流商列表
        """
        all_providers = []
        page = 1
        page_size = 100

        while True:
            result = await self.get_head_logistics_providers(
                access_token=access_token,
                page=page,
                length=page_size,
                enabled=enabled,
                is_auth=is_auth,
            )

            if result.code != 0:
                break

            data = result.data
            if isinstance(data, dict):
                providers = data.get('providers', [])
                total = data.get('total', 0)
            else:
                break

            if not providers:
                break

            all_providers.extend(providers)

            if len(all_providers) >= total:
                break

            page += 1

        return all_providers

    # ==================== 自发货物流方式 ====================

    async def get_used_logistics_types(
        self,
        access_token: str,
        provider_type: int = 0,
        page: int = 1,
        length: int = 20,
    ) -> ResponseResult:
        """
        查询已启用的自发货物流方式

        对应系统: 【物流】>【物流管理】
        包括 API物流、三方仓物流、平台物流、自定义物流

        API: POST /erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType

        Args:
            access_token: 访问令牌
            provider_type: 物流商类型
                - 0: API物流
                - 1: 自定义物流
                - 2: 海外仓物流
                - 4: 平台物流
            page: 分页页码
            length: 分页长度

        Returns:
            ResponseResult: 包含物流方式列表

        返回字段:
            - type_id: 物流方式id
            - name: 物流方式名称
            - code: 物流方式代码
            - is_used: 物流渠道是否启用（0=停用，1=启用）
            - logistics_provider_id: 物流商id
            - logistics_provider_name: 物流商名称
            - type: 物流商类型

        Example:
            >>> result = await logistics.get_used_logistics_types(
            ...     access_token="xxx",
            ...     provider_type=0,  # API物流
            ...     page=1,
            ...     length=20
            ... )
        """
        req_body = {
            "param": {
                "provider_type": provider_type,
                "page": page,
                "length": length,
            }
        }

        return await self._request_with_token(
            access_token=access_token,
            route=self.USED_LOGISTICS_TYPE,
            req_body=req_body
        )

    async def get_all_used_logistics_types(
        self,
        access_token: str,
        provider_type: int = 0,
    ) -> list[dict[str, Any]]:
        """
        获取所有已启用的自发货物流方式（自动分页）

        Args:
            access_token: 访问令牌
            provider_type: 物流商类型

        Returns:
            所有物流方式列表
        """
        all_types = []
        page = 1
        page_size = 100

        while True:
            result = await self.get_used_logistics_types(
                access_token=access_token,
                provider_type=provider_type,
                page=page,
                length=page_size,
            )

            if result.code != 0:
                break

            data = result.data
            if isinstance(data, list):
                types = data
            elif isinstance(data, dict):
                types = data.get('data', [])
            else:
                break

            if not types:
                break

            all_types.extend(types)

            if len(types) < page_size:
                break

            page += 1

        return all_types

    # ==================== 运输方式 ====================

    async def get_transport_methods(
        self,
        access_token: str,
    ) -> ResponseResult:
        """
        查询运输方式列表

        对应系统: 【设置】>【业务配置】>【物流】>【运输方式】

        API: POST /basicOpen/businessConfig/transportMethod/list

        Args:
            access_token: 访问令牌

        Returns:
            ResponseResult: 包含运输方式列表

        返回字段:
            - method_id: 运输方式id
            - code: 序号
            - name: 运输方式名称
            - is_system: 是否为系统运输方式
            - enabled: 启用状态（0=停用，1=启用）
            - remark: 备注
            - creator_id: 创建人id
            - creator_name: 创建人名称
            - created_at: 创建时间（秒级时间戳）
            - updated_at: 更新时间（秒级时间戳）

        Example:
            >>> result = await logistics.get_transport_methods(
            ...     access_token="xxx"
            ... )
        """
        req_body = {}

        return await self._request_with_token(
            access_token=access_token,
            route=self.TRANSPORT_METHOD_LIST,
            req_body=req_body
        )

    # ==================== 批量添加操作 ====================

    async def add_logistics_channels(
        self,
        access_token: str,
        channels_data: list[dict[str, Any]],
    ) -> ResponseResult:
        """
        批量添加头程物流方式

        对应系统: 【物流】>【头程物流】>【物流渠道】
        每次请求限制20条

        API: POST /erp/sc/routing/tms/FirstVessel/addChannels

        Args:
            access_token: 访问令牌
            channels_data: 物流方式数据列表，每项包含：
                - channel_name: 头程物流方式名称
                - volume_calc_param: 材积计算参数
                - zip_code: 邮编
                - valid_period: 时效天数
                - remark: 备注
                - billing_type: 计费类型（0=重量，1=体积）
                - logistics_provider_id: 所属头程物流商id
                - billing: 运费信息，格式：重量范围开始(kg),重量范围结束(kg),价格(元/kg)
                  多条运费以竖线分隔，如 "1,10,2|11,15,2.8"

        Returns:
            ResponseResult: 包含创建的物流方式id列表

        Example:
            >>> result = await logistics.add_logistics_channels(
            ...     access_token="xxx",
            ...     channels_data=[{
            ...         "channel_name": "test-001",
            ...         "volume_calc_param": 5000,
            ...         "zip_code": "",
            ...         "valid_period": 7,
            ...         "remark": "测试渠道",
            ...         "billing_type": 0,
            ...         "logistics_provider_id": "36",
            ...         "billing": "1,10,2|11,15,2.8"
            ...     }]
            ... )
        """
        req_body = {"channelsData": channels_data}

        return await self._request_with_token(
            access_token=access_token,
            route=self.ADD_CHANNELS,
            req_body=req_body
        )

    async def add_logistics_providers(
        self,
        access_token: str,
        providers_data: list[dict[str, Any]],
    ) -> ResponseResult:
        """
        批量添加头程物流商

        对应系统: 【物流】>【头程物流】>【物流商】
        每次请求限制20条

        API: POST /erp/sc/routing/tms/FirstVessel/addProviders

        Args:
            access_token: 访问令牌
            providers_data: 物流商数据列表，每项包含：
                - logistics_provider_name: 物流商名称（不能重复，限制30个字符）
                - code: 物流商代码（限制20个字符）
                - remark: 备注（限制200个字符）

        Returns:
            ResponseResult: 包含创建的物流商id列表

        Example:
            >>> result = await logistics.add_logistics_providers(
            ...     access_token="xxx",
            ...     providers_data=[{
            ...         "logistics_provider_name": "测试物流商",
            ...         "code": "TEST001",
            ...         "remark": "测试备注"
            ...     }]
            ... )
        """
        req_body = {"providersData": providers_data}

        return await self._request_with_token(
            access_token=access_token,
            route=self.ADD_PROVIDERS,
            req_body=req_body
        )


__all__ = ['LogisticsEndpoints']

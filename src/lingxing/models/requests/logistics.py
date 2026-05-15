"""Request models for Logistics APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class LogisticsChannelListRequest(LingXingModel):
    """Request for 查询头程物流渠道列表.
    
    POST /erp/sc/data/local_inventory/channelList
    """
    offset: int  # 分页偏移量
    length: int  # 分页长度


class LogisticsQueryHeadLogisticsProviderRequestSearchItem(LingXingModel):
    length: Optional[int] = None  # 分页长度，每页显示的记录数
    page: Optional[int] = None  # 页码，从1开始
    enabled: Optional[int] = None  # 启用状态，枚举值：0-禁用, 1-启用，默认启用
    isAuth: Optional[int] = None  # 是否api对接，枚举值：0-否, 1-是，默认是
    payMethod: Optional[int] = None  # 结算方式，枚举值：1-现结, 2-月结，默认现结
    searchField: Optional[str] = None  # 搜索字段，指定搜索的目标字段名称，code 代码 ，name 物流商，默认物流商
    searchValue: Optional[str] = None  # 搜索值，用于模糊搜索物流商名称、编码等

class LogisticsQueryHeadLogisticsProviderRequest(LingXingModel):
    """Request for 查询物流-头程物流商.
    
    POST /basicOpen/logistics/headLogisticsProvider/query/list
    """
    search: Optional[LogisticsQueryHeadLogisticsProviderRequestSearchItem] = None


class LogisticsAddProvidersRequestProvidersdataItem(LingXingModel):
    logistics_provider_name: str  # 物流商名称，不能重复，限制30个字符
    code: Optional[str] = None  # 物流商代码，限制20个字符
    remark: Optional[str] = None  # 备注，限制200个字符

class LogisticsAddProvidersRequest(LingXingModel):
    """Request for 批量添加头程物流商.
    
    POST /erp/sc/routing/tms/FirstVessel/addProviders
    """
    providersData: List[LogisticsAddProvidersRequestProvidersdataItem]


class LogisticsAddChannelsRequestChannelsdataItem(LingXingModel):
    channel_name: Optional[str] = None  # 头程物流方式名称
    volume_calc_param: Optional[str] = None  # 材积计算参数
    zip_code: int  # 邮编
    valid_period: str  # 时效天数
    remark: str  # 备注
    billing_type: Optional[int] = None  # 计费类型：0 重量，1 体积
    logistics_provider_id: Optional[str] = None  # 所属头程物流商id
    billing: Optional[str] = None  # 运费信息，格式：【注意逗号使用英文逗号，多条运费以竖线分隔】 重量范围开始(kg),重量范围结束(kg),价格(元/kg)

class LogisticsAddChannelsRequest(LingXingModel):
    """Request for 批量添加头程物流方式.
    
    POST /erp/sc/routing/tms/FirstVessel/addChannels
    """
    channelsData: List[LogisticsAddChannelsRequestChannelsdataItem]


class LogisticsListusedlogisticstypeRequestParamItem(LingXingModel):
    provider_type: int  # 物流商类型： 0 API物流 1 自定义物流 2 海外仓物流 4 平台物流
    page: Optional[int] = None  # 分页页码
    length: Optional[int] = None  # 分页长度

class LogisticsListusedlogisticstypeRequest(LingXingModel):
    """Request for 查询已启用的自发货物流方式.
    
    POST 
    """
    param: LogisticsListusedlogisticstypeRequestParamItem

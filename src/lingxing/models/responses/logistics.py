"""Auto-generated response models for Logistics."""

from typing import List, Optional

from pydantic import Field

from ..common import LingXingModel


class BusinessconfigTransportmethodListResponse(LingXingModel):
    """查询运输方式列表."""

    total: Optional[int] = Field(None, description="总数")
    method_id: Optional[str] = Field(None, description="运输方式id")
    code: Optional[str] = Field(None, description="序号")
    name: Optional[str] = Field(None, description="运输方式名称")
    is_system: Optional[bool] = Field(None, description="是否为系统运输方式： true 是 false 否")
    enabled: Optional[int] = Field(None, description="启动状态： 0 停用 1 启用")
    remark: Optional[str] = Field(None, description="备注")
    creator_id: Optional[int] = Field(None, description="创建人id")
    creator_name: Optional[str] = Field(None, description="创建人名称")
    updater_id: Optional[int] = Field(None, description="最后编辑人id")
    updater_name: Optional[str] = Field(None, description="最后编辑人名称")
    created_at: Optional[int] = Field(None, description="创建时间，格式：秒级时间戳")
    updated_at: Optional[int] = Field(None, description="更新时间，格式：秒级时间戳")


class HeadlogisticsproviderQueryListProviders(LingXingModel):
    """providers sub-structure."""

    provider_id: Optional[str] = Field(None, description="物流商id")
    name: Optional[str] = Field(None, description="物流商名")
    code: Optional[str] = Field(None, description="物流商代码")
    enabled: Optional[int] = Field(None, description="是否启用 0禁用 1 启用")
    logistics_type: Optional[int] = Field(
        None, description="类型 0 API物流 1 自定义物流 2 第三方仓物流 3 头程物流 4 平台物流"
    )
    is_auth: Optional[int] = Field(None, description="是否api对接 0 否 1 是")
    supplier_code: Optional[int] = Field(None, description="授权方code")
    supplier_name: Optional[str] = Field(None, description="授权方")
    status: Optional[int] = Field(None, description="授权状态 0 未授权 1 已授权")
    remark: Optional[str] = Field(None, description="备注")
    pay_method: Optional[int] = Field(None, description="结算方式")
    contact_name: Optional[str] = Field(None, description="联系人")
    contact_phone: Optional[str] = Field(None, description="联系电话")
    creator_id: Optional[int] = Field(None, description="创建人id")
    creator_name: Optional[str] = Field(None, description="创建人名")
    created_at: Optional[int] = Field(None, description="创建时间，Unix时间戳（秒）")


class HeadlogisticsproviderQueryListResponse(LingXingModel):
    """查询物流-头程物流商."""

    total: Optional[int] = Field(None, description="总记录数")
    providers: Optional[List[HeadlogisticsproviderQueryListProviders]] = Field(None, description="物流商列表")
    total: Optional[int] = Field(None, description="总记录数")


class LocalInventoryChannellistProvider(LingXingModel):
    """provider sub-structure."""

    id: Optional[str] = Field(None, description="所属头程物流商id")
    logistics_provider_name: Optional[str] = Field(None, description="所属头程物流商名称")


class LocalInventoryChannellistFreight(LingXingModel):
    """freight sub-structure."""

    country_code: Optional[str] = Field(None, description="国家")
    region_code: Optional[str] = Field(None, description="分区")
    billing_weight_start: Optional[float] = Field(None, description="计费重量范围开始")
    billing_price: Optional[float] = Field(None, description="计费价格")


class LocalInventoryChannellistResponse(LingXingModel):
    """查询头程物流渠道列表."""

    total: Optional[int] = Field(None, description="总数")
    id: Optional[int] = Field(None, description="物流渠道id【对应ERP页面“物流方案代码”】")
    channel_name: Optional[str] = Field(None, description="物流渠道")
    method_id: Optional[str] = Field(None, description="运输方式id")
    method_name: Optional[str] = Field(None, description="运输方式名称")
    billing_type: Optional[int] = Field(None, description="计费类型：0 计费重，1 体积")
    volume_calc_param: Optional[str] = Field(None, description="材积计算参数")
    zip_code: Optional[str] = Field(None, description="邮编")
    valid_period: Optional[int] = Field(None, description="时效天数")
    remark: Optional[str] = Field(None, description="备注")
    enabled: Optional[int] = Field(None, description="状态：0 停用、1 启用")
    last_modify_uid: Optional[int] = Field(None, description="最后更新数据用户id")
    gmt_modified: Optional[str] = Field(None, description="更新时间")
    provider: Optional[List[LocalInventoryChannellistProvider]] = Field(None, description="物流商信息")
    freight: Optional[List[LocalInventoryChannellistFreight]] = Field(None, description="运费规则")
    send_place_code: Optional[str] = Field(None, description="提货地代码")
    receive_country_code: Optional[str] = Field(None, description="目的国家二字码")
    is_include_tax: Optional[int] = Field(None, description="是否包税：0 否，1 是")
    is_points_behind: Optional[int] = Field(None, description="是否分抛：0 否，1 是")
    points_behind_coeffient: Optional[float] = Field(None, description="分抛系数，不带%")


class TmsFirstvesselAddchannelsResponse(LingXingModel):
    """批量添加头程物流方式."""

    id: Optional[int] = Field(None, description="物流方式对应的id")
    total: Optional[int] = Field(None, description="总数")


class TmsFirstvesselAddprovidersResponse(LingXingModel):
    """批量添加头程物流商."""

    id: Optional[int] = Field(None, description="物流商对应的id")
    total: Optional[int] = Field(None, description="总数")


class WmsLogisticsListUsedLogisticsTypeResponse(LingXingModel):
    """查询已启用的自发货物流方式 (/erp/sc/routing/wms/WmsLogistics/listUsedLogisticsType)."""

    msg: Optional[str] = None


class LogisticsHeadReconciliationListResponse(LingXingModel):
    """头程对账列表 (/basicOpen/logistics/headLogisticsReconciliation/list)."""

    msg: Optional[str] = None


class LogisticsBillConfirmResponse(LingXingModel):
    """FBM物流对账-确认/批量确认 (/basicOpen/logistics/logisticsBill/confirm)."""

    msg: Optional[str] = None

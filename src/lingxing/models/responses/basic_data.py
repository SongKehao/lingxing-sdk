"""Response models for Basic Data APIs — 店铺、账户、市场、汇率等基础信息."""

from typing import List, Optional

from pydantic import Field

from ..common import LingXingModel

# ── 查询国家下州/省编码 ──


class ProfitReportStatelistStates(LingXingModel):
    """states sub-structure."""

    country_code: Optional[str] = Field(None, description="国家编码")
    state_or_province_name: Optional[str] = Field(None, description="州/省名称")
    code: Optional[str] = Field(None, description="州/省编码")


class ProfitReportStatelistResponse(LingXingModel):
    """获取国家下的州、省编码."""

    states: Optional[List[ProfitReportStatelistStates]] = Field(None, description="州/省列表")
    total: Optional[int] = Field(None, description="总数")


# ── 查询ERP用户信息列表 ──


class AccountListsResponse(LingXingModel):
    """查询ERP用户信息列表.

    POST /erp/sc/data/account/lists
    """

    uid: Optional[int] = Field(None, description="用户id")
    realname: Optional[str] = Field(None, description="姓名")
    username: Optional[str] = Field(None, description="用户名")
    mobile: Optional[str] = Field(None, description="电话")
    email: Optional[str] = Field(None, description="邮箱")
    login_num: Optional[int] = Field(None, description="登陆次数")
    last_login_time: Optional[str] = Field(None, description="最近登录时间")
    last_login_ip: Optional[str] = Field(None, description="最近登录IP")
    status: Optional[int] = Field(None, description="状态：0 禁用，1 正常")
    create_time: Optional[str] = Field(None, description="创建时间")
    role: Optional[str] = Field(None, description="角色")
    seller: Optional[str] = Field(None, description="店铺权限")
    is_master: Optional[int] = Field(None, description="是否为主账号：0 否，1 是")
    zid: Optional[int] = Field(None, description="企业id")


# ── 查询亚马逊店铺列表 ──


class SellerListsResponse(LingXingModel):
    """查询亚马逊店铺列表.

    POST /erp/sc/data/seller/lists
    """

    sid: Optional[int] = Field(None, description="店铺id 领星ERP对企业已授权店铺的唯一标识")
    mid: Optional[int] = Field(None, description="站点id")
    name: Optional[str] = Field(None, description="店铺名")
    seller_id: Optional[str] = Field(None, description="亚马逊店铺id")
    account_name: Optional[str] = Field(None, description="店铺账户名称")
    seller_account_id: Optional[int] = Field(None, description="店铺账号id")
    region: Optional[str] = Field(None, description="站点简称，例如NA指北美")
    country: Optional[str] = Field(None, description="商城所在国家名称")
    has_ads_setting: Optional[int] = Field(None, description="是否授权广告：0 否 1 是")
    marketplace_id: Optional[str] = Field(None, description="市场id")
    status: Optional[int] = Field(None, description="店铺状态：0 停止同步 1 正常 2 授权异常 3 欠费停服")


# ── 查询亚马逊概念店铺列表 ──


class ConceptSellerListsResponse(LingXingModel):
    """查询亚马逊概念店铺列表.

    POST /erp/sc/data/seller/conceptLists
    """

    id: Optional[int] = Field(None, description="概念店铺id")
    mid: Optional[int] = Field(None, description="站点id")
    name: Optional[str] = Field(None, description="店铺名")
    seller_id: Optional[str] = Field(None, description="亚马逊店铺id")
    seller_account_id: Optional[int] = Field(None, description="店铺账号id")
    seller_account_name: Optional[str] = Field(None, description="店铺账号名称")
    region: Optional[str] = Field(None, description="站点简称")
    country: Optional[str] = Field(None, description="商城所在国家")
    status: Optional[int] = Field(None, description="店铺状态")


# ── 查询亚马逊市场列表 ──


class SellerAllmarketplaceResponse(LingXingModel):
    """查询亚马逊市场列表.

    POST /erp/sc/data/seller/allMarketplace
    """

    mid: Optional[int] = Field(None, description="站点id")
    region: Optional[str] = Field(None, description="地区")
    aws_region: Optional[str] = Field(None, description="亚马逊地区")
    country: Optional[str] = Field(None, description="商城所在国家名称")
    code: Optional[str] = Field(None, description="亚马逊国家code")
    marketplace_id: Optional[str] = Field(None, description="亚马逊市场id")


# ── 查询亚马逊国家下地区列表 ──


class WorldstateListsResponse(LingXingModel):
    """查询亚马逊国家下地区列表.

    POST /erp/sc/data/worldState/lists
    """

    country_code: Optional[str] = Field(None, description="国家code")
    state_or_province_name: Optional[str] = Field(None, description="地区名称")
    code: Optional[str] = Field(None, description="地区code")
    total: Optional[int] = Field(None, description="总数")


# ── 查询汇率 ──


class FinanceCurrencyCurrencymonthResponse(LingXingModel):
    """查询汇率.

    POST /erp/sc/routing/finance/currency/currencyMonth
    """

    date: Optional[str] = Field(None, description="汇率年月")
    code: Optional[str] = Field(None, description="币种")
    icon: Optional[str] = Field(None, description="币种符号")
    name: Optional[str] = Field(None, description="币种名")
    rate_org: Optional[str] = Field(None, description="官方汇率 数据来源中国银行官方汇率")
    my_rate: Optional[str] = Field(None, description="我的汇率 用户自定义汇率")
    update_time: Optional[str] = Field(None, description="更新时间")
    total: Optional[int] = Field(None, description="记录条数")


# ── 批量修改店铺名称 ──


class SellerBatcheditsellernameFailureDetail(LingXingModel):
    """failure_detail sub-structure."""

    sid: Optional[str] = Field(None, description="店铺id")
    name: Optional[str] = Field(None, description="店铺名")
    error: Optional[str] = Field(None, description="失败原因")


class SellerBatcheditsellernameResponse(LingXingModel):
    """批量修改店铺名称.

    POST /erp/sc/data/seller/batchEditSellerName
    """

    success_num: Optional[int] = Field(None, description="成功个数")
    failure_num: Optional[int] = Field(None, description="失败个数")
    failure_detail: Optional[List[SellerBatcheditsellernameFailureDetail]] = Field(None, description="失败详情")


# ── 下载附件 ──


class CommonFileDownloadResponse(LingXingModel):
    """下载附件.

    POST /erp/sc/routing/common/file/download
    """

    total: Optional[int] = Field(None, description="总数")
    file_name: Optional[str] = Field(None, description="文件名")
    mime_type: Optional[str] = Field(None, description="文件类型")
    content: Optional[str] = Field(None, description="base64 编码的文件内容")


class SettingsExchangerateUpdateResponse(LingXingModel):
    """修改我的汇率."""

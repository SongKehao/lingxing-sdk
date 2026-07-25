"""Request models for BasicData APIs (auto-generated from API docs)."""

from typing import List

from ..common import LingXingModel


class BasicDataWorldStateListsRequest(LingXingModel):
    """Request for 查询亚马逊国家下地区列表.

    POST /erp/sc/data/worldState/lists
    """

    country_code: str  # 国家code，查询亚马逊市场列表 接口对应字段【code】


class BasicDataSellerBatchRenameRequestSidNameListItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    name: str  # 店铺名称


class BasicDataSellerBatchRenameRequest(LingXingModel):
    """Request for 批量修改店铺名称.

    POST /erp/sc/data/seller/batchEditSellerName
    """

    sid_name_list: List[BasicDataSellerBatchRenameRequestSidNameListItem]


class BasicDataCurrencyRequest(LingXingModel):
    """Request for 查询汇率.

    POST /erp/sc/routing/finance/currency/currencyMonth
    """

    date: str  # 汇率月份


class BasicDataExchangeRateUpdateRequest(LingXingModel):
    """Request for 修改我的汇率.

    POST /basicOpen/settings/exchangeRate/update
    """

    my_rate: str  # 我的汇率【小数位数最多10位】，查询汇率列表 接口对应字段【my_rate】
    date: str  # 汇率年月，查询汇率列表 接口对应字段【date】
    code: str  # 币种，查询汇率列表 接口对应字段【code】


class BasicDataAttachmentDownloadRequest(LingXingModel):
    """Request for 下载附件.

    POST /erp/sc/routing/common/file/download
    """

    file_id: int  # 附件id【取对应功能接口返回结果中的附件id值】


class BasicDataStateListRequest(LingXingModel):
    """Request for 获取国家下的州、省编码.

    POST /basicOpen/multiplatform/profit/report/stateList
    """

    countryCode: str  # 国家编码，二字码

"""Request models for Tools APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class ToolsGetKeywordListRequest(LingXingModel):
    """Request for 关键词列表.
    
    POST /erp/sc/routing/tool/toolKeywordRank/getKeywordList
    """
    mid: Optional[int] = None  # 国家id
    start_date: Optional[str] = None  # 开始日期，格式：Y-m-d
    end_date: Optional[str] = None  # 结束日期，格式：Y-m-d
    offset: int  # 分页偏移量，默认0
    length: int  # 分页长度，默认20，最大值为2000


class ToolsCompetitiveMonitorListRequest(LingXingModel):
    """Request for 查询竞品监控列表.
    
    POST /basicOpen/tool/competitiveMonitor/list
    """
    levels: Optional[list] = None  # 竞品等级： 1 A 2 B 3 C 4 D
    update_time_start: Optional[str] = None  # 开始时间【更新时间】，闭区间，格式：Y-m-d
    update_time_end: Optional[str] = None  # 结束时间【更新时间】，闭区间，格式：Y-m-d
    search_field: Optional[str] = None  # 搜索字段：asin ASIN
    search_value: Optional[str] = None  # 搜索值：多个使用英文逗号分隔，上限200
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class ToolsWarningmessagegoodslistRequest(LingXingModel):
    """Request for 查询预警消息列表-商品.
    
    POST /basicOpen/settings/warningMessage/goodsList
    """
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，默认50，上限200
    model_id_list: Optional[list] = None  # 预警模型： 1  Listing调价预警 2  FBA费变更预警 3  Listing下架预警 6  FBA费异常预警 7  折扣异常预警 18  业务指标预警 20  折扣叠加预警 21  buyb
    sids: Optional[list] = None  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str  # 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: str  # 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    search_field: Optional[str] = None  # 搜索类型： rule_name   规则名称 asin  ASIN msku  MSKU
    search_value: Optional[str] = None  # 搜索值
    show_status: int  # 处理状态： 0  待处理 1  全部


class ToolsWarningmessageinventorylistRequest(LingXingModel):
    """Request for 查询预警消息列表-库存.
    
    POST /basicOpen/settings/warningMessage/inventoryList
    """
    offset: Optional[int] = None  # 分页偏移量
    length: Optional[int] = None  # 分页长度，默认50，上限200
    model_id_list: Optional[list] = None  # 预警模型：  4  本地库存预警 5  亚马逊库存预警 22  本地库龄预警 23  亚马逊库龄预警
    product_type_list: Optional[list] = None  # 产品类型： 2  MSKU 3   SKU+仓库+店铺+FNSKU
    start_date: str  # 开始日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: str  # 结束日期【提醒时间】，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    show_status: int  # 处理状态： 0   待处理  1    全部

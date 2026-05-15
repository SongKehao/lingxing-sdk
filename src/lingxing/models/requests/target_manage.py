"""Request models for TargetManage APIs (auto-generated from API docs)."""

from typing import List

from ..common import LingXingModel


class TargetManageStoreBatchSelectRequest(LingXingModel):
    """Request for 店铺维度-批量查询目标.
    
    POST /bd/goal/management/open/store/batchSelect
    """
    assessYear: str  # 目标年份


class TargetManageStoreBatchOperateRequestGoallistItem(LingXingModel):
    sid: int  # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    amount1: float  # 1月目标
    amount2: float  # 2月目标
    amount3: float  # 3月目标
    amount4: float  # 4月目标
    amount5: float  # 5月目标
    amount6: float  # 6月目标
    amount7: float  # 7月目标
    amount8: float  # 8月目标
    amount9: float  # 9月目标
    amount10: float  # 10月目标
    amount11: float  # 11月目标
    amount12: float  # 12月目标

class TargetManageStoreBatchOperateRequest(LingXingModel):
    """Request for 店铺维度-批量新增/更新目标.
    
    POST /bd/goal/management/open/store/batchOperate
    """
    assessYear: int  # 目标年份(只允许去年、今年、明年)
    currencyCode: str  # 币种【仅支持USD、EUR、GBP、CNY、JPY、原币种】
    operateType: int  # 操作类型： 1 仅新增 2 新增并更新
    goalList: List[TargetManageStoreBatchOperateRequestGoallistItem]


class TargetManageStoreBatchDeleteRequest(LingXingModel):
    """Request for 店铺维度-批量删除目标.
    
    POST /bd/goal/management/open/store/batchDelete
    """
    assessYear: int  # 目标年份【只允许去年、今年、明年】
    sids: List  # 需要删除的店铺id列表 ，对应查询亚马逊店铺列表接口对应字段【sid】


class TargetManageUserBatchSelectRequest(LingXingModel):
    """Request for 组织维度-批量查询目标.
    
    POST /bd/goal/management/open/user/batchSelect
    """
    assessYear: int  # 目标年份
    assessType: int  # 考核指标：1 销售额，2 销量


class TargetManageUserBatchOperateRequestUsergoallistItem(LingXingModel):
    uid: int  # 用户id
    value1: float  # 1月目标
    value2: float  # 2月目标
    value3: float  # 3月目标
    value4: float  # 4月目标
    value5: float  # 5月目标
    value6: float  # 6月目标
    value7: float  # 7月目标
    value8: float  # 8月目标
    value9: float  # 9月目标
    value10: float  # 10月目标
    value11: float  # 11月目标
    value12: float  # 12月目标

class TargetManageUserBatchOperateRequest(LingXingModel):
    """Request for 组织维度-批量新增/更新目标.
    
    POST /bd/goal/management/open/user/batchOperate
    """
    assessYear: int  # 目标年份(只允许去年、今年、明年)
    assessType: int  # 考核指标：1 销售额，2 销量
    operateType: int  # 操作类型： 1 覆盖 2 更新
    currencyCode: str  # 币种【仅支持USD、EUR、GBP、CNY、JPY】
    userGoalList: List[TargetManageUserBatchOperateRequestUsergoallistItem]


class TargetManageUserBatchDeleteRequest(LingXingModel):
    """Request for 组织维度-批量删除目标.
    
    POST /bd/goal/management/open/user/batchDelete
    """
    assessYear: int  # 目标年份【只允许去年、今年、明年】
    assessType: int  # 考核指标：1 销售额，2 销量
    uidList: List  # 用户id集合

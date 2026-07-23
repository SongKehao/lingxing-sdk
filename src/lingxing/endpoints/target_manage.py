"""目标管理 API endpoints (TargetManage)."""
from __future__ import annotations

from ..models.responses.target_manage import (
    ManagementStoreBatchdeleteResponse,
    ManagementStoreBatchoperateResponse,
    ManagementStoreBatchselectResponse,
    ManagementUserBatchdeleteResponse,
    ManagementUserBatchoperateResponse,
    ManagementUserBatchselectResponse,
)
from ._base import BaseEndpoint


class TargetManageEndpoints(BaseEndpoint):
    """领星目标管理 API (6个接口)."""

    async def store_batch_select(self, assess_year: int = None) -> list[ManagementStoreBatchselectResponse]:
        """店铺维度-批量查询目标.

POST /bd/goal/management/open/store/batchSelect

Args:
    assess_year: 考核年份 (required), int."""
        resp = await self._post("/bd/goal/management/open/store/batchSelect", {k: v for k, v in {"assessYear": assess_year}.items() if v is not None})
        return self._parse_list(resp.data, ManagementStoreBatchselectResponse)

    async def store_batch_operate(self, assess_year: int = None, currency_code: str = None, operate_type: int = None, goal_list: list = None) -> list[ManagementStoreBatchoperateResponse]:
        """店铺维度-批量新增/更新目标.

POST /bd/goal/management/open/store/batchOperate

Args:
    assess_year: 考核年份 (required), int.
    currency_code: 币种, string.
    operate_type: 操作类型, int.
    goal_list: 目标列表, array."""
        resp = await self._post("/bd/goal/management/open/store/batchOperate", {k: v for k, v in {"assessYear": assess_year, "currencyCode": currency_code, "operateType": operate_type, "goalList": goal_list}.items() if v is not None})
        return self._parse_list(resp.data, ManagementStoreBatchoperateResponse)

    async def store_batch_delete(self, assess_year: int = None, sids: list = None) -> list[ManagementStoreBatchdeleteResponse]:
        """店铺维度-批量删除目标.

POST /bd/goal/management/open/store/batchDelete

Args:
    assess_year: 考核年份 (required), int.
    sids: 店铺id列表, array."""
        resp = await self._post("/bd/goal/management/open/store/batchDelete", {k: v for k, v in {"assessYear": assess_year, "sids": sids}.items() if v is not None})
        return self._parse_list(resp.data, ManagementStoreBatchdeleteResponse)

    async def user_batch_select(self, assess_year: int = None, assess_type: int = None) -> list[ManagementUserBatchselectResponse]:
        """组织维度-批量查询目标.

POST /bd/goal/management/open/user/batchSelect

Args:
    assess_year: 考核年份 (required), int.
    assess_type: 考核类型 1销售额 2销量, int."""
        resp = await self._post("/bd/goal/management/open/user/batchSelect", {k: v for k, v in {"assessYear": assess_year, "assessType": assess_type}.items() if v is not None})
        return self._parse_list(resp.data, ManagementUserBatchselectResponse)

    async def user_batch_operate(self, assess_year: int = None, assess_type: int = None, currency_code: str = None, operate_type: int = None, user_goal_list: list = None) -> list[ManagementUserBatchoperateResponse]:
        """组织维度-批量新增/更新目标.

POST /bd/goal/management/open/user/batchOperate

Args:
    assess_year: 考核年份 (required), int.
    assess_type: 考核类型 1销售额 2销量, int.
    currency_code: 币种, string.
    operate_type: 操作类型, int.
    user_goal_list: 用户目标列表, array."""
        resp = await self._post("/bd/goal/management/open/user/batchOperate", {k: v for k, v in {"assessYear": assess_year, "assessType": assess_type, "currencyCode": currency_code, "operateType": operate_type, "userGoalList": user_goal_list}.items() if v is not None})
        return self._parse_list(resp.data, ManagementUserBatchoperateResponse)

    async def user_batch_delete(self, assess_year: int = None, assess_type: int = None, uid_list: list = None) -> list[ManagementUserBatchdeleteResponse]:
        """组织维度-批量删除目标.

POST /bd/goal/management/open/user/batchDelete

Args:
    assess_year: 考核年份 (required), int.
    assess_type: 考核类型 1销售额 2销量, int.
    uid_list: 用户id列表, array."""
        resp = await self._post("/bd/goal/management/open/user/batchDelete", {k: v for k, v in {"assessYear": assess_year, "assessType": assess_type, "uidList": uid_list}.items() if v is not None})
        return self._parse_list(resp.data, ManagementUserBatchdeleteResponse)

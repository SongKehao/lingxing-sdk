"""Goal management API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class GoalEndpoints:
    """Goal management API endpoints."""

    def __init__(self, openapi: OpenApiBase):
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

    # ==================== 店铺维度目标API ====================

    async def get_store_goals(
        self,
        access_token: str,
        assess_year: int,
        **kwargs
    ) -> ResponseResult:
        """
        店铺维度-批量查询目标

        API: POST /bd/goal/management/open/store/batchSelect

        查询指定年份所有店铺的销售目标及完成情况

        Args:
            access_token: 访问令牌
            assess_year: 目标年份
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含店铺目标列表，每个店铺包含:
                - goalName: 目标名
                - sid: 店铺ID
                - name: 店铺名
                - currencyCode: 币种
                - icon: 币种符号
                - assessYear: 目标年份
                - goalAmount1-12: 1-12月目标值
                - realAmount1-12: 1-12月完成值
                - completeRateAmount1-12: 1-12月完成率
                - totalGoalAmount: 累计目标值
                - totalRealAmount: 累计完成值
                - totalCompleteRate: 累计完成率
                - createUserId/createUserName: 创建用户
                - updateUserId/updateUserName: 更新用户
                - gmtCreate/gmtModified: 创建/更新时间

        Example:
            >>> result = await goal.get_store_goals(
            ...     access_token="xxx",
            ...     assess_year=2024
            ... )
            >>> data = result.data  # [{"goalName": "店铺1 2024 月度销售目标", ...}]
        """
        logger.debug("Fetching store goals: assess_year=%s", assess_year)

        req_body = {
            "assessYear": str(assess_year),
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/store/batchSelect",
            req_body=req_body
        )

    async def delete_store_goals(
        self,
        access_token: str,
        assess_year: int,
        sids: list[int],
        **kwargs
    ) -> ResponseResult:
        """
        店铺维度-批量删除目标

        API: POST /bd/goal/management/open/store/batchDelete

        删除指定年份和店铺的销售目标

        Args:
            access_token: 访问令牌
            assess_year: 目标年份（只允许去年、今年、明年）
            sids: 需要删除的店铺ID列表
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含删除的数据条数
                - data: 删除条数

        Example:
            >>> result = await goal.delete_store_goals(
            ...     access_token="xxx",
            ...     assess_year=2024,
            ...     sids=[135, 102]
            ... )
            >>> deleted_count = result.data  # 2
        """
        logger.debug("Deleting store goals: assess_year=%s, sids=%s", assess_year, sids)

        req_body = {
            "assessYear": str(assess_year),
            "sids": sids,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/store/batchDelete",
            req_body=req_body
        )

    async def batch_operate_store_goals(
        self,
        access_token: str,
        assess_year: int,
        currency_code: str,
        operate_type: int,
        goal_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        店铺维度-批量新增更新目标

        API: POST /bd/goal/management/open/store/batchOperate

        批量新增或更新店铺销售目标

        Args:
            access_token: 访问令牌
            assess_year: 目标年份（只允许去年、今年、明年）
            currency_code: 币种代码（USD、EUR、GBP、CNY、JPY、原币种）
            operate_type: 操作类型
                - 1: 仅新增（如果已存在则失败）
                - 2: 新增并更新（如果已存在则更新）
            goal_list: 目标列表，每个目标包含:
                - sid: 店铺ID
                - amount1-12: 1-12月目标金额
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含操作结果列表，失败时返回:
                - data: [{"sid": 1, "reason": "店铺目标已存在"}, ...]

        Example:
            >>> result = await goal.batch_operate_store_goals(
            ...     access_token="xxx",
            ...     assess_year=2024,
            ...     currency_code="原币种",
            ...     operate_type=1,
            ...     goal_list=[
            ...         {
            ...             "sid": 1,
            ...             "amount1": 953,
            ...             "amount2": 153,
            ...             # ... amount3-12
            ...         }
            ...     ]
            ... )
        """
        logger.debug(
            "Batch operating store goals: assess_year=%s, "
            "currency=%s, operate_type=%s, "
            "goal_count=%s",
            assess_year, currency_code, operate_type, len(goal_list),
        )

        req_body = {
            "assessYear": assess_year,
            "currencyCode": currency_code,
            "operateType": operate_type,
            "goalList": goal_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/store/batchOperate",
            req_body=req_body
        )

    # ==================== 组织维度目标API ====================

    async def get_user_goals(
        self,
        access_token: str,
        assess_year: int,
        assess_type: int,
        **kwargs
    ) -> ResponseResult:
        """
        组织维度-批量查询目标

        API: POST /bd/goal/management/open/user/batchSelect

        查询指定年份和考核指标的用户销售目标及完成情况

        Args:
            access_token: 访问令牌
            assess_year: 目标年份
            assess_type: 考核指标
                - 1: 销售额
                - 2: 销量
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含用户目标列表，每个用户包含:
                - realName: 用户名
                - uid: 用户ID
                - defaultOrg: 默认部门
                - defaultOrgId: 默认部门ID
                - orgs: 所有部门列表
                - currencyCode: 币种
                - icon: 货币符号
                - assessType: 考核指标
                - goalValue1-12: 1-12月目标值
                - realValue1-12: 1-12月完成值
                - completeRate1-12: 1-12月完成率
                - yearGoalValue: 年度目标值
                - yearRealValue: 年度完成值
                - completeProcess: 年度完成进度
                - createUserId/createUser: 目标创建用户
                - updateUserId/updateUser: 目标最后更新用户
                - gmtCreate/gmtModified: 创建/更新时间

        Example:
            >>> result = await goal.get_user_goals(
            ...     access_token="xxx",
            ...     assess_year=2024,
            ...     assess_type=1
            ... )
            >>> data = result.data  # [{"realName": "user1", "uid": 100108, ...}]
        """
        logger.debug("Fetching user goals: assess_year=%s, assess_type=%s", assess_year, assess_type)

        req_body = {
            "assessYear": str(assess_year),
            "assessType": assess_type,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/user/batchSelect",
            req_body=req_body
        )

    async def delete_user_goals(
        self,
        access_token: str,
        assess_year: int,
        assess_type: int,
        uid_list: list[int],
        **kwargs
    ) -> ResponseResult:
        """
        组织维度-批量删除目标

        API: POST /bd/goal/management/open/user/batchDelete

        删除指定年份、考核指标和用户的销售目标

        Args:
            access_token: 访问令牌
            assess_year: 目标年份（只允许去年、今年、明年）
            assess_type: 考核指标
                - 1: 销售额
                - 2: 销量
            uid_list: 用户ID列表
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含删除的数据条数
                - data: 删除条数

        Example:
            >>> result = await goal.delete_user_goals(
            ...     access_token="xxx",
            ...     assess_year=2024,
            ...     assess_type=1,
            ...     uid_list=[1001, 1002]
            ... )
            >>> deleted_count = result.data  # 2
        """
        logger.debug(
            "Deleting user goals: assess_year=%s, "
            "assess_type=%s, uid_list=%s",
            assess_year, assess_type, uid_list,
        )

        req_body = {
            "assessYear": str(assess_year),
            "assessType": assess_type,
            "uidList": uid_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/user/batchDelete",
            req_body=req_body
        )

    async def batch_operate_user_goals(
        self,
        access_token: str,
        assess_year: int,
        assess_type: int,
        operate_type: int,
        currency_code: str,
        user_goal_list: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        组织维度-批量新增更新目标

        API: POST /bd/goal/management/open/user/batchOperate

        批量新增或更新用户销售目标

        Args:
            access_token: 访问令牌
            assess_year: 目标年份（只允许去年、今年、明年）
            assess_type: 考核指标
                - 1: 销售额
                - 2: 销量
            operate_type: 操作类型
                - 1: 覆盖（完全替换原有目标）
                - 2: 更新（仅更新指定月份）
            currency_code: 币种代码（USD、EUR、GBP、CNY、JPY）
            user_goal_list: 用户目标集合，每个目标包含:
                - uid: 用户ID
                - value1-12: 1-12月目标值
            **kwargs: 其他查询参数

        Returns:
            ResponseResult: 包含操作结果列表，失败时返回:
                - data: [{"uid": 100109, "reason": "用户不存在"}, ...]

        Example:
            >>> result = await goal.batch_operate_user_goals(
            ...     access_token="xxx",
            ...     assess_year=2024,
            ...     assess_type=1,
            ...     operate_type=2,
            ...     currency_code="CNY",
            ...     user_goal_list=[
            ...         {
            ...             "uid": 100109,
            ...             "value1": 33.00,
            ...             "value2": 13.00,
            ...             # ... value3-12
            ...         }
            ...     ]
            ... )
        """
        logger.debug(
            "Batch operating user goals: assess_year=%s, "
            "assess_type=%s, operate_type=%s, "
            "currency=%s, user_goal_count=%s",
            assess_year, assess_type, operate_type,
            currency_code, len(user_goal_list),
        )

        req_body = {
            "assessYear": assess_year,
            "assessType": assess_type,
            "operateType": operate_type,
            "currencyCode": currency_code,
            "userGoalList": user_goal_list,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/bd/goal/management/open/user/batchOperate",
            req_body=req_body
        )


__all__ = [
    'GoalEndpoints',
]

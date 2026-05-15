#!/usr/bin/python3
"""openapi接口响应 schema"""
import logging
from typing import Any

from pydantic import BaseModel, root_validator

logger = logging.getLogger(__name__)


def reset_msg_and_trace_id(cls, values: dict):
    """重置异常信息"""
    try:
        values['message'] = values.get('message') or values.get('msg', '')
        values['request_id'] = values.get('request_id') or values.get('traceId', '')
        # 修复：API返回的code可能是字符串，需要转换为整数
        if 'code' in values and isinstance(values['code'], str):
            values['code'] = int(values['code'])
    except Exception:
        logger.debug("Failed to reset message and trace_id in response schema")
    return values


class ResponseResult(BaseModel):
    code: int | None                     # 响应码
    message: str | None                  # 响应信息
    data: Any                               # 接口响应数据
    error_details: Any | None = None     # 异常信息
    request_id: str | None = None        # 标记本次请求唯一ID
    response_time: str | None = None     # 响应时间
    total: int | None = None

    _reset_msg_and_trace_id = root_validator(allow_reuse=True, pre=True)(
        reset_msg_and_trace_id
    )


class AccessTokenDto(BaseModel):
    access_token: str           # 接口访问认证信息
    refresh_token: str          # RefreshToken用于续费AccessToken，只能使用一次
    expires_in: int             # AccessToken的有效期, TTL

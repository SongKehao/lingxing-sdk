"""openapi接口响应 schema"""

import logging
from typing import Any, Optional

from pydantic import BaseModel, model_validator

logger = logging.getLogger(__name__)


class ResponseResult(BaseModel):
    """领星API响应结果."""

    code: Optional[int] = None
    message: Optional[str] = None
    data: Any = None
    error_details: Any = None
    request_id: Optional[str] = None
    response_time: Optional[str] = None
    total: Optional[int] = None

    @model_validator(mode="before")
    @classmethod
    def _normalize_fields(cls, values: dict) -> dict:
        """统一字段名和类型."""
        if not isinstance(values, dict):
            return values
        try:
            values["message"] = values.get("message") or values.get("msg", "")
            values["request_id"] = values.get("request_id") or values.get("traceId", "")
            if "code" in values and isinstance(values["code"], str):
                values["code"] = int(values["code"])
        except Exception:
            logger.debug("Failed to normalize response fields")
        return values


class AccessTokenDto(BaseModel):
    """领星API访问令牌."""

    access_token: str
    refresh_token: str
    expires_in: int

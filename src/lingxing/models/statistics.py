"""Auto-generated Pydantic models from API fixtures."""

from typing import Optional
from pydantic import Field

from .common import LingXingModel


class MonthRefundData(LingXingModel):
    """Statistics/MonthRefund 响应数据项."""

    list: Optional[list] = None
    total: Optional[int] = None

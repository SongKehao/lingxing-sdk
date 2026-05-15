"""Pydantic models for Statistics APIs."""
from typing import Optional

from .common import LingXingModel


class MonthRefundItem(LingXingModel):
    """Response item for MonthRefund."""

    list: Optional[list] = None
    total: Optional[int] = None

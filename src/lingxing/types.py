"""Shared types for LingXing SDK."""

from __future__ import annotations

from pydantic import BaseModel, Field


class PageRequest(BaseModel):
    """通用分页请求参数."""

    page: int = Field(default=1, ge=1, description="页码，从1开始")
    page_size: int = Field(default=50, ge=1, le=200, description="每页条数，最大200")

    @property
    def offset(self) -> int:
        """计算偏移量."""
        return (self.page - 1) * self.page_size


class PageResult(BaseModel):
    """通用分页响应."""

    total: int = Field(default=0, description="总记录数")
    page: int = Field(default=1, description="当前页码")
    page_size: int = Field(default=50, description="每页条数")

    @property
    def has_more(self) -> bool:
        """是否还有下一页."""
        return self.page * self.page_size < self.total

    @property
    def total_pages(self) -> int:
        """总页数."""
        if self.page_size <= 0:
            return 0
        return (self.total + self.page_size - 1) // self.page_size


class DateRangeRequest(BaseModel):
    """通用日期范围请求."""

    start_date: str | None = Field(None, description="开始日期，格式 YYYY-MM-DD")
    end_date: str | None = Field(None, description="结束日期，格式 YYYY-MM-DD")


class SellerFilteredRequest(BaseModel):
    """需要指定店铺的请求."""

    sid: int | None = Field(None, description="店铺ID")
    sids: list[int] | None = Field(None, description="店铺ID列表")

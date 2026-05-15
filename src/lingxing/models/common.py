"""Common shared models."""
from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field


class LingXingModel(BaseModel):
    """Base model for all LingXing data models."""
    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PageResult(LingXingModel):
    """通用分页结果."""
    total: int = 0
    page: int = 1
    page_size: int = 50

    @property
    def has_more(self) -> bool:
        return self.page * self.page_size < self.total

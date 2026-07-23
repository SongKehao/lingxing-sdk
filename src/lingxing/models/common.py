"""Common shared models."""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


def _to_camel(name: str) -> str:
    """Convert snake_case to camelCase for API field aliasing."""
    parts = name.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])


class LingXingModel(BaseModel):
    """Base model for all LingXing data models.

    Supports both camelCase (from API) and snake_case (Python) field names.
    API responses use camelCase which gets automatically mapped to snake_case.
    """
    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        alias_generator=_to_camel,
        coerce_numbers_to_str=True,
    )


class PageResult(LingXingModel):
    """通用分页结果."""
    total: int = 0
    page: int = 1
    page_size: int = 50

    @property
    def has_more(self) -> bool:
        return self.page * self.page_size < self.total

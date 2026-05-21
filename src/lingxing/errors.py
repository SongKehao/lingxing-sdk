from __future__ import annotations
"""LingXing SDK Custom Exceptions."""


class LingXingError(Exception):
    """Base exception for all LingXing SDK errors."""

    def __init__(self, message: str, code: int | None = None):
        self.code = code
        super().__init__(message)


class AuthenticationError(LingXingError):
    """Token acquisition or refresh failed."""


class RateLimitError(LingXingError):
    """API rate limit exceeded (error code 3001008)."""

    def __init__(self, message: str = "Rate limit exceeded", retry_after: float | None = None):
        self.retry_after = retry_after
        super().__init__(message, code=3001008)


class ApiError(LingXingError):
    """API returned a non-zero error code."""

    def __init__(
        self,
        message: str,
        code: int,
        request_id: str | None = None,
        url: str | None = None,
    ):
        self.request_id = request_id
        self.url = url
        super().__init__(message, code=code)


class ValidationError(LingXingError):
    """Request parameter validation failed (client-side)."""

#!/usr/bin/env python3
"""LingXing Integration Base Classes — standalone, no dependencies on integrations.base."""

from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import Any


class IntegrationStatus(StrEnum):
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    ERROR = "error"


class IntegrationHealth(StrEnum):
    UNKNOWN = "unknown"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"


@dataclass
class IntegrationHealthCheck:
    """Health check result"""
    status: IntegrationHealth
    message: str = ""
    timestamp: datetime = None
    details: dict[str, Any] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.details is None:
            self.details = {}


class BaseIntegration:

    def __init__(self, name: str, config: Any = None):
        self.name = name
        self.config = config
        self._status = IntegrationStatus.DISCONNECTED
        self._last_error: str | None = None

    @property
    def status(self) -> IntegrationStatus:
        return self._status

    @property
    def last_error(self) -> str | None:
        return self._last_error

    def is_connected(self) -> bool:
        """Check if integration is connected"""
        return self._status == IntegrationStatus.CONNECTED

    async def connect(self) -> bool:
        """Connect to the integration"""
        raise NotImplementedError

    async def disconnect(self) -> None:
        """Disconnect from the integration"""
        self._status = IntegrationStatus.DISCONNECTED

    async def health_check(self) -> IntegrationHealthCheck:
        """Check health of the integration"""
        raise NotImplementedError


class HTTPIntegration(BaseIntegration):

    def __init__(self, name: str, config: Any = None, base_url: str = ""):
        super().__init__(name, config)
        self.base_url = base_url


# Error classes
class IntegrationError(Exception):
    pass


class IntegrationTimeoutError(IntegrationError):
    pass


class IntegrationAuthError(IntegrationError):
    pass


class IntegrationRateLimitError(IntegrationError):
    pass

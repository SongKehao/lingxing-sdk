#!/usr/bin/env python3
"""领星SDK可观测性模块 — Prometheus指标收集"""

import logging
import time
from contextlib import asynccontextmanager

from prometheus_client import Counter, Gauge, Histogram

logger = logging.getLogger(__name__)

api_requests_total = Counter(
    'lingxing_api_requests_total',
    'Total Lingxing API requests',
    ['endpoint', 'method', 'status']
)

api_duration_seconds = Histogram(
    'lingxing_api_duration_seconds',
    'Lingxing API request duration in seconds',
    ['endpoint', 'method']
)

active_connections = Gauge(
    'lingxing_active_connections',
    'Number of active Lingxing API connections'
)


@asynccontextmanager
async def track_request(endpoint: str, method: str = "POST"):
    """
    追踪API请求的上下文管理器

    Args:
        endpoint: API端点路径
        method: HTTP方法

    Yields:
        None

    Example:
        async with track_request("/api/orders", "GET"):
            response = await client.request(...)
    """
    start_time = time.time()
    status = "unknown"

    try:
        active_connections.inc()
        yield
        status = "success"
    except Exception:
        status = "error"
        logger.debug("API request to %s %s failed", method, endpoint)
        raise
    finally:
        duration = time.time() - start_time
        api_duration_seconds.labels(endpoint=endpoint, method=method).observe(duration)
        api_requests_total.labels(endpoint=endpoint, method=method, status=status).inc()
        active_connections.dec()

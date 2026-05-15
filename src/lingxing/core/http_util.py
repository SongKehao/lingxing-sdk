"""领星OpenAPI HTTP请求封装"""
import logging
import os
import ssl

import aiohttp
import orjson

from .resp_schema import ResponseResult

logger = logging.getLogger(__name__)

# 从环境变量读取配置
DISABLE_SSL_VERIFY = os.getenv("DISABLE_SSL_VERIFY", "false").lower() == "true"
DEFAULT_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "120"))


class HttpBase:
    """HTTP 请求基类，支持异步请求"""

    def __init__(self, default_timeout: int | None = None):
        self.default_timeout = default_timeout or DEFAULT_TIMEOUT

    async def request(self, method: str, req_url: str,
                      params: dict | None = None,
                      json: dict | None = None,
                      headers: dict | None = None,
                      **kwargs) -> ResponseResult:
        timeout = kwargs.pop('timeout', self.default_timeout)
        data = orjson.dumps(json, option=orjson.OPT_SORT_KEYS) if json else None

        if DISABLE_SSL_VERIFY:
            logger.warning("SSL 证书验证已禁用（不安全，仅用于开发/测试环境）")
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            connector = aiohttp.TCPConnector(ssl=ssl_context)
        else:
            connector = aiohttp.TCPConnector()

        async with (
            aiohttp.ClientSession(connector=connector) as aio_session,
            aio_session.request(method=method, url=req_url, params=params, data=data,
                                timeout=timeout, headers=headers, **kwargs) as resp,
        ):
            if resp.status != 200:
                error_body = await resp.text()
                msg = f"Response error, status code: {resp.status}, body: {error_body}"
                raise ValueError(msg)
            resp_json = await resp.json()
            return ResponseResult(**resp_json)

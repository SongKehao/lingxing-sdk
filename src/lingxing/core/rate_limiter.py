#!/usr/bin/python3
"""
领星API请求限流器

领星API限流规则（基于实际测试）：
1. Token请求（generate_access_token/refresh_token）：
   - 错误码: 3001008
   - 错误信息: "new requests too frequently. please request later."
   - 限流周期: 约每小时重置
   - 建议间隔: 60秒以上

2. 业务API请求：
   - 限流: 100次/分钟（根据文档）
   - 建议间隔: 0.6秒以上

3. IP白名单：
   - 需要在领星后台添加当前IP
   - IP变化时需要重新添加白名单
   - 检测IP: https://toolbox.lingxing.com/api/getIp

使用方法:
    from rate_limiter import RateLimiter, check_ip_whitelist

    # 创建限流器
    limiter = RateLimiter()

    # 在请求前检查
    await limiter.wait_if_needed('token')  # Token请求
    await limiter.wait_if_needed('api')    # 业务API请求

    # 检测IP白名单
    result = await check_ip_whitelist(['219.144.200.230', '221.11.17.222'])

"""
import asyncio
import logging
import re
import time
from collections import deque
from typing import Any, ClassVar

import aiohttp

logger = logging.getLogger(__name__)


IP_CHECK_URL = "https://toolbox.lingxing.com/api/getIp"
_cached_ip: str | None = None


async def detect_current_ip(use_cache: bool = True) -> str | None:
    """
    检测当前环境的公网IP

    Args:
        use_cache: 是否使用缓存（默认True）

    Returns:
        str: 当前IP地址，失败返回None
    """
    global _cached_ip

    if use_cache and _cached_ip:
        return _cached_ip

    try:
        async with (
            aiohttp.ClientSession() as session,
            session.get(IP_CHECK_URL, timeout=10) as resp,
        ):
            if resp.status == 200:
                data = await resp.json()
                if data.get("success") and data.get("data"):
                    # 解析 "真实的Ip是: x.x.x.x" 格式
                    ip_str = data["data"]
                    match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', ip_str)
                    if match:
                        _cached_ip = match.group(1)
                        return _cached_ip
    except Exception as e:
        logger.warning("Failed to detect current IP: %s", e)
        return None
    else:
        return None


async def check_ip_whitelist(expected_ips: set[str]) -> dict[str, Any]:
    """
    检查当前IP是否在预期白名单中

    Args:
        expected_ips: 预期的IP白名单集合

    Returns:
        Dict: 包含检测结果
            - current_ip: 当前检测到的IP
            - is_whitelisted: 是否在白名单中
            - expected_ips: 预期的白名单IP
            - warning: 警告信息（如果有）
    """
    current_ip = await detect_current_ip()

    result = {
        "current_ip": current_ip,
        "is_whitelisted": True,
        "expected_ips": list(expected_ips),
        "warning": None
    }

    if current_ip and expected_ips:
        if current_ip not in expected_ips:
            result["is_whitelisted"] = False
            result["warning"] = (
                f"IP白名单警告: 当前IP {current_ip} 不在预期白名单中! "
                f"请将此IP加入领星API白名单，否则API调用可能失败。"
            )
            logger.warning(result["warning"])
        else:
            logger.info("IP白名单检查通过: %s", current_ip)

    return result



class RateLimiter:
    """
    领星API请求限流器

    防止请求过于频繁导致被限流（错误码3001008）
    """

    # 限流配置
    TOKEN_MIN_INTERVAL = 60.0  # Token请求最小间隔（秒）
    API_MIN_INTERVAL = 0.6     # 业务API请求最小间隔（秒）
    API_MAX_REQUESTS_PER_MINUTE = 100  # 每分钟最大请求数

    # 全局状态（跨实例共享）
    _last_token_request: float = 0.0
    _last_api_request: float = 0.0
    _api_requests: ClassVar[deque] = deque()  # 记录最近1分钟的请求时间
    _lock = asyncio.Lock()

    def __init__(
        self,
        token_min_interval: float | None = None,
        api_min_interval: float | None = None,
    ):
        """
        初始化限流器

        Args:
            token_min_interval: Token请求最小间隔（秒），默认60秒
            api_min_interval: 业务API请求最小间隔（秒），默认0.6秒
        """
        self.token_min_interval = token_min_interval or self.TOKEN_MIN_INTERVAL
        self.api_min_interval = api_min_interval or self.API_MIN_INTERVAL

    async def wait_if_needed(self, request_type: str = 'api') -> float:
        """
        如果需要，等待以满足限流要求

        Args:
            request_type: 请求类型
                - 'token': Token请求（generate_access_token/refresh_token）
                - 'api': 业务API请求

        Returns:
            float: 实际等待的秒数
        """
        async with self._lock:
            if request_type == 'token':
                return await self._wait_for_token()
            return await self._wait_for_api()

    async def _wait_for_token(self) -> float:
        """等待Token请求间隔"""
        now = time.time()
        elapsed = now - self._last_token_request
        wait_time = max(0, self.token_min_interval - elapsed)

        if wait_time > 0:
            logger.debug("Rate limiter: waiting %.1fs before token request", wait_time)
            await asyncio.sleep(wait_time)

        self._last_token_request = time.time()
        return wait_time

    async def _wait_for_api(self) -> float:
        """等待业务API请求间隔"""
        now = time.time()

        # 清理1分钟前的请求记录
        while self._api_requests and now - self._api_requests[0] > 60:
            self._api_requests.popleft()

        # 检查每分钟请求限制
        if len(self._api_requests) >= self.API_MAX_REQUESTS_PER_MINUTE:
            oldest = self._api_requests[0]
            wait_time = 60 - (now - oldest) + 0.1
            logger.warning("Rate limiter: approaching rate limit, waiting %.1fs", wait_time)
            await asyncio.sleep(wait_time)
            now = time.time()

        # 检查最小间隔
        elapsed = now - self._last_api_request
        wait_time = max(0, self.api_min_interval - elapsed)

        if wait_time > 0:
            await asyncio.sleep(wait_time)

        self._last_api_request = time.time()
        self._api_requests.append(self._last_api_request)

        return wait_time

    @classmethod
    def get_status(cls) -> dict[str, Any]:
        """
        获取限流器状态

        Returns:
            Dict: 包含限流器状态信息
        """
        now = time.time()
        return {
            "last_token_request": cls._last_token_request,
            "seconds_since_token": now - cls._last_token_request if cls._last_token_request else None,
            "token_cooldown_remaining": max(0, cls.TOKEN_MIN_INTERVAL - (now - cls._last_token_request)) if cls._last_token_request else 0,
            "last_api_request": cls._last_api_request,
            "api_requests_last_minute": len(cls._api_requests),
            "api_capacity_remaining": cls.API_MAX_REQUESTS_PER_MINUTE - len(cls._api_requests),
        }

    @classmethod
    def reset(cls):
        """重置限流器状态（慎用）"""
        cls._last_token_request = 0.0
        cls._last_api_request = 0.0
        cls._api_requests.clear()
        logger.info("Rate limiter reset")


# 全局限流器实例
_global_limiter: RateLimiter | None = None


def get_rate_limiter() -> RateLimiter:
    """获取全局限流器实例"""
    global _global_limiter
    if _global_limiter is None:
        _global_limiter = RateLimiter()
    return _global_limiter

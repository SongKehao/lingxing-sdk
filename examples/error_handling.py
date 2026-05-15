#!/usr/bin/env python3
"""
领星 SDK 错误处理示例

演示:
- 认证错误
- API错误
- 限流错误
- 网络重试
"""
import asyncio

from lingxing import LingXingConfig
from lingxing.core.openapi import OpenApiBase
from lingxing.endpoints.basic import BasicEndpoints
from lingxing.errors import ApiError, AuthenticationError, RateLimitError


async def main():
    config = LingXingConfig()
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    basic = BasicEndpoints(api)

    # 1. 捕获API错误
    try:
        await basic.list_sellers_with_invalid_param()
    except ApiError as e:
        print(f"API错误: code={e.code}, message={e.message}")

    # 2. 捕获认证错误
    bad_api = OpenApiBase(
        host=config.host,
        app_id="invalid_id",
        app_secret="invalid_secret",
    )
    bad_basic = BasicEndpoints(bad_api)
    try:
        await bad_basic.list_sellers()
    except AuthenticationError as e:
        print(f"认证错误: {e.message}")

    # 3. Rate limit会自动重试（最多3次），超出后抛出异常
    # SDK内置自动重试，通常不需要手动处理

    print("\n错误处理示例完成")


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python3
"""
领星 SDK 基础使用示例

Usage:
    export LINGXING_APP_ID=your_app_id
    export LINGXING_APP_SECRET=your_app_secret
    python basic_usage.py
"""
import asyncio
import os

from lingxing import LingXingConfig
from lingxing.core.openapi import OpenApiBase
from lingxing.endpoints.sale import SaleEndpoints
from lingxing.endpoints.basic import BasicEndpoints


async def main():
    # 1. 配置 - 从环境变量读取
    config = LingXingConfig()

    # 2. 创建API客户端
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    # 3. 使用endpoint方法
    basic = BasicEndpoints(api)
    sellers = await basic.list_sellers()
    print(f"共有 {len(sellers)} 个店铺")
    for s in sellers[:5]:
        print(f"  - {s.name} (sid={s.sid}, 市场={s.country})")

    # 4. 带参数查询
    sale = SaleEndpoints(api)
    listings = await sale.listing(sid="123", offset=0, length=20)
    print(f"\n查询到 {len(listings)} 个Listing")


if __name__ == "__main__":
    asyncio.run(main())

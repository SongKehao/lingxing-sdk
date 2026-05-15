#!/usr/bin/env python3
"""
领星 SDK 分页遍历示例 - 自动翻页获取全部数据

Usage:
    export LINGXING_APP_ID=your_app_id
    export LINGXING_APP_SECRET=your_app_secret
    python pagination.py
"""
import asyncio

from pydantic import BaseModel

from lingxing import LingXingConfig
from lingxing.core.openapi import OpenApiBase
from lingxing.endpoints._base import BaseEndpoint


class ListingItem(BaseModel):
    sid: int = 0
    asin: str = ""
    seller_sku: str = ""


async def main():
    config = LingXingConfig()
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    ep = BaseEndpoint(api)

    # 方法1: 逐页遍历
    print("=== 逐页遍历 ===")
    page_count = 0
    async for page in ep._iter_pages(
        "/erp/sc/routing/amzod/listing/mws",
        ListingItem,
        page_size=100,
        base_params={"sid": "123"},
    ):
        page_count += 1
        print(f"第{page_count}页: {len(page)}条记录")

    # 方法2: 一次性收集全部
    print("\n=== 一次性收集全部（最多1000条）===")
    all_items = await ep._collect_all(
        "/erp/sc/routing/amzod/listing/mws",
        ListingItem,
        page_size=100,
        base_params={"sid": "123"},
        max_items=1000,
    )
    print(f"共收集 {len(all_items)} 条记录")


if __name__ == "__main__":
    asyncio.run(main())

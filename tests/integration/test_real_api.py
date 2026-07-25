"""真实集成测试 — 调领星真实 API 验证端到端（token/签名/分页/响应解析）。

CI 无凭证时整个模块 skip（pytestmark）；本地配 LINGXING_APP_ID/SECRET
（复制 .env.example 为 .env，或 export 环境变量）后运行：

    pytest tests/integration/test_real_api.py -v

只读 GET，不触发任何写操作。
"""

import os

import pytest

pytestmark = pytest.mark.skipif(
    not (os.getenv("LINGXING_APP_ID") and os.getenv("LINGXING_APP_SECRET")),
    reason="需 LINGXING_APP_ID/SECRET（本地手动跑，CI skip）",
)

from lingxing import LingXingClient


@pytest.fixture
async def client():
    c = LingXingClient()
    await c.connect()
    yield c
    await c.disconnect()


@pytest.mark.asyncio
async def test_real_get_stores(client):
    """token 获取 + MD5 签名 + StoreInfo 解析端到端。"""
    stores = await client.get_stores()
    assert isinstance(stores, list)
    assert len(stores) > 0  # 真实账号应有店铺


@pytest.mark.asyncio
async def test_real_get_products_paginated(client):
    """分页参数 page/page_size 生效 + ProductInfo 解析。"""
    products = await client.get_products(page=1, page_size=5)
    assert len(products) <= 5  # page_size 生效


@pytest.mark.asyncio
async def test_real_get_sellers(client):
    """原始 dict 返回路径（get_sellers 返回 list[dict]）。"""
    sellers = await client.get_sellers(page=1, page_size=5)
    assert isinstance(sellers, list)

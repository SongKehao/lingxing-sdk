#!/usr/bin/env python3
"""测试产品管理API

测试内容:
1. 获取Token
2. 查询产品列表

Author: AI Platform Team
Date: 2026-02-24
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

# 添加项目路径

# 导入SDK
from lingxing.core.openapi import OpenApiBase
from lingxing.endpoints.product import ProductEndpoints

from .config import get_lingxing_config

# 响应文件目录
RESPONSE_DIR = Path(__file__).parent / "api_results"


async def test_product_list(api: OpenApiBase, access_token: str):
    """测试产品列表API"""
    print("\n" + "=" * 60)
    print("测试: 查询本地产品列表")
    print("=" * 60)

    product_ep = ProductEndpoints(api)

    # 测试1 - 基本查询
    print("\n[测试1] 基本查询 (offset=0, length=10)")
    try:
        products = await product_ep.get_products(
            access_token=access_token,
            offset=0,
            length=10
        )

        print("返回状态: 成功")
        print(f"产品数量: {len(products)}")

        if products:
            print("\n第一个产品示例:")
            first_product = products[0]
            print(f"  - ID: {first_product.get('id')}")
            print(f"  - SKU: {first_product.get('sku')}")
            print(f"  - 品名: {first_product.get('product_name')}")
            print(f"  - 类别: {first_product.get('category_name')}")
            print(f"  - 品牌: {first_product.get('brand_name')}")
            print(f"  - 状态: {first_product.get('status_text')}")
            print(f"  - 采购成本: {first_product.get('cg_price')}")

            # 保存响应
            response_file = RESPONSE_DIR / "product_list_live.json"
            response_file.parent.mkdir(parents=True, exist_ok=True)
            with Path(response_file).open('w', encoding='utf-8') as f:
                json.dump({
                    "test": "product_list",
                    "timestamp": datetime.now().isoformat(),
                    "count": len(products),
                    "sample": first_product,
                    "all_data": products
                }, f, ensure_ascii=False, indent=2)
            print(f"\n响应已保存到: {response_file}")
        else:
            print("返回数据为空")

    except Exception as e:
        print(f"请求失败: {e}")
        import traceback  # noqa: PLC0415
        traceback.print_exc()

    # 测试2 - 按SKU查询
    print("\n[测试2] 按SKU查询 (使用第一个产品的SKU)")
    if products and products[0].get('sku'):
        test_sku = products[0].get('sku')
        print(f"查询SKU: {test_sku}")
        try:
            product = await product_ep.get_product_by_sku(
                access_token=access_token,
                sku=test_sku
            )
            if product:
                print(f"找到产品: {product.get('product_name')}")
            else:
                print("未找到产品")
        except Exception as e:
            print(f"请求失败: {e}")


async def main():
    """主测试函数"""
    print("=" * 60)
    print("领星ERP 产品管理API测试")
    print("=" * 60)

    # 从环境变量或 .env.core 加载配置
    _config = get_lingxing_config()
    HOST = _config.host
    APP_ID = _config.app_id
    APP_SECRET = _config.app_secret

    print(f"Host: {HOST}")
    print(f"App ID: {APP_ID[:8]}...")

    api = OpenApiBase(HOST, APP_ID, APP_SECRET)

    # 获取Token
    print("\n获取Token...")
    token_dto = await api.generate_access_token()
    print(f"Token: {token_dto.access_token[:20]}...")
    print(f"有效期: {token_dto.expires_in}秒")

    # 测试产品API
    await test_product_list(api, token_dto.access_token)

    print("\n" + "=" * 60)
    print("测试完成!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

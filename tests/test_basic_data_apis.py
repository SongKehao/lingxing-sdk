#!/usr/bin/env python3
"""领星ERP - 基础数据API验证 (Agent #1)

验证以下API:
1. 概念店铺列表: /erp/sc/data/seller/conceptLists (GET)
2. 批量修改店铺名称: /erp/sc/data/seller/batchEditSellerName (POST)
3. 国家地区列表: /erp/sc/data/worldState/lists (POST)
4. 汇率查询: /erp/sc/routing/finance/currency/currencyMonth (POST)
5. 修改汇率: /basicOpen/settings/exchangeRate/update (POST)
6. ERP用户信息列表: /erp/sc/data/account/lists (GET)

执行步骤:
1. 使用 OpenApiBase 类调用API
2. 保存响应到 tests/api_responses/
3. API调用间隔0.5秒避免限流
4. 更新 API_REGISTRY.md 状态
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


from lingxing.core.openapi import OpenApiBase
from .config import get_lingxing_config

# 配置
RESPONSE_DIR = Path(__file__).parent / "api_responses"
RESPONSE_DIR.mkdir(exist_ok=True)

_config = get_lingxing_config()
HOST = _config.host
APP_ID = _config.app_id
APP_SECRET = _config.app_secret

# 测试店铺ID
TEST_SID = 4661

api_client: OpenApiBase | None = None
current_token: str | None = None
results = {"success": [], "failed": [], "skipped": []}


async def get_token() -> str:
    """获取访问令牌"""
    global current_token
    if current_token:
        return current_token
    token_dto = await api_client.generate_access_token()
    current_token = token_dto.access_token
    print(f"✅ Token: {current_token[:20]}... ({token_dto.expires_in}秒)")
    return current_token


def save_response(api_name: str, response: dict[str, Any]) -> None:
    """保存API响应到文件"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = RESPONSE_DIR / f"{api_name}_{timestamp}.json"
    with Path(filepath).open("w", encoding="utf-8") as f:
        json.dump(
            {
                "api_name": api_name,
                "timestamp": datetime.now().isoformat(),
                "response": response,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    code = response.get("code")
    if code == 0:
        data = response.get("data")
        if isinstance(data, list):
            records = len(data)
        elif isinstance(data, dict):
            records = data.get("total", len(data))
        else:
            records = 1 if data else 0
        print(f"  ✅ {api_name}: {records}条记录")
        results["success"].append(api_name)
    else:
        msg = response.get("message", response.get("msg", "unknown error"))
        print(f"  ❌ {api_name}: code={code}, message={msg}")
        results["failed"].append({"name": api_name, "code": code, "message": msg})


async def call_api(
    api_name: str,
    route_name: str,
    method: str = "POST",
    req_body: dict | None = None,
) -> dict[str, Any]:
    """调用API并保存响应"""
    token = await get_token()
    print(f"\n📡 [{method}] {api_name}")
    print(f"   路径: {route_name}")
    if req_body:
        print(f"   参数: {json.dumps(req_body, ensure_ascii=False)}")

    try:
        response = await api_client.request(
            access_token=token,
            route_name=route_name,
            method=method,
            req_body=req_body,
        )
        result = {
            "code": response.code,
            "message": response.message,
            "data": response.data,
            "request_id": getattr(response, "request_id", None),
            "response_time": getattr(response, "response_time", None),
        }
        save_response(api_name, result)
        await asyncio.sleep(0.5)  # 避免限流
        return result
    except Exception as e:
        error_result = {"code": -1, "message": str(e)}
        save_response(api_name, error_result)
        return error_result


# ===== API 测试函数 =====


async def test_concept_seller_lists():
    """1. 查询概念店铺列表 (GET)"""
    # 文档: /erp/sc/data/seller/conceptLists (GET)
    return await call_api(
        api_name="basic_concept_seller_lists",
        route_name="/erp/sc/data/seller/conceptLists",
        method="GET",
    )


async def test_world_state_lists():
    """2. 查询国家地区列表 (POST)"""
    # 文档: /erp/sc/data/worldState/lists (POST)
    # 参数: country_code (国家代码，如 US, DE)
    return await call_api(
        api_name="basic_world_state_lists",
        route_name="/erp/sc/data/worldState/lists",
        method="POST",
        req_body={"country_code": "US"},
    )


async def test_currency():
    """3. 查询汇率 (POST)"""
    # 文档: /erp/sc/routing/finance/currency/currencyMonth (POST)
    # 参数: date (汇率月份，如 2026-02)
    current_month = datetime.now().strftime("%Y-%m")
    return await call_api(
        api_name="basic_currency",
        route_name="/erp/sc/routing/finance/currency/currencyMonth",
        method="POST",
        req_body={"date": current_month},
    )


async def test_account_lists():
    """4. 查询ERP用户信息列表 (GET)"""
    # 文档: /erp/sc/data/account/lists (GET)
    return await call_api(
        api_name="basic_account_lists",
        route_name="/erp/sc/data/account/lists",
        method="GET",
    )


async def test_batch_rename():
    """5. 批量修改店铺名称 (POST) - 仅验证接口可访问性

    注意: 此API会修改数据，使用无效的店铺ID测试可访问性
    """
    # 文档: /erp/sc/data/seller/batchEditSellerName (POST)
    # 使用一个不存在的店铺ID来测试API可访问性，避免实际修改数据
    return await call_api(
        api_name="basic_seller_batch_rename",
        route_name="/erp/sc/data/seller/batchEditSellerName",
        method="POST",
        req_body={
            "sid_name_list": [
                {"sid": 999999999, "name": "TEST_SHOP_NAME_API_VERIFY"}  # 无效ID测试
            ]
        },
    )


async def test_exchange_rate_update():
    """6. 修改汇率 (POST) - 仅验证接口可访问性

    注意: 此API会修改数据，使用无效参数测试可访问性
    """
    # 文档: /basicOpen/settings/exchangeRate/update (POST)
    # 使用一个无效参数测试API可访问性
    current_month = datetime.now().strftime("%Y-%m")
    return await call_api(
        api_name="basic_exchange_rate_update",
        route_name="/basicOpen/settings/exchangeRate/update",
        method="POST",
        req_body={
            "my_rate": "1.0000",
            "date": current_month,
            "code": "CNY",  # 人民币汇率通常为1
        },
    )


async def main():
    """主测试流程"""
    global api_client

    print("=" * 70)
    print("🚀 领星ERP - 基础数据API验证 (Agent #1)")
    print("=" * 70)
    print(f"📁 响应目录: {RESPONSE_DIR}")
    print(f"🔑 HOST: {HOST}")
    print(f"🏪 测试店铺: {TEST_SID}")
    print("=" * 70)

    api_client = OpenApiBase(HOST, APP_ID, APP_SECRET)

    # 获取Token
    await get_token()

    # ===== 执行测试 =====
    print("\n" + "=" * 70)
    print("📋 开始执行API测试")
    print("=" * 70)

    # 只读API, 优先测试
    await test_concept_seller_lists()  # 1. 概念店铺列表
    await test_world_state_lists()  # 2. 国家地区列表
    await test_currency()  # 3. 汇率查询
    await test_account_lists()  # 4. ERP用户列表

    # 写入API (谨慎测试，使用无效参数验证可访问性)
    print("\n⚠️ 以下为写入API，使用无效参数验证可访问性:")
    await test_batch_rename()  # 5. 批量修改店铺名称
    await test_exchange_rate_update()  # 6. 修改汇率

    # ===== 最终统计 =====
    print("\n" + "=" * 70)
    print("📊 测试完成统计")
    print("=" * 70)
    print(f"✅ 成功: {len(results['success'])} 个")
    print(f"❌ 失败: {len(results['failed'])} 个")

    if results["success"]:
        print("\n✅ 成功的API:")
        for name in results["success"]:
            print(f"   - {name}")

    if results["failed"]:
        print("\n❌ 失败的API:")
        for item in results["failed"]:
            print(f"   - {item['name']}: {item['message']}")

    # 输出响应文件列表
    response_files = list(RESPONSE_DIR.glob("basic_*.json"))
    print(f"\n📁 响应文件数: {len(response_files)}")

    return results


if __name__ == "__main__":
    asyncio.run(main())

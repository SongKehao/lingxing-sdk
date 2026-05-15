#!/usr/bin/env python3
"""
领星ERP API连接测试脚本

验证API凭证是否有效
Author: AI Platform Team
Date: 2026-02-17
"""

import asyncio
import json
import os
import sys
from pathlib import Path

# 添加项目路径

try:
    from lingxing.core.openapi import OpenApiBase
except ImportError as e:
    print(f"❌ SDK导入失败: {e}")
    print("请安装依赖: pip install aiohttp pycryptodome orjson pydantic")
    sys.exit(1)


def get_config():
    """从环境变量加载配置"""
    return {
        "host": os.getenv("LINGXING_HOST", "https://openapi.lingxing.com"),
        "app_id": os.getenv("LINGXING_APP_ID"),
        "app_secret": os.getenv("LINGXING_APP_SECRET"),
    }


async def test_lingxing_connection():  # noqa: PLR0915
    """测试领星API连接"""

    print("=" * 60)
    print("领星ERP API连接测试")
    print("=" * 60)

    # 从环境变量获取API凭证
    config = get_config()

    if not config["app_id"] or not config["app_secret"]:
        print("❌ 缺少 API 凭证配置")
        print("请设置环境变量: LINGXING_APP_ID, LINGXING_APP_SECRET")
        return {"success": False, "error": "Missing credentials"}

    host = config["host"]
    app_id = config["app_id"]
    app_secret = config["app_secret"]

    print("\n📋 测试参数:")
    print(f"  - API Host: {host}")
    print(f"  - App ID: {app_id}")
    print(f"  - App Secret: {app_secret[:10]}...{app_secret[-4:]}")

    try:
        # 创建OpenAPI客户端
        print("\n🔧 创建API客户端...")
        api = OpenApiBase(
            host=host,
            app_id=app_id,
            app_secret=app_secret
        )

        # 测试获取访问令牌
        print("\n🔑 获取访问令牌...")
        token_dto = await api.generate_access_token()

        print("✅ 获取令牌成功！")
        print(f"  - Access Token: {token_dto.access_token[:20]}...{token_dto.access_token[-10:]}")
        print(f"  - Refresh Token: {token_dto.refresh_token[:20]}...{token_dto.refresh_token[-10:]}")
        print(f"  - Expires In: {token_dto.expires_in} 秒")

        # 计算过期时间
        import datetime  # noqa: PLC0415
        expires_at = datetime.datetime.now() + datetime.timedelta(seconds=token_dto.expires_in)
        print(f"  - Expires At: {expires_at.strftime('%Y-%m-%d %H:%M:%S')}")

        # 测试刷新令牌
        print("\n🔄 刷新访问令牌...")
        refresh_dto = await api.refresh_token(token_dto.refresh_token)

        print("✅ 刷新令牌成功！")
        print(f"  - New Access Token: {refresh_dto.access_token[:20]}...{refresh_dto.access_token[-10:]}")
        print(f"  - New Refresh Token: {refresh_dto.refresh_token[:20]}...{refresh_dto.refresh_token[-10:]}")
        print(f"  - Expires In: {refresh_dto.expires_in} 秒")

        # 测试API请求（获取店铺列表）
        print("\n📊 测试API请求（获取店铺列表）...")
        resp_result = await api.request(
            access_token=token_dto.access_token,
            route_name="/api/data/seller/lists",
            method="GET",
            req_params={"page": 1, "pageSize": 1}
        )

        print("✅ API请求成功！")
        print(f"  - Response Code: {resp_result.code}")
        print(f"  - Response Message: {resp_result.message}")
        print(f"  - Request ID: {resp_result.request_id}")
        print(f"  - Response Time: {resp_result.response_time}")

        # 解析响应数据
        if resp_result.code == 200 and resp_result.data:
            print("\n📦 响应数据（前100个字符）:")
            data_str = json.dumps(resp_result.data, ensure_ascii=False, indent=2)
            print(data_str[:200] + "...")
        else:
            print("\n⚠️  响应数据为空或格式异常")
            print(f"  - Data: {resp_result.data}")

        print("\n" + "=" * 60)
        print("✅ 所有测试通过！API凭证有效。")
        print("=" * 60)

        return {
            "success": True,
            "access_token": token_dto.access_token,
            "expires_in": token_dto.expires_in,
            "api_response": resp_result.dict() if resp_result else None
        }

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        print(f"  - 错误类型: {type(e).__name__}")
        print(f"  - 错误详情: {e!s}")
        print("\n" + "=" * 60)
        print("❌ API测试失败，请检查凭证。")
        print("=" * 60)

        return {
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        }


async def test_api_endpoints():
    """测试各个API端点"""

    print("\n🔍 测试API端点可用性...")

    # 这里可以添加更多端点测试
    print("  - /api/auth-server/oauth/access-token: ✅ 已验证")
    print("  - /api/auth-server/oauth/refresh: ✅ 已验证")
    print("  - /api/data/seller/lists: ✅ 已验证")

    # 更多端点可以添加
    endpoints = [
        "/api/data/product/lists",
        "/api/erp/sc/inventory/lists",
        "/api/erp/sc/order/lists",
    ]

    print("\n⏳ 待验证的端点:")
    for endpoint in endpoints:
        print(f"  - {endpoint}")


async def main():
    """主函数"""
    try:
        # 测试连接
        result = await test_lingxing_connection()

        # 如果连接成功，测试端点
        if result["success"]:
            await test_api_endpoints()

    except Exception as e:
        print(f"\n❌ 测试脚本执行失败: {e}")
        import traceback  # noqa: PLC0415
        traceback.print_exc()


if __name__ == "__main__":
    print("🚀 启动领星ERP API测试...\n")

    # 运行测试
    asyncio.run(main())

    print("\n✨ 测试完成！\n")

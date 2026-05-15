# lingxing-sdk

领星 ERP OpenAPI Python SDK — 类型安全、异步、Pydantic 模型

## 安装

```bash
pip install lingxing-sdk
```

开发模式：

```bash
pip install -e ".[dev]"
```

## 快速开始

```python
import asyncio
from lingxing import LingXingConfig
from lingxing.core.openapi import OpenApiBase
from lingxing.endpoints.basic import BasicEndpoints

async def main():
    # 配置（从环境变量 LINGXING_APP_ID / LINGXING_APP_SECRET 读取）
    config = LingXingConfig()
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    # 使用 typed endpoint
    basic = BasicEndpoints(api)
    sellers = await basic.list_sellers()

    for s in sellers:
        print(f"店铺: {s.name} (sid={s.sid}, 市场={s.country})")

asyncio.run(main())
```

## 特性

- **400个API** — 覆盖领星官方文档全部接口
- **类型安全** — Pydantic 请求/响应模型
- **异步** — 基于 aiohttp 的 async/await
- **自动Token管理** — 获取、缓存、刷新全自动
- **限流保护** — 内置 rate limiter
- **录制回放测试** — 真实API响应录制用于单元测试

## 模块

| 模块 | 方法数 | 说明 |
|------|--------|------|
| basic | 10 | 店铺、账户、市场、汇率 |
| sale | 44 | Listing、订单、促销 |
| warehouse | 76 | 仓库、海外仓、库存 |
| fba | 31 | FBA发货、头程物流 |
| finance | 19 | 利润、结算、多平台财务 |
| product | 23 | 产品、SPU、UPC |
| purchase | 19 | 采购、供应商 |
| statistics | 30 | 销量、利润统计 |
| customer_service | 16 | Review、Feedback、邮件 |
| amazon_source | 20 | MWS报表 |
| vc | 10 | VC店铺/订单 |
| restocking | 13 | 补货建议 |
| multiplatform_ads | 38 | Lazada/Shopee/TikTok/Walmart广告 |
| multiplatform_platforms | 33 | 多平台商品/发货 |
| 其他 | 61 | 物流、工具、限流、新广告等 |

## 测试

```bash
# 运行全部测试（26个）
LINGXING_APP_ID=test LINGXING_APP_SECRET=test pytest tests/ -v

# 仅单元测试
pytest tests/unit/ -v
```

## 项目结构

```
src/lingxing/
├── client.py          # 高级客户端封装
├── config.py          # 配置管理
├── errors.py          # 自定义异常
├── types.py           # 通用类型
├── core/              # 内部核心（HTTP、认证、签名）
│   ├── openapi.py     # HTTP客户端 + Token管理
│   ├── sign.py        # 签名算法
│   ├── aes.py         # AES加密
│   └── ...
├── models/            # Pydantic 响应模型（37个）
│   ├── common.py      # 基础模型
│   ├── basic.py       # 店铺/账户模型
│   ├── product.py     # 产品模型
│   └── ...
└── endpoints/         # API方法（19个模块，400个方法）
    ├── _base.py       # BaseEndpoint 基类
    ├── basic.py       # 基础数据API
    ├── sale.py        # 销售API
    └── ...
```

## License

MIT

# lingxing-sdk

领星 ERP OpenAPI Python SDK — 类型安全、异步、Pydantic 模型

[![PyPI](https://img.shields.io/badge/version-0.3.0-blue)](https://pypi.org/project/lingxing-sdk/)
[![Python](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-115%20passing-brightgreen)](./tests/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)

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
    config = LingXingConfig()  # reads LINGXING_APP_ID/SECRET from env
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    basic = BasicEndpoints(api)
    sellers = await basic.list_sellers()  # returns list[SellerListsItem]

    for s in sellers:
        print(f"店铺: {s.name} (sid={s.sid}, 市场={s.country})")

asyncio.run(main())
```

## 特性

- **400个API** — 覆盖领星官方文档全部接口
- **37个Pydantic模型** — 基于真实API响应自动生成，类型安全
- **异步** — 基于 aiohttp 的 async/await
- **自动Token管理** — 获取、缓存、刷新全自动
- **优雅降级** — Pydantic解析失败时自动fallback到原始dict
- **录制回放测试** — 51个真实API响应fixture用于单元测试
- **零警告** — 完全迁移到Pydantic V2

## 模块

| 模块 | 方法数 | Pydantic模型 | 说明 |
|------|--------|-------------|------|
| basic | 10 | 4 | 店铺、账户、市场、汇率 |
| sale | 44 | - | Listing、订单、促销 |
| warehouse | 76 | 17 | 仓库、海外仓、库存 |
| fba | 31 | 6 | FBA发货、头程物流 |
| finance | 19 | - | 利润、结算、多平台财务 |
| product | 23 | 5 | 产品、SPU、UPC、品牌 |
| purchase | 19 | 4 | 采购、供应商 |
| statistics | 30 | 1 | 销量、利润统计 |
| customer_service | 16 | - | Review、Feedback、邮件 |
| amazon_source | 20 | - | MWS报表 |
| vc | 10 | - | VC店铺/订单 |
| restocking | 13 | - | 补货建议 |
| logistics | 5 | - | 物流 |
| tools | 4 | - | 工具 |
| restocking_limit | 2 | - | FBA库存限制 |
| new_ad | 4 | - | 新版广告 |
| multiplatform_ads | 38 | - | 多平台广告 |
| multiplatform_platforms | 33 | - | 多平台商品/发货 |
| multiplatform_other | 3 | - | 多平台其他 |
| **合计** | **400** | **37** | |

## 测试

```bash
# 115个测试全部通过
LINGXING_APP_ID=test LINGXING_APP_SECRET=test pytest tests/ -v

# 仅单元测试（115个）
pytest tests/unit/ -v
```

## 项目结构

```
src/lingxing/
├── __init__.py         # v0.3.0, exports client + config
├── client.py           # 高级客户端封装
├── config.py           # 配置管理
├── errors.py           # ApiError / AuthError / RateLimitError
├── types.py            # PageRequest / PageResult / DateRangeRequest
├── core/               # 内部核心
│   ├── openapi.py      # HTTP客户端 + Token管理
│   ├── sign.py         # MD5签名
│   ├── aes.py          # AES加密
│   └── resp_schema.py  # ResponseResult (Pydantic V2)
├── models/             # Pydantic 响应模型
│   ├── common.py       # LingXingModel 基类
│   ├── basic.py        # 4个模型
│   ├── fba.py          # 6个模型
│   ├── product.py      # 5个模型
│   ├── purchase.py     # 4个模型
│   ├── warehouse.py    # 17个模型
│   ├── statistics.py   # 1个模型
│   └── business.py     # 业务模型（StoreInfo等）
└── endpoints/          # API方法（19个模块）
    ├── _base.py        # BaseEndpoint 基类
    ├── basic.py        # 基础数据（typed示范）
    └── ...
```

## License

MIT

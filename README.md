# lingxing-sdk

领星 ERP OpenAPI Python SDK — 类型安全、异步、Pydantic 模型

[![PyPI](https://img.shields.io/badge/version-0.5.0-blue)](https://pypi.org/project/lingxing-sdk/)
[![Python](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-135%20passing-brightgreen)](./tests/)
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
from lingxing.endpoints.sale import SaleEndpoints

async def main():
    config = LingXingConfig()  # reads LINGXING_APP_ID/SECRET from env
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    sale = SaleEndpoints(api)
    # Typed parameters, Chinese docstrings
    listings = await sale.listing(sid="123", offset=0, length=20)

asyncio.run(main())
```

## 特性

- **400个API** — 覆盖领星官方文档全部接口，全部typed参数
- **1260个Pydantic模型** — 795个Request + 465个Response模型
- **395个中文Docstring** — 从官方API文档自动生成，含参数说明
- **异步** — 基于 aiohttp 的 async/await
- **自动Token管理** — 获取、缓存、刷新全自动
- **自动重试** — Rate limit错误自动指数退避重试
- **分页迭代器** — `_iter_pages()` / `_collect_all()` 翻页遍历
- **优雅降级** — Pydantic解析失败时自动fallback到原始dict
- **异常层级** — LingXingError → ApiError / RateLimitError / AuthenticationError
- **限流保护** — 内置令牌桶限流器

## 模块

| 模块 | 方法数 | 说明 |
|------|--------|------|
| basic | 10 | 店铺、账户、市场、汇率 |
| sale | 44 | Listing、订单、促销 |
| warehouse | 76 | 仓库、海外仓、库存 |
| fba | 31 | FBA发货、头程物流 |
| finance | 19 | 利润、结算、多平台财务 |
| product | 23 | 产品、SPU、UPC、品牌 |
| purchase | 19 | 采购、供应商 |
| statistics | 30 | 销量、利润统计 |
| customer_service | 16 | Review、Feedback、邮件 |
| amazon_source | 20 | MWS报表 |
| vc | 10 | VC店铺/订单 |
| restocking | 13 | 补货建议 |
| logistics | 5 | 物流 |
| tools | 4 | 工具 |
| restocking_limit | 2 | FBA库存限制 |
| new_ad | 4 | 新版广告 |
| multiplatform_ads | 38 | 多平台广告 |
| multiplatform_platforms | 33 | 多平台商品/发货 |
| multiplatform_other | 3 | 多平台其他 |
| **合计** | **400** | |

## 测试

```bash
# 135个测试全部通过
LINGXING_APP_ID=test LINGXING_APP_SECRET=test pytest tests/ -v
```

## 项目结构

```
src/lingxing/
├── __init__.py              # v0.4.0, 57个公开API
├── client.py                # 高级客户端封装
├── config.py                # 配置管理
├── errors.py                # 异常层级
├── types.py                 # PageRequest / PageResult
├── core/                    # 内部核心
│   ├── openapi.py           # HTTP客户端 + Token管理
│   ├── sign.py              # MD5签名
│   ├── rate_limiter.py      # 令牌桶限流器
│   └── resp_schema.py       # ResponseResult
├── models/
│   ├── requests/            # 795个Request模型 (19文件)
│   ├── responses/           # 465个Response模型 (18文件)
│   └── business.py          # 业务模型
└── endpoints/               # 400个API方法 (19模块)
    ├── _base.py             # retry + pagination基类
    └── ...
```

## License

MIT

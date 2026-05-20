# lingxing-sdk

领星 ERP OpenAPI Python SDK — 类型安全、异步、Pydantic 模型

[![PyPI](https://img.shields.io/badge/version-0.6.0-blue)](https://pypi.org/project/lingxing-sdk/)
[![Python](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)

## 安装

```bash
pip install lingxing-sdk
```

开发模式：

```bash
pip install -e ".[dev]"
```

带 Prometheus 指标：

```bash
pip install -e ".[metrics]"
```

## 快速开始

```python
import asyncio
from lingxing import LingXingConfig, OpenApiBase
from lingxing.endpoints.sale import SaleEndpoints

async def main():
    config = LingXingConfig()  # reads LINGXING_APP_ID/SECRET from env
    api = OpenApiBase(
        host=config.host,
        app_id=config.app_id,
        app_secret=config.app_secret,
    )

    sale = SaleEndpoints(api)
    listings = await sale.listing(sid="123", offset=0, length=20)

asyncio.run(main())
```

高级客户端：

```python
from lingxing import LingXingClient

async def main():
    client = LingXingClient()
    await client.connect()
    stores = await client.get_stores()
    # client.openapi 可直接访问底层 OpenApiBase
```

## 特性

- **480个API** — 覆盖领星官方文档全部接口，全部typed参数
- **1800+个Pydantic模型** — Request + Response 模型，camelCase 自动映射
- **480个中文Docstring** — 从官方API文档自动生成，含参数说明
- **异步** — 基于 aiohttp 的 async/await
- **自动Token管理** — 获取、缓存、刷新全自动
- **自动重试** — Rate limit错误自动指数退避重试
- **分页迭代器** — `_iter_pages()` / `_collect_all()` 翻页遍历
- **优雅降级** — Pydantic解析失败时自动fallback到原始dict
- **异常层级** — LingXingError → ApiError / RateLimitError / AuthenticationError
- **限流保护** — 内置令牌桶限流器
- **camelCase ↔ snake_case** — LingXingModel 自动 alias 映射

## 模块

| 模块 | 方法数 | 说明 |
|------|--------|------|
| basic | 10 | 店铺、账户、市场、汇率 |
| sale | 44 | Listing、订单、促销 |
| warehouse | 76 | 仓库、海外仓、库存 |
| fba | 31 | FBA发货、头程物流 |
| finance | 45 | 利润、结算、多平台财务 |
| product | 23 | 产品、SPU、UPC、品牌 |
| purchase | 19 | 采购、供应商 |
| statistics | 31 | 销量、利润统计 |
| customer_service | 16 | Review、Feedback、邮件 |
| amazon_source | 20 | MWS报表 |
| vc | 10 | VC店铺/订单 |
| restocking | 13 | 补货建议 |
| logistics | 5 | 物流 |
| tools | 4 | 工具 |
| restocking_limit | 2 | FBA库存限制 |
| new_ad | 57 | 新版广告（SP/SB/SD） |
| multiplatform_ads | 38 | 多平台广告 |
| multiplatform_platforms | 33 | 多平台商品/发货 |
| multiplatform_other | 3 | 多平台其他 |
| **合计** | **481** | |

## 测试

```bash
LINGXING_APP_ID=test LINGXING_APP_SECRET=*** pytest tests/ -v
```

## 项目结构

```
src/lingxing/
├── __init__.py              # 公开API导出
├── client.py                # 高级客户端（委托 OpenApiBase token管理）
├── config.py                # 配置管理
├── errors.py                # 异常层级
├── types.py                 # PageRequest / PageResult
├── py.typed                 # PEP 561 类型标记
├── core/
│   ├── openapi.py           # HTTP客户端 + Token管理
│   ├── sign.py              # MD5签名
│   ├── rate_limiter.py      # 令牌桶限流器
│   └── resp_schema.py       # ResponseResult
├── models/
│   ├── common.py            # LingXingModel (camelCase alias)
│   ├── requests/            # Request模型
│   ├── responses/           # Response模型
│   └── business.py          # 业务模型
└── endpoints/               # 481个API方法 (19模块)
    ├── _base.py             # retry + pagination基类
    └── ...
```

## Changelog

### 0.6.0
- **LingXingModel**: 添加 `alias_generator=_to_camel`，自动 camelCase ↔ snake_case 映射
- **LingXingClient**: 移除重复 token 管理，完全委托 OpenApiBase
- **移除非SDK模块**: keyword_classifier, integration_base, observability
- **prometheus-client**: 改为 optional `[metrics]` 依赖
- **添加 py.typed**: PEP 561 类型标记
- **清理空壳模型文件**: finance, tools, restocking_limit
- **client.py**: 新增 `openapi` 属性，暴露底层 OpenApiBase 实例

### 0.5.0
- 480+ API 端点覆盖
- Pydantic v2 模型
- 自动 token 管理
- 分页迭代器

## License

MIT

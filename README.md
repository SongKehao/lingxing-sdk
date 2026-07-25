# lingxing-sdk

领星 ERP OpenAPI Python SDK — 类型安全、异步、Pydantic 模型

[![PyPI](https://img.shields.io/badge/version-0.7.0-blue)](https://pypi.org/project/lingxing-sdk/)
[![Python](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)

## 安装

要求 Python 3.11+。本地开发环境：

```bash
python3.11 -m venv .venv && .venv/bin/pip install -e '.[dev]'
```

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

- **613个API** — 覆盖领星官方文档全部接口；入参类型化进行中（64 处业务入参仍标注为 `Any`，待迁移为 TypedDict，见 [生产级路线图](.omc/plans/production-grade-roadmap.md) Phase 4）
- **1800+个Pydantic模型** — Request + Response 模型，camelCase 自动映射
- **613个中文Docstring** — 从官方API文档自动生成，含参数说明
- **Response 模型绑定 563/613 (91%)** — 已绑定方法返回类型安全的 Pydantic 模型；约 9% (50 个) 方法仍返回原始 `dict`/`list`，待补绑定
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
| sale | 58 | Listing、订单、促销 |
| warehouse | 106 | 仓库、海外仓、库存 |
| fba | 56 | FBA发货、头程物流 |
| finance | 48 | 利润、结算、多平台财务 |
| product | 27 | 产品、SPU、UPC、品牌 |
| purchase | 19 | 采购、供应商 |
| statistics | 41 | 销量、利润统计 |
| customer_service | 18 | Review、Feedback、邮件 |
| amazon_source | 20 | MWS报表 |
| vc | 10 | VC店铺/订单 |
| restocking | 13 | 补货建议 |
| logistics | 8 | 物流 |
| tools | 5 | 工具 |
| restocking_limit | 2 | FBA库存限制 |
| new_ad | 58 | 新版广告（SP/SB/SD） |
| multiplatform_ads | 38 | 多平台广告 |
| multiplatform_platforms | 67 | 多平台商品/发货 |
| multiplatform_other | 3 | 多平台其他 |
| target_manage | 6 | 店铺/用户目标管理 |
| **合计** | **613** | |

> 计数配方（可复现）：`for f in src/lingxing/endpoints/*.py（排除 _base.py / __init__.py）; do grep -cE '^[[:space:]]*async def [a-z][a-z0-9_]*\(' "$f"; done` —— 统计各 endpoint 模块的公共（非 `_` 开头）`async def` 方法。`_base.py` 的 3 个分页辅助方法（`collect_all`/`iter_pages`/`collect_all_raw`）不计入 API 方法，故 616（含辅助）− 3 = **613**。

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
└── endpoints/               # 613个API方法 (20模块)
    ├── _base.py             # retry + pagination基类
    └── ...
```

## Changelog

### 勘误 / Errata

- **commit `030ac28` "Any 1925->0 (100%类型化)" 修正** — 该提交信息不准确。`grep` 实测仍有 `Any` 残留（截至 2026-07-24）：
  - `: Any` 字段/参数标注 **76 处**（endpoints 68 + models 5 + core 2 + client 1）
  - `[Any]`（多为 `Optional[Any]`）**29 处**（全在 `models/requests/`）
  - `-> Any` 返回标注 **0 处**
  - 合计 **105 处** `Any`，非 0。其中 **64 处** 为 endpoint 业务入参 `: Any = None`，待 [生产级路线图](.omc/plans/production-grade-roadmap.md) Phase 4 迁移为 TypedDict；core 层 `dict[str, Any]` 容器惯用法（24 处）有意保留。

### 0.7.0
- **Response Model 绑定**: 434/480 (90%) endpoint 方法绑定类型安全的 Pydantic response model
- **数据校验**: 所有绑定的方法通过 `_parse_list`/`_parse_one`/`_parse_page` 自动校验 API 返回数据
- **旧 Model 迁移**: 6 个手写 model 文件 (basic/fba/product/purchase/statistics/warehouse) 合并到 `models/responses/`
- **字段验证**: 94% 的 response model 字段与真实 API 数据完全匹配 (32/34 fixtures)
- **覆盖率**: 全部 19 个核心 endpoint 文件完成绑定，包括 multiplatform、restocking、new_ad 等
- 148 单元测试通过、4 skipped（**需 Python 3.11+**；旧 3.8 环境下因 PEP 604 语法导致 collection 崩溃，已在 Phase 0 修复，`pytest --co -q` 现收集 152 tests）

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

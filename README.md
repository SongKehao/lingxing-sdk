# lingxing-sdk

领星 ERP OpenAPI Python SDK

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
from lingxing import LingXingClient, LingXingConfig

# 方式1：通过环境变量配置
# 设置 LINGXING_APP_ID 和 LINGXING_APP_SECRET
config = LingXingConfig()

# 方式2：直接传参
config = LingXingConfig(
    app_id="your_app_id",
    app_secret="your_app_secret",
)

# 创建客户端
client = LingXingClient(config)

# 使用API
products = await client.get_products()
```

## 配置说明

### 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `LINGXING_HOST` | API 地址 | `https://openapi.lingxing.com` |
| `LINGXING_APP_ID` | 应用 ID | - |
| `LINGXING_APP_SECRET` | 应用密钥 | - |

### 代码传参

```python
from lingxing import LingXingConfig

config = LingXingConfig(
    host="https://openapi.lingxing.com",
    app_id="your_app_id",
    app_secret="your_app_secret",
)
```

## API 覆盖范围

| 数据域 | 模块 | 说明 |
|--------|------|------|
| 产品 | `endpoints.product` | 产品列表、详情、分类 |
| 广告 | `endpoints.ads` | SP/SB/SD 广告管理 |
| 利润 | `endpoints.finance` | 利润核算、结算、应收 |
| 库存 | `endpoints.fba` | FBA 库存、发货 |
| 物流 | `endpoints.logistics` | 物流商、物流渠道 |
| 财务 | `endpoints.finance` | 费用、报表、交易 |
| 订单 | `endpoints.order` | 订单查询、分配 |
| 采购 | `endpoints.purchase` | 采购单、供应商 |
| 退货 | `endpoints.restocking` | 退货分析 |
| 补货 | `endpoints.restocking_limit` | 补货限制 |
| VC | `endpoints.vc` | Vendor Central |
| 基础数据 | `endpoints.basic` | 站点、店铺、类目 |
| 客服 | `endpoints.customer_service` | 客服数据 |
| 目标 | `endpoints.goal` | 销售目标 |
| 工具 | `endpoints.tools` | 通用工具接口 |
| 多平台 | `endpoints.multiplatform` | 多平台数据 |
| 亚马逊来源 | `endpoints.amazon_source` | Amazon 数据源 |
| 关键词 | `endpoints.statistics` | 销量、库存、绩效统计 |

## 开发指南

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
ruff check src/ tests/
```

## License

MIT

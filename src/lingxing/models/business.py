from __future__ import annotations
#!/usr/bin/env python3
"""领星ERP业务数据模型"""

from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

try:
    from pydantic import model_validator
except ImportError:
    from pydantic import root_validator as model_validator


class LingXingBaseModel(BaseModel):
    """领星基础数据模型"""

    model_config = ConfigDict(
        extra="allow",
        ser_json_timedelta="iso8601",
    )


class ProductInfo(LingXingBaseModel):
    """产品信息"""

    product_id: str | None = Field(None, description="产品ID")
    product_name: str | None = Field(None, description="产品名称")
    product_sku: str | None = Field(None, description="产品SKU")
    product_asin: str | None = Field(None, description="产品ASIN")
    product_image: str | None = Field(None, description="产品图片URL")
    product_cost: Decimal | None = Field(None, description="产品成本")
    product_weight: float | None = Field(None, description="产品重量")
    product_status: str | None = Field(None, description="产品状态")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class SupplierInfo(LingXingBaseModel):
    """供应商信息"""

    supplier_id: str | None = Field(None, description="供应商ID")
    supplier_name: str | None = Field(None, description="供应商名称")
    supplier_code: str | None = Field(None, description="供应商编码")
    contact_person: str | None = Field(None, description="联系人")
    contact_phone: str | None = Field(None, description="联系电话")
    address: str | None = Field(None, description="地址")
    status: str | None = Field(None, description="状态")


class PurchaseOrderInfo(LingXingBaseModel):
    """采购单信息 - 包含1688采购订单"""

    purchase_order_id: str | None = Field(None, description="采购单ID")
    purchase_order_no: str | None = Field(None, description="采购单编号")
    supplier_id: str | None = Field(None, description="供应商ID")
    supplier_name: str | None = Field(None, description="供应商名称")
    sku: str | None = Field(None, description="商品SKU")
    product_name: str | None = Field(None, description="商品名称")
    quantity: int | None = Field(None, description="采购数量")
    unit_price: Decimal | None = Field(None, description="单价")
    total_amount: Decimal | None = Field(None, description="总金额")
    status: str | None = Field(None, description="状态: 待采购/待到货/部分到货/已完成/已作废")
    order_time: datetime | None = Field(None, description="下单时间")
    expected_arrival_time: datetime | None = Field(None, description="预计到货时间")
    actual_arrival_time: datetime | None = Field(None, description="实际到货时间")
    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    remark: str | None = Field(None, description="备注")
    is_1688: bool | None = Field(None, description="是否为1688订单")
    source_platform: str | None = Field(None, description="采购来源平台")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class PurchasePlanInfo(LingXingBaseModel):
    """采购计划信息"""

    plan_id: str | None = Field(None, description="采购计划ID")
    plan_no: str | None = Field(None, description="采购计划编号")
    sku: str | None = Field(None, description="商品SKU")
    product_name: str | None = Field(None, description="商品名称")
    planned_quantity: int | None = Field(None, description="计划采购数量")
    purchased_quantity: int | None = Field(None, description="已采购数量")
    pending_quantity: int | None = Field(None, description="待采购数量")
    status: str | None = Field(None, description="状态")
    priority: str | None = Field(None, description="优先级")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class PurchaseReturnInfo(LingXingBaseModel):
    """采购退货单信息"""

    return_id: str | None = Field(None, description="退货单ID")
    return_no: str | None = Field(None, description="退货单编号")
    purchase_order_id: str | None = Field(None, description="原采购单ID")
    purchase_order_no: str | None = Field(None, description="原采购单编号")
    supplier_id: str | None = Field(None, description="供应商ID")
    supplier_name: str | None = Field(None, description="供应商名称")
    sku: str | None = Field(None, description="商品SKU")
    product_name: str | None = Field(None, description="商品名称")
    quantity: int | None = Field(None, description="退货数量")
    return_amount: Decimal | None = Field(None, description="退货金额")
    return_reason: str | None = Field(None, description="退货原因")
    status: str | None = Field(None, description="退货状态")
    return_time: datetime | None = Field(None, description="退货时间")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class OrderInfo(LingXingBaseModel):
    """订单信息"""

    order_id: str | None = Field(None, description="订单ID")
    order_number: str | None = Field(None, description="订单编号")
    platform_order_id: str | None = Field(None, description="平台订单ID")
    store_id: str | None = Field(None, description="店铺ID")
    platform: str | None = Field(None, description="平台")
    order_status: str | None = Field(None, description="订单状态")
    order_amount: Decimal | None = Field(None, description="订单金额")
    order_currency: str | None = Field(None, description="订单币种")
    payment_status: str | None = Field(None, description="支付状态")
    payment_time: datetime | None = Field(None, description="支付时间")
    shipping_address: str | None = Field(None, description="收货地址")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class OrderItem(LingXingBaseModel):
    """订单商品项"""

    item_id: str | None = Field(None, description="商品项ID")
    order_id: str | None = Field(None, description="订单ID")
    product_id: str | None = Field(None, description="产品ID")
    sku: str | None = Field(None, description="商品SKU")
    quantity: int | None = Field(None, description="数量")
    unit_price: Decimal | None = Field(None, description="单价")
    total_price: Decimal | None = Field(None, description="总价")


class InventoryInfo(LingXingBaseModel):
    """库存信息"""

    inventory_id: str | None = Field(None, description="库存ID")
    product_id: str | None = Field(None, description="产品ID")
    sku: str | None = Field(None, description="SKU")
    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    available_quantity: int | None = Field(None, description="可用库存")
    total_quantity: int | None = Field(None, description="总库存")
    in_transit_quantity: int | None = Field(None, description="在途库存")
    update_time: datetime | None = Field(None, description="更新时间")


class WarehouseInfo(LingXingBaseModel):
    """仓库信息"""

    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    warehouse_code: str | None = Field(None, description="仓库编码")
    warehouse_type: str | None = Field(None, description="仓库类型")
    location: str | None = Field(None, description="仓库位置")


class WarehouseInventoryInfo(LingXingBaseModel):
    """仓库库存明细"""

    inventory_id: str | None = Field(None, description="库存ID")
    sku: str | None = Field(None, description="SKU")
    product_name: str | None = Field(None, description="产品名称")
    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    bin_id: str | None = Field(None, description="仓位")
    available_quantity: int | None = Field(None, description="可用库存")
    locked_quantity: int | None = Field(None, description="锁定库存")
    total_quantity: int | None = Field(None, description="总库存")
    in_transit_quantity: int | None = Field(None, description="在途库存")
    cost_price: Decimal | None = Field(None, description="成本价")
    update_time: datetime | None = Field(None, description="更新时间")


class WarehouseStatementInfo(LingXingBaseModel):
    """库存流水"""

    statement_id: str | None = Field(None, description="流水ID")
    sku: str | None = Field(None, description="SKU")
    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    order_type: str | None = Field(None, description="订单类型: 入库/出库/调拨/盘点")
    order_no: str | None = Field(None, description="关联单号")
    quantity_change: int | None = Field(None, description="变动数量 (+/-)")
    quantity_before: int | None = Field(None, description="变动前数量")
    quantity_after: int | None = Field(None, description="变动后数量")
    operator: str | None = Field(None, description="操作人")
    operate_time: datetime | None = Field(None, description="操作时间")
    remark: str | None = Field(None, description="备注")


class AllocationOrderInfo(LingXingBaseModel):
    """调拨单信息"""

    allocation_id: str | None = Field(None, description="调拨单ID")
    allocation_no: str | None = Field(None, description="调拨单号")
    from_warehouse_id: str | None = Field(None, description="源仓库ID")
    from_warehouse_name: str | None = Field(None, description="源仓库名称")
    to_warehouse_id: str | None = Field(None, description="目标仓库ID")
    to_warehouse_name: str | None = Field(None, description="目标仓库名称")
    status: str | None = Field(None, description="状态")
    total_quantity: int | None = Field(None, description="总数量")
    create_time: datetime | None = Field(None, description="创建时间")
    complete_time: datetime | None = Field(None, description="完成时间")
    remark: str | None = Field(None, description="备注")


class CheckOrderInfo(LingXingBaseModel):
    """盘点单信息"""

    check_id: str | None = Field(None, description="盘点单ID")
    check_no: str | None = Field(None, description="盘点单号")
    warehouse_id: str | None = Field(None, description="仓库ID")
    warehouse_name: str | None = Field(None, description="仓库名称")
    status: str | None = Field(None, description="状态")
    create_time: datetime | None = Field(None, description="创建时间")
    check_time: datetime | None = Field(None, description="盘点时间")
    operator: str | None = Field(None, description="操作人")


class FBAShipment(LingXingBaseModel):
    """FBA发货计划"""

    shipment_id: str | None = Field(None, description="发货计划ID")
    shipment_name: str | None = Field(None, description="发货计划名称")
    destination_fulfillment_center: str | None = Field(
        None, description="目的仓库"
    )
    shipment_status: str | None = Field(None, description="发货状态")
    create_time: datetime | None = Field(None, description="创建时间")
    update_time: datetime | None = Field(None, description="更新时间")


class FBAInventory(LingXingBaseModel):
    """FBA库存信息"""

    fnsku: str | None = Field(None, description="FNSKU")
    asin: str | None = Field(None, description="ASIN")
    seller_sku: str | None = Field(None, description="卖家SKU")
    fulfillment_center: str | None = Field(None, description="履约中心")
    total_quantity: int | None = Field(None, description="总库存")
    afn_restocking_quantity: int | None = Field(None, description="AFN补货数量")
    afn_warehouse_quantity: int | None = Field(None, description="AFN仓库数量")



class InboundShipmentInfo(LingXingBaseModel):
    """FBA发货单信息 - 包含头程费用"""

    shipment_id: int | None = Field(None, alias="id", description="发货单ID")
    shipment_no: str | None = Field(None, alias="shipment_sn", description="发货单编号")
    store_id: int | None = Field(None, alias="sid", description="店铺ID")
    store_name: str | None = Field(None, alias="sname", description="店铺名称")
    destination_fulfillment_center: str | None = Field(None, alias="destination_fulfillment_center_id", description="目的FBA仓库")
    status: int | None = Field(None, description="发货单状态: -1待配货, 0待发货, 1已发货, 2已完成, 3已作废")
    status_name: str | None = Field(None, description="状态名称")
    total_quantity: int | None = Field(None, description="总数量")
    total_cost: Decimal | None = Field(None, description="总成本")
    head_logistics_cost: Decimal | None = Field(None, description="头程运费")
    customs_cost: Decimal | None = Field(None, description="关税")
    other_cost: Decimal | None = Field(None, description="其他费用")
    logistics_provider: str | None = Field(None, description="物流商")
    logistics_channel: str | None = Field(None, alias="logistics_channel_name", description="物流渠道")
    shipping_method: str | None = Field(None, description="运输方式(海运/空运/快递)")
    create_time: datetime | None = Field(None, description="创建时间")
    ship_time: datetime | None = Field(None, alias="shipment_time", description="发货时间")
    arrival_time: datetime | None = Field(None, alias="eta_date", description="预计到达时间")
    warehouse_id: int | None = Field(None, alias="wid", description="仓库ID")
    warehouse_name: str | None = Field(None, alias="wname", description="仓库名称")
    create_user: str | None = Field(None, description="创建人")
    update_time: datetime | None = Field(None, description="更新时间")

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode='before')
    @classmethod
    def handle_empty_datetime(cls, data: dict) -> dict:
        """处理空字符串的日期时间字段"""
        if isinstance(data, dict):
            datetime_fields = ['shipment_time', 'eta_date', 'create_time', 'update_time']
            for field in datetime_fields:
                if field in data and data[field] == '':
                    data[field] = None
        return data


class ShipmentDetailInfo(LingXingBaseModel):
    """发货单明细 - SKU级别的运费分配"""

    shipment_id: str | None = Field(None, description="发货单ID")
    sku: str | None = Field(None, description="SKU")
    msku: str | None = Field(None, description="MSKU")
    fnsku: str | None = Field(None, description="FNSKU")
    asin: str | None = Field(None, description="ASIN")
    product_name: str | None = Field(None, description="产品名称")
    quantity: int | None = Field(None, description="数量")
    unit_cost: Decimal | None = Field(None, description="单件成本")
    allocated_logistics_cost: Decimal | None = Field(None, description="分配的头程运费")
    allocated_customs_cost: Decimal | None = Field(None, description="分配的关税")
    total_cost: Decimal | None = Field(None, description="总成本")


class LogisticsProviderInfo(LingXingBaseModel):
    """头程物流商信息"""

    provider_id: str | None = Field(None, description="物流商ID")
    provider_name: str | None = Field(None, description="物流商名称")
    provider_code: str | None = Field(None, description="物流商编码")
    contact_person: str | None = Field(None, description="联系人")
    contact_phone: str | None = Field(None, description="联系电话")
    status: str | None = Field(None, description="状态")


class LogisticsChannelInfo(LingXingBaseModel):
    """头程物流渠道信息"""

    channel_id: str | None = Field(None, alias="id", description="渠道ID")
    channel_name: str | None = Field(None, description="渠道名称")
    provider_id: str | None = Field(None, description="物流商ID")
    provider_name: str | None = Field(None, description="物流商名称")
    method_id: str | None = Field(None, description="运输方式ID")
    method_name: str | None = Field(None, description="运输方式名称")
    shipping_method: str | None = Field(None, description="运输方式(海运/空运/快递)")
    status: int | None = Field(None, alias="enabled", description="状态: 1启用, 0禁用")
    billing_type: int | None = Field(None, description="计费类型")
    volume_calc_param: int | None = Field(None, description="体积计算参数")
    valid_period: int | None = Field(None, description="有效期")
    send_place_codes: list[str] | None = Field(None, description="发货地代码列表")
    receive_country_codes: list[str] | None = Field(None, description="收货国家代码列表")
    is_include_tax: int | None = Field(None, description="是否含税")
    is_points_behind: int | None = Field(None, description="是否积分后置")
    points_behind_coeffient: Decimal | None = Field(None, description="积分后置系数")
    last_modify_uid: int | None = Field(None, description="最后修改人ID")
    gmt_modified: str | None = Field(None, description="最后修改时间")
    remark: str | None = Field(None, description="备注")
    freight: list[dict] | None = Field(None, description="运费规则")

    model_config = ConfigDict(populate_by_name=True)

    @model_validator(mode='before')
    @classmethod
    def extract_provider_info(cls, data: dict) -> dict:
        """从嵌套的 provider 对象中提取信息"""
        if isinstance(data, dict):
            # 提取 provider 信息
            provider = data.get('provider', {})
            if isinstance(provider, dict):
                if 'provider_id' not in data:
                    data['provider_id'] = provider.get('id')
                if 'provider_name' not in data:
                    data['provider_name'] = provider.get('logistics_provider_name')
            # 使用 method_name 作为 shipping_method
            if 'shipping_method' not in data and data.get('method_name'):
                data['shipping_method'] = data['method_name']
        return data



class StoreInfo(LingXingBaseModel):
    """店铺信息 - 根据领星API文档定义"""

    sid: int | None = Field(None, description="领星ERP对企业已授权店铺的唯一标识")
    mid: int | None = Field(None, description="站点ID")
    name: str | None = Field(None, description="店铺名称")
    seller_id: str | None = Field(None, description="亚马逊店铺ID")
    account_name: str | None = Field(None, description="店铺账户名称")
    seller_account_id: int | None = Field(None, description="店铺账号ID")
    region: str | None = Field(None, description="站点简称，例如NA指北美")
    country: str | None = Field(None, description="商城所在国家名称，例如西班牙")
    has_ads_setting: int | None = Field(None, description="是否授权广告：0否 1是")
    marketplace_id: str | None = Field(None, description="市场ID")
    status: int | None = Field(None, description="店铺状态：0停止同步 1正常 2授权异常 3欠费停服")


class FinanceRecord(LingXingBaseModel):
    """财务记录"""

    record_id: str | None = Field(None, description="记录ID")
    record_type: str | None = Field(None, description="记录类型")
    order_id: str | None = Field(None, description="订单ID")
    amount: Decimal | None = Field(None, description="金额")
    currency: str | None = Field(None, description="币种")
    transaction_date: datetime | None = Field(None, description="交易日期")
    remark: str | None = Field(None, description="备注")


class OrderProfitInfo(LingXingBaseModel):
    """订单利润信息"""

    order_id: str | None = Field(None, description="订单ID")
    msku: str | None = Field(None, description="MSKU")
    asin: str | None = Field(None, description="ASIN")
    sku: str | None = Field(None, description="SKU")
    store_id: str | None = Field(None, description="店铺ID")
    order_time: datetime | None = Field(None, description="订单时间")
    sales_amount: Decimal | None = Field(None, description="销售额")
    product_cost: Decimal | None = Field(None, description="产品成本")
    head_cost: Decimal | None = Field(None, description="头程成本")
    fba_fee: Decimal | None = Field(None, description="FBA费用")
    commission: Decimal | None = Field(None, description="佣金")
    advertising_fee: Decimal | None = Field(None, description="广告费")
    other_fee: Decimal | None = Field(None, description="其他费用")
    profit: Decimal | None = Field(None, description="利润")
    profit_rate: float | None = Field(None, description="利润率")


class MSKUProfitInfo(LingXingBaseModel):
    """MSKU维度利润信息"""

    msku: str | None = Field(None, description="MSKU")
    asin: str | None = Field(None, description="ASIN")
    sku: str | None = Field(None, description="SKU")
    store_id: str | None = Field(None, description="店铺ID")
    start_date: datetime | None = Field(None, description="统计开始日期")
    end_date: datetime | None = Field(None, description="统计结束日期")
    sales_quantity: int | None = Field(None, description="销售数量")
    sales_amount: Decimal | None = Field(None, description="销售额")
    product_cost: Decimal | None = Field(None, description="产品成本")
    head_cost: Decimal | None = Field(None, description="头程成本")
    fba_fee: Decimal | None = Field(None, description="FBA费用")
    commission: Decimal | None = Field(None, description="佣金")
    advertising_fee: Decimal | None = Field(None, description="广告费")
    other_fee: Decimal | None = Field(None, description="其他费用")
    profit: Decimal | None = Field(None, description="利润")
    profit_rate: float | None = Field(None, description="利润率")


class SettlementInfo(LingXingBaseModel):
    """结算明细信息"""

    settlement_id: str | None = Field(None, description="结算ID")
    order_id: str | None = Field(None, description="订单ID")
    transaction_type: str | None = Field(None, description="交易类型")
    amount: Decimal | None = Field(None, description="金额")
    currency: str | None = Field(None, description="币种")
    transaction_time: datetime | None = Field(None, description="交易时间")
    description: str | None = Field(None, description="描述")
    store_id: str | None = Field(None, description="店铺ID")


class SettlementSummaryInfo(LingXingBaseModel):
    """结算汇总信息"""

    store_id: str | None = Field(None, description="店铺ID")
    settlement_date: datetime | None = Field(None, description="结算日期")
    total_amount: Decimal | None = Field(None, description="总金额")
    currency: str | None = Field(None, description="币种")
    status: str | None = Field(None, description="状态")
    settlement_id: str | None = Field(None, description="结算ID")


class SyncStatus(str):
    """同步状态枚举"""

    PENDING = "pending"  # 待同步
    SYNCING = "syncing"  # 同步中
    SUCCESS = "success"  # 成功
    FAILED = "failed"  # 失败
    PARTIAL = "partial"  # 部分成功


class SyncTask(LingXingBaseModel):
    """同步任务"""

    task_id: str | None = Field(None, description="任务ID")
    task_type: str | None = Field(None, description="任务类型")
    status: str | None = Field(None, description="状态")
    start_time: datetime | None = Field(None, description="开始时间")
    end_time: datetime | None = Field(None, description="结束时间")
    total_records: int | None = Field(None, description="总记录数")
    success_records: int | None = Field(None, description="成功记录数")
    failed_records: int | None = Field(None, description="失败记录数")
    error_message: str | None = Field(None, description="错误信息")


class SyncProgress(LingXingBaseModel):
    """同步进度"""

    task_id: str | None = Field(None, description="任务ID")
    current_page: int | None = Field(None, description="当前页")
    total_pages: int | None = Field(None, description="总页数")
    percentage: float | None = Field(None, description="百分比")
    message: str | None = Field(None, description="消息")


class LingXingResponse(LingXingBaseModel):
    """领星API响应封装"""

    code: int | None = Field(None, description="响应码")
    message: str | None = Field(None, description="响应消息")
    data: Any | None = Field(None, description="响应数据")
    request_id: str | None = Field(None, description="请求ID")

    @property
    def is_success(self) -> bool:
        """是否成功 - 领星API返回code=0表示成功"""
        return self.code == 0

    @property
    def error_details(self) -> dict[str, Any] | None:
        """错误详情"""
        if not self.is_success:
            return {
                "code": self.code,
                "message": self.message,
                "request_id": self.request_id,
            }
        return None


class StockoutRiskAlert(LingXingBaseModel):
    """缺货风险预警"""
    sku: str | None = Field(None, description="SKU")
    product_name: str | None = Field(None, description="产品名称")
    available_days: int | None = Field(None, description="可售天数")
    out_stock_flag: int | None = Field(None, description="断货标记")


class SlowMovingAlert(LingXingBaseModel):
    """滞销预警"""
    sku: str | None = Field(None, description="SKU")
    product_name: str | None = Field(None, description="产品名称")
    available_sale_days: int | None = Field(None, description="可售天数")
    inventory_quantity: int | None = Field(None, description="库存数量")


class ReplenishmentRecommendation(LingXingBaseModel):
    """补货推荐"""
    sku: str | None = Field(None, description="SKU")
    product_name: str | None = Field(None, description="产品名称")
    quantity_sug_purchase: int | None = Field(None, description="建议采购数量")
    restock_date: datetime | None = Field(None, description="建议补货日期")


__all__ = [
    "AllocationOrderInfo",
    "CheckOrderInfo",
    "FBAInventory",
    # FBA
    "FBAShipment",
    # 财务
    "FinanceRecord",
    # 头程物流
    "InboundShipmentInfo",
    # 库存
    "InventoryInfo",
    # 基础
    "LingXingBaseModel",
    # 响应
    "LingXingResponse",
    "LogisticsChannelInfo",
    "LogisticsProviderInfo",
    "MSKUProfitInfo",
    # 订单
    "OrderInfo",
    "OrderItem",
    "OrderProfitInfo",
    # 产品
    "ProductInfo",
    # 采购
    "PurchaseOrderInfo",
    "PurchasePlanInfo",
    "PurchaseReturnInfo",
    "ReplenishmentRecommendation",
    "SettlementInfo",
    "SettlementSummaryInfo",
    "ShipmentDetailInfo",
    "SlowMovingAlert",
    # 库存预警
    "StockoutRiskAlert",
    # 店铺
    "StoreInfo",
    "SupplierInfo",
    "SyncProgress",
    # 同步
    "SyncStatus",
    "SyncTask",
    "WarehouseInfo",
    "WarehouseInventoryInfo",
    "WarehouseStatementInfo",
]

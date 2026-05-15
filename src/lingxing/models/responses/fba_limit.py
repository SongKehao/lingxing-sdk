"""Auto-generated response models for FBALimit."""
from typing import Any, List, Optional

from pydantic import Field

from ..common import LingXingModel


class ReplenishmentrestrictionPageListData(LingXingModel):
    """data sub-structure."""
    month: Optional[list] = Field(None, description="月份【近4个月份】")

class ReplenishmentrestrictionPageListList(LingXingModel):
    """list sub-structure."""
    sid: Optional[str] = Field(None, description="店铺id")
    vol_unit_type: Optional[int] = Field(None, description="体积单位类型： 1 立方米 2 立方英尺")
    ipi: Optional[int] = Field(None, description="IPI")
    update_type: Optional[int] = Field(None, description="更新类型： 1 插件 2 手动 3 导入")
    excess_inventory_rate: Optional[str] = Field(None, description="冗余库存率")
    excess_inventory_color: Optional[int] = Field(None, description="冗余库存颜色： 1 dark-green 2 light-green 3 yellow 4 red")
    sell_through_rate: Optional[str] = Field(None, description="售出率")
    sell_through_color: Optional[int] = Field(None, description="售出率颜色： 1 dark-green 2 light-green 3 yellow 4 red")
    stranded_inventory_rate: Optional[str] = Field(None, description="无在售信息的库存率")
    stranded_inventory_color: Optional[int] = Field(None, description="无在售信息的库存率颜色： 1 dark-green 2 light-green 3 yellow 4 red")
    in_stock_rate: Optional[str] = Field(None, description="有存货库存率")
    in_stock_color: Optional[int] = Field(None, description="有存货库存率颜色： 1 dark-green 2 light-green 3 yellow 4 red")
    create_time: Optional[str] = Field(None, description="创建时间")
    update_time: Optional[str] = Field(None, description="更新时间")
    update_time_report: Optional[str] = Field(None, description="报告更新时间")
    items: Optional[list] = Field(None, description="子项数据")
    overview: Optional[dict] = Field(None, description="当月数据")
    sub_items: Optional[list] = Field(None, description="子项数据")

class ReplenishmentrestrictionPageListResponse(LingXingModel):
    """查询补货限制列表."""
    total: Optional[int] = Field(None, description="总数")
    data: Optional[List[ReplenishmentrestrictionPageListData]] = Field(None, description="月份数据")


class FbalimitRestockGetipiinfoSubItems(LingXingModel):
    """sub_items sub-structure."""
    qty_predict_remain: Optional[float] = Field(None, description="预计剩余量（数量）")
    qty_predict_used: Optional[float] = Field(None, description="预计占用量（数量）")
    qty_stock_max: Optional[float] = Field(None, description="最高库存水平（数量）")
    qty_stock_remain: Optional[float] = Field(None, description="实际剩余量（数量）")
    qty_stock_used: Optional[float] = Field(None, description="库存限额使用量（数量）")
    storage_type: Optional[str] = Field(None, description="Standard标准尺寸 Oversize大件 Apparel服装 Footwear鞋靴")
    vol_predict_remain: Optional[str] = Field(None, description="预计剩余量（体积）")
    vol_predict_used: Optional[str] = Field(None, description="预计占用量（体积）")
    vol_stock_max: Optional[str] = Field(None, description="最高库存水平（体积）")
    vol_stock_remain: Optional[str] = Field(None, description="实际剩余量（体积）")
    vol_stock_used: Optional[str] = Field(None, description="库存限额使用量（体积）")
    vol_unit_type: Optional[int] = Field(None, description="单位： 1 立方米 2 立方英尺")

class FbalimitRestockGetipiinfoResponse(LingXingModel):
    """查询IPI信息."""
    total: Optional[int] = Field(None, description="总数")
    seller_id: Optional[str] = Field(None, description="亚马逊店铺id")
    seller_account_name: Optional[str] = Field(None, description="店铺账户名称")
    seller_name: Optional[str] = Field(None, description="店铺名称")
    marketplace: Optional[str] = Field(None, description="国家")
    update_date: Optional[str] = Field(None, description="更新时间")
    vol_unit_text: Optional[str] = Field(None, description="体积单位")
    ipi: Optional[float] = Field(None, description="IPI")
    excess_inventory_rate: Optional[float] = Field(None, description="冗余库存")
    sell_through_rate: Optional[float] = Field(None, description="售出率")
    stranded_inventory_rate: Optional[float] = Field(None, description="无在售信息的库存")
    in_stock_rate: Optional[float] = Field(None, description="有存货库存")
    sub_items: Optional[List[FbalimitRestockGetipiinfoSubItems]] = Field(None, description="是")

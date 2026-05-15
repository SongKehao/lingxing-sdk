"""FBA发货 API endpoints."""
from __future__ import annotations

from ..models.fba import (
    GetFbaProductListItem,
    GetHeadLogisticsFeeTypesItem,
    GetInboundShipmentListItem,
    GetSeaTrackSupplierCarriersItem,
    ShipmentPlanListsItem,
)
from ._base import BaseEndpoint


class FBAEndpoints(BaseEndpoint):
    """领星FBA发货 API (31个接口)."""

    async def box_info(self, **kwargs) -> list | dict:
        """查询货件装箱信息.

POST /erp/sc/routing/fba/shipment/boxInfo

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    shipment_id: 货件编号 (required), string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/boxInfo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_sended_order(self, **kwargs) -> dict:
        """生成已发货的发货单.

POST /erp/sc/storage/shipment/createSendedOrder

Args:
    wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid, int.
    sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (required), int.
    expected_arrival_date: 预计到达时间：Y-m-d, string.
    etd_date: 开船时间，格式：Y-m-d, string.
    eta_date: 预计到港时间，格式：Y-m-d, string.
    delivery_date: 实际妥投时间，格式：Y-m-d, string.
    actual_shipment_time: 实际发货时间，格式：Y-m-d, string.
    head_fee_type: 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积, int.
    tax_fee_type: 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 5 箱子-体积, int.
    is_points_behind: 是否分抛计算：0 否，1 是，头程分摊方式为按计费重时用, int.
    points_behind_coeffient: 分抛系数：0~100，分抛计算选是时必填, int.
    logistics_channel_id: 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】, int.
    is_related: 组合商品扣减库存时是否自动拆分成单品进行扣减： 0 否 1 是【会拆分组合商品】, int.
    request_flag: 自定义请求标识，本次请求超时后可根据此标识查询此次请求的结果，由请求方保持标识唯一性, string.
    ship_mode: 发货方式：1-默认，2-工厂直发, int.
    hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是, int.
    remark: 备注, string.
    box_type: 装箱类型： SINGLE 每箱只允许一款SKU MULTIPLE 每箱允许多款SKU, string.
    box_remark: 装箱备注, string.
    box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填, array.
    logistics_list_type: 物流信息版本： 0 旧版 1 新版, int.
    head_logistics_list: 新版头程物流信息 (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/storage/shipment/createSendedOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def create_ship_from_address(self, **kwargs) -> dict:
        """地址簿-发货地址创建.

POST /erp/sc/routing/fba/shipment/createShipFromAddress

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    alias_name: 地址簿别名，店铺内唯一 (required), string.
    country_name: 发货国家/地区 (required), string.
    sender_name: 发货方名称 (required), string.
    street_detail1: 街道地址1 (required), string.
    street_detail2: 街道地址2, string.
    city: 城市 (required), string.
    region: 区, string.
    province: 省/州/地区，美国发货地址限制长度为2位 (required), string.
    zip_code: 邮政编码 (required), string.
    phone: 电话号码, string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/createShipFromAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def create_shipment_plan(self, **kwargs) -> dict:
        """创建FBA发货计划.

POST /erp/sc/routing/storage/shipment/createShipmentPlan

Args:
    remark: 批次信息备注, string.
    product_list: 商品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/createShipmentPlan", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_received_inventory(self, **kwargs) -> dict:
        """查询FBA到货接收明细.

POST /erp/sc/data/fba_report/receivedInventory

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    event_date: 签收日期，格式：Y-m-d，未填写fba_shipment_id时必填 (required), string.
    fba_shipment_id: 货件单号，未填写event_date时必填, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int."""
        resp = await self._post("/erp/sc/data/fba_report/receivedInventory", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_shipment_list(self, **kwargs) -> list | dict:
        """查询货件列表.

POST /erp/sc/data/fba_report/shipmentList

Args:
    sid: 店铺id，多个以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    start_date: 货件创建开始日期，格式：Y-m-d，左闭右开 (required), string.
    end_date: 货件创建截止日期，格式：Y-m-d，左闭右开 (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000, int.
    shipment_id: 货件单号，多个以英文逗号隔开，仅支持精确搜索, string.
    shipment_status: 货件状态，多个以英文逗号分隔： UNCONFIRMED IN_TRANSIT DELIVERED CHECKED_IN ABANDONED  DELETED CLOSED CANCELLED WORKING RECEIVING SHIPPED READY_TO_SHIP, string.
    extra_date_field: 根据start_extra_date和end_extra_date日期范围查询： update 货件修改日期【默认值为update，目前只支持查询货件修改日期】, string.
    start_extra_date: 开始日期，格式：Y-m-d，左闭右开, string.
    end_extra_date: 结束日期，格式：Y-m-d，左闭右开, string."""
        resp = await self._post("/erp/sc/data/fba_report/shipmentList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_fba_product_list(self, **kwargs) -> list[GetFbaProductListItem]:
        """查询FBA商品信息列表.

POST /erp/sc/routing/fba/shipment/getFbaProductList

Args:
    sids: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 模糊搜索字段：【搜索时支持以下单个字段】 msku=>MSKU fnsku=>FNSKU asin=>ASIN sku=>SKU title=>标题 product_name=>品名, string.
    search_value: 搜索值【对应搜索字段的值】, string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/getFbaProductList", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetFbaProductListItem)
    async def get_head_logistics_fee_types(self, **kwargs) -> list[GetHeadLogisticsFeeTypesItem]:
        """获取发货单头程物流信息-其他费类型.

POST /erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes"""
        resp = await self._post("/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetHeadLogisticsFeeTypesItem)
    async def get_inbound_shipment_list(self, **kwargs) -> tuple[list[GetInboundShipmentListItem], int]:
        """查询发货单列表.

POST /erp/sc/routing/storage/shipment/getInboundShipmentList

Args:
    search_value: 搜索的值, string.
    search_field: 搜索字段： sku shipment_sn 发货单号 shipment_id 货件单号, string.
    sids: 店铺id,多个时通过英文逗号分隔,如1,2,3，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    mids: 国家id,多个时通过英文逗号分隔,如1,2,3, string.
    wid: 仓库id,多个时通过英文逗号分隔,如1,2,3, string.
    logistics_type: 物流方式id, array.
    status: 发货单状态： -1 : 待配货，  0：待发货， 1：已发货， 3：已作废， 4：已删除, int.
    print_status: 打印状态 0未打印 1 已打印, string.
    pick_status: 拣货状态 0 未拣货 1已拣货, string.
    time_type: 时间类型：  3创建时间 (允许精确到时分秒)  2创建时间  1到货时间   0发货时间  4更新时间 (允许精确到时分秒), int.
    start_date: 开始日期, string.
    end_date: 结束日期, string.
    offset: 偏移量=（currentPage -1）*length (required), int.
    length: 长度 (required), int.
    is_delete: 是否删除：0 未删除【默认】 1 已删除 2 全部, number.
    senior_search_list: 精准搜索, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentList", kwargs if kwargs else None)
        return self._parse_page(resp.data, GetInboundShipmentListItem)
    async def get_inbound_shipment_list_mws_detail_list(self, **kwargs) -> list | dict:
        """批量查询发货单详情.

POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList

Args:
    shipment_sn_arr: 发货单号数组，上限50 (required), array.
    return_deleted: 是否返回已删除数据: false-否(默认)，true-是, boolean."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_sea_track_supplier_carriers(self, **kwargs) -> list[GetSeaTrackSupplierCarriersItem]:
        """获取发货单头程物流信息-承运商信息.

POST /erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers

Args:
    vehicle_type: 运输类型【默认Sea】： Sea 海运 Express 快递 Aviation 空运, string."""
        resp = await self._post("/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetSeaTrackSupplierCarriersItem)
    async def invalid_shipment_sn(self, **kwargs) -> list | dict:
        """FBA-作废发货单.

POST /basicOpen/openapi/fbaShipment/shipmentSn/invalid

Args:
    shipmentNos: 发货单号 (required), array.
    isReturnStock: 产品库存是否恢复 1恢复 0不恢复 (required), int.
    isReturnStockAux: 辅料库存是否恢复 1恢复 0不恢复 (required), int.
    cancelReason: 作废原因, string."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shipmentSn/invalid", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def send_goods(self, **kwargs) -> dict:
        """FBA发货单发货.

POST /erp/sc/storage/shipment/sendGoods

Args:
    shipment_nos: 发货单号列表 (required), array."""
        resp = await self._post("/erp/sc/storage/shipment/sendGoods", kwargs if kwargs else None)
        return resp.data or {}
    async def ship_from_address_list(self, **kwargs) -> dict:
        """地址簿-发货地址列表.

POST /erp/sc/routing/fba/shipment/shipFromAddressList

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】, array.
    search_field: 搜索字段： alias_name 地址簿别名 sender_name 发货方名称, string.
    search_value: 对应搜索字段模糊搜索值, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/shipFromAddressList", kwargs if kwargs else None)
        return resp.data or {}
    async def shipment_lock_stock(self, **kwargs) -> list | dict:
        """发货单分配库存.

POST /erp/sc/routing/storage/shipment/lockStock

Args:
    shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (required), array.
    is_auto_batch: 是否锁定至批次，1：是，0：否，默认为否，否：只锁定库存数量，发货时按先进先出规则匹配出库批次；是：按先进先锁规则自动指定批次并锁定，发货时按锁定批次出库；分配库存后，可在【查询发货单详情】接口的采购信息中查看锁定的批次, int."""
        resp = await self._post("/erp/sc/routing/storage/shipment/lockStock", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipment_plan_lists(self, **kwargs) -> list[ShipmentPlanListsItem]:
        """查询FBA发货计划.

POST /erp/sc/data/fba_report/shipmentPlanLists

Args:
    sids: 店铺ids，12,13组成，对应查询亚马逊店铺列表接口对应字段【sid】, string.
    wid: 仓库id, string.
    packing_type: 包装类型2原装 1混装, string.
    search_field_time: 查找时间字段(gmt_create-创建时间,estimated_delivery_time-计划发货时间)，不传该字段默认为gmt_create, string.
    search_field: 查找字段  order_sn发货计划单号, string.
    search_value: 查找值, string.
    status: 状态, string.
    mids: 国家id, string.
    offset: 偏移量 0 偏移量 (currentPage -1) * length, int.
    length: 长度 默认20, int.
    start_date: 开始日期 如:2021-09-07, string.
    end_date: 结束日期 如:2021-09-08, string."""
        resp = await self._post("/erp/sc/data/fba_report/shipmentPlanLists", kwargs if kwargs else None)
        return self._parse_list(resp.data, ShipmentPlanListsItem)
    async def shopping_address(self, **kwargs) -> dict:
        """地址簿-配送地址详情.

POST /basicOpen/openapi/fbaShipment/shoppingAddress

Args:
    id: 唯一记录id，查询FBA列表接口对应字段【id】 (required), int."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/shoppingAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def sync_shipment(self, **kwargs) -> dict:
        """同步亚马逊货件到ERP.

POST /erp/sc/routing/fba/shipment/syncShipment

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    shipment_ids: 货件编号 (required), array.
    sync_anyway: 报错是否继续：0 否【默认】，1 是 当系统检测到货件归属国家与店铺不符时，会提示报错，此时传1则按照店铺进行同步, int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/syncShipment", kwargs if kwargs else None)
        return resp.data or {}
    async def update_custom_cost(self, **kwargs) -> dict:
        """更新发货单自定义成本.

POST /erp/sc/routing/storage/shipment/updateCustomCost

Args:
    shipment_sn: 发货单号 (required), string.
    is_custom_cost: 是否自定义成本 (required), int.
    list: 自定义成本信息数组, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateCustomCost", kwargs if kwargs else None)
        return resp.data or {}
    async def update_plan_lists(self, **kwargs) -> dict:
        """编辑FBA发货计划.

POST /erp/sc/routing/storage/shipment/updateShipmentPlan

Args:
    order_sn: 发货计划单号 (required), string.
    shipment_time: 发货时间，格式：Y-m-d, string.
    packing_type: 包装类型： 1 混装，2 原厂, int.
    logistics_provider_id: 物流商id, int.
    logistics_channel_id: 物流渠道id, int.
    shipment_plan_quantity: 计划发货量, int.
    quantity_in_case: 单箱数量（PCS）, int.
    box_num: 箱数, int.
    sys_wid: 系统仓库id【发货仓库】, int.
    cg_package_length: 包装规格长（cm）【保留两位小数】, number.
    cg_package_width: 包装规格宽（cm）【保留两位小数】, number.
    cg_package_height: 包装规格高（cm）【保留两位小数】, number.
    cg_box_length: 箱规长（cm）【保留两位小数】, number.
    cg_box_width: 箱规宽（cm）【保留两位小数】, number.
    cg_box_height: 箱规高（cm）【保留两位小数】, number.
    nw: 单品净重（g）【保留两位小数】, number.
    gw: 单品毛重（g）【保留两位小数】, number.
    cg_box_weight: 单箱重量（kg）【保留两位小数】, number.
    remark: 备注, string."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentPlan", kwargs if kwargs else None)
        return resp.data or {}
    async def update_ship_from_address(self, **kwargs) -> dict:
        """地址簿-发货地址修改.

POST /erp/sc/routing/fba/shipment/updateShipFromAddress

Args:
    sid: 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), int.
    alias_name: 地址簿别名，店铺内唯一 (required), string.
    country_name: 发货国家/地区 (required), string.
    sender_name: 发货方名称 (required), string.
    street_detail1: 街道地址1 (required), string.
    street_detail2: 街道地址2, string.
    city: 城市 (required), string.
    region: 区, string.
    province: 省/州/地区，美国发货地址限制长度为2位 (required), string.
    zip_code: 邮政编码 (required), string.
    phone: 电话号码, string.
    id: 地址簿-发货地址列表接口返回id (required), int."""
        resp = await self._post("/erp/sc/routing/fba/shipment/updateShipFromAddress", kwargs if kwargs else None)
        return resp.data or {}
    async def update_shipment_actual_status(self, **kwargs) -> dict:
        """修改货件实际状态.

POST /erp/sc/routing/storage/shipment/updateShipmentActualStatus

Args:
    is_closed: 货件状态：0 进行中，1 已完成 (required), int.
    list: 货件信息 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateShipmentActualStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def vc_batch_send_goods(self, **kwargs) -> dict:
        """VC发货单-确认发货.

POST /basicOpen/openapi/getInvoice/invoice/batchSendGoods

Args:
    orderNoList: orderNo列表, array."""
        resp = await self._post("/basicOpen/openapi/getInvoice/invoice/batchSendGoods", kwargs if kwargs else None)
        return resp.data or {}
    async def create_ready_send_order(self, **kwargs) -> dict:
        """生成待发货的发货单.

POST /erp/sc/routing/storage/shipment/createReadySendOrder

Args:
    wid: 自定义仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。, int.
    sys_wid: 系统仓库 ID。wid 和 sys_wid 至少传一个，若都传则优先用 wid。多仓库发货时传 -1。, int.
    expected_arrival_date: 预计到达时间，格式：Y-m-d, string.
    etd_date: 开船时间，格式：Y-m-d, string.
    eta_date: 预计到港时间，格式：Y-m-d, string.
    delivery_date: 实际妥投时间，格式：Y-m-d, string.
    actual_shipment_time: 实际发货时间，格式：Y-m-d, string.
    head_fee_type: 头程费分配方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积, int.
    tax_fee_type: 实际税费分配方式：【默认0】 0 产品-计费重 1 产品-实重 2 产品-体积重 3 产品-数量 4 自定义 5 箱子-体积, int.
    is_points_behind: 是否分抛计算：0 否，1 是；头程分摊方式为按计费重时用, int.
    points_behind_coeffient: 分抛系数：0~100,分抛计算选是时必填, int.
    logistics_channel_id: 物流渠道id：按计费重分摊时必填，以获取材积参数用于计算 查询头程物流渠道列表接口对应字段【id】, int.
    is_related: 是否关联普通商品： 0 否 1 是【会拆分组合商品】, int.
    vat_code: 店铺VAT税号, string.
    is_pick: 是否拣货：【默认0】 0 否 1 是, int.
    remark: 备注, string.
    ship_mode: 发货方式：1-默认，2-工厂直发, int.
    hand_pick_purchase: 工厂直发时手动选择出库批次：1-否，2-是, int.
    box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU, string.
    box_remark: 装箱备注, string.
    box_list: 箱规列表，每个子项代表一个箱规，在装箱类型为MULTIPLE时必填 (required), array.
    logistics_list_type: 物流信息版本： 0 旧版 1 新版, int.
    head_logistics_list: 新版头程物流信息 (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/createReadySendOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_inbound_shipment_list_mws_detail(self, **kwargs) -> list | dict:
        """查询发货单详情.

POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail

Args:
    shipment_sn: 发货单号 (required), string.
    return_deleted: 是否返回已删除数据: false-否(默认)，true-是, boolean."""
        resp = await self._post("/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_order_release_stock(self, **kwargs) -> dict:
        """发货单释放库存.

POST /erp/sc/routing/storage/shipment/releaseStock

Args:
    shipment_nos: 发货单号 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/releaseStock", kwargs if kwargs else None)
        return resp.data or {}
    async def print_fba_labels(self, **kwargs) -> dict:
        """查询FBA货件箱子、卡板标签.

POST /erp/sc/storage/shipment/printFbaLabels

Args:
    data: 请求数据 (required), array.
    hide_ship_from_company_name: 隐藏ship from公司名,默认不隐藏,非必填,传值1为开启, int.
    hide_ship_to_company_name: 传值1为隐藏ship to公司名,默认不隐藏,非必填,传值1为开启, int.
    print_sta_name_page: 传值1为新增任务名称页,默认不新增,非必填,仅打印box箱子标签时生效,传值1为开启, int.
    sort_label: 传值1为按箱子顺序重排,默认不按箱子顺序重排,仅打印box箱子子标签时生效(说明:不按箱子顺序重排时,打印文件, int.
    type: 打印类型：box 箱子标签，card 卡板标签 (required), string."""
        resp = await self._post("/erp/sc/storage/shipment/printFbaLabels", kwargs if kwargs else None)
        return resp.data or {}
    async def print_fnsku_labels(self, **kwargs) -> dict:
        """查询FBA货件商品FNSKU标签.

POST /erp/sc/storage/shipment/printFnskuLabels

Args:
    page_type: 标签页面类型： SINGLE_COL_50_30 热敏纸【50X30】单排 SINGLE_COL_70_30 热敏纸【70X30】单排 DOUBLE_COL_100_30 热敏纸【100X30】双排 A4_FOUR_COL_40 A4纸【每页40个标签】四排 A4_FOUR_COL_44 A4纸【每页44个标签】四排 US_LETTER_THREE_COL_30 美国信纸【每页30个标签】三排 (required), string.
    print_content: 是否打印：【默认yes】 yes 是 no 否, string.
    content_type: 打印SKU/品名：【默认sku】 sku SKU sku_name 品名, string.
    print_custom: 是否打印自定义内容：【默认yes】 yes 是 no 否, string.
    custom_content: 自定义内容，默认MADE IN CHINA, string.
    new_tag: 标签中是否显示‘new’字样：【默认yes】 yes 是 no 否, string."""
        resp = await self._post("/erp/sc/storage/shipment/printFnskuLabels", kwargs if kwargs else None)
        return resp.data or {}
    async def search_process_result(self, **kwargs) -> list | dict:
        """发货单创建接口结果查询.

POST /erp/sc/routing/storage/shipment/searchProcessResult

Args:
    request_flag: 生成单据时传的请求标识 (required), string."""
        resp = await self._post("/erp/sc/routing/storage/shipment/searchProcessResult", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_inbound_shipment_list_mws(self, **kwargs) -> dict:
        """编辑发货单.

POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws

Args:
    shipment_sn: 发货单号 (required), string.
    remark: 备注, string.
    items: 发货商品, array.
    box_type: 装箱类型：SINGLE-每箱只允许一款SKU，MULTIPLE-每箱允许多款SKU, string.
    box_list: 装箱数据, array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateInboundShipmentListMws", kwargs if kwargs else None)
        return resp.data or {}
    async def update_list_logistics(self, **kwargs) -> dict:
        """更新发货单物流信息.

POST /erp/sc/routing/storage/shipment/updateListLogistics

Args:
    data: 参数数组 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/shipment/updateListLogistics", kwargs if kwargs else None)
        return resp.data or {}

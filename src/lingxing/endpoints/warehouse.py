"""仓库/库存 API endpoints."""
from __future__ import annotations

from ..models.warehouse import (
    GetProcessOrderListsItem,
    GetStorageAdjustOrderListItem,
    InboundGetCustomTypesItem,
    InboundgetOrdersItem,
    InventoryBinDetailsItem,
    InventoryDetailsItem,
    OutboundGetCustomTypesItem,
    OutboundgetOrdersItem,
    PurchaseReceiptOrderListItem,
    RemovalInboundListItem,
    WareHouseBinStatementItem,
    WarehouseListsItem,
    WarehouseStatementItem,
    WarehouseStatementNewItem,
    WmsOrderListItem,
)
from ._base import BaseEndpoint


class WarehouseEndpoints(BaseEndpoint):
    """领星仓库/库存 API (76个接口)."""

    async def add_allocation_order(self, **kwargs) -> dict:
        """创建待收货/已完成的调拨单.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder

Args:
    wid: 客户出库仓库id（与系统仓库出库id任一必填，优先取客户出库仓库id）, int.
    sys_wid: 系统仓库出库id（与客户仓库出库id任一必填，优先取客户出库仓库id）, int.
    to_wid: 客户入库仓库id（与系统仓库入库id任一必填，优先取客户入库仓库id）, int.
    sys_to_wid: 系统仓库入库id（与客户仓库入库id任一必填，优先取客户入库仓库id）, int.
    freight_fee: 运费, string.
    other_fee: 其他费用, string.
    fee_part_type: 费用分摊方式：【默认0】 0 不分摊 2 按sku数量分摊 3 按重量 4 按体积 5 按自定义, int.
    remark: 备注, string.
    type: 调拨类型：【默认1】 1 简易调拨【创建已完成状态的单据】 2 完整调拨【创建待收货状态的单据】, int.
    predict_time: 预计到货时间，格式：Y-m-d, string.
    out_available_bin: 出库可用仓位列表, array.
    out_inferior_bin: 出库次品仓位列表, array.
    to_available_bin: 入库可用仓位列表, array.
    to_inferior_bin: 入库次品仓位列表, array.
    out_bin_type: 0 默认  1 出库仓位不为空时，必传, string."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/addAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def adjust_order_confirm(self, **kwargs) -> dict:
        """调整单确认调整.

POST /basicOpen/adjustOrder/adjust/setAdjust

Args:
    orderSn: 调整单单号, array."""
        resp = await self._post("/basicOpen/adjustOrder/adjust/setAdjust", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_storage_allocation_list(self, **kwargs) -> dict:
        """撤销调拨单.

POST /basicOpen/storageAllocationList/cancel

Args:
    order_sn: 调拨单号 对应查询调拨单列表data>>order_sn字段 (required), string."""
        resp = await self._post("/basicOpen/storageAllocationList/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def create_inbound(self, **kwargs) -> dict:
        """创建待发货/待收货/已完成的备货单.

POST /erp/sc/routing/owms/inbound/createInbound

Args:
    inbound_order_no: 客户参考号（唯一单号） (required), string.
    custom_s_wid: 自定义仓库id，custom_s_wid和s_wid其中一项必填，都填则优先custom_s_wid, string.
    s_wid: 发货仓库，仅限本地仓 (required), int.
    r_wid: 收货仓库，仅限海外仓 (required), int.
    logistics_id: 物流方式id，查询头程物流渠道列表接口对应字段【id】 （按计费重分摊时，需有传对应物流方式，以获取材积参数用于计算） (required), int.
    status: 订单状态：【默认60】 40 待发货 50 待收货 60 已完成 注：收货仓支持三方海外仓的备货单状态只会到待发货, int.
    estimated_time: 预计到货时间, string.
    arrival_time: 实际到货时间, string.
    share_id: 头程费分摊方式：【默认0】 0 按计费重 1 按实重 2 按体积重 3 按SKU数量 4 自定义 5 按箱子体积 注意：生成待发货状态备货单时，需要通过接口上传备货单装箱信息上传箱子信息； 待收货和已完成的订单不支持【上传备货单装箱信息】，无法按箱子体积分摊, int.
    remark: 备注, string.
    file_id: 附件id, string.
    overseas_type: 下单至第三方【默认2】： 1 否，2 是 注：当收货仓为API海外仓时可填，不填默认为是, int.
    real_delivery_time: 实际发货时间, string.
    logistics_list: 物流信息, array.
    product_list: 产品信息 (required), array.
    logistics_list_type: 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object.
    method_id: 运输方式 查询运输方式列表接口对应字段【method_id】, string.
    custom_fields: 自定义字段, object."""
        resp = await self._post("/erp/sc/routing/owms/inbound/createInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_fba_shipment_list(self, **kwargs) -> dict:
        """删除发货单.

POST /basicOpen/openapi/fbaShipment/deleteShipmentList

Args:
    shipment_nos: 发货单单号，对应查询FBA发货单列表接口字段【shipment_sn】 (required), array."""
        resp = await self._post("/basicOpen/openapi/fbaShipment/deleteShipmentList", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_over_sea_stock_order(self, **kwargs) -> dict:
        """删除备货单.

POST /basicOpen/overSeaWarehouse/stockOrder/delete

Args:
    overseas_order_nos: 备货单单号，对应获取备货单号接口字段【overseas_order_no】 (required), array."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def delete_storage_allocation_list(self, **kwargs) -> dict:
        """删除调拨单.

POST /basicOpen/storageAllocationList/delete

Args:
    orderSn: 调拨单单号，对应查询调拨单列表接口字段【order_sn】 (required), array."""
        resp = await self._post("/basicOpen/storageAllocationList/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def edit_warehouse(self, **kwargs) -> dict:
        """添加/修改仓库.

POST /erp/sc/storage/wareHouse/edit

Args:
    sys_wid: 领星系统仓库id，编辑时必传, int.
    wid: 客户自定义仓库id【非领星系统ERP内仓库id】, string.
    name: 仓库名称 (required), string.
    contact: 负责人, string.
    telephone: 联系电话, string.
    address: 仓库地址, string.
    remark: 备注, string.
    type: 仓库属性：1 -本地仓 3 -海外自建仓，不传默认 1, int."""
        resp = await self._post("/erp/sc/storage/wareHouse/edit", kwargs if kwargs else None)
        return resp.data or {}
    async def fba_stock(self, **kwargs) -> list | dict:
        """查询FBA库存列表.

POST /erp/sc/routing/fba/fbaStock/fbaList

Args:
    sid: 店铺id，多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】 (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认15, int."""
        resp = await self._post("/erp/sc/routing/fba/fbaStock/fbaList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fba_stock_v2(self, **kwargs) -> list | dict:
        """查询FBA库存列表-v2.

POST /basicOpen/openapi/storage/fbaWarehouseDetail

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20,取值范围[20,200], int.
    search_field: 搜索维度: sku product_name seller_sku fnsku asin parent_asin spu spu_name, string.
    search_value: 搜索值, string.
    cid: 分类, string.
    sid: 店铺id（支持多个，使用,分隔）, string.
    bid: 品牌, string.
    attribute: 属性, string.
    asin_principal: Listing负责人uid，对应查询ERP用户信息列表uid字段 多个使用,分隔, string.
    status: 在售状态: 0 停售 1 在售, string.
    senior_search_list: 高级搜索列表，详情见附加说明, string.
    fulfillment_channel_type: 配送方式: FBA FBM, string.
    is_hide_zero_stock: 是否隐藏零库存行: 0 不隐藏零库存行 1 隐藏零库存行, string.
    is_parant_asin_merge: 是否合并父ASIN: 0 不合并父ASIN 1 合并父ASIN, string.
    is_contain_del_ls: 是否显示已删除Listing: 0 不显示已删除Listing 1 显示已删除Listing, string.
    query_fba_storage_quantity_list: true 是、false 否；默认false，如果传入true,则出参数据中的欧洲共享仓会将出参字段-fba_storage_quantity_list的值返回, Boolean."""
        resp = await self._post("/basicOpen/openapi/storage/fbaWarehouseDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fast_receive(self, **kwargs) -> dict:
        """收货单快捷入库.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive

Args:
    order_sn: 收货单号 (required), string.
    expect_arrival_time: 预计收货时间，不传时默认取自收货单, string.
    custom_receive_time: 自定义收货时间，  自定义日期须早于请求当天日期, string.
    logistics_company: 物流商，不传时默认取自收货单, string.
    logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单, string.
    shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单, number.
    other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单, number.
    remark: 备注，最大支持255个字符，不传时默认取自收货单, string.
    item_list: 收货明细 (required), array."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/fastReceive", kwargs if kwargs else None)
        return resp.data or {}
    async def get_adjust_order_confirm_result(self, **kwargs) -> dict:
        """查询调整单确认调整异步结果.

POST /basicOpen/adjustOrder/adjust/getAdjustStatus

Args:
    taskNo: 异步任务编号, string."""
        resp = await self._post("/basicOpen/adjustOrder/adjust/getAdjustStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def get_batch_detail_list(self, **kwargs) -> dict:
        """查询批次明细.

POST /erp/sc/routing/data/local_inventory/getBatchDetailList

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限400, int.
    show_zero_stock: 是否显示0库存信息：0 不显示，1 显示, int.
    wids: 仓库id，多个使用英文逗号分隔, string.
    stock_in_type_list: 入库类型，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 26 退货入库 27 移除入库 45 赠品入库, string.
    search_field: 搜索字段： sku SKU msku MSKU fnsku FNSKU order_sn 单据号 product_name 品名 batch_number 批次号 receipt_order 收货单 purchase_order 采购单 purchase_plan 采购计划 source_batch_number 源头批次号, string.
    search_value: 搜索值, string."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchDetailList", kwargs if kwargs else None)
        return resp.data or {}
    async def get_batch_statement_list(self, **kwargs) -> dict:
        """查询批次流水.

POST /erp/sc/routing/data/local_inventory/getBatchStatementList

Args:
    statement_type_list: 批次流水主类型id，多个使用英文逗号分隔： 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 16 换标入库 17 加工入库 18 拆分入库 47 VC-PO出库 48 VC-DF出库 42 其他出库 41 调拨出库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 71 采购上架 72 委外上架 65 WFS出库 45 赠品入库 46 赠品质检入库 73 赠品上架 201 期初成本调整 202 尾差成本调整, string.
    search_field: 搜索字段： sku SKU msku MSKU fnsku FNSKU product_name 品名 purchase_plan 采购计划 purchase_order 采购单 receipt_order 收货单 order_sn 单据号 batch_number 批次号 source_batch_number 源头批次号, string.
    search_value: 搜索值, string.
    wid_list: 仓库id，多个使用英文逗号分隔, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限400, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/getBatchStatementList", kwargs if kwargs else None)
        return resp.data or {}
    async def get_receive_good_records(self, **kwargs) -> dict:
        """查询备货单收货记录.

POST /erp/sc/routing/owms/inbound/getReceiveGoodRecords

Args:
    overseas_order_no: 备货单单号【不支持批量】, string.
    start_date: 收货开始时间，闭区间，格式：Y-m-d, string.
    end_date: 收货结束时间，开区间，格式：Y-m-d, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认500, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/getReceiveGoodRecords", kwargs if kwargs else None)
        return resp.data or {}
    async def inbound_order_confirm(self, **kwargs) -> dict:
        """入库单确认入库.

POST /basicOpen/inboundOrder/inbound/setInbound

Args:
    orderSn: 入库单单号, array."""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def inventory_details(self, **kwargs) -> list[InventoryDetailsItem]:
        """查询仓库库存明细.

POST /erp/sc/routing/data/local_inventory/inventoryDetails

Args:
    wid: 仓库id，多个使用英文逗号分隔, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限800, int.
    sku: SKU，单个,（模糊搜索）, string."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryDetails", kwargs if kwargs else None)
        return self._parse_list(resp.data, InventoryDetailsItem)
    async def order_add(self, **kwargs) -> dict:
        """添加入库单.

POST /erp/sc/routing/storage/storage/orderAdd

Args:
    wid: 自定义仓库id，wid和sys_wid其中一项必填，都填则优先wid, string.
    sys_wid: 系统仓库id，wid和sys_wid其中一项必填，都填则优先wid (required), int.
    type: 单据类型： 1 其他入库 2 采购入库 26 退货入库 27 移除入库 (required), int.
    supplier_id: 自定义供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】, string.
    sys_supplier_id: 系统供应商id【supplier_id、sys_supplier_id 二选一必填，都填优先取supplier_id】, int.
    order_sn: 采购单号【对此采购单执行快捷入库】，不支持自定义采购单号, string.
    remark: 单据备注, string.
    ship_fee: 运费, string.
    other_fee: 其它费用, string.
    fee_part_type: 费用分配方式: 0 不分摊 1 按金额 2 按数量, int.
    inbound_time: 自定义入库时间，格式：Y-m-d, string.
    inbound_idempotent_code: （入库单）客户参考号, 该字段校验唯一不可重复, string.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAdd", kwargs if kwargs else None)
        return resp.data or {}
    async def order_add_out(self, **kwargs) -> dict:
        """添加出库单.

POST /erp/sc/routing/storage/storage/orderAddOut

Args:
    wid: 自定义仓库ID，wid和sys_wid其中一项必填，都填则优先wid, string.
    sys_wid: 系统仓库ID，sys_wid和wid其中一项必填，都填则优先wid (required), int.
    type: 单据类型： 11 其他出库 12 FBA出库 14 退货出库 18 销毁出库 (required), int.
    status: 新建单据状态： 10：待提交 30：待出库 40：已完成【默认值】, int.
    sys_supplier_id: 系统客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）, int.
    supplier_id: 客户供应商ID（退货出库：客户供应商ID, sys_supplier_id和supplier_id其中一个必填，都填则取supplier_id）, string.
    idempotent_code: 客户参考号, 该字段校验唯一不可重复, string.
    remark: 单据备注, string.
    return_price: 退货费（退货出库）, number.
    other_fee: 其它费用（退货出库）, number.
    sys_to_wid: 系统客户目的仓库ID（非退货出库）, int.
    to_wid: 客户目的仓库ID（非退货出库）, string.
    outbound_time: 自定义出库时间，格式：Y-m-d, string.
    bin_type: 出库仓位指定方式： 0 系统指定仓位【默认值】 1 手动指定仓位, int.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/storage/storage/orderAddOut", kwargs if kwargs else None)
        return resp.data or {}
    async def outbound_order_confirm(self, **kwargs) -> dict:
        """出库单确认出库.

POST /basicOpen/outboundOrder/outbound/setOutbound

Args:
    orderSn: 出库单单号, array."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOutbound", kwargs if kwargs else None)
        return resp.data or {}
    async def over_seas_stock_detail(self, **kwargs) -> list | dict:
        """查询备货单详情.

POST /basicOpen/overSeaWarehouse/stockOrder/detail

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_match_list(self, **kwargs) -> list | dict:
        """查询海外仓sku配对列表.

POST /basicOpen/overseaWarehouseSetting/matchList

Args:
    wpId: 三方服务商id (required), int.
    twIds: 三方仓id，多个之间用逗号隔开, string.
    offset: 分页偏移量，默认0, int.
    length: 分页大小，默认20，上限200, int.
    isMatched: 是否配对，0否，1是, int.
    keyword: 关键词，搜索sku / 品名 / 第三方产品名 / 产品编码, string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/matchList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_product_match(self, **kwargs) -> list | dict:
        """海外仓sku配对.

POST /basicOpen/overseaWarehouseSetting/productMatch

Args:
    twId: 三方仓id (required), int.
    twpId: 三方商品id (required), int.
    wpId: 三方服务商id (required), int.
    productId: 商品id (required), int.
    matchNum: 整箱配对数量 (required), int.
    matchAll: 是否配对海外仓所有仓库，0否；1是，默认0, int.
    fnsku: fnsku, string.
    sellerId: 店铺id, string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productMatch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def oversea_warehouse_product_un_match(self, **kwargs) -> list | dict:
        """海外仓sku取消配对.

POST /basicOpen/overseaWarehouseSetting/productUnMatch

Args:
    wpId: 三方服务商id (required), string.
    wpmId: 配对id (required), string."""
        resp = await self._post("/basicOpen/overseaWarehouseSetting/productUnMatch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def purchase_receipt_order_list(self, **kwargs) -> tuple[list[PurchaseReceiptOrderListItem], int]:
        """查询收货单列表.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList

Args:
    date_type: 查询时间类型：1 预计到货时间，2 收货时间，3 创建时间，4 更新时间, int.
    start_date: 开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sns: 收货单号，多个使用英文逗号分隔, string.
    status: 状态：10 待收货，40 已完成, int.
    wid: 仓库id，多个使用英文逗号分隔, string.
    order_type: 收货类型：1 采购订单，2 委外订单, int.
    qc_status: 质检状态，多个使用英文逗号分隔：0 未质检，1 部分质检，2 完成质检, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认200，上限500, int."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/getOrderList", kwargs if kwargs else None)
        return self._parse_page(resp.data, PurchaseReceiptOrderListItem)
    async def receive(self, **kwargs) -> dict:
        """收货单到货.

POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive

Args:
    order_sn: 收货单号 (required), string.
    expect_arrival_time: 预计收货时间，不传时默认取自收货单, string.
    custom_receive_time: 自定义收货时间，  自定义日期须早于请求当天日期, string.
    logistics_company: 物流商，不传时默认取自收货单, string.
    logistics_order_no: 物流单号，仅支持字母、数字、下划线、中横线，不传时默认取自收货单, string.
    shipping_cost: 运费，仅支持2位小数，不传时默认取自收货单, number.
    other_fee: 其他费用，仅支持2位小数，不传时默认取自收货单, number.
    remark: 备注，最大支持255个字符，不传时默认取自收货单, string.
    item_list: 收货明细 (required), array."""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/receive", kwargs if kwargs else None)
        return resp.data or {}
    async def send_inbound(self, **kwargs) -> dict:
        """海外仓备货单发货.

POST /erp/sc/routing/owms/inbound/sendInbound

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/sendInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def set_inbound_order_revoke(self, **kwargs) -> list | dict:
        """撤销入库单.

POST /basicOpen/inboundOrder/inbound/setOrderRevoke

Args:
    order_sn: 入库单号 对应查询入库单列表data>>order_sn字段 (required), string.
    delete_receipt_order: 是否同步删除收货单  删除则传值 1，否则不传值, int."""
        resp = await self._post("/basicOpen/inboundOrder/inbound/setOrderRevoke", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_outbound_order_revoke(self, **kwargs) -> list | dict:
        """撤销出库单.

POST /basicOpen/outboundOrder/outbound/setOrderRevoke

Args:
    order_sn: 出库单号 对应查询出库单列表data>>order_sn字段 (required), string."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/setOrderRevoke", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def update_logistics(self, **kwargs) -> dict:
        """更新备货单物流信息.

POST /erp/sc/routing/owms/inbound/updateLogistics

Args:
    overseas_order_no: 海外仓备货单号 (required), string.
    logistics_list: 物流信息 (required), array.
    logistics_list_type: 物流信息版本： 0：旧版，即将下线 1：新版 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object."""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateLogistics", kwargs if kwargs else None)
        return resp.data or {}
    async def warehouse_lists(self, **kwargs) -> list[WarehouseListsItem]:
        """查询仓库列表.

POST /erp/sc/data/local_inventory/warehouse

Args:
    type: 仓库类型： 1 本地仓【默认值】 3 海外仓 4 亚马逊平台仓 6 AWD仓, int.
    sub_type: 海外仓子类型：  1 无API海外仓  2 有API海外仓【此参数只在type=3生效】, int.
    is_delete: 是否删除，多个使用英文逗号分隔： 0 未删除【默认值】 1 已删除, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认1000条, int."""
        resp = await self._post("/erp/sc/data/local_inventory/warehouse", kwargs if kwargs else None)
        return self._parse_list(resp.data, WarehouseListsItem)
    async def warehouse_statement(self, **kwargs) -> list[WarehouseStatementItem]:
        """查询库存流水（旧）.

POST /erp/sc/routing/data/local_inventory/wareHouseStatement

Args:
    wid: 仓库ID，多个仓库ID用英文逗号分隔，不填默认所有仓库, string.
    type: 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】  1 其他入库 2 采购入库 3 调拨入库 10 其它入库（已撤销） 11 其他出库 12 FBA出库 13 调拨出库 14 退货出库 15 FBM退货 16 换标入库 17 加工入库 18 拆分入库 20 采购入库（已撤销） 21 库存调整 23 委外入库 25 盘盈入库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 43 FBM出库 50 成本补录 110 其它出库（已撤销） 120 FBA出库（已撤销） 130 调拨出库（已撤销） 140 退货出库（已撤销） 210 库存调整（已撤销） 500 成本补录（已撤销）, string.
    start_date: 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseStatement", kwargs if kwargs else None)
        return self._parse_list(resp.data, WarehouseStatementItem)
    async def warehouse_statement_new(self, **kwargs) -> list[WarehouseStatementNewItem]:
        """查询库存流水（新）.

POST /erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement

Args:
    wids: 仓库id，多个使用英文逗号分隔, string.
    types: 流水类型，多个使用英文逗号分隔：【不填默认全部类型】 19 其他入库 22 采购入库 24 调拨入库 23 委外入库 25 盘盈入库 15 FBM退货  16 换标入库 17 加工入库 18 拆分入库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 71 采购上架 72 委外上架 42 其他出库 41 调拨出库 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 65 WFS出库 100 锁定流水  51 销毁出库 47 VC-PO出库 48 VC-DF出库 49 Temu出库, string.
    sub_types: 子类流水类型，多个使用英文逗号分隔：【不填默认全部类型】 1901 其他入库 手工其他入库 1902 其他入库 用户初始化 1903 其他入库 系统初始化 2201 采购入库 手工采购入库 2202 采购入库 采购单创建入库单 2801 采购质检 质检 7101 采购上架 PDA上架入库 7201 委外上架 PDA委外上架 2401 调拨入库 调拨单入在途 2402 调拨入库 调拨单收货 2403 调拨入库 备货单入在途 2404 调拨入库 备货单收货 2405 调拨入库 备货单入库结束到货 2301 委外入库 委外订单完成加工后入库 2901 委外质检 委外订单质检 2501 盘盈入库 盘点单入库 2502 盘盈入库 数量调整单正向 1501 FBM退货 退货入库 1502 FBM退货 退货入库质检 1601 换标入库 换标调整入库 1701 加工入库 加工单入库 1702 加工入库 委外订单加工入库 1801 拆分入库 拆分单入库 2601 自动退货入库 2602 手动退货入库 2701 移除入库 4201 其他出库 手工其他出库 4101 调拨出库 调拨单出库 4102 调拨出库 备货单出库 3201 委外出库 委外订单完成加工后出库 3301 盘亏出库 盘点单出库 3302 盘亏出库 数量调整单负向 3401 换标出库 换标调整出库 3501 加工出库 加工单出库 3502 加工出库 委外订单加工出库 3601 拆分出库 拆分单出库 3701 FBA出库 发货单出库 3702 FBA出库 手工FBA出库 3801 FBM出库 销售出库单 3901 退货出库 手工退货出库 3902 退货出库 采购单生成的退货出库单 10001 库存锁定-出库 10002 库存锁定-调拨 10003 库存锁定-调整 10004 库存锁定-加工 10005 库存锁定-加工计划 10006 库存锁定-拆分 10007 库存锁定-海外备货 10008 库存锁定-发货 10009 库存锁定-自发货 10010 库存锁定-主动释放 10012 库存锁定-发货拣货 10013 库存锁定-发货计划 10014 库存锁定-WFS库存调整 10011 仓位转移和一键上架, string.
    start_date: 操作开始时间，格式：Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，格式：Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0 (required), int.
    length: 分页长度，默认20 (required), int."""
        resp = await self._post("/erp/sc/routing/inventoryLog/WareHouseInventory/wareHouseCenterStatement", kwargs if kwargs else None)
        return self._parse_list(resp.data, WarehouseStatementNewItem)
    async def wms_order_detail(self, **kwargs) -> list | dict:
        """查询销售出库单详情.

POST /basicOpen/wmsOrder/getWmsOrdersByOrderNumbers

Args:
    isPrintCenter: 是否需要拣货信息，枚举值：1-是, 0-否, int.
    orderNumbers: 系统单号，必填，多个以逗号连接, string."""
        resp = await self._post("/basicOpen/wmsOrder/getWmsOrdersByOrderNumbers", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wms_order_list(self, **kwargs) -> list[WmsOrderListItem]:
        """查询销售出库单列表.

POST /erp/sc/routing/wms/order/wmsOrderList

Args:
    page: 分页页码，默认1, int.
    page_size: 分页长度，默认20，上限200, int.
    sid_arr: 店铺id, array.
    status_arr: 状态： 1 物流下单 2 待出库 3 已出库 4 已截单, array.
    logistics_status_arr: 物流状态： 1 待导入 2 物流待下单 3 物流下单中 4 下单异常 5 下单完成 6 待海外仓下单 7 海外仓下单中 11 待导入国内物流 41 物流取消中 42 物流取消异常 43 物流取消完成, array.
    platform_order_no_arr: 平台单号, array.
    order_number_arr: 系统单号, array.
    wo_number_arr: 销售出库单号, array.
    time_type: 时间类型： 创建时间 create_at  出库时间【单据操作】 delivered_at 流水出库时间 stock_delivered_at 变更时间 update_at, string.
    start_date: 开始日期，格式：Y-m-d，默认为最近1个月, string.
    end_date: 结束日期，格式：Y-m-d，默认为最近1个月, string."""
        resp = await self._post("/erp/sc/routing/wms/order/wmsOrderList", kwargs if kwargs else None)
        return self._parse_list(resp.data, WmsOrderListItem)
    async def add_adjustment_order(self, **kwargs) -> dict:
        """创建已完成的数量调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addAdjustmentOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def add_rebrand_adjustment_order(self, **kwargs) -> dict:
        """创建已完成的换标调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    bin_type: 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位, int.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addRebrandAdjustmentOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def add_sku_adjustment_order(self, **kwargs) -> dict:
        """创建已完成的SKU调整单.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder

Args:
    wid: 系统仓库id (required), int.
    remark: 单据备注, string.
    bin_type: 出库仓位方式：【默认1】 1 系统自定选择 2 指定出库仓位, int.
    product_list: 调整的产品明细数据 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/addSkuAdjustmentOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def add_storage_process_order(self, **kwargs) -> dict:
        """创建加工单 / 拆分单.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder

Args:
    type: 单据类型：1 加工单，2 拆分单 (required), int.
    wid: 系统仓库id (required), int.
    remark: 备注, string.
    product_list: 产品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/addStorageProcessOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def bin_create(self, **kwargs) -> dict:
        """添加仓位.

POST /erp/sc/routing/storage/wareHouseBin/create

Args:
    wid: 仓库id (required), int.
    code: 仓位名称 (required), string.
    type: 仓位类型： 5 可用 6 次品 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/create", kwargs if kwargs else None)
        return resp.data or {}
    async def cancel_wms_order(self, **kwargs) -> dict:
        """销售出库单截单.

POST /basicOpen/wmsOrder/cancel

Args:
    orderNumbers: 系统单号 对应查询销售出库单列表data>>order_number字段 (required), array.
    tagType: 截单标签，3-5：待人工审核；3-17：其他 (required), string.
    orderComment: 截单备注, string."""
        resp = await self._post("/basicOpen/wmsOrder/cancel", kwargs if kwargs else None)
        return resp.data or {}
    async def check_add_order(self, **kwargs) -> dict:
        """创建已完成的盘点单.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder

Args:
    wid: 盘点仓库id,对应领星系统的仓库id (required), int.
    is_display_check: 是否明盘：0 否，1 是【默认值】 (required), int.
    check_uid: 盘点人id (required), int.
    remark: 单据备注, string.
    product_list: 盘点明细 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/addOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def check_get_order_detail(self, **kwargs) -> list | dict:
        """查询盘点单详情.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail

Args:
    order_sn: 盘点单号 (required), string.
    search_field: 搜索字段： sku SKU fnsku FNSKU product_name 品名 whb_code_text 仓位 whb_type_text 仓位类型, string.
    search_value: 搜索值, string.
    sort_field: 排序字段： book_inventory 账面库存 actual_inventory 实盘库存 different_count 库存差异, string.
    sort_type: 排序规则：desc 降序【默认】，asc 升序, string.
    page: 分页页码，默认1【控制 product_list 返回数目】, int.
    page_size: 分页长度，默认20【控制 product_list 返回数目】, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def check_get_order_list(self, **kwargs) -> list | dict:
        """查询盘点单列表.

POST /erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList

Args:
    wid: 盘点仓库id，多个使用英文逗号分隔, string.
    check_type: 盘点类型，多个盘点类型用英文逗号分隔： 1 整仓盘点 2 SKU盘点 3 仓位盘点 4 SKU+仓位盘点, string.
    date_field: 搜索时间类型： create_date 创建时间【默认值】 check_date 盘点时间, string.
    start_date: 开始日期，格式：Y-m-d, string.
    end_date: 结束日期，格式：Y-m-d, string.
    search_field: 搜索字段： order_sn 盘点单号 create_user 创建人 check_user 盘点人 remark 备注, string.
    search_value: 搜索值, string.
    status: 盘点状态： 10 待盘点 20 预锁 30 盘点中 40 已盘点 121 待审核 122 已驳回 123 通过 124 作废, int.
    page: 分页页码，默认1, int.
    page_size: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/InventoryCheck/getOrderList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def create_receipt_order(self, **kwargs) -> dict:
        """写操作 createReceiptOrder. POST /erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder"""
        resp = await self._post("/erp/sc/routing/deliveryReceipt/PurchaseReceiptOrder/createReceiptOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def finish_receive_allocation_order(self, **kwargs) -> dict:
        """写操作 finishReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/finishReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def get_packing_data(self, **kwargs) -> list | dict:
        """查询备货单装箱信息.

POST /erp/sc/routing/owms/inbound/getPackingData

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/getPackingData", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def get_process_order_lists(self, **kwargs) -> list[GetProcessOrderListsItem]:
        """加工单列表.

POST /erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists

Args:
    type: 单据类型：1加工单，2拆分单, 是.
    wid: 仓库id，多个用英文逗号分隔, 否.
    process_sn: 加工单号，多个用英文逗号分隔, 否.
    status: 加工状态： 0 待配货 1 待完成 2 已完成, 否.
    search_field_time: 时间搜索维度： create_time 创建时间 finish_time 完成时间 update_time 更新时间, 否.
    start_date: 开始时间，格式：Y-m-d, 否.
    end_date: 结束时间，格式：Y-m-d, 否.
    offset: 分页偏移量，默认0, 是.
    length: 分页长度，默认500, 是."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageProcess/getOrderLists", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetProcessOrderListsItem)
    async def get_storage_adjust_order_list(self, **kwargs) -> list[GetStorageAdjustOrderListItem]:
        """查询调整单列表.

POST /erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList

Args:
    search_date_type: 时间类型： 1 创建时间 2 调整时间 3 更新时间, int.
    start_date: 开始日期，格式：Y-m-d, string.
    end_date: 结束日期，格式：Y-m-d, string.
    order_sn: 调整单号，多个使用英文逗号分隔, string.
    adjust_status: 单据状态： 5 待提交 10 待调整 20 已完成 30 已删除 121 待审批 122 已驳回, int.
    wid: 系统仓库id，多个使用英文逗号分隔, string.
    type: 调整类型： 0 数量调整 1 换标调整 2 sku调整, int.
    page: 当前页码，默认1, int.
    page_size: 分页条数，默认20, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAdjustment/getStorageAdjustOrderList", kwargs if kwargs else None)
        return self._parse_list(resp.data, GetStorageAdjustOrderListItem)
    async def get_storage_allocation_list(self, **kwargs) -> list | dict:
        """查询调拨单列表.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList

Args:
    wid: 出库仓库id，多个以英文逗号分隔, string.
    to_wid: 入库仓库id，多个以英文逗号分隔, string.
    search_date_type: 时间类型：【不传或传空则默认为 1】 1 创建时间 2 调拨时间 3 完成时间 4 更新时间, int.
    start_date: 开始日期，格式：Y-m-d，只有和结束日期同时有值才会生效, string.
    end_date: 结束日期，格式：Y-m-d，只有和开始日期同时有值才会生效, string.
    page: 当前页码，默认1, int.
    page_size: 分页条数，默认15, int."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/getStorageAllocationList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_batches_receipt(self, **kwargs) -> dict:
        """备货单分批收货.

POST /erp/sc/routing/owms/inbound/batchesReceipt

Args:
    overseas_order_no: 备货单号 (required), string.
    product_list: 产品信息 (required), array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/batchesReceipt", kwargs if kwargs else None)
        return resp.data or {}
    async def inbound_complete_receipt(self, **kwargs) -> list | dict:
        """备货单结束到货.

POST /erp/sc/routing/owms/inbound/completeReceipt

Args:
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/completeReceipt", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def inbound_get_custom_types(self, **kwargs) -> tuple[list[InboundGetCustomTypesItem], int]:
        """获取自定义入库类型.

POST /erp/sc/routing/storage/inbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/inbound/getCustomTypes", kwargs if kwargs else None)
        return self._parse_page(resp.data, InboundGetCustomTypesItem)
    async def inboundget_orders(self, **kwargs) -> list[InboundgetOrdersItem]:
        """查询入库单列表.

POST /erp/sc/routing/storage/inbound/getOrders

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    wid: 系统仓库id, int.
    search_field_time: 日期筛选类型： 创建时间 create_time 入库时间 opt_time 更新时间 increment_time, string.
    start_date: 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sn: 入库单单号，多个使用英文逗号分隔, string.
    inbound_idempotent_code: 客户参考单号，多个使用英文逗号分隔, string.
    status: 入库单状态： 10 待提交 20 待入库 40 已完成 50 已撤销 121 待审批 122 已驳回, int.
    type: 入库类型： -1 其他入库（含所有自定义类型）  1 其他入库（非自定义类型） 2 采购入库 3 调拨入库 4 赠品入库 26 退货入库 27 移除入库, int."""
        resp = await self._post("/erp/sc/routing/storage/inbound/getOrders", kwargs if kwargs else None)
        return self._parse_list(resp.data, InboundgetOrdersItem)
    async def inventory_bin_details(self, **kwargs) -> list[InventoryBinDetailsItem]:
        """查询仓位库存明细.

POST /erp/sc/routing/data/local_inventory/inventoryBinDetails

Args:
    wid: 仓库id，多个仓库用英文逗号分隔，默认所有仓库, string.
    bin_type_list: 仓位类型，多个类型用英文逗号分隔： 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20 ，上限500, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/inventoryBinDetails", kwargs if kwargs else None)
        return self._parse_list(resp.data, InventoryBinDetailsItem)
    async def list_inbound(self, **kwargs) -> list | dict:
        """查询海外仓备货单列表.

POST /erp/sc/routing/owms/inbound/listInbound

Args:
    status: 状态： 10 待审核 20 已驳回 30 待配货 40 待发货 50 待收货 51 已撤销 60 已完成, int.
    sub_status: 子状态：【仅在待收货状态下生效】  0 全部  1 未收货  2 部分收货, int.
    s_wid: 发货仓库id, array.
    r_wid: 收货仓库id, array.
    overseas_order_no: 备货单号, string.
    create_time_from: 查询开始日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    create_time_to: 查询结束日期，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    page_size: 分页数量，最大50，默认20, int.
    page: 当前页码，默认1, int.
    date_type: 备货单时间查询类型：【默认create_time】 delivery_time 发货时间 create_time 创建时间 receive_time 收货时间 update_time 更新时间, string.
    is_delete: 订单是否删除： 0 未删除【默认】 1 已删除 2 全部, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/listInbound", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def list_order_nos(self, **kwargs) -> list | dict:
        """获取备货单号.

POST /erp/sc/routing/owms/inbound/listOrderNos

Args:
    inbound_order_no: 客户参考号 数组, array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/listOrderNos", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def match_sku_list(self, **kwargs) -> list | dict:
        """查询系统产品与第三方海外仓产品映射列表.

POST /erp/sc/routing/owms/inbound/matchSkuList

Args:
    wid: 仓库id，多个用英文逗号分隔 (required), string.
    is_matched: 是否配对：【空表示都返回】 0 未配对 1 配对, int.
    offset: 分页偏移量, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/owms/inbound/matchSkuList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def outbound_get_custom_types(self, **kwargs) -> tuple[list[OutboundGetCustomTypesItem], int]:
        """获取自定义出库类型.

POST /erp/sc/routing/storage/outbound/getCustomTypes"""
        resp = await self._post("/erp/sc/routing/storage/outbound/getCustomTypes", kwargs if kwargs else None)
        return self._parse_page(resp.data, OutboundGetCustomTypesItem)
    async def outbound_order_delete(self, **kwargs) -> dict:
        """删除出库单.

POST /basicOpen/outboundOrder/outbound/delete

Args:
    orderSn: 出库单单号, array."""
        resp = await self._post("/basicOpen/outboundOrder/outbound/delete", kwargs if kwargs else None)
        return resp.data or {}
    async def outboundget_orders(self, **kwargs) -> list[OutboundgetOrdersItem]:
        """查询出库单列表.

POST /erp/sc/routing/storage/outbound/getOrders

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    wid: 系统仓库id, string.
    search_field_time: 日期筛选类型： 创建时间 create_time 出库时间 opt_time 更新时间 increment_time, string.
    start_date: 日期查询开始时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    end_date: 日期查询结束时间，格式：Y-m-d 当筛选更新时间时，支持Y-m-d或Y-m-d H:i:s, string.
    order_sn: 出库单单号，多个使用英文逗号分隔, string.
    idempotent_code: 客户参考号，多个使用英文逗号分隔, string.
    status: 出库单状态： 10 待提交 30 待出库 40 已完成 50 已撤销 121 待审批 122 已驳回, int.
    type: 出库类型： 11 其他出库 12 FBA出库 14 退货出库 15 调拨出库 16 WFS出库 17 Temu出库 18 销毁出库, int."""
        resp = await self._post("/erp/sc/routing/storage/outbound/getOrders", kwargs if kwargs else None)
        return self._parse_list(resp.data, OutboundgetOrdersItem)
    async def oversea_stock_order_allocate(self, **kwargs) -> dict:
        """备货单分配库存.

POST /basicOpen/overSeaWarehouse/stockOrder/allocate

Args:
    orderNo: 备货单号 (required), string."""
        resp = await self._post("/basicOpen/overSeaWarehouse/stockOrder/allocate", kwargs if kwargs else None)
        return resp.data or {}
    async def package_label(self, **kwargs) -> list | dict:
        """获取第三方箱唛.

POST /erp/sc/routing/owms/inbound/packageLabel

Args:
    size: 尺寸映射： 1=西邮尺寸专属 2=谷仓A4 3=谷仓100x100 4=谷仓100x150 5=谷仓100x60 11=易仓A4(按SKU) 12=易仓A4(按箱) 13=易仓100x100(无产品名称) 14=易仓100x150(无产品名称) 15=易仓100x100(有产品名称) 16=易仓100x150(有产品名称) 17=易仓100x100(二维码) 18=易仓70x30(显示条码) 19=易仓70x30(无条码) (required), int.
    overseas_order_no: 备货单号 (required), string."""
        resp = await self._post("/erp/sc/routing/owms/inbound/packageLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def packing(self, **kwargs) -> list | dict:
        """上传备货单装箱信息.

POST /erp/sc/routing/owms/inbound/packing

Args:
    overseas_order_no: 备货单号 (required), string.
    packaging_type: 装箱类型：1 每箱多个sku，2 每箱一个sku (required), int.
    box_count: 总箱数 (required), int.
    box_list: 装箱数据 (required), array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/packing", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def partly_receive_allocation_order(self, **kwargs) -> dict:
        """写操作 partlyReceiveAllocationOrder. POST /erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder"""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/partlyReceiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def product_label(self, **kwargs) -> list | dict:
        """获取第三方SKU标签PDF文件.

POST /erp/sc/routing/owms/inbound/productLabel"""
        resp = await self._post("/erp/sc/routing/owms/inbound/productLabel", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def quality_inspection_order_detail(self, **kwargs) -> list | dict:
        """查询质检单详情.

POST /basicOpen/qualityInspectionOrder/detail"""
        resp = await self._post("/basicOpen/qualityInspectionOrder/detail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def receive_allocation_order(self, **kwargs) -> dict:
        """调拨单全部收货.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder

Args:
    orderSnMany: 调拨单号，支持多个，英文逗号分隔 (required), string."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/receiveAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def removal_inbound_list(self, **kwargs) -> list[RemovalInboundListItem]:
        """查询移除入库单列表.

POST /erp/sc/routing/owms/removalInbound/list

Args:
    status: 订单状态： 1 待提交-未提交 2 待提交-提交中 3 待提交-失败 4 待收货-未收货 5 待收货-异常 6 已完成 7 已作废, int.
    start_date: 开始日期【发货日期，双闭区间】, string.
    end_date: 结束日期【发货日期，双闭区间】, string.
    order_no: 移除入库单号, array.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限1000, int."""
        resp = await self._post("/erp/sc/routing/owms/removalInbound/list", kwargs if kwargs else None)
        return self._parse_list(resp.data, RemovalInboundListItem)
    async def set_tracking_no(self, **kwargs) -> dict:
        """物流下单 - 编辑运单号/跟踪号.

POST /basicOpen/logisticsOrdering/setTrackingNo

Args:
    waybill_no: 运单号 (required), string.
    wo_number: 销售出库单号 (required), string.
    tracking_no: 跟踪号, string.
    logistics_freight: 物流运费, string.
    logistics_freight_currency_code: 物流运费币种： CNY USD EUR JPY AUD CAD MXN GBP INR AED SGD SAR BRL SEK PLN TRY HKD, string.
    pkg_fee_weight: 计费重, string.
    pkg_fee_weight_unit: 计费重单位： g kg, string."""
        resp = await self._post("/basicOpen/logisticsOrdering/setTrackingNo", kwargs if kwargs else None)
        return resp.data or {}
    async def submit_allocation_order(self, **kwargs) -> dict:
        """创建待调拨的调拨单.

POST /erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder

Args:
    sys_wid: 系统出库仓库ID (required), int.
    sys_to_wid: 系统入库仓库ID (required), int.
    freight_fee: 运费, string.
    other_fee: 其他费用, string.
    fee_part_type: 费用分摊方式：0 不分摊【默认值】，2 按sku数量分摊，3 按重量，4 按体积，5 按自定义, int.
    remark: 备注, string.
    predict_time: 预计到货时间, string.
    type: 默认为2-标准调拨, string.
    out_bin_type: 默认0 出库仓位不为空时必传1 (required), string.
    product_list: 产品明细 (required), array."""
        resp = await self._post("/erp/sc/routing/inventoryReceipt/StorageAllocation/submitAllocationOrder", kwargs if kwargs else None)
        return resp.data or {}
    async def switch_status(self, **kwargs) -> dict:
        """启用、禁用仓位.

POST /erp/sc/routing/storage/wareHouseBin/switchStatus

Args:
    wid: 仓库id (required), string.
    whbCode: 仓位名称 (required), string.
    status: 仓位状态：0 禁用，1 启用 (required), int."""
        resp = await self._post("/erp/sc/routing/storage/wareHouseBin/switchStatus", kwargs if kwargs else None)
        return resp.data or {}
    async def update_inbound(self, **kwargs) -> dict:
        """更新备货单.

POST /erp/sc/routing/owms/inbound/updateInbound

Args:
    overseas_order_no: 海外仓备货单号 (required), string.
    logistics_id: 物流方式id【按计费重分摊时，需传对应物流方式，以获取材积参数用于计算】, int.
    product_list: 产品信息, array.
    estimated_time: 预计到货时间, string.
    arrival_time: 实际到货时间, string.
    share_id: 头程费分配方式： 0 按计费重【默认值】 1 按实重 2 按体积重 3 按SKU数量 4自定义, int.
    remark: 备注, string.
    file_id: 附件id, string.
    overseas_type: 下单至第三方【当收货仓为API海外仓时可填，不填默认为是】：1 否，2 是【默认】, int.
    real_delivery_time: 实际发货时间，格式：Y-m-d H:i:s, string.
    logistics_list_type: 物流信息版本：0或者不传：默认旧版物流信息 1：新版物流信息 (required), int.
    head_logistics_list: 新版头程物流信息（当logistics_list_type 为1时才有意义） (required), object.
    logistics_list: 旧版物流信息，即将下线, array."""
        resp = await self._post("/erp/sc/routing/owms/inbound/updateInbound", kwargs if kwargs else None)
        return resp.data or {}
    async def ware_house_bin_statement(self, **kwargs) -> list[WareHouseBinStatementItem]:
        """查询仓位流水.

POST /erp/sc/routing/data/local_inventory/wareHouseBinStatement

Args:
    wid: 仓库ID，多个仓库ID用英文逗号,分隔，传或者传空则默认所有仓库, string.
    type: 流水类型：【多个流水类型用英文逗号分隔，不填默认全部类型】 16 换标入库 17 加工入库 18 拆分入库 19 其他入库 22 采购入库 23 委外入库 24 调拨入库 25 盘盈入库 26 退货入库 27 移除入库 28 采购质检 29 委外质检 32 委外出库 33 盘亏出库 34 换标出库 35 加工出库 36 拆分出库 37 FBA出库 38 FBM出库 39 退货出库 41 调拨出库 42 其他出库 65 WFS出库 71 采购上架 72 委外上架 100 库存调整 200 成本补录 30001 已撤销, string.
    bin_type_list: 仓位类型：【多个类型用逗号分隔】 1 待检暂存 2 可用暂存 3 次品暂存 4 拣货暂存 5 可用 6 次品, string.
    start_date: 操作开始时间，Y-m-d，闭区间，联合结束时间使用, string.
    end_date: 操作结束时间，Y-m-d，开区间，联合开始时间使用, string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/wareHouseBinStatement", kwargs if kwargs else None)
        return self._parse_list(resp.data, WareHouseBinStatementItem)
    async def warehouse_bin(self, **kwargs) -> list | dict:
        """查询本地仓位列表.

POST /erp/sc/routing/data/local_inventory/warehouseBin

Args:
    wid: 仓库ID，字符串id，多个使用英文逗号分隔, string.
    id: 仓位ID，字符串id，多个使用英文逗号分隔, string.
    status: 仓位状态： 1 禁用 2 启用, string.
    type: 仓位类型： 5 可用 6 次品, string.
    offset: 分页偏移量，默认为0, int.
    limit: 限制条数，默认20条, int."""
        resp = await self._post("/erp/sc/routing/data/local_inventory/warehouseBin", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wms_order_get_wms_logistics_labels(self, **kwargs) -> list | dict:
        """查询销售出库单物流面单.

POST /erp/sc/routing/wms/order/getWmsLogisticsLabels

Args:
    wo_number_arr: 销售出库单号,上限50【销售出库单号与系统单号二选一必填】, array.
    order_number_arr: 系统单号,上限50【销售出库单号与系统单号二选一必填】, array."""
        resp = await self._post("/erp/sc/routing/wms/order/getWmsLogisticsLabels", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

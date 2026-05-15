"""多平台商品 API endpoints."""
from __future__ import annotations

from ._base import BaseEndpoint


class MultiplatformPlatformsEndpoints(BaseEndpoint):
    """领星多平台商品 API (33个接口)."""

    async def aliexpress_list_v2(self, **kwargs) -> list | dict:
        """查询AliExpress在线商品 - 托管模式.

POST /basicOpen/multiplatform/aliexpress/list/v2

Args:
    isParent: 是否父体，必填，枚举值：1-父体, 0-子体, int.
    length: 分页长度，必填，每页条数, int.
    brandIds: 品牌ID列表, array.
    categoryIds: 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来, array.
    end: 结束时间，格式：yyyy-MM-dd, string.
    offset: 分页偏移量，必填，从0开始, int.
    pairingStatus: 配对状态，枚举值：0-未配对, 1-配对, null-全部, int.
    platformCodeList: 平台编码列表, array.
    price: 供货价金额, int.
    priceCondition: 供货价金额筛选条件，枚举值：1-大于, 2-小于, int.
    principalUids: 商品负责人UID列表, array.
    productTypeList: 发货模式列表，枚举值：0-仓发, 1-JIT, 2-海外备仓, array.
    productUniqueId: 商品全局唯一ID, long.
    productUniqueIdList: 父体唯一ID列表, array.
    quantity: 库存数, int.
    quantityCondition: 库存筛选条件，枚举值：1-大于, 2-小于, int.
    searchField: 搜索类型，枚举值：1-msku, 2-商品ID, 3-SKU, 4-品名, 5-SKU, 6-品名, 7-标题, int.
    searchSingleValue: 搜索值，单个模糊搜索, string.
    searchValues: 搜索值，数组，多个精确搜索, array.
    sortField: 排序字段，直接传返参的字段名, string.
    sortType: 排序类型，枚举值：asc-升序, desc-降序, string.
    start: 开始时间，格式：yyyy-MM-dd, string.
    statusList: 状态列表，枚举值：S1-待售, S2-可售, array.
    storeIds: 店铺ID列表, array.
    storeType: 店铺类型，枚举值：半托管, 全托管, 海外托管, int."""
        resp = await self._post("/basicOpen/multiplatform/aliexpress/list/v2", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def batch_temu_address_decrypt(self, **kwargs) -> dict:
        """批量TEMU地址解密.

POST /basicOpen/temu/temuAddressDecrypt

Args:
    decryptSnList: 系统单号数组 (required), array."""
        resp = await self._post("/basicOpen/temu/temuAddressDecrypt", kwargs if kwargs else None)
        return resp.data or {}
    async def coupang_stock_list(self, **kwargs) -> list | dict:
        """多平台-查询Coupang库存.

POST /basicOpen/multiplatform/coupang/stockSearch

Args:
    length: 每页条数，必填, int.
    offset: 偏移量，必填, int.
    storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】, array."""
        resp = await self._post("/basicOpen/multiplatform/coupang/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def delete_cargo_storage(self, **kwargs) -> dict:
        """删除暂存货件.

POST /basicOpen/multiplatform/deleteCargoStorage

Args:
    id: WFS货件id，查询WFS货件列表 接口对应字段【id】 (required), string."""
        resp = await self._post("/basicOpen/multiplatform/deleteCargoStorage", kwargs if kwargs else None)
        return resp.data or {}
    async def fbs_stock_list(self, **kwargs) -> list | dict:
        """多平台-查询FBS库存.

POST /basicOpen/multiplatform/fbs/stockSearch

Args:
    length: 每页条数，必填，最大200, int.
    offset: 偏移量，必填, int.
    storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】, array.
    hideZeroStorage: 是否隐藏0库存，默认0，枚举值：0-不隐藏，1-隐藏, long.
    whsIdList: 仓库ID列表, array."""
        resp = await self._post("/basicOpen/multiplatform/fbs/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbt_stock_list(self, **kwargs) -> list | dict:
        """多平台-查询FBT库存.

POST /basicOpen/multiplatform/fbt/stockSearch/v2

Args:
    length: 每页条数，必填，最大200, int.
    offset: 偏移量，必填，最小0, int.
    storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】, array."""
        resp = await self._post("/basicOpen/multiplatform/fbt/stockSearch/v2", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def fbt_stock_search(self, **kwargs) -> list | dict:
        """查询Temu库存.

POST /basicOpen/multiplatform/fbt/stockSearch

Args:
    length: 每页条数, long.
    offset: 偏移量, long.
    storeIdList: 店铺Id集合 (required), array."""
        resp = await self._post("/basicOpen/multiplatform/fbt/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def full_list(self, **kwargs) -> list | dict:
        """查询FULL库存.

POST /basicOpen/multiplatform/full/stockSearch

Args:
    length: 每页条数，必填，最大200条, int.
    offset: 分页偏移量，必填，从0开始, int.
    selectTypeEnum: 数据维度，COUNT_TYPE-数量 PRICE_TYPE-成本（必填）, string.
    custom: 自定义搜索参数, object.
    hideZeroStorage: 是否隐藏0库存，0不隐藏，1隐藏, int.
    storeIdList: 店铺ID列表, array."""
        resp = await self._post("/basicOpen/multiplatform/full/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def line_list(self, **kwargs) -> list | dict:
        """多平台-查询Line在线商品.

POST /basicOpen/multiplatform/line/list

Args:
    isParent: 是否父体，枚举值：1-父体, 0-子体, int.
    availableNumber: 可用库存数，用于库存筛选, string.
    availableNumberCondition: 库存筛选条件，枚举值：1-大于, 2-小于, int.
    brandIds: 品牌ID列表, array.
    categoryIds: 分类ID列表，如果选了父分类，要把父分类以及其下所有子分类传进来, array.
    length: 分页长度，每页条数，最大200, int.
    offset: 分页偏移量，从0开始, int.
    pairingStatus: 配对状态，枚举值：0-未配对, 1-配对, null-全部, int.
    parentUniqueIds: 父体全局唯一ID列表, array.
    price: 金额，用于价格筛选, string.
    priceCondition: 金额筛选条件，枚举值：1-大于, 2-小于, int.
    principalUids: 商品负责人UID列表, array.
    productUniqueId: 商品全局唯一ID, long.
    searchField: 搜索类型，枚举值：1-msku, 2-msku ID, 3-SKU, 4-品名, string.
    searchSingleValue: 搜索值，单个模糊搜索，字符串类型, string.
    searchValues: 搜索值，数组类型，多个精确搜索, array.
    sortField: 排序字段，直接传返参的字段名, string.
    sortType: 排序类型，枚举值：asc-升序, desc-降序, string.
    statusList: 状态列表，枚举值：0-正常, 1-已删除, array.
    storeIds: 店铺ID列表, array."""
        resp = await self._post("/basicOpen/multiplatform/line/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def query_shipping_list_v2(self, **kwargs) -> list | dict:
        """查询平台仓发货单列表v2.

POST /basicOpen/multiplatform/query/shippingList

Args:
    platformCodes: 平台代码 Walmart 10008 TikTok 10011 Temu 10022 Shein 10027 (required), array.
    offset: 分页偏移量, int.
    length: 分页长度, int.
    timeField: 时间维度 1 创建时间 2 发货时间 3 开船时间 4 预计到港时间 5 实际妥投时间 6 实际发货时间, int.
    startTime: 开始时间, string.
    endTime: 结束时间, string.
    pickingStatus: 拣货状态 1 已拣货 0 待拣货, string.
    shippingListStatus: 发货单状态 0 待配货 1 待发货 2 已发货 3 已作废, int.
    searchField: 搜索维度 1 MSKU 2 发货单号 7 货件单号 8 商品条码, int.
    searchSingleValue: 模糊搜索值, string.
    storeIds: 店铺id列表，对应查询多平台店铺信息接口对应字段【store_id】, array.
    updateStartTime: 修改开始时间, string.
    updateEndTime: 修改结束时间, string.
    isDelete: 是否删除 0 未删除（默认） 1 已删除, int."""
        resp = await self._post("/basicOpen/multiplatform/query/shippingList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shein_list(self, **kwargs) -> list | dict:
        """查询Shein在线商品.

POST /basicOpen/multiplatform/shein/list

Args:
    brandIds: 品牌ID列表, array.
    categoryIds: 分类ID列表, array.
    offset: 偏移量, int.
    length: 分页长度，上限1000, int.
    pairingStatus: 配对状态 0、未配对 1、已配对, int.
    searchField: 搜索字段 1、标题 2、品名 3、SPU货号 4、SKC货号 5、平台SPU 6、平台SKC 7、MSKU ID 8、SKU 9、MSKU, string.
    status: 状态 0、删除 1、在售 2、停售, int.
    storeIds: 店铺ID列表, array.
    searchSingleValue: 单一值搜索, string.
    searchValues: 精确搜索值列表, array."""
        resp = await self._post("/basicOpen/multiplatform/shein/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shopify_variant_list(self, **kwargs) -> list | dict:
        """查询Shopify在线商品.

POST /basicOpen/multiplatform/shopify/variantList

Args:
    store_ids: 店铺Id, array.
    status: 状态 1、Active 2、Draft 3、Archived 4、Deleted, array.
    inventory_policy: 库存策略 1、不跟踪库存 2、缺货停止销售 3、缺货继续销售, array.
    type_id: 分类Id, array.
    offset: 分页偏移量, int.
    length: 分页长度，上限1000, int.
    search_field: 搜索维度, int.
    search_single_value: 模糊搜索值, string.
    search_values: 精确搜索列表，上限200个, array.
    quantity: 库存数量, string.
    quantity_condition: 库存数量大于或小于 1、大于 2、小于, int.
    price: 售价, long.
    price_condition: 售价大于或小于 1、大于 2、小于, int.
    listing_time_field: 时间维度, int.
    listing_start_time: 开始时间, string.
    listing_end_time: 结束时间, string."""
        resp = await self._post("/basicOpen/multiplatform/shopify/variantList", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_cargo(self, **kwargs) -> list | dict:
        """查询Temu货件.

POST /basicOpen/multiplatform/temu/cargo

Args:
    endTime: yyyy-MM-dd (required), date.
    length: 每页条数, long.
    offset: 偏移量, long.
    startTime: yyyy-MM-dd (required), date.
    statusList: 待发货：0 ；待收货：1 ；已收货：2 ；已入库：3 ；已退货：4 ；已取消：5 ；部分收货：6 ;待申报（本地状态）7 (required), array.
    timeType: 1:创建时间  2：发货时间 3：收货时间  4：入库时间 (required), int."""
        resp = await self._post("/basicOpen/multiplatform/temu/cargo", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_list(self, **kwargs) -> list | dict:
        """查询Temu在线商品.

POST /basicOpen/multiplatform/temu/list

Args:
    brandIds: 品牌id列表, array.
    categoryIds: 分类id列表, array.
    offset: 分页偏移量, int.
    length: 分页长度，上限1000, int.
    pairingStatus: 配对状态 0、未配对 1、已配对, int.
    searchField: 搜索维度 1、标题 2、品名 4、SKC货号 5、平台SPU 6、平台SKC 7、MSKU ID 8、SKU 9、MSKU (required), string.
    status: 状态 0、删除 2、正常, int.
    storeIds: 店铺id列表, array.
    searchValues: 精确搜索值列表, array.
    searchSingleValue: 模糊搜索值, string."""
        resp = await self._post("/basicOpen/multiplatform/temu/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def tik_tok_list(self, **kwargs) -> list | dict:
        """查询TikTok在线商品.

POST /basicOpen/multiplatform/tiktok/list

Args:
    brandIds: 品牌id列表, array.
    categoryIds: 分类id列表, array.
    offset: 分页偏移量, int.
    length: 分页长度，上限1000, int.
    pairingStatus: 配对状态, int.
    searchField: 搜索维度 1、标题 2、品名 5、平台SPU 7、MSKU ID 8、SKU 9、MSKU 10、SPU货号, string.
    platformStatus: 状态 DRAFT PENDING FAILED ACTIVATE SELLER_DEACTIVATED PLATFORM_DEACTIVATED FREEZE DELETED, array.
    storeIds: 店铺id列表, array.
    searchSingleValue: 搜索值, string.
    searchValues: 搜索值列表, array."""
        resp = await self._post("/basicOpen/multiplatform/tiktok/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def wayfair_stock_list(self, **kwargs) -> list | dict:
        """多平台-查询wayfair库存.

POST /basicOpen/multiplatform/wayfair/stockSearch

Args:
    length: 每页条数，必填，最大200, int.
    offset: 偏移量，必填，表示从第几条开始，最小为0, int.
    storeIds: 店铺ID列表，必填，对应查询多平台店铺信息接口对应字段【store_id】, array.
    warehouseIds: 仓库ID列表, array."""
        resp = await self._post("/basicOpen/multiplatform/wayfair/stockSearch", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def add_cargo_goods_list(self, **kwargs) -> dict:
        """查询WFS货件可添加商品列表.

POST /basicOpen/multiplatform/cargo/addCargoGoods/list

Args:
    store_id: 店铺id (required), string.
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int."""
        resp = await self._post("/basicOpen/multiplatform/cargo/addCargoGoods/list", kwargs if kwargs else None)
        return resp.data or {}
    async def address_return_address_list(self, **kwargs) -> dict:
        """查询退件地址列表.

POST /basicOpen/multiplatform/address/returnAddressList

Args:
    store_id: 店铺id (required), string."""
        resp = await self._post("/basicOpen/multiplatform/address/returnAddressList", kwargs if kwargs else None)
        return resp.data or {}
    async def aliexpress_list(self, **kwargs) -> list | dict:
        """查询AliExpress在线商品 - 自运营.

POST /basicOpen/multiplatform/aliExpress/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    store_ids: 店铺id, array.
    status: 状态： 1 正在销售 2 已下架 3 审核中 4 审核不通过, array.
    listing_time_field: 查询时间类型： 1 创建时间 2 结束时间, int.
    listing_start_time: 开始日期，Y-m-d，闭区间【开始结束时间不超过31天】, string.
    listing_end_time: 结束日期，Y-m-d，闭区间【开始结束时间不超过31天】, string.
    search_field: 搜索字段类型： 1 MSKU 2 商品ID 3 SKU 4 标题, int.
    search_single_value: 搜索值(字符串,单个模糊搜索）, string."""
        resp = await self._post("/basicOpen/multiplatform/aliExpress/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def e_bay_list(self, **kwargs) -> list | dict:
        """查询eBay在线商品列表.

POST /basicOpen/multiplatform/ebay/list

Args:
    offset: 分页偏移量, int.
    length: 分页长度，默认20，最大上限200, int.
    store_ids: 店铺id, array.
    site_code: 站点code, array.
    listing_status: 销售状态, array.
    auto_restocks: 是否自动补货： 0 无补货规则 1 启用 2 停用, array.
    listing_type: 销售类型： 1 拍卖 2 固价 3 多属性, array.
    search_field: 查询字段类型： 1 msku 2 商品ID 3 sku 4 标题 5 品名 6 walmart gtin码, int.
    search_single_value: 搜索值(字符串,单个模糊搜索), string.
    listing_time_field: 查询时间类型： 1 创建时间 2 结束时间, int.
    listing_start_time: 开始时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】, string.
    listing_end_time: 结束时间(站点时间)，Y-m-d，闭区间【开始结束时间不超过31天】, string."""
        resp = await self._post("/basicOpen/multiplatform/ebay/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def multiplatform_cargo_storage(self, **kwargs) -> list | dict:
        """WFS货件暂存.

POST /basicOpen/multiplatform/cargo/storage

Args:
    store_id: 店铺id (required), string.
    cargo_goods_list: 货件包含的商品 (required), array.
    cargo_remark: 货件备注, string.
    inbound_order_id: 入库订单id, string.
    return_address: 退件地址，查询退件地址列表 接口获取 (required), object."""
        resp = await self._post("/basicOpen/multiplatform/cargo/storage", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_msku(self, **kwargs) -> list | dict:
        """查询结算利润（利润报表）-msku.

POST /basicOpen/multiplatform/profit/report/msku

Args:
    offset: 分页偏移量，默认0 (required), number.
    length: 分页长度，默认20，最大200 (required), number.
    platformCodeS: 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein平台模式 10022 Temu全托 10024 Temu半托 10028 Shein半托管, array.
    mids: 国家id，多个使用英文逗号分隔, string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】, string.
    currencyCode: 币种code： 原币种 USD EUR GBP CNY, string.
    startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    searchField: 搜索值类型： msku MSKU local_sku SKU platform_order_no 平台单号, string.
    searchValue: 搜索值, string.
    developers: 开发人, array.
    cids: 分类, array.
    bids: 品牌, array."""
        resp = await self._post("/basicOpen/multiplatform/profit/report/msku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_order(self, **kwargs) -> list | dict:
        """查询结算利润（利润报表）-订单.

POST /basicOpen/multiplatform/profit/report/order

Args:
    offset: 分页偏移量，默认0 (required), number.
    length: 分页长度，默认200 (required), number.
    platformCodeS: 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee 10007 Lazada  10008 walmart 10011 Tiktok 10021 Shein平台模式 10022 Temu全托 10024 Temu半托 10028 Shein半托管 10038 Line Shopping, array.
    mids: 国家id，多个使用英文逗号分隔, string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】, string.
    transactionTypeS: 交易类型：0 销售，2 退货，4 退款，5 补发，6 调整，7 其他, array.
    currencyCode: 币种code：原币种，USD，EUR，GBP，CNY, string.
    searchDateType: 时间筛选方式：1 下单时间，2 结算日期【默认】，3 发货日期, string.
    startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    searchField: 搜索值类型：msku MSKU，local_sku SKU，product_name，品名，platform_order_no 平台单号, string.
    searchValue: 搜索值, string."""
        resp = await self._post("/basicOpen/multiplatform/profit/report/order", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_seller(self, **kwargs) -> list | dict:
        """查询结算利润（利润报表）-店铺.

POST /basicOpen/multiplatform/profit/report/seller

Args:
    offset: 分页偏移量，默认0 (required), number.
    length: 分页长度，默认1000 (required), number.
    platformCodeS: 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein平台模式 10022 Temu全托 10024 Temu半托 10028 Shein半托管, array.
    mids: 国家id，多个使用英文逗号分隔, string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】, string.
    currencyCode: 币种code： 原币种 USD EUR GBP CNY, string.
    startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (required), string."""
        resp = await self._post("/basicOpen/multiplatform/profit/report/seller", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def profit_report_sku(self, **kwargs) -> list | dict:
        """查询结算利润（利润报表）-sku.

POST /basicOpen/multiplatform/profit/report/sku

Args:
    offset: 分页偏移量，默认0 (required), number.
    length: 分页长度，默认1000 (required), number.
    platformCodeS: 平台id： 10002 Shopify 10003 eBay 10005 AliExpress 10006 Shopee  10008 walmart 10011 Tiktok 10021 Shein平台模式 10022 Temu全托 10024 Temu半托 10028 Shein半托管, array.
    mids: 国家id，多个使用英文逗号分隔 (required), string.
    sids: 店铺id，多个使用英文逗号分隔 ，对应查询多平台店铺信息接口对应字段【store_id】, string.
    currencyCode: 币种code： 原币种 USD EUR GBP CNY, string.
    startDate: 开始时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    endDate: 结束时间【结算日期】，闭区间，格式：Y-m-d (required), string.
    searchField: 搜索值类型： local_sku SKU platform_order_no 平台单号, string.
    searchValue: 搜索值, string.
    developers: 开发人, array.
    cids: 分类, array.
    bids: 品牌, array."""
        resp = await self._post("/basicOpen/multiplatform/profit/report/sku", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def self_shipment_order_delivery_goods(self, **kwargs) -> list | dict:
        """订单发货.

POST /basicOpen/selfShipmentOrder/deliveryGoods

Args:
    order_number_list: 系统单号列表，多个使用英文逗号分隔，上限100 (required), string."""
        resp = await self._post("/basicOpen/selfShipmentOrder/deliveryGoods", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def set_order_weighed(self, **kwargs) -> list | dict:
        """订单称重.

POST /erp/sc/routing/wms/order/setOrderWeighed

Args:
    order_number: 系统单号 与销售出库单二选一, string.
    wo_number: 销售出库单 与系统单号二选一, string.
    pkg_real_weight: 重量 (required), string.
    pkg_real_weight_unit: 单位 支持 g,kg,oz,lb (required), string.
    sync_product_gross_weight: 一单一件同步重量到产品模块 0:否,1:是  默认否, string."""
        resp = await self._post("/erp/sc/routing/wms/order/setOrderWeighed", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_detail_by_code(self, **kwargs) -> list | dict:
        """查询平台仓发货单详情.

POST /basicOpen/multiplatform/query/shippingDetail

Args:
    shippingListCode: 发货单编号 (required), string."""
        resp = await self._post("/basicOpen/multiplatform/query/shippingDetail", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_order_allocate(self, **kwargs) -> dict:
        """平台仓发货单分配库存.

POST /basicOpen/multiplatform/allocate/stock

Args:
    shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id, array."""
        resp = await self._post("/basicOpen/multiplatform/allocate/stock", kwargs if kwargs else None)
        return resp.data or {}
    async def shipping_order_delivery(self, **kwargs) -> list | dict:
        """平台仓发货单发货.

POST /basicOpen/multiplatform/shippingList/delivery

Args:
    shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id, array."""
        resp = await self._post("/basicOpen/multiplatform/shippingList/delivery", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def shipping_order_picking(self, **kwargs) -> list | dict:
        """平台仓发货单拣货.

POST /basicOpen/multiplatform/shippingList/picking

Args:
    shippingIdList: 发货单ID列表，对应查询平台仓发货单列表v2接口出参id, array."""
        resp = await self._post("/basicOpen/multiplatform/shippingList/picking", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def temu_stock_order_query_page(self, **kwargs) -> list | dict:
        """查询Temu平台仓备货单列表.

POST /basicOpen/stockOrder/temu/queryPage

Args:
    length: 每页条数，最小 20，最大 500 (required), number.
    offset: 分页偏移量，最小 0 (required), number.
    current: 当前页码, number.
    storeIdList: 店铺 ID 列表，可多选, array.
    statusList: 备货单时效状态列表。 0 发货即将逾期 1 发货已逾期 2 到货即将逾期 3 到货已逾期, array.
    bizStatusList: 单据状态列表。 0 待接单 1 待发货 2 已送货 3 已收货 5 质检全部退回 6 已验收 7 已入库 8 已作废 9 已超时, array.
    settlementType: VMI 单标识。 0 非 VMI(采购) 1 VMI(备货), number.
    urgencyType: 紧急备货单标识。 0 否 1 是, number.
    timeType: 日期类型。 0 下单时间 1 发货时间 2 收货时间 3 最晚发货时间 4 最晚到货时间, number.
    startTime: 开始日期，格式 `yyyy-MM-dd`, string.
    endTime: 结束日期，格式 `yyyy-MM-dd`, string.
    searchType: 搜索类型。 0 备货单号 1 货件号 2 SKC 3 MSKU 4 SPU 5 SKU 6 品名 7 备注 8 MSKU_CODE。当传入 `searchValueList` 时，`searchType` 必传。, number.
    fuzzySearchValue: 模糊搜索值，多个值时以下游要求的换行符拼接, string.
    searchValueList: 批量搜索值列表。传入后系统会自动以换行符拼接。当传入 `searchValueList` 时，`searchType` 必传。, array.
    receivingWarehouseList: 收货仓库列表, array.
    joinPlatformStatus: 发货台状态。 0 不可加入发货台 1 已加入发货台 2 可以加入发货台, number.
    isGenerateCargo: 是否已经生成货件。 0 未生成 1 已生成, number.
    isJitOrder: 是否 JIT 订单。 0 否 1 是, number.
    isFirst: 是否首单, boolean.
    ids: ID 列表筛选, array."""
        resp = await self._post("/basicOpen/stockOrder/temu/queryPage", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}
    async def walmart_list(self, **kwargs) -> list | dict:
        """查询Walmart在线商品.

POST /basicOpen/multiplatform/walmart/list

Args:
    offset: 分页偏移量，默认0, int.
    length: 分页长度，默认20，上限200, int.
    store_ids: 店铺id, array.
    status: 状态： 0 PUBLISHED 1 READY TO PUBLISH 2 IN PROGRESS 3 UNPUBLISHED 4 STAGE 5 SYSTEM PROBLEM, array.
    fulfillment_types: 发货方式： 0 WFS Eligible 1 Walmart Fulfilled 2 Seller Fulfilled, array.
    listing_time_field: 搜索时间类型： 1 创建时间 2 更新时间, int.
    listing_start_time: 开始日期，Y-m-d，闭区间【开始结束时间不超过31天】, string.
    listing_end_time: 结束日期，Y-m-d，闭区间【开始结束时间不超过31天】, string.
    search_field: 搜索字段类型： 1 MSKU 2 商品ID 3 SKU 4 标题, int.
    search_single_value: 搜索值(字符串,单个模糊搜索), string."""
        resp = await self._post("/basicOpen/multiplatform/walmart/list", kwargs if kwargs else None)
        if isinstance(resp.data, list):
            return resp.data
        return resp.data or {}

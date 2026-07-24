"""Auto-generated request models for {category} APIs."""

from typing import Optional

from ..common import LingXingModel


class RequestBase(LingXingModel):
    """Base class for all request models."""

    pass


class SourcedataFbmreturnorderlistRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBM退货订单.

    API: POST /erp/sc/routing/data/order/fbmReturnOrderList
    Doc: https://apidoc.lingxing.com/#/SourceData/fbmReturnOrderList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str
    # 开始时间，左闭区间，格式：Y-m-d
    end_date: str
    # 结束时间，右开区间，格式：Y-m-d
    date_type: Optional[int] = None
    # 时间查询类型：【默认1】 1 退货日期 2 下单日期
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataRefundordersRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBA退货订单.

    API: POST /erp/sc/data/mws_report/refundOrders
    Doc: https://apidoc.lingxing.com/#/SourceData/RefundOrders
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    date_type: Optional[int] = None
    # 时间查询类型【默认1】： 1 退货时间【站点时间】 2 更新时间【北京时间】
    start_date: str
    # 开始时间，左闭右开，格式：Y-m-d
    end_date: str
    # 结束时间，左闭右开，格式：Y-m-d
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataAllordersRequest(RequestBase):
    """Request model for 查询亚马逊源报表-所有订单.

    API: POST /erp/sc/data/mws_report/allOrders
    Doc: https://apidoc.lingxing.com/#/SourceData/AllOrders
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    date_type: Optional[int] = None
    # 时间查询类型：【默认1】 1 下单日期 2 亚马逊订单更新时间
    start_date: str
    # 亚马逊当地下单时间，左闭区间，格式：Y-m-d
    end_date: str
    # 亚马逊当地下单时间，右开区间，格式：Y-m-d
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataFbaordersRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBA订单.

    API: POST /erp/sc/data/mws_report/fbaOrders
    Doc: https://apidoc.lingxing.com/#/SourceData/FbaOrders
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    date_type: Optional[int] = None
    # 日期搜索维度：【默认1】 1 下单日期 2 配送日期
    start_date: str
    # 开始日期，左闭区间，Y-m-d格式
    end_date: str
    # 结束日期，右开区间，Y-m-d格式
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataFbaexchangeorderlistRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBA换货订单.

    API: POST /erp/sc/routing/data/order/fbaExchangeOrderList
    Doc: https://apidoc.lingxing.com/#/SourceData/fbaExchangeOrderList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str
    # 开始时间，左闭区间，格式：Y-m-d
    end_date: str
    # 结束时间，右开区间，格式：Y-m-d
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataRemovalorderlistnewRequest(RequestBase):
    """Request model for 查询亚马逊源报表-移除订单（新）.

    API: POST /erp/sc/routing/data/order/removalOrderListNew
    Doc: https://apidoc.lingxing.com/#/SourceData/RemovalOrderListNew
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str
    # 查询时间【更新时间】，左闭区间,格式：Y-m-d
    end_date: str
    # 查询时间【更新时间】，右开区间,格式：Y-m-d
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000
    search_field_time: str
    # 搜索时间类型：【默认 last_updated_date】 last_updated_date 更新时间 request_date 创建时间


class SourcedataSourceremovalordersRequest(RequestBase):
    """Request model for 查询亚马逊源报表-移除订单（旧）.

    API: POST /erp/sc/data/mws_report/removalOrders
    Doc: https://apidoc.lingxing.com/#/SourceData/SourceRemovalOrders
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str
    # 更新时间，左闭区间，格式：Y-m-d
    end_date: str
    # 更新时间，右开区间，格式：Y-m-d格式
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataRemovalshipmentlistRequest(RequestBase):
    """Request model for 查询亚马逊源报表-移除货件（新）.

    API: POST /erp/sc/statistic/removalShipment/list
    Doc: https://apidoc.lingxing.com/#/SourceData/RemovalShipmentList
    """

    sid: Optional[int] = None
    # 店铺id【seller_id同时传值时，以sid为准】 ，对应查询亚马逊店铺列表接口对应字段【sid】
    seller_id: Optional[str] = None
    # 亚马逊店铺id ,对应查询亚马逊店铺列表接口对应字段【seller_id】
    start_date: str
    # 开始日期【发货日期】，左闭右开
    end_date: str
    # 结束日期【发货日期】，左闭右开
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataRemovallistsRequest(RequestBase):
    """Request model for 查询亚马逊源报表-移除货件（旧）.

    API: POST /erp/sc/data/fba_report/removalLists
    Doc: https://apidoc.lingxing.com/#/SourceData/RemovalLists
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    start_date: str
    # 开始时间，格式：Y-m-d，闭区间
    end_date: str
    # 结束时间，格式：Y-m-d，开区间
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataManageinventoryRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBA库存.

    API: POST /erp/sc/data/mws_report/manageInventory
    Doc: https://apidoc.lingxing.com/#/SourceData/ManageInventory
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataDailyinventoryRequest(RequestBase):
    """Request model for 查询亚马逊源报表-每日库存.

    API: POST /erp/sc/data/mws_report/dailyInventory
    Doc: https://apidoc.lingxing.com/#/SourceData/DailyInventory
    """

    sid: int
    # 店铺id【欧洲传UK下的店铺，美国传US下的店铺】 ，对应查询亚马逊店铺列表接口对应字段【sid】
    event_date: str
    # 报表日期，格式：Y-m-d
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataAfnfulfillablequantityRequest(RequestBase):
    """Request model for 查询亚马逊源报表-FBA可售库存.

    API: POST /erp/sc/data/mws_report/getAfnFulfillableQuantity
    Doc: https://apidoc.lingxing.com/#/SourceData/AfnFulfillableQuantity
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataReservedinventoryRequest(RequestBase):
    """Request model for 查询亚马逊源报表-预留库存.

    API: POST /erp/sc/data/mws_report/reservedInventory
    Doc: https://apidoc.lingxing.com/#/SourceData/ReservedInventory
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataGetfbaagelistRequest(RequestBase):
    """Request model for 查询亚马逊源报表—库龄表.

    API: POST /erp/sc/routing/fba/fbaStock/getFbaAgeList
    Doc: https://apidoc.lingxing.com/#/SourceData/getFbaAgeList
    """

    sid: str
    # 店铺id, 多个使用英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    offset: Optional[int] = None
    # 分页偏移量
    length: Optional[int] = None
    # 分页长度，默认20


class SourcedataTransactionRequest(RequestBase):
    """Request model for 查询亚马逊源报表-交易明细.

    API: POST /erp/sc/data/mws_report/transaction
    Doc: https://apidoc.lingxing.com/#/SourceData/Transaction
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    event_date: str
    # 报表日期，格式：Y-m-d【每月３日后支持查询上月数据】
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataGetamazonfulfilledshipmentslistRequest(RequestBase):
    """Request model for 查询亚马逊源报表—Amazon Fulfilled Shipments.

    API: POST /erp/sc/data/mws_report/getAmazonFulfilledShipmentsList
    Doc: https://apidoc.lingxing.com/#/SourceData/getAmazonFulfilledShipmentsList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    shipment_date_after: str
    # 快照开始时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天
    shipment_date_before: str
    # 快照结束时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataV1getamazonfulfilledshipmentslistRequest(RequestBase):
    """Request model for 查询亚马逊源报表—Amazon Fulfilled Shipments v1.

    API: POST /erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList
    Doc: https://apidoc.lingxing.com/#/SourceData/v1getAmazonFulfilledShipmentsList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    shipment_date_after: str
    # 快照开始时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天
    shipment_date_before: str
    # 快照结束时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss， 开始结束时间区间支持7天
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataGetfbainventoryeventdetaillistRequest(RequestBase):
    """Request model for 查询亚马逊源报表——Inventory Event Detail.

    API: POST /erp/sc/data/mws_report/getFbaInventoryEventDetailList
    Doc: https://apidoc.lingxing.com/#/SourceData/getFbaInventoryEventDetailList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    snapshot_date_after: str
    # 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天
    snapshot_date_before: str
    # 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000


class SourcedataV1getfbainventoryeventdetaillistRequest(RequestBase):
    """Request model for 查询亚马逊源表数据--Inventory Event Detail v1.

    API: POST /erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList
    Doc: https://apidoc.lingxing.com/#/SourceData/v1getFbaInventoryEventDetailList
    """

    sid: int
    # 店铺id ，对应查询亚马逊店铺列表接口对应字段【sid】
    snapshot_date_after: str
    # 快照开始时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天
    snapshot_date_before: str
    # 快照结束时间【snapshot_date_locale】，格式：Y-m-d，开始结束时间区间支持7天
    offset: Optional[int] = None
    # 分页偏移量，默认0
    length: Optional[int] = None
    # 分页长度，默认1000，上限10000


class SourcedataAdjustmentlistRequest(RequestBase):
    """Request model for 查询亚马逊源报表-盘存记录.

    API: POST /basicOpen/openapi/mwsReport/adjustmentList
    Doc: https://apidoc.lingxing.com/#/SourceData/AdjustmentList
    """

    offset: int
    # 分页偏移量，默认0
    length: int
    # 分页长度，默认20，上限10000
    sids: Optional[str] = None
    # 店铺id，多个店铺以英文逗号分隔 ，对应查询亚马逊店铺列表接口对应字段【sid】
    search_field: Optional[str] = None
    # 搜索的字段： asin ASIN msku MSKU fnsku FNSKU item_name 标题 transaction_item_id 交易编号
    search_value: Optional[str] = None
    # 搜索值
    start_date: str
    # 发货日期开始时间【闭区间】，格式Y-m-d【report_date】
    end_date: str
    # 发货日期结束时间【闭区间】，格式Y-m-d【report_date】

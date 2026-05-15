"""Request models for VC APIs (auto-generated from API docs)."""

from typing import Any, List, Optional

from ..common import LingXingModel


class VCPlatformauthvcsellerpagelistRequest(LingXingModel):
    """Request for 查询VC店铺列表.
    
    POST /basicOpen/platformAuth/vcSeller/pageList
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200


class VCListingmanagevclistingpagelistRequest(LingXingModel):
    """Request for 查询Listing列表.
    
    POST /basicOpen/listingManage/vcListing/pageList
    """
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    vc_store_ids: Optional[list] = None  # vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】


class VCVcorderpagelistRequest(LingXingModel):
    """Request for 查询VC订单列表.
    
    POST /basicOpen/platformOrder/vcOrder/pageList
    """
    purchase_order_type: List  # 订单类型： 0  DF 1  PO  2  DI
    offset: Optional[int] = None  # 分页偏移量，默认0
    length: Optional[int] = None  # 分页长度，默认20，上限200
    vc_store_ids: Optional[list] = None  # vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】
    search_field_time: Optional[str] = None  # 查询时间类型： 1  订购时间 2  要求发货时间 3  订单更新时间
    start_date: Optional[str] = None  # 开始时间，开区间，格式：Y-m-d，时间间隔最长不超过90天
    end_date: Optional[str] = None  # 结束时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天
    search_field: Optional[str] = None  # 搜索类型： purchase_order_number 订单号 asin ASIN local_name 品名  customer_order_number 客户订单号【DF类型订单】 vendor_
    search_value: Optional[list] = None  # 搜索值


class VCVcorderpodetailRequest(LingXingModel):
    """Request for 查询VC订单详情【PO】.
    
    POST /basicOpen/platformOrder/vcOrderPo/detail
    """
    local_po_number: str  # 本地po号，查询VC订单列表 接口字段【local_po_number】


class VCVcorderdfdetailRequest(LingXingModel):
    """Request for 查询VC订单详情【DF】.
    
    POST /basicOpen/platformOrder/vcOrderDf/detail
    """
    vc_store_id: str  # vc店铺id，查询VC店铺列表 接口对应字段【vc_store_id】
    purchase_order_number: str  # 订单编号


class VCVcorderdfconfirmshipmentRequest(LingXingModel):
    """Request for VC订单-确认发货【DF】.
    
    POST /basicOpen/platformOrder/vcOrderDf/confirmShipment
    """
    ids: List  # 订单ID，查询VC订单列表接口对应字段【id】


class VCVcorderdfsubmitshippinglabelRequest(LingXingModel):
    """Request for VC订单-请求标签【DF】.
    
    POST /basicOpen/platformOrder/vcOrderDf/submitShippingLabel
    """
    ids: List  # 订单ID，查询VC订单列表接口对应字段【id】


class VCVcorderdfgetshippinglabelRequest(LingXingModel):
    """Request for VC订单-打印标签【DF】.
    
    POST /basicOpen/platformOrder/vcOrderDf/getShippingLabel
    """
    ids: List  # 订单ID，查询VC订单列表接口对应字段【id】


class VCVcdeliverpagelistRequest(LingXingModel):
    """Request for 查询VC发货单列表.
    
    POST /basicOpen/openapi/getInvoice/page/list
    """
    offset: Optional[float] = None  # 偏移量(默认0)
    length: Optional[float] = None  # 每页条数(默认20）
    sids: Optional[list] = None  # 店铺id
    wid: Optional[list] = None  # 国家id
    shipmentType: str  # 出库类型 1:DF 2:PO 3:DI
    status: Optional[float] = None  # 订单状态 0: 全部 5:待配货 10:待出库 15:已完成 100:已作废 (默认0）
    createTimeStartTime: Optional[str] = None  # 创建日期-开始
    createTimeEndTime: Optional[str] = None  # 创建日期-结束
    shipmentTimeStartTime: Optional[str] = None  # 出库日期-开始
    shipmentTimeEndTime: Optional[str] = None  # 出库日期-结束


class VCVcdeliverdetailRequest(LingXingModel):
    """Request for 查询VC发货单详情.
    
    POST /basicOpen/openapi/getInvoice/detail
    """
    orderNo: str  # 订单号

"""FBA shipment management API endpoints."""

import logging
from typing import Any

from lingxing.core.openapi import OpenApiBase
from lingxing.core.resp_schema import ResponseResult

logger = logging.getLogger(__name__)


class FBAEndpoints:
    """FBA shipment management API endpoints."""

    def __init__(self, openapi: OpenApiBase):
        """
        初始化FBA端点

        Args:
            openapi: OpenAPI基础客户端实例
        """
        self.openapi = openapi

    async def _request_with_token(
        self,
        access_token: str,
        route: str,
        req_body: dict[str, Any],
        **kwargs
    ) -> ResponseResult:
        """
        发送带Token的POST请求

        Args:
            access_token: 访问令牌
            route: API路由
            req_body: 请求体
            **kwargs: 其他参数

        Returns:
            ResponseResult: API响应结果
        """
        return await self.openapi.request(
            access_token=access_token,
            route_name=route,
            method="POST",
            req_body=req_body,
            **kwargs
        )

    # ==================== 货件查询API ====================

    async def get_shipment_list(
        self,
        access_token: str,
        sid: str,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 1000,
        shipment_id: str | None = None,
        shipment_status: str | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA货件列表

        API: POST /erp/sc/data/fba_report/shipmentList

        Args:
            access_token: 访问令牌
            sid: 店铺ID，多个以英文逗号分隔
            start_date: 货件创建开始日期，格式 YYYY-MM-DD
            end_date: 货件创建截止日期，格式 YYYY-MM-DD
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000
            shipment_id: 货件单号，多个以英文逗号隔开，仅支持精确搜索
            shipment_status: 货件状态，多个以英文逗号分隔
                (UNCONFIRMED, IN_TRANSIT, DELIVERED, CHECKED_IN, ABANDONED,
                 DELETED, CLOSED, CANCELLED, WORKING, RECEIVING, SHIPPED, READY_TO_SHIP)
            **kwargs: 其他查询参数
                - extra_date_field: 根据日期范围查询字段(update=货件修改日期)
                - start_extra_date: 额外开始日期
                - end_extra_date: 额外结束日期

        Returns:
            ResponseResult: 包含 {list: [...], total: int}

        Example:
            >>> result = await fba.get_shipment_list(
            ...     access_token="xxx",
            ...     sid="4661",
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
            >>> data = result.data  # {"list": [...], "total": 100}
        """
        logger.debug("Fetching FBA shipment list: sid=%s, start=%s, end=%s", sid, start_date, end_date)

        req_body = {
            "sid": sid,
            "start_date": start_date,
            "end_date": end_date,
            "offset": offset,
            "length": length,
            **kwargs
        }

        if shipment_id:
            req_body["shipment_id"] = shipment_id
        if shipment_status:
            req_body["shipment_status"] = shipment_status

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/fba_report/shipmentList",
            req_body=req_body
        )

    async def get_fba_received_inventory(
        self,
        access_token: str,
        sid: int,
        event_date: str | None = None,
        fba_shipment_id: list[str] | None = None,
        offset: int = 0,
        length: int = 1000
    ) -> ResponseResult:
        """
        查询FBA到货接收明细

        API: POST /erp/sc/data/fba_report/receivedInventory

        查询库存分类账里货件在FBA仓库的签收数据

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            event_date: 签收日期，格式 YYYY-MM-DD，未填写fba_shipment_id时必填
            fba_shipment_id: 货件单号列表，未填写event_date时必填
            offset: 分页偏移量，默认0
            length: 分页长度，默认1000

        Returns:
            ResponseResult: 包含签收明细列表

        Example:
            >>> result = await fba.get_fba_received_inventory(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     event_date="2026-02-01"
            ... )
        """
        logger.debug("Fetching FBA received inventory: sid=%s, event_date=%s", sid, event_date)

        req_body = {
            "sid": sid,
            "offset": offset,
            "length": length
        }

        if event_date:
            req_body["event_date"] = event_date
        if fba_shipment_id:
            req_body["fba_shipment_id"] = fba_shipment_id

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/fba_report/receivedInventory",
            req_body=req_body
        )

    # ==================== STA任务API ====================

    async def create_sta_task(
        self,
        access_token: str,
        sid: int,
        address_line1: str,
        city: str,
        country_code: str,
        phone_number: str,
        postal_code: str,
        shipper_name: str,
        state_or_province_code: str,
        inbound_plan_items: list[dict[str, Any]],
        position_type: int = 1,
        **kwargs
    ) -> ResponseResult:
        """
        创建STA任务

        API: POST /amzStaServer/openapi/inbound-plan/createInboundPlan

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            address_line1: 详细街道地址1
            city: 城市
            country_code: 国家(地区)编码
            phone_number: 电话号码
            postal_code: 邮政编码
            shipper_name: 发货方名称
            state_or_province_code: 州/省/地区编码
            inbound_plan_items: 计划明细列表
                - msku: MSKU (必填)
                - quantity: 申报量 (必填)
                - labelOwner: 标签类型 (AMAZON/SELLER/NONE)
                - prepOwner: 预处理提供方 (AMAZON/SELLER/NONE)
                - expiration: 有效期
                - prepCategory: 预处理分类
                - prepTypes: 预处理类型列表
            position_type: 分仓方式 (1=先装箱再分仓, 2=先分仓再装箱)
            **kwargs: 其他参数
                - addressLine2: 详细街道地址2
                - companyName: 公司名称
                - email: 邮箱
                - planName: 计划名称
                - remark: 备注

        Returns:
            ResponseResult: 包含 {inboundPlanId, taskId, taskStatus}

        Example:
            >>> result = await fba.create_sta_task(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     address_line1="123 Main St",
            ...     city="Seattle",
            ...     country_code="US",
            ...     phone_number="1234567890",
            ...     postal_code="98101",
            ...     shipper_name="ABC Company",
            ...     state_or_province_code="WA",
            ...     inbound_plan_items=[
            ...         {"msku": "SKU001", "quantity": 100, "labelOwner": "SELLER"}
            ...     ]
            ... )
        """
        logger.debug("Creating STA task: sid=%s", sid)

        req_body = {
            "sid": sid,
            "addressLine1": address_line1,
            "city": city,
            "countryCode": country_code,
            "phoneNumber": phone_number,
            "postalCode": postal_code,
            "shipperName": shipper_name,
            "stateOrProvinceCode": state_or_province_code,
            "inboundPlanItems": inbound_plan_items,
            "positionType": str(position_type),
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-plan/createInboundPlan",
            req_body=req_body
        )

    async def get_sta_task_list(
        self,
        access_token: str,
        page: int,
        length: int,
        date_begin: str,
        date_end: str,
        date_type: int = 1,
        sids: list[int] | None = None,
        status_list: list[str] | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        查询STA任务列表

        API: POST /amzStaServer/openapi/inbound-plan/page

        Args:
            access_token: 访问令牌
            page: 分页页码
            length: 分页大小，上限200
            date_begin: 开始时间，格式 YYYY-MM-DD
            date_end: 结束时间，格式 YYYY-MM-DD
            date_type: 时间类型 (1=创建, 2=更新)
            sids: 店铺ID列表
            status_list: STA任务状态列表
                (ACTIVE, VOIDED, SHIPPED, ERRORED)
            **kwargs: 其他参数
                - planName: STA任务名称(模糊搜索)
                - shipmentIdList: 货件ID或货件单号列表(精确搜索)
                - sortField: 排序字段
                - sortType: 排序类型

        Returns:
            ResponseResult: 包含分页数据

        Example:
            >>> result = await fba.get_sta_task_list(
            ...     access_token="xxx",
            ...     page=1,
            ...     length=10,
            ...     date_begin="2026-02-01",
            ...     date_end="2026-02-24",
            ...     date_type=1
            ... )
        """
        logger.debug("Fetching STA task list: page=%s, length=%s", page, length)

        req_body = {
            "page": page,
            "length": length,
            "dateBegin": date_begin,
            "dateEnd": date_end,
            "dateType": date_type,
            **kwargs
        }

        if sids:
            req_body["sids"] = sids
        if status_list:
            req_body["statusList"] = status_list

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-plan/page",
            req_body=req_body
        )

    async def get_sta_shipment_detail_list(
        self,
        access_token: str,
        inbound_plan_id: str,
        shipment_ids: list[str],
        sid: int
    ) -> ResponseResult:
        """
        查询STA任务货件详情列表

        API: POST /amzStaServer/openapi/inbound-shipment/shipmentDetailList

        Args:
            access_token: 访问令牌
            inbound_plan_id: STA任务编号
            shipment_ids: 货件ID列表
            sid: 店铺ID

        Returns:
            ResponseResult: 包含货件详情列表

        Example:
            >>> result = await fba.get_sta_shipment_detail_list(
            ...     access_token="xxx",
            ...     inbound_plan_id="wf0a914e89-xxx",
            ...     shipment_ids=["shd10e38ca-xxx"],
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching STA shipment detail list: inbound_plan_id=%s", inbound_plan_id)

        req_body = {
            "inboundPlanId": inbound_plan_id,
            "shipmentIds": shipment_ids,
            "sid": sid
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-shipment/shipmentDetailList",
            req_body=req_body
        )

    async def generate_placement_options(
        self,
        access_token: str,
        inbound_plan_id: str,
        sid: int
    ) -> ResponseResult:
        """
        生成货件方案

        API: POST /amzStaServer/openapi/inbound-shipment/generatePlacementOptions

        Args:
            access_token: 访问令牌
            inbound_plan_id: STA任务编号
            sid: 店铺ID

        Returns:
            ResponseResult: 包含 {inboundPlanId, taskId, taskStatus}

        Example:
            >>> result = await fba.generate_placement_options(
            ...     access_token="xxx",
            ...     inbound_plan_id="wf0a914e89-xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Generating placement options: inbound_plan_id=%s", inbound_plan_id)

        req_body = {
            "inboundPlanId": inbound_plan_id,
            "sid": sid
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-shipment/generatePlacementOptions",
            req_body=req_body
        )

    async def get_shipment_boxes(
        self,
        access_token: str,
        inbound_plan_id: str,
        shipment_id_list: list[str],
        sid: int
    ) -> ResponseResult:
        """
        查询货件装箱信息

        API: POST /amzStaServer/openapi/inbound-shipment/listShipmentBoxes

        Args:
            access_token: 访问令牌
            inbound_plan_id: STA任务编号
            shipment_id_list: 货件ID列表
            sid: 店铺ID

        Returns:
            ResponseResult: 包含装箱明细

        Example:
            >>> result = await fba.get_shipment_boxes(
            ...     access_token="xxx",
            ...     inbound_plan_id="wf0a914e89-xxx",
            ...     shipment_id_list=["shd10e38ca-xxx"],
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching shipment boxes: inbound_plan_id=%s", inbound_plan_id)

        req_body = {
            "inboundPlanId": inbound_plan_id,
            "shipmentIdList": shipment_id_list,
            "sid": sid
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-shipment/listShipmentBoxes",
            req_body=req_body
        )

    async def get_transport_list(
        self,
        access_token: str,
        inbound_plan_id: str,
        shipment_id: str,
        sid: int
    ) -> ResponseResult:
        """
        查询承运方式列表

        API: POST /amzStaServer/openapi/inbound-shipment/getTransportList

        Args:
            access_token: 访问令牌
            inbound_plan_id: STA任务编号
            shipment_id: 货件ID
            sid: 店铺ID

        Returns:
            ResponseResult: 包含承运方式列表

        Example:
            >>> result = await fba.get_transport_list(
            ...     access_token="xxx",
            ...     inbound_plan_id="wf0a914e89-xxx",
            ...     shipment_id="shd10e38ca-xxx",
            ...     sid=4661
            ... )
        """
        logger.debug("Fetching transport list: shipment_id=%s", shipment_id)

        req_body = {
            "inboundPlanId": inbound_plan_id,
            "shipmentId": shipment_id,
            "sid": sid
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-shipment/getTransportList",
            req_body=req_body
        )

    async def update_shipment_track(
        self,
        access_token: str,
        sid: int,
        **kwargs
    ) -> ResponseResult:
        """
        上传货件跟踪号

        API: POST /amzStaServer/openapi/inbound-shipment/updateShipmentTrack

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            **kwargs: 其他参数
                - inboundPlanId: STA任务编号
                - shipmentId: 货件ID
                - shipmentConfirmationId: 货件单号
                - billOfLadingNumber: 提货单号(LTL建议填写)
                - freightBillNumber: LTL跟踪编号(LTL必填)
                - trackBOList: 跟踪编号列表(SPD必填)
                    - boxId: 箱子ID
                    - localBoxId: 本地箱子ID
                    - trackingId: 跟踪ID

        Returns:
            ResponseResult: 包含 {taskId, taskStatus}

        Example:
            >>> result = await fba.update_shipment_track(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     inbound_plan_id="wf0a914e89-xxx",
            ...     shipment_id="shd10e38ca-xxx",
            ...     track_bo_list=[{"boxId": "1", "trackingId": "TRACK123"}]
            ... )
        """
        logger.debug("Updating shipment track: sid=%s", sid)

        req_body = {
            "sid": sid,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/inbound-shipment/updateShipmentTrack",
            req_body=req_body
        )

    # ==================== AWD入库任务API ====================

    async def create_awd_inbound_task(
        self,
        access_token: str,
        sid: int,
        awd_shipping_address: dict[str, Any],
        awd_delivered_goods: list[dict[str, Any]],
        destination_region: str | None = None
    ) -> ResponseResult:
        """
        创建AWD入库任务

        API: POST /amzStaServer/openapi/awd/inbound-plan/createInboundPlan

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            awd_shipping_address: 发货地址
                - addressLine1: 详细街道地址1 (必填)
                - city: 城市 (必填)
                - countryCode: 国家(地区)编码 (必填)
                - phoneNumber: 电话号码 (必填)
                - postalCode: 邮政编码 (必填)
                - shipperName: 发货方名称 (必填)
                - stateOrProvinceCode: 州/省/地区编码 (必填)
                - addressLine2: 详细街道地址2
                - zone: 区
            awd_delivered_goods: 发货商品列表
                - msku: MSKU (必填)
                - length: 箱子长 (必填)
                - width: 箱子宽 (必填)
                - height: 箱子高 (必填)
                - weight: 箱子重量 (必填)
                - boxQuantity: 箱数 (必填)
                - quantityInBox: 单箱数量 (必填)
                - lengthUnit: 长度单位 (INCHES/CENTIMETERS)
                - weightUnit: 重量单位 (POUNDS/KILOGRAMS)
                - labelOwner: 标签类型 (AMAZON/SELF)
                - prepOwner: 预处理提供方 (AMAZON/SELF)
                - prepCategory: 预处理类别
                - expiration: 有效期
            destination_region: 地区偏好
                (us-east, us-west, us-southcentral, us-southeast, null=亚马逊分配)

        Returns:
            ResponseResult: 包含 {orderId: AWD任务编号}

        Example:
            >>> result = await fba.create_awd_inbound_task(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     awd_shipping_address={
            ...         "addressLine1": "123 Main St",
            ...         "city": "Seattle",
            ...         "countryCode": "US",
            ...         "phoneNumber": "1234567890",
            ...         "postalCode": "98101",
            ...         "shipperName": "ABC Company",
            ...         "stateOrProvinceCode": "WA"
            ...     },
            ...     awd_delivered_goods=[
            ...         {
            ...             "msku": "SKU001",
            ...             "length": 20.5,
            ...             "width": 15.25,
            ...             "height": 12.34,
            ...             "weight": 15.75,
            ...             "boxQuantity": "5",
            ...             "quantityInBox": "10"
            ...         }
            ...     ]
            ... )
        """
        logger.debug("Creating AWD inbound task: sid=%s", sid)

        req_body = {
            "sid": sid,
            "awdShippingAddressBO": awd_shipping_address,
            "awdDeliveredGoodsBOS": awd_delivered_goods
        }

        if destination_region:
            req_body["destinationRegion"] = destination_region

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/awd/inbound-plan/createInboundPlan",
            req_body=req_body
        )

    async def get_awd_inbound_task_list(
        self,
        access_token: str,
        page: int,
        length: int,
        start_date_time: str,
        end_date_time: str,
        date_type: int = 1,
        sid_list: list[int] | None = None,
        status_list: list[str] | None = None,
        **kwargs
    ) -> ResponseResult:
        """
        查询AWD入库任务列表

        API: POST /amzStaServer/openapi/awd/inbound-plan/page

        Args:
            access_token: 访问令牌
            page: 分页页码
            length: 分页大小
            start_date_time: 开始时间，格式 YYYY-MM-DD
            end_date_time: 结束时间，格式 YYYY-MM-DD
            date_type: 时间类型 (1=创建, 2=更新)
            sid_list: 店铺ID列表
            status_list: 任务状态列表
                (LOCALDRAFT=草稿, DRAFT=待确认, VALIDATING=更新中,
                 CONFIRMED=已确认, CLOSED=已关闭, EXPIRED=已过期, CANCELLED=已取消)
            **kwargs: 其他参数
                - orderId: AWD入库任务编号
                - shipmentId: AWD货件单号
                - sortField: 排序字段
                - sortType: 排序类型

        Returns:
            ResponseResult: 包含分页数据

        Example:
            >>> result = await fba.get_awd_inbound_task_list(
            ...     access_token="xxx",
            ...     page=1,
            ...     length=10,
            ...     start_date_time="2026-02-01",
            ...     end_date_time="2026-02-24",
            ...     date_type=1
            ... )
        """
        logger.debug("Fetching AWD inbound task list: page=%s, length=%s", page, length)

        req_body = {
            "page": page,
            "length": length,
            "startDateTime": start_date_time,
            "endDateTime": end_date_time,
            "dateType": date_type,
            **kwargs
        }

        if sid_list:
            req_body["sidList"] = sid_list
        if status_list:
            req_body["statusList"] = status_list

        return await self._request_with_token(
            access_token=access_token,
            route="/amzStaServer/openapi/awd/inbound-plan/page",
            req_body=req_body
        )

    # ==================== 发货单API ====================

    async def get_shipment_order_list(
        self,
        access_token: str,
        offset: int,
        length: int,
        **kwargs
    ) -> ResponseResult:
        """
        查询发货单列表

        API: POST /erp/sc/routing/storage/shipment/getInboundShipmentList

        Args:
            access_token: 访问令牌
            offset: 偏移量
            length: 长度
            **kwargs: 其他查询参数
                - search_value: 搜索的值
                - search_field: 搜索字段 (sku/shipment_sn)
                - sids: 店铺ID，多个以英文逗号分隔
                - mids: 国家ID，多个以英文逗号分隔
                - wid: 仓库ID
                - logistics_type: 物流方式ID列表
                - status: 发货单状态
                    (-1=待配货, 0=待发货, 1=已发货, 3=已作废, 4=已删除)
                - print_status: 打印状态 (0=未打印, 1=已打印)
                - pick_status: 拣货状态 (0=未拣货, 1=已拣货)
                - time_type: 时间类型
                    (0=发货时间, 1=到货时间, 2=创建时间, 3=创建时间精确, 4=更新时间精确)
                - start_date: 开始日期
                - end_date: 结束日期
                - is_delete: 是否删除 (0=未删除, 1=已删除, 2=全部)

        Returns:
            ResponseResult: 包含 {list: [...], total: int}

        Example:
            >>> result = await fba.get_shipment_order_list(
            ...     access_token="xxx",
            ...     offset=0,
            ...     length=20,
            ...     sids="4661",
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching shipment order list: offset=%s, length=%s", offset, length)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/getInboundShipmentList",
            req_body=req_body
        )

    async def get_shipment_order_detail(
        self,
        access_token: str,
        shipment_sn: str
    ) -> ResponseResult:
        """
        查询发货单详情

        API: POST /erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail

        Args:
            access_token: 访问令牌
            shipment_sn: 发货单号

        Returns:
            ResponseResult: 包含发货单详情

        Example:
            >>> result = await fba.get_shipment_order_detail(
            ...     access_token="xxx",
            ...     shipment_sn="SP241016009"
            ... )
        """
        logger.debug("Fetching shipment order detail: shipment_sn=%s", shipment_sn)

        req_body = {
            "shipment_sn": shipment_sn
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail",
            req_body=req_body
        )

    async def create_ready_send_order(
        self,
        access_token: str,
        list_items: list[dict[str, Any]],
        **kwargs
    ) -> ResponseResult:
        """
        生成待发货的发货单

        API: POST /erp/sc/routing/storage/shipment/createReadySendOrder

        Args:
            access_token: 访问令牌
            list_items: 发货商品列表
                - seller_id: 亚马逊店铺ID (必填)
                - marketplace_id: 亚马逊市场ID (必填)
                - shipment_id: 货件单号 (必填)
                - fulfillment_network_sku: 货件FNSKU (必填)
                - num: 发货数量 (必填)
                - sku: SKU (必填)
                - fnsku: 本地发货的FNSKU
                - box_num: 箱数
                - quantity_in_case: 单箱数量
                - warehouse_seller_id: 仓库店铺ID
            **kwargs: 其他参数
                - wid: 自定义仓库ID
                - sys_wid: 系统仓库ID
                - expected_arrival_date: 预计到达时间
                - etd_date: 开船时间
                - eta_date: 预计到港时间
                - delivery_date: 实际妥投时间
                - head_fee_type: 头程费分配方式 (0-5)
                - remark: 备注
                - box_type: 装箱类型 (SINGLE/MULTIPLE)
                - box_list: 装箱数据列表

        Returns:
            ResponseResult: 包含 {order_sn: 发货单号}

        Example:
            >>> result = await fba.create_ready_send_order(
            ...     access_token="xxx",
            ...     list_items=[{
            ...         "seller_id": "A1XXX",
            ...         "marketplace_id": "ATVPDKIKX0DER",
            ...         "shipment_id": "FBA15XXX",
            ...         "fulfillment_network_sku": "X00XXX",
            ...         "num": 100,
            ...         "sku": "SKU001"
            ...     }]
            ... )
        """
        logger.debug("Creating ready send order with %s items", len(list_items))

        req_body = {
            "list": list_items,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/createReadySendOrder",
            req_body=req_body
        )

    async def update_shipment_order(
        self,
        access_token: str,
        shipment_sn: str,
        **kwargs
    ) -> ResponseResult:
        """
        编辑发货单

        API: POST /erp/sc/routing/storage/shipment/updateInboundShipmentListMws

        Args:
            access_token: 访问令牌
            shipment_sn: 发货单号
            **kwargs: 其他参数
                - remark: 备注
                - items: 发货商品列表
                    - id: 商品明细ID
                    - num: 发货量
                - box_type: 装箱类型 (SINGLE/MULTIPLE)
                - box_list: 装箱数据
                    - box_num: 箱子数
                    - cg_box_length: 箱子长(CM)
                    - cg_box_width: 箱子宽(CM)
                    - cg_box_height: 箱子高(CM)
                    - cg_box_weight: 箱子重(KG)
                    - box_skus: 箱子内包含的SKU信息
                    - box_nos: 自定义箱号

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await fba.update_shipment_order(
            ...     access_token="xxx",
            ...     shipment_sn="SP241016009",
            ...     remark="更新备注"
            ... )
        """
        logger.debug("Updating shipment order: shipment_sn=%s", shipment_sn)

        req_body = {
            "shipment_sn": shipment_sn,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/updateInboundShipmentListMws",
            req_body=req_body
        )

    async def ship_order(
        self,
        access_token: str,
        shipment_sn: str
    ) -> ResponseResult:
        """
        发货单发货

        API: POST /erp/sc/routing/storage/shipment/shipOrder

        Args:
            access_token: 访问令牌
            shipment_sn: 发货单号

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await fba.ship_order(
            ...     access_token="xxx",
            ...     shipment_sn="SP241016009"
            ... )
        """
        logger.debug("Shipping order: shipment_sn=%s", shipment_sn)

        req_body = {
            "shipment_sn": shipment_sn
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/shipOrder",
            req_body=req_body
        )

    async def cancel_shipment_order(
        self,
        access_token: str,
        shipment_sn: str
    ) -> ResponseResult:
        """
        作废发货单

        API: POST /erp/sc/routing/storage/shipment/cancelOrder

        Args:
            access_token: 访问令牌
            shipment_sn: 发货单号

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await fba.cancel_shipment_order(
            ...     access_token="xxx",
            ...     shipment_sn="SP241016009"
            ... )
        """
        logger.debug("Cancelling shipment order: shipment_sn=%s", shipment_sn)

        req_body = {
            "shipment_sn": shipment_sn
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/cancelOrder",
            req_body=req_body
        )

    # ==================== 发货计划API ====================

    async def get_shipment_plan_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询FBA发货计划列表

        API: POST /erp/sc/data/fba_report/shipmentPlanLists

        Args:
            access_token: 访问令牌
            offset: 偏移量，默认0
            length: 长度，默认20
            **kwargs: 其他查询参数
                - sids: 店铺ID列表，逗号分隔
                - wid: 仓库ID
                - packing_type: 包装类型 (1=混装, 2=原装)
                - search_field_time: 时间字段 (gmt_create/estimated_delivery_time)
                - search_field: 搜索字段 (order_sn)
                - search_value: 搜索值
                - status: 状态
                - mids: 国家ID
                - start_date: 开始日期
                - end_date: 结束日期

        Returns:
            ResponseResult: 包含发货计划列表

        Example:
            >>> result = await fba.get_shipment_plan_list(
            ...     access_token="xxx",
            ...     offset=0,
            ...     length=20,
            ...     start_date="2026-02-01",
            ...     end_date="2026-02-24"
            ... )
        """
        logger.debug("Fetching shipment plan list: offset=%s, length=%s", offset, length)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/data/fba_report/shipmentPlanLists",
            req_body=req_body
        )

    async def create_shipment_plan(
        self,
        access_token: str,
        product_list: list[dict[str, Any]],
        remark: str | None = None
    ) -> ResponseResult:
        """
        创建FBA发货计划

        API: POST /erp/sc/routing/storage/shipment/createShipmentPlan

        Args:
            access_token: 访问令牌
            product_list: 商品信息列表
                - sid: 店铺ID (必填)
                - packing_type: 包装类型 (1=混装, 2=原装) (必填)
                - msku: MSKU (必填)
                - fnsku: FNSKU (必填)
                - shipment_plan_quantity: 计划发货量 (必填)
                - shipment_time: 发货时间
                - quantity_in_case: 单箱数量
                - box_num: 箱数
                - logistics_provider_id: 物流商ID
                - logistics_channel_id: 物流渠道ID
                - wid: 系统仓库ID
                - remark: 商品备注
                - purchase_plan_sn: 关联采购计划单号
            remark: 批次信息备注

        Returns:
            ResponseResult: 包含 {seq: 批次号, order_sn: 计划编号列表}

        Example:
            >>> result = await fba.create_shipment_plan(
            ...     access_token="xxx",
            ...     product_list=[{
            ...         "sid": 4661,
            ...         "packing_type": 1,
            ...         "msku": "SKU001",
            ...         "fnsku": "X00XXX",
            ...         "shipment_plan_quantity": 100
            ...     }]
            ... )
        """
        logger.debug("Creating shipment plan with %s products", len(product_list))

        req_body = {
            "product_list": product_list
        }

        if remark:
            req_body["remark"] = remark

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/storage/shipment/createShipmentPlan",
            req_body=req_body
        )

    # ==================== 地址簿API ====================

    async def get_ship_from_address_list(
        self,
        access_token: str,
        offset: int = 0,
        length: int = 20,
        **kwargs
    ) -> ResponseResult:
        """
        查询发货地址列表

        API: POST /erp/sc/routing/fba/shipment/shipFromAddressList

        Args:
            access_token: 访问令牌
            offset: 分页偏移量，默认0
            length: 分页长度，默认20
            **kwargs: 其他查询参数
                - sid: 店铺ID列表
                - search_field: 搜索字段 (alias_name/sender_name)
                - search_value: 搜索值

        Returns:
            ResponseResult: 包含地址簿列表

        Example:
            >>> result = await fba.get_ship_from_address_list(
            ...     access_token="xxx",
            ...     offset=0,
            ...     length=20
            ... )
        """
        logger.debug("Fetching ship from address list: offset=%s, length=%s", offset, length)

        req_body = {
            "offset": offset,
            "length": length,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fba/shipment/shipFromAddressList",
            req_body=req_body
        )

    async def create_ship_from_address(
        self,
        access_token: str,
        sid: int,
        country_code: str,
        sender_name: str,
        province: str,
        city: str,
        street_detail1: str,
        zip_code: str,
        **kwargs
    ) -> ResponseResult:
        """
        创建发货地址

        API: POST /erp/sc/routing/fba/shipment/saveShipFromAddress

        Args:
            access_token: 访问令牌
            sid: 店铺ID
            country_code: 国家编码
            sender_name: 发货方名称
            province: 省/州/地区
            city: 城市
            street_detail1: 街道地址1
            zip_code: 邮编
            **kwargs: 其他参数
                - alias_name: 地址别名
                - region: 区
                - street_detail2: 街道地址2
                - phone: 电话

        Returns:
            ResponseResult: 包含新创建的地址ID

        Example:
            >>> result = await fba.create_ship_from_address(
            ...     access_token="xxx",
            ...     sid=4661,
            ...     country_code="CN",
            ...     sender_name="ABC Company",
            ...     province="Guangdong",
            ...     city="Shenzhen",
            ...     street_detail1="123 Main St",
            ...     zip_code="518000"
            ... )
        """
        logger.debug("Creating ship from address: sid=%s", sid)

        req_body = {
            "sid": sid,
            "country_code": country_code,
            "sender_name": sender_name,
            "province": province,
            "city": city,
            "street_detail1": street_detail1,
            "zip_code": zip_code,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fba/shipment/saveShipFromAddress",
            req_body=req_body
        )

    async def update_ship_from_address(
        self,
        access_token: str,
        address_id: int,
        **kwargs
    ) -> ResponseResult:
        """
        修改发货地址

        API: POST /erp/sc/routing/fba/shipment/updateShipFromAddress

        Args:
            access_token: 访问令牌
            address_id: 发货地址ID
            **kwargs: 其他参数
                - alias_name: 地址别名
                - country_code: 国家编码
                - sender_name: 发货方名称
                - province: 省/州/地区
                - city: 城市
                - region: 区
                - street_detail1: 街道地址1
                - street_detail2: 街道地址2
                - zip_code: 邮编
                - phone: 电话

        Returns:
            ResponseResult: 操作结果

        Example:
            >>> result = await fba.update_ship_from_address(
            ...     access_token="xxx",
            ...     address_id=320,
            ...     sender_name="New Company Name"
            ... )
        """
        logger.debug("Updating ship from address: address_id=%s", address_id)

        req_body = {
            "id": address_id,
            **kwargs
        }

        return await self._request_with_token(
            access_token=access_token,
            route="/erp/sc/routing/fba/shipment/updateShipFromAddress",
            req_body=req_body
        )


__all__ = [
    'FBAEndpoints',
]

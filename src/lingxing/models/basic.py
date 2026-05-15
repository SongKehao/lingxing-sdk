"""Pydantic models for BasicData APIs."""
from typing import Optional

from .common import LingXingModel


class AccoutListsItem(LingXingModel):
    """Response item for AccoutLists."""

    create_time: Optional[str] = None
    email: Optional[str] = None
    is_master: Optional[int] = None
    last_login_ip: Optional[str] = None
    last_login_time: Optional[str] = None
    login_num: Optional[int] = None
    mobile: Optional[str] = None
    realname: Optional[str] = None
    role: Optional[str] = None
    seller: Optional[str] = None
    status: Optional[int] = None
    uid: Optional[int] = None
    username: Optional[str] = None
    zid: Optional[int] = None

class AllMarketplaceItem(LingXingModel):
    """Response item for AllMarketplace."""

    aws_region: Optional[str] = None
    code: Optional[str] = None
    country: Optional[str] = None
    marketplace_id: Optional[str] = None
    mid: Optional[int] = None
    region: Optional[str] = None

class ConceptSellerListsItem(LingXingModel):
    """Response item for ConceptSellerLists."""

    country: Optional[str] = None
    id: Optional[int] = None
    mid: Optional[int] = None
    name: Optional[str] = None
    region: Optional[str] = None
    seller_account_id: Optional[int] = None
    seller_account_name: Optional[str] = None
    seller_id: Optional[str] = None
    status: Optional[int] = None

class SellerListsItem(LingXingModel):
    """Response item for SellerLists."""

    account_name: Optional[str] = None
    country: Optional[str] = None
    has_ads_setting: Optional[int] = None
    marketplace_id: Optional[str] = None
    mid: Optional[int] = None
    name: Optional[str] = None
    region: Optional[str] = None
    seller_account_id: Optional[int] = None
    seller_id: Optional[str] = None
    sid: Optional[int] = None
    status: Optional[int] = None

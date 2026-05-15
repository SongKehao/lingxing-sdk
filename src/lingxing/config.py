"""领星ERP配置管理模块"""
from __future__ import annotations

import os

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
except ImportError:
    from pydantic import BaseSettings
    SettingsConfigDict = dict


class LingXingConfig(BaseSettings):
    """领星ERP配置类"""

    model_config = SettingsConfigDict(
        env_prefix="",  # 不使用前缀，直接使用完整环境变量名
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    # API配置 - 直接使用完整环境变量名
    host: str = os.getenv("LINGXING_HOST", "https://openapi.lingxing.com")
    app_id: str = os.getenv("LINGXING_APP_ID", "")
    app_secret: str = os.getenv("LINGXING_APP_SECRET", "")

    # 同步配置
    sync_batch_size: int = int(os.getenv("LINGXING_SYNC_BATCH_SIZE", "1000"))
    sync_full_sync_interval_hours: int = int(os.getenv("LINGXING_SYNC_FULL_SYNC_INTERVAL_HOURS", "168"))
    sync_max_retries: int = int(os.getenv("LINGXING_SYNC_MAX_RETRIES", "3"))
    sync_retry_delay_seconds: int = int(os.getenv("LINGXING_SYNC_RETRY_DELAY_SECONDS", "5"))
    sync_api_request_delay_seconds: float = float(os.getenv("LINGXING_SYNC_API_REQUEST_DELAY_SECONDS", "1.0"))

    # 客户端配置
    request_timeout: int = int(os.getenv("LINGXING_REQUEST_TIMEOUT", "30"))

    # Token管理
    token_refresh_threshold_seconds: int = int(os.getenv("LINGXING_TOKEN_REFRESH_THRESHOLD_SECONDS", "300"))

    def __init__(self, **data):
        """初始化配置，验证必填字段"""
        super().__init__(**data)
        # 验证必填字段
        if not self.app_id:
            msg = "app_id is required (set LINGXING_APP_ID env var)"
            raise ValueError(msg)
        if not self.app_secret:
            msg = "app_secret is required (set LINGXING_APP_SECRET env var)"
            raise ValueError(msg)

    def __str__(self) -> str:
        """脱敏显示配置信息"""
        return (
            f"LingXingConfig(host={self.host}, "
            f"app_id={self.app_id}, "
            f"app_secret=***REDACTED***)"
        )

    def __repr__(self) -> str:
        """脱敏显示配置信息"""
        return self.__str__()

    @classmethod
    def from_env(cls) -> "LingXingConfig":
        """
        从环境变量创建配置实例

        Returns:
            LingXingConfig: 配置实例
        """
        return cls()


# 全局配置实例
_config: LingXingConfig | None = None


def get_config() -> LingXingConfig:
    """
    获取全局配置实例（单例模式）

    Returns:
        LingXingConfig: 配置实例
    """
    global _config
    if _config is None:
        _config = LingXingConfig.from_env()
    return _config


def set_config(config: LingXingConfig) -> None:
    """
    设置全局配置实例（主要用于测试）

    Args:
        config: 配置实例
    """
    global _config
    _config = config


__all__ = [
    "LingXingConfig",
    "get_config",
    "set_config",
]

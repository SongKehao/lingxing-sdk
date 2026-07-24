import os

from lingxing.config import LingXingConfig


def get_lingxing_config() -> LingXingConfig:
    """从环境变量加载测试配置。保留原函数名以兼容迁移的测试文件。"""
    return LingXingConfig(
        host=os.getenv("LINGXING_HOST", "https://openapi.lingxing.com"),
        app_id=os.getenv("LINGXING_APP_ID", ""),
        app_secret=os.getenv("LINGXING_APP_SECRET", ""),
    )

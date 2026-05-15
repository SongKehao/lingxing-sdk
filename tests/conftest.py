import pytest
from lingxing.config import LingXingConfig


@pytest.fixture
def config():
    return LingXingConfig(
        host="https://openapi.lingxing.com",
        app_id="test_app_id",
        app_secret="test_app_secret",
    )

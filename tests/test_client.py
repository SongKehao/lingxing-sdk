from lingxing.client import LingXingClient
from lingxing.config import LingXingConfig


def test_client_creation():
    config = LingXingConfig(
        app_id="test_id",
        app_secret="test_secret",
    )
    client = LingXingClient(config)
    assert client.config.app_id == "test_id"

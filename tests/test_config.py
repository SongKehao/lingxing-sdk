from lingxing.config import LingXingConfig


def test_default_config():
    config = LingXingConfig(app_id="test", app_secret="test")
    assert config.host == "https://openapi.lingxing.com"


def test_config_with_params():
    config = LingXingConfig(
        host="https://custom.host.com",
        app_id="test_id",
        app_secret="test_secret",
    )
    assert config.host == "https://custom.host.com"
    assert config.app_id == "test_id"
    assert config.app_secret == "test_secret"


def test_config_env_prefix():
    assert LingXingConfig.model_config.get("env_prefix") == ""

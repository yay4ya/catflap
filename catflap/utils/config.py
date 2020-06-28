import os

from catflap.exceptions import ConfigurationError


def get_config_from_env(key: str, default_value: str = None) -> str:
    value = os.environ.get(key, default_value)

    if value is None:
        raise ConfigurationError(f"Environment variable ({key}) is required.")

    return value

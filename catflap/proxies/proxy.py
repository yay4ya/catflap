from __future__ import annotations
from typing import Dict, Type

from catflap.data import Message
from catflap.exceptions import ConfigurationError


class Proxy:
    _registry: Dict[str, Type[Proxy]] = {}

    @classmethod
    def register(cls, name: str):
        def decorator(subclass: Type[Proxy]):
            cls._registry[name] = subclass
            return subclass

        return decorator

    @classmethod
    def by_name(cls, name: str) -> Proxy:
        subclass = cls._registry.get(name)
        if subclass is None:
            raise ConfigurationError(f"Proxy {name} is not registered.")
        return subclass()

    def post(self, message: Message) -> None:
        raise NotImplementedError

    def post_system_message(self, text: str) -> None:
        raise NotImplementedError

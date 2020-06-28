from __future__ import annotations
import dataclasses
import datetime
from typing import List

import dateutil.parser
from pytchat.processors.default.renderer.base import BaseRenderer

from catflap.data.author import Author


@dataclasses.dataclass
class Message:
    type: str
    id: str
    message: str
    message_ex: List[str]
    timestamp: int
    datetime: datetime.datetime
    elapsed_time: str
    amount_value: float
    amount_string: str
    currency: str
    bg_color: int
    author: Author

    @classmethod
    def from_renderer(cls, renderer: BaseRenderer) -> Message:
        message = cls(
            type=renderer.type,
            id=renderer.id,
            message=renderer.message,
            message_ex=renderer.messageEx,
            timestamp=renderer.timestamp,
            datetime=dateutil.parser.parse(renderer.datetime),
            elapsed_time=renderer.elapsedTime,
            amount_value=renderer.amountValue,
            amount_string=renderer.amountString,
            currency=renderer.currency,
            bg_color=renderer.bgColor,
            author=Author.from_renderer(renderer.author),
        )
        return message

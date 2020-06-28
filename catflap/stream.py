from __future__ import annotations
from typing import Iterator, List

from pytchat import LiveChat
from pytchat.processors.default.renderer.base import BaseRenderer

from catflap.data import Message


class LiveChatStream:
    def __init__(self, video_id: str) -> None:
        self._livechat = LiveChat(video_id)

    def __enter__(self) -> LiveChatStream:
        return self

    def __exit__(self, *args) -> None:
        self.terminate()

    def terminate(self) -> None:
        self._livechat.terminate()

    def __call__(self) -> Iterator[Message]:
        while self._livechat.is_alive():
            for item in self.get():
                yield item

    def get(self) -> List[Message]:
        chatdata = self._livechat.get()
        chatlist = chatdata.items  # type: List[BaseRenderer]
        if chatlist:
            chatdata.tick()

        messages = [Message.from_renderer(x) for x in chatlist]
        return messages

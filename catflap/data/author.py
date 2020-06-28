from __future__ import annotations
import dataclasses

from pytchat.processors.default.renderer.base import Author as _Author


@dataclasses.dataclass
class Author:
    id: str
    url: str
    name: str
    image_url: str
    badge_url: str
    is_verified: bool
    is_chat_owner: bool
    is_chat_sponsor: bool
    is_chat_moderator: bool

    @classmethod
    def from_renderer(cls, renderer: _Author) -> Author:
        channel = cls(
            id=renderer.channelId,
            url=renderer.channelUrl,
            name=renderer.name,
            image_url=renderer.imageUrl,
            badge_url=renderer.badgeUrl,
            is_verified=renderer.isVerified,
            is_chat_owner=renderer.isChatOwner,
            is_chat_sponsor=renderer.isChatSponsor,
            is_chat_moderator=renderer.isChatModerator,
        )
        return channel

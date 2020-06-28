from __future__ import annotations
import dataclasses

from pytchat import VideoInfo


@dataclasses.dataclass
class Video:
    id: str
    title: str
    duration: int
    thumbnail: str
    moving_thumbnail: str
    channel_id: str
    channel_name: str
    author_image: str

    @classmethod
    def by_id(cls, video_id: str) -> Video:
        info = VideoInfo(video_id)
        video = Video(
            id=info.video_id,
            title=info.get_title(),
            duration=info.get_duration(),
            thumbnail=info.get_thumbnail(),
            moving_thumbnail=info.get_moving_thumbnail(),
            channel_id=info.get_channel_id(),
            channel_name=info.get_channel_name(),
            author_image=info.get_author_image(),
        )
        return video

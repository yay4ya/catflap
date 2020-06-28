from catflap.data import Video


def test_video_by_id():
    video_id = "hDnU_ivo9Lo"
    video = Video.by_id(video_id)

    assert video.id == video_id
    assert video.channel_id == "UCpnvhOIJ6BN-vPkYU9ls-Eg"

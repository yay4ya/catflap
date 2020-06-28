from catflap.stream import LiveChatStream


def test_live_chat_stream():
    video_id = "hDnU_ivo9Lo"
    with LiveChatStream(video_id) as stream:
        _chatlist = stream.get()

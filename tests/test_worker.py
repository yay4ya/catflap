from catflap.worker import Worker
from catflap.proxies import StdoutProxy


def test_worker():
    video_id = "YGRKqrEprEo"
    proxy = StdoutProxy()
    max_requests = 1

    worker = Worker(
        video_id=video_id,
        proxy=proxy,
        max_requests=max_requests,
    )

    worker()

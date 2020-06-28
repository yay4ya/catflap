from catflap.proxies import Proxy
from catflap.stream import LiveChatStream


class Worker:
    def __init__(
            self,
            video_id: str,
            proxy: Proxy,
            max_requests: int = None,
    ) -> None:
        self._video_id = video_id
        self._proxy = proxy
        self._max_requests = max_requests

    def __call__(self) -> None:
        num_requests = 0
        max_requests = self._max_requests or float("inf")

        with LiveChatStream(self._video_id) as stream:
            for message in stream():
                self._proxy.post(message)

                if num_requests >= max_requests:
                    break

                num_requests += 1

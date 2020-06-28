from catflap.data import Message
from catflap.proxies.proxy import Proxy


@Proxy.register("stdout")
class StdoutProxy(Proxy):
    def post(self, message: Message) -> None:
        output = f"{message.datetime} [{message.author.name}] - {message.message}"
        print(output)

    def post_system_message(self, text: str) -> None:
        output = f"[ SYSTEM MESSAGE ] {text}"
        print(output)

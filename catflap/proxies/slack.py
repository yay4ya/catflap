from slack import WebClient

from catflap.data import Message
from catflap.proxies.proxy import Proxy
from catflap.utils.config import get_config_from_env


@Proxy.register("slack")
class SlackProxy(Proxy):
    def __init__(self) -> None:
        self._client = WebClient(get_config_from_env("SLACK_BOT_TOKEN"))
        self._channel = get_config_from_env("SLACK_BOT_CHANNEL")

    def post(self, message: Message) -> None:
        channel = self._channel
        username = message.author.name
        icon_url = message.author.image_url
        text = message.message

        if message.author.is_chat_owner:
            text = f"<!channel> {text}"

        self._client.chat_postMessage(
            channel=channel,
            username=username,
            icon_url=icon_url,
            text=text,
        )

    def post_system_message(self, text: str) -> None:
        channel = self._channel
        username = "SYSTEM INFO"
        icon_emoji = ":robot_face:"

        self._client.chat_postMessage(
            channel=channel,
            username=username,
            icon_emoji=icon_emoji,
            text=text,
        )

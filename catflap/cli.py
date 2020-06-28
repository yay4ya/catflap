import argparse
import dataclasses
import json
import logging

from catflap import __version__
from catflap.data import Video
from catflap.proxies import Proxy
from catflap.utils.youtube import get_videoid_from_urllike
from catflap.worker import Worker

logger = logging.getLogger(__name__)


def create_parser(prog: str = None) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Real time YouTube Live Chat Proxy",
        prog=prog,
    )
    parser.add_argument("--version",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("video",
                        type=str,
                        help="specify target video ID or URL")
    parser.add_argument("--proxy",
                        type=str,
                        default="stdout",
                        help="choose proxy for live chat stream")
    parser.add_argument("--max-requests",
                        type=int,
                        default=None,
                        help="set limit of number of requests")
    return parser


def run_from_args(args: argparse.Namespace) -> None:
    params_str = json.dumps(vars(args))
    logger.info("parameters: %s", params_str)

    video_id = get_videoid_from_urllike(args.video)
    video = Video.by_id(video_id)
    video_str = json.dumps(dataclasses.asdict(video))
    logger.info("video: %s", video_str)

    proxy = Proxy.by_name(args.proxy)

    worker = Worker(
        video_id=video_id,
        proxy=proxy,
        max_requests=args.max_requests,
    )

    try:
        worker()
    except KeyboardInterrupt:
        proxy.post_system_message("Keyboard Interrupted")
    except Exception as err:
        proxy.post_system_message(str(err))
        raise


def main(prog: str = None) -> None:
    parser = create_parser(prog)
    args = parser.parse_args()
    run_from_args(args)

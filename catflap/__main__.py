#!/usr/bin/env python
import logging
import os

from catflap.cli import main

if os.environ.get("CATFLAP_DEBUG"):
    LEVEL = logging.DEBUG
else:
    level_name = os.environ.get("CATFLAP_LOG_LEVEL", "")
    LEVEL = logging._nameToLevel.get(level_name, logging.INFO)  # pylint: disable=protected-access

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=LEVEL,
)


def run():
    main(prog="catflap")


if __name__ == "__main__":
    run()

catflap
=======

[![Actions Status](https://github.com/yay4ya/catflap/workflows/build/badge.svg)](https://github.com/yay4ya/catflap/actions?query=workflow%3Abuild)
[![License](https://img.shields.io/github/license/yay4ya/catflap)](https://github.com/yay4ya/catflap/blob/master/LICENSE)

`catflap` is a command line tool to export messages from YouTube Live Chat to other services such as Slack.



### Installation

```
$ pip install git+https://github.com/yay4ya/catflap
```

### Usage

```
$ catflap --help
usage: catflap [-h] [--version] [--proxy PROXY] [--max-requests MAX_REQUESTS] video

Real time YouTube Live Chat Proxy

positional arguments:
  video                 specify target video ID or URL

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --proxy PROXY         choose proxy for live chat stream
  --max-requests MAX_REQUESTS
                        set limit of number of requests
```


### Example

```
$ export SLACK_BOT_TOKEN=xxxx-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX
$ export SLACK_BOT_CHANNEL="#your-channel"
$ catflap videoid --proxy slack
```

Run in Docker:

```
$ docker build -t catflap -f docker/Dockerfile
$ docker run -d  --restart=always \
    -e SLACK_BOT_TOKEN=xxxx-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX \
    -e SLACK_BOT_CHANNEL="#your-channel" \
    catflap:latest poetry run catflap videoid --proxy slack
```

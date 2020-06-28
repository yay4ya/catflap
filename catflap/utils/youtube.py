from urllib.parse import parse_qs, urlparse


def get_videoid_from_urllike(video_url: str) -> str:
    url = urlparse(video_url)

    if not url.query:
        return video_url

    queries = parse_qs(url.query)
    return queries["v"][0]

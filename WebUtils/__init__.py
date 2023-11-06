# just to make sure this doesnt mess up
import grequests
import requests
from urllib.parse import urlparse, urljoin, ParseResult

DEFAULT_HTTP_SCHEME = "http"
DEFAULT_WS_SCHEME = "ws"
BASE_URL = None

def setBaseURL(url: str):
    """
    Parses a http/https url and sets the HTTP scheme and BASE_URL for future use.
    """
    global BASE_URL, DEFAULT_HTTP_SCHEME, DEFAULT_WS_SCHEME
    parsed_url = urlparse(url)
    BASE_URL = parsed_url.netloc

    match parsed_url.scheme:
        case "http":
            DEFAULT_HTTP_SCHEME = "http"
            DEFAULT_WS_SCHEME = "ws"
        case "https":
            DEFAULT_HTTP_SCHEME = "https"
            DEFAULT_WS_SCHEME = "wss"
        case _:
            pass


def getHTTPURLFor(path: str):
    return urljoin(f"{DEFAULT_HTTP_SCHEME}://{BASE_URL}", path)

def getWSURLFor(path: str):
    return urljoin(f"{DEFAULT_WS_SCHEME}://{BASE_URL}", path)

__all__ = ["HTTPSync", "HTTPAsync", "HTTPEncodings", "JSCore", "HTTPHost"]
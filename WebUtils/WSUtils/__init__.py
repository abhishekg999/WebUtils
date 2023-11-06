import WebUtils
from websocket import create_connection
from functools import partial

class WebSocketContext:
    def __init__(self, proto, url):
        if url.startswith('/') and WebUtils.HTTP_BASE_URL:
            url = WebUtils.HTTP_BASE_URL + url

        print(proto, url)


WSContext = partial(WebSocketContext, "ws")
WSSContext = partial(WebSocketContext, "wss")
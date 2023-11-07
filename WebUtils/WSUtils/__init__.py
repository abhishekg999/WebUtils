import WebUtils
from websocket import WebSocket

class WebSocketContext:
    def __init__(self, url, **kwargs):
        if url.startswith('/') and WebUtils.BASE_URL:
            url = WebUtils.getWSURLFor(url)    
        self.url = url
        self.ws = WebSocket()
        self.ws_args = kwargs
    
    def __enter__(self):
        self.ws.connect(self.url, **self.ws_args)
        return self.ws
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ws.close()

WS = WebSocketContext

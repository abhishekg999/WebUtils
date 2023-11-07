import WebUtils
import socketio
import websocket
from urllib.parse import urlparse

class WebSocketContext:
    def __init__(self, url, **kwargs):
        if url.startswith('/') and WebUtils.BASE_URL:
            url = WebUtils.getWSURLFor(url)    
        self.url = url
        self.ws = websocket.WebSocket()
        self.ws_args = kwargs
    
    def __enter__(self):
        self.ws.connect(self.url, **self.ws_args)
        return self.ws
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ws.close()

WS = WebSocketContext

class SocketIOContext:
    def __init__(self,  url , **kwargs):
        if url.startswith('/') and WebUtils.BASE_URL:
            # namespace is the relative path
            # url will be the http base url 
            namespace = url
            url = WebUtils.getHTTPURLFor('')
        else:
            # expecting a url in form of ws(s)://, convert to http(s):// 
            # namespace will be the path
            _url = urlparse(url) 
            namespace = _url.path
            match _url.scheme:
                case 'ws':
                    url = _url._replace(scheme='http', params='', query='', fragment='').geturl()
                case 'wss':
                    url = _url._replace(scheme='https', params='', query='', fragment='').geturl()
                case _:
                    raise Exception()

        self.url = url
        self.ws_args = kwargs
        self.sio = socketio.SimpleClient()

    def __enter__(self):
        print(self.url)
        print(self.ws_args)
        self.sio.connect(self.url, **self.ws_args)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sio.disconnect()
    
    def getEventsSync(self):
        while True:
            event = self.sio.receive()
            yield event
    
    def emit(self, event, data):
        self.sio.emit(event, data)


SocketIO = SocketIOContext

__all__ = ['WS', 'SocketIO']
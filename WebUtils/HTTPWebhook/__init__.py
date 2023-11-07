from flask import Flask, request
from multiprocessing import Process, Queue
import flask.cli
import logging
from urllib.parse import urlparse
from time import sleep
import json
import base64

flask.cli.show_server_banner = lambda *args: None
logging.getLogger('werkzeug').disabled = True

from typing import Generator, TypedDict, Dict

class WebHook:
    def __init__(self, port, **options):
        self.port = port
        self.options = options
        self.url = f"http://127.0.0.1:{self.port}"
        self.requests = Queue()

        app = Flask(__name__)

        @app.route('/')
        @app.route('/<first>')
        @app.route('/<first>/<path:rest>')
        def hook(first=None, rest=None):
            request_data = {
                "method": request.method,
                "path": request.path,
                "body": request.get_data().decode('latin-1'),
                "headers": dict(request.headers),
                "ip": request.remote_addr, 
                "query_parameters": dict(request.args), 
                "cookies": dict(request.cookies), 
            }
            self.requests.put(request_data)
            return f"{first}/{rest}"

        def run_flask_app():
            app.run(host='127.0.0.1', port=self.port, debug=False, **self.options)

        self.process = Process(target=run_flask_app)
    
    def __enter__(self):
        self.process.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.process.terminate()
        self.process.join()
        self.process = None

    def getRequestsSync(self) -> Generator[dict, None, None]:
        while True:
            request_data = self.requests.get()
            yield request_data

class PublicHTTPWebHook(WebHook):
    def __init__(self, port, **options):
        super().__init__(port, **options)
        from WebUtils.HTTPTunnel import TCPTunnel
        self.tunnel = TCPTunnel(self.port)
      
    def __enter__(self):
        super().__enter__()
        self.listener = self.tunnel.__enter__()
        self.url = urlparse(self.listener.url())._replace(scheme='http').geturl()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self.tunnel.__exit__(exc_type, exc_val, exc_tb)
        
class RequestBinWebHook():
    def __init__(self, api_key):
        self.api_key = api_key
        from socketio import Client
        self.sio = Client()
        self.url = f"https://{self.api_key}.x.pipedream.net/"

        self.requests = []

        @self.sio.on('request')
        def request(data):
            data = json.loads(data)['step']['request']
            data['body'] = base64.b64decode(data['body']).decode('latin-1')
            self.requests.append(data)
    
    def __enter__(self):
        self.sio.connect(f'https://requestbin-api.pipedream.com/?api_key={self.api_key}', socketio_path="/api/v2/public/socket.io", transports=['websocket'], wait_timeout=20)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sio.disconnect()
        self.sio.wait()
    
    def getRequestsSync(self) -> Generator[dict, None, None]:
        while True:
            if self.requests:
                request_data = self.requests.pop(0)
                yield request_data
            else:
                sleep(0.1)
        


        

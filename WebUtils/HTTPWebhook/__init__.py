from flask import Flask, request
from multiprocessing import Process
import flask.cli
import logging

flask.cli.show_server_banner = lambda *args: None
logging.getLogger('werkzeug').disabled = True

class WebHook:
    def __init__(self, port, **options):
        self.port = port
        self.options = options
        self.url = f"http://127.0.0.1:{self.port}"
        self.app = Flask(__name__)

        @self.app.route('/')
        @self.app.route('/<first>')
        @self.app.route('/<first>/<path:rest>')
        def hook(first=None, rest=None):
            return request


        self.process = Process(target=lambda: self.app.run(host='127.0.0.1', port=self.port))
    
    def __enter__(self):
        self.process.start()
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.process.terminate()
        self.process.join()


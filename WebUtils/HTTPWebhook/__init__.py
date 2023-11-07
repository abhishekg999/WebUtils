from WebUtils import flask
from multiprocessing import Process
import flask.cli
import logging

Flask = flask.Flask
request = flask.request
flask_cli = flask.cli

flask.cli.show_server_banner = lambda *args: None
logging.getLogger('werkzeug').disabled = True

class WebHook:
    def __init__(self, port, **options):
        self.port = port
        self.options = options
        self.url = f"http://127.0.0.1:{self.port}"
        self.responses = []

        app = Flask(__name__)

        @app.route('/')
        @app.route('/<first>')
        @app.route('/<first>/<path:rest>')
        def hook(first=None, rest=None):
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
        

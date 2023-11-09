import ngrok
from functools import partial

class NgrokTunnel:
    def __init__(self, l_type, port=4444, **options):
        self.port = port
        self.l_type = l_type

        if options:
            self.options = options
        else:
            self.options = {
                "authtoken_from_env": True
            }
    
        self.listener = None
    
    def __enter__(self):
        if self.listener:
            raise Exception("Context manager should not be entered with an already created ngrok listener.")

        self.listener = ngrok.connect(self.port, self.l_type, **self.options)
        return self.listener

    def __exit__(self, exc_type, exc_val, exc_tb):
        ngrok.disconnect(self.listener.url())

TCPTunnel = partial(NgrokTunnel, "tcp")
HTTPTunnel = partial(NgrokTunnel, "http")

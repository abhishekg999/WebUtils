import sys
sys.path.append('../')

from WebUtils.Websocket import SocketIO
from time import sleep
from socketio import Client
from WebUtils.Webhook import RequestBinWebhook
from WebUtils.Webhook import PublicHTTPWebhook


with PublicHTTPWebhook() as host:
    print(host.url)
    for e in host.getRequestsSync():
        print(e)
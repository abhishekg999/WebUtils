import sys
sys.path.append('../')

from WebUtils.Websocket import SocketIO
from time import sleep
from socketio import Client
from WebUtils.Webhook import RequestBinWebhook
from WebUtils.Webhook import PublicHTTPWebhook


with RequestBinWebhook('') as host:
    print(host.url)
    for e in host.getRequestsSync():
        if e['path'] == '/asdf':
            break
    
    for e in host.getRequestsSync():
        if e['path'] == '/1234':
            break
import sys
sys.path.append('../')

from WebUtils.Websocket import SocketIO
from time import sleep
from socketio import Client
from WebUtils.HTTPWebhook import RequestBinWebHook

with RequestBinWebHook("enbit6i3l2ra4") as bin:
    print(bin.url)
    for e in bin.getRequestsSync():
        print(e)

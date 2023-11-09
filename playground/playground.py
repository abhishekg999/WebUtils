import sys
sys.path.append('../')

from WebUtils.Websocket import SocketIO
from time import sleep
from socketio import Client
from WebUtils.Webhook import RequestBinWebhook
from WebUtils.Webhook import PublicHTTPWebhook
from WebUtils.Websocket import WS

with WS("ws://echo.websocket.events/") as ws:
    while 1:
        for e in ws.get_events_sync():
            ws.send(input())
            print(e)
            if e == "endloop":
                break
            elif e == "done":
                exit()
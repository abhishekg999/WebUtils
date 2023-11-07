import sys
sys.path.append("../")

import WebUtils
from WebUtils.WSUtils import *

WebUtils.setBaseURL('http://chall.polygl0ts.ch:9010/')
with WS("/ws", ) as ws:
    print(ws.recv())
    print(ws.recv())

print("done")
import sys
sys.path.append('../')

from WebUtils.HTTPTunnel import TCPTunnel
from time import sleep

with TCPTunnel(4444) as t:
    print(t.url())
    sleep(20)
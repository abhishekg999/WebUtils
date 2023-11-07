import sys
sys.path.append('../')

from WebUtils.HTTPTunnel import TCPTunnel
from WebUtils.HTTPWebhook import WebHook
from time import sleep

with WebHook(4444) as WH:
    print(WH.url)
    sleep(30)

print('done')

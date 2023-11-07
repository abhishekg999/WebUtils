import sys
sys.path.append('../')


from WebUtils.HTTPWebhook import PublicHTTPWebHook
from time import sleep

with PublicHTTPWebHook(4444) as W:
    print(W.url)
    for request in W.handleRequest():
        print(request)

print('done')

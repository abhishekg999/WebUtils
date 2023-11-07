import sys
sys.path.append('../')


from WebUtils.HTTPWebhook import WebHook
from time import sleep


print(WebHook)
with WebHook(4444) as W:
    sleep(30)

print('done')

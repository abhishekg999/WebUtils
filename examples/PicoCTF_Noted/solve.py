import sys
sys.path.append('../')

import WebUtils
WebUtils.setBaseURL("http://saturn.picoctf.net:56528/")
from WebUtils.HTTPSync import *
from WebUtils.MiscUtils import *
from WebUtils.HTTPHost import http_host

url = http_host("""
        <body>
            <iframe src="http://saturn.picoctf.net:56528/">

        </body>                     
""")
print(url)

username = random_string(20)
password = random_string(20)
res = post('/register', data={
    "username": username,
    "password": password
})
cookies = res.cookies

res = get('/new', cookies=cookies)
print(res.text)
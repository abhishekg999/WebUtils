import sys
sys.path.append("../")

import WebUtils
from WebUtils.WSUtils import *

WebUtils.setBaseURL('http://asdf:asdf@chall.polygl0ts.ch:9009/#asdf')
print(WebUtils.getHTTPURLFor('/'))
WSContext('/')
WSSContext('/')
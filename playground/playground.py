import sys
sys.path.append('../')

import WebUtils
from WebUtils.Websocket import SocketIO

WebUtils.setBaseURL("https://chall.polygl0ts.ch:9011")
with SocketIO('/') as io:
    for event in io.getEventsSync():
        if event[1] == 'auth':
            io.emit('auth', '1048ff1a0c075060d3ede382ba685f28')

        else:
            print(event)


# sio = socketio.SimpleClient()

# # Connect to the Socket.IO server
# sio.connect('https://chall.polygl0ts.ch:9011/')

# print(sio.receive())
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     # Gracefully close the connection when done
#     sio.disconnect()

import socketio
import sys

sio = socketio.Client(ssl_verify=False)

try:
    sio.connect("http://192.168.31.200:3000")
except socketio.exceptions.ConnectionError:
    print("Socket Server unavailable or unreachable at {}"
          .format("localhost:3000"))
    sys.exit(0)
except Exception as ex:
    print(ex)
    sys.exit(0)

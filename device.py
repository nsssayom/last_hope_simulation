import socketio
import json
from threading import Timer

from classes.DeviceBase import DeviceBase
from classes.LocationService import LocationService
from classes.Sensor import Sensor
import time

device = DeviceBase("53e5c16f-d87b-4b87-9af9-f5bbdc79d818",
                    "IMEI0001",
                    "+8801717018376")

sio = socketio.Client(ssl_verify=False)
sio.connect("http://192.168.31.200:3000")


@sio.on('connect')
def on_io_connect():
    print("Socket Connection Established")
    main()


@sio.event()
def on_disaster_time(self, msg):
    msg_arr = json.loads(msg)
    device.disaster_time = msg_arr['data']


@sio.event()
def on_location_update_at(self, msg):
    msg_arr = json.loads(msg)
    device.location_update_at = msg_arr['data']


def init_disaster_mode():
    location = None

    if (LocationService.isGNSSActive):
        location = LocationService.getGNSSLocation()
    else:
        location = LocationService.getGSMLocation()

    payload = {"uuid": device.uuid,
               "long": location[0],
               "lat": location[1],
               "heart_rate": Sensor.getHeartRate()}
    sio.emit("location_update", payload)
    print(payload)


def main():
    while (True):
        init_disaster_mode()
        time.sleep(3)
        

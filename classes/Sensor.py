import random


class Sensor:
    @staticmethod
    def getHeartRate():
        return random.randint(60, 100)

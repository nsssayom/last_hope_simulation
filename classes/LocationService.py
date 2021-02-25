import random


class LocationService:
    base_lat = 23.81
    base_long = 90.42

    @staticmethod
    def isGNSSActive():
        return random.choice([True, False])

    @staticmethod
    def getGNSSLocation():
        for _ in range(15):
            dec_lat = random.random()/100
            dec_lon = random.random()/100
        return [
            LocationService.base_long + dec_lat,
            LocationService.base_lat + dec_lon]

    @staticmethod
    def getGSMLocation():
        return LocationService.getGPSLocation()

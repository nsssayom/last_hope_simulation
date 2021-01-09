import random


class LocationService:
    base_lat = 19.99
    base_long = 80.05

    @staticmethod
    def isGNSSActive():
        return random.choice([True, False])

    @staticmethod
    def getGNSSLocation():
        for _ in range(5):
            dec_lat = random.random()/100
            dec_lon = random.random()/100
        return [LocationService.base_lat + dec_lon,
                LocationService.base_long + dec_lat]

    @staticmethod
    def getGSMLocation():
        return LocationService.getGPSLocation()

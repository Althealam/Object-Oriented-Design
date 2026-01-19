# Level have lots of parkingspot
from ParkingSpot import ParkingSpot
class Level:
    def __init__(self, level_id: int, spots: list[ParkingSpot]):
        self.level_id = level_id
        self.spots = spots
# Level->ParkingSpot
from Vehicle import VehicleType, Vehicle
class ParkingSpot:
    def __init__(self, spot_id: str, allowed_vehicle_type: VehicleType):
        self.spot_id = spot_id
        self.allowed_vehicle_type = allowed_vehicle_type
        self.vehicle = None
    
    def can_fit_vehicle(self, vehicle: Vehicle)->bool:
        # each parking spot accommodates a specific vehicle type
        return vehicle.vehicle_type == self.allowed_vehicle_type

    def is_available(self)->bool:
        return self.vehicle is None


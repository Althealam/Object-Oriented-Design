from enum import Enum
from abc import ABC, abstractmethod

class VehicleType(Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"
    TRUCK = "truck"

class Vehicle(ABC):
    @abstractmethod
    def __init__(self, license_plate:str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)

class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)

class Truck(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)
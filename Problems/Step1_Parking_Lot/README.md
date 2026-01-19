## Parking Lot System
### Requirements
1. The parking lot should have multiple levels, each level with a certain number of parking spots.<br>
2. The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.<br>
3. Each parking spot should be able to accommodate a specific type of vehicle.<br>
4. The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.<br>
5. The system should track the availability of parking spots and provide real-time information to customers.<br>
6. The system should handle multiple entry and exit points and support concurrent access.<br>

### Analysis
#### Step1: Requirement Analysis
From 1, we can know that the structure of parking lot contains parkinglot, level, parking sports<br>
From 2, we can know that the types of vehicles contain cars, motorcycles, trucks<br>

#### Step2: Classes
1. Vehicles
* Vehicle (abstract class): vehicleType, licensePlate
* Car
* Motorcycle
* Truck
2. Parking Structure
* ParkingLot: levels[], partVehicle(), leaveVehicle()
* Parking Level: sport[], findAvailabelSpot(vehicleType)
* Parking Spot: spotType, isAvailable, assignedVehicle
3. Statement
* Ticket: vehicleId, spotId, entryTime
* EntryGate
* ExitGate
4. Relationships of classes
* ParkingLot->Level: Aggregation
* Level->ParkingSpot: Composition
* ParkingSpot->Vehicle: Association
* EntryGate->ParkingLot: Association
* Ticket->ParkingSpot: Association
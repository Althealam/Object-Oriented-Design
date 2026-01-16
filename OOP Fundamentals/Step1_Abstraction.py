# Goal: hide complexity and expose only what users need to do
# Key Takeaway:
# (1) user calls start()
# (2) user does not care how the engine works

class Car:
    def start(self):
        self.__open_fuel_valve()
        self.__ignite_engine()
        print("Car Started")
    
    def __open_fuel_value(self): # Encapsulation: internal detail
        pass

    def __ignite_engine(self): # Encapsulation
        pass

car = Car()
car.start

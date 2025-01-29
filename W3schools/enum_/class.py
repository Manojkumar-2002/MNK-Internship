from enum import Enum

class Vehicle(Enum):
    Car = 1
    Bike = 2
    Truck = 3
    
    def __str__(self):
        return f"This is a {self.name}"

for vehicle in Vehicle:
    print(vehicle)

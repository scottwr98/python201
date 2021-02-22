class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

my_bus = Vehicle(name = "bus",
              max_speed=  70,
              mileage = 10)

print(f"Vehicle Name: {my_bus.name} Speed: {my_bus.max_speed} Mileage: {my_bus.mileage}")

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Car(Vehicle):
    pass

my_bus = Bus(name = "bus",
              max_speed=  70,
              mileage = 10)


print(f"Color: {my_bus.color}: Vehicle Name: {my_bus.name} Speed: {my_bus.max_speed} Mileage: {my_bus.mileage}")
#!/usr/bin/env python3
""" Testing my understanding of classes and objects in Python.
Exercises were taken from
[PYnative](https://pynative.com/python-object-oriented-programming-oop-exercise/)
"""


# Que 1
class Vehicle:
    """Create Vehicle class with max_speed and mileage attr"""
    def __init__(self, max_speed, mileage):
        """initialize Vehicle"""
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(f"ModelX max speed: {modelX.max_speed}\nMileage: {modelX.mileage}")


# Que 2
class Vehicle:
    """ Create Vehicle class w/o any attrs """
    pass


# Que 3
class Vehicle:
    """Create vehicle class"""
    def __init__(self, name, max_speed, mileage):
        """initialize Vehicle class

        Args:
            name(str): name of vehicle model
            max_speed(int): top speed of vehicle model
            mileage(int): number of miles
        """
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    """Create child class of Vehicle"""
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

car = Bus("School Volvo", 180, 12)
print(f"Vehicle name: {car.name} Speed: {car.max_speed} Mileage: {car.mileage}")


# Que 4
class Vehicle:
    """create Vehicle"""
    def __init__(self, name, max_speed, mileage):
        """initialize Vehicle

        Args:
            name(str): vehicle name
            max_speed(int): top speed of vehicle
            mileage(int): number of miles in vehicle
        """
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

   def seating_capacity(self, capacity):
        """create seating capacity in vehicle

        Args:
            capacity(int): seating capacity in vehicle
        """
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    """child class of Vehicle"""
    def seating_capacity(self, capacity=50):  # override method
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())


# Que 5
class Vehicle:
    color = 'White'  # class variable
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
School_car = Car("Audi Q5", 240, 18)
print("Color:", Vehicle.color, "Vehicle name:", School_bus.name,
        "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
print("Color:", Vehicle.color, "Vehicle name:", School_car.name,
        "Speed:", School_car.max_speed, "Mileage:", School_car.mileage)

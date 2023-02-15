#!/usr/bin/python3
"""Working wih getters and setters"""


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

# don = Duck("Donald")
# print(don.get_name())
# don.set_name("Donna")
# print(don.get_name())
#####################################################################

class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self):
        self.diameter = diameter

c = Circle(7)
#c.diameter = 20
print(f"Radius is: {c.radius}")
print(f"Diameter is: {c.diameter}")

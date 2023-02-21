#!/bin/python3

class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print("inside getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("inside setter")
        self.__name = input_name

# fowl = Duck("Howard")
# print(fowl.name)
# fowl.name = "Donald"
# print(fowl.name)
# print(fowl.__name)  # invalid
# print(fowl._Duck__name)  # correct way to access hidden method
######################################################################

# METHOD TYPES
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
#        print("A has", cls.count, "little objects.")
        print("A has", A.count, "little objects")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

# static methods
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")

CoyoteWeapon.commercial()

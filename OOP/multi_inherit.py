#!/usr/bin/python3
"""Demonstrates multiple inheritance in Python OOP"""

class Animal:
    """describes an animal"""
    def says(self):
        """return a speech statement"""
        return 'I speak!'

class Horse(Animal):
    """one child class of Animal"""
    def says(self):
        """describes the sound a horse makes"""
        return 'Neigh!'

class Donkey(Animal):
    """another child class of Animal"""
    def says(self):
        """describes the sound a donkey makes"""
        return 'Hee-haw!'

class Mule(Donkey, Horse):
    """subclass of child classes Donkey and Horse"""
    pass

class Hinny(Horse, Donkey):
    """subclass of child classes Horse and Donkey"""
    pass

#print(Mule.mro())  # show order of attribute/object search
#print(Hinny.mro())

mule = Mule()
hinny = Hinny()
print(mule.says())
print(hinny.says())

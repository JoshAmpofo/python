#!/usr/bin/pythom3
"""
This module gives a sample code on how inheritance works
"""

class Car():
    """define Car"""
    def exclaim(self):
        print("I am a car!")

class Yugo(Car):
    """child of parent Car"""
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here")

# create objects
gimme_car = Car()
gimme_yugo = Yugo()
gimme_car.exclaim()
gimme_car.need_a_push()  # error because Parent has no such method
gimme_yugo.exclaim()  # will now inherit its own method (overwrite the parent)
gimme_yugo.need_a_push()

# __INIT__ METHOD
class Person():
    def __init__(self, name):
        self.name = name
        print(self.name)

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
        print(self.name)

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
        print(self.name)

person = Person("Fudd")
doctor = MDPerson("Fudd")
lawyer = JDPerson("Fudd")
print(person.name)
print(doctor.name)
print(lawyer.name)

# CALLING PARENT METHOD from CHILD
class Person():
    """create a Person"""
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    """ defines email and name details of Person"""
    def __init__(self, name, email):
        """initialize method

        Args:
            name (str): name of Person
            email: email of Person
        """
        super().__init__(name)  # calls parent init method
        self.email = email  # only attribute that belongs to EmailPerson

bob = EmailPerson("Bob Frapples", 'bob@frapples.com')
print(bob.name)
print(bob.email)

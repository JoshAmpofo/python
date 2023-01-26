# REFRESH
# class Cat():
    # """define an empty class"""
    # pass

# CREATE AN INSTANCE (OBJECT) OF THE CLASS
# a_cat = Cat()
# another_cat = Cat()

# ASSIGNING DATA TO OBJECTS BY ASSIGNING VALUES TO ATTRIBUTES
# a_cat.age = 3
# a_cat.name = 'Mr. Fuzzybuttons'
# a_cat.nemesis = another_cat
# a_cat.nemesis.name = "Mr. Bigglesworth"

# RETRIEVING DATA BY ACCESSING ATTRIBUTES VALUE
# print(a_cat.age)  # will print age
# print(a_cat.name)  # will print name
# print(a_cat.nemesis)  # will print pointer address
# print(a_cat.nemesis.name)

# INITIALIZING A CLASS
# class Cat():
#     """define the animal Cat"""
#     def __init__(self, name):
#         """initialize Cat
#         Args:
#             name (str): stores name of cat
#         """
        # self.name = name
        
# creating an object and passing a value to name parameter
# furball = Cat("Grumpy")
# print("Our latest addition:", furball.name)

# INHERITANCE
# class Car(): 
#     """define parent class"""
#     def exclaim(self):
#         print("I'm a Car!")

# class Yugo(Car):
#     """define an empty child class"""
#     pass
# check if one class is derived from another class
# print(issubclass(Yugo, Car))

# create object for each class
# give_me_a_car = Car()
# give_me_a_subcar = Yugo()
# give_me_a_car.exclaim()
# give_me_a_subcar.exclaim()

# OVERRIDING A METHOD
# class Car():
#     """define parent class"""
#     def exclaim(self):
#         print("I'm a Car!")

# class Yugo(Car):
#     """define a child class"""
#     def exclaim(self):
#         print("I'm a Yugo! Much like a Car, but more Yugo-ish")
        
# gimme_car = Car()
# gimme_car.exclaim()
# gimme_yugo = Yugo()
# gimme_yugo.exclaim()

# MODIFYING INIT BEHAVIOUR
# class Person():
#     """define a person"""
#     def __init__(self, name):
#         """initialize person
#         Args:
#             name (str): defines name of Person
#         """
#         self.name = name

# class MDPerson(Person):
#     """define medical doctor subclass"""
#     def __init__(self, name):
#         """initialize doctor
#         Args:
#             name (str): defines name of Medical doctor 
#         """
#         self.name = "Doctor " + name
        
# class JDPerson(Person):
#     """define lawyer subclass"""
#     def __init__(self, name):
#         """initialize lawyer
#         Args:
#             name (str): define the name of lawyer
#         """
#         self.name = name + ", Esquire"
        
# main_person = Person("Fudd")
# print(main_person.name)
# doctor_person = MDPerson("Fudd")
# print(doctor_person.name)
# lawyer_person = JDPerson("Fudd")
# print(lawyer_person.name)


# ADDING A METHOD TO SUBCLASS
class Car():
    """define a car"""
    def exclaim(self):
        """define method to print out statement"""
        print("I'm a Car!")
    
class Yugo(Car):
    """define a car type"""
    def exclaim(self):
        """method prints out a statement"""
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        """method prints a statement crying out for help"""
        print("A little help here?")
        
gimme_car = Car()
gimme_yugo = Yugo()
gimme_yugo.need_a_push()  # will print method statement
gimme_car.need_a_push()  # will print error since method doesn't exist here

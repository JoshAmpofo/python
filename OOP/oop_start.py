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
class Cat():
    """define the animal Cat"""
    def __init__(self, name):
        """initialize Cat
        Args:
            name (str): stores name of cat
        """
        self.name = name
        
# creating an object and passing a value to name parameter
furball = Cat("Grumpy")
print("Our latest addition:", furball.name)
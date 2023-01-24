# start
class Person:
    pass

p = Person()  # object/instance/variable of the class
print(p)

# METHODS (colloquially known as functions)
class Person:
    def say_hi(self):
        print("Hello, how are you?")
        
p = Person()
p.say_hi()  # calling the function
# alternatively
Person().say_hi()  # also calling the function

# the __init__method()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def say_hi(self):
        print("Hello, my name is", self.name, self.age)
        
p = Person('Josh')
p.say_hi()
Person("Josh").say_hi()

class User:
    id = 89
    name = "no name"
    __password = None
    
    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
            
u = User()
print(u.is_new)

class Square:
    """Create an empty class Square"""
    pass

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

class Square:
    """Create an empty class Square"""
    def __init__(self, size):
        """Args:
                size: private instance object useful for deterrming
                some computational attribute of Square such as Area computation
        """
        self.__size = size
          
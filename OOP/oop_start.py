# start
class Person:
    pass

# p = Person()  # object/instance/variable of the class
# print(p)

# METHODS (colloquially known as functions)
# class Person:
    # def say_hi(self):
        # print("Hello, how are you?")
        
# p = Person()
# p.say_hi()  # calling the function
# alternatively
# Person().say_hi()  # also calling the function

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
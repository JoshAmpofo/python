#!/usr/bin/python3

# decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keywords arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function

# applying the decorator mannually
def add_ints(a, b):  # actual function we want to run
    return a + b 

cool_add_ints = document_it(add_ints)
print(cool_add_ints(3, 5))

# applying decorators automatically (or pythonic way)
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

# using double decorators
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return new_function

@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

# reversing the order (only difference is the running function)
@square_it
@document_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))

# NAMESPACES AND SCOPES

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)
    
print('at the top level:', animal)  # the global variable
print_global()  # also the global variable

# trying to get and change the value of the global variable
def change_and_print_global():
    print('inside change_and_print_global:', animal)  #  error trying to access a global variable within a local function
    animal = 'wombat'
    print('after the change:', animal)
    
change_and_print_global()

# to use a global variable inside a function
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
    
print(animal)
change_and_print_global()
print(animal)

# ACCESSING CONTENTS OF NAMESPACES IN PROGRAMS
animal = 'squirrel'
def change_local():
    animal = 'raven'
    print('locals:', locals())
    
print(animal)
change_local()
print('globals:', globals())
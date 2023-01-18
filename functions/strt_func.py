#!/usr/bin/python3

# a function that does nothing
#def do_nothing():
#    pass

#do_nothing()

#def make_a_sound():  # has no parameters but prints a value
#   print('quack')

#make_a_sound()

# def agree():  # no parameter but returns a value
#    return True
#if agree():  # test value of function
#    print('Splendid!')
#else:
#    print('That was unexpected')

## Arguments and Parameters ###############
# def echo(anything):
#     return anything + ' ' + anything

# print(echo('Rumpelstiltskin'))

#
# def commentary(color):
#     if color == 'red':
#         return "It's a tomato"
#     elif color == 'green':
#         return "It's a  green pepper"
#     elif color == 'bee purple':
#         return "I don't know what it is, but only bees can see it"
#     else:
#         return "I've never heard of the color " + color + "."
    
# comment = commentary('blue')
# print(comment)

# NONE
# thing = None  # using None as a boolean operator
# if thing:
#     print("It's some thing")
# else:
#     print("It's no thing")
    
# distinguishing None from False using the 'is' operator
# thing = None
# if thing is None:
    # print("It's nothing")
# else:
    # print ("it's something")
    
# Test of None
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


# whatis(None)
# whatis(True)
# whatis(False)

# some real values
# whatis(0)
# whatis(0.0)
# whatis('')
# whatis("")
# whatis('''''')
# whatis(())
# whatis([])
# whatis({})
# whatis(set())
# whatis(0.00001)
# whatis([0])
# whatis([''])
# whatis(' ')

### TYPES OF ARGUMENTS TO FUNCTIONS ########

## POSITIONAL ARGUMENTS
# arguments are copied to their corresponding parameter in order

# def menu(wine, entree, dessert):
    # return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay', 'chicken', 'cake'))

# submitting wrong positional args
# print(menu('beef', 'bagel', 'bordeaux'))

## KEYWORD ARGUMENTS
# print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# using both positional and keyword arguments
# print(menu('frontenac', dessert='flan', entree='fish'))

# working with default values for parameters
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

# print(menu('chardonnay', 'chicken'))

# NB: supplying an argument to a parameter with a default value
# results in a replacement of the default value with the 
# specified value
print(menu('dunkelfelder', 'duck', 'dougnut'))
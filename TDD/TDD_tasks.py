# #0. Write a function that adds two integers
# # a and b must be integers or floats, otherwise raise a TypeError exception
# # with the message a must be an integer or b must be an integer
# # a and b must first be casted to integers if they are float
# # Returns an integer

def add_integer(a, b=98):
    """add two integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    a, b = int(a), int(b)
    return a + b
    
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
    
# # 1. Write a function that divides all elements of a matrix

def matrix_divided(matrix, div):
    """divide all elements of a matrix"""
    if (not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(isinstance(element, int) or isinstance(element, float)
                   for element in [item for row in matrix for item in row])):
            raise TypeError("matrix must be a matrix (lists of lists)"
                            "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
] 
print(matrix_divided(matrix, 3))
print(matrix)

# #2. Write a function that prints My name is <first name> <last name>

def say_my_name(first_name, last_name=""):
    """print first and last name from an input"""
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
    

# # 3. Write a function that prints a square with the character #

def print_square(size):
    """print a square using #"""
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")

# # USE type() instead of isinstance()

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")


# Text Indentation
def text_indentation(text):
    """
    print text with 2 lines after encountering 
    the characters ".,?:"
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    indent = False
    for char in text:
        if char in ['.', '?', ':']:
            print(char, end="\n\n")
            indent = True
        elif indent and char == " ":
            continue
        else:
            print(char, end="")
            indent = False

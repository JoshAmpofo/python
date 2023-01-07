# define functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# create dictionary to store operands
ops = {"add": "+",
        "sub": "-",
        "mul": "*",
        "div": "/"
        }

# Ask user for input
print("******* Welcome to the Awesome Calculator *******")
print("What operation do you want to perform: ")
print("Operators are: \n")
print("""addition: 1\nsubtraction: 2\nmultiplication: 3\ndivision: 4\n""")
print(input("Select option[choose number]: "))
#for i, (key, value) in enumerate(ops.items()):
 #   print(f"Index {i}: {key}, {value}")
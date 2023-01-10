# define functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# create list to store operands
ops = ['+', '-', '*', '/']

# Ask user for input
print("******* Welcome to the Awesome Calculator *******")
print("What operation do you want to perform: ")
print("Operators are: \n")
print("""addition: 1\nsubtraction: 2\nmultiplication: 3\ndivision: 4\n""")
user_input_option = (input("Select option[choose number]: "))

# Ask user to enter two numbers
a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

# Display chosen operation option
if user_input_option == "1":
    print(f"You have chosen {user_input_option}: add\n")
    print(f"Results: {a} {ops[0]} {b} = {add(a, b)}")
elif user_input_option == "2":
     print(f"You have chosen {user_input_option}: subtract\n")
     print(f"Results: {a} {ops[1]} {b} = {sub(a, b)}")
elif user_input_option == "3":
     print(f"You have chosen {user_input_option}: multiply\n")
     print(f"Results: {a} {ops[2]} {b} = {mul(a, b)}")     
elif user_input_option == "4":
     print(f"You have chosen {user_input_option}: divide\n")
     print(f"Results: {a} {ops[3]} {b} = {div(a, b)}")

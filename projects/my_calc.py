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

# Ask user to choose operand
print("******* Welcome to the Awesome Calculator *******\n")

while True: # repeat action
    print("What operation do you want to perform: ")
    print("""addition: 1\nsubtraction: 2\nmultiplication: 3\ndivision: 4\n""")
    user_input_option = (input("Select option [choose number or q to quit]: "))
    
    # exit clause
    if user_input_option == "q":
        exit()
    
    # store input, raise a ValueError exception if wrong input received
    try:
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Incorrect input. Enter a valid number")
        continue
    
    # run operations
    if user_input_option == "1":
        print(f"\nYou have chosen {user_input_option}: add\n")
        print(f"Result: {a} {ops[0]} {b} = {add(a, b)}\n")
    elif user_input_option == "2":
        print(f"\nYou have chosen {user_input_option}: subtract\n")
        print(f"Result: {a} {ops[1]} {b} = {sub(a, b)}\n")
    elif user_input_option == "3":
        print(f"\nYou have chosen {user_input_option}: multiply\n")
        print(f"Result: {a} {ops[2]} {b} = {mul(a, b)}\n")     
    try:
        if user_input_option == "4":
            print(f"\nYou have chosen {user_input_option}: divide\n")
            print(f"\nResult: {a} {ops[3]} {b} = {div(a, b)}\n")
    except ZeroDivisionError:
        print("Cannot divide by zero\n")
        continue

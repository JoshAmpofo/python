''' This is a basic calculator program written entirely in python. 
It can perform basic operations such as addition, subtraction, multiplication 
and division. 
It takes two integers from a user, performs a user-chosen operation, 
prints the result and ask the user to perform another operation if they
so choose. 
Author: Joshua Ampofo Yentumi. 
P.S. Will be improving functionality and overall performance as I keep learning
more about Python''' 


# define functions
def add(a, b):
    return a + b
        
def sub(a, b):
    return a - b
    
def mul(a, b):
    return a * b
    
def div(a, b):
    return a / b

def return_result(func, a, b):
   print(func(a, b))

# Ask user to choose operand
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
        print("\nIncorrect input. Enter a valid number")
        continue
    
    # run operations
    if user_input_option == "1":
        return_result(add, a, b)

    if user_input_option == "2":
        return_result(sub, a, b)

    if user_input_option == "3":
        return_result(mul, a, b)   

    try:
        if user_input_option == "4":
            return_result(div, a, b)
    except ZeroDivisionError:
        print("Cannot divide by zero\n")
        continue

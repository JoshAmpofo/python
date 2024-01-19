"""
Author: Joshua Ampofo Yentumi

Challenge Day 23: Simple Calculator

Description: Create a simple calculator. The calculator should be able to perform the following basic math operations:
             add, subtract, divide and multiply. The calculator should take input from users.
             The calculator should be able to handle ZeroDivisionError and ValueError.
"""


class Calculator:
    """
    Creates a simple calculator that performs basic addition, subtraction, multiplication and
    division functions.

    Methods:
        - add(x, y): returns the sum of x and y.
        - subtract(x, y): returns the difference between x and y.
        - multiply(x, y): returns the product of x and y.
        - divide(x, y): returns the result of dividing x by y. Handles ZeroDivisionError 
    """
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            raise ZeroDivisionError('Cannot divide by zero')


calc = Calculator()

while True:
    print('\nSimple Calculator')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Quit')
    
    choice = input("\nChoose an operation: ")
    
    if choice == '5':
        print('Ending program...')
        print('Goodbye!')
        break
    
    try:
        num_1 = float(input("\nEnter first number: "))
        num_2 = float(input('Enter second number: '))
    except ValueError:
        print('Error: Invalid value entered')
        continue
    
    if choice == '1':
        result = calc.add(num_1, num_2)
    elif choice == '2':
        result = calc.subtract(num_1, num_2)
    elif choice == '3':
        result = calc.multiply(num_1, num_2)
    elif choice == '4':
        result = calc.divide(num_1, num_2)
    else:
        print("Invalid choice. Please choose a valid Operation")
        continue
    
    print("\nResult: ", result)
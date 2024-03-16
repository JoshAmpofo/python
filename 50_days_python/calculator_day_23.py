#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Challenge Day 23: Simple Calculator

Description: Create a simple calculator. The calculator should be able to perform the ff basic math operations:
             - add
             - subtract
             - divide
             - multiply
             The calculator should take input from users. The calculator should be able to handle:
                - ZeroDivisionError
                - NameError
                - ValueError
"""
import operator


def calculator():
    """perform simple calculations"""
    try:
        num_1 = int(input("Enter a number: "))
        operation = input("Choose operation(+, -, *, /): ")
        num_2 = int(input("Choose another number: "))

        if operation not in ["+", "-", "*", "/"] or len(operation) > 1:
            print("Please enter a valid operation")
    except ValueError:
        print("Please enter a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero. try again")
    else:
        if operation == "+":
            return f"{num_1} + {num_2} = {operator.add(num_1, num_2)}"
        elif operation == "-":
            return f"{num_1} - {num_2} = {operator.sub(num_1, num_2)}"
        elif operation == "*":
            return f"{num_1} * {num_2} = {operator.mul(num_1, num_2)}"
        elif operation == "/":
            return f"{num_1} / {num_2} = {operator.truediv(num_1, num_2)}"
    return "Try again"


if __name__ == "__main__":
    print(calculator())

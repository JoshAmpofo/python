"""
Author: Joshua Ampofo Yentumi

Day 8 Extra Challenge: List of Prime Numbers

Description: A function that returns the list oof all prime numbers within the range
             of the given number argument
"""


def prime_numbers():
    """
    Find the prime numbers within the range of the given argument

    Args:
        number (int): number to find prime numbers in range
        
    Return:
        prime_list (list): range of prime numbers
    """
    prime_list = [] # create empty list
    number = int(input("Enter a number (integer): "))  # request for user input
    for num in range(2, number):  # loop through each number in the range from 2 to the given number
        for i in range(2, num): # loop through each number in the range from 2 to the current number
            # if current number can be divided by i, then it's not a prime number
            if (num % i) == 0:
                break  # skip inner loop to next number
        else:
            prime_list.append(num)  # if no divisor is found, number is prime, append to list
    return f"Prime numbers within range of {number}: {prime_list}"


print(prime_numbers())
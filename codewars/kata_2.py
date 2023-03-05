#!/usr/bin/env python3
"""Jaden Smith is known for capitalizing the first letter of every word when he writes on Twitter.
Your task is to convert strings to how they would be written by Jaden Smith.
Strings are actual quotes from Jaden Smith but not capitalized in the same way he originally typed them.
"""


def to_jaden_case(string):
    """convert string to Jaden Case"""
    new_string = string.split()  # split sentence into words
    for i in range(len(new_string)):
        new_string[i] = new_string[i].capitalize()  # capitalize 1st letter of each word
    return ' '.join(new_string) 

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

# Alternatively
def to_jaden_case(string):
    return " ".join(new_string.capitalize() for new_string in string.split())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

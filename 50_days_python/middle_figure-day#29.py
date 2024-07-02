"""
Author: Joshua Ampofo Yentumi

Challenge day 29: Middle Figure

Description: A function that has two string parameters "a" and "b". 
             The function joins the two strings and finds the middle element.
             If the combined string has a middle element, the function should return the element
             If otherwise, it should return "no middle figure".
             Whitespaces should be removed.
             Use "make love" as an argument for a and "not wars" as an argument for b.
"""


def middle_figure(a: str, b: str) -> str:
    """
    Takes two strings and returns the middle element if there is one.

    Arg(s):
        a (str): first string
        b (str): second string

    Returns:
        str: middle element if there is one, else "no middle figure"
    """
    # concat both strings and remove whitespacces
    combined_string = (a + b).replace(" ", "")
    # find length of combined_string
    length = len(combined_string)
    # if length is odd, return middle element
    if length % 2 != 0:
        middle_element = length // 2
        return combined_string[middle_element]
    # if length is even, return "no middle figure"
    else:
        return "no middle figure"


a = "make love"
b = "not wars"
result = middle_figure(a, b)
print(result)

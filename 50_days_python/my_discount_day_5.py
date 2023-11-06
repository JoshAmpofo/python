"""
Author: Joshua Ampofo Yentumi
    
Day 5 Challenge: Discount
    
Description: Write a function that takes no argument but asks the user
             to input the price and discount of the product.
             Calculate the price of the product after the discount and return it.
"""


def my_discount():
    """
    Calculates the price of a product after discount
    
    Returns:
        price of product after discount
    """ 
    price = float(input("Enter price of product ($): "))
    discount = float(input("Enter discount: "))
    price_after_discount = price - (price * discount / 100)
    return f"New price after {discount}% discount on ${price} is {price_after_discount}"


print(my_discount())
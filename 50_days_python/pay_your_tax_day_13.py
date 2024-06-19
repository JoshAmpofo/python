"""
Author: Joshua Ampofo Yentumi

Day 13 Challenge: Pay Your Tax

Description: A function that takes no parameters.
             It asks a user to input the price of an item and the VAT (as a percentage).
             The function then returns the price of the item plus VAT

             The program should handle VAlueError and negative inputs form the user.
             The program should run until valid numbers are entered.
"""


def your_vat() -> float:
    """
    Calculate the price with VAT inclusive on an item

    Returns:
        vat_price (float): new price of item, VAT inclusive
    """
    while True:
        try:
            item_price = float(input('Enter item price: '))
            vat_amnt = float(input('Enter VAT rate: '))
        
            if item_price < 0 or vat_amnt < 0:
                print("Invalid input. Please enter a positive number!")
                continue
        
            # calculate VAT price on item
            vat_item_price = (item_price * vat_amnt) / 100
    
            # calculate new price of item with vat
            vat_price = item_price + vat_item_price
    
            # return new amount
            return f"Price of item + VAT: {vat_price:.2f}"
        except ValueError:
            print("Invalid input. Please enter an integer or float!")


print(your_vat())
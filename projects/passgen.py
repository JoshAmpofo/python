# This program is a simple password generator
# The password consists of a combination of letters, numbers and special chars
# Generated randomly
# The user can specify the length of the password
# However if no length argument is given, default value is 12
# Author: Joshua Ampofo Yentumi @dev_ampofo

# import modules
import string
import random

# Ask user for length of password
user_inp = input("Enter desirable length of password: ")

# define passgen function
def passgen(user_inp=''):
    if user_inp == '':
        user_inp = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    psswrd = ''.join(random.choice(chars) for char in range(int(user_inp)))
    return f"Your password is: {psswrd}"


print(passgen(user_inp))

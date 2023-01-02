# Working with Sentence cases
setup = 'a duck goes into a bar...'
# remove . sequences from both ends
print(setup.strip('.'))

# capitalize the first word
print(setup.capitalize())

# capitalize all starting letters (sentence case)
print(setup.title())

# convert all to uppercase
print(setup.upper())

# convert all to lowercase
print(setup.lower())

# swap uppercase and lowercase (i.e. if string is lower, will be converted to upper and vice versa)
print(setup.swapcase())

# Aligning string layout
print(setup.center(30)) # center within 30 spaces

# left justify
print(setup.ljust(30))

# right justify
print(setup.rjust(30))
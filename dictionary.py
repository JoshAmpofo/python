# Create dictionary
# empty_dict = {}
# print(empty_dict)
# print(type(empty_dict))

# Create quotes
# bierce = {
#     "day": "A period of twenty-four hours, mostly misspent",
#     "positive": "Mistaken at the top of one's voice",
#     "misfortune": "The kind of fortune that never misses"
# }
# print(bierce)

# Create with dict()
# acme_customer = dict(first="Wile", middle="E", last="Coyote")
# print(acme_customer)

# Convert with dict()
# lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(lol))

# los = ['ab', 'cd', 'ef'] # two-character string
# print(dict(los))

# ADDING/CHANGING ITEMS BY [Key]
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael'
}
# print(pythons)
# # Adding/Updating a dict value by assignment
# pythons['Gilliam'] = 'Gerry'
# print(pythons)
# # Updating by assignment
# pythons['Gilliam'] = 'Terry'
# print(pythons)

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones'
}
# print(some_pythons)

# Get an item by [key] or with get()
print(some_pythons['John'])
print(some_pythons['Groucho'])
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

# some_pythons = {
#     'Graham': 'Chapman',
#     'John': 'Cleese',
#     'Eric': 'Idle',
#     'Terry': 'Gilliam',
#     'Michael': 'Palin',
#     'Terry': 'Jones'
# }
# print(some_pythons)

# Get an item by [key] or with get()
# print(some_pythons['John'])
# print(some_pythons['Groucho'])
# print(some_pythons.get('John'))
# print(some_pythons.get("Groucho", "Not a Python"))  # will print 'Not a Python' since key doesn't exist in dict
# print(some_pythons.get("Groucho")) # default error value of None will be printed if element doesn't exist in dict

# GET ALL KEYS FROM A DICTIONARY USING keys()
signal = {'green':'go', 'yellow':'go faster', 'red':'smile for the camera'}
# print(signal.keys())
# print(list(signals.keys()))

# All values
print(signal.values())
print(list(signal.values()))
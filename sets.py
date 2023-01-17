# Creating Sets
empty_set = set()
print(empty_set)

# convert with set()
print(set('letters'))

# CREATING SETS FROM LISTS
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# CREATING FROM A TUPLE
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# WORKING WITH DICTIONARIES
print(set({'name': 'Ampofo', 'age': 30, 'sex': 'male'}))

# FIND LENGTH OF A SET WITH len()
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

# ADD AN ITEM WITH add()
s = set((1, 2, 3))
print(s)
s.add(4)
print(s)

# DELETE AN ITEM WITH remove()
s.remove(3)
print(s)

# ITERATE WITH FOR AND IN
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

# TESTING FOR VALUE WITH in
drinks = {'martini': {'vodka', 'vermouth'},
'black russian': {'vodka', 'kahlua'}, 'white russian':
{'cream', 'kahlua', 'vodka'}, 'manhattan': {'rye', 'vermouth', 'bitters'},
'screwdriver': {'orange juice', 'vodka'}
}

# which drinks contain vodka
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

# want vodka but are lactose intolerant and vermouth tastes like kerosene
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream'in contents): 
        print(name)

#USING COMBINATIONS and OPERATORS
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:  # check for drinks with vermouth and orange juice
        print(name)
        
# want vodka but not vermouth and cream
for name, contents in drinks.items():
   if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
       print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']

# intersection
print(bruss & wruss)
print(bruss.intersection(wruss))
# union
print(bruss | wruss)
print(bruss.union(wruss))
# difference
print(bruss - wruss)
print(bruss.difference(wruss))
print(wruss - bruss)
print(wruss.difference(bruss))

# other complex types of set operations
a = {1, 2}
b = {2, 3}

# symmetric difference (mems in one set or the other but not both)
print(a ^ b)
print(a.symmetric_difference(b))

# subset (all mems in one set are also in the other)
print(a <= b)
print(a.issubset(b))

# a set is always its own subset 
print(a <= a)
print(a.issubset(a))

# proper subset (second set has all the mems of the 1st set)
print(a < b)

# superset (all second set mems are part of first set)
print(a >= b)
print(a.issuperset(b))

# Any set is a superset of itself
print(a >= a)
print(a.issuperset(a)) 

# Proper superset
print(a > b)
# a set cannot be a superset of itself
print(a > a)

# SET COMPREHENSION
set_comp = {num for num in range(1, 10) if num % 3 == 1}
print(set_comp)

# FROZENSET
print(frozenset([3, 2, 1]))
print(frozenset(set([2, 1, 3])))

# let's see if it is truly frozen
fs = frozenset([1, 3, 2])
fs.add(4)
print(fs)
fs.remove(2)
print(fs)

# MAKING BIGGER DATA STRUCTURES
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

# make tuple of lists
tuples_of_lists = marxes, pythons, stooges
print(tuples_of_lists)

# make list of lists
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

# make a dictionary of lists
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
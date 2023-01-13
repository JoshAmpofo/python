# Creating Sets
# empty_set = set()
# print(empty_set)

# convert with set()
# print(set('letters'))

# CREATING SETS FROM LISTS
# print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))

# CREATING FROM A TUPLE
# print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))

# WORKING WITH DICTIONARIES
# print(set({'name': 'Ampofo', 'age': 30, 'sex': 'male'}))

# FIND LENGTH OF A SET WITH len()
# reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
# print(len(reindeer))

# ADD AN ITEM WITH add()
# s = set((1, 2, 3))
# print(s)
# s.add(4)
# print(s)

# DELETE AN ITEM WITH remove()
# s.remove(3)
# print(s)

# ITERATE WITH FOR AND IN
# furniture = set(('sofa', 'ottoman', 'table'))
# for piece in furniture:
#     print(piece)

# TESTING FOR VALUE WITH in
# drinks = {'martini': {'vodka', 'vermouth'},
# 'black russian': {'vodka', 'kahlua'}, 'white russian':
# {'cream', 'kahlua', 'vodka'}, 'manhattan': {'rye', 'vermouth', 'bitters'},
# 'screwdriver': {'orange juice', 'vodka'}
# }

# which dricnks contain vodka
# for name, contents in drinks.items():
    # if 'vodka' in contents:
        # print(name)

# want vodka but are lactose intolerant and vermouth tastes like kerosene
# for name, contents in drinks.items():
#     if 'vodka' in contents and not ('vermouth' in contents or 'cream'in contents): 
#         print(name)

# JUMPING TO LAMBDA, MAP, FILTER AND REDUCE()
# lambda & map()
# a = [1, 2, 3]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]

# print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))

# filter
# fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# odd_numbers = list(filter(lambda x: x % 2, fibonacci))
# even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
# print(odd_numbers)
# print(even_numbers)

# extended version
# for number in fibonacci:
#     if number % 2 == 1:
#         print(number, end=" ")

# REDUCE
# import functools
# print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4]))

#finding the max number in a list using reduce
# from functools import reduce
# f = lambda a, b : a if (a > b) else b
# print(reduce(f, [47, 11, 42, 102, 13]))

# calculating the sum of numbers from 1 to 100
# print(reduce(lambda x, y: x+y, range(1, 101)))

# my_list = [1, 2, 3, 1, 4, 2, 5]
# result = 0
# new_list = set(my_list)
# for item in new_list:
#     result +=  item
# print(result)

# set_1 = { "Python", "C", "Javascript" }
# set_2 = { "Bash", "C", "Ruby", "Perl" }
# print(set_1 & set_2)

# a_dict = {"language": "C", "number": 13, "track": "Low_level"}
# count = 0
# for key in a_dict.keys():
#     count += 1
# print(count)

# a_dict = {"language": "C", "number": [3, 1, 2], "track": "Low_level"}
# for keys in sorted(a_dict.keys()):
#     print("{}: {}".format(keys, a_dict[keys]))

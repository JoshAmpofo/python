# Strating with tuples (you can pronounce them as too-pull or tub-pull - no one cares!)
# empty_tuple = ()
# print(empty_tuple)

# or
# one_marx = 'Groucho',
# print(one_marx)
# print(type(one_marx))

# or
# marx_tuple = "Groucho", "Chico", "Harpo"
# print(marx_tuple)
# print(type(marx_tuple))

# check the difference
# one_marx = "Groucho",
# print(type(one_marx))  # this returns a tuple
# print(type("Groucho",))  # this returns a string
# print(type(("Groucho",)))  # this returns a tuple

# Multiple assignments
# marx_tuple = ("Groucho", "Chico", "Harpo")
# a, b, c = marx_tuple
# print(f"{a}\n{b}\n{c}")  # each variable takes one element respectively

# Swapping values using tuples (does not require temp variables)
# first_name, last_name = "Joshua", "Ampofo"
# first_name, last_name = last_name, first_name  # swap
# print(first_name)
# print(last_name)

# Making tuples of other data types
# name_list = ["Shelly", "Colby", "Dodge"]
# print(tuple(name_list))  # convert list to tuple

# Combine tuples using "+"
# name = ("Groucho",) + ("Chico", "Harpo")
# print(name)

# Duplicate Items with "*"
# print(("yada",) * 3)

# Comparing Tuples
# a = (7, 2)
# b = (7, 2, 9)
# print(a == b)
# print(a <= b)
# print(a < b)

# Iterating with for and in
# words = ("This", "ends", "here", "and", "now")
# for word in words:
#     print(word)

# Modifying tuples (YOU JUST CAN'T!!!)
# t1 = ('Fee', 'Fie', 'Foe')
# t2 = ('Flop',)
# print(id(t1))  # old ID

# t1 += t2
# print(id(t1))  # new ID

############ LISTS ##########
# creating lists
# empty_lists = [ ]
# print(empty_lists)
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# print(weekdays)
# big_birds = ["enu", "ostrich", "cassowary"]
# print(big_birds)
# first_names = ["Graham", "John", "Terry", "Terry", "Michael"]
# print(first_names)
# leap_years = [200, 2004, 2008]
# print(leap_years)
# randomness = ["Punxsatawney", {"groundhog": "Phil"}, "Feb. 2"]
# print(randomness)

# another_empty_list = list()
# print(another_empty_list)

# converting other data types to list
# tuple_list = ('My', 'tuple', 'is', 'now', 'a', 'list',)
# print(list(tuple_list))

# converting strings to single chars list
# print(list("cat"))

# creating a list of strings with split()
# talk_like_a_pirate_day = '9/19/2019'
# print(talk_like_a_pirate_day.split('/'))

# splitting when delimiter is '//'
# splitme = 'a/b//c/d///e'
# print(splitme.split('//'))

# SLICING
# marxes = ['Groucho', 'Chico', 'Harpo']
# print(marxes[0:2])

# print(marxes[::2])
# print(marxes[::-2])  # start from the back and move two steps to the right
# print(marxes[::-1])  # start from the back and move 1 step to the left - this is reversal
# These slices do not modify the lis in place. To modify in place:
# marxes.reverse()  # function to use to reverse in place
# print(marxes)  # reversed list, changes value but returns None

# print(marxes[4:])
# print(marxes[-6:])

# LIST METHODS
# marxes.append('Zeppo')
# print(marxes)

# marxes.insert(2, 'Gummo')
# print(marxes)
# marxes.insert(10, "Zeppo")
# print(marxes)

# List can also be duplicated using *
# print(["word"] * 3)

# Combine lists using extend() or +
# marxes = ["Groucho", "Chico", "Harpo", "Zeppo"] 
# others = ["Gummo", "Karl"]
# marxes.extend(others)
# marxes += others  # Alternatively
# print(marxes)

# You can change the item in a list by using its offset
# marxes[2] = 'Wanda'
# print(marxes)

# Changing the values in a list using slicing
# numbers = [1, 2, 3, 4]
# numbers[1:3] = [8, 9]
# numbers[1:3] = [7, 8, 9]  # diff length can be inserted into a list
# numbers[1:3] = []
# numbers[1:3] = (98, 99, 100)
# numbers[1:3] = "wat?"
# print(numbers)

# Deleting list items wih del
# marxes = ["Groucho", "Chico", "Harpo", "Gummo", "Karl"]
# print(marxes[-1])
# del marxes[-1]
# print(marxes)

# rep_list = ["rep", "rep_2", "rep", "rep_3"]
# rep_list.remove("rep")
# print(rep_list)

# get and delete an item using pop()
# print(rep_list.pop(0))
# print(rep_list.pop())
# print(rep_list)

# Remove all items using clear()
# work_quotes = ["working hard?", "Quick question!", "Number one priorities!"]
# print(work_quotes)
# work_quotes.clear()
# print(work_quotes)

# Copy with copy(), list() or a Slice
# a = [1, 2, 3]
# b = a.copy()
# print(b)
# c = list(a)
# print(c)
# d = a[:]
# print(d)

# changing a does not affect any of the copies
# a[0] = 'integer lists are boring'
# print(a)

# DEEPCOPY()
# import copy
# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)  # keeps the value of the copy in place
# print(a)
# print(b)
# a[2][1] = 10
# print(a)  # change will only affect this 
# print(b)

# Index
# We can use an index to find the position of an element in a list
# simpsons = ["Lisa", "Bart", "Marge", "Homer", "Bart"]
# print(simpsons.index("Bart"))
# You can use in to test if an element exists in a list
# print("Lisa" in simpsons)
# print(simpsons.count("Bart"))
# print(type(', '.join(simpsons)))  # convert list to string

# Compare lists
# a = [7, 2]
# b = [7, 2, 9]
# print(a == b)
# print(a <= b)
# print(a < b)

# cheeses = ['brie', 'gjetost', 'havarti']
# for cheese in cheeses:
#     if cheese.startswith('x'):
#         print("I won't eat anything that starts with 'x'")
#         break
#     else:
#         print(cheese)
# else:
#     print("Didn't find anything that started with 'x'")

# ITERATING MULTIPLE SEQUENCES WITH ZIP()
# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    # print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# Using zip() to create a tuple
# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'

# days = list(zip(english, french))
# print(days)

# LIST COMPREHENSION

# WAYS TO BUILD A LIST
# number_list = []
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# number_list.append(4)
# number_list.append(5)
# print(number_list)

# OR
# number_list = []
# for number in range(1, 6):
#     number_list.append(number)
# print(number_list)

# OR
# number_list = list(range(1, 6))
# print(number_list)

# USING LIST COMPREHENSION: the more pythonic way
# number_list = [number for number in range(1, 6)]
# print(number_list)

# a_list = [number for number in range(1, 6) if number % 2 == 1]
# print(a_list)

# plain nested
# rows = range(1, 4)
# cols = range(1, 3)

# for row in rows:
#     for col in cols:
#         print(row, col)

# using list comprehension
# rows = range(1, 4)
# cols = range(1, 3)

# cells = [(row, col) for row in rows for col in cols]
# for cell in cells:
#     print(cell)

# LIST OF LISTS
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
# print(all_birds)
# print(all_birds[0])
print(all_birds[1][0])
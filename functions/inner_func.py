# INNER FUNCTIONS
# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)

# print(outer(4, 7))

# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % quote
#     return inner(saying)

# print(knights('Hurrah!'))

# CLOSURES
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2

# a = knights2('Duck')
# b = knights2('Hasenpfeffer')

# print(type(a))
# print(type(b))

# print(a)
# print(b)
# print(a())
# print(b())

# ANONYMOUS FUNCTION: LAMBDA
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
        
# stairs = ['thud', 'meow', 'thud', 'hiss']

# def enliven(word):
#     return word.capitalize() + '!'

# edit_story(stairs, enliven)

# using lambda to compress the above functions
# edit_story(stairs, lambda word: word.capitalize() + '!')

# GENERATORS
# print(sum(range(1, 101)))  # range() is the generator

# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step 
        
# ranger = my_range(1, 5)
# print(ranger)
# for num in ranger:  # looping is used to print items in a generator
    # print(num)
    
# for try_again in ranger:
    # print(try_again)
    
# GENERATOR COMPREHENSION
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
# print(genobj)
for pair in genobj:
    print(pair)
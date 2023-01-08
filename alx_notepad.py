# def print_list_integer(my_list=[]):
#     for integer in my_list:
#         print(integer)

# def element_at(my_list, idx):
#     if (idx < 0) or (idx > len(my_list) - 1):
#         return None
#     else:
#         return my_list[idx]

# def replace_in_list(my_list, idx, element):
#     if (idx < 0) or (idx > len(my_list) - 1):
#         return my_list 
#     else:
#         my_list[idx] = element 
#         return my_list 
# MY SOLUTION THAT WORKS but ALX won't accept it all
# def print_reversed_list_integer(my_list=[]):
#     for integer in my_list[::-1]:
#         print("{:d}".format(integer))

# ALTERNATIVE SOLUTION THAT ALX ACCEPTS
# def print_reversed_list_integer(my_list=[]):
#     if my_list:  # check if list is not empty, which was missing from my initial code
#         for integer in my_list[::-1]:
#             print("{:d}".format(integer))

# def new_in_list(my_list, idx, element):     
#     if (idx < 0) or (idx > len(my_list) - 1):
#         return my_list 
#     else:
#         new_list = my_list.copy()
#         new_list[idx] = element 
#         return new_list 

# def no_c(my_string):
#     new_string = ""
#     for char in my_string:
#         if char != 'c' and char != 'C':
#             new_string += char
#     return new_string

# def no_c(my_string):
#     new_string = [char for char in my_string if char != 'c' and char != 'C']
#     return "".join(new_string)
# LONG NO SPACES APPROACH
# def print_matrix_integer(matrix=[[]]):
#     if matrix:
#         for row in matrix:
#             for element in row:
#                 print("{:d}".format(element), end="")
#             print()
# SHORT SPACES PRESENT APPROACH
# def print_matrix_integer(matrix=[[]]):
#     for row in matrix:
#         row_str = " ".join(["{:d}".format(element) for element in row])
#         print("{}".format(row_str))

# def add_tuple(tuple_a=(), tuple_b=()):
#     # get the first elements of the tuples
#     a1 = tuple_a[0] if len(tuple_a) > 0 else 0
#     b1 = tuple_b[0] if len(tuple_b) > 0 else 0

#     # get the second elements of the tuples
#     a2 = tuple_a[1] if len(tuple_a) > 1 else 0
#     b2 = tuple_b[1] if len(tuple_b) > 1 else 0

#     # return the tuple with the sum of the elements
#     return (a1 + b1, a2 + b2)

def multiple_returns(sentence):
    return (len(sentence), sentence[0])

print(multiple_returns("At school, I learnt C!"))
# Test Run
# array_1 = [1, 2, 1]
# array_2 = [4, 4, 1]

# for i in range(len(array_1)):
#     a = sorted(array_1)
#     b = sorted(array_2)
# if (a[i])**2 == b[i]:
#     print("True")
# else:
#     print("False")
#    if (a[i])**2 == b[i]:
#        print("True")
#    else:
#        print("False")

########## ORIGINAL VERSION ###########
def same(array_1, array_2):
    arr_1 = sorted(array_1) # amke copies of arrays before sorting
    arr_2 = sorted(array_2)
    if len(arr_1) != len(arr_2): # length equality check
        return False
    for i in range(len(arr_1)): # iterating through array_1 elements
        if (arr_1[i])**2 != arr_2[i]: # array_2 element square equality check
            return False 
    return True # if square equality check passes

print(same([1,2,3], [4, 1, 9]))
print(same([1,2,1], [1,9]))
print(same([1,2,1], [4,4,1]))

######### ALTERNATIVE VERSION: USING SORT() #######################
def same(array_1, array_2):
    array_1.sort() # modify list element in place, no need for copies
    array_2.sort()
    if len(array_1) != len(array_2): # check if length of arrays are equal
        return False
    for i in range(len(array_1)): # iterate through length of array_1
        if (array_1[i])**2 != array_2[i]: # check if array_1 elements are not square of elements in array_2
            return False 
    return True # do this if they are

print(same([1,2,3], [4, 1, 9]))
print(same([1,2,1], [1,9]))
print(same([1,2,1], [4,4,1]))
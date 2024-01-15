"""
Project 8: Learn Data Structures and Algorithms by building a Merge Sort Algorithm
"""


def merge_sort(array):
    """
    Merge-Sort Algorithm

    Args:
        array (list): array of numbers to sort using merge-sort algorithm
        
    Return:
        list: sorted list
    """
    # create recursion termination function
    if len(array) <= 1:
        return
    
    # obtain two halves of array
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    
    # call sort function on both halves to sort each individually
    merge_sort(left_part)
    merge_sort(right_part)
    
    # define sorting conditions
    
    # set array indexes
    left_array_index = 0 
    right_array_index = 0 
    sorted_index = 0
    
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
    # sort left side     
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    # sort right side    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
        

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print(f'Unsorted array: {numbers}')
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))   
"""
Project 7: Tower of Hanoi Puzzle
"""

# set number of disks
NUMBER_OF_DISKS = 3

# set rods and their values
A = list(range(NUMBER_OF_DISKS, 0, -1)) # source rod
B = [] # auxiliary rod
C = [] # target rod


def move(n: int, source: list, auxiliary: list, target: list) -> list:
    """
    Move disks from source rod to target rod using auxiliary rod as a helper.

    Args:
        n (int): Number of disks.
        source (list): The rod containing all the disks.
        auxiliary (list): The helper rod.
        target (list): The target rod.

    Returns:
        list: The state of the rods after the move.
    """
    # set recursion termination condition
    if n <= 0:
        return
    
    # define disk movement conditions
    
    # move n - 1 disks from source to auxiliary recursively
    move(n - 1, source, target, auxiliary)
    
    # move nth disk from source to target
    target.append(source.pop())
    
    # display progress
    print(A, B, C, '\n')
    
    # move remaining disks on auxiliary to target
    move(n - 1, auxiliary, source, target)

# initiate function call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
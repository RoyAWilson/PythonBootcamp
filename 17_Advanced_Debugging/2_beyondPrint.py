''' Using the build in debugger in python

'''

import pdb


def add(L) -> int:
    '''
    Adds the items in  a list of integers
    Typing the name of the variables afte the breakpint will show the value of the variable
    n will move to the next line of code and can check the vars each time
    Conditional you will be able to see whether triggered or not
    pressing c continues to end of code or the next breakpoint in the code
    '''

    size: int = len(L)
    total: int = 0
    iterator: int = 0
    # Set up the debugger
    pdb.set_trace()

    while iterator < size:
        total = total + L[iterator]
        iterator += 1
    return total


my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(add(my_list_2))

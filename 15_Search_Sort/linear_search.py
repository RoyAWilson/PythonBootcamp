'''
Create a function to perform a linear search
'''


def linear_search(item, my_list) -> bool:
    return True if item in my_list else False


print(linear_search(1, [2, 4, 3, 1]))

# For some reason the tutor uses a while loop and tests each iteration.  Seems overly involved to me.
# not particularly efficient as big O of n
# Could take a lot of resources if used on a larger list.

''' Code a binary search funtion '''


def binary_search(item, my_list) -> bool:
    '''
    To return true of false result binary search
    args:
    item - the value to find passed to function by caller.
    my_list - list of values to search through passed to function from caller

    vars:
    found - boolean value to return
    first variable to hod present postion in list
    last - integer: place of the last memeber of the list.
    midpoint - floor division of length of string by 2


    '''
    found: bool = False
    first: int = 0
    last: int = len(my_list) - 1

    while first <= last and found == False:
        midpoint = (first + last) // 2
        # Floor division to avoid decimal fractions not useable as an index.
        if my_list[midpoint] == item:
            found = True
        elif my_list[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return found


test = [6, 5, 8, 2, 3, 45, 87, 24, 70]
test = sorted(test)

print(binary_search(87, test))

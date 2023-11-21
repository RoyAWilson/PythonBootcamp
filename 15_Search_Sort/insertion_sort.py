'''
To practive insertion sort
'''


def insertion_sort(mylist) -> list:
    '''
    Insertion sort function to return a sorted list from input
    Arge:
        mylist - a list of n members to sort.
    vars:
        n = length of list
        value - holds presnt value in list.
    iterators:
        i
        j
    '''
    n: int = len(mylist)
    for i in range(1, n):
        # current value of in list
        value = mylist[i]
        j = i
        while j > 0 and mylist[j - 1] > value:
            mylist[j] = mylist[j-1]
            j -= 1
        mylist[j] = value
    return mylist


test = [6, 5, 8, 2, 3, 45, 87, 24, 70]
print(insertion_sort(test))

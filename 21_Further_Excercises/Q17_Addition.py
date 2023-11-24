'''
Write a function to add two positive integers together without using the + operator.
(Note, this will require some research - start here https://en.wikipedia.org/wiki/Bitwise_operation)
'''


def add(n1: int, n2: int) -> int:
    while (n2 != 0):
        a = n1 & n2
        n1 = n1 ^ n2
        n2 = a << 1
    return n1


x = add(56, 10)
print(x)

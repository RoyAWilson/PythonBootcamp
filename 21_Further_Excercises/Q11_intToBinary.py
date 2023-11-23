'''
Write a function that will convert an integer into binary.
'''


def bnum(number: int) -> bin:

    bin_number = bin(number)
    return bin_number


x = bnum(0)
print(x)

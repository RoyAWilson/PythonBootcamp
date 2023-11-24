''''
Write a function that uses bitwise operations to determine whether a number is odd or even.
'''


def odd_even(num):

    if num & 1 == 1:
        return f'{num} is odd'
    else:
        return f'{num} is even'


x = odd_even(7)
y = odd_even(500)
print(x, y)

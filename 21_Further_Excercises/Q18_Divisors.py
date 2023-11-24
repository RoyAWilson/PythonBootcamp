'''
Write a function that will calculate the number of divisors of a positive integer and return
those divisors.
'''


def divisors(num: int) -> list:
    div_list: list = []

    for i in range(1, (num//2) + 1):
        if num % i == 0:
            div_list.append(i)
    return div_list


x = divisors(240)
print(x)

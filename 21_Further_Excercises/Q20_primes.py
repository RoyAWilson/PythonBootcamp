'''
Write a function which prints the prime numbers in a given range.
'''


def primes(num_1, num_2):
    primenos = []
    for nums in range(num_1, num_2):
        if nums > 1:
            for i in range(2, nums):
                if nums % i == 0:
                    break

            else:
                primenos.append(nums)
    return primenos


x = primes(3, 17)
print(x)

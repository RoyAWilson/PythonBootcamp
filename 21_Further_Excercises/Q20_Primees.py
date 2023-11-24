'''
Write a function which prints the prime numbers in a given range.
'''
def primes(num_1: int, num_2: int) -> list:
    num_list = []
    prime_list = []
    if num_1 > 1 and num_2 > num_1:
        for x in range(num_1, num_2):
            num_list.append(x)
        for i in range(0, len(num_list)):
            if j in range(1 to num_2):
                if num_list[i] % j == 0:
                    prime_list.append(num_list[i])
    return prime_list
x = primes(2, 5)
print(x)
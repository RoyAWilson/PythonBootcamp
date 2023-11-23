'''
Write a function to determine whether all numbers in a list are unique.
'''


def uniqueNos(numbers: list) -> bool:
    for items in numbers:
        # print(items)
        for members in range(0, len(numbers)-1):
            if items == numbers[members + 1]:
                return True
        return False


x = uniqueNos([1, 2, 2, 4, 5])
y = uniqueNos([1, 2, 3, 4, 5])
z = uniqueNos([1, 2, 3, 4, 1])
print(x, y, z)

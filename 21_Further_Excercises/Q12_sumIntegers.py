'''
Write a function that calculates the sum of all integers up to n. Use the iterative method
and the formula and compare the results. (sum of n integers given by S = (n(n+1))/2)
'''

# # Misread the question
# def sum_ints(s):
#     result: int = 0
#     s = str(s)
#     for i in range(0, len(s)+1):
#         result += int(i)
#     return result


# x = sum_ints(123456)
# print(x)

def sum_ints(s: int) -> int:
    result: int = 0
    for i in range(0, s+1):
        result = result + i
    return result


x = sum_ints(7)
print(x)

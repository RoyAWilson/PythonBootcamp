# Two Sum problem - write function to take a list of integers
# loop through the list and find if any 2 integers add up to 10
# and return the indices.  If no 2 numbers add up to 10
# then return 0
# Tutor has not made it clear if numbers should be consecutive or
# if you need to check non consecutive numbers too.

# First instatiate a list with some numbers:
# Using tutors explanatory example numbers here to start off with

# number = [2, 5, 3, 7, 4]
i = 0
# Work out how to do it before making a function

# for numbers in range(1, len(number)):
#     # might need to be number - 1
#     # Add 1 to both i and numbers as python is 0 indexing, makes it easier to read as a human
#     if number[numbers] + number[i] == 10:
#         print(f'Indices {i+1} and {numbers+1} = 10')
#     else:
#         i += 1
# print('-1')

# Now that it works form it as a function

# This works for numbers contiguous in the list, but not for non-contiguous.
# Will check the answer and update to work on non-contiguous if necessary


# def indices(number):
#     i = 0
#     # pass list to function rather than coding it in here
#     for numbers in range(1, len(number)):
#         if number[numbers] + number[i] == 10:
#             return (f'Indices {i + 1} and {numbers+1} = 10')
#         else:
#             i = i + 1
#     return -1


# print(indices([2, 5, 3, 7, 4]))

# Non contiguous is required.  Tutor thinks a dictionary would be a better way to do this
# So give it a go doing it his way:

def indices_2(number, target):
    num_dict = {}
    for i in range(len(number)):
        if target - number[i] in num_dict:
            return [num_dict[target - number[i]], i]
        num_dict[number[i]] = i
    return -1


my_nums = [8, 6, 11, 3]
print(indices_2(my_nums, 9))

# That's a pretty neat solution.

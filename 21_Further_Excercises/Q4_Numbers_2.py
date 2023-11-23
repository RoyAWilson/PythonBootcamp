'''
Question 4
Write a program that takes a list of non-negative integers and prints each integer
to the screen the same number of times as the value of the integer, each new value
on a new line. For example
[2,3,4,1] would print:
22
333
4444
1
'''

num_list: list = []
inp_nums: str = ''

inp_nums = input(
    'Please enter a list of positive integers separated by commas: > ')
while '-' in inp_nums:
    print('Please only enter positive integers!\n\n')
    inp_nums = input('Please enter your numbers: > ')
    break
num_list = inp_nums.split(',')
for items in range(0, len(num_list)):
    num_list[items] = int(num_list[items])
    print(str(num_list[items]) * num_list[items])

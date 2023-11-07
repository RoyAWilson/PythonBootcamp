# Ask user for a number then display a multiplication table for that number

num: int = int(input('Please enter an integer: >'))

for nums in range(13):
    print(f'{num} x {nums} = {num * nums}')

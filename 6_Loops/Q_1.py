# Ask user for 2 numbers between 1 & 100
# print a count from lower to the higher number

lower: int = input(
    'Plsease enter a number between 1 and 100 as an integer: > ')
higher: int = input(
    'Please enter a second higher number between lower number and 100: > ')

if lower.isnumeric() and higher.isnumeric():
    lower = int(lower)
    higher = int(higher)
    if lower < higher and higher <= 100:
        for i in range(lower, higher + 1):
            print(i, end=', ')
    else:
        print('Sorry the first number has to be lower than the second\nand the highest number allowed is 100')
else:
    print('At least one of your inputs was not an integer!')

"""
More on Try
"""

while True:
    try:
        x = int(input('Please enter a number: > '))
        break
    except ValueError:
        print('Whoops that\'s not a number.  Please enter again carefullly ....')

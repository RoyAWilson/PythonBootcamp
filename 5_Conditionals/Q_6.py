# Get user to input two integers and
# and swap the contents of the variables

print('Please enter 2 integer values below:')
x = input('Integer 1 (x), please: > ')
y = input('Integer 2 (y), plaase: > ')
if x.isnumeric() and y.isnumeric():
    x = int(x)
    y = int(y)
    x, y = y, x
    print(f'Integer x = {x}, integer y = {y}')
else:
    print(f'Either {x}, {y} or both are not integers, cannot conitinue')

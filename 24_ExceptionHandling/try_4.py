'''
More on try again
'''

# x = 'My name is Roy'
x = 7000
try:
    if not type(x) is int:
        raise TypeError('Only integers are allowed')
except TypeError as e:
    print(e)
else:
    print('Valid Input')

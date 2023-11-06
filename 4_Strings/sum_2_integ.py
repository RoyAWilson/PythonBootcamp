# To sum 2 integters

try:
    x: int = int(input('Enter integer 1 : '))
except:
    raise TypeError('Not an Ineger ending program')

try:
    y: int = int(input('Enter a second integer: '))
except:
    raise TypeError(
        'That is not an integer, please enter only integers. Ending program')
print(f'The sum of {x} plus {y} is {x + y}')

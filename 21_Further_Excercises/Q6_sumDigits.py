'''
Write a program that will return the sum of the digits of an integer
'''

number: str = ''
digits: list = []

number = input('Please enter a number and I will sum the digits: > ')

while not number.isnumeric():
    number = input(
        'I can only sum numbers.  Please only enter integer number: > ')
    break
for numbers in range(0, len(number)):
    digits.append(int(number[numbers]))
print(sum(digits))

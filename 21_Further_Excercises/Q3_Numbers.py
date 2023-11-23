'''
Write code to determine if a number is within 10 of 100 or 200
'''

number: int = 0

number: str = input('Enter a number: > ')

while not number.isdigit():
    number = input(
        f'Sorry I can only take numberic input \'{number}\' is not an integer; please try another entry: > ')
    break
number = int(number)
if ((number - 10 >= 90) or (number + 10 <= 110 and number + 10 >= 100)) and number < 111:
    print(f'Your number {number} is within 10 of 100')
elif ((number - 10 >= 190) or (number + 10 <= 210 and number + 10 >= 200)) and number < 211:
    print(f'Your number {number} is within 10 of 200')
else:
    print(f'Your number {number} is not in the permitted range range.')

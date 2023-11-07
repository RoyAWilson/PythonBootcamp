# Ask user to input 2 numbers between 1 and 2o
# if both greater than 15 then return the product
# if one greater than 15 return sum
# Otherwise return 0

print('Please input 2 numbers between 1 and 20')

num1 = input('Please enter first number:\n\t>> ')
num2 = input('Please enter sencond number:\n\t>> ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    if num1 >= 15 and num2 >= 15:
        print(f'The product of {num1} and {num2} is {num1 * num2}')
    elif num1 >= 15 or num2 >= 15:
        print(f'The sum of {num1} and {num2} is {num1 + num2}')
    else:
        print('Sorry, I can\'t be bothered with those numbers so your answer is 0!!')
else:
    print(f'Sorry I don\'t recognise either {
          num1} or {num2} as being integers')

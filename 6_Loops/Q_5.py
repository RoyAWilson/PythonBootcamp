# Ask the user to input a sequence of numbers.  Then calculate the mean and print the result.  Type exit to finish the inputs.
# NOTE CANNOT MAKE IT WORK WITH ISDIGIT AS PER COURSE BUT WORKS OK WITH ISNUMERIC() must be as I have a newer version of Python

user_input = input('Please enter a number: > ')
numbers = []

while not user_input.lower() == 'exit':
    while not user_input.isdigit():
        print('That is not a number, please only input numbers or exit to finish')
        user_input = input('Try again: > ')
    numbers.append(int(user_input))
    user_input = input('Please enter next nu8mber: > ')
total = 0
for number in numbers:
    total += number
print(f'The mean is: {sum(numbers)/len(numbers)}')

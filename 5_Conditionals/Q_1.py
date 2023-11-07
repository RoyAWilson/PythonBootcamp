# Write code that asks the user to input a number betwee 1 and 5 inclusive.
# The code will take the integer value and print out the string value.
# E.g.: If the user inputs 2 it will print out 'two'
# Reject any input that is not a number in that range.

x: int = int(
    input('Please enter a number between 1 and 5 as a digit:\n\t >>'))
if x == 1:
    print('You entered \'one\'')
elif x == 2:
    print('You entered \'two\'')
elif x == 3:
    print('You entered \'three\'')
elif x == 4:
    print('You entered \'four\'')
elif x == 5:
    print('You entered \'five\'')
else:
    print(f'{x} is not a digit between 1 and 5')

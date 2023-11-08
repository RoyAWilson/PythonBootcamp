# Modify Q_6 code to ask for user input

fact = input('Please input a number to calcualte the factorial: > ')
while not fact.isnumeric():
    input('Please only input a number: > ')
fact = int(fact)
for numbers in range(1, fact+1):
    fact = fact * numbers
print(f'The factorial is {fact}')

# Get the user to enter their name
# if the name is more that 5 letters long#
# then print out length of name
# else print the name is secret

nme: str = input('Please enter your name:\n\t>>')
if nme.isdigit():
    print(f'Really, your name is {nme}? How odd')
else:
    if len(nme) > 5:
        print(f'Your name {nme.upper()} is {len(nme)} characters long')
    else:
        print('Your name is secret')

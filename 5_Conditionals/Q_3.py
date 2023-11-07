# Create a variable holding a number between 1 and 10
# Get the use to guess the number and print a message
# to let them know if they win

NUM = 8
guess = input('Please enter an integer between 1 and 10\n\t>> ')
if guess.isdigit():
    guess = int(guess)
    if guess == NUM:
        print(f'Great guess the number was indeed {NUM}')
    else:
        print(f'Sorry your guess {guess} was incorrect')
else:
    print(f'Since when was {guess} an integer between 1 and ten?')

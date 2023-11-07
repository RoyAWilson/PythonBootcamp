# Simple guess the word game

word: str = 'summer'
guess: str = input(
    'I am thinking of a word.  Can you guess what it is?\n Hint it\'s a season\n\t> ')
guess = guess.lower()

if guess == word:
    print('Correct! The word is summer')
elif guess == 'winter':
    print('Sorry not winter')
elif guess == 'spring':
    print('Sorry not spring')
elif guess == 'autumn':
    print('Sorry Autumn is not the word')
else:
    print(f'{guess.upper()} is not a season!')

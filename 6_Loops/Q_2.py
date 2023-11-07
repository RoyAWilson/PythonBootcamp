# Ask user for a string and print in reverse using a for loop

word: str = input('Please enter a word to be reversed: >')

for char in range(len(word)-1, -1, -1):
    print(word[char], end='')

# Or:
reverse_name = ''
for char in word:
    reverse_name = char + reverse_name
print(reverse_name)

# Or without needing to loop:

print(word[::-1])

'''
Write a program that converts text into pig latin. Pig latin works as follows:
All letters before initial vowel are placed at the end of the word and then 'ay'
is added (explanation adapted from Wikipedia), so pig becomes igpay, cat becomes
atcay, potential becomes otentialpay etc.
'''

word: str = ''
splt_word: str = ''
end_chrs: str = ''
word_chunk: str = ''

word = input('Please enter a word to be redered in pig Latin: > ')
word = word.lower()
for letters in word:
    if letters not in 'aeiou':
        end_chrs += letters
        word_chunk = word[len(letters):]
        break
word = word_chunk + end_chrs + 'ay'
print(word)

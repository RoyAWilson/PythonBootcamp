'''
Write a function that will check if a string is a palindrome
'''


def pallindrome(word: str) -> str:
    word = word.lower().strip()
    wrd_list: list = []
    rvrsd_lst: list = []

    for letters in word:
        if letters in 'abcdefghijklmnopqrstuvwxyz':
            wrd_list.append(letters)
    # print(wrd_list)
    for rvletters in reversed(wrd_list):
        rvrsd_lst.append(rvletters)
    # print(rvrsd_lst)
    if wrd_list == rvrsd_lst:
        return f'{word} is a pallindrome'
    return f'{word} is not a pallindrome'


z = pallindrome('big')  # Test return when non-pallindrome
x = pallindrome('madam')  # Test return when pallindrome
w = pallindrome('madam i\'m adam')  # Test for pallindromic sentence
print(f'{z}\n{x}\n{w}')

'''
Write a function that will check for the occurrence of double letters in
a string. If the string contains double letters next to each other it
will return True, otherwise it will return False.
'''


def dbl_lttrs(words) -> bool:
    for letters in range(0, len(words)-1):
        if words[letters] == words[letters + 1]:
            return True

    return False


x = dbl_lttrs('assimilated')  # Test double letters contiguous
y = dbl_lttrs('pending')  # Test no double letters
z = dbl_lttrs('ttsirkd')  # Test double letters contiguous start of word
a = dbl_lttrs('pass')  # Test contiguous letters end of word
b = dbl_lttrs('talented')  # Test non-coniguous double letters
print(x, y, z, a, b)

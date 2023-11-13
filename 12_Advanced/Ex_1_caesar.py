# Encode the phrase The cat sat on the mat in caesar cipher

# Write a function to take an input of a phrase and a number and cipher the phrase by moving each letter n places to the right.

# Some problems that need solving - what to do if number runs off the end of the alphabet - Solved - wrap to start again.
# What to do with caps/lower case letters - Solved - encrypt each separately.
# What to do if with punctuation and spaces -Solved (keep the punctuation as is)

# Maybe ignore spaces and punctuation and keep as is.
# Maybe run straight through from the lower to the upper case letters rather that dealing with both - not good idea

# Will need to recognise thet chars numbers for each letter and add relevant number of chars
# If char + n > char of last letter of alsphabet wrap to first char again (if char(x) + n > char(highest) then char(highest)) - char(x) + char(first))?

# Lower case A = 97, lower case Z = 122, upper case A = 65, upper case Z = 90, space = 32, stop = 46, comma = 44

# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))
# print(ord(' '))
# print(ord('.'))
# print(ord(','))
punctuation = ['!', ':', ';', '?', '.', ',', ' ']

# get it to work as basic code then make it inot a function.

# cipher = []
# phrase = input(
#     'Please enter a phrase to encode.  Please use only letters and no digits. > ')
# num = int(input('Please enter a number for the encryption key: > '))
# for letters in phrase:
#     # grab spaces and punctuation
#     if letters in punctuation:
#         cipher.append(letters)
#     elif ord(letters) >= 65 and ord(letters) < 90 and ord(letters) + num > 90:
#         cipher.append(chr(ord(letters) + num - 26))
#     elif ord(letters) + num > 122:
#         cipher.append(chr(ord(letters) - 26 + num))
#     # print(cipher)
#     elif ord(letters) > 65 and ord(letters) - num < 123:
#         cipher.append(chr(ord(letters) + num))
#     # elif ord(letters) > 65 and ord(letters) < 91:
#     #     cipher.append(chr(ord(letters) + num))


# print(cipher)
# Now make it a cypher function

def caeser_enc(phrase, num):
    cipher = []
    encd = ''
    for letters in phrase:
        # grab spaces and punctuation
        if letters in punctuation:
            cipher.append(letters)
        elif ord(letters) >= 65 and ord(letters) < 90 and ord(letters) + num > 90:
            cipher.append(chr(ord(letters) + num - 26))
        elif ord(letters) + num > 122:
            cipher.append(chr(ord(letters) - 26 + num))
        # print(cipher)
        elif ord(letters) > 65 and ord(letters) - num < 123:
            cipher.append(chr(ord(letters) + num))
        elif ord(letters) > 65 and ord(letters) < 91:
            cipher.append(chr(ord(letters) + num))
        encd = ''.join(cipher)
    return encd


phrase = input('Please enter a phrase: > ')
enum = int(input(
    'Please enter seed number for encryption (Number less than 26, please): > '))
print(caeser_enc(phrase, enum))

# Tutors solution used modulus to perform the wrap
# if adding num runs off end of the alphabet, neat trick wish I had thought of that
# However the tutor ignores upper case letters by forcing input to lower case which is cheating!
# Tutor ignores punctuations by just adding input char if
# char not found in his variable holding the whole alphabet.

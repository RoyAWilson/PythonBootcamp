# Draw an F with stars:
# ******
# *
# ****
# *
# *
# *
# *

star = '*'
for i in range(1, 8):
    if i == 1:
        print(star * 6)
    elif i == 2:
        print(star)
    elif i == 3:
        print(star * 5, end='')
    elif i >= 4:
        print(star)

# Course tutor used to loops to print the stars:

for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 and j < 6:
            print(star, end='')
        elif i == 2 and j == 1:
            print
            print(star)
        elif i == 3 and j < 5:
            print(star, end='')
        elif i == 4 and j == 1:
            print()
            print(star)
        elif i == 5 and j == 1:
            print(star)
        elif i == 6 and i == 1:
            print(star)

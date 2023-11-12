# create a dictinoary with the keys A - Z assign a random value to each
# plot the results.

import random
import matplotlib.pyplot as plt
# set up dictionary

dict_1 = {}

# Set yo the keys

# keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
#         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# populate the dict and print the results.

for letter in keys:
    dict_1[letter] = random.randint(1, 100)
print(dict_1)
x, y = zip(* dict_1.items())

print(x, y)

# plt.boxplot(data=dict_1)  # , x=dict_1)
# plt.show()
# plt.close()
plt.bar(x, y)
plt.show()
plt.close()

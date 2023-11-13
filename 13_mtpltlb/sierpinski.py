import matplotlib.pyplot as plt
from random import choice

# Define transformation 1


def trans_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1


def trans_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1


def trans_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1


transformations = [trans_1, trans_2, trans_3]
a1 = [0]
b1 = [0]
a, b = 0, 0

# Step through i sets of transformations

for i in range(1000000):
    # Choose random transformation from list trans
    trans = choice(transformations)
    a, b = trans((a, b))  # Trnasform with chosen transformation
    a1.append(a)  # Append results to the lists
    b1.append(b)
    # print(a, b)
# Print out the results

plt.rc('figure', figsize=(16, 16))
plt.plot(a1, b1, 'o')
plt.show()
plt.close()

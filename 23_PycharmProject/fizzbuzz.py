
# FizzBuzz revisited.
# If number is divisible by 3 print fizz if divisible by 3 and
# 5 print fizzbuzz else return the number

import matplotlib.pyplot as plt

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz', end=' ')
    elif i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')

x = [k for k in range(1, 11)]
y = [j for j in range(1, 11)]
plt.plot(x, y)
plt.show()
plt.close()
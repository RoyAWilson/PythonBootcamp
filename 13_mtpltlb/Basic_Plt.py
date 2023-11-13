import matplotlib.pyplot as plt
from random import choice

plt.rc('figure', figsize=(12, 6))

values = list(range(0, 55, 5))

plt.plot(values)
plt.show()
plt.close()


x_axis = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.plot(x_axis, values)
plt.xlim(0, 1.0)
plt.ylim(0, 50)
plt.title('Our Plot')
plt.xlabel('This is the horizontal axis')
plt.ylabel('This is the vertical axis')
plt.show()
plt.close()

plt.plot(x_axis, values, 'ko--')
plt.xlim(0, 1.0)
plt.ylim(0, 50)
plt.title('Our Plot')
plt.xlabel('This is the horizontal axis')
plt.ylabel('This is the vertical axis')
plt.show()
plt.close()

# Same as preivous using class
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)
ax[0].plot([x for x in range(25)], [y**2 for y in range(25)])
ax[1].plot([x for x in range(25)], [y**3 for y in range(25)])
plt.savefig('./squarecubed_2.png')
plt.show()
plt.close()

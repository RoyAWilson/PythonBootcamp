import matplotlib
import matplotlib.pyplot as plt

# (2, 1, 1) = 2 want 1 plots, 1 column, 1 am working on 1 atm
plt.subplot(2, 1, 1)
# Plot squares of y
plt.plot([x for x in range(25)], [y**2 for y in range(25)])
# plot y
plt.plot([x for x in range(25)], [y for y in range(25)])
plt.title('Squared Numbers')
# Second plot
plt.subplot(2, 1, 2)
plt.plot([x for x in range(25)], [y**3 for y in range(25)])
plt.title('Cubed Numbers')
plt.savefig('./plots/sqrcbd.png')
plt.show()
plt.close()

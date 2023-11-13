import matplotlib.pyplot as plt
from random import choice

plt.rc('figure', figsize=(12, 6))

# step_option = [1, -1]
# step_choice = choice(step_option)

# walk = []
# walk.append(step_choice)
# for step in range(1, 1000):
#     next_step = walk[step-1] + choice(step_option)
#     walk.append(next_step)
# plt.plot(walk)
# plt.show()
# plt.close()

# Do it as a function


def Rand_Walk(step_number):
    walk = []
    step_choice = choice([1, -1])
    walk.append(step_choice)
    for i in range(1, step_number):
        step_choice_2 = choice([1, -1])
        next_step = walk[i - 1] + step_choice_2
        walk.append(next_step)
    return walk


def Plot_Walk(walk):
    x = list(range(1, len(walk) + 1))
    plt.plot(x, walk)
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.title('Our Random Walk')
    plt.show()
    plt.close()


Plot_Walk(Rand_Walk(1000))

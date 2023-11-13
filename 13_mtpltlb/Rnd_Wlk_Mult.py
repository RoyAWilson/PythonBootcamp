import matplotlib.pyplot as plt
from random import choice

plt.rc('figure', figsize=(12, 6))


def Rand_Walk(step_number):
    walk = []
    step_choice = choice([1, -1])
    walk.append(step_choice)
    for i in range(1, step_number):
        step_choice_2 = choice([1, -1])
        next_step = walk[i - 1] + step_choice_2
        walk.append(next_step)
    return walk


def plot_walks(num, walk_steps):
    lab_list = list(range(1, num + 1))
    for i in range(0, num):
        x = list(range(1, walk_steps + 1))
        plt.plot(x, Rand_Walk(walk_steps),
                 label='Plot Number:' + ' ' + str(lab_list[i]))
        plt.xlabel('Number of Steps')
        plt.ylabel('Distance from Origin')
        plt.title('Our Walk')
        plt.legend(loc='lower left')
    plt.show()
    plt.close()


plot_walks(5, 100000)

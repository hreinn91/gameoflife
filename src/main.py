from random import randrange
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from brain import Brain
from copy import deepcopy


# Unix requires python3-tk

ON = 255
OFF = 0

def plot_conf_style():
    # TkAgg required for display in Pycharm - render in canvas
    matplotlib.use('TkAgg')
    matplotlib.pyplot.style.use('dracula')


def foo_plot():
    random_matrix = np.random.rand(3, 3)
    fig = plt.subplots()
    matshow_matrix = ax.matshow(random_matrix)
    plt.colorbar(matshow_matrix)
    ani = animation.FuncAnimation(fig, lambda i: i, frames=19, interval=500)
    plt.show()


def update(i, img, brain):
    grid = brain.matrix.copy()
    row = randrange(brain.size)
    col = randrange(brain.size)
    print(grid[row, col])
    if grid[row, col] == ON:
        grid[row, col] = OFF
    else:
        grid[row, col] = ON
    img.set_data(grid)
    brain.matrix = grid
    return img,


def plot(brain):
    fig, ax = plt.subplots()
    img = ax.imshow(brain.matrix, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, brain),
                                  frames=19, interval=500, save_count=50)
    plt.show()
    pass


if __name__ == '__main__':
    plot_conf_style()
    brain = Brain(50)
    # grid = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)
    plot(brain)

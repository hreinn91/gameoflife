import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from brain import Brain
from copy import deepcopy


# Unix requires python3-tk

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


def update(i, img, grid):
    new_grid = grid
    if new_grid[0, 1] == 255:
        new_grid[0, 1] = 0
    else:
        new_grid[0, 1] = 255

    img.set_data(new_grid)
    # grid[:] = new_grid[:]
    return img,


def plot(grid):
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid),
                                  frames=19, interval=500, save_count=50)
    plt.show()
    pass


if __name__ == '__main__':
    plot_conf_style()
    N = 5
    vals = [255, 0]
    grid = np.random.choice(vals, N * N, p=[0.2, 0.8]).reshape(N, N)
    plot(grid)

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from brain import Brain


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


def update(i, img, brain):
    matrix = brain.step().copy()
    img.set_data(matrix)
    return img,


def plot(brain):
    matrix = brain.matrix
    fig, ax = plt.subplots()
    img = ax.imshow(matrix, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, brain),
                                  frames=19, interval=500, save_count=50)
    plt.show()
    pass


if __name__ == '__main__':
    plot_conf_style()
    brain = Brain(4)
    plot(brain)

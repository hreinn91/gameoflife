import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Unix requires python3-tk

def plot_conf_style():
    # TkAgg required for display in Pycharm - render in canvas
    matplotlib.use('TkAgg')
    matplotlib.pyplot.style.use('dracula')


def foo_plot():
    random_matrix = np.random.rand(3, 3)
    fig, ax = plt.subplots()
    matshow_matrix = ax.matshow(random_matrix)
    plt.colorbar(matshow_matrix)
    ani = animation.FuncAnimation(fig, lambda i: i, frames=19, interval=500)
    plt.show()


if __name__ == '__main__':
    plot_conf_style()
    foo_plot()

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from brain import Brain, random_init


# Unix requires python3-tk

def plot_conf_style():
    # TkAgg required for display in Pycharm - render in canvas
    matplotlib.use('TkAgg')
    matplotlib.pyplot.style.use('dracula')


def update(i, img, brain):
    img.set_data(brain.step())
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
    init_mat = random_init(100)
    brain = Brain(ini_mat=init_mat)
    brain.inject_block(10, 10)
    brain.inject_block(30, 30)
    brain.inject_block(50, 50)
    plot(brain)

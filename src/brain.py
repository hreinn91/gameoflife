import numpy as np
from random import randrange

ON = 255
OFF = 0


class Brain:
    def __init__(self, size):
        print('Init')
        self.size = size
        # self.matrix = np.random.choice([ON, OFF], size * size, p=[0.2, 0.8]).reshape(size, size)
        self.matrix = empty_init(size)

    def step(self):
        print('Arrrg')
        row = randrange(self.size)
        col = randrange(self.size)
        print(self.matrix[row, col])

        if self.matrix[row, col] == ON:
            self.matrix[row, col] = OFF
        else:
            self.matrix[row, col] = ON

        print(self.matrix)
        return self.matrix


def random_init(size):
    return np.random.choice([ON, OFF], size * size, p=[0.2, 0.8]).reshape(size, size)


def empty_init(size):
    np.zeros(size * size).reshape(size, size)
    # One value needed to init animation
    self.matrix[1, 1] = 1

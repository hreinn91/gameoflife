"""
 GOL RULES
 1 Any live cell with 2-3 nb will survive
 2 Any dead cell with 3 nb will become live
 3 All other cells die
"""
from random import randrange
from copy import deepcopy
import math
import numpy as np

ON = 255
OFF = 0


class Brain:
    def __init__(self, size=0, ini_mat=None):
        self.age = 0
        if ini_mat is None:
            self.matrix = empty_init(size)
            self.size = size
        else:
            self.matrix = ini_mat
            self.size = int(math.sqrt(ini_mat.size))
        self.life_count = self.calc_life_count()

    def get_val(self, i, j):
        return self.matrix[i, j]

    def inject_block(self, row, column, block_size=4):
        self.matrix[row:row + block_size, column:column + block_size] = np.full((block_size, block_size), ON)

    def step(self):
        self.age = self.age + 1
        grid = deepcopy(self.matrix)
        # GOL RULES
        # 1 Any live cell with 2-3 nb will survive
        # 2 Any dead cell with 3 nb will become live
        # 3 All other cells die
        for row in range(self.size):
            for col in range(self.size):
                count = self.count_neighbours(self.matrix, row, col)
                if count == 3:
                    grid[row, col] = ON
                elif count != 2:
                    grid[row, col] = OFF

        self.matrix = grid
        self.life_count = self.calc_life_count()
        print('age: {} count: {}'.format(self.age, self.life_count))
        return self.matrix

    @staticmethod
    def count_neighbours(matrix, i, j):
        N = int(math.sqrt(matrix.size))
        return int((matrix[i, (j - 1) % N] + matrix[i, (j + 1) % N] +
                    matrix[(i - 1) % N, j] + matrix[(i + 1) % N, j] +
                    matrix[(i - 1) % N, (j - 1) % N] + matrix[(i - 1) % N, (j + 1) % N] +
                    matrix[(i + 1) % N, (j - 1) % N] + matrix[(i + 1) % N, (j + 1) % N]) / ON)

    def calc_life_count(self):
        count = 0
        for row in self.matrix:
            for index in row:
                if index == ON:
                    count = count + 1
        return count


def random_init(size):
    return np.random.choice([ON, OFF], size * size, p=[0.2, 0.8]).reshape(size, size)


def empty_init(size):
    matrix = np.zeros(size * size).reshape(size, size)
    # One value needed to init animation
    matrix[1, 1] = ON
    return matrix


def random_step(matrix, size):
    row = randrange(size)
    col = randrange(size)
    if matrix[row, col] == ON:
        matrix[row, col] = OFF
    else:
        matrix[row, col] = ON

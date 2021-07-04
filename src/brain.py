import numpy as np
from random import randrange

class Brain:
    def __init__(self, size):
        print('Init')
        self.size = size
        self.matrix = np.zeros([size, size]).astype('int64')

    def step(self):
        print('Arrrg')
        row = randrange(self.size)
        col = randrange(self.size)
        # self.matrix[row][col] = self.matrix[row][col] + 1
        self.matrix[1, 1] = self.matrix[1, 1] + 10
        self.matrix[0, 1] = self.matrix[0, 1] + 10
        print(self.matrix)
        return self.matrix

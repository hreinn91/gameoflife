import numpy as np


class Brain:
    def __init__(self, size):
        self.size = size
        self.matrix = np.zeros([size, size])

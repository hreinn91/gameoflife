import unittest
from src.brain import Brain, ON, OFF
import numpy as np


class MyTestCase(unittest.TestCase):
    def test_sanity_check(self):
        size = 3
        brain = Brain(size=size)
        self.assertEqual(brain.matrix.shape, (size, size))
        self.assertEqual(brain.matrix.size, size * size)

    def test_get_live_count(self):
        x = np.array([[ON, ON, ON], [ON, ON, ON], [ON, ON, ON]])
        brain = Brain(ini_mat=x)
        self.assertEqual(x.size, 9)
        self.assertEqual(x.size, brain.get_live_count())

    def test_step(self):
        x = np.array([[ON, ON, ON], [ON, ON, ON], [ON, ON, ON]])
        brain = Brain(ini_mat=x)
        brain.step()
        brain.step()
        brain.step()


if __name__ == '__main__':
    unittest.main()

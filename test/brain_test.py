import unittest
from src.brain import Brain


class MyTestCase(unittest.TestCase):
    def test_sanity_check(self):
        size = 3
        brain = Brain(size=size)
        self.assertEqual(brain.matrix.shape, (size, size))
        self.assertEqual(brain.matrix.size, size * size)


if __name__ == '__main__':
    unittest.main()

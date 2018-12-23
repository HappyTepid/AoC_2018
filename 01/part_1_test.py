import unittest
from part_1 import solve_examples as solve


class TestSolve(unittest.TestCase):

    def setUp(self):
        pass

    def test_example_1(self):
        self.assertEqual(solve('+1, +1, +1'), 3)

    def test_example_2(self):
        self.assertEqual(solve('+1, +1, -2'), 0)

    def test_example_3(self):
        self.assertEqual(solve('-1, -2, -3'), -6)


if __name__ == '__main__':
    unittest.main()

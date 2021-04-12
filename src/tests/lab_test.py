import unittest
from lab import Lab

LAB_MAP_1 =   [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

CELL_SIZE = 50


class TestLab(unittest.TestCase):
    def setUp(self):
        self.lab_1 = Lab(LAB_MAP_1, CELL_SIZE)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_initial_rat_is_correct(self):
        rat = self.lab_1.rat

        self.assert_coordinates_equal(rat, 3 * CELL_SIZE, 2 * CELL_SIZE)
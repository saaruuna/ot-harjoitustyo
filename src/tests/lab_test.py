import unittest
from lab import Lab

LAB_MAP_1 =   [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 2, 3, 4, 1],
               [1, 1, 1, 1, 1]]

SCALE = 20


class TestLab(unittest.TestCase):
    def setUp(self):
        self.lab_1 = Lab(LAB_MAP_1, SCALE)

    def assert_coordinates_equal(self, sprite, x_position, y_position):
        self.assertEqual(sprite.rect.x, x_position)
        self.assertEqual(sprite.rect.y, y_position)

    def test_initial_rat_is_correct(self):
        rat = self.lab_1.rat

        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

    def test_can_move_in_floor(self):
        rat = self.lab_1.rat

        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

        self.lab_1.move_rat(y_change=-SCALE)
        self.assert_coordinates_equal(rat, 3 * SCALE, SCALE)

        self.lab_1.move_rat(x_change=-CELL_SIZE)
        self.assert_coordinates_equal(rat, 2 * SCALE, SCALE)

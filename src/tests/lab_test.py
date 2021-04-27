import unittest
from ui.lab import Lab

LAB_MAP =     [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 3, 2, 4, 1],
               [1, 1, 1, 1, 1]]

SCALE = 20


class TestLab(unittest.TestCase):
    def setUp(self):
        self.lab = Lab("TEST", LAB_MAP)

    def assert_coordinates_equal(self, sprite, x_position, y_position):
        self.assertEqual(sprite.rect.x, x_position)
        self.assertEqual(sprite.rect.y, y_position)

    def test_initial_rat_is_correct(self):
        rat = self.lab.rat

        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

    def test_can_move_in_floor(self):
        rat = self.lab.rat

        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

        self.lab.move_rat(y_change=-SCALE)
        self.assert_coordinates_equal(rat, 3 * SCALE, SCALE)

        self.lab.move_rat(x_change=-SCALE)
        self.assert_coordinates_equal(rat, 2 * SCALE, SCALE)

    def test_cannot_move_through_walls(self):
        rat = self.lab.rat

        self.assertEqual(self.lab.rat_can_move(x_change = SCALE), False)

    def test_does_not_move_through_walls(self):
        rat = self.lab.rat

        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)
        self.lab.move_rat(x_change = SCALE)
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)
        self.lab.move_rat(y_change = SCALE)
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

    def test_rat_gets_cheese(self):
        rat = self.lab.rat

        self.assertEqual(self.lab.rat_got_cheese(), False)
        self.lab.move_rat(y_change=-SCALE)
        self.lab.move_rat(x_change=-SCALE)
        self.lab.move_rat(x_change=-SCALE)
        self.lab.move_rat(y_change=SCALE)
        self.assertEqual(self.lab.rat_got_cheese(), True)

    def test_rat_hits_trap(self):
        rat = self.lab.rat
        self.assertEqual(self.lab.rat_hit_trap(), False)
        self.lab.move_rat(x_change=-SCALE)
        self.assertEqual(self.lab.rat_hit_trap(), True)

import unittest
from logic.lab import Lab

LAB_MAP1 =    [[1, 1, 1, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 3, 2, 4, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 1, 1, 1]]

LAB_MAP2 =    [[1, 1, 1, 0, 1],
               [1, 0, 0, 0, 1],
               [1, 3, 2, 0, 1],
               [0, 0, 0, 4, 0],
               [0, 0, 0, 0, 0]]

SCALE = 20


class TestLab(unittest.TestCase):
    def setUp(self):
        self.lab1 = Lab("TEST1", LAB_MAP1)
        self.lab2 = Lab("TEST2", LAB_MAP2)

    def assert_coordinates_equal(self, sprite, x_position, y_position):
        self.assertEqual(sprite.rect.x, x_position)
        self.assertEqual(sprite.rect.y, y_position)

    def test_initial_rat_is_correct(self):
        rat = self.lab1.rat
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

    def test_can_move_in_floor(self):
        rat = self.lab1.rat
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)
        self.lab1.move_rat(y_change=-SCALE)
        self.assert_coordinates_equal(rat, 3 * SCALE, SCALE)
        self.lab1.move_rat(x_change=-SCALE)
        self.assert_coordinates_equal(rat, 2 * SCALE, SCALE)

    def test_cannot_move_through_walls(self):
        self.assertEqual(self.lab1.rat_can_move(x_change = SCALE), False)

    def test_does_not_move_through_walls(self):
        rat = self.lab1.rat
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)
        self.assertEqual(self.lab1.rat_can_move(x_change = SCALE), False)
        self.assertEqual(self.lab1.rat_can_move(y_change = 2*SCALE), False)

    def test_rat_does_not_go_out_of_bounds(self):
        self.assertEqual(self.lab2.rat_can_move(x_change = 2*SCALE), False)
        self.assertEqual(self.lab2.rat_can_move(y_change = 2*SCALE), False)
        self.assertEqual(self.lab2.rat_can_move(x_change = -4*SCALE), False)
        self.assertEqual(self.lab2.rat_can_move(y_change = -4*SCALE), False)

    def test_rat_gets_cheese(self):
        self.lab1.move_rat(y_change=-SCALE)
        self.lab1.move_rat(x_change=-SCALE)
        self.lab1.move_rat(x_change=-SCALE)
        self.lab1.move_rat(y_change=SCALE)
        self.assertEqual(self.lab1.rat_got_cheese(), True)

    def test_rat_does_not_get_cheese(self):
        self.assertEqual(self.lab1.rat_got_cheese(), False)

    def test_rat_does_not_hit_trap(self):
        self.assertEqual(self.lab1.rat_hit_trap(), False)


    def test_rat_hits_trap(self):
        self.lab1.move_rat(x_change=-SCALE)
        self.assertEqual(self.lab1.rat_hit_trap(), True)

    def test_lab_resets(self):
        self.lab1.move_rat(x_change=-SCALE)
        self.lab1.reset_lab()
        rat = self.lab1.rat
        self.assert_coordinates_equal(rat, 3 * SCALE, 2 * SCALE)

import unittest
from logic.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_set_up(self):
        self.assertEqual(self.game.running, True)
        self.assertEqual(self.game.playing, False)
        self.assertEqual(self.game.designing, False)
        self.assertEqual(self.game.curr_menu, self.game.main_menu)

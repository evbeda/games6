import unittest
from wumpus.game import WumpusGame
from wumpus.constants import IN_PROGRESS


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = WumpusGame()

    def test_initial_game(self):
        self.assertEqual(self.game.state, IN_PROGRESS)

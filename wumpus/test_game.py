import unittest
from wumpus.game import WumpusGame
from wumpus.constants import IN_PROGRESS, COL, ROW


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = WumpusGame()

    def test_initial_game(self):
        self.assertEqual(self.game.state, IN_PROGRESS)

    def test_board_columns(self):
        for row in self.game.board:
            self.assertEqual(len(row), COL)

    def test_board_rows(self):
        self.assertEqual(len(self.game.board), ROW)

    def test_initial_place_player(self):
        self.game.place_player()
        self.assertEqual(self.game.board[0][0], "J")

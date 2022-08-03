import unittest
from othello.othello_game import Othello


class Test_othello(unittest.TestCase):

    def setUp(self):
        self.game = Othello()
        self.board = self.game.init_board

    def test_board_size(self):
        self.assertEqual(len(self.board), 8)
        for row in self.board:
            self.assertEqual(len(row), 8)


if __name__ == "__main__":
    unittest.main()

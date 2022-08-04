import unittest
from parameterized import parameterized

from othello.othello_game import Othello
from othello.scenarios_test import (
    black_12,
    white_12,
    mix_6)


class Test_othello(unittest.TestCase):

    def setUp(self):
        self.game = Othello()
        self.board = self.game.init_board

    def test_board_size(self):
        self.assertEqual(len(self.board), 8)
        for row in self.board:
            self.assertEqual(len(row), 8)

    def test_initial_black_piece_count(self):
        black_pieces = self.game.get_piece_count(self.game.init_board, 'B')
        self.assertEqual(2, black_pieces)

    @parameterized.expand(
        [
            (black_12, 12, 'B'),
            (white_12, 12, 'W'),
            (mix_6, 6, 'W'),
            (mix_6, 6, 'B'),
        ]
    )
    def test_initia_white_piece_count(self, board, expected, kind):
        pieces = self.game.get_piece_count(board, kind)
        self.assertEqual(expected, pieces)

    @parameterized.expand(
        [
            (black_12, 'B', 1, 1),
            (white_12, 'W', 1, 5),
            (mix_6, 'W', 4, 4),
            (mix_6, 'B', 7, 1),
            (mix_6, None, 4, 5),
            (black_12, None, 2, 5),
            (white_12, None, 6, 6)
        ]
    )
    def test_what_is(self, board, expected, row, col):
        self.game.init_board = board
        value = self.game.what_is(row, col)
        self.assertEqual(expected, value)


if __name__ == "__main__":
    unittest.main()

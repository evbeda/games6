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

    def test_initial_play(self):
        self.assertTrue(self.game.player_turn == 'B')

    @parameterized.expand(
        [
            (1, 'W'),
            (3, 'W'),
            (4, 'B'),
            (7, 'W'),
        ]
    )
    def test_current_turn(self, it, expected):
        for _ in range(it):
            self.game.next_turn()
        self.assertEqual(expected, self.game.player_turn)


if __name__ == "__main__":
    unittest.main()

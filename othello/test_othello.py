import unittest
from parameterized import parameterized

from othello.othello_game import Othello
from othello.scenarios_test import (
    black_12,
    white_12,
    mix_6,
    mix_10)


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

    @parameterized.expand(
        [
            (black_12, False, 1, 1),
            (white_12, False, 1, 5),
            (mix_6, False, 4, 4),
            (mix_6, False, 7, 1),
            (mix_6, True, 4, 5),
            (black_12, True, 2, 5),
            (white_12, True, 6, 6)
        ]
    )
    def test_is_empty(self, board, expected, row, col):
        self.game.init_board = board
        value = self.game.is_empty(row, col)
        self.assertEqual(expected, value)

    @parameterized.expand(
        [
            (1, 'B'),
            (3, 'B'),
            (4, 'W'),
            (7, 'B'),
        ]
    )
    def test_opposite_piece(self, it, expected):
        for _ in range(it):
            self.game.next_turn()
        self.assertEqual(expected, self.game.get_opposite_piece())

    @parameterized.expand(
        [
            ({'from_row': 0,
                'to_row': 1,
                'from_col': 0,
                'to_col': 1}, 0, 0),

            ({'from_row': 6,
                'to_row': 7,
                'from_col': 6,
                'to_col': 7}, 7, 7),

            ({'from_row': 0,
                'to_row': 1,
                'from_col': 6,
                'to_col': 7}, 0, 7),

            ({'from_row': 6,
                'to_row': 7,
                'from_col': 0,
                'to_col': 1}, 7, 0),

            ({'from_row': 0,
                'to_row': 1,
                'from_col': 0,
                'to_col': 1}, 0, 0),

            ({'from_row': 3,
                'to_row': 5,
                'from_col': 3,
                'to_col': 5}, 4, 4),
        ]
    )
    def test_get_llimits(self, expected, row, col):

        self.assertEqual(expected, self.game.get_limits(row, col))

    @parameterized.expand(
        [
            (black_12, [], 'B', 1, 1),
            (white_12, [], 'W', 1, 5),
            (mix_6, [(3, 4), (4, 3)], 'W', 4, 4),
            (mix_6, [], 'B', 7, 1),
            (black_12, [(3, 4), (4, 3)], 'W', 3, 3),
            (mix_10, [(3, 3), (4, 4), (5, 2), (5, 4)], 'B', 4, 3),
            (mix_10, [(2, 2), (3, 4), (4, 3)], 'W', 3, 3)
        ]
    )
    def test_close_opposite_pieces(self, board, expected, player, row, col):
        self.game.init_board = board
        self.game.player_turn = player
        self.assertEqual(expected, self.game.close_opposite_around(row, col))


if __name__ == "__main__":
    unittest.main()

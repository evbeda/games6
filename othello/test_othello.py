import unittest
from parameterized import parameterized

from othello.othello_game import Othello
from othello.scenarios_test import (
    black_12,
    white_12,
    mix_6,
    mix_10,
    flip_black,
    final_flip_black,
    flip_row_white,
    final_flip_row_white,
    diagonal_flip,
    final_diagonal_flip,
    validate_direction_1,
    validate_direction_2)


class Test_othello(unittest.TestCase):

    def _convert_scenario_to_matrix(self, scenario):
        matrix = []
        for scenario_line in scenario:
            matrix_line = [
                scenario_letter
                if scenario_letter in 'BW'
                else None
                for scenario_letter in scenario_line
            ]
            matrix.append(matrix_line)
        return matrix

    def setUp(self):
        self.game = Othello()

    def test_board_size(self):
        self.assertEqual(len(self.game.board), 8)
        for row in self.game.board:
            self.assertEqual(len(row), 8)

    def test_initial_black_piece_count(self):
        black_pieces = self.game.get_piece_count('B')
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
        # replace board to see diferents situacions
        self.game.board = self._convert_scenario_to_matrix(board)
        pieces = self.game.get_piece_count(kind)
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
        self.game.board = self._convert_scenario_to_matrix(board)
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
        self.game.board = self._convert_scenario_to_matrix(board)
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
        self.game.board = self._convert_scenario_to_matrix(board)
        self.game.player_turn = player
        self.assertEqual(expected, self.game.close_opposite_around(row, col))

    @parameterized.expand(
        # initial_board , coordinates , index_player, final_board
        [
            (flip_black, [(0, 0)], 1, final_flip_black),
            (flip_row_white, [(5, 0), (5, 2), (5, 4)], 0,
                final_flip_row_white),
            (diagonal_flip, [(0, 0), (1, 1), (2, 2)], 1,
                final_diagonal_flip)
        ]
    )
    def test_flip_pieces(self, initial_board, cordinates, index, final_board):
        self.game.board = self._convert_scenario_to_matrix(initial_board)
        self.game.player_turn = self.game.possibles_players[index]
        self.game.flip_pieces(cordinates)
        self.assertEqual(
            self._convert_scenario_to_matrix(final_board), self.game.board)

    @parameterized.expand(
        [
            (validate_direction_1, 'B', 6, 4, "n", [[5, 4], [4, 4]]),
            (validate_direction_1, 'W', 7, 4, "ne", [[6, 5], [5, 6]]),
            (validate_direction_1, 'W', 0, 5, "e", [[0, 6]]),
            (validate_direction_1, 'B', 0, 0, "se", [[1, 1]]),
            (validate_direction_2, 'B', 0, 6, "s", [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6]]),
            (validate_direction_1, 'W', 2, 5, "sw", [[3, 4], [4, 3]]),
            (validate_direction_2, 'W', 4, 3, "w", [[4, 2], [4, 1]]),
            (validate_direction_2, 'W', 6, 4, "nw", [[5, 3], [4, 2], [3, 1]]),
            (validate_direction_2, 'W', 0, 4, "n", False),
            (validate_direction_2, 'B', 3, 0, "w", False),
            (validate_direction_2, 'W', 7, 1, "s", False),
            (validate_direction_2, 'B', 5, 7, "e", False),
        ]
    )
    def test_validate_direction(self, board, player, row, col, direction, expected):
        self.game.board = board
        self.game.player_turn = player
        self.assertEqual(expected, self.game.validate_direction(row, col, direction))


if __name__ == "__main__":
    unittest.main()

import unittest
from parameterized import parameterized

from othello.othello_game import Othello
from othello.scenarios_test import (
    black_12,
    white_12,
    mix_6,
    # mix_10,
    flip_black,
    final_flip_black,
    flip_row_white,
    final_flip_row_white,
    diagonal_flip,
    final_diagonal_flip,
    board_winner_w,
    board_tie,
    board_tie_empty,
    validate_direction_1,
    validate_direction_2,
    all_poss_moves_board_1,
    all_poss_moves_exp_1,
    none_pos_exp_1,
    black_12_that_will_print,
    white_12_that_will_print)


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
        self.assertEqual(len(self.game._board), 8)
        for row in self.game._board:
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
        self.game._board = self._convert_scenario_to_matrix(board)
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
        self.game._board = self._convert_scenario_to_matrix(board)
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
        self.game._board = self._convert_scenario_to_matrix(board)
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
        self.game._board = self._convert_scenario_to_matrix(initial_board)
        self.game.player_turn = self.game.possibles_players[index]
        self.game.flip_pieces(cordinates)
        self.assertEqual(
            self._convert_scenario_to_matrix(final_board), self.game._board)

    @parameterized.expand(
        [
            (validate_direction_1, 'B', 6, 4, "n", [(5, 4), (4, 4)]),
            (validate_direction_1, 'W', 7, 4, "ne", [(6, 5), (5, 6)]),
            (validate_direction_1, 'W', 0, 5, "e", [(0, 6)]),
            (validate_direction_1, 'B', 0, 0, "se", [(1, 1)]),
            (validate_direction_2, 'B', 0, 6, "s", [(1, 6), (2, 6), (3, 6),
                                                    (4, 6), (5, 6), (6, 6)]),
            (validate_direction_1, 'W', 2, 5, "sw", [(3, 4), (4, 3)]),
            (validate_direction_2, 'W', 4, 3, "w", [(4, 2), (4, 1)]),
            (validate_direction_2, 'W', 6, 4, "nw", [(5, 3), (4, 2), (3, 1)]),
            (validate_direction_2, 'W', 0, 4, "n", []),
            (validate_direction_2, 'B', 3, 0, "w", []),
            (validate_direction_2, 'W', 7, 1, "s", []),
            (validate_direction_2, 'B', 5, 7, "e", []),
            (validate_direction_2, 'B', 1, 3, "e", []),
        ]
    )
    def test_validate_direction(self, board, player,
                                row, col, direction, expected):
        self.game._board = board
        self.game.player_turn = player
        self.assertEqual(expected,
                         self.game.validate_direction(row, col, direction))

    def test_select_winner_white(self):
        self.game._board = self._convert_scenario_to_matrix(board_winner_w)
        winner = self.game.determine_winner()
        self.assertEqual("W", winner)

    def test_select_winner_black(self):
        self.game._board = self._convert_scenario_to_matrix(diagonal_flip)
        winner = self.game.determine_winner()
        self.assertEqual("B", winner)

    def test_select_winner_tie(self):
        self.game._board = self._convert_scenario_to_matrix(board_tie)
        winner = self.game.determine_winner()
        self.assertEqual("Tie", winner)

    def test_select_empty_tie(self):
        self.game._board = self._convert_scenario_to_matrix(board_tie_empty)
        winner = self.game.determine_winner()
        self.assertEqual("Tie", winner)

    @parameterized.expand(
        [
            (validate_direction_2, 'B', 1, 2, []),
            (validate_direction_2, 'B', 0, 6, [(1, 6), (2, 6), (3, 6),
                                               (4, 6), (5, 6), (6, 6)]),
        ]
    )
    def test_validate_move(self, board, player, row, col, expected):
        self.game._board = board
        self.game.player_turn = player
        self.assertEqual(expected, self.game.validate_move(row, col))

    @parameterized.expand(
        [
            ({}, False),
            ({(1, 1): [(1, 2), (1, 3)]}, True)
        ]
    )
    def test_check_if_the_player_can_play(self, moves, expected_result):
        self.assertEqual(self.game.check_if_the_player_can_play(moves),
                         expected_result)

    @parameterized.expand(
        [
            (False, False, False),
            (False, True, True),
            (True, False, True),
            (True, True, True)
        ]
    )
    def test_end_game(self, black_player, white_player, expected_result):
        self.game.black_can_play = black_player
        self.game.white_can_play = white_player
        self.game.end_game()
        self.assertEqual(self.game.is_playing, expected_result)

    @parameterized.expand(
        [
            (all_poss_moves_board_1, all_poss_moves_exp_1)
        ]
    )
    def test_all_possible_moves_values(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.all_possible_moves()
        for key, value in result.items():
            result_list = sorted(value, key=lambda tup: (tup[0], tup[1]))
            expected_list = sorted(expected[key],
                                   key=lambda tup: (tup[0], tup[1]))
            self.assertEqual(result_list, expected_list)

    @parameterized.expand(
        [
            (all_poss_moves_board_1, all_poss_moves_exp_1)
        ]
    )
    def test_all_possible_moves_values_key(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.all_possible_moves()
        self.assertEqual(result.keys(), expected.keys())

    @parameterized.expand(
        [
            (all_poss_moves_board_1, none_pos_exp_1)
        ]
    )
    def test_none_pos(self, board, expected):
        self.game._board = self._convert_scenario_to_matrix(board)
        result = self.game.none_pos()
        self.assertListEqual(result, expected)

    @parameterized.expand([
        (black_12, black_12_that_will_print)
    ])
    def test_board_printer(self, board, expected_result):
        self.game._board = board
        result = self.game.board_printer()
        for row in range(len(self.game._board)):
            self.assertEqual(result[row], expected_result[row])

    @parameterized.expand([
        (black_12, black_12_that_will_print),
        (white_12, white_12_that_will_print),
    ])
    def test_board(self, board, expected_result):
        expected_result_as_string = ''
        for rows in expected_result:
            expected_result_as_string += rows + '\n'
        self.game._board = board
        result = self.game.board
        self.assertEqual(result, expected_result_as_string)


if __name__ == "__main__":
    unittest.main()

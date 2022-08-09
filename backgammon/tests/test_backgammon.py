import unittest
from parameterized import parameterized
from backgammon.game.backgammon import BackgammonGame
from backgammon.tests.test_scenarios import initial_board, board_1
from unittest.mock import patch


class BackgammonGameTest(unittest.TestCase):

    def setUp(self):
        self.backgammon = BackgammonGame()

    def test_game_active_change(self):
        self.backgammon.game_active_change()
        self.assertEqual(self.backgammon.active_game, False)

    def test_slots(self):
        self.assertEqual(len(self.backgammon.board), 24)

    def test_initial_board(self):
        expected_board = [
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
            [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
        ]
        self.assertListEqual(expected_board, self.backgammon.board)

    @parameterized.expand([
        ("WHITE", initial_board, 0, 11, 16, 18),
        ("BLACK", initial_board, 5, 7, 12, 23)
    ])
    def test_available_pieces(self, side, board, *expected_result):
        self.backgammon.board = board
        result = self.backgammon.available_pieces(side)
        self.assertEqual(result, list(expected_result))

    @patch('random.choice', return_value='WHITE')
    def test_player_1(self, patched_randint):
        new_game = BackgammonGame()
        player = new_game.player
        self.assertEqual(player, 'WHITE')

    @patch('random.choice', return_value='BLACK')
    def test_player_2(self, patched_randint):
        new_game = BackgammonGame()
        player = new_game.player
        self.assertEqual(player, 'BLACK')

    @parameterized.expand([
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ])
    @patch('random.randint')
    def test_roll_dices_number_interval(self, expetc_value,
                                        patch_value, patch_function):
        patch_function.return_value = patch_value
        self.assertEqual(self.backgammon.roll_dices(),
                         (expetc_value, expetc_value))

    @parameterized.expand([
        ('WHITE', 'BLACK'),
        ('BLACK', 'WHITE'),
    ])
    def test_opposite(self, current_player, expected):

        self.backgammon.player = current_player
        self.assertEqual(self.backgammon.opposite, expected)

    @parameterized.expand(
        [
            (3, 'BLACK', 'WHITE'),
            (1, 'WHITE', 'BLACK'),
            (4, 'WHITE', 'WHITE'),
            (7, 'WHITE', 'BLACK'),
        ]
    )
    @patch('random.choice')
    def test_change_player(self, it, expected,
                           patch_value, patch_function):
        patch_function.return_value = patch_value
        game = BackgammonGame()
        for _ in range(it):
            game.change_active_player()
        self.assertEqual(expected, game.player)

    @parameterized.expand([
        ("BLACK", 0, False),
        ("WHITE", 1, True)


    ])
    def test_less_than_two_enemies_in_position(self, current_player, position,
                                               expected_result):
        self.backgammon.player = current_player
        result = self.backgammon.less_than_two_enemies_in_position(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ('WHITE', 11, False),
        ('WHITE', 16, True),
        ('WHITE', 18, False),
        ('BLACK', 5, False),
        ('BLACK', 12, False),
    ])
    def test_less_than_five_own_pieces(self, current_player,
                                       position, expected):
        self.backgammon.player = current_player
        result = self.backgammon.less_than_five_own_pieces(position)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            ('BLACK', 0, False),
            ('WHITE', 1, False),
            ('WHITE', 11, True),
            ('BLACK', 5, True),
        ]
    )
    def test_at_least_one_piece_of_the_player(self, current_player,
                                              position, expected_result):
        self.backgammon.player = current_player
        result = self.backgammon.at_least_one_piece_of_the_player(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([

        ('WHITE', 1, 5, False),
        ('WHITE', 5, 6, False),
        ('WHITE', 0, 11, False),
        ('BLACK', 5, 2, True),
        ('BLACK', 12, 7, True),
        ('BLACK', 23, 19, True),
        ('BLACK', 21, 22, False),
        ('BLACK', 23, 18, False),

    ])
    def test_valid_move(self, current_player,
                        initial_pos, final_pos, expected):
        self.backgammon.player = current_player
        result = self.backgammon.is_valid_move(initial_pos, final_pos)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (5,)
    ])
    def test_capture_opposite_piece(self, position):
        game = BackgammonGame()
        game.player = "WHITE"
        game.capture_opposite_piece(position)
        captured_piece = game.expelled["BLACK"]
        self.assertEqual(1, captured_piece)

    @parameterized.expand([
        (initial_board, 0, 0, 1, 0)
    ])
    def test_change_position(self, board, actual_row, actual_col,
                             new_row, new_col):
        game = BackgammonGame()
        game.board = board
        game.change_position(actual_row, actual_col, new_row, new_col)
        self.assertEqual(1, game.board[new_row][new_col])

    @parameterized.expand([

        (2, 3, [2, 3, 5]),
        (3, 4, [3, 4, 7]),
        (5, 5, [5, 10, 15, 20])
    ])
    def test_get_move_options(self, d1, d2, expected):
        self.backgammon.dice_one = d1
        self.backgammon.dice_two = d2
        # self.backgammon.move_points = points
        result = self.backgammon.get_move_options()
        self.assertEqual(result, expected)

    @parameterized.expand([
        (board_1, "WHITE", 5, True),
        (board_1, "WHITE", 1, False),
    ])
    def test_can_capture(self, board, current_player, position, expected):
        game = BackgammonGame()
        game.board = board
        game.player = current_player
        result = game.can_capture(position)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (board_1, "WHITE", 0, 0, 1, 0, True),
        (board_1, "WHITE", 0, 0, 11, 0, False),
        (board_1, "WHITE", 0, 0, 2, 0, True)
    ])
    def test_make_move(self, board, current_player, actual_cell, actual_col,
                       new_cell, new_col, expected):
        game = BackgammonGame()
        game.board = board
        game.player = current_player
        result = game.make_move(actual_cell, actual_col,
                                new_cell, new_col)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

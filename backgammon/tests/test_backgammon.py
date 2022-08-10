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

    @parameterized.expand([
        ('WHITE',),
        ('BLACK',),
    ])
    def test_player(self, patch_color):
        with patch('random.choice', return_value=patch_color):
            new_game = BackgammonGame()
            player = new_game.player
        self.assertEqual(player, patch_color)

    @parameterized.expand([
        (1, 2,),
        (2, 3,),
        (3, 4,),
        (4, 6,),
        (5, 5,),
        (6, 1,),
    ])
    @patch('random.randint')
    def test_roll_dices_number_interval(self, first_dice,
                                        second_dice, patch_function):
        patch_function.side_effect = [first_dice, second_dice]
        self.assertEqual(self.backgammon.roll_dices(),
                         (first_dice, second_dice))

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
        (0, 5,)
    ])
    def test_capture_opposite_piece(self, actual_position, new_position):
        game = BackgammonGame()
        game.player = "WHITE"
        game.capture_opposite_piece(actual_position, new_position)
        captured_piece = game.expelled["BLACK"]
        self.assertEqual(1, captured_piece)

    @parameterized.expand([
        (initial_board, 0, 1, 0)
    ])
    def test_change_position(self, board, old_position, new_position, col):
        game = BackgammonGame()
        game.board = board
        game.change_position(old_position, new_position, col)
        self.assertEqual(1, game.board[new_position][col])

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
        (3, 4, [3, 4, 7], 3, [4]),
        (3, 4, [3, 4, 7], 4, [3]),
        (3, 4, [3, 4, 7], 7, []),
        (3, 4, [3], 7, []),
        (3, 4, [4], 7, []),
        (4, 4, [4, 8, 12, 16], 16, []),
        (4, 4, [4, 8, 12, 16], 12, [4]),
        (4, 4, [4, 8, 12, 16], 8, [4, 8]),
        (4, 4, [4, 8, 12, 16], 4, [4, 8, 12]),
        (5, 5, [5, 10, 15], 15, []),
        (5, 5, [5, 10, 15], 10, [5]),
        (5, 5, [5, 10, 15], 5, [5, 10]),
        (6, 6, [6, 12], 6, [6]),
        (6, 6, [6, 12], 12, []),
        (2, 2, [2], 2, []),
    ])
    def test_update_move_options(self, d1, d2, move_options, move,
                                 expectedResult):
        self.backgammon.dice_one = d1
        self.backgammon.dice_two = d2
        self.backgammon.move_options = move_options
        self.backgammon.update_move_options(move)
        self.assertEqual(self.backgammon.move_options, expectedResult)

    @parameterized.expand([
        (board_1, "WHITE", 5, True),
        (board_1, "WHITE", 1, False),
        (board_1, "BLACK", 10, True),
        (board_1, "BLACK", 11, False)
    ])
    def test_can_capture(self, board, current_player, new_position, expected):
        game = BackgammonGame()
        game.board = board
        game.player = current_player
        result = game.can_capture(new_position)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (board_1, "WHITE", 0, 1, 1, 3, True),
        (board_1, "WHITE", 0, 11, 6, 5, False),
        (board_1, "WHITE", 0, 2, 1, 1, True),
        (board_1, "BLACK", 3, 10, 4, 3, True),
        (board_1, "BLACK", 21, 23, 2, 3, True),
        (board_1, "BLACK", 16, 18, 3, 2, False)
    ])
    def test_make_move(self, board, current_player, actual_position,
                       new_position, first_dice, second_dice, expected):
        game = BackgammonGame()
        game.board = board
        game.player = current_player
        game.dice_one = first_dice
        game.dice_two = second_dice
        game.get_move_options()
        result = game.make_move(actual_position, new_position)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

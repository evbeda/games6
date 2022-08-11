import unittest
from parameterized import parameterized
from backgammon.game.backgammon import BackgammonGame
from backgammon.tests.test_scenarios import (
    initial_board,
    board_1,
    board_3,
    next_turn_active,
    next_turn_message_B,
    next_turn_message_W,
    next_turn_message_TIE)
from unittest.mock import patch
from copy import deepcopy
from backgammon.game.constants import BLACK, WHITE
from ..game.constants import TIE, WINNER_BLACK, WINNER_WHITE


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
        (WHITE, initial_board, 0, 11, 16, 18),
        (BLACK, initial_board, 5, 7, 12, 23)
    ])
    def test_available_pieces(self, side, board, *expected_result):
        self.backgammon.board = board
        result = self.backgammon.available_pieces(side)
        self.assertEqual(result, list(expected_result))

    @parameterized.expand([
        (WHITE,),
        (BLACK,),
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
        (WHITE, BLACK),
        (BLACK, WHITE),
    ])
    def test_opposite(self, current_player, expected):

        self.backgammon.player = current_player
        self.assertEqual(self.backgammon.opposite, expected)

    @parameterized.expand(
        [
            (3, BLACK, WHITE),
            (1, WHITE, BLACK),
            (4, WHITE, WHITE),
            (7, WHITE, BLACK),
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
        (BLACK, 0, False),
        (WHITE, 1, True)


    ])
    def test_less_than_two_enemies_in_position(self, current_player, position,
                                               expected_result):
        self.backgammon.player = current_player
        result = self.backgammon.less_than_two_enemies_in_position(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (WHITE, 11, False),
        (WHITE, 16, True),
        (WHITE, 18, False),
        (BLACK, 5, False),
        (BLACK, 12, False),
    ])
    def test_less_than_five_own_pieces(self, current_player,
                                       position, expected):
        self.backgammon.player = current_player
        result = self.backgammon.less_than_five_own_pieces(position)
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (BLACK, 0, False),
            (WHITE, 1, False),
            (WHITE, 11, True),
            (BLACK, 5, True),
        ]
    )
    def test_at_least_one_piece_of_the_player(self, current_player,
                                              position, expected_result):
        self.backgammon.player = current_player
        result = self.backgammon.at_least_one_piece_of_the_player(position)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (BLACK, 2, -1, True),
        (WHITE, 21, 27, True),
        (WHITE, 1, 5, False),
        (WHITE, 5, 6, False),
        (WHITE, 0, 11, False),
        (BLACK, 5, 2, True),
        (BLACK, 12, 7, True),
        (BLACK, 23, 19, True),
        (BLACK, 21, 22, False),
        (BLACK, 23, 18, False),
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
        game.player = WHITE
        game.capture_opposite_piece(actual_position, new_position)
        captured_piece = game.expelled[BLACK]
        self.assertEqual(1, captured_piece)

    @parameterized.expand([
        (initial_board, 0, 1, 0),
        (initial_board, 23, 21, 1)
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
        (board_1, WHITE, 5, True),
        (board_1, WHITE, 1, False),
        (board_1, BLACK, 10, True),
        (board_1, BLACK, 11, False)
    ])
    def test_can_capture(self, board, current_player, new_position, expected):
        game = BackgammonGame()
        game.board = board
        game.player = current_player
        result = game.can_capture(new_position)
        self.assertEqual(result, expected)

    @parameterized.expand([
        (board_1, WHITE, 0, 1, 1, 3, True),
        (board_1, WHITE, 0, 11, 6, 5, False),
        (board_1, WHITE, 0, 2, 1, 1, True),
        (board_1, BLACK, 3, 10, 4, 3, True),
        (board_1, BLACK, 21, 23, 2, 3, True),
        (board_1, BLACK, 16, 18, 3, 2, False),
        (board_3, WHITE, 22, 25, 2, 1, True),
        (board_3, BLACK, 3, -1, 4, 1, True),
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

    @parameterized.expand([  # test check game status
        (6, 8, 20, True),
        (15, 8, 20, False),
        (6, 15, 20, False),
        (6, 8, 20, True),
        (6, 12, 40, False),
        (11, 5, 40, False),
        (11, 11, 40, False),
    ])
    def test_check_game_status(self, black_points, white_points, turn,
                               expected):
        self.backgammon.points[BLACK] = black_points
        self.backgammon.points[WHITE] = white_points
        self.backgammon.current_turn = turn
        self.backgammon.check_game_status()
        self.assertEqual(self.backgammon.active_game, expected)

    @parameterized.expand([
        (15, 8, WINNER_BLACK),
        (15, 15, TIE),
        (6, 15, WINNER_WHITE),
    ])
    def test_get_current_winner(self, black_points, white_points,
                                expected):
        self.backgammon.points[BLACK] = black_points
        self.backgammon.points[WHITE] = white_points
        result = self.backgammon.get_current_winner()
        self.assertEqual(result, expected)

    @parameterized.expand([
        (board_1, WHITE, 3, 2, 1, 3, 1),
        (board_1, BLACK, 1, 1, 1, 21, 2)
    ])
    def test_insert_captured_piece(self, board, current_player,
                                   pieces_captured,
                                   first_dice, second_dice, new_position,
                                   expected):
        game = BackgammonGame()
        game.board = deepcopy(board)
        game.player = current_player
        game.expelled[current_player] = pieces_captured
        game.dice_one = first_dice
        game.dice_two = second_dice
        col = 0 if game.player == WHITE else 1
        result_before = game.board[new_position][col]
        game.insert_captured_piece(new_position)
        self.assertEqual(expected, result_before + 1)

    @parameterized.expand([
        (WHITE, 24, 1),
        (BLACK, 0, 0),
        (BLACK, -1, 1),
        (WHITE, 23, 0)
    ])
    def test_increment_points(self, current_player,
                              new_position, expected):
        game = BackgammonGame()
        game.player = current_player
        game.increment_points(new_position)
        points = game.points[current_player]
        self.assertEqual(points, expected)

    @parameterized.expand([
        (True, 1, 2,
            {
                BLACK: 3, WHITE: 2
            },
            {
                BLACK: 1, WHITE: 0
            }, 20, BLACK, next_turn_active),
        (False, 3, 5,
            {
                BLACK: 15, WHITE: 2
            },
            {
                BLACK: 1, WHITE: 0
            }, 20, BLACK, next_turn_message_B),
        (False, 3, 5,
            {
                BLACK: 10, WHITE: 15
            },
            {
                BLACK: 1, WHITE: 0
            }, 20, BLACK, next_turn_message_W),
        (False, 3, 5,
            {
                BLACK: 15, WHITE: 15
            },
            {
                BLACK: 1, WHITE: 0
            }, 20, WHITE, next_turn_message_TIE),
    ])
    def test_next_turn(self, is_active, first_dice, second_dice, points,
                       captured, turn, current_player, expected):
        self.backgammon.active_game = is_active
        self.backgammon.player = current_player
        self.backgammon.dice_one = first_dice
        self.backgammon.dice_two = second_dice
        self.backgammon.points = points
        self.backgammon.expelled = captured
        self.backgammon.current_turn = turn
        result = self.backgammon.next_turn()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

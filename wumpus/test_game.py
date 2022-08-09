import unittest
from copy import deepcopy

from parameterized import parameterized
from .constants import (GOLD, GOLD_QUANTITY, PLAYER, WUMPUS, WUMPUS_QUANTITY,
                        HOLES_QUANTITY, HOLES)

from wumpus.constants import COL, IN_PROGRESS, ROW
from wumpus.game import WumpusGame

from .scenarios import (SCENARIO_1, SCENARIO_2, SCENARIO_3, SCENARIO_4,
                        SCENARIO_5, SCENARIO_TEST_GOLD,
                        SCENARIO_DANGER_SIGNAL_HOLES,
                        SCENARIO_DANGER_LEFT_DOWN, SCENARIO_DANGER_RIGTH_DOWN,
                        SCENARIO_DANGER_RIGTH_UP, SCENARIO_DANGER_LEFT,
                        SCENARIO_DANGER_RIGTH, SCENARIO_DANGER_UP,
                        SCENARIO_DANGER_DOWN, SCENARIO_TEST_DELETE,
                        SCENARIO_WIN_GOLD)


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

    @parameterized.expand([
        (SCENARIO_1, "J", [(0, 0)]),
        (SCENARIO_2, "J", [(1, 3)]),
        (SCENARIO_3, "J", [(3, 5)]),
        (SCENARIO_4, "J", [])
    ])
    def test_position_finder(self, board, item, expected):
        self.game.board = board
        position_list = self.game.position_finder(item)
        self.assertEqual(position_list, expected)

    @parameterized.expand([
        (0, 0, "s"),
        (1, 3, "w"),
        (3, 5, "a"),
        (3, 5, "d"),
    ])
    def test_is_not_out_of_bounds(self, row, col, direction):
        is_not_out = self.game.is_not_out_of_bounds(row, col, direction)
        self.assertTrue(is_not_out)

    @parameterized.expand([
        (14, 0, "s"),
        (0, 3, "w"),
        (3, 0, "a"),
        (3, 7, "d"),
    ])
    def test_is_out_of_bounds(self, row, col, direction):
        is_out = self.game.is_not_out_of_bounds(row, col, direction)
        self.assertFalse(is_out)

    @parameterized.expand([
        (SCENARIO_1, 7, 0, True),
        (SCENARIO_2, 1, 3, False),
        (SCENARIO_3, 3, 0, True),
        (SCENARIO_4, 3, 6, True),
    ])
    def test_check_is_empty(self, board, row, col, expected):
        self.game.board = board
        is_empty = self.game.check_is_empty(row, col)
        self.assertEqual(is_empty, expected)

    @parameterized.expand([
        (SCENARIO_5, 1, 4),
        (SCENARIO_5, 3, 4),
        (SCENARIO_5, 2, 5),
        (SCENARIO_5, 2, 6)

    ])
    def test_move_transaction(self, board, row, col):
        self.game.board = board
        old_row, old_row = self.game.position_finder("J")[0]
        value_cell = self.game.board[old_row][old_row]
        self.game.move_player_transaction(row, col)
        self.assertEqual(self.game.board[old_row][old_row],
                         value_cell.replace('J', ''))
        self.assertEqual(self.game.board[row][col], "J")

    # @parameterized.expand([
    #     (SCENARIO_1, )
    # ])
    # @patch("random.randint")
    @parameterized.expand([
        (GOLD, GOLD_QUANTITY),
        (WUMPUS, WUMPUS_QUANTITY),
        (HOLES, HOLES_QUANTITY)
    ])
    def test_place_item(self, item, quantity):
        gameTest = WumpusGame()
        gameTest.board = [['' for j in range(COL)] for i in range(ROW)]
        gameTest.place_item(item, quantity)
        self.assertEqual(len(gameTest.position_finder(item)), 8)

    @parameterized.expand([
        (2, 4, True),
        (4, 12, False),
        (4, 5, True),
        (7, 14, True),
        (1, 0, False),
        (0, 0, False),
        (6, 4, True),
        (5, 5, True),
        (7, 0, False),
        (5, 6, False),
    ])
    def test_there_is_gold(self, row, col, expeted):
        game = WumpusGame()
        game.board = SCENARIO_TEST_GOLD
        result = game.there_is_gold(row, col)
        self.assertEqual(result, expeted)

    @parameterized.expand([
        (GOLD, 5, 5, ''),
        (WUMPUS, 7, 8, ''),
        (WUMPUS, 7, 14, ''),
        (GOLD, 2, 10, ''),
        (PLAYER, 3, 4, ''),
    ])
    def test_delete_item(self, item, row, col, expected):
        game = WumpusGame()
        game.board = SCENARIO_TEST_DELETE
        game.delete_item_on_position(item, row, col)
        result = game.board[row][col]
        self.assertEqual(result, expected)

    @parameterized.expand([
        (SCENARIO_DANGER_SIGNAL_HOLES, [(0, 1), (2, 1), (1, 2), (1, 0)]),
        (SCENARIO_DANGER_LEFT_DOWN, [(6, 0), (7, 1)]),
        (SCENARIO_DANGER_RIGTH_DOWN, [(6, 7), (7, 6)]),
        (SCENARIO_DANGER_RIGTH_UP, [(1, 7), (0, 6)]),
        (SCENARIO_DANGER_LEFT, [(3, 0), (5, 0), (4, 1)]),
        (SCENARIO_DANGER_RIGTH, [(3, 7), (5, 7), (4, 6)]),
        (SCENARIO_DANGER_UP, [(1, 4), (0, 5), (0, 3)]),
        (SCENARIO_DANGER_DOWN, [(6, 4), (7, 5), (7, 3)]),
    ])
    def test_find_signal_indicator(self, board, positions):
        self.game.board = board
        self.assertEqual(self.game.find_signal_indicator(HOLES), positions)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_move_and_win_gold(self, row, col):

        game = WumpusGame()
        game.board = deepcopy(SCENARIO_WIN_GOLD)
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_win_gold(row, col)
        new_player_row, new_player_col = game.position_finder(PLAYER)[0]
        self.assertEqual((new_player_row, new_player_col), (row, col))
        self.assertEqual(game.board[old_player_row][old_player_col], '')
        self.assertTrue(GOLD not in game.board[row][col])
        self.assertEqual(len(game.position_finder(GOLD)), 3)

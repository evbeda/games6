import unittest

from parameterized import parameterized
from .constants import (GOLD, GOLD_QUANTITY, WUMPUS, WUMPUS_QUANTITY,
                        HOLES_QUANTITY, HOLES)

from wumpus.constants import COL, IN_PROGRESS, ROW
from wumpus.game import WumpusGame

from .scenarios import (SCENARIO_1, SCENARIO_2, SCENARIO_3, SCENARIO_4,
                        SCENARIO_5)


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
        pos = self.game.position_finder("J")[0]
        self.game.move_player_transaction(row, col)
        self.assertEqual(self.game.board[pos[0]][pos[1]], None)
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
        gameTest.board = [[None for j in range(COL)] for i in range(ROW)]
        gameTest.place_item(item, quantity)
        self.assertEqual(len(gameTest.position_finder(item)), 8)

import unittest
from wumpus.game import WumpusGame
from wumpus.constants import IN_PROGRESS, COL, ROW
from parameterized import parameterized
from .scenarios import SCENARIO_1, SCENARIO_2, SCENARIO_3, SCENARIO_4


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
        ((0, 0), "s"),
        ((1, 3), "w"),
        ((3, 5), "a"),
        ((3, 5), "d"),
    ])
    def test_is_not_out_of_bounds(self, coordinate, direction):
        is_not_out = self.game.is_not_out_of_bounds(coordinate, direction)
        self.assertTrue(is_not_out)

    @parameterized.expand([
        ((14, 0), "s"),
        ((0, 3), "w"),
        ((3, 0), "a"),
        ((3, 7), "d"),
    ])
    def test_is_out_of_bounds(self, coordinate, direction):
        is_out = self.game.is_not_out_of_bounds(coordinate, direction)
        self.assertFalse(is_out)

    @parameterized.expand([
        (SCENARIO_1, (7, 0), True),
        (SCENARIO_2, (1, 3), False),
        (SCENARIO_3, (3, 0), True),
        (SCENARIO_4, (3, 6), True),
    ])
    def test_check_is_empty(self, board, coordinate, expected):
        self.game.board = board
        is_empty = self.game.check_is_empty(coordinate)
        self.assertEqual(is_empty, expected)

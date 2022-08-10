import unittest
from copy import deepcopy

from parameterized import parameterized
from .constants import (GOLD, GOLD_QUANTITY, LOSE, PLAYER, SCORE_GAME, VISITED_CELL, WIN,
                        WUMPUS, WUMPUS_QUANTITY, HOLES_QUANTITY, HOLES, COL,
                        ROW, MOVES, MOVES_DIRECTION)


from wumpus.game import WumpusGame

from .scenarios import (SCENARIO_1, SCENARIO_2, SCENARIO_3, SCENARIO_4,
                        SCENARIO_EATEN_BY_WUMPUS,
                        SCENARIO_MOVE_ACTION,
                        SCENARIO_5,
                        SCENARIO_FALL_IN_HOLES,
                        SCENARIO_TEST_GOLD,
                        SCENARIO_DANGER_SIGNAL_HOLES,
                        SCENARIO_DANGER_LEFT_DOWN, SCENARIO_DANGER_RIGTH_DOWN,
                        SCENARIO_DANGER_RIGTH_UP, SCENARIO_DANGER_LEFT,
                        SCENARIO_DANGER_RIGTH, SCENARIO_DANGER_UP,
                        SCENARIO_DANGER_DOWN, SCENARIO_TEST_DELETE,
                        SCENARIO_WIN_GOLD,
                        SCENARIO_DANGER_COMPLETE_FINAL,
                        SCENARIO_DANGER_COMPLETE_INIT,
                        SCENARIO_DANGER_LEFT_DOWN_INIT,
                        SCENARIO_DANGER_LEFT_DOWN_FINAL,
                        SCENARIO_DANGER_RIGTH_DOWN_INI,
                        SCENARIO_DANGER_RIGTH_DOWN_FINAL,
                        SCENARIO_DANGER_DOWN_INITI,
                        SCENARIO_DANGER_DOWN_FINAL,
                        SCENARIO_CROSS_ELEMENT_INIT,
                        SCENARIO_CROSS_ELEMENT_FINAL,
                        SCENARIO_CROSS_DIF_ELEMENT_INI,
                        SCENARIO_CROSS_DIF_ELEMENT_FIN,
                        SCENARIO_SHOOT_WUMPUS_INIT,
                        SCENARIO_SHOOT_WUMPUS_FINAL,
                        SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT,
                        SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN,
                        SCENARIO_SHOOT_FAIL_INIT)


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = WumpusGame()

    def test_initial_game(self):
        self.assertEqual(self.game.is_playing, True)

    def test_board_columns(self):
        for row in self.game.board:
            self.assertEqual(len(row), COL)

    def test_board_rows(self):
        self.assertEqual(len(self.game.board), ROW)

    def test_initial_place_player(self):
        self.game.place_player()
        self.assertEqual(self.game.board[0][0], PLAYER)

    @parameterized.expand([
        (SCENARIO_1, PLAYER, [(0, 0)]),
        (SCENARIO_2, PLAYER, [(1, 3)]),
        (SCENARIO_3, PLAYER, [(3, 5)]),
        (SCENARIO_4, PLAYER, [])
    ])
    def test_position_finder(self, board, item, expected):
        self.game.board = board
        position_list = self.game.position_finder(item)
        self.assertEqual(position_list, expected)

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
        old_row, old_row = self.game.position_finder(PLAYER)[0]
        value_cell = self.game.board[old_row][old_row]
        self.game.move_player_transaction(row, col)
        self.assertEqual(self.game.board[old_row][old_row],
                         value_cell.replace(PLAYER, ''))
        self.assertEqual(self.game.board[row][col], PLAYER)

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
        self.assertEqual(game.board[old_player_row][old_player_col], VISITED_CELL)
        self.assertTrue(GOLD not in game.board[row][col])
        self.assertEqual(len(game.position_finder(GOLD)), 3)

    @parameterized.expand([
        (SCENARIO_DANGER_DOWN_INITI, WUMPUS, SCENARIO_DANGER_DOWN_FINAL),
        (SCENARIO_DANGER_COMPLETE_INIT, HOLES, SCENARIO_DANGER_COMPLETE_FINAL),
        (SCENARIO_DANGER_LEFT_DOWN_INIT, WUMPUS,
            SCENARIO_DANGER_LEFT_DOWN_FINAL),
        (SCENARIO_DANGER_RIGTH_DOWN_INI, WUMPUS,
            SCENARIO_DANGER_RIGTH_DOWN_FINAL),
        (SCENARIO_CROSS_ELEMENT_INIT, WUMPUS,
            SCENARIO_CROSS_ELEMENT_FINAL),
        (SCENARIO_CROSS_ELEMENT_INIT, WUMPUS,
            SCENARIO_CROSS_ELEMENT_FINAL)
    ])
    def test_print_signals(self, board_init, item, final_board):
        test_game = WumpusGame()
        test_game.board = board_init
        test_game.print_signals(item)
        self.assertEqual(test_game.board, final_board)

    def test_print_signals_dif(self):
        test_game = WumpusGame()
        test_game.board = SCENARIO_CROSS_DIF_ELEMENT_INI
        test_game.print_signals(HOLES)
        test_game.print_signals(WUMPUS)
        self.assertEqual(test_game.board, SCENARIO_CROSS_DIF_ELEMENT_FIN)

    @parameterized.expand([
        (1000, 2000, SCORE_GAME["gold_wumpus"]),
        (0, -10, SCORE_GAME["move"]),
        (1000, 950, SCORE_GAME["lost_shoot"])
    ])
    def test_score_manager(self, initial_score, final_score, score):
        self.game.score = initial_score
        self.game.modify_score(score)
        self.assertEqual(final_score, self.game.score)

    @parameterized.expand([
        (WIN),
        (LOSE),
    ])
    def test_game_over(self, result):
        game = WumpusGame()
        game.game_over(result)
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, result)

    @parameterized.expand([  # parameters of shoot_arrow
        (SCENARIO_SHOOT_WUMPUS_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_WUMPUS_FINAL, 2000),
        (SCENARIO_SHOOT_WUMPUS_SIGNAL_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_WUMPUS_SIGNAL_FIN, 2000),
        (SCENARIO_SHOOT_FAIL_INIT, 1000, 4, 4,
         SCENARIO_SHOOT_FAIL_INIT, 950)
    ])
    def test_shoot_arrow(self, initial_board, initial_score,
                         row, col, final_board, final_score):
        self.game.board = initial_board
        self.game.score = initial_score
        self.game.shoot_arrow(row, col)
        self.assertEqual(self.game.board, final_board)
        self.assertEqual(self.game.score, final_score)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_fall_in_hole(self, row, col):

        game = WumpusGame()
        game.board = deepcopy(SCENARIO_FALL_IN_HOLES)

        content_destination_cell = game.board[row][col]
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_game_over(row, col)
        player_in_board = game.position_finder(PLAYER)

        self.assertEqual(game.board[old_player_row][old_player_col], VISITED_CELL)
        self.assertEqual(game.board[row][col], content_destination_cell)
        self.assertEqual(player_in_board, [])
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, LOSE)

    @parameterized.expand([
        (5, 4),
        (5, 6),
        (4, 5),
        (6, 5),
    ])
    def test_eaten_by_wumpus(self, row, col):

        game = WumpusGame()
        game.board = deepcopy(SCENARIO_EATEN_BY_WUMPUS)
        content_destination_cell = game.board[row][col]
        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_and_game_over(row, col)
        player_in_board = game.position_finder(PLAYER)

        self.assertEqual(game.board[old_player_row][old_player_col], VISITED_CELL)
        self.assertEqual(game.board[row][col], content_destination_cell)
        self.assertEqual(player_in_board, [])
        self.assertEqual(game.is_playing, False)
        self.assertEqual(game.result_of_game, LOSE)

    @parameterized.expand([

        (5, 4, WUMPUS, True),
        (5, 6, WUMPUS, False),
        (5, 6, HOLES, True),
        (4, 5, HOLES, False),
        (4, 5, GOLD, True),
        (6, 5, GOLD, False),
    ])
    def test_is_there_item(self, row, col, item, expected):

        game = WumpusGame()
        game.board = deepcopy(SCENARIO_MOVE_ACTION)
        game.there_is_item(item, row, col)

    @parameterized.expand([
        ("s", 0, 0, (1, 0)),
        ("w", 0, 0, ()),
        ("w", 1, 1, (0, 1)),
        ("a", 0, 0, ()),
        ("a", 1, 1, (1, 0)),
        ("d", 0, 0, (0, 1)),
        ("y", 0, 0, ()),
        ("s", 7, 7, ()),
    ])
    def test_find_coord(self, direction, row, col, final_coord):
        game = WumpusGame()
        game.board[0][0] = ""
        game.board[row][col] = "J"
        final_dir = game.find_coord(direction)
        self.assertEqual(final_dir, final_coord)

    @parameterized.expand([  # test with correct moves
        (MOVES["move"], MOVES_DIRECTION["south"], 0, 0, 1, 0, -10),
        (MOVES["move"], MOVES_DIRECTION["east"], 0, 0, 0, 1, -10),
        (MOVES["move"], MOVES_DIRECTION["north"], 1, 1, 0, 1, -10),
        (MOVES["move"], MOVES_DIRECTION["south"], 1, 1, 2, 1, -10),
        (MOVES["shoot"], MOVES_DIRECTION["east"], 0, 0, 0, 0, -50),
        (MOVES["shoot"], MOVES_DIRECTION["north"], 1, 1, 1, 1, -50),
        (MOVES["shoot"], MOVES_DIRECTION["west"], 1, 1, 1, 1, -50),
    ])
    def test_admin_move(self, accion, direccion, row, col,
                        final_row, final_col, expected_score):
        self.game.board = [["" for j in range(COL)] for i in range(ROW)]
        self.game.board[row][col] = "J"
        self.game.score = 0
        self.game.manager_move(accion, direccion)
        position_player = self.game.position_finder(PLAYER)
        self.assertEqual(self.game.score, expected_score)
        self.assertEqual(position_player[0], (final_row, final_col))

    @parameterized.expand([  # test exceptions moves
        (MOVES["shoot"], MOVES_DIRECTION["north"], 0, 0),
        (MOVES["shoot"], MOVES_DIRECTION["south"], 7, 7),
        (MOVES["shoot"], MOVES_DIRECTION["east"], 7, 7),
        (MOVES["shoot"], MOVES_DIRECTION["west"], 7, 0),
    ])
    def test_admin_move_exceptions_shoot(self, accion, direccion, row, col):
        self.game.board = [["" for j in range(COL)] for i in range(ROW)]
        self.game.board[row][col] = "J"
        self.game.score = 0
        with self.assertRaises(Exception):
            self.game.manager_move(accion, direccion)

    @parameterized.expand([  # test exceptions moves
        (MOVES["move"], MOVES_DIRECTION["north"], 0, 0),
        (MOVES["move"], MOVES_DIRECTION["south"], 7, 7),
        (MOVES["move"], MOVES_DIRECTION["east"], 7, 7),
        (MOVES["move"], MOVES_DIRECTION["west"], 7, 0),
    ])
    def test_admin_move_exceptions(self, accion, direccion, row, col):
        self.game.board = [["" for j in range(COL)] for i in range(ROW)]
        self.game.board[row][col] = "J"
        self.game.score = 0
        with self.assertRaises(Exception):
            self.game.manager_move(accion, direccion)

    @parameterized.expand([
        (5, 4, WUMPUS, False),
        (5, 6, HOLES, False),
        (4, 5, PLAYER, True),
        (6, 5, PLAYER, True),
    ])
    def test_move_action(self, row, col, expeted_item, is_playing):

        game = WumpusGame()
        game.board = deepcopy(SCENARIO_MOVE_ACTION)

        old_player_row, old_player_col = game.position_finder(PLAYER)[0]
        game.move_player(row, col)

        self.assertEqual(game.board[old_player_row][old_player_col], VISITED_CELL)
        self.assertEqual(game.board[row][col], expeted_item)
        self.assertEqual(game.is_playing, is_playing)

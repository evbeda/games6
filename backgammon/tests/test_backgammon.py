import unittest
from parameterized import parameterized
from backgammon.game.backgammon import BackgammonGame
from backgammon.tests.test_scenarios import initial_board
from unittest.mock import patch


class BackgammonGameTest(unittest.TestCase):

    def setUp(self):
        self.backgammon = BackgammonGame()

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

    @patch('random.randint', return_value=1)
    def test_player_1(self, patched_randint):
        player = BackgammonGame.select_initial_player()
        self.assertEqual(player, 1)

    @patch('random.randint', return_value=2)
    def test_player_2(self, patched_randint):
        player = BackgammonGame.select_initial_player()
        self.assertEqual(player, 2)


if __name__ == '__main__':
    unittest.main()

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

    @patch('random.choice', return_value='WHITE')
    def test_player_1(self, patched_randint):
        player = BackgammonGame.select_initial_player()
        self.assertEqual(player, 'WHITE')

    @patch('random.choice', return_value='BLACK')
    def test_player_2(self, patched_randint):
        player = BackgammonGame.select_initial_player()
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
    def test_current_turn(self, it, expected,
                          patch_value, patch_function):
        patch_function.return_value = patch_value
        game = BackgammonGame()
        for _ in range(it):
            game.next_turn()
        self.assertEqual(expected, game.player)


if __name__ == '__main__':
    unittest.main()

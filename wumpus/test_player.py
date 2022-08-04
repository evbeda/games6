import unittest
from parameterized import parameterized
from wumpus.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.row = 5
        self.player.col = 10

    @parameterized.expand([
        ("s", 6, 10),
        ("w", 4, 10),
        ("d", 5, 11),
        ("a", 5, 9),


    ])
    def test_valid_move(self, movement, expected_row, expected_col):
        self.player.move(movement)
        self.assertEqual(self.player.row, expected_row)
        self.assertEqual(self.player.col, expected_col)

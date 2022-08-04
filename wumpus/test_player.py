import unittest
from parameterized import parameterized
from wumpus.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    @parameterized.expand([
        ("s", [1, 0]),
        ("d", [0, 1]),
        ("w", [0, 0]),
        ("a", [0, 0])
    ])
    def test_valid_move(self, movement, expected_movement):
        self.player.move(movement)
        self.assertEqual([self.player.row, self.player.col], expected_movement)

import unittest
from wumpus.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_move_s(self):
        self.player.move("s")
        self.assertEqual(self.player.row, 1)

    def test_move_d(self):
        self.player.move("d")
        self.assertEqual(self.player.col, 1)

    def test_move_w(self):
        self.player.row = 1
        self.player.move("w")
        self.assertEqual(self.player.row, 0)

    def test_move_a(self):
        self.player.col = 1
        self.player.move("a")
        self.assertEqual(self.player.col, 0)

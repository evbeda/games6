import unittest
from parameterized import parameterized
from ..game.moves import new_positon_check


class Moves_test(unittest.TestCase):

    @parameterized.expand(
        [
            (1, 1, True),  # empty space
            (1, 2, True),  # only one oponent piece
            (1, 5, False),  # oponent defended position
            (1, 11, False),  # full family pieces
            (20, 5, True),  # border table dades
            (20, 6, True),
            (24, 6, False),
        ])
    def test_new_position_check(self, position, dice, flag):
        # initial_position ,board, daces
        board = [
            [0, 0],
            [2, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [0, 0], [3, 0],
            [0, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 2]]

        result = new_positon_check(board, position, dice)
        self.assertEqual(flag, result)

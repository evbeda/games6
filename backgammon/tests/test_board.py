import unittest
from parameterized import parameterized
from ..game.board import create_board, available_pieces


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.expected_board = [
            [0, 0],
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [0, 0], [3, 0],
            [0, 0], [5, 0], [0, 0], [0, 0], [0, 0], [0, 2]]

        self.create_board = create_board()

    def test_slots(self):
        self.assertEqual(len(self.create_board), 25)

    def test_initial_board(self):
        self.assertListEqual(self.expected_board, self.create_board)

    @parameterized.expand(
        [
            ("W", [1, 12, 18, 20]),
            ("B", [6, 8, 13, 24])]
    )
    def test_availabel_pieces(self, side, expected):
        result = available_pieces(self.expected_board, side)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

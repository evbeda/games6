import unittest
from .create_board import create_board


class BoardTest(unittest.TestCase):

    def test_slots(self):
        board = create_board()
        self.assertEqual(len(board), 24)


if __name__ == '__main__':
    unittest.main()

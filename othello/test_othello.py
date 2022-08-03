import unittest
from othello.othello_game import Othello
from parameterized import parameterized


class Test_othello(unittest.TestCase):

    def setUp(self):
        self.game = Othello()
        self.board = self.game.init_board

    def test_board_size(self):
        self.assertEqual(len(self.board), 8)
        for row in self.board:
            self.assertEqual(len(row), 8)

    # 0 is a black win, 1 is a white win, None there are still moves available
    @parameterized.expand([
        ([
            ["B", "W", "W", "W", "W", "B", "W", "W"],
            ["B", "B", "B", "W", "W", "W", "W", "W"],
            ["B", "W", "B", "W", "W", "W", "B", "W"],
            ["B", "B", "B", "W", "W", "W", "W", "B"],
            ["B", "B", "B", "W", "B", "B", "W", "B"],
            ["B", "B", "W", "B", "W", "B", "B", "B"],
            ["B", "B", "B", "W", "W", "B", "B", "B"],
            ["B", "W", "B", "B", "B", "B", "B", "B"]], 37, 27)
    ])
    def test_pieces_count(self, final_board, expected_black, expected_white):
        result = Othello.pieces_count(final_board)
        self.assertEqual(result[0], expected_black)
        self.assertEqual(result[1], expected_white)


if __name__ == "__main__":
    unittest.main()

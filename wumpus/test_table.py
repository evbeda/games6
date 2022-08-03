import unittest
from wumpus.table import Table


class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = Table(8, 15)
        self.col = 15
        self.row = 8

    def test_create_table(self):
        table = Table(2, 3)
        self.assertEqual([[None, None, None], [None, None, None]], table.board)

    def test_creat_real_table(self):
        self.assertEqual([8, 15], [len(self.table.board), len(self.table.board[0])])

    def test_board_columns(self):
        flag = True
        for row in self.table.board:
            if len(row) != self.col:
                flag = False
        self.assertTrue(flag)

    def test_board_rows(self):
        self.assertTrue(len(self.table.board) == self.row)

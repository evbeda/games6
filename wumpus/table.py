class Table:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = [[None for j in range(col)] for i in range(row)]

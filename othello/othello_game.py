
class Othello():

    def __init__(self):
        self.possibles_players = ['B', 'W']
        self.player_turn = self.possibles_players[0]
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, "W", "B", None, None, None],
            [None, None, None, "B", "W", None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]

    def get_piece_count(self, board, kind):
        return sum(
            [ficha == kind for row in board for ficha in row])

    def next_turn(self):
        self.player_turn = self.get_opposite_piece()

    def what_is(self, row, col):
        return self.board[row][col]

    def is_empty(self, row, col):
        value = self.what_is(row, col)
        return value is None

    def get_opposite_piece(self):
        aux = self.possibles_players.copy()
        aux.remove(self.player_turn)
        return aux[0]

    def get_index_limit(self, i):
        if i == 0:

            from_i = i
            to_i = i + 1

        elif i == 7:
            from_i = i - 1
            to_i = i
        else:
            from_i = i - 1
            to_i = i + 1
        return from_i, to_i

    def get_limits(self, row, col):

        from_row, to_row = self.get_index_limit(row)
        from_col, to_col = self.get_index_limit(col)

        return {
            'from_row': from_row,
            'to_row': to_row,
            'from_col': from_col,
            'to_col': to_col}

    def close_opposite_around(self, row, col):
        limits = self.get_limits(row, col)
        close_opposite_list = []
        for i in range(limits["from_row"], limits["to_row"] + 1):
            for j in range(limits["from_col"], limits["to_col"] + 1):
                if self.what_is(i, j) == self.get_opposite_piece():
                    close_opposite_list.append((i, j))
        return close_opposite_list

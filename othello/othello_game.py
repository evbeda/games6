
class Othello():

    def __init__(self):
        self.possibles_players = ['B', 'W']
        self.player_turn = self.possibles_players[0]
        self.init_board = [
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
        return self.init_board[row][col]

    def is_empty(self, row, col):
        value = self.what_is(row, col)
        return value is None

    def get_opposite_piece(self):
        aux = self.possibles_players.copy()
        aux.remove(self.player_turn)
        return aux[0]

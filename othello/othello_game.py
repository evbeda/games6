
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
        aux = self.possibles_players.copy()
        aux.remove(self.player_turn)
        self.player_turn = aux[0]

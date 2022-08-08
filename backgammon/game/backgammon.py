class BackgammonGame():

    def __init__(self):
        self.board = [
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
            [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
        ]
        self.expelled = {"BLACK": 0, "WHITE": 0}

    def available_pieces(self, side):
        color = 0 if side == "WHITE" else 1
        result = []
        for index, pyramid in enumerate(self.board):
            if pyramid[color]:
                result.append(index)
        return result

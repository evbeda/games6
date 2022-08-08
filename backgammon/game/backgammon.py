import random


class BackgammonGame():

    def __init__(self):
        self.board = [
            [2, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 5],
            [0, 0], [0, 3], [0, 0], [0, 0], [0, 0], [5, 0],
            [0, 5], [0, 0], [0, 0], [0, 0], [3, 0], [0, 0],
            [5, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 2]
        ]
        self.expelled = {"BLACK": 0, "WHITE": 0}
        self.player = BackgammonGame.select_initial_player()

    def available_pieces(self, side):
        color = 0 if side == "WHITE" else 1
        result = []
        for index, pyramid in enumerate(self.board):
            if pyramid[color]:
                result.append(index)
        return result

    def select_initial_player():
        player = random.randint(1, 2)
        return player

    def roll_dices(self):

        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        return (dice_one, dice_two)

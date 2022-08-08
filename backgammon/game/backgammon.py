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
        self.active_game = True

    def available_pieces(self, side):
        color = 0 if side == "WHITE" else 1
        result = []
        for index, pyramid in enumerate(self.board):
            if pyramid[color]:
                result.append(index)
        return result

    # if there are no movements, the game must finish
    def game_active_change(self):
        self.active_game = False

    def select_initial_player():
        player = random.choice(['WHITE', 'BLACK'])
        return player

    def roll_dices(self):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        return (dice_one, dice_two)

    @property
    def opposite(self):
        return 'BLACK' if self.player == 'WHITE' else 'WHITE'

    def next_turn(self):
        self.player = self.opposite

    def less_than_two_enemies_in_position(self, position):
        index_opp = 0 if self.opposite == "WHITE" else 1
        result = True if self.board[position][index_opp] < 2 else False
        return result

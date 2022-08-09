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
        self.player = random.choice(['WHITE', 'BLACK'])
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

    def roll_dices(self):
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)
        return (dice_one, dice_two)

    @property
    def opposite(self):
        return 'BLACK' if self.player == 'WHITE' else 'WHITE'

    def change_active_player(self):
        self.player = self.opposite

    def less_than_two_enemies_in_position(self, position):
        index_opp = 0 if self.opposite == "WHITE" else 1
        result = True if self.board[position][index_opp] < 2 else False
        return result

    def less_than_five_own_pieces(self, position):
        side = 0 if self.player == "WHITE" else 1
        return self.board[position][side] < 5

    def at_least_one_piece_of_the_player(self, position):
        player_piece = 0 if self.player == "WHITE" else 1
        if not self.board[position][player_piece]:
            return False
        return True

    def is_valid_move(self, initial_pos, final_pos) -> bool:

        enenmy_condition = self.less_than_two_enemies_in_position(final_pos)
        own_condition = (self.less_than_five_own_pieces(final_pos) and
                         self.at_least_one_piece_of_the_player(initial_pos))

        return enenmy_condition and own_condition

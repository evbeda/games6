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
        self.dice_one = 0
        self.dice_two = 0

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

    # Modified dices mechanism
    def roll_dices(self):
        self.dice_one = random.randint(1, 6)
        self.dice_two = random.randint(1, 6)
        return (self.dice_one, self.dice_two)

    @property
    def move_points(self):
        '''Determines the different move options the player has, based on "move points", which is based on the
        rolled dices.
        returns a list of the possible moves a player can make, based only on the move points.'''
        if self.dice_one != self.dice_two:
            return [self.dice_one, self.dice_two]
        else:
            return [self.dice_one, self.dice_two, self.dice_one, self.dice_two]

    def get_move_options(self):
        '''Determines the move options based ONLY on the dices.
        Should be used only once per turn'''
        d1 = self.dice_one
        d2 = self.dice_two
        move_options = []
        if len(self.move_points) == 2:
            move_options = [d1, d2, d1 + d2]
            move_options = list(set(move_options))
        elif len(self.move_points) == 4:
            move_options = [d1, d1 * 2, d1 * 3, d1 * 4]
        return move_options

    '''
    def update_move_options(self, move):
        Updates the move options remaining, based on the last move

        return True
    '''

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

    def capture_opposite_piece(self, position):
        inter_position_player = 0 if self.player == "WHITE" else 1
        inter_position_to_capture = 1 if self.player == "WHITE" else 0
        self.board[position][inter_position_player] += 1
        self.board[position][inter_position_to_capture] -= 1
        self.expelled[self.opposite] += 1

    def change_position(self, actual_row, actual_col, new_row, new_col):
        self.board[actual_row][actual_col] -= 1
        self.board[new_row][new_col] += 1

    def can_capture(self, position):
        opposite_piece = 1 if self.player == "WHITE" else 0
        return self.board[position][opposite_piece] == 1

    def make_move(self, actual_cell, actual_col, new_cell, new_col):
        if (
            self.is_valid_move(actual_cell, new_cell)
            and self.can_capture(new_cell)
        ):
            self.capture_opposite_piece(new_cell)
            return True
        elif self.is_valid_move(actual_cell, new_cell):
            self.change_position(actual_cell, actual_col, new_cell, new_col)
            return True
        return False

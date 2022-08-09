from wumpus.constants import (
    IN_PROGRESS,
    COL,
    ROW,
    SWORDS_QUANTITY
)


class WumpusGame:

    def __init__(self) -> None:
        self.state = IN_PROGRESS
        self.board = [[None for j in range(COL)] for i in range(ROW)]
        self.place_player()
        self.swords = SWORDS_QUANTITY
        self.collected_gold = 0

    def place_player(self):
        self.board[0][0] = "J"

    def position_finder(self, item):
        position_list = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == item:
                    position_list.append((i, j))
        return position_list

    def is_not_out_of_bounds(self, row, col, direction):
        validator = True
        if direction == "w" and not row > 0:
            validator = False
        if direction == "s" and not row < 14:
            validator = False
        if direction == "a" and not col > 0:
            validator = False
        if direction == "d" and not col < 7:
            validator = False
        return validator

    def check_is_empty(self, row, col):
        cell = self.board[row][col]
        return cell is None

    def move_player_transaction(self, row, col):
        pos = self.position_finder("J")[0]
        self.board[row][col] = "J"
        self.board[pos[0]][pos[1]] = None

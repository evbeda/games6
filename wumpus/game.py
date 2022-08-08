from wumpus.constants import IN_PROGRESS, COL, ROW


class WumpusGame:

    def __init__(self) -> None:
        self.state = IN_PROGRESS
        self.board = [[None for j in range(COL)] for i in range(ROW)]

    def place_player(self):
        self.board[0][0] = "J"

    def position_finder(self, item):
        position_list = []
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == item:
                    position_list.append((i, j))
        return position_list

    def is_not_out_of_bounds(self, coordinate, direction):
        validator = True
        if direction == "w" and not coordinate[0] > 0:
            validator = False
        if direction == "s" and not coordinate[0] < 14:
            validator = False
        if direction == "a" and not coordinate[1] > 0:
            validator = False
        if direction == "d" and not coordinate[1] < 7:
            validator = False
        return validator

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

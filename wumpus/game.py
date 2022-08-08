from wumpus.constants import (
    IN_PROGRESS,
    COL,
    ROW,
    GOLD_QUANTITY,
    GOLD,
    WUMPUS_QUANTITY,
    WUMPUS,
    SWORDS_QUANTITY
)
import random


class WumpusGame:

    def __init__(self) -> None:
        self.state = IN_PROGRESS
        self.board = [[None for j in range(COL)] for i in range(ROW)]
        self.player = self.place_player()
        self.gold = self.place_item(GOLD, GOLD_QUANTITY)
        self.wumpus = self.place_item(WUMPUS, WUMPUS_QUANTITY)
        self.swords = SWORDS_QUANTITY
        self.collected_gold = 0

    def place_player(self):
        self.board[0][0] = "J"

    def place_item(self, item, quantity):
        for _ in range(quantity - 1):
            while True:  # busca hasta encontrar una posicion libre
                row = random.randint(0, ROW - 1)
                col = random.randint(0, COL - 1)
                if self.check_is_empty((row, col)):
                    self.board[row][col] = item
                    break

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

    def check_is_empty(self, coordinate):
        cell = self.board[coordinate[0]][coordinate[1]]
        return True if cell is None else False

    def move_J_transaction(self, coordinate):
        pos = self.position_finder("J")[0]
        self.board[coordinate[0]][coordinate[1]] = "J"
        self.board[pos[0]][pos[1]] = None

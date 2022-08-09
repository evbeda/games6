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
        self.board = [['' for j in range(COL)] for i in range(ROW)]
        self.player = self.place_player()
        self.gold = self.place_item(GOLD, GOLD_QUANTITY)
        self.wumpus = self.place_item(WUMPUS, WUMPUS_QUANTITY)
        self.swords = SWORDS_QUANTITY
        self.collected_gold = 0

    def place_player(self):
        self.board[0][0] = "J"

    def place_item(self, item, quantity):
        for _ in range(quantity):
            while True:  # busca hasta encontrar una posicion libre
                row = random.randint(0, ROW - 1)
                col = random.randint(0, COL - 1)
                if self.check_is_empty(row, col):
                    self.board[row][col] = item
                    break

    def position_finder(self, item):
        position_list = []
        for i in range(ROW):
            for j in range(COL):
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
        return cell == ''

    def move_player_transaction(self, new_row, new_col):

        row, col = self.position_finder("J")[0]
        self.board[row][col] = self.board[row][col].replace('J', '')
        self.board[new_row][new_col] += "J"

    def there_is_gold(self, row: int, col: int) -> bool:
        return (row, col) in self.position_finder(GOLD)

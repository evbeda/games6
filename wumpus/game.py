from wumpus.constants import (
    COL,
    LOSE,
    ROW,
    GOLD_QUANTITY,
    GOLD,
    WUMPUS_QUANTITY,
    WUMPUS,
    SWORDS_QUANTITY,
    PLAYER,
    ITEMS_DICTIONARY,
    SCORE_GAME
)
import random


class WumpusGame:

    def __init__(self) -> None:
        self.is_playing = True
        self.board = [['' for j in range(COL)] for i in range(ROW)]
        self.player = self.place_player()
        self.gold = self.place_item(GOLD, GOLD_QUANTITY)
        self.wumpus = self.place_item(WUMPUS, WUMPUS_QUANTITY)
        self.swords = SWORDS_QUANTITY
        self.collected_gold = 0

        self.score = 0
        self.result_of_game = str()

    def place_player(self):
        self.board[0][0] = PLAYER

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

    def check_is_empty(self, row, col):
        cell = self.board[row][col]
        return cell == ''

    def move_player_transaction(self, new_row, new_col):

        row, col = self.position_finder(PLAYER)[0]
        self.delete_item_on_position(PLAYER, row, col)
        self.board[new_row][new_col] += PLAYER
        self.modify_score(SCORE_GAME["move"])

    def there_is_gold(self, row: int, col: int) -> bool:
        return (row, col) in self.position_finder(GOLD)

    def delete_item_on_position(self, item, row, col):
        self.board[row][col] = self.board[row][col].replace(item, '')

    def _posible_position(self, row, col):
        positions = {
            "nort": (row - 1, col),
            "sout": (row + 1, col),
            "east": (row, col + 1),
            "west": (row, col - 1)
        }

        if row - 1 < 0:
            del (positions['nort'])
        if row + 1 > 7:
            del (positions['sout'])
        if col + 1 > 7:
            del (positions['east'])
        if col - 1 < 0:
            del (positions['west'])

        return list(positions.values())

    def find_signal_indicator(self, item):
        position_items = self.position_finder(item)
        position_signals = []
        for pos in position_items:
            list_int = self._posible_position(pos[0], pos[1])
            for tuple in list_int:
                position_signals.append(tuple)
        return position_signals

    def move_and_win_gold(self, row, col):
        self.delete_item_on_position(GOLD, row, col)
        self.move_player_transaction(row, col)
        self.modify_score(SCORE_GAME["gold_wumpus"])
        self.modify_score(SCORE_GAME["move"])

    def move_and_game_over(self, row, col):
        self.move_player_transaction(row, col)
        self.delete_item_on_position(PLAYER, row, col)
        self.game_over(LOSE)

    def print_signals(self, item):
        positions = self.find_signal_indicator(item)
        for row, col in positions:
            if ITEMS_DICTIONARY[item] not in self.board[row][col]:
                self.board[row][col] += ITEMS_DICTIONARY[item]

    def modify_score(self, score_to_modify):
        self.score += score_to_modify

    def game_over(self, result: str):
        self.is_playing = False
        self.result_of_game = result

    def shoot_arrow(self, row, col):
        if WUMPUS in self.board[row][col]:
            self.delete_item_on_position(WUMPUS, row, col)
            self.modify_score(SCORE_GAME["gold_wumpus"])
        else:
            self.modify_score(SCORE_GAME["lost_shoot"])

    def find_coord(self, coord):
        row, col = self.position_finder(PLAYER)[0]
        if coord == "w" and row - 1 >= 0:
            return (row - 1, col)
        elif coord == "s" and row + 1 <= 7:
            return (row + 1, col)
        elif coord == "a" and col - 1 >= 0:
            return (row, col - 1)
        elif coord == "d" and col + 1 <= 7:
            return (row, col + 1)
        else:
            return ()

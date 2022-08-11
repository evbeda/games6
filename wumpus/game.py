from wumpus.constants import (
    COL,
    HIDE_CELL,
    HOLES,
    LOSE,
    ROW,
    GOLD_QUANTITY,
    GOLD,
    VISITED_CELL,
    WUMPUS_QUANTITY,
    WUMPUS,
    SWORDS_QUANTITY,
    PLAYER,
    ITEMS_DICTIONARY,
    SCORE_GAME,
    MOVES,
    MESSAGE_NEXT_TURN,
    MESSAGE_GAME_OVER
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
        self.board[row][col] = VISITED_CELL
        self.board[new_row][new_col] += PLAYER
        self.modify_score(SCORE_GAME["move"])

    def there_is_item(self, item, row: int, col: int) -> bool:
        return (row, col) in self.position_finder(item)

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
            self.board[row][col] = VISITED_CELL
            self.modify_score(SCORE_GAME["gold_wumpus"])
        else:
            self.modify_score(SCORE_GAME["lost_shoot"])

    def move_player(self, row: int, col: int):

        if self.there_is_item(GOLD, row, col):
            self.move_and_win_gold(row, col)

        elif (self.there_is_item(WUMPUS, row, col) or
              self.there_is_item(HOLES, row, col)):
            self.move_and_game_over(row, col)

        else:
            self.move_player_transaction(row, col)

    def find_coord(self, coord):
        row, col = self.position_finder(PLAYER)[0]
        result = ()
        if coord == "w" and row - 1 >= 0:
            result = (row - 1, col)
        elif coord == "s" and row + 1 <= 7:
            result = (row + 1, col)
        elif coord == "a" and col - 1 >= 0:
            result = (row, col - 1)
        elif coord == "d" and col + 1 <= 7:
            result = (row, col + 1)
        return result

    def manager_move(self, action, direction):
        directions = self.find_coord(direction)
        if action == MOVES['move'] and directions:
            self.move_player(directions[0], directions[1])
        elif action == MOVES['shoot'] and directions:
            self.shoot_arrow(directions[0], directions[1])
        else:
            raise Exception("Out of range move")

    def find_signal(self, item, row, col):
        item_array = list(item)
        positions = self._posible_position(row, col)
        wumpus_flag = False
        hole_flag = False
        for p_row, p_col in positions:
            if WUMPUS in self.board[p_row][p_col]:
                wumpus_flag = True
            if HOLES in self.board[p_row][p_col]:
                hole_flag = True
        if wumpus_flag:
            item_array[2] = "+"
        if hole_flag:
            item_array[0] = "~"
        return "".join(item_array)

    def parse_cell(self, row: int, col: int) -> str:
        cell = self.board[row][col]

        if cell == PLAYER or cell == VISITED_CELL:
            cell = ' ' + cell + ' '
            cell = self.find_signal(cell, row, col)

        else:
            cell = HIDE_CELL

        return cell

    def next_turn(self):
        result = ""
        if self.is_playing:
            result = MESSAGE_NEXT_TURN
        else:
            result = MESSAGE_GAME_OVER + str(self.score)
        return result

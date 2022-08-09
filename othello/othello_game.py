
class Othello():

    def __init__(self):
        self.possibles_players = ['B', 'W']
        self.player_turn = self.possibles_players[0]
        self.board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, "W", "B", None, None, None],
            [None, None, None, "B", "W", None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
        ]
        self.black_can_play = True
        self.white_can_play = True
        self.is_playing = True

    def get_piece_count(self, kind):
        return sum(
            [ficha == kind for row in self.board for ficha in row])

    def next_turn(self):
        self.player_turn = self.get_opposite_piece()

    def what_is(self, row, col):
        return self.board[row][col]

    def is_empty(self, row, col):
        value = self.what_is(row, col)
        return value is None

    def get_opposite_piece(self):
        aux = self.possibles_players.copy()
        aux.remove(self.player_turn)
        return aux[0]

    # def get_index_limit(self, i):
    #     '''
    #     Argument i is an index'''
    #     if i == 0:

    #         from_i = i
    #         to_i = i + 1

    #     elif i == 7:
    #         from_i = i - 1
    #         to_i = i
    #     else:
    #         from_i = i - 1
    #         to_i = i + 1
    #     return from_i, to_i

    # def get_limits(self, row, col):
    #     '''
    #     Returns a dictionary with 4 values, which are the coordinates of
    #     edges that define a square.
    #     It can be a 3x3, 2x3 or 3x2 square or a 2x2 square,
    #     depending if the entered
    #     coordinates are in an edge or not.'''

    #     from_row, to_row = self.get_index_limit(row)
    #     from_col, to_col = self.get_index_limit(col)

    #     return {
    #         'from_row': from_row,
    #         'to_row': to_row,
    #         'from_col': from_col,
    #         'to_col': to_col}

    # def close_opposite_around(self, row, col):
    #     limits = self.get_limits(row, col)
    #     close_opposite_list = []
    #     for i in range(limits["from_row"], limits["to_row"] + 1):
    #         for j in range(limits["from_col"], limits["to_col"] + 1):
    #             if self.what_is(i, j) == self.get_opposite_piece():
    #                 close_opposite_list.append((i, j))
    #     return close_opposite_list

    def determine_winner(self):
        if self.get_piece_count("W") == self.get_piece_count("B"):
            return "Tie"
        elif self.get_piece_count("W") > self.get_piece_count("B"):
            return self.possibles_players[1]
        else:
            return self.possibles_players[0]

    def flip_pieces(self, coordinates):
        for row, col in coordinates:
            self.board[row][col] = self.player_turn
        # self.black_can_play = True
        # self.white_can_play = True

    def end_game(self):
        if self.black_can_play is False and self.white_can_play is False:
            self.is_playing = False
            self.determine_winner()

    '''
    def validate_move(self, row, col):
        NEEDS TO BE COMPLETED
        Used by validate_direction(), generates array if valid
        Returns False if not valid.
        Suggested: if true, it should return a list of list, where
        each list is a list of coordinates returned by validate_direction,
        hence, in most of the cases this function should
        call validate_direction() eigth times,
        one for every direction. If a move is on an edge,
        this list will include three False.
        if self.board[row][col] is not None:
            return False
    '''
    def validate_move(self, row, col):
        '''
        Tells whether a move is valid or not.
        Returns False if not valid,
        Returns an list of lists, where the contained lists consist '''
        directions = ["n", "ne", "e", "se", "s", "sw", "w", "nw"]
        flips = []
        for i in directions:
            potential_flips = self.validate_direction(row, col, i)
            if potential_flips:
                flips = flips + potential_flips
        if not flips:
            return False
        else:
            return flips

    def validate_direction(self, row, col, direction):
        '''
        used by validate_move()
        gets row and col, direction is a string.
        returns false is direction is not valid,
        returns the array if direction is valid.
        The returned array does not include the
        position where we are placing a piece,
        nor the last position that includes a
        piece of the same color of the active player
        '''
        my_dictionary = {
            "n": [-1, 0],
            "ne": [-1, 1],
            "e": [0, 1],
            "se": [1, 1],
            "s": [1, 0],
            "sw": [1, -1],
            "w": [0, -1],
            "nw": [-1, -1]
        }
        change = my_dictionary[direction]
        myList = []
        while (row + change[0] >= 0 and
               row + change[0] < 8 and
               col + change[0] >= 0 and col + change[1] < 8):
            row = row + change[0]
            col = col + change[1]
            if self.board[row][col] is None:
                return False
            if self.board[row][col] == self.player_turn:
                break
            myList.append([row, col])
        if myList:
            return myList
        else:
            # self.player_turn = False
            return False

    def check_if_the_player_can_play(self, moves):
        if moves == {}:
            return False
        return True

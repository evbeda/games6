
class Othello():

    def __init__(self):
        self.possibles_players = ['B', 'W']
        self.player_turn = self.possibles_players[0]
        self._board = [
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
            [ficha == kind for row in self._board for ficha in row])

    def change_player(self):
        self.player_turn = self.get_opposite_piece()

    def get_opposite_piece(self):
        aux = self.possibles_players.copy()
        aux.remove(self.player_turn)
        return aux[0]

    def determine_winner(self):
        if self.get_piece_count("W") == self.get_piece_count("B"):
            return "Tie"
        elif self.get_piece_count("W") > self.get_piece_count("B"):
            return self.possibles_players[1]
        else:
            return self.possibles_players[0]

    def flip_pieces(self, coordinates):
        for row, col in coordinates:
            self._board[row][col] = self.player_turn

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
        ending_same_color = False

        while (row + change[0] >= 0 and
               row + change[0] < 8 and
               col + change[1] >= 0 and col + change[1] < 8):
            row = row + change[0]
            col = col + change[1]
            if self._board[row][col] is None:
                return []
            if self._board[row][col] == self.player_turn:
                ending_same_color = True
                break
            myList.append((row, col))

        return myList if ending_same_color else []

    def all_possible_moves(self):
        moves = {}
        positions = self.none_pos()

        for pos in positions:
            aux = self.validate_move(pos[0], pos[1])
            if aux:
                moves[(pos[0], pos[1])] = aux

        return moves

    def none_pos(self):
        pos = []
        for x, row in enumerate(self._board):
            for y, element in enumerate(row):
                if element is None:
                    pos.append((x, y))
        return pos

    # this method may be unused...
    def board_printer(self):
        list_of_the_printable_board = []
        list_of_the_printable_board.append(' 0 1 2 3 4 5 6 7   ')
        for row_count, row in enumerate(self._board):
            string_row = ''
            for element in row:
                string_row += '|'
                string_row += ' ' if element is None else element
            string_row += '| ' + str(row_count)
            list_of_the_printable_board.append(string_row)
        return list_of_the_printable_board

    @property
    def board(self):
        string_board = ' 0 1 2 3 4 5 6 7   \n'
        for row_count, row in enumerate(self._board):
            for element in row:
                string_board += '|'
                string_board += ' ' if element is None else element
            string_board += '| ' + str(row_count) + '\n'
        return string_board

    def play(self, row, col):

        move = (row, col)
        moves = self.all_possible_moves()
        # pdb.set_trace()
        if not (move in moves):
            return (f"Bad move of player {self.player_turn}. Try again")

        self.put_piece(move)
        self.flip_pieces(moves[move])

        self.change_player()

        if not self.all_possible_moves():
            self.change_player()
            if not self.all_possible_moves():
                winner = self.determine_winner()
                self.is_playing = False
                return "tie match" if winner == "Tie" else f"{winner} wins the match"

        return "204"

    def next_turn(self):
        if self.is_playing:
            return f"Turn of Player {self.player_turn}"
        else:
            return "Game Over"

    def put_piece(self, coordinate):
        row, col = coordinate
        self._board[row][col] = self.player_turn

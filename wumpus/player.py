class Player:

    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, direction):
        if direction == "w" and self.row != 0:
            self.row -= 1
        if direction == "s" and self.row != 14:
            self.row += 1
        if direction == "a" and self.col != 0:
            self.col -= 1
        if direction == "d" and self.col != 7:
            self.col += 1

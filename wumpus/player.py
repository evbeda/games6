class Player:

    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, direction):
        if direction == "w" and self.row != 0:
            self.row -= 1
        elif direction == "s" and self.row != 14:
            self.row += 1
        elif direction == "a" and self.col != 0:
            self.col -= 1
        elif direction == "d" and self.col != 7:
            self.col += 1

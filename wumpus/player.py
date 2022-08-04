class Player:

    def __init__(self):
        self.row = 0
        self.col = 0

    def move(self, direction):
        if direction == "w":
            self.row -= 1
        elif direction == "s":
            self.row += 1
        elif direction == "a":
            self.col -= 1
        elif direction == "d":
            self.col += 1

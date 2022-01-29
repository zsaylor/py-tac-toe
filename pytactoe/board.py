class Board:
    def __init__(self):
        self.board = [["-"] * 3 for i in range(3)]

    def __str__(self):
        return "\n| " + " |\n| ".join(" | ".join(row) for row in self.board) + " |\n"

    def insert_symbol(self, symbol, tile_coords_tuple):
        row, col = tile_coords_tuple
        if self.board[row][col] == "-":
            self.board[row][col] = symbol
            print(self)
            return True
        else:
            return False

    def clear_board(self):
        self.board = [["-"] * 3 for i in range(3)]
        print(self)
        return True

    def check_full_board(self):
        if any("-" in row for row in self.board):
            return False
        else:
            return True

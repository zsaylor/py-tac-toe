class Game:
    def __init__(self, board, p1, p2):
        self.game_board = board
        self.players = [p1, p2]
        self.choice_row = 0

    def turn(self, player):
        print(f"{player.name}, please enter the coordinates for your next move.")
        self.choose_coords()
        while not self.game_board.insert_symbol(player.symbol, (self.choice_row - 1, self.choice_column - 1)):
            print("Oops! That spot is already taken. Please enter different coordinates.")
            self.choose_coords()

    def choose_coords(self):
        valid_coords = [1, 2, 3]
        while True:
            try:
                self.choice_row = int(input("Enter a row number (1-3):\n"))
            except ValueError:
                print("Sorry, that is not a valid row. Try again.")
                continue
            else:
                while self.choice_row not in valid_coords:
                    print("Sorry, that is not a valid row. Try again.")
                    self.choice_row = int(input("Enter a row number (1-3):\n"))
                break

        while True:
            try:
                self.choice_column = int(input("Enter a column number (1-3):\n"))
            except ValueError:
                print("Sorry, that is not a valid row. Try again.")
                continue
            else:
                while self.choice_column not in valid_coords or self.choice_row == '':
                    print("Sorry, that is not a valid column. Try again.")
                    self.choice_column = int(input("Enter a column number (1-3):\n"))
                break

    def check_win(self):
        check_set = set()

        for row in self.game_board.board:
            check_set.add(tuple(row))

        board_cols = zip(self.game_board.board[0], self.game_board.board[1], self.game_board.board[2])
        for col in board_cols:
            check_set.add(tuple(col))

        left_diag = (self.game_board.board[0][0], self.game_board.board[1][1], self.game_board.board[2][2])
        right_diag = (self.game_board.board[2][2], self.game_board.board[1][1], self.game_board.board[0][0])
        check_set.update((left_diag, right_diag))

        check_results = {True if (len(set(combo)) == 1 and combo[0] != "-") else False for combo in check_set}
        if True in check_results:
            return True
        return False

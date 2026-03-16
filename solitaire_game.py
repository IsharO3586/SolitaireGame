class SolitaireGame:
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        self.board = []

        for r in range(7):
            row = []
            for c in range(7):
                if (r < 2 or r > 4) and (c < 2 or c > 4):
                    row.append(None)
                elif r == 3 and c == 3:
                    row.append(" ")
                else:
                    row.append("●")
            self.board.append(row)

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if self.board[end_row][end_col] != " ":
            return False

        dr = end_row - start_row
        dc = end_col - start_col

        if not ((abs(dr) == 2 and dc == 0) or (abs(dc) == 2 and dr == 0)):
            return False

        mid_row = start_row + dr // 2
        mid_col = start_col + dc // 2

        if self.board[mid_row][mid_col] != "●":
            return False

        if self.board[start_row][start_col] != "●":
            return False

        return True

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            mid_row = (start_row + end_row) // 2
            mid_col = (start_col + end_col) // 2

            self.board[start_row][start_col] = " "
            self.board[mid_row][mid_col] = " "
            self.board[end_row][end_col] = "●"
            return True

        return False
    


    def is_game_over(self):
        for r in range(7):
            for c in range(7):
                if self.board[r][c] == "●":

                    # check up
                    if r - 2 >= 0 and self.is_valid_move(r, c, r - 2, c):
                        return False

                    # check down
                    if r + 2 < 7 and self.is_valid_move(r, c, r + 2, c):
                        return False

                    # check left
                    if c - 2 >= 0 and self.is_valid_move(r, c, r, c - 2):
                        return False

                    # check right
                    if c + 2 < 7 and self.is_valid_move(r, c, r, c + 2):
                        return False

        return True
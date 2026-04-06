class SolitaireGame:
    def __init__(self, size=7):
        self.size = size
        self.board = []
        self.create_board()

    def create_board(self):
        pass

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
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == "●":
                    if r - 2 >= 0 and self.is_valid_move(r, c, r - 2, c):
                        return False
                    if r + 2 < len(self.board) and self.is_valid_move(r, c, r + 2, c):
                        return False
                    if c - 2 >= 0 and self.is_valid_move(r, c, r, c - 2):
                        return False
                    if c + 2 < len(self.board[r]) and self.is_valid_move(r, c, r, c + 2):
                        return False
        return True
    
    def count_pegs(self):
        count = 0
        for row in self.board:
            for cell in row:
                if cell == "●":
                    count += 1
        return count
    
    def get_rating(self):
        pegs = self.count_pegs()

        if pegs == 1:
            return "Outstanding"
        elif pegs == 2:
            return "Very Good"
        elif pegs == 3:
            return "Good"
        else:
            return "Average"


class EnglishSolitaire(SolitaireGame):
    def create_board(self):
        self.board = []

        for r in range(self.size):
            row = []
            for c in range(self.size):
                if (r < 2 or r > 4) and (c < 2 or c > 4):
                    row.append(None)
                elif r == self.size // 2 and c == self.size // 2:
                    row.append(" ")
                else:
                    row.append("●")
            self.board.append(row)


class HexagonSolitaire(SolitaireGame):
    def create_board(self):
        self.board = []

        center = self.size // 2

        for r in range(self.size):
            row = []
            for c in range(self.size):
                #condition
                if abs(r - center) + abs(c - center) > center + 1:
                    row.append(None)
                elif r == center and c == center:
                    row.append(" ")
                else:
                    row.append("●")
            self.board.append(row)


class DiamondSolitaire(SolitaireGame):
    def create_board(self):
        self.board = []

        center = self.size // 2

        for r in range(self.size):
            row = []
            for c in range(self.size):
                if abs(r - center) + abs(c - center) > center:
                    row.append(None)
                elif r == center and c == center:
                    row.append(" ")
                else:
                    row.append("●")
            self.board.append(row)




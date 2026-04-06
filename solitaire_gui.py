import tkinter as tk
from solitaire_game import EnglishSolitaire, HexagonSolitaire, DiamondSolitaire

class SolitaireGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Solitaire Game")
        
        self.new_game_button = tk.Button(self.window, text="New Game", command=self.new_game)
        self.new_game_button.pack()

        title = tk.Label(self.window, text="Solitaire Game", font=("Arial", 16))
        title.pack()

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.game = EnglishSolitaire()

        self.board_type_label = tk.Label(self.window, text="Board Type")
        self.board_type_label.pack()

        self.board_type_var = tk.StringVar()
        self.board_type_var.set("English")

        self.board_type_menu = tk.OptionMenu(self.window, self.board_type_var, "English", "Hexagon", "Diamond")
        self.board_type_menu.pack()

        self.selected_peg = None
        self.buttons = []

        self.create_board()
        self.board_size_label = tk.Label(self.window, text="Board Size")
        self.board_size_label.pack()

        self.board_size_var = tk.StringVar()
        self.board_size_var.set("7")

        self.board_size_menu = tk.OptionMenu(self.window, self.board_size_var, "7")
        self.board_size_menu.pack()

        self.message_label = tk.Label(self.window, text="")
        self.message_label.pack()

        self.window.mainloop()



    def new_game(self):
        board_type = self.board_type_var.get()
        board_size = int(self.board_size_var.get())

        if board_type == "English":
            self.game = EnglishSolitaire(board_size)
        elif board_type == "Hexagon":
            self.game = HexagonSolitaire(board_size)
        else:
            self.game = DiamondSolitaire(board_size)

        self.message_label.config(text="")

        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        self.create_board()

        


    def create_board(self):
        rows = len(self.game.board)
        cols = len(self.game.board[0])

        for r in range(rows):
            button_row = []

            for c in range(cols):

                value = self.game.board[r][c]

                if value is None:
                    empty = tk.Label(self.board_frame, text=" ", width=4, height=2)
                    empty.grid(row=r, column=c)
                    button_row.append(None)
                    continue

                value = self.game.board[r][c]

                button = tk.Button(
                    self.board_frame,
                    text=value,
                    width=4,
                    height=2,
                    command=lambda row=r, col=c: self.select_peg(row, col)
)

                button.grid(row=r, column=c)
                button_row.append(button)

            self.buttons.append(button_row)


    def select_peg(self, row, col):
        button = self.buttons[row][col]

        #9f no peg selected yet
        if self.selected_peg is None:

            if button["text"] == "●":
                button.config(relief="sunken", bd=5)
                self.selected_peg = (row, col)

            return

        #if peg already selected
        start_row, start_col = self.selected_peg
        start_button = self.buttons[start_row][start_col]

        if button["text"] == " ":
            if self.game.make_move(start_row, start_col, row, col):
                self.refresh_board()

                if self.game.is_game_over():
                    rating = self.game.get_rating()
                    self.message_label.config(text=f"Game Over! Rating: {rating}")

        #reset 
        start_button.config(relief="raised", bd=2)
        self.selected_peg = None
    
    def refresh_board(self):
        for r in range(7):
            for c in range(7):
                if self.buttons[r][c] is not None:
                    self.buttons[r][c].config(
                        text=self.game.board[r][c],
                        relief="raised",
                        bd=2
                    )                if (r < 2 or r > 4) and (c < 2 or c > 4):
                    empty = tk.Label(self.board_frame, text=" ", width=4, height=2)
                    empty.grid(row=r, column=c)
                    button_row.append(None)
                    continue

                value = self.game.board[r][c]

                button = tk.Button(
                    self.board_frame,
                    text=value,
                    width=4,
                    height=2,
                    command=lambda row=r, col=c: self.select_peg(row, col)
)

                button.grid(row=r, column=c)
                button_row.append(button)

            self.buttons.append(button_row)


    def select_peg(self, row, col):
        button = self.buttons[row][col]

        # if no peg selected yet
        if self.selected_peg is None:

            if button["text"] == "●":
                button.config(relief="sunken", bd=5)
                self.selected_peg = (row, col)

            return

        # if peg already selected
        start_row, start_col = self.selected_peg
        start_button = self.buttons[start_row][start_col]

        if button["text"] == " ":
            if self.game.make_move(start_row, start_col, row, col):
                self.refresh_board()

                if self.game.is_game_over():
                    self.message_label.config(text="Game Over!")

        # reset selection
        start_button.config(relief="raised", bd=2)
        self.selected_peg = None
    
    def refresh_board(self):
        for r in range(7):
            for c in range(7):
                if self.buttons[r][c] is not None:
                    self.buttons[r][c].config(
                        text=self.game.board[r][c],
                        relief="raised",
                        bd=2
                    )

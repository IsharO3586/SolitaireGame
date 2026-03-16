import tkinter as tk
from solitaire_game import SolitaireGame

class SolitaireGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Solitaire Game")

        title = tk.Label(self.window, text="Solitaire Game", font=("Arial", 16))
        title.pack()

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.game = SolitaireGame()

        self.selected_peg = None
        self.buttons = []

        self.create_board()

        self.message_label = tk.Label(self.window, text="")
        self.message_label.pack()

        self.window.mainloop()


    def create_board(self):
        rows = 7
        cols = 7

        for r in range(rows):
            button_row = []

            for c in range(cols):

                if (r < 2 or r > 4) and (c < 2 or c > 4):
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
import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.current_player = "X"
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.create_board()
        
    def create_board(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        # buttons for the tic tac toe grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 60), width=4, height=2,bg='skyblue',foreground='red', command=lambda x=i, y=j: self.button_click(x, y))
                button.grid(row=i, column=j, sticky='news')
                row.append(button)
            self.buttons.append(row)

        # a reset button
        reset_button = tk.Button(self.root, text="Reset", font=('Arial', 20), command=self.reset)
        reset_button.grid(row=3, column=0, columnspan=3, sticky='news')

    def button_click(self, x, y):
        if self.board[x][y] == "":
            self.board[x][y] = self.current_player
            self.buttons[x][y].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", "Player " + self.current_player + " wins!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.switch_player()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset(self):
        self.current_player = "X"
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    tic_tac_toe_gui = TicTacToeGUI()
    tic_tac_toe_gui.run()


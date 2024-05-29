import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.configure(bg='black')

        # Initialize empty_image attribute first
        empty_image = Image.open("images/empty.png")  # Load empty.svg image
        self.empty_image = ImageTk.PhotoImage(empty_image)  # Make it an attribute

        # Initialize top bar frame
        self.initialize_top_bar_frame()
        self.pack_top_bar_frame()

        # Initialize board
        self.board = [[' ']*3 for _ in range(3)]

        # Initialize board frame and buttons
        self.initialize_board()

        self.current_player = 'X'

        x_image = Image.open("images/X.png")  # Load X.svg image
        self.x_image = ImageTk.PhotoImage(x_image)

        o_image = Image.open("images/O.png")  # Load O.svg image
        self.o_image = ImageTk.PhotoImage(o_image)

        self.update_turn_label()

        self.waiting_for_input = True

    
    def initialize_board(self):
        self.board_frame = tk.Frame(self.master, bg='black', highlightbackground='black', highlightthickness=15)
        self.board_frame.pack(padx=20, pady=20)    
        self.buttons = [[None]*3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.board_frame, image=self.empty_image, width=120, height=120,
                                            bg='black', bd=0, activebackground="black",
                                            command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
                self.buttons[i][j].config(image=self.empty_image)

    
    def initialize_top_bar_frame(self):
        self.top_bar_frame = tk.Frame(self.master, bg='#131313', highlightbackground='#131313', highlightthickness=15)

        self.turn_label = tk.Label(self.top_bar_frame, text="It's ", fg='grey', bg='#131313', font=('Arial Bold', 16))
        self.turn_label.pack(side='left', padx=(115, 0))

        self.player_image_label = tk.Label(self.top_bar_frame, image=None, bg='#131313')
        self.player_image_label.pack(side='left')

        self.turn_text_label = tk.Label(self.top_bar_frame, text="turn!", fg='grey', bg='#131313',
                                        font=('Arial Bold', 16))
        self.turn_text_label.pack(side='left')

   
    def pack_top_bar_frame(self):
        self.top_bar_frame.pack(fill='both')

    
    def make_move(self, i, j):
        if self.waiting_for_input and self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            if self.current_player == 'X':
                self.buttons[i][j].config(image=self.x_image)  # set X image
            else:
                self.buttons[i][j].config(image=self.o_image)  # set O image
            if self.check_winner(self.current_player):
                self.display_winner(self.current_player)
                self.waiting_for_input = False  # Disable further input until reset
            elif self.check_tie():
                self.display_tie_screen()
                self.waiting_for_input = False  # Disable further input until reset
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.update_turn_label()


    def update_turn_label(self):
        player_image = self.x_image if self.current_player == 'X' else self.o_image
        self.player_image_label.config(image=player_image)

    
    def display_winner(self, winner):
        player_image = self.x_image if winner == 'X' else self.o_image
        self.player_image_label.config(image=player_image)

        # Remove the existing "It's turn!" label
        self.turn_label.pack_forget()
        self.turn_text_label.pack_forget()

        # Adjust padding to center the image horizontally
        self.player_image_label.pack(side='left', padx=(154, 0))

        # Create a label for the "won!" text
        won_label = tk.Label(self.top_bar_frame, text="won!", fg='grey', bg='#131313', font=('Arial Bold', 16))

        # Center the "won!" label horizontally
        won_label.pack(side='left')

        # Clear any existing "won!" label
        if hasattr(self, 'won_label'):
            self.won_label.destroy()

        # Pack the new "won!" label
        self.won_label = won_label

        # Wait for button click to reset the game
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(command=self.reset_game)

    
    def display_tie_screen(self):
        self.turn_label.pack_forget()
        self.turn_text_label.pack_forget()
        self.player_image_label.pack_forget()

        tie_label = tk.Label(self.top_bar_frame, text="It's a tie!", fg='grey', bg='#131313', font=('Arial Bold', 16))

        tie_label.pack(side='left', padx=(160, 0), pady=38)

        # Pack the new "won!" label
        self.tie_label = tie_label

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(command=self.reset_game)


    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for j in range(3):
            if all(self.board[i][j] == player for i in range(3)):
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

   
    def check_tie(self):
        return all(cell != ' ' for row in self.board for cell in row)

    
    def reset_game(self):
        # Destroy the existing board frame
        self.board_frame.destroy()

        # Destroy the existing top bar frame
        self.top_bar_frame.destroy()

        # Reinitialize and repack the top bar frame
        self.initialize_top_bar_frame()
        self.pack_top_bar_frame()

        self.initialize_board()

        # Reset the game state
        self.board = [[' ']*3 for _ in range(3)]
        self.current_player = 'X'
        self.update_turn_label()
        
        self.waiting_for_input = True


def main():
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()

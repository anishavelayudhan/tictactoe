import os


def clear_screen():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def draw_board(board):
  print(f"   1   2   3\n"
    f"a  {board[0][0]} | {board[0][1]} | {board[0][2]}  \n"
    f"  -----------\n"
    f"b  {board[1][0]} | {board[1][1]} | {board[1][2]}  \n"
    f"  -----------\n"
    f"c  {board[2][0]} | {board[2][1]} | {board[2][2]}  \n")


def move(board, current_player, player_name):
  while True:
    next_move = input(f"{player_name}'s turn ({current_player}). Enter XY coordinate: ")
    if len(next_move) == 2 and next_move[0].isalpha() and next_move[1].isdigit():
      next_move = next_move[0].upper() + next_move[1:]
      if next_move[0] in ['A', 'B', 'C']:
        x = ord(next_move[0]) - ord('A')
        y = int(next_move[1]) - 1
        if board[x][y] == ' ':
          board[x][y] = current_player
          clear_screen()
          draw_board(board)
          break
        else:
          print("Spot has been taken. Try again.")
      else:
        print("Invalid coordinates. Try again.")


def check_winner(board):
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] != ' ':
      return True
  for column in range(3):
    if board[0][column] == board[1][column] == board[2][column] != ' ':
      return True
  if (board[0][0] == board[1][1] == board[2][2] != ' ') or \
     (board[0][2] == board[1][1] == board[2][0] != ' '):
    return True



def game(scores, player_names):
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
  draw_board(board)

  players = ['X', 'O']
  current_player_index = 0

  while True:
    current_player = players[current_player_index]
    player_name = player_names[current_player_index]
    move(board, current_player, player_name)

    if check_winner(board):
      scores[current_player_index] += 1
      return scores
        
    if all(cell != ' ' for row in board for cell in row):
      print("It's a tie")
      return scores

    current_player_index = (current_player_index + 1) % 2 


def main():
  print("Welcome to Tic-Tac-Toe!\n")
  player_names = []
  player_names.append(input("Enter name for Player 1 (X): "))
  player_names.append(input("Enter name for Player 2 (O): "))
  clear_screen()

  scores = [0, 0]
  while True:
    scores = game(scores, player_names)
    print(f"Scores:\n{player_names[0]} (X): {scores[0]}\n{player_names[1]} (O): {scores[1]}\n")
    restart = input("Do you want to play again? (Y/N): ").upper()
    if restart != 'Y':
      clear_screen()
      print("Thank you for playing!\n")
      print(f"Scores:\n{player_names[0]} (X): {scores[0]}\n{player_names[1]} (O): {scores[1]}\n")
      break
    clear_screen()


main()

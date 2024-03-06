# Define the game board as a list
board = [' ' for _ in range(9)]  # Initialize all positions as empty

# Function to display the game board with visual enhancements
def display_board(board):
  """Displays the current state of the Tic Tac Toe board with visual formatting."""
  for i in range(3):
    for j in range(3):
      print(board[i * 3 + j], end=" ")
    print("|")
  print("-" * 11)

# Function to check if a player has won
def has_won(board, player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

# Function to check if the board is full (tie)
def is_board_full(board):
  return all(cell != ' ' for cell in board)

# Function for player input validation with informative messages
def validate_move(board, move):
 
  try:
    if move >= 0 and move <= 8 and board[move] == ' ':
      return True
    elif board[move] != ' ':
      print("That space is already occupied. Please choose another one.")
    else:
      print("Invalid move. Please enter a number between 1 and 9.")
    return False
  except IndexError:
    print("Invalid move. Please enter a number between 1 and 9.")
    return False

# Function to get player input with clear instructions
def get_player_move(board):
  while True:
    print("Available moves:")
    for i in range(3):
      for j in range(3):
        print(f"{i * 3 + j + 1} ", end="")
      print()
    move = int(input("Enter your move (1-9): ")) - 1
    if validate_move(board, move):
      return move

# Main game loop
def main():
  current_player = 'X'  
  game_over = False

  while not game_over:
    display_board(board)

    move = get_player_move(board)

    board[move] = current_player

    if has_won(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      game_over = True

    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      game_over = True

    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
  main()

# Tic-Tac-Toe

# Create an empty game board
board = [' '] * 9

# Define winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Variable to track the current player
current_player = 'X'

# Function to print the game board


def print_board():
    print('-------------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |')
        print('-------------')

# Function to check if a player has won


def check_winner(player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to play the game


def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    # Game loop
    while True:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position. Try again.")
            continue

        if board[position] != ' ':
            print("Position already taken. Try again.")
            continue

        board[position] = current_player
        print_board()

        if check_winner(current_player):
            print(f"Player {current_player} wins!")
            break

        if ' ' not in board:
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


# Start the game
play_game()

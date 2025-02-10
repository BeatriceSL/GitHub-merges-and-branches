import random

# Kitty and Pikachu representations
KITTY = "😺"
PIKACHU = "🐭"

# Initialize the board
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(player):
    # Check rows, columns, and diagonals
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_board_full():
    return " " not in board

def player_move(player):
    while True:
        try:
            move = int(input(f"{player}'s turn! Enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player
                break
            else:
                print("Invalid move! Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move(player):
    print(f"{player}'s turn (Computer)...")
    available_moves = [i for i, val in enumerate(board) if val == " "]
    move = random.choice(available_moves)
    board[move] = player

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("You are the Kitty (😺), and the computer is Pikachu (🐭).")
    print_board()

    while True:
        # Player's move
        player_move(KITTY)
        print_board()
        if check_winner(KITTY):
            print("You win! 😺")
            break
        if is_board_full():
            print("It's a tie!")
            break

        # Computer's move
        computer_move(PIKACHU)
        print_board()
        if check_winner(PIKACHU):
            print("Pikachu wins! 🐭")
            break
        if is_board_full():
            print("It's a tie!")
            break

# Start the game
play_game()
"""
projekt_2.py: druhý další varianta projekt do Engeto Online Python Akademie
author: Karel Provázek
email: provazek@24s.cz
discord: provazek24s.cz_84357
"""

# Úvodní pozdravení a pravidla hry
print("Welcome to Tic Tac Toe")
print("="*40)
print("GAME RULES:")
print("Each player can place one mark (or stone)")
print("per turn on the 3x3 grid. The WINNER is")
print("who succeeds in placing three of their marks in a:")
print("* horizontal,")
print("* vertical or")
print("* diagonal row")
print("="*40)
print("Let's start the game\n")

# Hrací plocha
board = [" " for _ in range(9)]

# Zobrazení hrací plochy
def display_board():
    for row in range(3):
        print("+---+---+---+")
        print(f"| {board[row*3]} | {board[row*3+1]} | {board[row*3+2]} |")
    print("+---+---+---+")

# Kontrola vítězství
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontální
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertikální
        [0, 4, 8], [2, 4, 6]              # Diagonální
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Hlavní smyčka hry
current_player = "X"
for turn in range(9):
    display_board()
    while True:
        try:
            move = int(input(f"Player {current_player}, enter a move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move, try again.")
            else:
                board[move] = current_player
                break
        except ValueError:
            print("Please enter a number.")

    if check_winner(current_player):
        display_board()
        print(f"Congratulations, the player {current_player} WON!")
        break

    current_player = "O" if current_player == "X" else "X"
else:
    display_board()
    print("It's a tie!")

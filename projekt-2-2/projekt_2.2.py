
"""
projekt_2.py: druhý další varianta projekt do Engeto Online Python Akademie
author: Karel Provázek
email: provazek@24s.cz
discord: provazek24s.cz_84357
"""
# Úvodní pozdravení a pravidla hry
def welcome_message():
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

# Funkce pro zobrazení hrací plochy
def display_board(board):
    print("+---+---+---+")
    for row in range(3):
        print("| " + " | ".join(board[row]) + " |")
        print("+---+---+---+")

# Funkce pro kontrolu výhry
def check_winner(board, player):
    # Horizontální, vertikální a diagonální podmínky výhry
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # 1. řádek
        [board[1][0], board[1][1], board[1][2]],  # 2. řádek
        [board[2][0], board[2][1], board[2][2]],  # 3. řádek
        [board[0][0], board[1][0], board[2][0]],  # 1. sloupec
        [board[0][1], board[1][1], board[2][1]],  # 2. sloupec
        [board[0][2], board[1][2], board[2][2]],  # 3. sloupec
        [board[0][0], board[1][1], board[2][2]],  # Diagonála zleva doprava
        [board[0][2], board[1][1], board[2][0]]   # Diagonála zprava doleva
    ]
    return [player, player, player] in win_conditions

# Funkce pro získání uživatelského vstupu
def get_player_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player} | Please enter your move number (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move // 3][move % 3] != " ":
                print("This spot is already taken. Choose another one.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

# Hlavní logika hry
def tic_tac_toe():
    welcome_message()

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_count = 0

    while moves_count < 9:
        display_board(board)
        move = get_player_move(current_player, board)
        board[move // 3][move % 3] = current_player
        moves_count += 1

        if check_winner(board, current_player):
            display_board(board)
            print(f"Congratulations, the player {current_player} WON!")
            break

        current_player = "O" if current_player == "X" else "X"
    
    if moves_count == 9 and not check_winner(board, current_player):
        print("It's a tie!")

# Spuštění hry
if __name__ == "__main__":
    tic_tac_toe()

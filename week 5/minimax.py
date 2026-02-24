import math

board = [" " for _ in range(9)]

def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if not available_moves():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            board[move] = "O"
            score = minimax(False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            board[move] = "X"
            score = minimax(True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -math.inf
    best_move = None
    for move in available_moves():
        board[move] = "O"
        score = minimax(False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def tic_tac_toe():
    for turn in range(9):
        print_board()
        if turn % 2 == 0:
            move = int(input("Your move (1-9): ")) - 1
            if board[move] != " ":
                print("Invalid move! Try again.")
                continue
            board[move] = "X"
            if check_winner("X"):
                print_board()
                print("You win!")
                return
        else:
            move = computer_move()
            board[move] = "O"
            print(f"Computer chose {move + 1}")
            if check_winner("O"):
                print_board()
                print("Computer wins!")
                return

    print_board()
    print("It's a tie!")

tic_tac_toe()

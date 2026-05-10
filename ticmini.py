import math

board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("---------")

def check_win(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    return None

def board_full(b):
    return ' ' not in b

# 🔥 MINIMAX
def minimax(depth, isMax):
    winner = check_win(board)

    if winner == 'X':
        return 10 - depth
    elif winner == 'O':
        return depth - 10
    elif board_full(board):
        return 0

    if isMax:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth+1, False)
                board[i] = ' '
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth+1, True)
                board[i] = ' '
                best = min(best, score)
        return best

def find_move():
    best = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(0, False)
            board[i] = ' '
            if score > best:
                best = score
                move = i
    return move

print("TIC-TAC-TOE")
print("0 1 2\n3 4 5\n6 7 8")

while True:
    move = find_move()
    board[move] = 'X'
    print("AI played:", move)
    print_board()

    if check_win(board):
        print("Winner:", check_win(board))
        break
    if board_full(board):
        print("Draw")
        break

    user = int(input("Enter your move: "))
    if board[user] != ' ':
        print("Invalid move")
        continue

    board[user] = 'O'
    print("You played:", user)
    print_board()

    if check_win(board):
        print("Winner:", check_win(board))
        break
    if board_full(board):
        print("Draw")
        break

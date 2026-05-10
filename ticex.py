board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("---------")

def checkwin(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for i,j,k in wins:
        if b[i] == b[j] == b[k] and b[i] != ' ':
            return b[i]
    return None

def board_full(b):
    return ' ' not in b

def exhaustive_search(b, player):
    if checkwin(b) or board_full(b):
        return
    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            next_player = 'O' if player == 'X' else 'X'
            exhaustive_search(b, next_player)
            b[i] = ' '   # backtrack

def ai_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            exhaustive_search(board, 'O')
            board[i] = ' '
            return i

print("Tic-Tac-Toe")
print("0 1 2\n3 4 5\n6 7 8")

while True:
    move = ai_move()
    board[move] = 'X'
    print("AI played:", move)
    print_board()

    if checkwin(board):
        print("Winner:", checkwin(board))
        break
    if board_full(board):
        print("Draw")
        break

    user = int(input("Enter move: "))
    if board[user] != ' ':
        print("Invalid move")
        continue

    board[user] = 'O'

    if checkwin(board):
        print("Winner:", checkwin(board))
        break
    if board_full(board):
        print("Draw")
        break

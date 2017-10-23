from random import randint

# 定义方法
board = []
for row in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for i in board:
        print(" ".join(i))

print_board(board)

def ran_row(board):
    return randint(0, len(board) - 1)

def ran_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = ran_row(board)
ship_col = ran_col(board)

print(ship_row)
print(ship_col)

# 运行游戏
for turn in range(4):
    print("Turn : ", turn + 1)
    guess_row = int(input("Guess row :"))
    guess_col = int(input("Guess col :"))

    if guess_row == ship_row and guess_col == guess_col:
        print("猜对了")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("超出范围了")
        elif board[guess_row][guess_col] == "X":
            print("已经猜过了")
        else:
            print("你猜错了")
        if turn == 3:
            print("Game Over")
        print_board(board)
            
            

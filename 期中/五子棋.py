#參考chatgpt
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * len(board) * 4)

def check_winner(board, player):
    N = len(board)
    for i in range(N):
        if all([cell == player for cell in board[i]]):  # 橫線
            return True
        if all([board[j][i] == player for j in range(N)]):  # 縱線
            return True
    if all([board[i][i] == player for i in range(N)]):  # 主對角線
        return True
    if all([board[i][N-i-1] == player for i in range(N)]):  # 副對角線
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def ai_move(board):
    N = len(board)
    while True:
        row, col = random.randint(0, N-1), random.randint(0, N-1)
        if board[row][col] == ' ':
            return row, col

def player_move(board):
    while True:
        move = input("請輸入你的移動（格式：row,col）：")
        try:
            row, col = map(int, move.split(','))
            if board[row][col] == ' ':
                return row, col
            else:
                print("這個位置已經被佔用了，請重新選擇。")
        except (ValueError, IndexError):
            print("輸入無效，請按照格式輸入：row,col")

def play_game(N=5):
    board = [[' ' for _ in range(N)] for _ in range(N)]
    current_player = '玩家'
    
    while True:
        print_board(board)
        if current_player == '玩家':
            row, col = player_move(board)
            board[row][col] = 'X'
            if check_winner(board, 'X'):
                print_board(board)
                print("恭喜，你贏了！")
                break
            current_player = 'AI'
        else:
            row, col = ai_move(board)
            board[row][col] = 'O'
            if check_winner(board, 'O'):
                print_board(board)
                print("很遺憾，你輸了。")
                break
            current_player = '玩家'
        
        if is_full(board):
            print_board(board)
            print("平局！")
            break

if __name__ == "__main__":
    play_game()

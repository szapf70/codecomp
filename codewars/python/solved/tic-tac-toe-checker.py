# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python
# Tic-Tac-Toe Checker


def check_win(board):
    for p in [1,2]:
        for i in [0,1,2]:
            if board[i][0] == p and board[i][1] == p and board[i][2] == p:
                return p
            if board[0][i] == p and board[1][i] == p and board[2][i] == p:
                return p
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            return p  
        if board[2][0] == p and board[1][1] == p and board[0][2] == p:
            return p  
    return 0
    

def is_solved(board):
    res = check_win(board)
    if res > 0: return res
    for f in [x for r in board for x in r]:
        if not f:
            return -1
    return 0  

board = [[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]

print(is_solved(board))  
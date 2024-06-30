# https://www.codewars.com/kata/5b817c2a0ce070ace8002be0/train/python
# Tic-Tac-Toe-like table Generator

def display_board(board, width):
    bp = []
    while len(board) > 0:
        sp = [f" {f} " for f in board[:width]]
        bp.append("|".join([f" {f} " for f in board[0:width]]))
        board = board[width:]
    
    for i in range(1,(width-1)*2,2):
        bp.insert(i,"-" * ((width * 3) + (width -1)))
    
    return "\n".join(bp)
    
        
        
        
#print(display_board(["O", "X", "X", "O"],2),"\n O | X \n-------\n X | O ")
print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "],3),"\n O | X |   \n-----------\n   | X |   \n-----------\n X | O |   ")
#print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],5)," O | X |   |   | X \n-------------------\n   | X | O |   | O ")
#print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"],2)," O | X \n-------\n   |   \n-------\n X |   \n-------\n X | O \n-------\n   | O ")
#print(display_board(["1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1", "2", "3", "4", "5", "1"],6)," 1 | 2 | 3 | 4 | 5 | 1 \n-----------------------\n 2 | 3 | 4 | 5 | 1 | 2 \n-----------------------\n 3 | 4 | 5 | 1 | 2 | 3 \n-----------------------\n 4 | 5 | 1 | 2 | 3 | 4 \n-----------------------\n 5 | 1 | 2 | 3 | 4 | 5 \n-----------------------\n 1 | 2 | 3 | 4 | 5 | 1 ")
        
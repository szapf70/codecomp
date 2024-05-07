# https://www.codewars.com/kata/63d1bac72de941033dbf87ae/train/python
# Sudoku board validator

def get_house(board, type, num):
    if type == 'row':
        return board[num]
    
    if type == 'col':
        res = []
        for i in range(9):
            res.append(board[i][num])
        return res    
    
    if type == 'blk':
        res = []
        rb = 3*(num//3)
        cb = 3*(num%3)
        for r in range(3):
            for c in range(3):
                res.append(board[rb+r][cb+c])
        return res        

def valid_house(board, type, num):
    house = get_house(board, type, num)
    house = set(house)
    if len(house) != 9 or 0 in house: return False
    return True

def validate_sudoku(board):
    for i in range(9):
        if not valid_house(board,'row',i) : return False        
        if not valid_house(board,'col',i) : return False        
        if not valid_house(board,'blk',i) : return False        
    return True


board = [[5,3,4,6,7,8,9,1,2],
		 [6,7,2,1,9,5,3,4,8],
		 [1,9,8,3,4,2,5,6,7],
		 [8,5,9,7,6,1,4,2,3],
		 [4,2,6,8,5,3,7,9,1],
		 [7,1,3,9,2,4,8,5,6],
		 [9,6,1,5,3,7,2,8,4],
		 [2,8,7,4,1,9,6,3,5],
		 [3,4,5,2,8,6,1,7,9]]  


print(get_house(board,'blk',1)) 
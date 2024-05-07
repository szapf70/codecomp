# https://www.codewars.com/kata/63e5119516648934be4c98bd/train/python
# Sudoku board validator - Code Golf

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

def suprpr(board):
    for r in range(9):
        print(board[r])

def validate_sudoku_old(board):
    for i in range(9):
        if not valid_house(board,'row',i) : return False        
        if not valid_house(board,'col',i) : return False        
        if not valid_house(board,'blk',i) : return False        
    return True

def su150(b):
    for n in range(1,10):
        li = []
        for r in b:
            try:
                li.append(r.index(n))
            except:
                return False
        if len(set(li)) != 9: return False
    return True    

def sushort_old(b):
    try:
        return all([len(set([r.index(n) for r in b])) == 9 for n in range(1,10)])
    except:
        return False
    
def sushort(b):
    n=range(9)
    return all([sum(b[i])==sum([b[y][i] for y in n])==sum([b[3*(i//3)+y//3][3*(i%3)+y%3] for y in n]) for i in n])

#n=range(9)
#validate_sudoku=lambda b:all([[sum([b[i][y] for y in n]+[b[y][i]**2 for y in n]+[b[3*(i//3)+y//3][3*(i%3)+y%3]**3 for y in n])==2355] for i in n])
#n=range(9)
#validate_sudoku=lambda b:all([list(range(1,10))==set(b[i])==set([b[y][i] for y in n])==set([b[3*(i//3)+y//3][3*(i%3)+y%3] for y in n]) for i in n])
#n=range(9)
#validate_sudoku=lambda b:all([set(list(range(1,10)))==set(b[i])==set([b[y][i] for y in n])==set([b[3*(i//3)+y//3][3*(i%3)+y%3] for y in n]) for i in n])
#n=range(10)
#validate_sudoku=lambda b:all([set(n[1:])==set(b[i])==set([b[y][i]for y in n[:-1]])==set([b[3*(i//3)+y//3][3*(i%3)+y%3]for y in n[:-1]])for i in n[:-1]])
#n=range(9)
#validate_sudoku=lambda b:[[b[r][c] + 10*b[c][r] + 100*b[3*(r//3)+c//3][3*(r%3)+c%3] for c in n] for r in n]
    

"""    
    for i in n:
        print(sum([b[i][y] for y in n]))
        print(sum([b[y][i] for y in n]))
        print(sum([b[3*(i//3)+y//3][3*(i%3)+y%3] for y in n]))
"""

#validate_sudoku=lambda b: sum([((b[r][c]+1)*r+1)**3 for r in range(9) for c in range(len(set(b[r])))]) == 4160025



b1 = [[5,3,4,6,7,8,9,1,2],
		 [6,7,2,1,9,5,3,4,8],
		 [1,9,8,3,4,2,5,6,7],
		 [8,5,9,7,6,1,4,2,3],
		 [4,2,6,8,5,3,7,9,1],
		 [7,1,3,9,2,4,8,5,6],
		 [9,6,1,5,3,7,2,8,4],
		 [2,8,7,4,1,9,6,3,5],
		 [3,4,5,2,8,6,1,7,9]]  

b2 = [[1,3,2,5,7,9,4,6,8],
				  [4,9,8,2,6,1,3,7,5],
				  [7,5,6,3,8,4,2,1,9],
				  [6,4,3,1,5,8,7,9,2],
				  [5,2,1,7,9,3,8,4,6],
				  [9,8,7,4,2,6,5,3,1],
				  [2,1,4,9,3,5,6,8,7],
				  [3,6,5,8,1,7,9,2,4],
				  [8,7,9,6,4,2,1,5,3]]

   
b3 = [[1,1,1,1,1,1,1,1,1],
				  [2,2,2,2,2,2,2,2,2],
				  [3,3,3,3,3,3,3,3,3],
				  [4,4,4,4,4,4,4,4,4],
				  [5,5,5,5,5,5,5,5,5],
				  [6,6,6,6,6,6,6,6,6],
				  [7,7,7,7,7,7,7,7,7],
				  [8,8,8,8,8,8,8,8,8],
				  [9,9,9,9,9,9,9,9,9]] 

v = set(range(9))
print(v)

b = [[1,2,3,4,5,6,7,8,9],
     [4,5,6,7,8,9,1,2,3],
     [7,8,9,1,2,3,4,5,6],
     [2,3,1,5,6,4,8,9,7],
     [5,6,4,8,9,7,2,3,1],
     [8,9,7,2,3,1,5,6,4],
     [3,1,2,6,4,5,9,7,8],
     [6,4,5,9,7,8,3,1,2],
     [9,7,8,3,1,2,6,4,5]]

e=enumerate;print 243-len(set((a,t)for(i,r)in e(b)for(j,t)in e(r)for a in e([i,j,i/3*3+j/3]*(0<t<10))))

#print(list(range(1,10)))

#print(validate_sudoku(b1))
#print(validate_sudoku(b2))
#print(validate_sudoku(b3))

#print(validate_sudoku(b1))
#print(validate_sudoku(b2))
#print(validate_sudoku(b3))

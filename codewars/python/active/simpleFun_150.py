# https://www.codewars.com/kata/58aaa3ca821a767300000017/train/python
# Simple Fun #150: Robot Transfer


def retex(matrix,r,c,k):
    _r, _c = matrix[r][c]
    _k = 0
    for i in range(1,k+1):
        print(_r,_c)
        lm = matrix[_r][_c]
        
        if (_r,_c) == (r,c):
            break
        lm = matrix[_r][_c]
        _r, _c = lm[0],lm[1]
        _k += 1
    print("===")
    print(_r,_c,_k,k)
    print("===")

    return _k == k    
            
    
    
def robot_transfer(matrix, k):
    for i,r in enumerate(matrix):
        for j,c in enumerate(r):
            matrix[i][j] = [int(n) for n in matrix[i][j].split(',')]
    cnt = 0
    for i,r in enumerate(matrix):
        for j,c in enumerate(r):
            #print(i,j)
            if retex(matrix,i,j,k):
                cnt += 1
    return cnt            
            



print(robot_transfer([
         ["0,1","0,0","1,2"], 
         ["1,1","1,0","0,2"], 
         ["2,1","2,0","0,0"]],2))            
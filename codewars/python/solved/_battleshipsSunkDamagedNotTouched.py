# https://www.codewars.com/kata/58d06bfbc43d20767e000074/train/python
# Battle ships: Sunk damaged or not touched?

def damaged_or_sunk(board, attacks):
    def prboard(b):
        for l in b:
            print(l)
    
    def cnter(b):
        l = {}
        for x in range(len(b)):
            for y in range(len(b[0])):
                l[b[x][y]] = l.get(b[x][y],0) + 1
        return l

    prboard(board)
    pre = cnter(board)
    print(pre)
    
    
    for c in attacks:
        x = c[0] -1
        y = len(board) - c[1]
        if board[y][x] < 4:
            board[y][x] += 4
    
    prboard(board)        
    post = cnter(board)   
    print(post)
    
    res = {'sunk' : 0,
           'damaged' : 0,
           'not_touched' : 0,
           'points' : 0}

    for s in [1,2,3]:
        if s in pre:
            if post.get(s,0) == 0:
                res['points'] += 1
                res['sunk'] += 1
                continue
            if post.get(s,0) == pre.get(s,0):
                res['points'] -= 1
                res['not_touched'] += 1
                continue
            res['damaged'] += 1
            res['points'] += 0.5   


    return res



board = [ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1], 
          [0, 2, 0] ]

attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]

print(damaged_or_sunk(board, attacks))




"""
        result = damaged_or_sunk(board, attacks)
        test.assert_equals(result['sunk'], 1)
        test.assert_equals(result['damaged'], 1)
        test.assert_equals(result['not_touched'], 1)
        test.assert_equals(result['points'], 0.5)
"""        
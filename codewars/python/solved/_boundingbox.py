# https://www.codewars.com/kata/6644683b7c83db9ba33b7021/train/python
# Basic Bounding Box

# Return an array with the same shape as the input
def bounding_box(ia):
    fr,lr,fc,lc = None,None,None,None
    for r in range(len(ia)):
        for c in range(len(ia[0])):
            if ia[r][c] == 1:
                if fr == None:            fr = r 
                if  lr == None or r > lr: lr = r
                if fc == None or c < fc:  fc = c
                if lc == None or c > lc:  lc = c              
    res = [[0 for c in range(len(ia[0]))] for r in range(len(ia))] 
    for h in range(fc,lc+1):
        res[fr][h] = 1
        res[lr][h] = 1
    for v in range(fr,lr+1):
        res[v][fc] = 1
        res[v][lc] = 1
    return res

"""
res = bounding_box([[0,0,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,0,0,0,0]])
"""
res = bounding_box([[0,0,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0],
                                         [0,1,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,1,0,0,0],
                                         [0,0,0,1,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0,0,0]])

for l in res:
    print(l)


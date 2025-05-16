# https://www.codewars.com/kata/5464d6811e0c08e574000b76/train/python
# Stop the Zombie Apocalypse


def follow(x,y,n):
    seen.add((x,y))
    print(id(flags))
    flags[x][y] = 1
    for c in [(x+1,y), (x-1,y),(x,y+1),(x,y-1)]:
        if m.get(c,None) == n and c not in seen:
            follow(c[0],c[1],n)

def find_zombies(matrix):
    # Create Flag Matrix
    global m
    m = {}
    global seen
    seen = set()
    
    global flags 
    flags = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix)) ]
    print(id(flags))
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            m[(x,y)] = matrix[x][y]
    follow(0,0,matrix[0][0])
    return flags        






ex_1 =[
        [9, 1, 2],
        [9, 9, 9],
        [7, 4, 9],
        [7, 9, 7]
    ]
print(find_zombies(ex_1))

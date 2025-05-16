# https://www.codewars.com/kata/5576f6719988e71ea30000ae/train/python
# Flood Fill

def fill(x,y,n):
    seen.add((x,y))
    print(id(flags))
    for c in [(x+1,y), (x-1,y),(x,y+1),(x,y-1)]:
        if m.get(c,None) == n and c not in seen:
            fill(c[0],c[1],n)

def flood_fill(array, y, x, new_value):
    global m
    m = {}
    for x in range(len(array)):
        for y in range(len(array[x])):
            m[(x,y)] = array[x][y]

    global seen
    seen = set()
    fill(array,x,y,)

    return array


def find_zombies(matrix):
    # Create Flag Matrix
    
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            m[(x,y)] = matrix[x][y]

    follow(0,0,matrix[0][0])
    return flags        


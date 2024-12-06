import pprint





def check_rose(x,y,grid):
    xctr = 0
    for dir in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
        _x = x
        _y = y
        f = "X"
        for _ in range(3):
            _x += dir[0]
            _y += dir[1]
            if 0 <= _x < len(grid) and 0 <= _y < len(grid[0]):
                f += grid[_x][_y]
        if f == "XMAS":
            xctr += 1        
    return xctr

def check_mas(x,y,grid):
    if 1 <= x < len(grid)-1 and 1 <= y < len(grid[0])-1:
        cstr = grid[x-1][y-1] + grid[x-1][y+1] + grid[x+1][y+1] + grid[x+1][y-1]
        return cstr in ['MMSS','MSSM','SSMM','SMMS']  
    else:
        return False
    
            
grid = []

with open('day_04.txt') as f:
    for line in f:
        grid.append(list(line.strip()))

    gx_ctr = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'X':
                gx_ctr += check_rose(x,y,grid)
                
    print("Part 1:", gx_ctr)
 
    xm_ctr = 0
        
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'A':
                xm_ctr += check_mas(x,y,grid)

    print("Part 2:", xm_ctr)
    
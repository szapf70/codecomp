def pr_grid(grid):
    for r in grid:
        print("".join(r))

def get_start(grid):
    for x,r in enumerate(grid):
        if '^' in r:
            return (x, r.index('^'))

def in_grid(x,y,grid):
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))

facing = [('^',-1,0),('>',0,1),('v',1,0),('<',0,-1)]
grid = []

with open('showcase.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
   
x,y = get_start(grid)   
m_ctr = 0
while True:
    sym, offs_x, offs_y = facing[0] 
    next_x, next_y = x + offs_x, y + offs_y
    if in_grid(next_x, next_y, grid):
        if grid[next_x][next_y] == '#':    
            facing = facing[1:] + facing[:1]
            next_x, next_y = x + offs_x, y + offs_y
            if in_grid(next_x,next_y,grid):
                grid[x][y] = '.'
                x,y = x + offs_x, y + offs_y
                grid[x][y] = sym
                m_ctr += 1
                pr_grid(grid)
            
            else:
                break    
    else:
        break    
    




print(m_ctr, "Steps")

import copy
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
org_grid = []

visited = set()

with open('showcase.txt') as f:
    for line in f:
        org_grid.append(list(line.strip()))
   
x,y = get_start(org_grid)  
visited.add((x,y))
pr_grid(org_grid)

grid = copy.deepcopy(org_grid)

while True:
    grid[x][y] = 'X'
    next_x, next_y = x + facing[0][1], y + facing[0][2]
    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
        if grid[next_x][next_y] == '#':
            facing = facing[1:] + facing[:1]
            next_x, next_y = x + facing[0][1], y + facing[0][2]
        x = next_x
        y = next_y
        visited.add((x,y))
        grid[x][y] = facing[0][0]
    else:
        break    

print("".join(["".join(row) for row in grid]).count('X'))
print(len(visited))

endless = 0
for ox, oy in visited:
    grid = copy.deepcopy(org_grid)
    grid[ox][oy] = '#'
    pr_grid(grid)
    viscounter = 0
    while True:
        grid[x][y] = 'X'
        next_x, next_y = x + facing[0][1], y + facing[0][2]
        if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
            if grid[next_x][next_y] == '#':
                facing = facing[1:] + facing[:1]
                next_x, next_y = x + facing[0][1], y + facing[0][2]
            x = next_x
            y = next_y
            if (x,y) in visited:
                viscounter += 1
            else:
                print(viscounter)
                viscounter = 0
                visited.add((x,y))
            if viscounter > 500:
                endless += 1
                break
            grid[x][y] = facing[0][0]
        else:
            break 

print(endless)           

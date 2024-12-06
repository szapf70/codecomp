import copy
def pr_grid(grid,grid_c):
    for i in range(len(grid)):
        print("".join(grid[i]), "  ", "".join(grid_c[i]))

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
grid_c = copy.deepcopy(grid)   
grid_c[6][3] = 'O'
grid_c[7][6] = 'O'
grid_c[7][7] = 'O'
grid_c[8][1] = 'O'
grid_c[8][3] = 'O'
grid_c[9][7] = 'O'




x,y = get_start(grid)   
pr_grid(grid,grid_c)
obs_count = 0
visited = []


while True:
    next_x, next_y = x + facing[0][1], y + facing[0][2]
    if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
        if grid[next_x][next_y] == '#':
            facing = facing[1:] + facing[:1]
            next_x, next_y = x + facing[0][1], y + facing[0][2]
            visited.append(('turn',x,y))
        else:
            side_x, side_y = x + facing[1][1], y + facing[1][2]
            if ('turn',side_x,side_y) in visited or (facing[1][0],side_x,side_y) in visited:
                obs_count += 1


        visited.append((facing[0][0],x,y))
        x = next_x
        y = next_y
        grid[x][y] = facing[0][0]
        pr_grid(grid,grid_c)
        print(obs_count)
        input("Taste")
        #grid[x][y] = facing[0][0]
    else:
        break    



print("".join(["".join(row) for row in grid]).count('X'))
print(obs_count)
print(visited)

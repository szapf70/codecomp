

def load(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        grid = {}
        hiking_trails = []
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                h = int(lines[y][x])
                grid[(x,y)] = h
                if h == 0:
                    hiking_trails.append((x,y))

        return grid,hiking_trails

def follow_trail(grid,ht,plateaus):
    def get_slopes(grid,ht):
        slopes = []
        x,y = ht
        h = grid[ht]
        for ch in [(x,y-1),(x,y+1),(x+1,y),(x-1,y)]:
            if ch in grid:
                if grid[ch] == grid[ht] + 1:
                    slopes.append(ch)
        return slopes            
        
    if grid[ht] == 9:
        plateaus[ht] = plateaus.get(ht,0) + 1
        return
    slopes = get_slopes(grid,ht)
    for s in slopes:
        follow_trail(grid,s,plateaus)
    return        
    
    


    
grid, h_trails = load("puzzle.txt")        

distinct_sum = 0

for ht in h_trails:
    plat = dict()
    follow_trail(grid,ht,plat)
    distinct_sum += sum(plat.values())

print(distinct_sum)
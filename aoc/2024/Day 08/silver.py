import itertools



def load(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        field = {}
        ant = {}
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                sig = lines[y][x]
                field[(x,y)] = sig
                if not sig in ant:
                    ant[sig] = []
                ant[sig].append((x,y))
        ant.pop('.', None)
        return field, ant

def jumps(a,b):
    a_x, a_y = a
    b_x, b_y = b
    j1 = (a_x - (b_x - a_x),a_y - (b_y - a_y))
    j2 = (b_x - (a_x - b_x),b_y - (a_y - b_y))
    return j1,j2


field, ant = load('puzzle.txt')   

anti = set()

#print(ant)
print(field)
for sig in ant:
    if sig == '#':
        continue
    for a,b in itertools.combinations(ant[sig],2):
        anti_01, anti_02 = jumps(a,b)    
        if anti_01 in field:
            anti.add(anti_01)
        if anti_02 in field:
            anti.add(anti_02)   

print(len(anti))

        
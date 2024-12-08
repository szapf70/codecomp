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


    

def jumps(a,b,field):
    a_x, a_y = a
    b_x, b_y = b
    anti_x, anti_y = a_x, a_y
    res = []
    res.append((a_x,a_y))
    while True:
        anti_x -= (b_x - a_x)
        anti_y -= (b_y - a_y)
        _t = (anti_x,anti_y)
        if _t in field:
            res.append(_t)
        else:
            break  
    print(a,b,res)      
    return res


def i_jumps(a,b,field):
    res = []
    res = jumps(a,b,field) + jumps(b,a,field)
    return res

field, ant = load('puzzle.txt')   

anti = set()

#print(ant)
for sig in ant:
    if sig == '#':
        continue
    for a,b in itertools.combinations(ant[sig],2):
        anti = anti.union(i_jumps(a,b,field))    

print(len(anti))

        
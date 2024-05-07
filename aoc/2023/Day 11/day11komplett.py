from collections import defaultdict
import json
import sys

# faktor auf 2 für silber und 1000000 für gold

factor = 1000000

def calc_route(a,b):
    #print(a,b)
    sa, sb = (a[0], b[0]) if a[0] < b[0] else (b[0], a[0])
    koords = []
    for s in range(sa+1, sb+1):
        koords.append((s,a[1]))

    ea, eb = (a[1], b[1]) if a[1] < b[1] else (b[1], a[1])
    for s in range(ea+1, eb+1):
        koords.append((b[0],s))
    return koords
 



def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()
        

map = load("input.txt")

#leere reihen
erows = []
for r,l in enumerate(map):
    #print(r,l)
    if len(set(l)) == 1:
        erows.append(r)

print(erows)

# leere spalten
ecols = [i for i in range(0,len(map[0]))]

for c in range(0,len(map[0])):
    for line in map:
        for i,s in enumerate(line):
            if s != "." and i in ecols: 
                ecols.remove(i)

print(ecols)

# set expander and get raw galaxy coords

galaxies = {}
gcount = 1

for y,l in enumerate(map):
    lr = [*map[y]]
    for x in range(0,len(lr)):
        if lr[x] == "#":
            galaxies[gcount] = [x,y]
            gcount += 1
        if x in ecols or y in erows: lr[x] = 'X'
    map[y] = "".join(lr)

# get galaxies


pairs =[]

for o in range(1,gcount):
    for i in range(o+1,gcount):
        pairs.append((o, i))
    
tpairs = [(1,7)]
#for l in map:
    #print(l)    

sum_rl = 0
for pair in pairs:
    route = calc_route(galaxies[pair[0]],galaxies[pair[1]])
    #print(route)
    rl = 0
    for station in route:
        s = map[station[1]][station[0]]
        if s in '.#' : rl += 1
        if s == 'X': rl += factor
    #print(pairs,rl)
    sum_rl += rl
print(sum_rl)    
sys.exit()   

for l in map:
    print(l)    

print(galaxies)
print(pairs, len(pairs))          

sys.exit()    






for x in range(0,len(map[0])):
    for y in range(0, len(map)):
        if x in ecols and y in erows:
            rl = []
            map[x][y] = "X"        

for l in map:
    print(l)

sys.exit()










map = load("input.txt")
map270 = list(zip(*map))[::-1]    
ex270 = []
for c, l in enumerate(map270):
    if len(set(l)) == 1: ex270.insert(0,c)
for c in ex270: map270.insert(c,map270[ex270[-1]])     
map90 = list(zip(*map270[::-1]))
ex90 = []
for c, l in enumerate(map90):
    if len(set(l)) == 1: ex90.insert(0,c)
for c in ex90: map90.insert(c,map90[ex90[-1]])  

# ident galaxys
galaxies = {}
gcount = 1
for y, c in enumerate(map90):
    for x, s in enumerate(c):
        if s == '#': 
            galaxies[gcount] = [x, y]
            gcount += 1
        
# calculate pairs
g = [1,2,3,4,5,6,7,8,9]

pairs =[]

for o in range(1,gcount):
    for i in range(o+1,gcount):
        pairs.append((o, i))
        
print(pairs, len(pairs))          
print(galaxies)

sum_dist = 0
for pair in pairs:
    a = galaxies[pair[0]]
    b = galaxies[pair[1]]
    sum_dist += abs(a[0]-b[0])+abs(a[1]-b[1])

print(sum_dist)    
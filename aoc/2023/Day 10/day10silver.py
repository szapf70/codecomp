from collections import defaultdict
import json
import sys


def load(fname):
    with open(fname) as txt:
        l = txt.read().splitlines()
        for i in range(0,len(l)):
            l[i] = "."+l[i]+"."
        l.insert(0,"." * (len(l[0])))
        l.append("." * (len(l[0])))
        return l    


def getfield(y,x,dir = None):
    dirs = {'N' : (-1,0), 'E' : (0,1), 'S' : (1,0), 'W' : (0,-1)}    
    ly, lx = y, x
    if dir:
        dy, dx = dirs[dir]
        ly += dy
        lx += dy 


def fnv(y,x):
    if field[y][x] == "S": 
        pass
    
    #if dir != field[y-]
    pass

def fn():
    nl = ""
    af = field[sy][sx]
    nf =field[sy-1][sx]
    ef = field[sy][sx+1]
    sf =field[sy+1][sx]
    wf =field[sy][sx-1] 
    #print(af,nf,ef,sf,wf)
    if af in 'SL|J' and nf in 'S7|F': nl += 'N'
    if af in 'SL-F' and ef in 'S-7J': nl += 'E'
    if af in 'S7|F' and sf in 'SL|J': nl += 'S'
    if af in 'S7-J' and wf in 'SL-F': nl += 'W'
    #print("<-",nl)
    return nl


field = load("input.txt")
sx = -1
sy = -1
ld = None
steps = 0
for y, l in enumerate(field): 
    sx = l.find("S")
    if sx != -1:
        sy = y
        break    

opp = {"N":"S","E":"W","S":"N","W":"E"}
dirs = {'N' : {"dy" :-1, "dx" : 0, "l" : "S"},
        'E' : {"dy" : 0, "dx" : 1, "l" : "W"}, 
        'S' : {"dy" : 1, "dx" : 0, "l" : "N"}, 
        'W' : {"dy" : 0, "dx" : -1, "l" : "E"}}    

#while steps and field[sy][sx] != 'S':
while True:
    pn = fn()
    #print("Nachbarn", field[sy][sx],pn,ld,sy,sx)
    if ld and ld in 'NSEW': 
        pn = pn.replace(ld,"")
    else: pn = pn[:1]
    #print("-<",pn)
    steps += 1
    sy += dirs[pn[0]]['dy']
    sx += dirs[pn[0]]['dx']
    ld = dirs[pn[0]]['l']
    if field[sy][sx] == 'S': break
    #print("Nachbarn",field[sy][sx], pn,ld,sy,sx,opp[ld])

    #print("-" * 10)
    #input()
print(steps/2)



 
from collections import defaultdict
import json
import sys


def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()
 
def diffdown(hist):
    dd = [hist] 
    while any(dd[0]):
        dd.insert(0,[dd[0][i+1]-dd[0][i] for i in range(0,len(dd[0])-1)])
    return dd
    
def extraup(downed):
    ld = downed.copy()
    ld[0].append(0)
    for d in range(1,len(downed)):
        ld[d].append(ld[d][-1]+ld[d-1][-1])
    return ld

def preextraup(downed):
    #print(downed)
    ld = downed.copy()
    ld[0].insert(0,0)
    #print(ld)
    for d in range(1,len(ld)):
        ld[d].insert(0,ld[d][0]-ld[d-1][0])
        #print(ld)
    return ld



lines = load("input.txt")
hists = [list(map(int,line.split())) for line in lines]
nv_sum = 0
for hist in hists:
    downed = diffdown(hist)
    #print(downed)
    upped = preextraup(downed)
    #print(upped)
    #nv_sum += upped[-1][-1]
    nv_sum += upped[-1][0]
print(nv_sum)    
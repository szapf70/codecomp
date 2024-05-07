from collections import defaultdict
import json
import sys
import itertools

def checkmirror(map):
    rmap = [''] * len(map[0])
    for l in map:
        for i in range(0, len(l)):
            rmap[i] += l[i]
    lines = {}
    rlines = {}
    for num,line in enumerate(map,start=1):
        lines.setdefault(line,[]).append(num)
    for num,line in enumerate(rmap,start=1):
        rlines.setdefault(line,[]).append(num)
    for line in list(lines.keys()):
        if len(lines[line]) != 2:
            lines.pop(line)
    for rline in list(rlines.keys()):
        if len(rlines[rline]) != 2:
            rlines.pop(rline)

    lv = list(lines.values())
    rv = list(rlines.values())

    print(len(map), len(map[0])) 
    print("================================================================")  

    
    if lv and (lv[0][0] == 1 or lv[0][1] == len(map)):
        return lv[-1][0] * 100    
    if rv and (rv[0][0] == 1 or rv[0][1] == len(map[0])):
        return rv[-1][0]
    return 0



def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

maps = []
lines = load("input.txt")

llines = []
for line in lines:
    if line != "": llines.append(line)
    else:
        maps.append(llines)
        llines = []
maps.append(llines)

sum = 0
for map in maps:
    sum += checkmirror(map)
print(sum)
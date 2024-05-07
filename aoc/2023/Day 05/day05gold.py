import sys
import time
import re

def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()


lines = load("example.txt")
seedline = lines.pop(0)
lines.pop(0)
seeddata = list(map(int, re.findall('\d+', seedline)))
print(seeddata)
seedpairs = [(seeddata[idx], seeddata[idx] + seeddata[idx+1] - 1) for idx in range(0,len(seeddata),2)]
print("================================================================")
print(seedpairs)

# maps einlesen
maps = []
imaps = []

while lines:
    line = lines.pop(0)
    if line.endswith('map:'):
        imaps = []
        continue
    if line:
        imaps.append(list(map(int,line.split())))
        continue
    maps.append(imaps)
maps.append(imaps)
print(maps)
locations = []
for lo, hi in seedpairs:
    print("Neues Seedpair...", lo,hi)
    for lmaps in maps:
        print("Neues lmap...",lmaps,lo,hi)
        for smap in lmaps:
            print("Neues smap...", smap,lo,hi)
            if hi < smap[1] or lo > (smap[1] + smap[2] - 1): continue
            print(smap, lo,hi)
            hldiff = hi -lo
            lo = smap[0] + (lo - smap[1])
            hi = lo + hldiff
            print(smap,lo,hi,"Angepasst - nächstes lmap")
            break
    locations.append((lo,hi))

print(sorted(locations))

"""
seedpairs =  numbers 
[(lo, hi) for   
             pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
             """
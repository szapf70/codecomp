import re


def checkways(rdata):
    numways = 0
    for pressed in range(1,rdata[0]):
        if (rdata[0] - pressed)*pressed > rdata[1]: numways+=1
    return numways        
    

def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

lines = load("input.txt")
times = list(map(int,re.findall("\d+", lines[0])))
dists = list(map(int,re.findall("\d+", lines[1])))
races = tuple(zip(times,dists))

raceprod = 1
for race in races:
    raceprod*=checkways(race)

print(raceprod)

#races = zip(list(map(int,re.findall("/d+", lines[0]))),list(map(int,re.findall("/d+", lines[1]))))
#print(races)
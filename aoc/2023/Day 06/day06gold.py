import re


def checkways(time,dist):
    numways = 0
    for pressed in range(1,time):
        if (time - pressed)*pressed > dist: numways+=1
    return numways        
    

def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

lines = load("input.txt")
time = int("".join(list((re.findall("\d+", lines[0])))))
dist = int("".join(list((re.findall("\d+", lines[1])))))

ways = checkways(time,dist)
print(ways)
#print(raceprod)

#races = zip(list(map(int,re.findall("/d+", lines[0]))),list(map(int,re.findall("/d+", lines[1]))))
#print(races)
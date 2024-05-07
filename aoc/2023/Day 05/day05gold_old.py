import sys
import time

def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

def mapper(item, maps):
    #print(item, maps)
    for map in maps:
        #print(item, map[1], map[2])
        #if item in range(map[1], map[1] + map[2]):
        if item >= map[1] and item < map[2]:
           return map[0] + (item - map[1])
    return item

def multimapper(srcrange, destranges):
    print(srcrange, destranges)
    lsrcrange = srcrange
    for destrange in destranges:
        if srcrange[0] >= destrange[1] and srcrange[1] <= destrange[2]:
            print("Matched",lsrcrange, destrange)

            rd = destrange[0] - destrange[1]
            lsrcrange = (lsrcrange[0] + rd, lsrcrange[1] + rd)
            print("Changed",rd,lsrcrange, destrange)
    print(lsrcrange)
    return lsrcrange

"""  
def mapper(item, map)
    if item >= map[1] and item < map[1] + map[2]:
        return map[0] + (item - map[1])
    return item
"""    
almanac = {}    
    
lines = load("example.txt")
seedsall = 0
# Seeds einlesen, ändern für gold
almanac['seedspre'] = [int(s) for s in lines.pop(0)[6:].split()]
#print(almanac['seedspre'])
almanac['seedranges'] = []
while almanac['seedspre']:
    s, r = (almanac['seedspre'].pop(0),almanac['seedspre'].pop(0))
    almanac['seedranges'].append((s, s+r-1))
    seedsall += r
#print(almanac['seedranges'])
print(seedsall, "Seeds")

lines.pop(0)
#sys.exit()
# maps einlesen
key = ""
while lines:
    line = lines.pop(0)
    if line.endswith("map:"):
        key = line.split()[0]
        almanac[key] = []
        continue
    if line == "": continue
    temp = list(map(int,line.split()))
    temp.insert(2, temp[1] + (temp[2]-1))
    almanac[key].append(temp)

lowpos = seedmin = 1000000000000
seedmax = 0
actseed = 0
timestart = time.time()

for smin, smax in almanac['seedranges']:
    spos = smin
    while spos <= smax:
        lowpos = min(resolveseed(spos),lowpos) 
        spos += 1
        actseed +=1
        if actseed % 1000000 == 0:
            timeact = time.time() - timestart
            timeleft = timeact * (seedsall/actseed)
            print(f"{smin:12}, {smax:12}, {actseed:12}, {seedsall:12}/{seedsall-actseed:12}, {timeact:5.2f}/{timeleft:5.2f}, {lowpos:12}")    
    #'{0:,}'.format(1000000)
#print(seedmin, seedmax, seedmax-seedmin) 
#print(resolveseed(1047354752))
sys.exit()




minloc = 1000000000000000000
seedsall = 0

soilranges = []
fertilizerranges = []
waterranges = []
lightranges = []
temperatureranges = []
humidityranges = []
locationranges = []

for seedrange in almanac['seedranges']:
    soilranges.append(multimapper(seedrange,almanac['seed-to-soil']))
    
for soilrange in soilranges:
    fertilizerranges.append(multimapper(soilrange, almanac['soil-to-fertilizer']))
for fertilizerrange in fertilizerranges:
    waterranges.append(multimapper(fertilizerrange, almanac['fertilizer-to-water']))
for waterrange in waterranges:
    lightranges.append(multimapper(waterrange, almanac['water-to-light']))
for lightrange in lightranges:
    temperatureranges.append(multimapper(lightrange, almanac['light-to-temperature']))
for temperaturerange in temperatureranges:
    humidityranges.append(multimapper(temperaturerange, almanac['temperature-to-humidity']))
for humidityrange in humidityranges:
    locationranges.append(multimapper(humidityrange, almanac['humidity-to-location']))
    
print(soilranges)
print(fertilizerranges)
print(waterranges)
print(lightranges)
print(temperatureranges)
print(humidityranges)
print(locationranges)

    #print(soilrange)
    #fertilizerrange = multimapper(soilrange, almanac['soil-to-fertilizer'])
    #waterrange = multimapper(fertilizerrange, almanac['fertilizer-to-water'])
    #lightrange = multimapper(waterrange, almanac['water-to-light'])
    #temperaturerange = multimapper(lightrange, almanac['light-to-temperature'])
    #humidityrange = multimapper(temperaturerange, almanac['temperature-to-humidity'])
    #locationrange = multimapper(humidityrange, almanac['humidity-to-location'])
    #print("locationrange",locationrange) 
    #print("soilrange",soilrange)   
    
    
    
"""    
    print(f"{seednum} from {seedsall}")
    soil = mapper(seedrange, almanac['seed-to-soil'])
    fertilizer = mapper(soil, almanac['soil-to-fertilizer'])
    water = mapper(fertilizer, almanac['fertilizer-to-water'])
    light = mapper(water, almanac['water-to-light'])
    temperature = mapper(light, almanac['light-to-temperature'])
    humidity = mapper(temperature, almanac['temperature-to-humidity'])
    location = mapper(humidity, almanac['humidity-to-location'])
    minloc = min(minloc, location)
    seed += 1
    seednum += 1
"""

#print(minloc)

#print(almanac)    
    
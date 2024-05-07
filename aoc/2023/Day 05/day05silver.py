def load(fname):
    with open(fname) as txt:
        return txt.read().splitlines()

def mapper(item, maps):
    for map in maps:
        #print(item, map[1], map[2])
        if item in range(map[1], map[1] + map[2]):
           return map[0] + (item - map[1])
    return item
def resolveseed(seed):
    soil = mapper(seed, almanac['seed-to-soil'])
    fertilizer = mapper(soil, almanac['soil-to-fertilizer'])
    water = mapper(fertilizer, almanac['fertilizer-to-water'])
    light = mapper(water, almanac['water-to-light'])
    temperature = mapper(light, almanac['light-to-temperature'])
    humidity = mapper(temperature, almanac['temperature-to-humidity'])
    location = mapper(humidity, almanac['humidity-to-location'])
    return location

"""  
def mapper(item, map):
    if item >= map[1] and item < map[1] + map[2]:
        return map[0] + (item - map[1])
    return item
"""    
almanac = {}    
    
lines = load("example.txt")

# Seeds einlesen
almanac['seeds'] = [int(s) for s in lines.pop(0)[6:].split()]
lines.pop(0)

# maps einlesen
key = ""
while lines:
    line = lines.pop(0)
    if line.endswith("map:"):
        key = line.split()[0]
        almanac[key] = []
        continue
    if line == "": continue
    almanac[key].append(list(map(int,line.split())))

minloc = 1000000000000000000


print(resolveseed(82))
"""

for seed in almanac['seeds']:
    soil = mapper(seed, almanac['seed-to-soil'])
    fertilizer = mapper(soil, almanac['soil-to-fertilizer'])
    water = mapper(fertilizer, almanac['fertilizer-to-water'])
    light = mapper(water, almanac['water-to-light'])
    temperature = mapper(light, almanac['light-to-temperature'])
    humidity = mapper(temperature, almanac['temperature-to-humidity'])
    location = mapper(humidity, almanac['humidity-to-location'])
    minloc = min(minloc, location)

"""
#print(minloc)

#print(almanac)    
    
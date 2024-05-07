import sys

# Expanded version of schematic
scheme = []
# Partnumbers found
pnumbers = []

def checkflat(x,y):
    lAdjc = 0
    lAdj = [(x-1,y-1),(x,y-1),(x+1,y-1),
            (x-1,y),(x,y),(x+1,y),
            (x-1,y+1),(x,y+1),(x+1,y+1)]
    for x, y in lAdj:
        if not scheme[y][x] in ['0', '1', '2', '3', '4', '5', '6', '7', '8','9','.']:
            lAdjc +=1
    return lAdjc


with open("input.txt") as txt:
    raw_lines = txt.read().splitlines()
    scheme.extend(["."+raw+"." for raw in raw_lines])
  
    scheme.insert(0,"." * (len(raw_lines[0]) + 2))
    scheme.append("." * (len(raw_lines[0]) + 2))
    
    y = 0
    
    while y < len(scheme):
        x = 0
        while x < len(scheme[0]):
            # Wenn keine Zahl, weiter
            if not scheme[y][x].isdigit():
                x += 1
                continue
            # Hier ist ne Zahl, bis zum Ende gehen und checken.
            aAdjc = 0
            aNum = ""
            while scheme[y][x].isdigit():
                aNum += scheme[y][x]
                if checkflat(x,y):  aAdjc = 1
                x += 1
            if aAdjc: pnumbers.append(aNum) 
        y += 1       
    sum = 0
    print(pnumbers)
    for pnum in pnumbers:
        sum += int(pnum)
    print(sum)

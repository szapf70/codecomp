# schematic
scheme = []
# Partnumbers found
pnumbers = []
# Gears found
gears = []
validgears = []





def checkgear(gear):
    lAdj = []
    for number in pnumbers:
        if number['y'] < gear['y']-1 or number['y'] > gear['y']+1:
            continue
        if number['start'] > gear['x']+1 or (number['start'] + number['len']) < gear['x'] :
            continue
        lAdj.append(number)
    if len(lAdj) == 2:
        validgears.append(lAdj)
    return    

with open("input.txt") as txt:
    raw_lines = txt.read().splitlines()
    scheme.extend(["."+raw+"." for raw in raw_lines])
  
    scheme.insert(0,"." * (len(raw_lines[0]) + 2))
    scheme.append("." * (len(raw_lines[0]) + 2))
  
    # Collect all number
    y = 0
    while y < len(scheme):
        x = 0
        while x < len(scheme[0]):
            if scheme[y][x] == '*':
                gears.append({'x': x, 'y': y})
                x += 1
                continue
            if not scheme[y][x].isdigit():
                x += 1
                continue
            # number starts save x
            startx = x
            aNum = ""
            print(f"Actual y/x {y}/{x}")
            while scheme[y][x].isdigit():
                aNum += scheme[y][x]
                x += 1
            pnumbers.append({"num" : aNum, "y" : y, "start" : startx, "len" : x - startx}) 
        y += 1       
    
    # collect valid gears
    for gear in gears:
        checkgear(gear)
    sum = 0
    for validgear in validgears:
        sum += int(validgear[0]['num']) * int(validgear[1]['num'])
    print(sum)
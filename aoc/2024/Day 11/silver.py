import math

def blink(stns):
    _stns = []
    for stn in stns:
        if stn == 0:
            _stns.append(1)
            continue        
        _l = math.floor(math.log10(stn)) + 1   
        if _l % 2:
            _stns.append(stn*2024)
        else:
            left, right = divmod(stn, 10**(_l//2))
            _stns.append(left)
            _stns.append(right)     

    return _stns


stones_01 = "0 1 10 99 999"
stones_02 = "125 17"
puzzle = "112 1110 163902 0 7656027 83039 9 74"

stones = list(map(int, puzzle.split()))
print(len(stones), stones)
for nblink in range(25):
    stones = blink(stones)
    print(nblink+1, len(stones))    
    
    






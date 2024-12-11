import math
from functools import cache
from numba import jit

@cache
def rules(stn):
    if stn == 0:
        return [1]
    _l = math.floor(math.log10(stn)) + 1   
    if _l % 2:
        return [stn*2024]
    else:
        left, right = divmod(stn, 10**(_l//2))
        return [left,right]



def blink(stns):
    _stns = []
    for stn in stns:
        _stns += rules(stn)
    return _stns


stones_01 = "0 1 10 99 999"
stones_02 = "125 17"
puzzle = "112 1110 163902 0 7656027 83039 9 74"

stones = list(map(int, puzzle.split()))
print(len(stones), stones)
for nblink in range(75):
    stones = blink(stones)
    print(nblink+1, len(stones))    
    
    






import numpy as np
from numba import jit
# https://github.com/PetitCoinCoin/advent-of-code-24/blob/main/day_11.py
@jit(nopython=True)
def blink(stns):
    _stns = []
    for stn in stns:
        if stn == 0:
            _stns.append(1)
            continue
        _l = int(np.floor(np.log10(stn))) + 1
        if _l % 2:
            _stns.append(stn * 2024)
        else:
            left, right = divmod(stn, 10**(_l // 2))
            _stns.append(left)
            _stns.append(right)
    return np.array(_stns)

stones_01 = "0 1 10 99 999"
stones_02 = "125 17"
puzzle = "112 1110 163902 0 7656027 83039 9 74"

stones = np.array(list(map(int, puzzle.split())))
print(len(stones), stones)
for nblink in range(25):
    stones = blink(stones)
    print(nblink+1, len(stones))







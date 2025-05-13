# 
# Alex & snooker: points earned.

import re

def frame(balls):
    s = {'R':1,'Y':2,'G':3,'N':4,'E':5,'P':6,'K':7}
    if 'W' in balls: return 'Foul'
    balls = balls.replace('Bn', 'N').replace('Be', 'E').replace('Bk', 'K')
    pnts = 0
    p = []
    for e in re.findall(r'[A-Z]+|\d+', balls):
        if e.isnumeric():
            p.append(int(e))
        else:
            p.extend(list(e))    
    
    while p:
        c = p.pop(0)
        if p:
            if isinstance(p[0], int):
                pnts += (p.pop(0)-1) * s[c]
        pnts += s[c]
    
    if pnts > 147:
        return 'invalid data'
    return pnts


print(frame('Bk16YGBnBeP'))

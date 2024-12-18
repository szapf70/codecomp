# https://www.codewars.com/kata/57c7930dfa9fc5f0e30009eb/train/python
# Closest Perfect Power

import sys

def closest_power(n):
    if n <= 4:
        return 4
    l = []
    s = 2
    while True:
        ls = int(n**(1/s))
        l.append((abs(n-ls**s),ls**s))
        l.append((abs(ls+1)**s-n,(ls+1)**s))
        if ls == 1:
            break
        s += 1
    return sorted(l)[0][1]    



print(closest_power(0),4)
print(closest_power(9), 9)
print(closest_power(30), 32)
print(closest_power(32), 32)
print(closest_power(34), 32)
print(closest_power(123321456654), 123321773584)
"""



"""    
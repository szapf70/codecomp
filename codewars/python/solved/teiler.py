# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
# Integers: Recreation One

from functools import cache

@cache
def divs(n):
    s = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            s += i*i
    s += n*n
    return s

def list_squared(m, n):
    res = []
    for i in range(m, n+1):
        s = divs(i)
        if s**0.5 == int(s**0.5):
            res.append([i,s])
    return res

# Beispielaufruf
print(list_squared(42,250))  # Gibt [1, 2, 3, 4, 6, 12] aus
print(divs(246))
# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python
# Gap in Primes

from functools import cache
from itertools import pairwise

@cache
def isprime(x):
    for i in range(2, 2+int(x**0.5)):
        if (x%i) == 0:
            return False
    return True

def prime(n):
    if n < 2 :return []
    res = [2]
    pt = 2
    while res[-1] <= n:
        pt += 1
        if isprime(pt):
            res.append(pt)
    return res[:-1]        


print(prime(15))
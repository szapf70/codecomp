# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python
# Steps in Primes

from gmpy2 import is_prime, next_prime

def step(g, m, n):
    if g > n-m: return None
    res = []
    f = m if is_prime(m) else next_prime(m)    
    s = f + g
    while f <= n:
        if is_prime(s):
            return [int(f),int(s)]
        f = next_prime(f)
        s = f + g
    return None

print(step(2,5,5))
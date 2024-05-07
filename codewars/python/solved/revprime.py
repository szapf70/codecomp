# https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python
# Backwards Read Primes

from functools import cache

@cache
def is_prime(nstr):
    n = int(nstr)
    for i in range(2,int(n/2)+1):
        if n/i == int(n/i):
            return False
    return True    


def backwards_prime(start, stop):
    res = []
    for pt in range(start,stop+1):
        pts = str(pt)
        if not pts == pts[::-1]:
            if is_prime(pt):
                if is_prime(int(pts[::-1])):
                    res.append(pt)
    return res

print(backwards_prime(1,97))
print([13, 17, 31, 37, 71, 73, 79, 97])
        
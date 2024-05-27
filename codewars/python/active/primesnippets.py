# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
# Primes in numbers


pt = [2]

def fillPrimeTable(n):
    for n in range(pt[-1]+1,n+1):
        isPrime = True
        lidx = 0
        thres = int(n**0.5)
        while pt[lidx] <= thres:
            if n%pt[lidx] == 0:
                isPrime = False
            lidx += 1
        if isPrime:
            pt.append(n)        

def prime_factors(n):
    ns = n
    nt = int(n**0.5)+1
    fillPrimeTable(nt)
    print(pt)
    fac = []
    pidx = 0
    while n > 1 and pidx < len(pt) and pt[pidx] <= nt :
        if ns%pt[pidx] == 0:
            fac.append(pt[pidx])
            ns = ns // pt[pidx]
        else:
            pidx += 1
    if ns == n:
        fac.append(n)
    
    return "".join([f"({n}**{fac.count(n)})" if fac.count(n) > 1 else f"({n})" for n in list(sorted(set(fac)))])


print(prime_factors(201))
#fillPrimeTable(20)
#print(pt)


"""
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
        test.assert_equals(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        test.assert_equals(prime_factors(7919), "(7919)")
import re


def isprime(n):
    return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None

print [x for x in range(100) if isprime(x)]

###########Output#############
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""
# https://www.codewars.com/kata/5626ec066d35051d4500009e/train/python
# The Sum Of The Prime Factors Of a Number... What For?

from gmpy2 import is_prime

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
    fac = []
    pidx = 0
    while n > 1 and pidx < len(pt) and pt[pidx] <= nt :
        if ns%pt[pidx] == 0:
            fac.append(pt[pidx])
            ns = ns // pt[pidx]
        else:
            pidx += 1
    if ns > 1:
        fac.append(ns)
    return fac


def mult_primefactor_sum(a, b): # [a, b] range of numbers included a and b
    res = []
    for n in range(a, b+1):
        if not is_prime(n):
            pf = prime_factors(n)
            pfs = sum(pf)
            if not n%pfs:
                res.append(n)
    return res

print(mult_primefactor_sum(10,100))

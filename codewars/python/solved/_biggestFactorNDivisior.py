# https://www.codewars.com/kata/5646ac68901dc5c31a000022/train/python
# Give The Biggest Prime Factor And The Biggest Divisor Of A Number

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

def big_primefac_div(n):
    print(type(n),n)
    if n != int(n): return "The number has a decimal part. No Results"
    n = abs(int(n))
    if is_prime(n): return []
    pf = prime_factors(n)
    return [pf[-1], n//pf[0]]
print(big_primefac_div(-1800))
print(big_primefac_div(1969.1))

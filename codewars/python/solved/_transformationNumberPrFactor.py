# https://www.codewars.com/kata/572caa2672a38ba648001dcd/train/python
# Transformation of a Number Through Prime Factorization



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

def f(n):
    prf = prime_factors(n)
    if prf[0] == n: return 1
    res = 1

    for f in set(prf):
        c = prf.count(f)
        res = res * (c * f**(c-1))
    return res     


print(f(24500))






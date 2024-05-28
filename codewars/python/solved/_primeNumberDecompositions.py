# https://www.codewars.com/kata/53c93982689f84e321000d62/train/python
# Prime number decompositions

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

def getAllPrimeFactors(n):
    if not type(n) is int:
        return []
    if n < 0:
        return []
    if n == 0: return []
    if n == 1: return [1]
    if n == 2: return [2]
    return prime_factors(n)


def getUniquePrimeFactorsWithCount(n):
    if not type(n) is int:
        return [[],[]]
    if n < 0:
        return [[],[]]

    if n == 0: return [[],[]]
    if n == 1: return [[1],[1]]
    if n == 2: return [[2],[1]]

    pf = prime_factors(n)
    f = []
    c = []
    for i in sorted(set(pf)):
        f.append(i)
        c.append(pf.count(i))
    return [f,c]


def getUniquePrimeFactorsWithProducts(n):
    if not type(n) is int:
        return []
    if n < 0:
        return []

    if n == 0: return []
    if n == 1: return [1]
    if n == 2: return [2]
    pf = prime_factors(n)
    res = []
    for n in set(pf):
        res.append(n**pf.count(n))
    return res
print(getAllPrimeFactors(100))
print(getUniquePrimeFactorsWithCount(100))
print(getUniquePrimeFactorsWithProducts(100))

    
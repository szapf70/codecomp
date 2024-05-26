# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python
# Common Denominators

import math

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

def lcm(nums):
    pf = []
    spf = set()
    res = 1
    for n in nums:
        lpf = prime_factors(n)
        pf.append(lpf)
        spf.update(lpf)
    for p in spf:
        pm = 0
        for pfe in pf:
            pc = pfe.count(p)
            if pc > pm: pm = pc
        res *= p*pm
    return res
    
def convert_fracts(lst):
    llcm = lcm([l[1] for l in lst])
    return [[l[0]*(llcm//l[1]),llcm] for l in lst]




# halb fertig


a = [[1, 2], [1, 3], [1, 4]]
#print(lcm([130,1310,4]))

print(convert_fracts(a))

"""
        a = [[1, 2], [1, 3], [1, 4]]
        b = [[6, 12], [4, 12], [3, 12]]

"""    
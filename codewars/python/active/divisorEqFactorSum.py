# https://www.codewars.com/kata/562c04fc8546d8147b000039/train/python
# When The Sum of The Divisors Is A Multiple Of The Prime Factors Sum


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




def ds_multof_pfs(nMin, nMax):
    res = []
    for n in range(nMin, nMax+1):
        pf = prime_factors(n)
        dv = {1,n}
        pfs = set(pf)
        dv.update(pf)
        for lpfs in pfs:
            for p in range(1,pf.count(lpfs)+1):
                dv.add(n//(lpfs**p))    
            if not sum(dv)%sum(pf):
                print(n,pf,sum(pf),dv,sum(dv))
                res.append(n)
    return res   


#print(prime_factors(12))
print(ds_multof_pfs(10,100))
#print(104%13)
# https://www.codewars.com/kata/534a0c100d03ad9772000539/train/python
# Prime factorization

class PrimeFactorizer:
    def __init__(self,value):
        self.value = value
        self.pt = [2] 
        self.factor = {}  
        tfc = self.prime_factors(self.value)
        print(tfc)
        for i in set(tfc):
            self.factor[i] = tfc.count(i)    

    def fillPrimeTable(self,n):
        for n in range(self.pt[-1]+1,n+1):
            isPrime = True
            lidx = 0
            thres = int(n**0.5)
            while self.pt[lidx] <= thres:
                if n%self.pt[lidx] == 0:
                    isPrime = False
                lidx += 1
            if isPrime:
                self.pt.append(n)        

    def prime_factors(self,n):
        ns = n
        nt = int(n**0.5)+1
        self.fillPrimeTable(nt)
        fac = []
        pidx = 0
        while n > 1 and pidx < len(self.pt) and self.pt[pidx] <= nt :
            if ns%self.pt[pidx] == 0:
                fac.append(self.pt[pidx])
                ns = ns // self.pt[pidx]
            else:
                pidx += 1
        if ns > 1:
            fac.append(ns)
        return fac    
    
    
print(PrimeFactorizer(24).factor)    
        
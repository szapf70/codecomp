# https://www.codewars.com/kata/5bc027fccd4ec86c840000b7/train/python
# Simple sum of pairs

from functools import cache
from math import log10

@cache
def quer(n):
    return sum([int(d) for d in str(n)])    
    
def solve_old(n): 
    # return max([sum([int(d) for d in str(i)+str(n-i)]) for i in range(n+1)])
    l = 0
    for i in range(n//2+1):
        nquer = quer(i)+quer(n-i)
        print(i,n-i,nquer)
        if nquer > l: l = nquer
    return l     

def solve_old2(n):
    a = 10**int(log10(n))-1
    b = n - a
    qstr = str(a) + str(b)
    res = sum([int(d) for d in qstr])
    return res

def solve(n):
    a = 10**int(log10(n))-1
    s = str(a)+str(n-a)
    return sum([int(d) for d in s])



    

print(solve(18))
print(solve(29))        
print(solve(45))        
print(solve(1140))        
print(solve(7019))        
        
        
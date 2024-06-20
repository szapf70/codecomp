# https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python
# Irreducible Sum of Rationals

from math import gcd

def sum_fracts(lst):
    if lst == []:
        return None
    n = 0
    d = 1
    for b in lst:
        d *= b[1]
    for i in range(len(lst)):
        n += lst[i][0] * d//lst[i][1]
    g=gcd(n,d)
    if d == 1:
        return n
    return [n//g,d//g]
    
    
    
    
lst = [[1,2],[1,3],[1,4]]
    
print(sum_fracts(lst))    
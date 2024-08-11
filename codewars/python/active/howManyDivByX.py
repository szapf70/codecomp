# https://www.codewars.com/kata/62204bb40e88a5004a662265/train/python
# How Many are Divisible by x    

import math

def how_many(m, x):
    if m < 0:
        return 0
    xp = x.split()
    a = min(int(xp[0]),int(xp[2]))
    b = max(int(xp[2]),int(xp[0]))
    c = math.lcm(a,b)
    op = xp[1]
    res = 0

    if op == 'and':
        if b%a == 0:
            return m//b
        else:
            return m//c
        
    if op == 'or':
            if a == b:
                return m//a
            
            return (m//a - m//c) + (m//b - m//c)
    
n = 668237867
a = n//4
b = n//14
c = n//math.lcm(4,14)
print(n,a,b,c)
print(a+b-c)
#print(math.lcm(12,18))

     

"""
m:668237867 x:'4 or 14': 202857923 should equal 190925104
"""     
#print(how_many(1000, "2 or 9")) # should return 556
#print(how_many(1000, "2 and 9")) # should return 55
#print(how_many(200, "10 or 10")) # should return 20
    
    
"""
from 1 to 1000, random chosen number of numbers being multiple of 2 or 9 is 556

m: max range starting from 1
x: string with two numbers with "and" and  "or"

"""

  
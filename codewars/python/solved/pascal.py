# https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python
# Pascal's Triangle

from functools import cache
from itertools import pairwise,chain


def npl(l): # Next Pascal line after given.
    return [i+j for i,j in pairwise([0] + l + [0])]




def pascal(p):
    r = [1]
    res = [[1]]
    for i in range(1,p):
        r = npl(r)
        res.append(r)
    return res   


print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))

#print(npl([1]))


"""
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
"""
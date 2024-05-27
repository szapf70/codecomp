# https://www.codewars.com/kata/5a908da30025e995880000e3/train/python
# Simple prime streaming

from functools import cache

@cache
def create_stream(c):
    pt = [2,3]    
    stream = ""

    for n in range(pt[-1]+1,c+1):
        isPrime = True
        lidx = 0
        thres = int(n**0.5)
        while pt[lidx] <= thres:
            if n%pt[lidx] == 0:
                isPrime = False
            lidx += 1
        if isPrime:
            pt.append(n)       
    stream = "".join([str(i) for i in pt])
    #print(stream)
    return stream

def solve(a, b):
    stream = create_stream(50000)
    return stream[a:a+b]

print(solve(10,5))

"""
Consider a sequence made up of the consecutive prime numbers. This infinite sequence would start with:

"2357111317192329313741434753596167717379..."
You will be given two numbers: a and b, and your task will be to return b elements starting from index a in this sequence.

For example:
solve(10,5) == `19232` Because these are 5 elements from index 10 in the sequence.
Tests go up to about index 20000.

More examples in test cases. Good luck!

Please also try Simple time difference

"""


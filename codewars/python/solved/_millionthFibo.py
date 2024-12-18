# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python
# The Millionth Fibonacci Kata
# https://www.reddit.com/r/Python/comments/mkpifc/how_i_calculated_the_1000000th_fibonacci_number/?rdt=40030

import numpy as np
import timeit

def fib(n):
    fb = [0,1,1,2,3,5,8,13,21]

    if n > 0:
        while len(fb) <= n:
            fb.append(fb[-1]+fb[-2])
        return fb[n]
    else:
        l = abs(n)
        while len(fb) <= l:
            fb.append(fb[-1]+fb[-2])
        return fb[l] if l%2 else fb[l]*-1
  
fbn = np.array([0,1,1,2,3,5,8,13,21])


def npfib(n):
    fbn = np.array([0,1,1,2,3,5,8,13,21],dtype=object)
    while len(fbn) <= n:
        fbn = np.append(fbn, fbn[-1]+fbn[-2])
    return fbn[n] 

def fibt():
    fib(1000)

def fibnp():
    fib(1000)

#print(timeit.Timer(fibt).timeit(number=100))
#print(timeit.Timer(fibnp).timeit(number=100))

from numpy import matrix
def npmatrix(n):
    return (matrix('0 1; 1 1',object) ** n)[0, 1]

def ownmatrix(n):
    a = matrix('0 1; 1 1',object)
    a = a**n
    return a[0,1]


print(fib(1000))
print(npfib(1000))
print(npmatrix(1000))
print(ownmatrix(1000))

#print(fib(1000))
#print(npfib(1000))





"""
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
[0, 1, -1, 2, -3, 5, -8, 13, -21, 34, -55]

It allows us to also step backwards from the initial terms, giving a well-defined bidirectional sequence

negative fibo     Fn = F(n+2)-F(n+1)

…, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, …

Surprised?
"""
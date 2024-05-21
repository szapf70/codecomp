# https://www.codewars.com/kata/578dec07deaed9b17d0001b8/train/python
# Goldbach’s Conjecture

import math

primes = [True] * 32001
needcalc = True

def goldbach_partitions(n):
    if needcalc:
        for p in range(2,32001):
            pc = True
            for t in range(2, int(math.sqrt(p)+1)):
                if p%t == 0: 
                    primes[p] = False
                    break

    #res = []
    #pidx = 



goldbach_partitions(2)
print(list(enumerate(primes[:20])))
# https://www.codewars.com/kata/578dec07deaed9b17d0001b8/train/python
# Goldbach’s Conjecture

import gmpy2

def goldbach_partitions(n):
    if n%2: return []
    res = []
    tpr = 2
    while tpr <= int(n//2):
        if gmpy2.is_prime(n-tpr):
            res.append(f"{tpr}+{n-tpr}")
        tpr = gmpy2.next_prime(tpr)
    return res    




print(goldbach_partitions(7))

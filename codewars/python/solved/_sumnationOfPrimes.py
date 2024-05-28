# https://www.codewars.com/kata/59ab0ca4243eae9fec000088/train/python
# Summation Of Primes

from gmpy2 import next_prime

memo = {}
pr = [2,3,5,7,11,13]

def summation_of_primes(primes):
    while pr[-1] < primes:
        pr.append(next_prime(pr[-1]))
    idx = 0
    sum = 0
    while pr[idx] <= primes:
        sum += pr[idx]
        idx += 1
    return sum

        
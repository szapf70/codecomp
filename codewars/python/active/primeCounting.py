# https://www.codewars.com/kata/638c92b10e43cc000e615a07/train/python
# Prime counting

from gmpy2 import next_prime
from functools import cache

prlkt = []


def count_primes_less_than(n:int) -> int:
    res = 0
    num = 0
    while True:
        num = next_prime(num)
        if num <= n:
            res += 1
        else:
            break
    return res


"""
You need to count the number of prime numbers less than or equal to some natural n.

For example:

count_primes_less_than(34) = 11
count_primes_less_than(69) = 19
count_primes_less_than(420) = 81
count_primes_less_than(666) = 121
In this kata all the tests will be with 
1
⩽
𝑛
⩽
1
0
10
1⩽n⩽10 
10
 
Code length limited to 3000 characters to avoid hardcoding.
Good luck!


"""
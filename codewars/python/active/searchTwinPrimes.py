# https://www.codewars.com/kata/596549c7743cf369b900021b/train/python
# The search for Primes! Twin Primes!

from functools import cache

@cache
def create_sieve(c):
    pt = [2,3]    
    is_prime = [False] * (c+1)
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
    for n in pt:
        is_prime[n] = True
    return is_prime


def twin_prime(n):
    if n < 4 : return 0
    is_prime = create_sieve(50)
    res = 0
    for i in range(4,n+1):
        if is_prime[i-1] and is_prime[i+1]:
            res += 1
    return res


print(twin_prime(12))


"""
A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example, either member of the twin prime pair 
(41, 43). In other words, a twin prime is a prime that has a prime gap of two. Sometimes the term twin prime is used for a pair of twin primes; 
an alternative name for this is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)

Your mission, should you choose to accept it, is to write a function that counts the number of sets of twin primes from 1 to n.

If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should also count even though n+1 is outside the range.

Ex n = 10

Twin Primes are (3,5) (5,7) so your function should return 2!



"""


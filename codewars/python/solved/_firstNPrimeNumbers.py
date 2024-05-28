# https://www.codewars.com/kata/535bfa2ccdbf509be8000113/train/python
# First n Prime Numbers

from gmpy2 import next_prime

class Primes:
    primes = [2,3,5,7,11,13,17,19]
    
    @staticmethod
    def first(n):
        while len(Primes.primes) < n:
            Primes.primes.append(int(next_prime(Primes.primes[-1])))
        return Primes.primes[:n]    
    
    
    
print(Primes.first(100)[99])    
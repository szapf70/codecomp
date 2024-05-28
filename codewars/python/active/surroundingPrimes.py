# https://www.codewars.com/kata/560b8d7106ede725dd0000e2/train/python
# Surrounding Primes for a value

import gmpy2

def prime_bef_aft(num):
    return [int(gmpy2.prev_prime(num)), int(gmpy2.next_prime(num))]
    
    
print(prime_bef_aft(100))    

#print(gmpy2.prev_prime(10))
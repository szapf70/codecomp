

from gmpy2 import next_prime

res = 0
p = 0
j = 0

while j < 1000:
    i = 0
    while i < 10_000_000:
        p = next_prime(p)
        res += 1
    print(j*10_000_000,res)

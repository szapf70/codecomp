# https://www.codewars.com/kata/55e7d9d63bdc3caa2500007d/train/python
# Satisfying numbers

import gmpy2



def smallest(n):
    res = 1
    pr = 1
    while pr <= n:
        if res % pr:
            res *= pr
        pr = gmpy2.next_prime(pr)
        print(res,pr)
    return res


print(smallest(4))
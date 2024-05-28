# https://www.codewars.com/kata/59f38b033640ce9fc700015b/train/python
# Sum of prime-indexed elements

from gmpy2 import next_prime

def total(arr):
    sum = 0
    i = 2
    while i < len(arr):
        sum += arr[i]
        i = next_prime(i)
    return sum


print(total([1,2,3,4,5,6]))
# https://www.codewars.com/kata/59fa8e2646d8433ee200003f/train/python
# Sorting by bits

from functools import cache

@cache
def btuple(n):
    return (bin(n)[2:].count('1'),n)

def sort_by_bit(arr): 
    return [n for v,n in sorted([btuple(n) for n in arr])]

print(sort_by_bit([3, 8, 3, 6, 5, 7, 9, 1]))


"""

Wrong: [3, 8, 3, 6, 5, 7, 9, 1] should equal [1, 8, 3, 3, 5, 6, 9, 7]

E.g Given the array [7, 6, 15, 8]

7 has 3 on bits (000...0111)
6 has 2 on bits (000...0110)
15 has 4 on bits (000...1111)
8 has 1 on bit (000...1000)
So the array in sorted order would be [8, 6, 7, 15].

In cases where two numbers have the same number of bits, compare their real values instead.
"""      


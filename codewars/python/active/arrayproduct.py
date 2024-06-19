# https://www.codewars.com/kata/5b3e609cd58499284100007a/train/python
# Array Product (Sans n)

from math import prod

def product_sans_n(nums):
    p = prod(nums)
    res = []
    for i in nums:
        res.append(p//i)
    return res    


import math

def sum_or_product(array, n):
    array = sorted(array)
    sum_ = sum(array[-n:])
    prod_ = math.prod(array[:n])
    if sum_ > prod_: return "sum"
    if prod_ > sum_: return "prod"
    return "same"



n = 3
array = [10, 41, 8, 16, 20, 36, 9, 13, 20]
print(sum_or_product(array, n))


"""

Description
For this Kata you will be given an array of numbers and another number n. You have to find the sum of the n largest numbers of the array and the product of the n smallest numbers of the array, and compare the two.

If the sum of the n largest numbers is higher, return "sum"
If the product of the n smallest numbers is higher, return "product"
If the 2 values are equal, return "same"

Note The array will never be empty and n will always be smaller than the length of the array.

Example
sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3) # => "product"

"""    
"""
# Python3 code to demonstrate working of
# Addition of tuples
# using map() + lambda
 
# initialize tuples 
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)
 
# printing original tuples 
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
 
# Addition of tuples
# using map() + lambda
res = tuple(map(lambda i, j: i + j, test_tup1, test_tup2))
 
# printing result
print("Resultant tuple after addition : " + str(res))
"""

a, b = 12, 43
temp = (a*2, b/2)[a<b]
print(temp)
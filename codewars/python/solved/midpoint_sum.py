# https://www.codewars.com/kata/54d3bb4dfc75996c1c000c6d/train/python
# Midpoint Sum

def midpoint_sum(ints):
    for i in range(len(ints)):
        if sum(ints[:i]) == sum(ints[i+1:]): return i
    return None
    

print(midpoint_sum([-10,3,7,8,-6,-13,21]))